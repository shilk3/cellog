# The invitationals' own question sets (for review before they go in the
# game). Each invitational's Knowledge check asks from its own general set;
# after its first appearance that set joins the main general pool (marked,
# and tracked separately). Mobile asks three "Excel on a phone" questions plus
# one function-picker question (which category is a function under?).
# Each question: (league tier 5 easiest … 0 the top, skill, question, answer,
# [three wrong answers], source). Titan skill and the default skill are set
# per set.
SETS = {}
INFO = {
    "pq": {"name": "Power Query", "skill": "data", "titan": "speed"},
    "vba": {"name": "VBA", "skill": "games", "titan": "speed"},
    "robot": {"name": "OA Robot", "skill": "games", "titan": "speed"},
    "lam": {"name": "Lambda", "skill": "math", "titan": "lambda"},
    "py": {"name": "Python", "skill": "data", "titan": "speed"},
    "phone": {"name": "Excel on a phone", "skill": "map", "titan": "speed"},
}
_cur = None
def start(key, src):
    global _cur, _src
    _cur, _src = key, src
    SETS[key] = []
def q(tier, question, answer, wrong, skill=None, src=None):
    assert len(wrong) == 3 and len({answer, *wrong}) == 4, question
    SETS[_cur].append((tier, skill or INFO[_cur]["skill"], question, answer, list(wrong), src or _src))

# =============================== Power Query ===============================
# Microsoft Learn (Power Query docs, M language spec) and Excel's Get & Transform help.
start("pq", "Microsoft Power Query docs")
q(4, "Which button opens a selected range in the Power Query Editor?", "Data → From Table/Range", ["Insert → Table", "Formulas → Name Manager", "Review → Protect Sheet"])
q(4, "Which button sends a query's results back to the sheet?", "Close & Load", ["Refresh Preview", "Advanced Editor", "Keep Rows"])
q(4, "How do you undo one of a query's steps?", "Delete it from Applied Steps (the ✕ beside it)", ["Press Ctrl+Z after closing the editor", "Refresh the query", "Rename the query"])
q(4, "Which command uses the first row as the column names?", "Use First Row as Headers", ["Transpose", "Fill Down", "Group By"])
q(4, "Which command copies a value down into the empty (null) cells below it?", "Fill Down", ["Replace Values", "Flash Fill", "Fill Series"])
q(4, "Which command splits a column at each comma?", "Split Column → By Delimiter", ["Text to Columns", "Extract → Length", "Merge Columns"])
q(4, "Which command removes the junk rows at the top of an imported file?", "Remove Rows → Remove Top Rows", ["Keep Top Rows", "Remove Duplicates", "Filter → Does Not Equal"])
q(4, "Which command removes leading and trailing spaces?", "Trim", ["Clean", "Format → lowercase", "Replace Errors"], "text")
q(4, "Which command removes non-printing characters?", "Clean", ["Trim", "Remove Errors", "Split Column"], "text")
q(4, "Which command drops rows whose values repeat in the selected columns?", "Remove Duplicates", ["Keep Errors", "Remove Blank Rows", "Group By"])
q(4, "Which pane in Excel lists a workbook's queries?", "Queries & Connections", ["Name Manager", "Selection Pane", "Watch Window"])
q(3, "Unlike Excel's TRIM, Power Query's Trim leaves what alone?", "Repeated spaces between words", ["Spaces at the start", "Spaces at the end", "Line breaks at the end"], "text")
q(3, "A column header shows the ABC/123 icon. What's its type?", "Any (no type set yet)", ["Text", "Whole Number", "Decimal Number"])
q(3, "Which type does the 1.2 icon on a column header mean?", "Decimal Number", ["Whole Number", "Fixed Decimal (currency)", "Text"])
q(3, "How do you change a column's data type?", "Click the type icon on its header (or Transform → Data Type)", ["Format Cells", "Data Validation", "The Number Format box"])
q(3, "Which step does Power Query often add on its own after promoting headers?", "Changed Type", ["Removed Columns", "Sorted Rows", "Filtered Rows"])
q(3, "What's the default join kind in Merge Queries?", "Left Outer (all of the first, matches from the second)", ["Inner", "Full Outer", "Right Anti"])
q(3, "After a merge, the new column holds tables. How do you bring their columns in?", "The expand button (two arrows) on its header", ["Refresh", "Unpivot", "Transpose"])
q(3, "Which command turns a column's distinct values into new columns?", "Pivot Column", ["Unpivot Columns", "Transpose", "Group By"])
q(3, "Which command summarises rows by a key, like a SUMIFS per group?", "Group By", ["Pivot Column", "Merge Queries", "Index Column"])
q(3, "Which command adds a column from your own M formula?", "Custom Column", ["Conditional Column", "Index Column", "Duplicate Column"])
q(3, "Which command builds an if-then column without writing any M?", "Conditional Column", ["Custom Column", "Index Column", "Column From Examples"], "games")
q(3, "Which command builds a new column from a few examples you type?", "Column From Examples", ["Fill Down", "Flash Fill", "Custom Column"], "text")
q(3, "Add Column → Index Column adds…", "A column of running numbers", ["A copy of the key column", "Each row's text length", "A random ID per row"])
q(3, "Which command turns errors in a column into a value you choose?", "Replace Errors", ["Remove Errors", "Keep Errors", "Fill Down"])
q(3, "Extract → Text Before Delimiter keeps…", "The text before a character you choose", ["The text after the last space", "Only the numbers", "The first 10 characters"], "text")
q(2, "Split Column → By Delimiter can split into…", "Columns or rows", ["Only two columns", "Only new queries", "Only new sheets"])
q(2, "Which join kind keeps only the first table's rows that have no match?", "Left Anti", ["Left Outer", "Inner", "Right Anti"])
q(2, "Which join kind keeps only the rows that match in both tables?", "Inner", ["Full Outer", "Left Outer", "Left Anti"])
q(2, "Right-click a query → Reference makes…", "A new query that starts from the first one's result", ["An exact copy of all its steps", "A link to a cell", "A backup of the source file"])
q(2, "Load To… can send a query to…", "A table, a PivotTable, a PivotChart or only a connection", ["Only a new sheet", "Only the Data Model", "A chart sheet only"])
q(2, "Which View option shows each column's valid, error and empty percentages?", "Column quality", ["Query Dependencies", "Advanced Editor", "Monospaced"])
q(2, "Which view draws how a workbook's queries feed each other?", "Query Dependencies", ["Column profile", "Applied Steps", "Diagram of the Data Model"])
q(2, "Where do you change a query's file path or saved sign-in?", "Data Source Settings", ["Name Manager", "Trust Center", "Workbook Connections only"])
q(2, "What privacy levels can a data source have?", "None, Public, Organizational or Private", ["Low, Medium or High", "Read, Write or Admin", "Open, Shared or Locked"])
q(2, "In M, `each [Price] * 2` is…", "A function run for each row, using its Price", ["Price's header times two", "A loop that runs twice", "A list of every price"])
q(2, "How do you write a step name with a space in it in M?", "#\"Changed Type\"", ["[Changed Type]", "'Changed Type'", "{Changed Type}"])
q(2, "In M, {1, 2, 3} is a…", "List", ["Record", "Table", "Function"])
q(2, "In M, [Name = \"Ann\", Age = 30] is a…", "Record", ["List", "Table", "Text value"])
q(2, "Which operator joins two text values in M?", "&", ["+", "||", "CONCAT"], "text")
q(2, "How do you write 'not equal to' in M?", "<>", ["!=", "=/=", "NOT="])
q(2, "Which of these makes a date in M?", "#date(2024, 1, 31)", ["DATE(2024,1,31)", "Date(31/1/2024)", "@2024-01-31"], "time")
q(2, "Which is true of M?", "It's case-sensitive (Table.AddColumn works, table.addcolumn doesn't)", ["It ignores case everywhere", "Only text values ignore case", "Only step names ignore case"])
q(1, "In M, `each` is shorthand for…", "(_) => …, a function of one argument", ["A For loop", "The list of every row", "A table join"])
q(1, "In an M query, what do `let` and `in` do?", "let names the steps; in picks the result", ["They declare a loop", "They import a library", "They start an error handler"])
q(1, "A list is called L. How do you get its first item in M?", "L{0}", ["L{1}", "L[0]", "L(1)"])
q(1, "Which M operator gives the right-hand value when the left is null?", "??", ["||", "?:", "!!"])
q(1, "Which M expression gives a fallback when something errors?", "try … otherwise …", ["On Error Resume Next", "IFERROR(…)", "catch … finally"], "games")
q(1, "What's query folding?", "Turning steps into the source's own query (like SQL) so it runs there", ["Collapsing all steps into one", "Hiding queries in the pane", "Merging two queries into one"])
q(1, "Column profiling is based on how many rows by default?", "The first 1,000", ["The first 100", "The first 10,000", "Every row"])
q(1, "Which M function lists the tables and named ranges in the current workbook?", "Excel.CurrentWorkbook()", ["Excel.Workbook()", "Table.FromWorkbook()", "Sheet.All()"])
q(1, "How do you turn a query into a reusable function?", "Right-click → Create Function (or write it as (x) => …)", ["Save it as a template", "Load it to the Data Model", "Rename it with fn_ at the front"])
q(1, "What does Formula.Firewall mean in an error?", "The query combines sources in a way their privacy levels block", ["The file's password-protected", "A column name is misspelt", "Excel ran out of memory"])

