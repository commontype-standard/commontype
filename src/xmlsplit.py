#!/usr/bin/python
import argparse
from lxml import etree
from os.path import dirname, join

parser = argparse.ArgumentParser(description="Split an XML file by XPath")
parser.add_argument("file", metavar="FILE", type=str, help="file to process")

doctype = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
args = parser.parse_args()
mydoc = etree.parse(open(args.file, "r"))
counters = {}
roles = [
    "xml-representation",
    "implementation",
    "compiler",
    "decompiler",
    "validation",
    "test-suite",
]
predicate = ".//section[%s]" % " or ".join(['@role="%s"' % r for r in roles])
print(predicate)


def genfilename(role):
    if not role in counters:
        counters[role] = 0
    counters[role] += 1
    return join(dirname(args.file), "%s-%i.xml" % (role, counters[role]))


for elem in mydoc.xpath(predicate):
    parent = elem.getparent()
    parent_index = list(parent).index(elem)
    newfilename = genfilename(elem.get("role"))
    parent.remove(elem)
    new_elem = etree.Element(
        "{http://www.w3.org/2001/XInclude}include",
        attrib={"href": newfilename},
        nsmap={"xi": "http://www.w3.org/2001/XInclude"},
    )
    new_elem.tail = "\n"
    parent.insert(parent_index, new_elem)
    if parent[parent_index - 1].tag is etree.Comment:
        parent.remove(parent[parent_index - 1])
    print("Writing %s" % newfilename)
    with open(newfilename, "wb") as f:
        f.write(
            etree.tostring(elem, pretty_print=True, encoding="UTF-8", doctype=doctype,)
        )


etree.indent(mydoc, space="  ")
with open(args.file, "wb") as f:
    f.write(
        etree.tostring(mydoc, pretty_print=True, encoding="UTF-8", doctype=doctype,)
    )
