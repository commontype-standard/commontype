import json
import sys
import struct
from pprint import pprint

basetypes = {"USHORT": ">H", "F2DOT14": (">H", lambda x: x / (1 << 14))}


def consume(fmt, data, pos):
    if isinstance(fmt, str):
        (output,) = struct.unpack_from(fmt, data, offset=pos)
        pos += struct.calcsize(fmt)
        return output, pos
    if isinstance(fmt, tuple):
        (output,) = struct.unpack_from(fmt[0], data, offset=pos)
        pos += struct.calcsize(fmt[0])
        return fmt[1](output), pos


with open("datastructures.json") as json_file:
    commontype = json.load(json_file)

table = sys.argv[1]
if table not in commontype:
    print("Table %s not found" % table)
    print(sorted(commontype.keys()))
    sys.exit(1)

data = sys.stdin.buffer.read()


def readATable(table, data, pos=0):
    structure = commontype[table]["fields"]
    output = {}
    doOffsets = []
    for field in structure:
        fType = field["type"]
        fName = field["name"]
        if fType in basetypes:
            fmt = basetypes[fType]
            output[fName], pos = consume(fmt, data, pos)
        elif fType in commontype:  # Bare field singly embedded
            output[fName], pos = readATable(fType, data, pos)
        elif fType.endswith("[]"):
            fType = fType[:-2]
            counter = field["count"]
            output[fName] = []
            for i in range(output[counter]):
                rv = "Dummy"
                rv, pos = readATable(fType, data, pos)
                output[fName].append(rv)
    return output, pos


out, _ = readATable(table, data)
pprint(out)