# =================================== VBA ===================================
# Microsoft Learn (Office VBA reference) and Excel's macro help.
start("vba", "Microsoft Office VBA docs")
q(3, "What does VBA stand for?", "Visual Basic for Applications", ["Visual Builder for Automation", "Virtual Basic Add-in", "Very Basic Automation"])
q(3, "Which tab has Record Macro and Visual Basic?", "Developer", ["Data", "Formulas", "Review"])
q(3, "How do you show the Developer tab?", "File → Options → Customize Ribbon → tick Developer", ["Right-click a cell → Developer", "Ctrl+D", "View → Show Developer"])
q(3, "Where does a recorded macro's code go?", "A module in the VBA editor (like Module1)", ["A hidden sheet", "The Name Manager", "A cell comment"])
q(3, "Recording with 'Use Relative References' makes the macro…", "Work from the active cell instead of fixed addresses", ["Record formulas only", "Run faster", "Skip formatting"])
q(3, "Which keyword starts a macro you can run from the Macro dialog?", "Sub", ["Function", "Macro", "Begin"])
q(3, "How does a comment line start in VBA?", "With an apostrophe (')", ["With //", "With #", "With --"], "text")
q(3, "Which line sets A1 to 5?", "Range(\"A1\").Value = 5", ["Cell(\"A1\") = 5", "A1 := 5", "Set A1 = 5"], "map")
q(3, "Which shows a pop-up message to the user?", "MsgBox", ["Debug.Print", "InputBox", "Alert"])
q(3, "Which asks the user to type in a value?", "InputBox", ["MsgBox", "TextBox.Show", "Prompt"])
q(3, "Can Ctrl+Z undo what a macro just did?", "No — running a macro clears the undo list", ["Yes, step by step", "Yes, but only formatting", "Only in .xlsm files"])
q(2, "Which kind of procedure can return a value to a cell formula?", "Function", ["Sub", "Event", "Module"])
q(2, "Cells(2, 3) refers to…", "C2 (row 2, column 3)", ["B3", "Sheet 2, column C", "Two cells right of A1"], "map")
q(2, "Where does Debug.Print write?", "The Immediate window", ["The status bar", "A message box", "The active cell"])
q(2, "Which key runs the macro your cursor is in?", "F5", ["F8", "F9", "F2"])
q(2, "Which key steps through the code one line at a time?", "F8", ["F5", "F9", "F10"])
q(2, "Which statement makes VBA demand that every variable is declared?", "Option Explicit", ["Option Strict", "Option Base 1", "Dim All"])
q(2, "Which keyword declares a variable?", "Dim", ["Var", "Let", "Declare"])
q(2, "A variable declared without a type is a…", "Variant", ["String", "Integer", "Object"])
q(2, "Which type holds bigger whole numbers?", "Long", ["Integer", "Byte", "Boolean"], "math")
q(2, "Which loop visits each item of a collection, like each cell in a range?", "For Each … Next", ["Do Until … Loop", "While … Wend", "Select Case"])
q(2, "How many times does For i = 1 To 10 Step 2 run?", "5", ["10", "2", "4"], "math")
q(2, "Which statement leaves a For loop early?", "Exit For", ["Break", "Stop", "End Loop"])
q(2, "Which statement picks one of many branches by a value?", "Select Case", ["Switch Case", "Choose Case", "If Case"])
q(2, "What does On Error Resume Next do?", "Skips lines that error and carries on", ["Stops at the first error", "Restarts the macro", "Shows every error in a list"])
q(2, "Which property turns off screen redrawing to speed up a macro?", "Application.ScreenUpdating = False", ["Application.Visible = False", "Application.Calculate = False", "Screen.Hide"])
q(2, "Range(\"A1\").End(xlDown) is like pressing…", "Ctrl+Down Arrow", ["Page Down", "End then Enter", "Ctrl+End"], "map")
q(2, "Which property gives a cell's formula as text?", ".Formula", [".Text", ".Value", ".Address"])
q(2, "How do you call an Excel worksheet function like SUM from VBA?", "WorksheetFunction.Sum(…)", ["Excel.Sum(…)", "Math.Sum(…)", "Formula.Sum(…)"])
q(2, "What's With … End With for?", "Using one object several times without repeating its name", ["Running code in a loop", "Handling errors", "Declaring constants"])
q(2, "Which file name is the Personal Macro Workbook?", "PERSONAL.XLSB", ["Book1.xlsm", "Macros.xlam", "Normal.dotm"])
q(2, "A macro in the Personal Macro Workbook is available…", "In every workbook you open on that PC", ["Only in the workbook you recorded it in", "Only on the web", "Only after you email it"])
q(2, "Which setting lets macros in chosen folders run without a prompt?", "Trusted Locations", ["Protected View", "Safe Mode", "Shared Workbook"])
q(1, "Which shortcut opens the Immediate window?", "Ctrl+G", ["Ctrl+I", "F7", "Ctrl+R"])
q(1, "What does F9 do in the VBA editor?", "Toggles a breakpoint on the current line", ["Recalculates the workbook", "Runs the macro", "Steps over a line"])
q(1, "Which window lists a project's sheets, modules and forms?", "Project Explorer", ["Immediate window", "Locals window", "Object Browser"])
q(1, "Which window shows an object's settings, like a sheet's Visible?", "Properties window (F4)", ["Watch window", "Immediate window", "Call Stack"])
q(1, "What do you need to store an object, like a Range, in a variable?", "Set", ["Let", "Dim only", "Put"])
q(1, "What's the largest value an Integer can hold?", "32,767", ["65,535", "2,147,483,647", "255"], "math")
q(1, "Which object holds details of the last runtime error?", "Err", ["Error", "Debug", "Application.LastError"])
q(1, "ThisWorkbook means…", "The workbook that holds the running code", ["Whichever workbook is in front", "The newest workbook", "The Personal Macro Workbook"])
q(1, "Which line stops Excel's 'Are you sure?' prompts during a macro?", "Application.DisplayAlerts = False", ["Application.Prompts = False", "Application.ScreenUpdating = False", "Alerts.Off"])
q(1, "Which line finds the last used row in column A?", "Cells(Rows.Count, \"A\").End(xlUp).Row", ["Range(\"A1\").LastRow", "Rows.Count", "UsedRange.Row"], "map")
q(1, "Which character continues a statement on the next line?", "A space and an underscore ( _)", ["A backslash", "&&", "A semicolon"])
q(1, "Which event runs when a cell on a sheet is changed?", "Worksheet_Change", ["Worksheet_Calculate", "Worksheet_Activate", "Workbook_Open"])
q(1, "Where does Workbook_Open code go?", "The ThisWorkbook module", ["Module1", "A UserForm", "Sheet1's module"])
q(1, "A custom dialog with boxes and buttons that you design is a…", "UserForm", ["MsgBox", "Content control", "Ribbon group"])
q(1, "Since 2022, Office blocks macros in files from the internet. How do you unblock a file you trust?", "File Properties → tick Unblock (or use a Trusted Location)", ["Rename it to .xlsx", "Open it twice", "Turn off AutoSave"])
q(0, "Which statement turns normal error handling back on after On Error Resume Next?", "On Error GoTo 0", ["On Error Resume", "Err.Clear", "On Error Stop"])
q(0, "Which event runs when you select a different cell?", "Worksheet_SelectionChange", ["Worksheet_Change", "Worksheet_Activate", "Worksheet_Click"])
q(0, "What does ReDim Preserve do?", "Resizes an array and keeps its values", ["Clears an array", "Copies an array to a sheet", "Locks an array's size"])
q(0, "A function you write in VBA and use in a cell (a UDF) can't…", "Change other cells or their formatting", ["Return text", "Take a range as an argument", "Be used twice on a sheet"])
q(0, "Which line makes a UDF recalculate whenever the sheet calculates?", "Application.Volatile", ["Application.Calculate", "Me.Refresh", "Option Volatile"])

