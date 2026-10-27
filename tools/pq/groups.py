# Power Query functions grouped by purpose, for 📘 Knowledge mode: a check
# on a group asks "Which one …?" for each member (its look-alikes as the
# wrong answers). The group is what's mastered and counted; each function's
# own record is kept in the background. Every function is in exactly one
# group, except the 17 Microsoft marks "for internal use only" (no fair
# question can be asked), which are left out of the game. Members are written without the namespace when it's the group's
# `ns` (or with a full name, containing a dot).
G = []
def g(name, ns, members):
    G.append((name, [m if "." in m or m.startswith("#") else f"{ns}.{m}" for m in members.split()]))

# ---- Dates ----
g("Date: add time", "Date", "AddDays AddWeeks AddMonths AddQuarters AddYears")
g("Date: start of a period", "Date", "StartOfDay StartOfWeek StartOfMonth StartOfQuarter StartOfYear")
g("Date: end of a period", "Date", "EndOfDay EndOfWeek EndOfMonth EndOfQuarter EndOfYear")
g("Date: parts", "Date", "Day Month Year QuarterOfYear DayOfYear")
g("Date: weeks, names and lengths", "Date", "DayOfWeek DayOfWeekName MonthName WeekOfMonth WeekOfYear DaysInMonth IsLeapYear")
g("Date: in the current period", "Date", "IsInCurrentDay IsInCurrentWeek IsInCurrentMonth IsInCurrentQuarter IsInCurrentYear IsInYearToDate")
g("Date: in the next period", "Date", "IsInNextDay IsInNextWeek IsInNextMonth IsInNextQuarter IsInNextYear")
g("Date: in the previous period", "Date", "IsInPreviousDay IsInPreviousWeek IsInPreviousMonth IsInPreviousQuarter IsInPreviousYear")
g("Date: in the next N periods", "Date", "IsInNextNDays IsInNextNWeeks IsInNextNMonths IsInNextNQuarters IsInNextNYears")
g("Date: in the previous N periods", "Date", "IsInPreviousNDays IsInPreviousNWeeks IsInPreviousNMonths IsInPreviousNQuarters IsInPreviousNYears")
g("Date: converting", "Date", "From FromText ToText ToRecord")
# ---- Times and date-times ----
g("Time: converting", "Time", "From FromText ToText ToRecord")
g("Time: parts", "Time", "Hour Minute Second StartOfHour EndOfHour")
g("DateTime: converting", "DateTime", "From FromText ToText ToRecord FromFileTime AddZone")
g("DateTime: now and its parts", "DateTime", "LocalNow FixedLocalNow Date Time")
g("DateTime: this hour, minute or second", "DateTime", "IsInCurrentHour IsInCurrentMinute IsInCurrentSecond")
g("DateTime: the next hour, minute or second (or N)", "DateTime", "IsInNextHour IsInNextMinute IsInNextSecond IsInNextNHours IsInNextNMinutes IsInNextNSeconds")
g("DateTime: the last hour, minute or second (or N)", "DateTime", "IsInPreviousHour IsInPreviousMinute IsInPreviousSecond IsInPreviousNHours IsInPreviousNMinutes IsInPreviousNSeconds")
g("DateTimeZone: now", "DateTimeZone", "FixedLocalNow FixedUtcNow LocalNow UtcNow")
g("DateTimeZone: converting", "DateTimeZone", "From FromFileTime FromText ToText ToRecord #datetimezone")
g("DateTimeZone: zones", "DateTimeZone", "RemoveZone SwitchZone ToLocal ToUtc ZoneHours ZoneMinutes")
g("Duration: parts", "Duration", "Days Hours Minutes Seconds")
g("Duration: totals", "Duration", "TotalDays TotalHours TotalMinutes TotalSeconds")
g("Duration: converting", "Duration", "From FromText ToText ToRecord")
g("Literals (#)", "#", "#date #datetime #duration #time #table")
# ---- Numbers ----
g("Number: rounding", "Number", "Round RoundUp RoundDown RoundAwayFromZero RoundTowardZero")
g("Number: arithmetic", "Number", "Abs Sign Mod IntegerDivide Power Sqrt")
g("Number: exponents, logs and checks", "Number", "Exp Ln Log Log10 IsEven IsOdd IsNaN")
g("Number: trigonometry", "Number", "Sin Cos Tan Asin Acos Atan Atan2")
g("Number: hyperbolic and counting", "Number", "Sinh Cosh Tanh Factorial Combinations Permutations")
g("Random numbers", "Number", "Random RandomBetween List.Random")
g("Number: bitwise", "Number", "BitwiseAnd BitwiseNot BitwiseOr BitwiseXor BitwiseShiftLeft BitwiseShiftRight")
g("Number: converting", "Number", "From FromText ToText Currency.From Percentage.From")
g("Number types", "Number", "Decimal.From Double.From Single.From")
g("Integer and byte types", "Int64", "Int8.From Int16.From Int32.From From Byte.From")
g("Logical values, characters and GUIDs", "Logical", "From FromText ToText Character.FromNumber Character.ToNumber Guid.From Text.NewGuid")
# ---- Text ----
g("Text: by position", "Text", "Start End Middle Range At")
g("Text: picking parts out", "Text", "AfterDelimiter BeforeDelimiter BetweenDelimiters Select Remove")
g("Text: case and cleaning", "Text", "Upper Lower Proper Trim TrimStart TrimEnd Clean")
g("Text: searching", "Text", "Contains StartsWith EndsWith PositionOf PositionOfAny")
g("Text: changing", "Text", "Insert Replace ReplaceRange RemoveRange Repeat Reverse")
g("Text: joining, splitting and padding", "Text", "Combine Split SplitAny ToList Length PadStart PadEnd")
g("Text: converting", "Text", "From FromBinary ToBinary InferNumberType")
g("Combiners", "Combiner", "CombineTextByDelimiter CombineTextByEachDelimiter CombineTextByLengths CombineTextByPositions CombineTextByRanges")
g("Splitters: by delimiter", "Splitter", "SplitByNothing SplitTextByAnyDelimiter SplitTextByDelimiter SplitTextByEachDelimiter SplitTextByWhitespace")
g("Splitters: by position", "Splitter", "SplitTextByCharacterTransition SplitTextByLengths SplitTextByPositions SplitTextByRanges SplitTextByRepeatedLengths")
g("Replacers and comparers", "Replacer", "ReplaceText ReplaceValue Comparer.Ordinal Comparer.OrdinalIgnoreCase")
# ---- Lists ----
g("List: totals and counts", "List", "Sum Product Count Average")
g("List: highest, lowest and middle", "List", "Max Min Median Mode")
g("List: statistics", "List", "StandardDeviation Covariance Percentile Modes NonNullCount MaxN MinN")
g("List: first and last", "List", "First FirstN Last LastN Skip Single SingleOrDefault")
g("List: removing items", "List", "RemoveFirstN RemoveLastN RemoveItems RemoveMatchingItems RemoveNulls RemoveRange")
g("List: replacing and inserting", "List", "ReplaceValue ReplaceMatchingItems ReplaceRange InsertRange Reverse Repeat")
g("List: what it contains", "List", "Contains ContainsAll ContainsAny IsEmpty IsDistinct")
g("List: true for all or any", "List", "AllTrue AnyTrue MatchesAll MatchesAny")
g("List: finding items", "List", "PositionOf PositionOfAny Positions FindText Select Alternate Range")
g("List: combining and comparing", "List", "Union Intersect Difference Distinct Combine Zip")
g("List: sequences", "List", "Numbers Dates DateTimes DateTimeZones Durations Times")
g("List: looping", "List", "Generate Accumulate Transform TransformMany")
g("List: sorting, splitting and buffering", "List", "Sort Split Buffer")
# ---- Records ----
g("Record: reading fields", "Record", "Field FieldOrDefault FieldNames FieldValues FieldCount HasFields")
g("Record: changing fields", "Record", "AddField RemoveFields RenameFields ReorderFields SelectFields TransformFields Combine")
g("Record: converting", "Record", "FromList FromTable ToList ToTable")
# ---- Tables ----
g("Table: removing rows", "Table", "RemoveFirstN RemoveLastN RemoveRows RemoveMatchingRows RemoveRowsWithErrors Skip Distinct")
g("Table: picking rows", "Table", "First FirstN Last LastN Range SingleRow FirstValue")
g("Table: filtering rows", "Table", "SelectRows SelectRowsWithErrors AlternateRows FindText MatchesAllRows MatchesAnyRows")
g("Table: searching rows", "Table", "Contains ContainsAll ContainsAny PositionOf PositionOfAny IsDistinct")
g("Table: inserting and replacing rows", "Table", "InsertRows ReplaceRows ReplaceMatchingRows Repeat")
g("Table: choosing columns", "Table", "SelectColumns RemoveColumns ReorderColumns RenameColumns DuplicateColumn PrefixColumns")
g("Table: about its columns", "Table", "ColumnNames ColumnCount ColumnsOfType HasColumns Column")
g("Table: about its rows", "Table", "RowCount ApproximateRowCount IsEmpty")
g("Table: adding columns", "Table", "AddColumn AddIndexColumn AddRankColumn AddJoinColumn AddFuzzyClusterColumn")
g("Table: transforming", "Table", "TransformColumns TransformColumnTypes TransformColumnNames TransformRows ReplaceValue ReplaceErrorValues")
g("Table: headers and reshaping", "Table", "PromoteHeaders DemoteHeaders Transpose Pivot Unpivot UnpivotOtherColumns")
g("Table: filling, splitting and merging columns", "Table", "FillDown FillUp SplitColumn CombineColumns CombineColumnsToRecord")
g("Table: joining and appending", "Table", "Join NestedJoin FuzzyJoin FuzzyNestedJoin Combine")
g("Table: expanding", "Table", "ExpandTableColumn ExpandListColumn ExpandRecordColumn AggregateTableColumn")
g("Table: grouping and sorting", "Table", "Group FuzzyGroup Sort ReverseRows")
g("Table: largest and smallest", "Table", "Max Min MaxN MinN")
g("Table: building", "Table", "FromColumns FromList FromRecords FromRows FromValue FromPartitions")
g("Table: converting and splitting", "Table", "ToColumns ToList ToRecords ToRows Split SplitAt")
g("Table: keys and relationships", "Table", "AddKey Keys ReplaceKeys Tables.GetRelationships")
g("Table: partitions", "Table", "Partition PartitionKey PartitionValues ReplacePartitionKey")
g("Table: buffering and profiling", "Table", "Buffer StopFolding Profile Schema")
g("Table views (advanced)", "Table", "View ViewError ViewFunction")
g("Binary views (advanced)", "Binary", "Binary.View Binary.ViewError Binary.ViewFunction")
# ---- Types, values and expressions ----
g("Types", "Type", "Is IsNullable NonNullable TableColumn TableSchema")
g("Values: types and text", "Value", "Type ReplaceType Is FromText")
g("Values: arithmetic", "Value", "Add Subtract Multiply Divide As")
g("Values: comparing", "Value", "Equals NullableEquals Compare Comparer.Equals Comparer.FromCulture")
g("Values: metadata", "Value", "Metadata RemoveMetadata ReplaceMetadata")
g("Values: internals", "Value", "Expression Alternates Optimize NativeQuery VersionIdentity Versions Module.Versions RData.FromBinary")
g("Types: functions", "Type", "ForFunction FunctionParameters FunctionRequiredParameters FunctionReturn")
g("Types: records", "Type", "ForRecord RecordFields OpenRecord ClosedRecord IsOpenRecord")
g("Types: tables", "Type", "AddTableKey TableKeys ReplaceTableKeys TablePartitionKey ReplaceTablePartitionKey TableRow")
g("Types: facets and more", "Type", "Facets ReplaceFacets ListItem Union")
g("Item and row expressions", "RowExpression", "Column From ItemExpression.From")
g("Expressions and variables", "Expression", "Constant Evaluate Identifier Variable.Value Variable.ValueOrDefault Embedded.Value")
g("Geography and geometry", "Geography", "FromWellKnownText ToWellKnownText Geometry.FromWellKnownText Geometry.ToWellKnownText GeographyPoint.From GeometryPoint.From")
# ---- Getting data ----
g("Reading files and workbooks", "File", "Contents Folder.Contents Folder.Files Excel.Workbook Excel.CurrentWorkbook Pdf.Tables")
g("Reading text formats", "Csv", "Document Json.Document Json.FromValue Lines.FromText Lines.ToText")
g("XML and binary lines", "Xml", "Document Tables Lines.FromBinary Lines.ToBinary #binary")
g("Web", "Web", "Contents Page BrowserContents Headers Html.Table")
g("Web requests, feeds and URIs", "Uri", "BuildQueryString Combine EscapeDataString Parts WebAction.Request OData.Feed Soda.Feed")
g("Binary: converting", "Binary", "From FromList FromText ToList ToText InferContentType")
g("Binary: handling", "Binary", "Combine Split Range Length ApproximateLength Buffer Compress Decompress")
g("BinaryFormat: integers", "BinaryFormat", "7BitEncodedSignedInteger 7BitEncodedUnsignedInteger SignedInteger16 SignedInteger32 SignedInteger64 UnsignedInteger16 UnsignedInteger32 UnsignedInteger64")
g("BinaryFormat: other values", "BinaryFormat", "Byte Single Double Decimal Text Binary Null")
g("BinaryFormat: structure", "BinaryFormat", "ByteOrder Choice Group Length List Record Transform")
g("Databases (1)", "Access", "Database DB2.Database Informix.Database MySQL.Database Oracle.Database PostgreSQL.Database")
g("Databases (2)", "Sql", "Database Databases SapHana.Database Sybase.Database Teradata.Database")
g("ODBC, OLE DB and ADO.NET", "Odbc", "DataSource Query InferOptions OleDb.DataSource OleDb.Query AdoDotNet.DataSource AdoDotNet.Query")
g("Cloud storage", "AzureStorage", "BlobContents Blobs DataLake DataLakeContents Tables DeltaLake.Metadata DeltaLake.Table Cdm.Contents")
g("Big data and SharePoint", "Hdfs", "Contents Files HdInsight.Containers HdInsight.Contents HdInsight.Files SharePoint.Contents SharePoint.Files SharePoint.Tables")
g("Cubes and analytics sources", "AnalysisServices", "Database Databases Essbase.Cubes SapBusinessWarehouse.Cubes AdobeAnalytics.Cubes GoogleAnalytics.Accounts Salesforce.Data Salesforce.Reports")
g("Cube: building", "Cube", "AddAndExpandDimensionColumn AddMeasureColumn ApplyParameter CollapseAndRemoveColumns ReplaceDimensions Transform Dimensions Measures")
g("Cube: properties", "Cube", "AttributeMemberId AttributeMemberProperty DisplayFolders MeasureProperties MeasureProperty Parameters Properties PropertyKey")
g("Identity and services", "Identity", "From IsMemberOf IdentityProvider.Default AccessControlEntry.ConditionToIdentities ActiveDirectory.Domains Exchange.Contents FabricAI.Prompt")

