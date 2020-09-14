#!/usr/bin/python3
# Structure to JSON

from fontTools.ttLib.tables.otData import otData
import json
import sys

typemap = {
	"uint16": "USHORT",
	"Offset": "Offset16",
	"LOffset": "Offset32"
}

table = sys.argv[1]
ot = dict(otData)
if table not in ot:
    print("Table not found")
    print(sorted(ot.keys()))
    sys.exit(1)
fields = []
for line in ot[table]:
	mapped_type = line[0]
	name = line[1]
	if line[0] in typemap:
		mapped_type = typemap[line[0]]
	if mapped_type == "struct":
		mapped_type = name
	name = name[0].lower() + name[1:]
	field = {"type": mapped_type, "name": name}
	if line[2]:
		field["count"] = line[2]
		field["type"] = mapped_type + "[]"
		field["name"] = name + "s"
	if line[3]:
		field["condition"] = line[3]
	fields.append(field)

obj = { table: { "fields": fields } }
print(json.dumps(obj, sort_keys=True, indent=2))