# ================================ OA Robot =================================
# OA Robot's online documentation (oarobot.com/docs).
start("robot", "OA Robot docs")
q(2, "What's OA Robot?", "An Excel add-in that turns formulas, lambdas, macros and queries into commands you launch with a few keys", ["A Python library for Excel", "An Excel template gallery", "A chatbot built into Excel"])
q(2, "Which shortcut opens OA Robot?", "Ctrl+Shift+O", ["Ctrl+Shift+R", "Alt+O", "Ctrl+Space"])
q(2, "Which ribbon button also opens OA Robot?", "Robot Commands on the Home tab", ["Developer → Robot", "Data → Automate", "Add-ins → OA"])
q(2, "What's OA Robot's searchable window called?", "The Command Palette", ["The Task Pane", "The Name Box", "The Quick Access Toolbar"])
q(2, "Which key closes the Command Palette?", "Esc", ["Enter", "F1", "Tab"])
q(2, "How do you run the highlighted command?", "Press Enter (or double-click it)", ["Press F5", "Press Ctrl+Enter", "Press Space"])
q(2, "OA Robot's search, matching words, acronyms and launch codes, is called…", "Hypersearch", ["Smart Find", "Quick Search", "Fuzzy Lookup"])
q(2, "What's a launch code?", "A short code (like af) that brings a command to the top of the search", ["A licence key", "A password for a command", "A Ctrl key shortcut"])
q(2, "Can two commands share the same launch code?", "Yes", ["No, codes are unique", "Only in different collections", "Only with Enterprise"])
q(2, "In an OA Robot keyboard shortcut, what does ^ stand for?", "Ctrl", ["Shift", "Alt", "The Windows key"])
q(2, "In an OA Robot keyboard shortcut, what does % stand for?", "Alt", ["Ctrl", "Shift", "Caps Lock"])
q(2, "In an OA Robot keyboard shortcut, what does + stand for?", "Shift", ["Ctrl", "Alt", "Plus, the key itself"])
q(2, "What does typing @ in the search bar show?", "Your command collections", ["Your tags", "Your parameters", "Recent commands"])
q(2, "What does # followed by a word do in the search bar?", "Filters to commands with that tag", ["Searches cell values", "Opens the help for a command", "Lists number formats"])
q(2, "Where do OA Robot commands live?", "In command collections, each stored in an Excel workbook", ["In the Windows registry", "In the Name Manager", "On a web server only"])
q(2, "What's a setup code?", "A 6-character code that downloads and registers a collection from the OA Robot team", ["Your licence key", "A launch code for setup commands", "A password for a shared collection"])
q(2, "What does F1 (or right-click → Help) on a command do?", "Generates its documentation in the Excel Task Pane", ["Opens Excel's own Help", "Runs it in test mode", "Emails the author"])
q(2, "How do you move the Command Palette?", "Drag it by the Robot's face", ["Drag its search bar", "Alt+Space → Move", "Double-click its border"])
q(2, "What does a User Context Filter do?", "Shows a command only when it fits the current selection", ["Hides a command from other users", "Filters the sheet's data", "Limits a command to one workbook"])
q(2, "Can an out-of-context command still be run?", "Yes — it's greyed out lower in the list but still runs", ["No, it's hidden", "Only by its shortcut", "Only after a restart"])
q(1, "Which keyboard shortcut is ^+r?", "Ctrl+Shift+R", ["Ctrl+Alt+R", "Alt+Shift+R", "Ctrl+R+Enter"])
q(1, "You give an OA Robot command the same shortcut as an Excel one. Which wins?", "OA Robot's", ["Excel's", "Whichever was set first", "Neither runs"])
q(1, "Two commands share a keyboard shortcut. What does pressing it do?", "Opens the palette filtered to those commands", ["Runs both", "Runs the newer one", "Shows an error"])
q(1, "What does the ! key list in the search bar?", "Command types, to filter by", ["Errors from the last run", "Disabled commands", "Secret parameters"])
q(1, "What does typing { in the search bar list?", "Parameters", ["Command collections", "Tags", "Texts"])
q(1, "What does typing ++ in the search bar start?", "Adding a new command", ["Copying the last command", "A search in every collection", "Zooming the palette"])
q(1, "What does typing @+ in the search bar start?", "Adding a command collection", ["Adding a tag", "Emailing a collection", "Adding a user"])
q(1, "Which key edits the highlighted command?", "F2", ["F4", "F11", "Ctrl+E"])
q(1, "How is a parameter expression written?", "{{parameter_name}}", ["[[parameter_name]]", "<<parameter_name>>", "$parameter_name"])
q(1, "How is an application expression written?", "[[ActiveCell]]", ["{{ActiveCell}}", "=ActiveCell()", "@ActiveCell"], "map")
q(1, "With C4 active, what does the formula =[[ActiveCell]] + 1 become?", "=C4 + 1", ["=5", "=[[C4]] + 1", "=ActiveCell + 1"], "map")
q(1, "What does ::value after a range do, as in [[ActiveCell::value]]?", "Gives the cell's value instead of its address", ["Formats it as a number", "Checks it isn't blank", "Copies it to the clipboard"], "map")
q(1, "You use {{name}} without defining a parameter called name. What happens?", "It asks the user to type a value when the command runs", ["The command fails", "It uses blank", "It uses the active cell"])
q(1, "Parameter names can't contain…", "Spaces", ["Underscores", "Lower-case letters", "More than 8 letters"])
q(1, "A child parameter is available to…", "Only its command (and commands it triggers)", ["Every command in every collection", "Only the active workbook", "Only Enterprise users"])
q(1, "What does {{System.Now}} give?", "The present time", ["Today's date as text", "The OA Robot version", "The time Excel opened"], "time")
q(1, "An Excel Formula Command's Destination Range Address is blank. Where does the formula go?", "Into each selected cell", ["Into A1", "Into a new sheet", "Nowhere — it errors"], "map")
q(1, "Which command type comes with the free Standard licence?", "Excel Formula Command", ["VBA Macro Command", "Power Query Command", "AI Chat Command"])
q(1, "Which output comes with the free Standard licence?", "Message Box Output", ["Clipboard Output", "Excel Range Output", "Text File Output"])
q(1, "A VBA Macro Command can do what Excel's Macro dialog can't…", "Pass values into the macro as parameters", ["Run Sub procedures", "Run macros in .xlsm files", "Run macros from the Personal workbook"])
q(1, "Several procedures in one Macro Expression are separated by…", "Semicolons", ["Commas", "New lines", "Pipes (|)"])
q(1, "Before adding a VBA Macro Command, which Trust Center option must be on?", "Trust access to the VBA project object model", ["Enable all ActiveX controls", "Disable Protected View", "Allow external content"])
q(1, "In a Send Keys command, what does {DOWN 2}{RIGHT 5} do?", "Moves two cells down and five right", ["Selects a 2×5 range", "Inserts two rows and five columns", "Scrolls two pages down"], "map")
q(0, "What does Shift+F2 on a selected command open (Enterprise)?", "The Advanced Editor", ["The VBA editor", "The Name Manager", "Its documentation"])
q(0, "When looking up a parameter name, which comes first?", "The command's child parameters", ["Shared parameters in other collections", "Excel's defined names", "Built-in System parameters"])
q(0, "What does [[ActiveCell#]] mean?", "The active cell and its spill range", ["The active cell's row number", "Every numbered cell", "The active cell's address as text"], "map")
q(0, "What does [[Selection.EachCell]] do in a Formula or VBA Macro Command?", "Runs it once for each selected cell", ["Counts the selected cells", "Selects every cell on the sheet", "Lists the cells' addresses"], "map")
q(0, "What does AvailableCellBelow (NewTableTargetBelow) find?", "The next free spot below the data, for a new table", ["The last used cell", "The first blank in the column", "The cell below the active cell"], "map")
q(0, "A Power Query Command's Table Style is blank. Which style does its table get?", "TableStyleMedium2", ["TableStyleLight1", "TableStyleMedium7", "TableStyleDark1"], "data")
q(0, "A Hidden command is…", "Left out of the palette, but still usable inside other commands", ["Deleted after it runs", "Only visible to its author", "Encrypted on disk"])
q(0, "In User Visibility, what does a - in front of a Windows user name do?", "Hides the command from that user", ["Makes that user the owner", "Gives them edit rights", "Marks them as a guest"])
q(0, "Exported OA Robot settings are saved in which file type?", ".oax", [".xlam", ".json", ".oar"])
q(0, "Why does the Command History help search?", "It learns the words you type to find each command", ["It sorts commands by date added", "It removes old commands", "It shares your searches with your team"])

