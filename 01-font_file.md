<h3 id="font-file-structure">Font File Structure</h3>

A font file is represented as a collection of *tables*. The term <dfn>table</dfn> is used in two ways when discussing the font file. Generally, a "table" is equivalent to a C `struct`, a data structure with a number of fields; specifically, a table is also used in the sense of a database table, a top-level structure potentially containing a number of related sets of information. (For example, "the `cname` table".) In this second sense, a table may contain other tables; these contained tables are often referred to as "subtables".

<h4>Data types</h4>

* Data in the font file is stored in big-endian byte order. All types in this specification therefore refer to big-endian types.

<pre class="idl">
    typedef byte int8;
    typedef unsigned short USHORT;
    typedef short SHORT;
    typedef unsigned short F2DOT14;
    typedef unsigned long VERSION;
    typedef unsigned short NameID;
    typedef unsigned short Offset16;
    typedef long LONG;
    typedef unsigned long ULONG;
    typedef unsigned long Offset32;
    typedef byte[] Tag;
</pre>

* An `F2DOT14` type is a two byte fixed-point number with 14 fractional bits.
* Tables within the font file frequently use offset values (often measured from the beginning of the table containing the offset) to denote the location of their subtables. The `Offset16` and `Offset32` types refer to two-byte and four-byte offset descriptors respectively.
* A `Tag` is a four-byte character string referring to an entry in a tag registry. Tag registries exist for top-level tables, languages, scripts, features, baselines, and variable font axes.
* A `VERSION` consists of two bytes, each interpreted as an unsigned integer. The first describes the major version number of a table and the second the minor version number.

<h4 id="glyph-representation-formats"><dfn>Glyph representation formats</dfn></h4>

A font file may represent glyph data in a number of formats. A font file must have exactly one <dfn>primary outline representation format</dfn>, which must be either:

* TrueType outlines, stored in the [=glyf table=].
* CFF version 1 outlines, (sometimes informally called "PostScript outlines") stored in the [=CFF table=].
* CFF version 2 outlines, stored in the [=CFF2 table=].

A font file may also contain data in one or more of *secondary outline representation formats*. The only secondary outline representation format currently supported is Scalable Vector Graphics, stored in the [=SVG table=].

Additionally, the font file may contain one or more binary representations of the glyph data. The binary glyph representations available are:

* Monochrome bitmaps stored in the [=EBDT table=] and [=EBLC table=].
* Color bitmaps stored in the [=CBDT table=] and [=CBLC table=].

<h4 id="table-directory"><dfn>Table Directory</dfn></h4>

The font file begins with the table directory, which locates the remainder of the tables in the file.

<pre class=include>path: idl/TableDirectory.md</pre>

<dl dfn-type=attribute dfn-for=TableDirectory>
  <dt><dfn>sfntVersion</dfn></dt>
  <dd>File magic number. Must be `0x00010000` if the font file's [=primary outline representation format=] is TrueType outlines, or the four bytes `OTTO` if the primary outline representation format is CFF outlines.</dd>
  <dt><dfn>numTables</dfn></dt>
  <dd>The number of top-level tables in the font file.</dd>
  <dt><dfn>searchRange</dfn></dt>
  <dd>The maximum number of nodes in a binary search tree. </dd>
  <dt><dfn>entrySelector</dfn></dt>
  <dd>The maximum depth of a binary search tree. </dd>
  <dt><dfn>rangeShift</dfn></dt>
  <dd>Nobody really knows what this is.</dd>
</dl>

<dl dfn-type=attribute dfn-for=TableDirectoryEntry>
  <dt><dfn>tableTag</dfn></dt>
  <dd>The four-character tag name for this table, from the [=table tag registry=].</dd>
  <dt><dfn>checksum</dfn></dt>
  <dd>The table checksum. See below.</dd>
  <dt><dfn>offset</dfn></dt>
  <dd>Byte position of the table, measured from the start of the {{TableDirectory}} table.
</dl>

<h5 id="TableDirectory.in-prod">Implementation notes for font producers</h5>

* Tables must aligned to a four byte boundary.

* Table lengths must be a multiple of four bytes. Zero padding should be added to the end to make up an integral multiple if necessary.

* Table checksums are computed using the following <dfn>checksum algorithm</dfn> (in Python):

<pre>
def calcChecksum(table):
    # Zero-pad table to four-byte boundary
    while len(table) % 4 > 0:
        table += b"\0"

    # Calculate the unsigned sum of all four-byte values
    value = 0
    for i in range(0, len(table), 4):
        long = struct.unpack(">L", table[i:i+4])
        value = (value + long) & 0xffffffff
    return value
</pre>

* The [=head table=] is modified after its checksum is computed. Writing the font checksum must be done in the following sequence:
    * Fill in the values of all tables. In the `head` table, set the `checkSumAdjustment` to 0.
    * Calculate the checksum for all tables and fill in the {{TableDirectoryEntry}} structures.
    * Calculate the `checkSumAdjustment` as described in the [=head table=] chapter, and insert this into the table.

* Given a value *maxPower*, which is defined as being the largest power of two less than or equal to the number of tables, {{TableDirectory/searchRange}} is set to 16 times *maxPower*, the {{TableDirectory/entrySelector}} is set to the base 2 logarithm of `maxPower`, and the {{TableDirectory/rangeShift}} is `numTables*16` minus the `searchRange`.

This can be implemented with the following Python code:

<pre>
def maxPowerOfTwo(x):
    exponent = 0
    while x:
        x = x >> 1
        exponent = exponent + 1
    return max(exponent - 1, 0)

exponent = maxPowerOfTwo(numTables)
searchRange = (2 ** exponent) * 16
entrySelector = exponent
rangeShift = max(0, numTables * 16 - searchRange)
</pre>

<div class="example">
Here is an example of filling in the header information for a font file with 11 tables according to the formal definition. The largest power of 2 less than 11 is 8, so:

<table>
    <tr><th>numTables</th><td>11</td><td></td></tr>
    <tr><th>searchRange</th><td>128</td><td>maxPower * 16</td></tr>
    <tr><th>entrySelector</th><td>3</td><td>log(maxPower)/log(2)</td></tr>
    <tr><th>rangeShift</th><td>483</td><td>11 * 16 - 128</td> </tr>
</table>
</div>

<h5 id="TableDirectory.in-cons">Implementation notes for font consumers</h5>

* When validating table checksums, the [=head table=] must be treated as a special case, and its `checkSumAdjustment` value set to four zero bytes for the purposes of checksumming. Font consumers should not assume that the table length will be a multiple of four, and should use the above checksumming algorithm which adds zero padding to the table data.

* The {{TableDirectory/searchRange}}, {{TableDirectory/entrySelector}}, and {{TableDirectory/rangeShift}} fields should be ignored by font consumers. There is no requirement to use binary tree search to locate the tables, but if a binary tree is used, these values should be recomputed from the {{TableDirectory/numTables}} field.

<h4>Font collection files</h4>
