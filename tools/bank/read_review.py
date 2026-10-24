# Reads a filled-in review spreadsheet (from make_review.py) and writes
# tools/bank/sets.json: for each bank, the items marked "Keep? = No". Those
# aren't dropped: they're the completionist extras, while everything else is
# the default (esports) set. Comments and moves are listed for follow-up.
# Usage (from the repo root): python3 tools/bank/read_review.py review.xlsx
import json, sys
import openpyxl
# Removed outright (per the review): the Easter egg, and Excel's own LAMBDA
# functions, which are already in the Excel bank.
REMOVED = {"cmds": ["Eggy"], "lams": ["LAMBDA", "LET", "MAP", "REDUCE", "SCAN", "BYROW", "BYCOL", "MAKEARRAY", "ISOMITTED"]}
# Moves agreed after the review, applied on top of it (to_extra: Esports →
# Completionist; to_core: the other way).
ADJUST = {
    "excel": {
        "to_extra": "ASC DBCS JIS PHONETIC BAHTTEXT SINH COSH TANH ASINH ACOSH ATANH SEC SECH CSC CSCH COT COTH ACOT ACOTH "
                    "ERF ERF.PRECISE ERFC ERFC.PRECISE DELTA GESTEP SERIESSUM SQRTPI SUMX2MY2 SUMX2PY2 SUMXMY2 "
                    "LOGNORM.INV PHI HARMEAN STDEVPA VARPA".split(),
        "to_core": "MODE.SNGL PERCENTILE.INC QUARTILE.INC CORREL RANK.AVG FORECAST.LINEAR INTERCEPT".split(),
    },
    "pq": {
        "to_extra": "DateTimeZone.FixedLocalNow DateTimeZone.FixedUtcNow DateTimeZone.From DateTimeZone.FromFileTime "
                    "DateTimeZone.FromText DateTimeZone.LocalNow DateTimeZone.RemoveZone DateTimeZone.SwitchZone "
                    "DateTimeZone.ToLocal DateTimeZone.ToRecord DateTimeZone.ToText DateTimeZone.ToUtc DateTimeZone.UtcNow "
                    "DateTimeZone.ZoneHours DateTimeZone.ZoneMinutes #datetimezone "
                    "Access.Database Odbc.DataSource Odbc.InferOptions Odbc.Query OleDb.DataSource OleDb.Query "
                    "SharePoint.Contents SharePoint.Files SharePoint.Tables OData.Feed WebAction.Request Identity.IsMemberOf "
                    # Type / Value / Comparer internals, operators and connector-builder tools.
                    "Value.Add Value.Subtract Value.Multiply Value.Divide Value.Equals Value.Compare Value.NullableEquals Value.As "
                    "Value.Metadata Value.RemoveMetadata Value.ReplaceMetadata Value.Expression Value.Alternates Value.Optimize "
                    "Value.NativeQuery Value.Versions Value.VersionIdentity Embedded.Value Variable.Value Variable.ValueOrDefault "
                    "Comparer.Equals Comparer.FromCulture Type.ForFunction Type.FunctionParameters Type.FunctionRequiredParameters "
                    "Type.FunctionReturn Type.ForRecord Type.RecordFields Type.OpenRecord Type.ClosedRecord Type.IsOpenRecord "
                    "Type.AddTableKey Type.TableKeys Type.ReplaceTableKeys Type.TablePartitionKey Type.ReplaceTablePartitionKey "
                    "Type.Facets Type.ReplaceFacets Type.ListItem Type.TableRow Type.Union".split(),
    },
}
TABS = {"Excel": "excel", "Power Query": "pq", "VBA": "vba", "Robot commands": "cmds", "Lambdas": "lams", "Python": "py"}
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
out = {"extra": {}, "removed": REMOVED, "notes": {}}
for tab, key in TABS.items():
    rows = wb[tab].iter_rows(values_only=True)
    hdr = list(next(rows))
    keep = hdr.index("Keep?")
    note = next(i for i, h in enumerate(hdr) if h and h.startswith("Comments"))
    move = next((i for i, h in enumerate(hdr) if h and h.startswith("Change")), None)
    extra, kept, out["notes"][key] = [], set(), []
    for r in rows:
        if not r[0] or r[0] in REMOVED.get(key, []): continue
        if r[keep] == "No": extra.append(r[0])
        else: kept.add(r[0])
        if r[note] or (move is not None and r[move]):
            out["notes"][key].append({"name": r[0], "move": r[move] if move is not None else None, "note": r[note]})
    # A name listed twice (Power Query files a couple under two categories)
    # is kept if either listing was.
    out["extra"][key] = sorted(set(extra) - kept, key=extra.index)
    adj = ADJUST.get(key, {})
    out["extra"][key] = [n for n in out["extra"][key] if n not in adj.get("to_core", [])] + [n for n in adj.get("to_extra", []) if n not in out["extra"][key]]
json.dump(out, open("tools/bank/sets.json", "w"), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in out["extra"].items()})