# Hand-written questions where Microsoft's description doesn't make one
# (twins with the same wording, or a description that isn't a sentence).
CLUE = {
    "DateTime.LocalNow": "Which one returns the current local date and time, read afresh each time it's called?",
    "DateTime.FixedLocalNow": "Which one returns the current local date and time, fixed for the whole query run?",
    "RowExpression.From": "Which one returns the syntax tree of a function's body as a row expression?",
    "ItemExpression.From": "Which one returns the syntax tree of a function's body as an item expression?",
    "Replacer.ReplaceText": "Which one, passed to List.ReplaceValue or Table.ReplaceValue, replaces text inside values?",
    "Replacer.ReplaceValue": "Which one, passed to List.ReplaceValue or Table.ReplaceValue, replaces whole values?",
    "Table.ExpandListColumn": "Which one copies a row once for each item in a column of lists?",
    "Table.Pivot": "Which one turns an attribute column's values into new columns, filled from a value column?",
    "HdInsight.Containers": "Which one lists the containers in an HDInsight storage account?",
    "HdInsight.Contents": "Which one returns a navigation table of an HDInsight storage account's contents?",
}
INTERNAL = "This function is intended for internal use only"

def clue(name, desc):
    """The 'Which one …?' question for a function."""
    if name in CLUE: return CLUE[name]
    d = desc.strip().rstrip(".")
    first = d.split()[0] if d else ""
    if first == "Whether": return "Which one checks w" + d[1:] + "?"
    if first in ("This", "A", "An", "The", "Given"): return f"Which one is this: “{d}”?"
    return "Which one " + d[0].lower() + d[1:] + "?"