# ================================= Lambda ==================================
# Microsoft's LAMBDA, LET and helper-function help, and the Excel Labs
# (Advanced Formula Environment) docs.
start("lam", "Microsoft Excel LAMBDA help")
q(0, "What's the last argument of LAMBDA?", "The calculation to return", ["The function's name", "The first parameter", "An optional default value"])
q(0, "How many parameters can a LAMBDA take?", "Up to 253", ["Up to 255", "Up to 64", "Up to 30"])
q(0, "You type =LAMBDA(x, x+1) in a cell without calling it. What do you get?", "#CALC!", ["#NAME?", "0", "#VALUE!"])
q(0, "You call a LAMBDA with the wrong number of arguments. What do you get?", "#VALUE!", ["#CALC!", "#N/A", "#REF!"])
q(0, "Which of these can't be a LAMBDA parameter name?", "B2", ["rate", "x_1", "total"])
q(0, "How do you test a LAMBDA in a cell before naming it?", "Call it straight away: =LAMBDA(x, x+1)(5)", ["Press F9 on the Name Manager", "Put it in a comment", "Wrap it in TEST()"])
q(0, "In Name Manager, where does a LAMBDA go?", "The Refers to box", ["The Comment box", "The Scope list", "The Name box"])
q(0, "What does the Comment of a named LAMBDA do?", "Shows as its description when you type its name", ["Runs before it's called", "Sets its default argument", "Nothing — it's for printing only"])
q(0, "Why might you build a LAMBDA instead of a VBA function?", "It needs no macros, so it works in .xlsx files and on the web", ["It runs on any Excel version since 2007", "It can change other cells", "It can open files"])
q(0, "A named LAMBDA can be used in another workbook…", "Once its name is copied into that workbook", ["Straight away, everywhere", "Only through VBA", "Never"])
q(0, "How does a named LAMBDA call itself (recursion)?", "By using its own name in its formula", ["With a SELF() function", "Through a VBA loop", "It can't"])
q(0, "What must a recursive LAMBDA have?", "A stopping condition (usually an IF) so it ends", ["At least 10 parameters", "A LET at the start", "A Workbook scope"])
q(0, "Fact is named =LAMBDA(n, IF(n<=1, 1, n*Fact(n-1))). What's =Fact(4)?", "24", ["4", "10", "16"])
q(0, "What can a LAMBDA return?", "A value, an array, or even another LAMBDA", ["Only a single value", "Only numbers", "Only text"])
q(0, "What's =LAMBDA(a, LAMBDA(b, a+b))(2)(3)?", "5", ["6", "#CALC!", "23"])
q(0, "A LAMBDA with no parameters, like LAMBDA(SEQUENCE(3)), wrapping a value for later, is often called a…", "Thunk", ["Stub", "Closure loop", "Shell"])
q(0, "What's =LET(x, 2, y, 3, x*y)?", "6", ["5", "23", "#NAME?"])
q(0, "Names made with LET can be used…", "Only inside that formula", ["Anywhere in the workbook", "On the same sheet", "In VBA too"])
q(0, "What does MAP(A1:A3, LAMBDA(x, x*2)) return?", "Each value doubled, in the same shape", ["The sum of the doubled values", "Only the first value doubled", "A single TRUE or FALSE"])
q(0, "You pass two arrays to MAP. How many parameters does its LAMBDA need?", "Two — one per array", ["One", "Three", "None"])
q(0, "What does MAKEARRAY(3, 2, LAMBDA(r, c, r*c)) return?", "A 3-row, 2-column array of row × column", ["The number 6", "A 2-row, 3-column array", "#CALC!"])
q(0, "Which helper calls a LAMBDA for each row and column number to build an array?", "MAKEARRAY", ["MAP", "SEQUENCE", "SCAN"])
q(0, "What does BYCOL(A1:C3, LAMBDA(c, MAX(c))) return?", "Three column maximums, in a row", ["One maximum", "Three row maximums, in a column", "The whole range sorted"])
q(0, "What does BYROW(A1:C3, LAMBDA(r, SUM(r))) return?", "Three row totals, in a column", ["One grand total", "Three column totals", "Nine values"])
q(0, "BYROW's LAMBDA returns more than one value for a row. What do you get?", "#CALC! (Excel won't nest arrays)", ["Every value spilled", "Only the first value", "#SPILL!"])
q(0, "In REDUCE(0, A1:A5, LAMBDA(acc, v, acc+v)), what's the 0?", "The accumulator's starting value", ["The row to start at", "The error value", "How many times to loop"])
q(0, "REDUCE(0, A1:A5, LAMBDA(acc, v, acc+v)) gives the same as…", "SUM(A1:A5)", ["COUNT(A1:A5)", "MAX(A1:A5)", "A5"])
q(0, "What's SCAN(0, {1,2,3}, LAMBDA(a, v, a+v))?", "{1,3,6}", ["{6}", "{0,1,3}", "{1,2,3}"])
q(0, "What's REDUCE(1, {2,3,4}, LAMBDA(a, v, a*v))?", "24", ["9", "10", "{2,6,24}"])
q(0, "SCAN and REDUCE give their LAMBDA which two parameters?", "The accumulator and the current value", ["The row and the column", "The array and its size", "The value and its address"])
q(0, "=BYROW(A1:C3, SUM) works without writing LAMBDA because…", "You can pass a function's name in place of a LAMBDA", ["SUM is a LAMBDA in disguise", "BYROW sums by default", "Excel adds the LAMBDA when you save"])
q(0, "Which Excel versions have LAMBDA?", "Microsoft 365, Excel for the web and Excel 2024", ["Every version since 2010", "Only Excel for Mac", "Only with the Analysis ToolPak"])
q(0, "The Advanced Formula Environment is now part of which free add-in?", "Excel Labs", ["Analysis ToolPak", "Power Pivot", "Solver"])
q(0, "In the Advanced Formula Environment, how do you write a comment in a formula?", "// at the start of the comment", ["' like VBA", "# like Python", "A N(\"…\") wrapper only"])
q(0, "The Advanced Formula Environment can import LAMBDAs from…", "A GitHub Gist URL", ["A PDF", "A VBA module", "A PivotTable"])
q(0, "In the Advanced Formula Environment, what does a module do?", "Groups functions under a prefix, like Text.Reverse", ["Turns them into VBA", "Locks them with a password", "Runs them on open"])
q(0, "What's a lambda library?", "A collection of named LAMBDAs you reuse and share", ["Microsoft's list of all functions", "A folder of VBA files", "A Power Query connector"])
q(0, "Why put LET inside a LAMBDA?", "To name its steps so each is worked out once", ["To make it recursive", "To give it more parameters", "To make it volatile"])
q(0, "A LAMBDA is scoped to Workbook in Name Manager. Where can you use it?", "On any sheet of that workbook", ["Only on the sheet you made it on", "In every open workbook", "Only in Name Manager"])
q(0, "Which helper turns each item of one or more arrays into a new value?", "MAP", ["REDUCE", "BYCOL", "MAKEARRAY"])
q(0, "Which helper would you use for a running balance down a column?", "SCAN", ["REDUCE", "MAP", "BYCOL"])
q(0, "Which helper would you use to collapse a list into one number your own way?", "REDUCE", ["SCAN", "MAKEARRAY", "BYROW"])
q(0, "What's =MAP({1,2,3}, {10,20,30}, LAMBDA(a, b, a+b))?", "{11,22,33}", ["66", "{10,20,30}", "#VALUE!"])
q(0, "What's =MAKEARRAY(2, 2, LAMBDA(r, c, r+c))?", "{2,3;3,4}", ["{1,2;3,4}", "8", "{2,2;2,2}"])
q(0, "=LAMBDA(x, y, x^y)(2, 3) returns…", "8", ["6", "9", "5"])
q(0, "Which function can a LAMBDA use to give an optional argument a default?", "IF(ISOMITTED(arg), default, arg)", ["DEFAULT(arg, value)", "IFNA(arg, default)", "OPTIONAL(arg)"])
q(0, "Which helper returns one result per column?", "BYCOL", ["BYROW", "MAP", "SCAN"])
q(0, "GROUPBY's function argument can be your own LAMBDA. What must it return for each group?", "A single value", ["An array the size of the group", "A table", "TRUE or FALSE only"])
q(0, "Which is a good name for a library LAMBDA?", "A clear verb-style name like REVERSETEXT", ["A1", "SUM", "x"])
q(0, "What does =LET(s, SEQUENCE(4), SUM(s)) return?", "10", ["4", "{1;2;3;4}", "24"])

