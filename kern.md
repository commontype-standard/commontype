# kern - Kerning

## Overview

### Specification

Note: Apple has extended the definition of the [kern](#chapter.kern)
table to provide additional functionality. The Apple extensions are not
supported on Windows. Fonts intended for cross-platform use or for the
Windows platform in general should conform to the [kern](#chapter.kern)
table format specified here.

The kerning table contains the values that control the intercharacter
spacing for the glyphs in a font. There is currently no system level
support for kerning (other than returning the kern pairs and kern
values). OpenType fonts containing CFF outlines are not supported by the
[kern](#chapter.kern) table and must use the [GPOS](#chapter.GPOS)
OpenType Layout table.

Each subtable varies in format, and can contain information for vertical
or horizontal text, and can contain kerning values or minimum values.
Kerning values are used to adjust inter-character spacing, and minimum
values are used to limit the amount of adjustment that the scaler
applies by the combination of kerning and tracking. Because the
adjustments are additive, the order of the subtables containing kerning
values is not important. However, tables containing minimum values
should usually be placed last, so that they can be used to limit the
total effect of other subtables.

The kerning table in the OpenType font file has a header, which contains
the format number and the number of subtables present, and the subtables
themselves.

| Type   | Name    | Description                               |
| ------ | ------- | ----------------------------------------- |
| USHORT | version | Table version number (starts at 0)        |
| USHORT | nTables | Number of subtables in the kerning table. |

Kerning subtables will share the same header format. This header is used
to identify the format of the subtable and the kind of information it
contains:

| Type   | Name     | Description                                               |
| ------ | -------- | --------------------------------------------------------- |
| USHORT | version  | Kern subtable version number                              |
| USHORT | length   | Length of the subtable, in bytes (including this header). |
| USHORT | coverage | What type of information is contained in this table.      |

The coverage field is divided into the following sub-fields, with sizes
given in bits:

<table>
<thead>
<tr class="header">
<th>Type</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>1</td>
<td>1 if table has horizontal data, 0 if vertical.</td>
</tr>
<tr class="even">
<td>1</td>
<td>1</td>
<td>If this bit is set to 1, the table has minimum values. If set to 0, the table has kerning values.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>1</td>
<td><p>If set to 1, kerning is perpendicular to the flow of the text.</p>
<p>If the text is normally written horizontally, kerning will be done in the up and down directions. If kerning values are positive, the text will be kerned upwards; if they are negative, the text will be kerned downwards.</p>
<p>If the text is normally written vertically, kerning will be done in the left and right directions. If kerning values are positive, the text will be kerned to the right; if they are negative, the text will be kerned to the left.</p>
<p>The value 0x8000 in the kerning data resets the cross-stream kerning back to 0.</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>1</td>
<td>If this bit is set to 1 the value in this table should replace the value currently being accumulated.</td>
</tr>
<tr class="odd">
<td>4-7</td>
<td>4</td>
<td>Reserved. This should be set to zero.</td>
</tr>
<tr class="even">
<td>8-15</td>
<td>8</td>
<td>Format of the subtable. Only formats 0 and 2 have been defined. Formats 1 and 3 through 255 are reserved for future use.</td>
</tr>
</tbody>
</table>

## Format 0

### Specification

This is the only format that will be properly interpreted by Windows and
OS/2.

This subtable is a sorted list of kerning pairs and values. The list is
preceded by information which makes it possible to make an efficient
binary search of the list:

| Type   | Name          | Description                                                                                                                                                                                                                                                                       |
| ------ | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USHORT | nPairs        | This gives the number of kerning pairs in the table.                                                                                                                                                                                                                              |
| USHORT | searchRange   | The largest power of two less than or equal to the value of nPairs, multiplied by the size in bytes of an entry in the table.                                                                                                                                                     |
| USHORT | entrySelector | This is calculated as log2 of the largest power of two less than or equal to the value of nPairs. This value indicates how many iterations of the search loop will have to be made. (For example, in a list of eight items, there would have to be three iterations of the loop). |
| USHORT | rangeShift    | The value of nPairs minus the largest power of two less than or equal to nPairs, and then multiplied by the size in bytes of an entry in the table.                                                                                                                               |

This is followed by the list of kerning pairs and values. Each has the
following format:

| Type   | Name  | Description                                                                                                                                                                                            |
| ------ | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| USHORT | left  | The glyph index for the left-hand glyph in the kerning pair.                                                                                                                                           |
| USHORT | right | The glyph index for the right-hand glyph in the kerning pair.                                                                                                                                          |
| FWORD  | value | The kerning value for the above pair, in FUnits. If this value is greater than zero, the characters will be moved apart. If this value is less than zero, the character will be moved closer together. |

The left and right halves of the kerning pair make an unsigned 32-bit
number, which is then used to order the kerning pairs numerically.

A binary search is most efficiently coded if the search range is a power
of two. The search range can be reduced by half by shifting instead of
dividing. In general, the number of kerning pairs, nPairs, will not be a
power of two. The value of the search range, searchRange, should be the
largest power of two less than or equal to nPairs. The number of pairs
not covered by searchRange (that is, nPairs - searchRange) is the value
rangeShift.

Windows v3.1 does not make use of the [kern](#chapter.kern) data other
than to expose it to applications through the GetFontData() API.Format 2

## Format 2

### Specification

This subtable is a two-dimensional array of kerning values. The glyphs
are mapped to classes, using a different mapping for left- and
right-hand glyphs. This allows glyphs that have similar right- or
left-side shapes to be handled together. Each similar right- or
left-hand shape is said to be single class.

Each row in the kerning array represents one left-hand glyph class, each
column represents one right-hand glyph class, and each cell contains a
kerning value. Row and column 0 always represent glyphs that do not kern
and contain all zeros.

The values in the right class table are stored pre-multiplied by the
number of bytes in a single kerning value, and the values in the left
class table are stored pre-multiplied by the number of bytes in one row.
This eliminates needing to multiply the row and column values together
to determine the location of the kerning value. The array can be indexed
by doing the right- and left-hand class mappings, adding the class
values to the address of the array, and fetching the kerning value to
which the new address points.

The header for the simple array has the following format:

| Type   | Name            | Description                                                               |
| ------ | --------------- | ------------------------------------------------------------------------- |
| USHORT | rowWidth        | The width, in bytes, of a row in the table.                               |
| USHORT | leftClassTable  | Offset from beginning of this subtable to left-hand class table.          |
| USHORT | rightClassTable | Offset from beginning of this subtable to right-hand class table.         |
| USHORT | array           | Offset from beginning of this subtable to the start of the kerning array. |

Each class table has the following header:

| Type   | Name       | Description                     |
| ------ | ---------- | ------------------------------- |
| USHORT | firstGlyph | First glyph in class range.     |
| USHORT | nGlyphs    | Number of glyph in class range. |

This header is followed by nGlyphs number of class values, which are in
USHORT format. Entries for glyphs that don't participate in kerning
should point to the row or column at position zero.

The array itself is a left by right array of kerning values, which are
FWords, where left is the number of left-hand classes and R is the
number of right-hand classes. The array is stored by row.

Note that this format is the quickest to process since each lookup
requires only a few index operations. The table can be quite large since
it will contain the number of cells equal to the product of the number
of right-hand classes and the number of left-hand classes, even though
many of these classes do not kern with each other.

