from prettytable import PrettyTable


table = PrettyTable()

table.field_names = ["Name", "Age", "Gender"]
table.add_row(["Mark", 20, "Male"])
table.add_row(["Markdawdawd", 20, "Male"])
table.add_row(["Markadw", 20, "Male"])
table.add_row(["Markawdawdawd", 20, "Male"])
table.add_row(["Markadw", 20, "Male"])
table.add_row(["Markw", 20, "Male"])

print(table)