# ================================= Python ==================================
# Microsoft's Python in Excel help, and pandas basics.
start("py", "Microsoft Python in Excel help")
q(0, "How do you start a Python formula in a cell?", "Type =PY( (or Formulas → Insert Python)", ["Type =PYTHON(", "Press Alt+P", "Data → Run Python"])
q(0, "Which shortcut turns a cell into a Python cell?", "Ctrl+Alt+Shift+P", ["Ctrl+Shift+P", "Alt+F11", "Ctrl+P"])
q(0, "In a Python cell, what does Enter do?", "Starts a new line of code", ["Runs the code", "Leaves Python mode", "Shows the Diagnostics pane"])
q(0, "Which keys run (commit) the Python code in a cell?", "Ctrl+Enter", ["Enter", "Tab", "Shift+Enter"])
q(0, "Where does Python in Excel's code run?", "In the Microsoft Cloud", ["On your PC's own Python", "Inside VBA", "On a OneDrive folder"])
q(0, "Which function brings Excel ranges into Python?", "xl()", ["rng()", "excel()", "ref()"])
q(0, "What does headers=True in xl(\"A1:C10\", headers=True) say?", "The first row holds the column names", ["Hide the headers", "Add Excel's column letters", "Keep the cell formatting"])
q(0, "A range with headers comes into Python as…", "A pandas DataFrame", ["A NumPy matrix", "A Python string", "An Excel table object"])
q(0, "How do you bring a whole Excel table, headers and all, into Python?", "xl(\"Table1[#All]\", headers=True)", ["xl(\"Table1\")", "xl(\"Table1[#Headers]\")", "Table1.to_python()"])
q(0, "What does a Python cell show by default?", "The value of the last line it runs", ["Everything print() writes", "The first variable defined", "The code itself"])
q(0, "Where does print() output go?", "The Diagnostics pane", ["The cell", "The status bar", "A message box"])
q(0, "In =PY(code, return_type), what does return_type 0 mean?", "Return an Excel value", ["Return a Python object", "Don't return anything", "Return an error"])
q(0, "A Python object result shows in the cell as…", "A card icon you can open to preview it", ["A grey error", "Its code", "A hyperlink"])
q(0, "Where do you switch between a Python object and an Excel value?", "The Python output menu by the formula bar", ["Format Cells", "Data → Data Types", "File → Options"])
q(0, "A DataFrame returned as Excel values does what?", "Spills into a range of cells", ["Turns into a chart", "Shows only its first cell", "Becomes a PivotTable"])
q(0, "What alias is pandas imported as by default?", "pd", ["pa", "pn", "pds"])
q(0, "What alias is NumPy imported as by default?", "np", ["nu", "npy", "num"])
q(0, "Which plotting library is imported as plt by default?", "matplotlib.pyplot", ["seaborn", "plotly", "bokeh"])
q(0, "Which library is imported as sns by default?", "seaborn", ["statsmodels", "scipy", "sklearn"])
q(0, "Where do Python in Excel's libraries come from?", "Anaconda", ["PyPI, installed when you ask", "Your PC's Python", "Microsoft's VBA library"])
q(0, "Can you pip install other packages in Python in Excel?", "No — you get the Anaconda packages it comes with", ["Yes, with !pip", "Yes, from Options", "Only on Mac"])
q(0, "Why does pandas.read_csv(\"C:/data.csv\") fail in Python in Excel?", "It can't reach your local files (or the internet)", ["read_csv was removed from pandas", "CSV needs Power Query", "Paths need backslashes"])
q(0, "How should you get outside data into Python in Excel?", "Into the workbook first (e.g. with Power Query), then xl()", ["Through requests.get()", "By opening it in Python", "Through VBA"])
q(0, "Which error means the Python code itself failed?", "#PYTHON!", ["#CALC!", "#SCRIPT!", "#CODE!"])
q(0, "What does #BUSY! mean in a Python cell?", "It's still calculating in the cloud", ["Another user is editing", "The code has a loop", "The sheet is protected"])
q(0, "What does #CONNECT! mean in a Python cell?", "Excel couldn't reach the Python service", ["The code imports a missing library", "The range is empty", "The sheet has a broken link"])
q(0, "In what order do Python cells calculate?", "Row by row across each sheet, sheets in tab order", ["Column by column", "In the order you typed them", "All at once, in any order"])
q(0, "A variable made in one Python cell can be used…", "In Python cells that calculate after it", ["Only in that cell", "In any cell, even earlier ones", "Only on another sheet"])
q(0, "Partial calculation mode recalculates everything except…", "Python formulas and data tables", ["Volatile functions", "PivotTables", "Charts"], "cards")
q(0, "How do stale Python results look before you recalculate?", "Struck through", ["Greyed out", "In red", "Hidden"], "cards")
q(0, "Which key recalculates stale Python cells?", "F9", ["F5", "Ctrl+R", "F2"], "cards")
q(0, "A Matplotlib chart comes back into the cell as…", "An image", ["An Excel chart you can edit", "A list of points", "A link to a web page"])
q(0, "Where can you see the import statements every Python cell starts with?", "Formulas → Initialization (in the Python group)", ["File → Info", "The VBA editor", "Data → Queries"])
q(0, "Which pandas method shows the first five rows?", "df.head()", ["df.top()", "df.first()", "df.show(5)"])
q(0, "Which pandas method gives summary statistics (count, mean, std…)?", "df.describe()", ["df.info()", "df.summary()", "df.stats()"])
q(0, "What does df.shape give?", "(rows, columns)", ["The column types", "The first row", "The memory used"])
q(0, "What does df.columns give?", "The column names", ["The number of columns", "The first column's values", "The column widths"])
q(0, "What does df[\"Sales\"].sum() give?", "The total of the Sales column", ["The number of Sales rows", "Sales sorted", "Each Sales value doubled"], "math")
q(0, "What does df.groupby(\"Region\")[\"Sales\"].sum() give?", "Total Sales for each Region", ["Sales sorted by Region", "The number of Regions", "Each Region's first sale"])
q(0, "What does df.dropna() do?", "Drops rows with missing values", ["Drops duplicate rows", "Drops the first row", "Drops every number column"])
q(0, "What does df.fillna(0) do?", "Fills missing values with 0", ["Clears the whole DataFrame", "Counts the zeros", "Drops rows with 0"])
q(0, "What does df.sort_values(\"Sales\", ascending=False) do?", "Sorts the rows by Sales, largest first", ["Sorts the columns by name", "Keeps only the top sale", "Ranks Sales in a new column"])
q(0, "What does df[df[\"Sales\"] > 100] give?", "Only the rows where Sales is over 100", ["A TRUE/FALSE for each row", "Sales with 100 added", "The first 100 rows"])
q(0, "pd.merge(a, b, on=\"ID\") is most like…", "Merge Queries (or XLOOKUP) on ID", ["Append Queries", "SUMIF on ID", "Removing duplicate IDs"])
q(0, "Which pandas method builds a PivotTable-style summary?", "df.pivot_table()", ["df.crosstab_sum()", "df.summarise()", "df.pivotby()"])
q(0, "What's the difference between df.loc and df.iloc?", "loc picks by labels, iloc by positions", ["loc is for rows, iloc for columns", "iloc is the older name for loc", "loc changes values, iloc reads them"])
q(0, "Python counts positions from…", "0", ["1", "-1", "A"])
q(0, "How does a Python comment start?", "#", ["//", "'", "--"], "text")
q(0, "What does len(df) give?", "The number of rows", ["The number of columns", "The number of cells", "The longest text"])
q(0, "What does df[\"Name\"].str.upper() do?", "Puts every Name in capitals", ["Sorts the names", "Removes blank names", "Finds the longest name"], "text")