# Each group's two family questions: what do these do? and what do they
# take? (wrong answers: other groups' lines, nearest first).
TEXT = {
    "Date: add time": ("Add days, weeks, months, quarters or years to a date", "A date, then how many to add"),
    "Date: start of a period": ("Move a date back to the start of its day, week, month, quarter or year", "Just a date (week: optionally the first day of the week)"),
    "Date: end of a period": ("Move a date forward to the end of its day, week, month, quarter or year", "Just a date (week: optionally the first day of the week)"),
    "Date: parts": ("Pull the day, month, year, quarter or day of the year out of a date", "Just a date"),
    "Date: weeks, names and lengths": ("Day of the week, day and month names, week numbers, days in the month and leap years", "A date, sometimes with the first day of the week or a culture"),
    "Date: in the current period": ("Check whether a date is in the current day, week, month, quarter or year (or year to date)", "Just a date"),
    "Date: in the next period": ("Check whether a date is in the next day, week, month, quarter or year", "Just a date"),
    "Date: in the previous period": ("Check whether a date is in the previous day, week, month, quarter or year", "Just a date"),
    "Date: in the next N periods": ("Check whether a date is within the next N days, weeks, months, quarters or years", "A date, then how many periods"),
    "Date: in the previous N periods": ("Check whether a date is within the previous N days, weeks, months, quarters or years", "A date, then how many periods"),
    "Date: converting": ("Turn values or text into dates, and dates into text or a record", "A value or text, with optional culture or format options"),
    "Time: converting": ("Turn values or text into times, and times into text or a record", "A value or text, with optional culture or format options"),
    "Time: parts": ("Pull the hour, minute or second out of a time, or move it to the start or end of its hour", "Just a time or date-time"),
    "DateTime: converting": ("Turn values, text or file times into date-times, add a time zone, or turn them into text or a record", "A value, text or date-time, with optional format options"),
    "DateTime: now and its parts": ("Get the current date-time, or split a date-time into its date and its time", "Nothing, or a date-time"),
    "DateTime: this hour, minute or second": ("Check whether a date-time is in the current hour, minute or second", "Just a date-time"),
    "DateTime: the next hour, minute or second (or N)": ("Check whether a date-time is in the next hour, minute or second, or the next N of them", "A date-time (the N versions: then how many)"),
    "DateTime: the last hour, minute or second (or N)": ("Check whether a date-time is in the previous hour, minute or second, or the previous N of them", "A date-time (the N versions: then how many)"),
    "DateTimeZone: now": ("Get the current date-time with its time zone, local or UTC, fixed or live", "Nothing"),
    "DateTimeZone: converting": ("Turn values or text into date-times with a time zone, and back into text or a record", "A value or text, with optional format options"),
    "DateTimeZone: zones": ("Remove, switch or read a date-time's time zone, or convert it to local time or UTC", "A date-time with a zone (switching: then the new offset)"),
    "Duration: parts": ("Pull the days, hours, minutes or seconds part out of a duration", "Just a duration"),
    "Duration: totals": ("Express a whole duration in days, hours, minutes or seconds", "Just a duration"),
    "Duration: converting": ("Turn values or text into durations, and durations into text or a record", "A value, text or duration"),
    "Literals (#)": ("Write a date, date-time, time, duration or table straight into M code", "Its parts in order, like year, month, day"),
    "Number: rounding": ("Round a number to nearest, up, down, away from zero or towards zero", "A number, then optionally how many digits"),
    "Number: arithmetic": ("Absolute value, sign, remainder, whole-number division, powers and square roots", "One number, or a number and a divisor or power"),
    "Number: exponents, logs and checks": ("e to a power, logarithms, and checking whether a number is even, odd or not a number", "Just a number (Log: optionally a base)"),
    "Number: trigonometry": ("Sine, cosine, tangent and their inverses", "An angle or ratio (Atan2: y, then x)"),
    "Number: hyperbolic and counting": ("Hyperbolic sine, cosine and tangent, factorials, combinations and permutations", "A number, or a set size and how many to pick"),
    "Random numbers": ("Random numbers, between limits or as a list", "Nothing, two limits, or a count"),
    "Number: bitwise": ("Bit-level AND, OR, XOR, NOT and shifts on whole numbers", "Two numbers (NOT: one)"),
    "Number: converting": ("Turn values or text into numbers, currency or percentages, and numbers into text", "A value or text, with an optional culture or format"),
    "Number types": ("Turn a value into a decimal, double or single-precision number", "A value, then an optional culture"),
    "Integer and byte types": ("Turn a value into an 8, 16, 32 or 64-bit integer or a byte", "A value, then an optional culture and rounding mode"),
    "Logical values, characters and GUIDs": ("Turn values into true/false, characters into codes and back, and make GUIDs", "One value, number or character (NewGuid: nothing)"),
    "Text: by position": ("Take characters from the start, end or middle of text, or the one at a position", "Text, then a position and/or a count"),
    "Text: picking parts out": ("Take the text before, after or between delimiters, or keep or remove certain characters", "Text, then the delimiter(s) or characters"),
    "Text: case and cleaning": ("Change text to upper, lower or proper case, trim spaces or remove non-printing characters", "Just text (optionally a culture or what to trim)"),
    "Text: searching": ("Check whether text contains, starts or ends with something, or find where it is", "Text, then what to look for"),
    "Text: changing": ("Insert, replace, remove, repeat or reverse parts of text", "Text, then where and what to change"),
    "Text: joining, splitting and padding": ("Join texts, split text into a list, measure it or pad it out", "Text (or a list of texts), then a separator or length"),
    "Text: converting": ("Turn values or binary into text, text into binary, or work out a number type from text", "A value, text or binary, with optional culture or encoding"),
    "Combiners": ("Make the function that merges several columns' text into one (by delimiter, lengths or positions)", "The delimiter(s), lengths, positions or ranges to use"),
    "Splitters: by delimiter": ("Make the function that splits text at delimiters or whitespace", "The delimiter(s), with an optional quote style"),
    "Splitters: by position": ("Make the function that splits text by lengths, positions, ranges or character changes", "The lengths, positions or ranges (or the before/after test)"),
    "Replacers and comparers": ("Helpers that tell ReplaceValue how to replace, and comparisons how to compare (with or without case)", "Old and new values, or the two things to compare"),
    "List: totals and counts": ("Add up, multiply, count or average a list", "Just a list (optionally a precision)"),
    "List: highest, lowest and middle": ("The largest, smallest, median or most common item of a list", "A list, then optionally a default or how to compare"),
    "List: statistics": ("Standard deviation, covariance, percentiles, every mode, non-null count, or the top or bottom N", "A list, sometimes with a second list, percentiles or a count"),
    "List: first and last": ("Take the first or last item(s), skip some, or get the only item", "A list, then optionally a count or condition"),
    "List: removing items": ("Remove the first or last items, given items, matching items, nulls or a range", "A list, then what or how many to remove"),
    "List: replacing and inserting": ("Replace values, items or a range, insert items, or reverse or repeat a list", "A list, then a position or old and new values"),
    "List: what it contains": ("Check whether a list contains a value, all or any of some values, is empty or has no duplicates", "A list, then the value(s) to look for"),
    "List: true for all or any": ("Check whether all or any items are true, or meet a condition", "A list (Matches: then a condition)"),
    "List: finding items": ("Find where values are, find text, pick items by a condition, or take every nth or a range", "A list, then a value, text, condition or position"),
    "List: combining and comparing": ("Union, intersect, difference, distinct, join lists end to end, or zip them together", "A list of lists (or two lists)"),
    "List: sequences": ("Make a list of numbers, dates, times or durations from a start, a count and a step", "A start, a count and a step"),
    "List: looping": ("Build a list by looping, carry a running result, or transform each item", "A list (or a start value) and the function(s) to apply"),
    "List: sorting, splitting and buffering": ("Sort a list, split it into pages, or hold it in memory", "A list, then optionally how to sort or a page size"),
    "Record: reading fields": ("Get a field's value (or a default), the field names or values, how many, or whether fields exist", "A record, then optionally a field name"),
    "Record: changing fields": ("Add, remove, rename, reorder, select or transform fields, or combine records", "A record, then the fields and what to do with them"),
    "Record: converting": ("Turn lists or tables into records, and records into lists or tables", "A list (with field names), a table or a record"),
    "Table: removing rows": ("Remove the first or last rows, given rows, matching rows, rows with errors, or duplicates", "A table, then how many or which rows"),
    "Table: picking rows": ("Take the first or last row(s), a range of rows, the only row, or the first value", "A table, then optionally a count or offset"),
    "Table: filtering rows": ("Keep rows that meet a condition, have errors, alternate or contain text; test all or any rows", "A table, then a condition, text or pattern"),
    "Table: searching rows": ("Check whether a table contains rows, find where they are, or check its rows are distinct", "A table, then the row(s) to look for"),
    "Table: inserting and replacing rows": ("Insert, replace or repeat rows", "A table, then where, and the new rows"),
    "Table: choosing columns": ("Keep, remove, reorder, rename, duplicate or prefix columns", "A table, then the column(s)"),
    "Table: about its columns": ("Column names and count, columns of a type, whether columns exist, or one column's values", "A table, sometimes then a column or types"),
    "Table: about its rows": ("Count a table's rows (exactly or roughly), or check whether it's empty", "Just a table"),
    "Table: adding columns": ("Add a calculated, index, rank, joined or fuzzy-cluster column", "A table, a new column name, then how to fill it"),
    "Table: transforming": ("Change column values, types or names, transform each row, or replace values or errors", "A table, then the changes to make"),
    "Table: headers and reshaping": ("Promote or demote headers, transpose, pivot or unpivot", "A table, then the columns involved (if any)"),
    "Table: filling, splitting and merging columns": ("Fill blanks down or up, split a column, or merge columns", "A table, then the column(s) and a splitter or combiner"),
    "Table: joining and appending": ("Join two tables (exactly or fuzzily, flat or nested) or append tables", "Two tables and their key columns (appending: a list of tables)"),
    "Table: expanding": ("Expand a column of tables, lists or records into columns or rows, or aggregate nested tables", "A table, the column, then the fields to bring out"),
    "Table: grouping and sorting": ("Group rows (exactly or fuzzily), sort rows, or reverse their order", "A table, then the keys or sort order"),
    "Table: largest and smallest": ("Find the row(s) with the largest or smallest value", "A table, how to compare, then optionally a count"),
    "Table: building": ("Make a table from columns, a list, records, rows, a value or partitions", "The lists, records or rows to build it from"),
    "Table: converting and splitting": ("Turn a table into columns, a list, records or rows, or split it into smaller tables", "A table (splitting: then a size)"),
    "Table: keys and relationships": ("Add, read or replace a table's keys, or find relationships between tables", "A table, then the key columns"),
    "Table: partitions": ("Partition a table, read or replace its partition key, or list its partition values", "A table, then partition details"),
    "Table: buffering and profiling": ("Hold a table in memory, stop query folding, profile its columns, or describe its schema", "Just a table"),
    "Table views (advanced)": ("Take over how a table's operations are handled (custom connectors)", "A table and handler functions"),
    "Types": ("Compare types, make them nullable or not, or describe a table type's columns", "A type (or a table type and a column)"),
    "Values: types and text": ("Get or replace a value's type, check it against a type, or read a value from text", "A value, then a type"),
    "Item and row expressions": ("Get the syntax tree of a function's body, or refer to a column inside it", "A function (Column: a column name)"),
    "Geography and geometry": ("Convert geography or geometry to and from Well-Known Text, or make a point", "Text or a value (points: coordinates)"),
    "Reading files and workbooks": ("Read a file, a folder's files, an Excel workbook, this workbook's tables or a PDF's tables", "A path or file contents (CurrentWorkbook: nothing)"),
    "Reading text formats": ("Read CSV or JSON, write JSON, or turn text into lines and back", "Text or file contents, with optional options"),
    "Web": ("Download a web page or its headers, render it in a browser, or pull tables out of HTML", "A URL (or HTML), with optional options"),
    "Binary views (advanced)": ("Take over how a binary's operations are handled (custom connectors)", "A binary and handler functions"),
    "Values: arithmetic": ("Add, subtract, multiply or divide values, or assert a value's type", "Two values (As: a value and a type)"),
    "Values: comparing": ("Compare values for equality or order, or make culture-aware comparers", "Two values, or a culture"),
    "Values: metadata": ("Read, remove or replace a value's metadata", "A value (then the metadata)"),
    "Values: internals": ("A value's expression, alternates, optimisation, native queries and versions", "A value, or a target and a query"),
    "Types: functions": ("Make function types and read their parameters and return type", "A function type (making one: a signature and a minimum)"),
    "Types: records": ("Make record types, read their fields, or open and close them", "A record type (making one: the fields and whether it's open)"),
    "Types: tables": ("Add, read or replace a table type's keys and partition key, or get its row type", "A table type, then keys or a partition key"),
    "Types: facets and more": ("Read or replace a type's facets, get a list's item type, or combine types", "A type (or a list of types)"),
    "Expressions and variables": ("Make and evaluate M expressions, or read variables and embedded values", "A value, a name or an expression"),
    "XML and binary lines": ("Read XML, turn binary into lines and back, or write a binary literal", "XML or binary, with optional options"),
    "Web requests, feeds and URIs": ("Build and split URIs, make web requests, or read OData and SODA feeds", "A URL or query parts"),
    "Binary: converting": ("Turn values, lists or text into binary and back, or work out its content type", "A value, list, text or binary"),
    "Binary: handling": ("Combine, split, slice, measure, buffer, compress or decompress binary", "A binary (then a size, offset or compression type)"),
    "BinaryFormat: integers": ("Read signed, unsigned or 7-bit encoded integers from binary", "Just the binary"),
    "BinaryFormat: other values": ("Read a byte, single, double, decimal, text, binary or null from binary", "The binary, or a length"),
    "BinaryFormat: structure": ("Build binary formats for byte order, choices, groups, lengths, lists and records", "A binary format, then how to shape it"),
    "Databases (1)": ("Connect to Access, DB2, Informix, MySQL, Oracle or PostgreSQL", "A server and a database (Access: the file)"),
    "Databases (2)": ("Connect to SQL Server, SAP HANA, Sybase or Teradata", "A server, sometimes a database"),
    "ODBC, OLE DB and ADO.NET": ("Connect or run queries through ODBC, OLE DB or ADO.NET", "A connection string (queries: then the query)"),
    "Cloud storage": ("Read Azure blobs, Data Lake, tables, Delta Lake or CDM folders", "A URL or an account"),
    "Big data and SharePoint": ("Read HDFS, HDInsight or SharePoint contents, files or lists", "A URL or an account"),
    "Cubes and analytics sources": ("Connect to Analysis Services, Essbase, SAP BW, Adobe or Google Analytics, or Salesforce", "A server or URL, or just options"),
    "Cube: building": ("Add dimensions and measures, apply parameters, or collapse or transform a cube", "A cube, then dimensions, measures or parameters"),
    "Cube: properties": ("Read a cube's attribute, measure and property details", "A cube, attribute, measure or property"),
    "Identity and services": ("Identities and memberships, Active Directory, Exchange and AI prompts", "An identity, provider, mailbox or prompt"),
}
