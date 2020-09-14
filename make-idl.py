import yaml
import os
import re
import subprocess
import sys

with open("commontype.yaml") as yaml_file:
    commontype = yaml.load(yaml_file, Loader=yaml.FullLoader)

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
        if "to" in el:
            offsettype = el["to"]
            if offsettype not in commontype:
                print("Undefined offset type %s!" % offsettype)
                sys.exit(1)
            if offsettype not in done and ("status" not in commontype[offsettype]
                or commontype[offsettype]["status"] != "shared"
            ):
                todo.append(offsettype)
            f.write(f'\tattribute {el["type"]} {el["name"]} /* {offsettype} */;\n')
        else:
            f.write(f'\tattribute {el["type"]} {el["name"]};\n')

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
