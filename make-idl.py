import yaml
import os
import re
import subprocess
import sys

with open("commontype.yaml") as yaml_file:
    commontype = yaml.load(yaml_file, Loader=yaml.FullLoader)

if not os.path.exists("idl"):
    os.mkdir("idl")

done = {}


def dumpATable(table, f):
    if table not in commontype:
        print("Table %s not found" % table)
        print(sorted(commontype.keys()))
        sys.exit(1)
    todo = []
    if table in done:
        return
    if "union" in commontype[table]:
        union = " or ".join(commontype[table]["union"])
        f.write(f"typedef ({union}) {table};\n")
        todo.extend(commontype[table]["union"])
    else:
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
            f.write(f'\tattribute {el["type"]} {el["name"]}')
            if "value" in el:
                f.write(f' /* =={el["value"]} */')
            if "to" in el:
                offsettype2 = offsettype = el["to"]
                if offsettype.endswith("[]"):
                    offsettype2 = offsettype[:-2]
                if offsettype2 not in commontype:
                    print("Undefined offset type %s!" % offsettype2)
                    sys.exit(1)
                if offsettype not in done and ("status" not in commontype[offsettype2]
                    or commontype[offsettype2]["status"] != "shared"
                ):
                    todo.append(offsettype2)
                f.write(f' /* {offsettype} */')
            f.write(';\n')
        f.write("};\n")
    done[table] = True
    for t in todo:
        dumpATable(t, f)


def dumpAFile(filename, table):
    print("Writing %s" % filename)
    with open(filename, "w") as f:
        f.write("<pre class='idl'>\n")
        dumpATable(table, f)
        f.write("</pre>\n")


o = subprocess.run(["grep", "-ro", "path: idl/.*md", "."], capture_output=True)
for line in sorted(o.stdout.decode().split("\n")):
    if "*" in line:
        continue
    if "/" not in line:
        continue
    m = re.match(r".*(idl/(.*)\.md)", line)
    dumpAFile(m[1], m[2])
