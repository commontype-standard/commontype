# GDEF - The Glyph Definition Table

## Overview

### Specification

The Glyph Definition ([GDEF](#chapter.GDEF)) table contains three types
of information in three independent tables:

  - The *GlyphClassDef* table classifies the different types of glyphs
    in the font.

  - The *AttachmentList* table identifies all attachment points on the
    glyphs, which streamlines data access and bitmap caching.

  - The *LigatureCaretList* table contains positioning data for ligature
    carets, which the text-processing client uses on screen to select
    and highlight the individual components of a ligature glyph.

  - The *MarkAttachClassDef* table classifies mark glyphs, to help group
    together marks that are positioned similarly.

Both the [GSUB](#chapter.GSUB) and [GPOS](#chapter.GPOS) tables
reference the [GDEF](#chapter.GDEF) table information to supplement
their own data for substituting and positioning glyphs. Even so, a
[GDEF](#chapter.GDEF) table is optional for a font, included at the
discretion of the font developer. Without a [GDEF](#chapter.GDEF) table,
however, the text-processing client may have to define and maintain the
[GDEF](#chapter.GDEF) information on its own when substituting and
positioning glyphs.

A client may use any one or more of the three [GDEF](#chapter.GDEF)
tables during text processing. This overview explains how each of the
three tables are organized and used (See Figure 7a). The rest of this
chapter describes the individual [GDEF](#chapter.GDEF) tables and the
tables that they reference.

![Figure 7a. High-level organization of [GDEF](#chapter.GDEF)
table](fig7a.gif)

### Annotation

First sentence, both occurrences of 'three' should be replaced by
'four'.

Last two sentences of paragraph after the bullet list: I am not sure
that this comment applies to GlyphClassDef for example. There does not
seem to be any mandatory data in [GSUB](#chapter.GSUB) or
[GPOS](#chapter.GPOS) that would indicate the class of a glyph. Suppose
that there is only a [GSUB](#chapter.GSUB) table, no
[GPOS](#chapter.GPOS) and no [GDEF](#chapter.GDEF); that
[GSUB](#chapter.GSUB) contains only one SingleSubstitution lookup with
LookupFlag set to ignoreBaseGlyphs. What glyphs should be ignored by
this lookup? Or is this font illegal?

Last paragraph: both occurrences of 'three' should be replaced by
'four'.

## Glyph Class Definition Table

### Specification

The Glyph Class Definition (GlyphClassDef) table identifies four types
of glyphs in a font: base glyphs, ligature glyphs, combining mark
glyphs, and glyph components (see Figure 7b). [GSUB](#chapter.GSUB) and
[GPOS](#chapter.GPOS) lookups define and use these glyph classes to
differentiate the types of glyphs in a string. For example,
[GPOS](#chapter.GPOS) uses the glyph classes to distinguish between a
simple base glyph and the mark glyph that follows it.

![Figure 7b. A base glyph, ligature glyph, mark glyph, and glyph
components](fig7b.gif)

In addition, a client uses class definitions to apply
[GSUB](#chapter.GSUB) and [GPOS](#chapter.GPOS) LookupFlag data
correctly. For example, a LookupFlag may specify ignoring ligatures and
marks during a glyph operation. If the font does not include a
GlyphClassDef table, the client must define and maintain this
information when using the [GSUB](#chapter.GSUB) and
[GPOS](#chapter.GPOS) tables.

### Annotation

First sentence: shouldn’t “glyph components” be replaced by “component
glyphs”? Similarly in the figure’s title.

Last sentence: How can the client figure out the class of a glyph from a
font lacking a GlyphClassDef table?

## Attachment Point List Table

### Specification

The Attachment Point List table (AttachmentList) identifies all the
attachment points defined in the [GPOS](#chapter.GPOS) table and their
associated glyphs so a client can quickly access coordinates for each
glyph's attachment points. As a result, the client can cache coordinates
for attachment points along with glyph bitmaps and avoid recalculating
the attachment points each time it displays a glyph. Without this table,
processing speed would be slower because the client would have to decode
the [GPOS](#chapter.GPOS) lookups that define attachment points and
compile the points in a list.

## Ligature Caret List Table

### Specification

The Ligature Caret List table (LigatureCaretList), particularly useful
in Arabic and other scripts with many ligatures, specifies coordinates
for positioning carets on all ligatures in a font. The client uses this
data to select and highlight ligature components in displayed text (see
Figure 7c).

![Figure 7c. Proper ligature caret postioning](fig7c.gif)

Each ligature can have more than one caret position, with each position
defined as an X or Y value on the baseline according to the writing
direction of the script or language system. The font developer can use
any of three formats to represent a caret coordinate value. One format
represents values in design units only, another fine-tunes a value based
on a designated contour point, and the third uses a Device table to
adjust values at specific font sizes.

Without a Ligature Caret List table, the client would have to define
caret positions without knowing the positions of the ligature
components. The resulting highlighting or hit-testing might be
ambiguous. For example, suppose a client places a caret at the midpoint
position along the width of a hyphothetical "wi" ligature. Because the
"w" is wider than the "i," that position would not clearly indicate
which component is selected. Instead, for accurate selection, the caret
should be moved to the right so that either the "w" or "i" could be
clearly highlighted.

## GDEF Header

### Specification

The [GDEF](#chapter.GDEF) table begins with a header that consists of a
version number (Version), initially set to 0x00010000, an offset to a
table defining the types of glyphs in the font (GlyphClassDef), an
offset to a list defining attachment points on the glyphs(AttachList),
an offset to a ligature caret list (LigCaretList) and an offset to a
list defining types of marks that can be attached (MarkAttachClassDef).
The format used for the MarkAttachClassDef is the same as that for
GlyphClassDef. Please refer the 'LookupFlag bit enumeration' section in
the Common Table Formats for more on using lookup flags with the
information in these fields.

Example 1 at the end of this chapter shows a [GDEF](#chapter.GDEF)
Header table.

| Type   | Name               | Description                                                                                                            |
| ------ | ------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Fixed  | Version            | Version of the [GDEF](#chapter.GDEF) table-initially 0x00010000                                                        |
| Offset | GlyphClassDef      | Offset to class definition table for glyph type-from beginning of [GDEF](#chapter.GDEF) header (may be NULL)           |
| Offset | AttachList         | Offset to list of glyphs with attachment points-from beginning of [GDEF](#chapter.GDEF) header (may be NULL)           |
| Offset | LigCaretList       | Offset to list of positioning points for ligature carets-from beginning of [GDEF](#chapter.GDEF) header (may be NULL)  |
| Offset | MarkAttachClassDef | Offset to class definition table for mark attachment type-from beginning of [GDEF](#chapter.GDEF) header (may be NULL) |

GDEF Header

## Glyph Class Definition Table

### Specification

The [GSUB](#chapter.GSUB) and [GPOS](#chapter.GPOS) tables use the Glyph
Class Definition table (GlyphClassDef) to identify which glyph classes
to adjust with lookups.

The table uses the same format as the Class Definition table (for
details, see the chapter, Common Table Formats). However, the
GlyphClassDef table uses class values already defined in the
GlyphClassDef Enumeration list:

| Class | Description                                               |
| ----- | --------------------------------------------------------- |
| 1     | Base glyph (single character, spacing glyph)              |
| 2     | Ligature glyph (multiple character, spacing glyph)        |
| 3     | Mark glyph (non-spacing combining glyph)                  |
| 4     | Component glyph (part of single character, spacing glyph) |

GlyphClassDef Enumeration List

The font developer does not have to classify every glyph in the font,
but any glyph not assigned a class value falls into Class zero (0). For
instance, class values might be useful for the Arabic glyphs in a font,
but not for the Latin glyphs. Then the GlyphClassDef table will list
only Arabic glyphs, and-by default-the Latin glyphs will be assigned to
Class 0. Component glyphs can be put together to generate ligatures. A
ligature can be generated by creating a glyph in the font that
references the component glyphs, or outputting the component glyphs in
the desired sequence. Component glyphs are not used in defining any
[GSUB](#chapter.GSUB) or [GPOS](#chapter.GPOS) formats.

Example 2 at the end of this chapter defines a GlyphClassDef table with
a sample glyph for each of the assigned classes.

## Attachment List Table

### Specification

The Attachment List table (AttachList) may be used to cache attachment
point coordinates along with glyph bitmaps.

The table consists of an offset to a Coverage table (Coverage) listing
all glyphs that define attachment points in the [GPOS](#chapter.GPOS)
table, a count of the glyphs with attachment points (GlyphCount), and an
array of offsets to AttachPoint tables (AttachPoint). The array lists
the AttachPoint tables, one for each glyph in the Coverage table, in the
same order as the Coverage Index.

| Type   | Name                       | Description                                                                                       |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------- |
| Offset | Coverage                   | Offset to Coverage table - from beginning of AttachList table                                     |
| uint16 | GlyphCount                 | Number of glyphs with attachment points                                                           |
| Offset | AttachPoint \[GlyphCount\] | Array of offsets to AttachPoint tables-from beginning of AttachList table-in Coverage Index order |

AttachList table

An AttachPoint table consists of a count of the attachment points on a
single glyph (PointCount) and an array of contour indices of those
points (PointIndex), listed in increasing numerical order.

Example 3 at the end of the chapter demonstrates an AttachList table
that defines attachment points for two glyphs.

| Type   | Name                      | Description                                                   |
| ------ | ------------------------- | ------------------------------------------------------------- |
| uint16 | PointCount                | Number of attachment points on this glyph                     |
| uint16 | PointIndex \[PointCount\] | Array of contour point indices -in increasing numerical order |

AttachPoint table

## Ligature Caret List Table

### Specification

The Ligature Caret List table (LigCaretList) defines caret positions for
all the ligatures in a font. The table consists of an offset to a
Coverage table that lists all the ligature glyphs (Coverage), a count of
the defined ligatures (LigGlyphCount), and an array of offsets to
LigGlyph tables (LigGlyph). The array lists the LigGlyph tables, one for
each ligature in the Coverage table, in the same order as the Coverage
Index.

Example 4 at the end of this chapter shows a LigCaretList table.

| Type   | Name                       | Description                                                                                      |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------ |
| Offset | Coverage                   | Offset to Coverage table - from beginning of LigCaretList table                                  |
| uint16 | LigGlyphCount              | Number of ligature glyphs                                                                        |
| Offset | LigGlyph \[LigGlyphCount\] | Array of offsets to LigGlyph tables-from beginning of LigCaretList table-in Coverage Index order |

LigCaretList table

## Ligature Glyph Table

### Specification

A Ligature Glyph table (LigGlyph) contains the caret coordinates for a
single ligature glyph. The number of coordinate values, each defined in
a separate CaretValue table, equals the number of components in the
ligature minus one (1).

The LigGlyph table consists of a count of the number of CaretValue
tables defined for the ligature (CaretCount) and an array of offsets to
CaretValue tables (CaretValue).

Example 4 at the end of the chapter shows a LigGlyph table.

| Type   | Name                      | Description                                                                                           |
| ------ | ------------------------- | ----------------------------------------------------------------------------------------------------- |
| uint16 | CaretCount                | Number of CaretValues for this ligature (components - 1)                                              |
| Offset | CaretValue \[CaretCount\] | Array of offsets to CaretValue tables-from beginning of LigGlyph table-in increasing coordinate order |

LigGlyph table

## Caret Values Table

### Specification

A Caret Values table (CaretValues), which defines caret positions for a
ligature, can be any of three possible formats. One format uses design
units to define the caret position. The other two formats use a contour
point or Device table to fine-tune a caret's position at specific font
sizes and device resolutions. Caret coordinates are either X or Y
values, depending upon the text direction.

## CaretValue Format 1

### Specification

The first format (CaretValueFormat1) consists of a format identifier
(CaretValueFormat), followed by a single coordinate for the caret
position (Coordinate). The Coordinate is in design units.

This format has the benefits of small size and simplicity, but the
Coordinate value cannot be hinted for fine adjustments at different
device resolutions.

Exampel 4 at the end of this chapter shows a CaretValueFormat1 table.

| Type   | Name             | Description                   |
| ------ | ---------------- | ----------------------------- |
| uint16 | CaretValueFormat | Format identifier-format = 1  |
| int16  | Coordinate       | X or Y value, in design units |

CaretValueFormat1 table: Design units only

## CaretValue Format 2

### Specification

The second format (CaretValueFormat2) specifies the caret coordinate in
terms of a contour point index on a specific glyph. During font hinting,
the contour point on the glyph outline may move. The point's final
position after hinting provides the final value for rendering a given
font size.

The table contains a format identifier (CaretValueFormat) and a contour
point index (CaretValuePoint).

Example 5 at the end of this chapter demonstrates a CaretValueFormat2
table.

| Type   | Name             | Description                  |
| ------ | ---------------- | ---------------------------- |
| uint16 | CaretValueFormat | Format identifier-format = 2 |
| uint16 | CaretValuePoint  | Contour point index on glyph |

CaretValueFormat2 table: Contour point

## CaretValue Format 3

### Specification

The third format (CaretValueFormat3) also specifies the value in design
units, but it uses a Device table rather than a contour point to adjust
the value. This format offers the advantage of fine-tuning the
Coordinate value for any device resolution. (For more information about
Device tables, see the chapter, Common Table Formats.)

The format consists of a format identifier (CaretValueFormat), an X or Y
value (Coordinate), and an offset to a Device table (DeviceTable).

Example 6 at the end of this chapter shows a CaretValueFormat3 table.

| Type   | Name             | Description                                                                |
| ------ | ---------------- | -------------------------------------------------------------------------- |
| uint16 | CaretValueFormat | Format identifier-format = 3                                               |
| int16  | Coordinate       | X or Y value, in design units                                              |
| Offset | DeviceTable      | Offset to Device table for X or Y value-from beginning of CaretValue table |

CaretValueFormat3 table: Design units plus Device table

## Mark Attachment Class Definition Table

### Specification

A Mark Attachment Class Definition Table defines the class to which a
mark glyph may belong. This table uses the same format as the Class
Definition table (for details, see the chapter, Common Table Formats ).

Example 7 in this document shows a MarkAttachClassDef table.

## GDEF Table Examples

### Specification

The rest of this chapter describes examples of all the
[GDEF](#chapter.GDEF) table formats. All the examples reflect unique
parameters described below, but the samples provide a useful reference
for building tables specific to other situations.

The examples have three columns showing hex data, source, and comments.

## Example 1: GDEF Header

### Specification

Example 1 shows a [GDEF](#chapter.GDEF) Header definition with offsets
to each of the main tables in [GDEF](#chapter.GDEF).

| HexData  | Source                  | Comment                                          |
| -------- | ----------------------- | ------------------------------------------------ |
|          | GDEFHeader              |                                                  |
|          | TheGDEFHeader           | GDEFHeader table definition                      |
| 00010000 | 0x00010000              | Version                                          |
| 000A     | GlyphClassDefTable      | offset to GlyphClassDef table                    |
| 0026     | AttachListTable         | offset to AttachList table                       |
| 0040     | LigCaretListTable       | offset to LigCaretList table                     |
| 005A     | MarkAttachClassDefTable | offset to Mark Attachment Class Definition Table |

Example 1

## Example 2: GlyphClassDef Table

### Specification

The GlyphClassDef table in Example 2 specifies a glyph for the each of
the glyph classes predefined in the GlyphClassDef Enumeration List.

| HexData | Source                     | Comment                                          |
| ------- | -------------------------- | ------------------------------------------------ |
|         | ClassDefFormat2            |                                                  |
|         | GlyphClassDefTable         | ClassDef table definition                        |
| 0002    | 2                          | ClassFormat                                      |
| 0004    | 4                          | ClassRangeCount ClassRangeRecord\[0              |
| 0024    | iGlyphID                   | Start                                            |
| 0024    | iGlyphID                   | End                                              |
| 0001    | 1                          | Class, 1 = base glyphs ClassRangeRecord\[1\]     |
| 009F    | ffiLigGlyphID              | Start                                            |
| 009F    | ffiLigGlyphID              | End                                              |
| 0002    | 2                          | Class, 2 = ligature glyphs ClassRangeRecord\[2\] |
| 0058    | umlautAccentGlyphID        | Start                                            |
| 0058    | umlautAccentGlyphID        | End                                              |
| 0003    | 3                          | Class, 3 = mark glyphs ClassRangeRecord\[3\]     |
| 018F    | CurvedTailComponentGlyphID | Start                                            |
| 018F    | CurvedTailComponentGlyphID | End                                              |
| 0004    | 4                          | Class, 4 = component glyphs                      |

Example 2

## Example 3: AttachList Table

### Specification

In Example 3, the AttachList table enumerates the attachment points
defined for two glyphs. The GlyphCoverage table identifies the glyphs:
"a" and "e." For each covered glyph, an AttachPoint table specifies the
attachment point count and point indices: one point for the "a" glyph
and two for the "e" glyph.

| HexData | Source          | Comment                      |
| ------- | --------------- | ---------------------------- |
|         | AttachList      |                              |
|         | AttachListTable | AttachList table definition  |
| 0012    | GlyphCoverage   | offset to Coverage table     |
| 0002    | 2               | GlyphCount                   |
| 0008    | aAttachPoint    | AttachPoint\[0\]             |
| 000C    | eAttachPoint    | AttachPoint\[1               |
|         | AttachPoint     |                              |
|         | aAttachPoint    | AttachPoint table definition |
| 0001    | 1               | PointCount                   |
| 0012    | 18              | PointIndex\[0                |
|         | AttachPoint     |                              |
|         | eAttachPoint    | AttachPoint table definition |
| 0002    | 2               | PointCount                   |
| 000E    | 14              | PointIndex\[0\]              |
| 0017    | 23              | PointIndex\[1                |
|         | CoverageFormat1 |                              |
|         | GlyphCoverage   | Coverage table definition    |
| 0001    | 1               | CoverageFormat               |
| 0002    | 2               | GlyphCount                   |
| 001C    | aGlyphID        | GlyphArray\[0\]              |
| 0020    | eGlyphID        | GlyphArray\[1\]              |

Example 3

## Example 4: LigCaretList Table, LigGlyph Table and CaretValueFormat1 Table

### Specification

Example 4 defines a list of ligature carets. The LigCoverage table lists
all the ligature glyphs that define caret positions. In this example,
two ligatures are covered, "ffi" and "fi." For each covered glyph, a
LigGlyph table specifies the number of carets for the ligature and their
coordinate values. The "fi" ligature defines one caret, positioned
between the "f" and "i" components; the "ffi" ligature defines two, one
positioned between the two "f" components and the other positioned
between the "f" and "i." The CaretValue tables shown here use Format1,
where values are specified in design units only.

| HexData | Source            | Comment                                         |
| ------- | ----------------- | ----------------------------------------------- |
|         | LigCaretList      |                                                 |
|         | LigCaretListTable | LigCaretList table definition                   |
| 0008    | LigCoverage       | offset to Coverage table                        |
| 0002    | 2                 | LigGlyphCount                                   |
| 0010    | fiLigGlyph        | offset to LigGlyph table\[0\]                   |
| 0014    | ffiLigGlyph       | offset to LigGlyph table\[1                     |
|         | CoverageFormat1   |                                                 |
|         | LigCoverage       | Coverage table definition                       |
| 0001    | 1                 | CoverageFormat                                  |
| 0002    | 2                 | GlyphCount                                      |
| 009F    | ffiLigGlyphID     | GlyphArray\[0\]                                 |
| 00A5    | fiLigGlyphID      | GlyphArray\[1                                   |
|         | LigGlyph          |                                                 |
|         | fiLigGlyph        | LigGlyph table definition                       |
| 0001    | 1                 | CaretCount, equals the number of components - 1 |
| 000E    | CaretFI           | CaretValue\[0                                   |
|         | LigGlyph          |                                                 |
|         | ffiLigGlyph       | LigGlyph table definition                       |
| 0002    | 2                 | CaretCount, equals the number of components - 1 |
| 0006    | CaretFFI1         | CaretValue\[0\]                                 |
| 000E    | CaretFFI2         | CaretValue\[1                                   |
|         | CaretValueFormat1 |                                                 |
|         | CaretFI           | CaretValue table definition                     |
| 0001    | 1                 | CaretValueFormat design units only              |
| 025B    | 603               | Coordinate X or Y valu                          |
|         | CaretValueFormat1 |                                                 |
|         | CaretFFI1         | CaretValue table definition                     |
| 0001    | 1                 | CaretValueFormat design units only              |
| 025B    | 603               | Coordinate X or Y valu                          |
|         | CaretValueFormat1 |                                                 |
|         | CaretFFI2         | CaretValue table definition                     |
| 0001    | 1                 | CaretValueFormat design units only              |
| 04B6    | 1206              | Coordinate X or Y value                         |

Example 1

## Example 5: CaretValueFormat2 Table

### Specification

Example 5 shows a CaretValueFormat2 table that specifies a ligature
caret coordinate in terms of a contour point index on a specific glyph.
The final position of the caret depends on the location of the contour
point on the glyph after hinting.

| HexData | Source            | Comment                             |
| ------- | ----------------- | ----------------------------------- |
|         | CaretValueFormat2 |                                     |
|         | Caret1            | CaretValue table definition         |
| 0002    | 2                 | CaretValueFormat contour point      |
| 000D    | 13                | CaretValuePoint contour point index |

Example 5

## Example 6: CaretValueFormat3 Table

### Specification

In Example 6, the CaretValueFormat3 table defines a caret position in
design units, but includes a Device table to adjust the X or Y
coordinate for the point size and resolution of the output font. Here,
the Device table specifies pixel adjustments for font sizes from 12 ppem
to 17 ppem.

| HexData | Source             | Comment                                         |
| ------- | ------------------ | ----------------------------------------------- |
|         | CaretValueFormat3  |                                                 |
|         | Caret3             | CaretValue table definition                     |
| 0003    | 3                  | CaretValueFormat design units plus Device table |
| 04B6    | 1206               | Coordinate X or Y value, design units           |
| 0006    | CaretDevice        | offset to Device tabl                           |
|         | DeviceTableFormat2 |                                                 |
|         | CaretDevice        | Device Table definition                         |
| 000C    | 12                 | StartSize                                       |
| 0011    | 17                 | EndSize                                         |
| 0002    | 2                  | DeltaFormat                                     |
|         | 1                  | increase 12ppm by 1 pixel                       |
|         | 1                  | increase 13ppm by 1 pixel                       |
|         | 1                  | increase 14ppm by 1 pixel                       |
| 1111    | 1                  | increase 15ppm by 1 pixel                       |
|         | 2                  | increase 16ppm by 2 pixel                       |
| 2200    | 2                  | increase 17ppm by 2 pixel                       |

Example 6

## Example 7: MarkAttachClassDef Table

### Specification

In Example 7, the MarkAttachClassDef table specifies an attachment class
for the each of the glyph ranges predefined in the GlyphClassDef
Enumeration List as marks.

| HexData | Source                     | Comment                                       |
| ------- | -------------------------- | --------------------------------------------- |
|         | ClassDefFormat2            |                                               |
|         | theMarkAttachClassDefTable | ClassDef table definition                     |
| 0002    | 2                          | ClassFormat                                   |
| 0004    | 4                          | ClassRangeCount ClassRangeRecord\[0\]         |
| 0268    | graveAccentGlyphID         | Start                                         |
| 026A    | circumflexAccentGlyphID    | End                                           |
| 0001    | 1                          | Class, 1 = top marks ClassRangeRecord\[1\]    |
| 0270    | diaeresisAccentGlyphID     | Start                                         |
| 0272    | acuteAccentGlyphID         | End                                           |
| 0001    | 1                          | Class, 1 = top marks ClassRangeRecord\[2\]    |
| 028C    | diaeresisBelowGlyphID      | Start                                         |
| 028F    | cedillaGlyphID             | End                                           |
| 0002    | 2                          | Class, 2 = bottom marks ClassRangeRecord\[3\] |
| 0295    | circumflexBelowGlyphID     | Start                                         |
| 0295    | circumflexBelowGlyphID     | End                                           |
| 0002    | 2                          | Class, 2 = bottom marks                       |

Example 7

