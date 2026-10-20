# VBA: add the functions Microsoft keeps on other pages (Dir, FreeFile,
# InStrRev, IMEStatus, Tab; the type-conversion functions), fix two
# descriptions that picked up a note box, and mark the common ones (asked
# first). parsed.json -> levelled.json
import json
vba = json.load(open("parsed.json"))
extra = {
    "Dir": ("[ pathname, [ attributes ] ]", "Returns a String representing the name of a file, directory, or folder that matches a specified pattern or file attribute, or the volume label of a drive."),
    "FreeFile": ("[ rangenumber ]", "Returns an Integer representing the next file number available for use by the Open statement."),
    "InStrRev": ("stringcheck, stringmatch, [ start, [ compare ] ]", "Returns the position of an occurrence of one string within another, from the end of string."),
    "IMEStatus": ("", "Returns an Integer specifying the current Input Method Editor (IME) mode; available in East Asian versions only."),
    "Tab": ("[ n ]", "Used with the Print # statement or the Print method to position output."),
}
for k, (sx, d) in extra.items():
    vba.append({"name": k, "cat": "Other functions", "desc": d, "syntax": sx, "href": ""})
CONV = [("CBool", "Boolean"), ("CByte", "Byte"), ("CCur", "Currency"), ("CDate", "Date"), ("CDbl", "Double"), ("CDec", "Decimal"), ("CInt", "Integer"),
        ("CLng", "Long"), ("CLngLng", "LongLong"), ("CLngPtr", "LongPtr"), ("CSng", "Single"), ("CStr", "String"), ("CVar", "Variant")]
for fn, ret in CONV:
    vba.append({"name": fn, "cat": "Conversion functions", "desc": f"Converts an expression to the {ret} data type", "syntax": "expression", "href": ""})
fix = {"DatePart": "Returns a Variant (Integer) containing the specified part of a given date",
       "MacScript": "Executes an AppleScript script and returns its result (Mac only)"}
COMMON = set("""MsgBox InputBox Left Right Mid Len InStr InStrRev Replace Split Join Trim LTrim RTrim UCase LCase Format CStr CInt CLng CDbl CDate CBool Val
IsNumeric IsEmpty IsDate IsArray IsNull IsError IsObject UBound LBound Date Now Time DateAdd DateDiff DatePart DateSerial DateValue Year Month Day Weekday
Hour Minute Second Abs Int Fix Round Rnd Sqr IIf Choose Array Dir CreateObject Environ Timer StrConv Space String Chr Asc TypeName VarType Filter StrReverse""".split())
for v in vba:
    v["desc"] = fix.get(v["name"], v["desc"])
    v["level"] = 1 if v["name"] in COMMON else 2
json.dump(vba, open("levelled.json", "w"))
print(len(vba), "functions")