# ============================ Excel on a phone =============================
# Microsoft's Excel for iPhone and Android touch guides, the mobile ribbon,
# freeze panes, Data from Picture, Cards View, AutoSum and licensing help
# pages. Rows marked "Good practice" are advice rather than a documented step.
start("phone", "Microsoft Excel mobile help")
T = "Microsoft touch guide (iPhone/Android)"
q(4, "How do you zoom in on a sheet?", "Spread two fingers apart", ["Pinch two fingers together", "Double-tap the formula bar", "Tap and hold a cell"], src=T)
q(4, "How do you zoom out?", "Pinch two fingers together", ["Spread two fingers apart", "Swipe down with three fingers", "Double-tap the sheet tab"], src=T)
q(4, "How do you select a cell?", "Tap it", ["Double-tap it", "Swipe across it", "Pinch it"], src=T)
q(4, "How do you select several cells?", "Tap one, then drag the selection handle", ["Pinch over them", "Tap each one with two fingers", "Shake the phone"], src=T)
q(4, "How do you add or edit what's in a cell?", "Double-tap the cell, or tap in the formula bar", ["Tap and hold the column heading", "Swipe left on the cell", "Pinch the cell"], "text", src=T)
q(4, "How do you place the cursor to edit part of a formula?", "Tap in the formula bar", ["Pinch the cell", "Swipe the cell right", "Tap the sheet tab"], "text", src=T)
q(4, "How do you select a whole column or row?", "Tap its heading", ["Double-tap any cell in it", "Swipe along it", "Pinch it"], src=T)
q(4, "How do you scroll quickly through a big sheet?", "Drag the scroll handle", ["Pinch repeatedly", "Tap the sheet tab", "Shake the phone"], src=T)
q(4, "How do you scroll around a sheet?", "Slide a finger up, down, left or right", ["Tilt the phone", "Press the volume keys", "Tap the corner of the grid"], src=T)
q(3, "How do you quickly select every cell with data in one direction?", "Flick the selection handle that way", ["Double-tap the sheet tab", "Swipe with three fingers", "Tap the Name Box twice"], src=T)
q(3, "How do you move cells, or a column or row?", "Tap and hold the selection, then drag it", ["Swipe it with two fingers", "Double-tap it and type the new address", "Pinch it and spread it elsewhere"], src=T)
q(3, "How do you resize a column?", "Drag the double line at its heading's edge", ["Pinch inside the column", "Double-tap a cell in it", "Rotate the phone"], src=T)
q(3, "On iPhone, how do you AutoFit a column to its contents?", "Double-tap the column heading", ["Tap and hold the heading", "Flick the selection handle", "Pinch the heading"], "text", src=T)
q(3, "On iPhone, how can you tell cells are ready to be moved?", "Dotted lines animate around them", ["They turn green", "The phone vibrates twice", "A Move button appears"], src=T)
q(3, "On Android, how do you hide the on-screen keyboard?", "Tap the Back key", ["Swipe the keyboard up", "Tap the sheet tab", "Shake the phone"], "text", src=T)
q(3, "On Android, how do you open a cell's menu (cut, copy, paste…)?", "Tap and hold the cell", ["Pinch the cell", "Swipe right on the cell", "Tap the column heading twice"], src=T)
q(3, "On iPhone, how do you open the cell menu (cut, copy, paste…)?", "Tap the selected cell", ["Pinch the cell", "Swipe up from the bottom", "Triple-tap the sheet tab"], src=T)
R = "Microsoft: Show or hide the ribbon on mobile devices"
q(4, "On a phone (iPhone or Android), how do you bring up the ribbon?", "Tap the Edit icon", ["Swipe down from the top", "Rotate the phone", "Tap and hold a cell"], src=R)
q(4, "On a phone, how do you hide the ribbon again?", "Tap the down arrow", ["Tap the Edit icon twice", "Shake the phone", "Swipe it left"], src=R)
q(3, "On an iPad, how do you show or hide the ribbon?", "Tap any tab, like Home", ["Tap the Edit icon", "Swipe up with three fingers", "Press the volume key"], src=R)
q(3, "On an Android tablet, how do you show or hide the ribbon?", "Tap the arrows at the top right", ["Tap the Edit icon", "Tap the sheet tab", "Double-tap the grid"], src=R)
q(3, "On a phone's ribbon, how do you change from Home to another tab?", "Tap the tab's name (Home) and pick another", ["Swipe the ribbon sideways", "Shake the phone", "Long-press the sheet tab"], src="Microsoft: Freeze panes in Excel for iOS")
F = "Microsoft: Freeze panes in Excel for iOS"
q(2, "On iPhone, where's Freeze Panes?", "Ribbon → Home → View, then scroll to Freeze Panes", ["Data → Freeze", "Insert → Lock Rows", "Long-press the row heading → Pin"], src=F)
q(2, "To freeze the top rows, which row do you select first?", "The row below the last row you want frozen", ["The last row you want frozen", "Row 1, always", "Any cell in column A"], src=F)
q(2, "To freeze columns, which column do you select first?", "The column to the right of the last one you want frozen", ["The last column you want frozen", "Column A, always", "The column you're editing"], src=F)
q(2, "How do you unfreeze panes on iPhone or iPad?", "View → Freeze Panes, then clear the ticked options", ["Shake to undo", "Close and reopen the file", "Tap the frozen row twice"], src=F)
q(3, "Why freeze the header row on a phone?", "So the headings stay in view as you scroll", ["So nobody can edit them", "To save battery", "To make the file smaller"], src="Good practice")
P = "Microsoft: Insert data from picture"
q(3, "Which feature turns a photo of a printed table into cells?", "Data from Picture", ["Flash Fill", "Quick Analysis", "Text to Columns"], "data", src=P)
q(3, "Where's Data from Picture in the phone app?", "Insert → Data from Picture", ["Data → Get Data → Camera", "Home → Paste → Photo", "File → Import"], "data", src=P)
q(2, "While framing a table for Data from Picture, what shows Excel has found it?", "A red border round the data", ["A green tick", "The phone vibrates", "The cells flash"], "data", src=P)
q(2, "Excel flags things it may have misread from the picture. What can you do with each?", "Ignore it or Edit it", ["Accept or Delete it", "Keep or Retake it", "Undo or Redo it"], "data", src=P)
q(2, "How do you finish Data from Picture and put the data in the grid?", "Tap Insert", ["Tap Save", "Tap Share", "Tap Refresh"], "data", src=P)
q(1, "In the Microsoft 365 app (rather than Excel), where's the photo-to-table tool?", "Actions → Image to Table", ["Create → Scan Table", "Insert → Data from Picture", "Files → Import Image"], "data", src=P)
q(1, "Data from Picture can read which of these languages' characters?", "Swedish", ["Japanese", "Arabic", "Greek"], "data", src=P)
q(1, "Image to Table finds errors. What does Open Anyway do?", "Opens the table in Excel so you fix them there", ["Ignores them all for good", "Retakes the photo", "Deletes the rows with errors"], "data", src=P)
C = "Microsoft: Use Cards View to work with table data on your phone"
q(3, "What does Cards View show?", "A table one row at a time, as cards", ["Each sheet as a card", "Charts as flash cards", "Formulas as cards"], "data", src=C)
q(3, "Cards View only works with…", "Excel tables", ["Charts", "PivotTables", "Ranges under 100 rows"], "data", src=C)
q(3, "How do you open Cards View?", "Tap a cell in a table, then the Cards View button", ["Swipe left on a sheet tab", "Insert → Cards", "Pinch the table"], "data", src=C)
q(2, "What happens when you tap a card?", "A detailed view of the whole row opens, ready to edit", ["The row is deleted", "The row is copied", "The card flips to show formulas"], "data", src=C)
q(2, "How do you add or delete rows in Cards View?", "The ⋯ menu on a card", ["Swipe the card away", "Shake the phone", "Pinch two cards together"], "data", src=C)
q(2, "Cards View has which two levels?", "A list of cards and a detailed view", ["Cards and charts", "Summary and PivotTable", "Grid and print preview"], "data", src=C)
q(2, "Your data is a plain range. What must you do before using Cards View?", "Turn it into a table", ["Sort it", "Freeze the top row", "Save it to the phone"], "data", src=C)
L = "Microsoft: Excel mobile app listing / Microsoft 365 mobile help"
q(3, "Free editing in the Excel mobile app is for screens up to…", "10.1 inches", ["7 inches", "12.9 inches", "15.6 inches"], "games", src=L)
q(2, "On a bigger tablet without a Microsoft 365 subscription, you can…", "View files, but not create or edit them", ["Edit, but not save", "Do nothing — the app won't open", "Edit only .csv files"], "games", src=L)
B = "Microsoft: Basic tasks using a screen reader with Excel"
q(4, "On iPhone, how do you start a new blank workbook?", "New → Blank workbook", ["File → Duplicate", "Insert → Sheet", "Long-press the app icon"], "games", src=B)
q(3, "How do you add a sheet on a phone?", "The Add sheet (+) button by the sheet tabs", ["Insert → Chart", "Shake the phone", "Swipe right past the last column"], "games", src=B)
q(3, "On Android, which button lists the workbook's sheets?", "Sheets", ["Tabs", "Pages", "Windows"], "games", src=B)
q(3, "On iPhone, which File option saves the workbook under a new name?", "Save a copy", ["Export PDF", "Duplicate sheet", "Rename sheet"], "games", src=B)
q(3, "On Android, Save as is in which menu?", "More options (⋮)", ["Home tab", "The Sheets button", "Long-press the file name"], "games", src=B)
q(3, "Saving a copy on iPhone, which place keeps it on the phone itself?", "On my iPhone", ["iCloud Mail", "Recent", "Shared with me"], "games", src=B)
q(3, "Saving a copy on Android, which place keeps it on the phone itself?", "This device", ["Recent", "Shared", "Downloads only"], "games", src=B)
q(3, "Printing from Excel on iPhone goes through…", "AirPrint", ["Bluetooth Print", "Print to OneNote", "A PDF only"], "games", src=B)
q(3, "Where's Number Format on a phone?", "Ribbon → Home → Number Format", ["Data → Number", "Long-press the cell → Number", "View → Number Format"], "text", src=B)
q(3, "Which screen reader does Excel work with on iPhone?", "VoiceOver", ["TalkBack", "Narrator", "JAWS"], "games", src=B)
q(3, "Which screen reader does Excel work with on Android?", "TalkBack", ["VoiceOver", "Narrator", "NVDA"], "games", src=B)
A = "Microsoft: Use AutoSum to sum numbers (Android)"
q(3, "On Android, how do you add a quick total under a column of numbers?", "Tap the cell below, tap AutoSum, tap Sum, tap the check mark", ["Shake the phone over the column", "Long-press the numbers and choose Add", "Type TOTAL in the cell"], "math", src=A)
q(3, "After picking AutoSum → Sum on Android, what confirms the formula?", "Tap the check mark", ["Tap the Back key", "Shake the phone", "Tap the sheet tab"], "math", src=A)
W = "Microsoft: What's new in Excel on mobile platforms"
q(3, "Which mobile feature finds a command when you describe what you want?", "Tell Me", ["Ask Excel", "Smart Lookup", "Quick Steps"], "games", src=W)
q(2, "On mobile, Formula AutoComplete suggests functions that match…", "Any part of the name, not just the start", ["Only the first letter", "Only functions you've used", "Only the most popular 20"], "math", src=W)
q(2, "Can Excel on a phone open OpenDocument (.ods) spreadsheets?", "Yes, to view them", ["No, never", "Only after converting on a PC", "Only on Android tablets"], "games", src=W)
q(2, "What's the Draw tab for on mobile?", "Writing and drawing on the sheet with a finger or pen", ["Drawing borders only", "Making charts by hand", "Sketching shapes into formulas"], "games", src=W)
q(3, "Can you add comments in the phone app?", "Yes — view, add and delete them", ["Only read them", "Only on tablets", "No, comments are desktop-only"], "text", src=W)
q(3, "Where does AutoSave keep your changes on mobile?", "In the cloud copy (OneDrive or SharePoint)", ["In a hidden sheet", "In the phone's photos", "In an email draft"], "games", src=W)
q(3, "Can VBA macros run in Excel on iPhone or iPad?", "No — macros aren't supported there", ["Yes, all of them", "Only recorded ones", "Only if signed"], "games", src="Microsoft: Excel for iPad/iPhone feature support")
q(2, "You open a macro-enabled .xlsm on your phone. What about its macros?", "They stay in the file, but don't run", ["They're deleted", "They run as normal", "The file won't open"], "games", src="Microsoft: Excel for iPad/iPhone feature support")
q(3, "Which button beside the formula bar opens the list of functions by category?", "fx", ["Σ", "=", "⋯"], "math", src="Excel mobile app")
q(3, "In the phone's function list, what does Recently Used show?", "The functions you've used lately", ["The newest functions Microsoft added", "Your most-used cells", "Recently opened files"], "math", src="Excel mobile app")
q(4, "Where's Undo in the phone app?", "The Undo arrow at the top of the screen", ["Shake the phone", "Long-press the formula bar", "Swipe left with two fingers"], "text", src="Excel mobile app")
q(3, "How do you share a workbook from the phone app?", "The Share button — invite people or copy a link", ["Screenshot it", "Insert → Share sheet", "Save it to the photos"], "games", src="Excel mobile app")
q(2, "Can people edit a workbook at the same time as you on a phone?", "Yes, if it's saved in OneDrive or SharePoint", ["No, phones lock the file", "Only one at a time on mobile", "Only on Android"], "games", src="Microsoft: Collaborate on Excel workbooks")
q(3, "To save to OneDrive from the phone app you need to…", "Sign in with a Microsoft account", ["Plug the phone into a PC", "Turn on Bluetooth", "Buy a Microsoft 365 plan"], "games", src="Microsoft: Basic tasks using a screen reader with Excel")
q(3, "With a keyboard on an iPad, Excel's shortcuts mostly follow…", "The Mac ones (with the Command key)", ["The Windows ones (with Ctrl)", "Android's", "None — keyboards aren't supported"], "games", src="Microsoft: Keyboard shortcuts in Excel")
q(3, "With a keyboard on an iPad, which shortcut copies?", "Command+C", ["Ctrl+Insert", "Alt+C", "Option+C"], "text", src="Microsoft: Keyboard shortcuts in Excel")
q(2, "On iPad, how do you fill a series down?", "Tap a cell, tap Fill, then drag the fill arrows", ["Shake the phone", "Pinch down the column", "Double-tap the column heading"], "math", src="Microsoft: Fill data automatically (iPad)")
q(3, "Where's Sort & Filter on a phone?", "Ribbon → Home → Sort & Filter", ["Long-press a heading → Sort", "Insert → Sort", "View → Filter"], "data", src="Excel mobile app")
q(3, "With filters on, how do you filter a column on a phone?", "Tap the arrow on its header", ["Pinch the column", "Long-press any cell", "Swipe the header up"], "data", src="Excel mobile app")
q(3, "Where do you add a chart on a phone?", "Ribbon → Insert → Chart", ["Long-press the data → Chart", "Home → Chart", "View → Chart"], "data", src="Excel mobile app")
q(3, "Where do you add a table on a phone?", "Ribbon → Insert → Table", ["Home → Format as Grid", "Data → Make Table", "Long-press → Table"], "data", src="Excel mobile app")
q(3, "Where's Wrap Text on a phone?", "Ribbon → Home → Wrap Text", ["Long-press → Fit", "Insert → Wrap", "View → Wrap"], "text", src="Excel mobile app")
q(3, "Where's Merge & Center on a phone?", "Ribbon → Home → Merge & Center", ["Insert → Merge", "Data → Combine", "View → Merge"], "text", src="Excel mobile app")
q(3, "Where do you add a picture from your photos on a phone?", "Ribbon → Insert → Pictures", ["Home → Paste → Photo", "Data → From Picture", "View → Pictures"], "games", src="Excel mobile app")
q(4, "A cell shows ##### on your phone. What's wrong?", "The column's too narrow for the number", ["The formula has an error", "The file didn't load", "The cell's protected"], "math", src="Microsoft: How to correct a ##### error")
q(4, "Do formulas work the same in the phone app as on a PC?", "Yes — same functions, same results", ["No, mobile has its own formulas", "Only SUM works on mobile", "They only calculate when you save"], "math", src="Good practice")
q(4, "What should you type first to start a formula on the phone keyboard?", "=", ["+ only", "fx", "#"], "math", src="Good practice")
q(3, "You open a long table on your phone. What helps most to read it?", "Freeze the header row and zoom to fit", ["Hide the gridlines", "Turn on page breaks", "Delete the empty columns"], src="Good practice")
q(3, "What layout is easiest to use on a phone?", "A narrow table with the key columns first", ["A very wide sheet with many columns", "Lots of merged cells", "Text in tiny fonts"], src="Good practice")
q(3, "Why avoid merged cells in a sheet people use on phones?", "They break selecting, sorting and filtering", ["Phones can't show them", "They make the file huge", "They hide formulas"], "text", src="Good practice")
q(2, "Where should a dashboard's key numbers go for phone readers?", "Top-left, so they show without scrolling", ["Bottom-right", "On a hidden sheet", "In cell comments"], src="Good practice")
q(2, "Why are tables good for phone users?", "Filters are ready to tap and Cards View works", ["They're smaller files", "They can't be edited by accident", "They load offline only"], "data", src="Good practice")
q(2, "Typing long formulas on a phone is fiddly. What helps most?", "Named ranges and short, clear names", ["Typing in capitals", "Turning off AutoComplete", "Using only F-keys"], "math", src="Good practice")
q(2, "You need to enter a lot of rows on the go. Which is easiest on a phone?", "A table in Cards View (or a Microsoft Form feeding the sheet)", ["Typing straight into a wide sheet", "Recording a macro", "Emailing yourself the numbers"], "data", src="Good practice")
q(2, "Data validation drop-down lists on a phone…", "Show a list to tap, so there's less typing", ["Don't work at all", "Only work offline", "Turn into comments"], "data", src="Microsoft: What's new in Excel on mobile platforms")
q(2, "Conditional formatting made on a PC shows on a phone?", "Yes", ["No, it's stripped out", "Only colour scales", "Only after a refresh"], "data", src="Microsoft: What's new in Excel on mobile platforms")
q(2, "A PivotTable made on a PC opens on a phone?", "Yes, you can view it", ["No, it turns into values", "No, the file won't open", "Only as a picture"], "data", src="Microsoft: What's new in Excel on mobile platforms")
q(2, "Which file type keeps a workbook editable for others on their phones?", ".xlsx in OneDrive or SharePoint", [".pdf", "A screenshot", ".csv in an email"], "games", src="Good practice")
q(1, "You want a sheet to look good printed from a phone. What should you set on a PC first?", "The print area and page setup", ["Freeze panes", "A slicer", "Data validation"], "games", src="Good practice")
q(1, "Why keep phone-facing sheets free of very long formulas in single cells?", "They're hard to read and edit in a small formula bar", ["Phones can't calculate them", "They stop AutoSave", "They break Cards View"], "math", src="Good practice")
q(1, "A colleague can't see your new sheet on their phone. What's the likely cause?", "The file hasn't synced (or they have an old copy)", ["Phones show one sheet only", "Sheets over 100 rows are hidden", "Their screen's too small"], "games", src="Good practice")
q(1, "Which feature lets you see how a phone user will see a sheet, on your PC?", "Excel for the web in a narrow window (or the app on your phone)", ["Page Break Preview", "Print Preview", "Normal view"], "games", src="Good practice")
q(1, "On a phone, which is quicker than typing to enter a date?", "Shortcuts like =TODAY() or picking from a validation list", ["Typing the month in words", "Copying it from an email", "Typing it as text with quotes"], "time", src="Good practice")
q(1, "You want a phone user to only see a summary. What's the simplest way?", "Put the summary on the first sheet and keep it narrow", ["Protect every other cell", "Use very small fonts", "Hide all gridlines"], src="Good practice")
q(1, "Why use slicers on a dashboard meant for phones?", "They're big buttons that are easy to tap", ["They work offline only", "They hide the data", "They shrink the file"], "data", src="Good practice")
q(1, "A phone user complains they keep typing over formulas. What helps?", "Lock the formula cells and protect the sheet", ["Use bigger fonts", "Turn off AutoSave", "Add more colours"], src="Good practice")
q(1, "Hyperlinks to other sheets on a phone…", "Make navigation a single tap", ["Don't work on mobile", "Slow the file down", "Open the browser only"], src="Good practice")

