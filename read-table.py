import yaml
import sys
import struct
from pprint import pprint
from time import strftime, gmtime
import calendar


epoch_diff = calendar.timegm((1904, 1, 1, 0, 0, 0, 0, 0, 0))

basetypes = {
"USHORT": ">H",
"VERSION": (">HH", lambda x: x[0] + x[1]/(10**len(str(x[1])))),
"F2DOT14": (">H", lambda x: x[0] / (1 << 14)),
"LONGDATETIME": (">Q", lambda x: strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(x[0]+epoch_diff))),
"ULONG": ">L",
"FWORD": ">h",
"SHORT": ">h",
}


def consume(fmt, data, pos):
    if isinstance(fmt, str):
        output = struct.unpack_from(fmt, data, offset=pos)
        pos += struct.calcsize(fmt)
        return output[0], pos
    if isinstance(fmt, tuple):
        output = struct.unpack_from(fmt[0], data, offset=pos)
        pos += struct.calcsize(fmt[0])
        return fmt[1](output), pos


with open("commontype.yaml") as yaml_file:
    commontype = yaml.load(yaml_file, Loader=yaml.FullLoader)

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
        else:
            print("Unknown type %s" % fType)
            sys.exit(1)
    return output, pos


out, _ = readATable(table, data)
pprint(out)
