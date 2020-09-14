import yaml
import sys
import struct
from pprint import pprint
from time import strftime, gmtime
import calendar


epoch_diff = calendar.timegm((1904, 1, 1, 0, 0, 0, 0, 0, 0))

basetypes = {
    "USHORT": ">H",
    "Offset32": ">L",
    "VERSION": (">HH", lambda x: x[0] + x[1] / (10 ** len(str(x[1])))),
    "F2DOT14": (">H", lambda x: x[0] / (1 << 14)),
    "FIXED": (">H", lambda x: x[0] / (1 << 8)),
    "Tag": (">cccc", lambda x: "".join([g.decode() for g in x])),
    "LONGDATETIME": (
        ">Q",
        lambda x: strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(x[0] + epoch_diff)),
    ),
    "LONG": ">l",
    "ULONG": ">L",
    "FWORD": ">h",
    "SHORT": ">h",
}

trickyFields = {
    ("hmtxTable", "hMetrics"): lambda f, d, p, o: (0, p),
    ("hmtxTable", "leftSideBearings"): lambda f, d, p, o: (0, p),
    ("postTableVersion20", "names"): lambda f, d, p, o: ([], p),
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

data = sys.stdin.buffer.read()


def readAField(field, data, pos, tableSoFar):
    fType = field["type"]
    if fType in basetypes:
        fmt = basetypes[fType]
        output, pos = consume(fmt, data, pos)
    elif fType in commontype:  # Bare field singly embedded
        output, pos = readATable(fType, data, pos)
    elif fType.endswith("[]"):
        fType = fType[:-2]
        if not "count" in field:
            print(field["name"] + " is tricky but is not in my list of tricky fields")
            sys.exit(1)
        counter = field["count"]
        output = []
        for i in range(tableSoFar[counter]):
            rv, pos = readATable(fType, data, pos)
            output.append(rv)
    else:
        print("Unknown type %s" % fType)
        sys.exit(1)
    return output, pos


def readATable(table, data, pos=0):
    # Format switching header
    if "union" in commontype[table]:
        origtable = table
        table = None
        for t in commontype[origtable]["union"]:
            firstField = commontype[t]["fields"][0]
            assert "value" in firstField
            expected = firstField["value"]
            got, _ = readAField(firstField, data, pos, {})
            if expected == got:
                table = t
                break
        if not table:
            print("No table format matched for %s at position %i" % (origtable, pos))
            sys.exit(1)

    structure = commontype[table]["fields"]
    output = {}
    doOffsets = []
    for field in structure:
        if (table, field["name"]) in trickyFields:
            output[field["name"]], pos = trickyFields[(table, field["name"])](
                field, data, pos, output
            )
        else:
            output[field["name"]], pos = readAField(field, data, pos, output)
    return output, pos


if len(sys.argv) > 1:
    table = sys.argv[1]
    if table not in commontype:
        print("Table %s not found" % table)
        print(sorted(commontype.keys()))
        sys.exit(1)
    out, _ = readATable(table, data)
    pprint(out)
else:
    fdir, pos = readATable("TableDirectory", data)
    output = {}
    entries = [(x, x["tableTag"] + "Table") for x in fdir["entries"]]
    entries = filter(lambda x: x[1] in commontype, entries)
    for entry, tablename in entries:
        output[entry["tableTag"]], _ = readATable(tablename, data, pos=entry["offset"])
    pprint(output)