# ========================= Function picker categories =======================
# One Mobile question per Knowledge check: which category of the function
# list (fx) is a function under? Categories from Microsoft's function lists.
PICKER = """SUM AVERAGE COUNT COUNTA COUNTIF COUNTIFS SUMIF SUMIFS MAX MIN MEDIAN LARGE
ROUND INT MOD ABS RAND SEQUENCE
IF IFS IFERROR AND OR SWITCH
VLOOKUP XLOOKUP INDEX MATCH FILTER SORT UNIQUE HYPERLINK
TODAY NOW DATE WEEKDAY NETWORKDAYS EOMONTH
LEFT LEN TRIM TEXTJOIN TEXT FIND SUBSTITUTE
PMT NPV
ISBLANK ISNUMBER
CONVERT""".split()
# The function list's category names, and which others each is easily
# mistaken for (the wrong answers are picked from these).
CAT = {"Math and trigonometry": "Math & Trig", "Statistical": "Statistical", "Lookup and reference": "Lookup & Reference",
       "Logical": "Logical", "Date and time": "Date & Time", "Text": "Text", "Financial": "Financial",
       "Information": "Information", "Engineering": "Engineering"}
NEAR = {
    "Math & Trig": ["Statistical", "Logical", "Engineering", "Financial"],
    "Statistical": ["Math & Trig", "Logical", "Information", "Financial"],
    "Lookup & Reference": ["Logical", "Information", "Text", "Statistical"],
    "Logical": ["Information", "Lookup & Reference", "Math & Trig", "Text"],
    "Date & Time": ["Text", "Math & Trig", "Financial", "Information"],
    "Text": ["Lookup & Reference", "Information", "Logical", "Date & Time"],
    "Financial": ["Math & Trig", "Statistical", "Engineering", "Date & Time"],
    "Information": ["Logical", "Lookup & Reference", "Text", "Statistical"],
    "Engineering": ["Math & Trig", "Statistical", "Information", "Financial"],
}

def picker_rows():
    """The picker questions: (function, tier, skill, titan, question, answer,
    [three wrong answers], what it does). Read from edu-functions.js (run from
    the repo root); the wrong answers are fixed by a seeded shuffle."""
    import json, random, re
    js = open("edu-functions.js").read()
    funcs = {r[0]: r for r in json.loads("[" + re.search(r"const EDU_FUNCS = \[(.*?)\];", js, re.S).group(1).strip().rstrip(",") + "]")}
    rng = random.Random(11)
    out = []
    for name in PICKER:
        f = funcs[name]
        cat = CAT[f[6]]
        out.append((name, f[3], f[1], f[2], f"In the function list (fx), which category is {name} under?", cat, rng.sample(NEAR[cat], 3), f[4]))
    return out
