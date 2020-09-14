import json
import os
import re
import subprocess
import sys

with open("datastructures.json") as json_file:
    commontype = json.load(json_file)

if not os.path.exists("idl"):
    os.mkdir("idl")


def dumpATable(table, done, f):
    if table not in commontype:
        print("Table %s not found" % table)
        print(sorted(commontype.keys()))
        sys.exit(1)
    todo = []
    f.write("interface %s {\n" % table)
    for el in commontype[table]["fields"]:
        f.write(f'\tattribute {el["type"]} {el["name"]};\n')
        basetype = el["type"].replace("[]", "")
        if (
            basetype in commontype
            and basetype not in done
            and (
                "status" not in commontype[basetype]
                or commontype[basetype]["status"] != "shared"
            )
        ):
            todo.append(basetype)
    f.write("};\n")
    done[table] = True
    for t in todo:
        dumpATable(t, done, f)


def dumpAFile(filename, table):
    print("Writing %s" % filename)
    with open(filename, "w") as f:
        f.write("<pre class='idl'>\n")
        done = {}
        dumpATable(table, done, f)
        f.write("</pre>\n")


o = subprocess.run(["grep", "-hro", "path: idl/.*md", "."], capture_output=True)
for line in o.stdout.decode().split("\n"):
    if "*" in line:
        continue
    if "/" not in line:
        continue
    m = re.match(r".*(idl/(.*)\.md)", line)
    dumpAFile(m[1], m[2])