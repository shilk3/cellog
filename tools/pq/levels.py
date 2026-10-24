# Power Query difficulty levels (my picks, for review): 1 Common (asked from
# League 4), 2 Everyday (League 3), 3 Rare — connectors, binary, types etc.
# (League 2). parsed.json -> levelled.json
import json
COMMON = set("""Table.SelectRows Table.AddColumn Table.RemoveColumns Table.SelectColumns Table.RenameColumns Table.TransformColumnTypes Table.Group
Table.NestedJoin Table.ExpandTableColumn Table.ExpandRecordColumn Table.UnpivotOtherColumns Table.Unpivot Table.Pivot Table.Sort Table.Distinct
Table.PromoteHeaders Table.DemoteHeaders Table.SplitColumn Table.ReplaceValue Table.FillDown Table.FillUp Table.Combine Table.FirstN Table.LastN
Table.Skip Table.RemoveRowsWithErrors Table.RemoveFirstN Table.RemoveLastN Table.Transpose Table.ReorderColumns Table.DuplicateColumn
Table.TransformColumns Table.AddIndexColumn Table.RowCount Table.ColumnNames Table.Column Table.ToRows Table.FromRows Table.FromRecords
Table.ReplaceErrorValues Table.SelectRowsWithErrors Table.Buffer Table.CombineColumns Table.Join Table.Range Table.Max Table.Min
Text.Combine Text.Split Text.Upper Text.Lower Text.Proper Text.Trim Text.Clean Text.Start Text.End Text.Middle Text.Range Text.Length
Text.Contains Text.StartsWith Text.EndsWith Text.Replace Text.Remove Text.Select Text.BeforeDelimiter Text.AfterDelimiter Text.BetweenDelimiters
Text.PadStart Text.PadEnd Text.From Text.PositionOf Text.Reverse Text.Format
List.Sum List.Max List.Min List.Average List.Count List.Distinct List.Sort List.Contains List.Dates List.Numbers List.First List.Last
List.Transform List.Select List.Combine List.Generate List.Accumulate List.Range List.FirstN List.LastN List.RemoveNulls List.Zip
Date.AddDays Date.AddMonths Date.AddYears Date.Year Date.Month Date.Day Date.DayOfWeek Date.DayOfWeekName Date.MonthName Date.StartOfMonth
Date.EndOfMonth Date.StartOfWeek Date.StartOfYear Date.EndOfYear Date.WeekOfYear Date.QuarterOfYear Date.From Date.ToText Date.FromText
DateTime.LocalNow DateTime.Date DateTime.Time DateTime.From DateTime.FixedLocalNow Duration.Days Duration.TotalDays
Number.Round Number.RoundUp Number.RoundDown Number.From Number.ToText Number.Mod Number.IntegerDivide Number.Abs Number.Power Number.Sqrt
Number.FromText Number.Random Number.RandomBetween
Excel.CurrentWorkbook Excel.Workbook Csv.Document Folder.Files Folder.Contents File.Contents Web.Contents Web.Page Json.Document Sql.Database
Splitter.SplitTextByDelimiter Splitter.SplitTextByPositions Combiner.CombineTextByDelimiter Replacer.ReplaceText Replacer.ReplaceValue
Record.Field Record.FieldNames Record.ToTable Value.Type Logical.From Logical.ToText""".split())
RARE_CATS = {"accessing-data", "binary", "comparer", "expression", "lines", "uri", "type", "value", "datetimezone", "logical"}
pq = json.load(open("parsed.json"))
for x in pq:
    x["level"] = 1 if x["name"] in COMMON else 3 if x["cat"] in RARE_CATS else 2
# A few functions are listed under two categories: keep the commoner listing.
best = {}
for x in pq:
    if x["name"] not in best or x["level"] < best[x["name"]]["level"]: best[x["name"]] = x
pq = [x for x in pq if best[x["name"]] is x]
json.dump(pq, open("levelled.json", "w"))
print(len(pq), "functions")
