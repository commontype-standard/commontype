import json
import sys

with open('datastructures.json') as json_file:
    data = json.load(json_file)

table = sys.argv[1]
if not table in data:
	print("Table %s not found" % table)
	print(sorted(data.keys()))
	sys.exit(1)

print("<pre rel='idl'>")

def dumpATable(table, done):
	todo = []
	print("interface %s {" % table)
	for el in data[table]:
		print(f'\tattribute {el["type"]} {el["name"]};')
		basetype = el["type"].replace("[]","")
		if basetype in data and basetype not in done:
			todo.append(basetype)
	print("};")
	done[table] = True
	for t in todo:
		dumpATable(t, done)

done = {}
dumpATable(table, done)
print("</pre>")
