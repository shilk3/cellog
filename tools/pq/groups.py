# Power Query functions grouped by purpose, for 📘 Knowledge mode: a check
# on a group asks "Which one …?" for each member (its look-alikes as the
# wrong answers). The group is what's mastered and counted; each function's
# own record is kept in the background. Every function is in exactly one
# group. Members are written without the namespace when it's the group's
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
g("DateTime: this, next or last hour, minute, second", "DateTime", "IsInCurrentHour IsInCurrentMinute IsInCurrentSecond IsInNextHour IsInNextMinute IsInNextSecond IsInPreviousHour IsInPreviousMinute IsInPreviousSecond")
g("DateTime: the next or last N", "DateTime", "IsInNextNHours IsInNextNMinutes IsInNextNSeconds IsInPreviousNHours IsInPreviousNMinutes IsInPreviousNSeconds")
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
g("List: totals and averages", "List", "Sum Average Max Min Median Mode Product Count")
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
g("Table: about the table", "Table", "ColumnNames ColumnCount ColumnsOfType HasColumns Column RowCount ApproximateRowCount IsEmpty")
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
g("Table: keys and partitions", "Table", "AddKey Keys ReplaceKeys Partition PartitionKey PartitionValues ReplacePartitionKey Tables.GetRelationships")
g("Table: buffering and profiling", "Table", "Buffer StopFolding Profile Schema")
g("Table views (advanced)", "Table", "View ViewError ViewFunction")
g("Value and binary views", "Value", "ViewError ViewFunction Binary.View Binary.ViewError Binary.ViewFunction")
g("Table: rarely used", "Table", "ConformToPageReader FilterWithDataTable ReplaceRelationshipIdentity WithErrorContext Action.WithErrorContext List.ConformToPageReader Excel.ShapeTable")
# ---- Types, values and expressions ----
g("Types", "Type", "Is IsNullable NonNullable TableColumn TableSchema")
g("Values: types and text", "Value", "Type ReplaceType Is FromText")
g("Values: arithmetic", "Value", "Add Subtract Multiply Divide As")
g("Values: comparing", "Value", "Equals NullableEquals Compare Comparer.Equals Comparer.FromCulture")
g("Values: metadata", "Value", "Metadata RemoveMetadata ReplaceMetadata Lineage Traits")
g("Values: internals", "Value", "Expression Alternates Optimize NativeQuery Firewall VersionIdentity Versions")
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
g("Databases (2)", "Sql", "Database Databases SapHana.Database Sybase.Database Teradata.Database SqlExpression.SchemaFrom SqlExpression.ToExpression")
g("ODBC, OLE DB and ADO.NET", "Odbc", "DataSource Query InferOptions OleDb.DataSource OleDb.Query AdoDotNet.DataSource AdoDotNet.Query")
g("Cloud storage", "AzureStorage", "BlobContents Blobs DataLake DataLakeContents Tables DeltaLake.Metadata DeltaLake.Table Cdm.Contents")
g("Big data and SharePoint", "Hdfs", "Contents Files HdInsight.Containers HdInsight.Contents HdInsight.Files SharePoint.Contents SharePoint.Files SharePoint.Tables")
g("Cubes and analytics sources", "AnalysisServices", "Database Databases Essbase.Cubes SapBusinessWarehouse.Cubes AdobeAnalytics.Cubes GoogleAnalytics.Accounts Salesforce.Data Salesforce.Reports")
g("Cube: building", "Cube", "AddAndExpandDimensionColumn AddMeasureColumn ApplyParameter CollapseAndRemoveColumns ReplaceDimensions Transform Dimensions Measures")
g("Cube: properties", "Cube", "AttributeMemberId AttributeMemberProperty DisplayFolders MeasureProperties MeasureProperty Parameters Properties PropertyKey")
g("Identity and services", "Identity", "From IsMemberOf IdentityProvider.Default AccessControlEntry.ConditionToIdentities ActiveDirectory.Domains Exchange.Contents Graph.Nodes FabricAI.Prompt")
g("Odds and ends", "Module", "Module.Versions RData.FromBinary Progress.DataSourceProgress DirectQueryCapabilities.From")

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
