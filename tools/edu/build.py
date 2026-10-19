# Builds edu-functions.js for the game from classified.json.
import json, re, sys

C = json.load(open("classified.json"))

# Shorter (phone-sized) or corrected descriptions.
DESC = {
    "ASC": "Changes full-width (double-byte) letters or katakana in text to half-width (single-byte)",
    "DBCS": "Changes half-width (single-byte) letters or katakana in text to full-width (double-byte)",
    "BINOM.INV": "Returns the smallest value whose cumulative binomial distribution reaches a criterion value",
    "CEILING.PRECISE": "Rounds a number up to the nearest integer or multiple of significance, whatever its sign",
    "FLOOR.PRECISE": "Rounds a number down to the nearest integer or multiple of significance, whatever its sign",
    "CELL": "Returns information about the formatting, location, or contents of a cell",
    "CONCAT": "Combines the text from multiple ranges and/or strings, with no delimiter",
    "COVARIANCE.S": "Returns the sample covariance: the average product of deviations for each pair of points",
    "CUBEKPIMEMBER": "Returns a key performance indicator (KPI) property and shows its name in the cell",
    "CUBEMEMBER": "Returns a member or tuple in a cube hierarchy, checking that it exists in the cube",
    "CUBEMEMBERPROPERTY": "Returns the value of a member property in the cube",
    "CUBERANKEDMEMBER": "Returns the nth, or ranked, member in a set — e.g. the top sales performer",
    "CUBESET": "Defines a calculated set of members or tuples by sending a set expression to the cube",
    "DATEDIF": "Calculates the number of days, months, or years between two dates — handy for ages",
    "DDB": "Returns an asset's depreciation for a period by the double-declining balance (or another) method",
    "EDATE": "Returns the serial number of the date a given number of months before or after a start date",
    "FILTERXML": "Returns specific data from XML content by using a given XPath",
    "FORECAST": "Returns a value along a linear trend (the older name for FORECAST.LINEAR)",
    "FORECAST.ETS": "Returns a future value from historical values using exponential smoothing (ETS)",
    "IFERROR": "Returns a value you choose if a formula gives an error; otherwise the formula's result",
    "IFNA": "Returns a value you choose if an expression gives #N/A; otherwise the expression's result",
    "IFS": "Checks one or more conditions and returns the value for the first TRUE one",
    "INFO": "Returns information about the current operating environment",
    "MAP": "Returns an array made by applying a LAMBDA to each value in the array(s)",
    "MIRR": "Returns the internal rate of return where positive and negative cash flows use different rates",
    "MODE.MULT": "Returns a vertical array of the most frequently occurring values in a range",
    "NETWORKDAYS.INTL": "Returns the number of whole workdays between two dates, with your choice of weekend days",
    "NPV": "Returns the net present value of an investment from periodic cash flows and a discount rate",
    "PERMUTATIONA": "Returns the number of permutations (with repetitions) for a number of objects",
    "RANDARRAY": "Returns an array of random numbers — you can set rows, columns, min, max and whole numbers",
    "REDUCE": "Reduces an array to one accumulated value by applying a LAMBDA to each value",
    "SKEW.P": "Returns the skewness of a distribution based on a population",
    "SWITCH": "Compares an expression against a list of values and returns the result for the first match",
    "T.INV": "Returns the left-tailed inverse of the Student's t-distribution",
    "TRIMRANGE": "Trims blank rows and columns from the outer edges of a range or array",
    "VDB": "Returns an asset's depreciation for a specified or partial period by a declining balance method",
    "WORKDAY.INTL": "Returns the date a number of workdays before or after a date, with your choice of weekend days",
    "XLOOKUP": "Searches a range or array and returns the item for the first match (or the closest match)",
}
for k in DESC: assert any(c["name"] == k for c in C), k

def tidy(s):
    s = re.sub(r"\s*This function is not available in Excel for the web\.?", "", s)
    return s.strip().rstrip(".")

def spec(args):
    return "|".join("..." if a["n"] == "..." else ("[" + a["n"] + "]" if a["opt"] else a["n"]) for a in args)

SKILLS = ["data", "map", "text", "games", "math", "time", "cards"]
rows = []
for c in sorted(C, key=lambda c: c["name"]):
    d = DESC.get(c["name"]) or tidy(c["desc"])
    assert len(d) <= 110, (c["name"], len(d), d)
    rows.append([c["name"], c["skill"], c["titan"], c["tier"], d, spec(c["args"]), c["cat"]])

js = """// Excel's functions for 📘 Education mode — built by tools/build_edu.py
// from Microsoft's function reference (support.microsoft.com, Excel
// functions alphabetical + each function's syntax page). Argument names are
// exactly as Excel shows them; descriptions are Microsoft's, some shortened
// to fit a phone. Compatibility versions and add-in functions are left out.
// Each row: [name, skill, Titan skill, league tier (5 easiest … 0 Titan),
//            description, arguments ("[x]" optional, "..." repeats),
//            Microsoft's category].
const EDU_FUNCS = [
""" + "".join("  " + json.dumps(r, ensure_ascii=False) + ",\n" for r in rows) + "];\n"
pandas = json.load(open("pandas.json"))
js += """// The 🐍 Python Invitational's set: Python in Excel's PY() and xl(), and the
// pandas commands most used with it — their main arguments (pandas 2), in
// order. Each row: [name, description, arguments].
const EDU_PANDAS = [
""" + "".join("  " + json.dumps(r, ensure_ascii=False) + ",\n" for r in pandas) + "];\n"
open(sys.argv[1] if len(sys.argv) > 1 else "edu-functions.js", "w").write(js)
print(len(rows), "functions,", len(js), "bytes")
