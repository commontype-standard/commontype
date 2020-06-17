# The OpenType Font File

## Introduction

### Specification

An OpenType font file contains data, in table format, that comprises
either a TrueType or a PostScript outline font. Rasterizers use
combinations of data from the tables contained in the font to render the
TrueType or PostScript glyph outlines. Some of this supporting data is
used no matter which outline format is used; some of the supporting data
is specific to either TrueType or PostScript.

### XML Representation

Here is the scrap that collects all the definitions for our Relax NG
grammar:

    OpenType Relax NG Schema ==
          
    
    ##_____________________________________________________________________________
    ##
    ##  Copyright 2000-2016 Adobe Systems Incorporated. All Rights Reserved.
    ##
    ##  Licensed under the Apache License, Version 2.0 (the "License");
    ##  you may not use these files except in compliance with the License.
    ##  You may obtain a copy of the License at
    ##
    ##   http://www.apache.org/licenses/LICENSE-2.0
    ##
    ##  Unless required by applicable law or agreed to in writing, software
    ##  distributed under the License is distributed on an "AS IS" BASIS,
    ##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    ##  See the License for the specific language governing permissions and
    ##  limitations under the License.
    ##_____________________________________________________________________________
    
    start =
      element font {
        attribute name { text }?,
        base-font?,
        (BASE?
         & CFF?
         & glyf?
         & DSIG?
         & GDEF?
         & GPOS?
         & GSUB?
         & OS2?
         & cmap?
         & head?
         & hhea?
         & hmtx?
         & hdmx?
         & VDMX?
         & vhea?
         & vmtx?
         & maxp?
         & name?
         & post?
         & VORG?)
      }
    
      base-font =
        element base-font {
          attribute name { text }
        }
    
      yesOrNo = "yes" | "no"
    
      schema: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95

## Filenames

### Specification

OpenType fonts may have the extension .OTF or .TTF, depending on the
kind of outlines in the font and the creator's desire for compatibility
on systems without native OpenType support.

  - In all cases, fonts with only CFF data (no TrueType outlines) always
    have an .OTF extension.

  - Fonts containing TrueType outlines may have either .OTF or .TTF,
    depending on the desire for backward compatibility on older systems
    or with previous versions of the font. TrueType Collection fonts
    should have a .TTC extension whether or not the fonts have OpenType
    layout tables present.

## Data Types

### Specification

The following data types are used in the OpenType font file. All
OpenType fonts use Motorola-style byte ordering (Big Endian):

| Data Type    | Description                                                                                                                       |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| BYTE         | 8-bit unsigned integer.                                                                                                           |
| CHAR         | 8-bit signed integer.                                                                                                             |
| USHORT       | 16-bit unsigned integer.                                                                                                          |
| SHORT        | 16-bit signed integer.                                                                                                            |
| UINT24       | 24-bit signed integer.                                                                                                            |
| ULONG        | 32-bit unsigned integer.                                                                                                          |
| LONG         | 32-bit signed integer.                                                                                                            |
| Fixed        | 32-bit signed fixed-point number (16.16)                                                                                          |
| FUNIT        | Smallest measurable distance in the em space.                                                                                     |
| FWORD        | 16-bit signed integer (SHORT) that describes a quantity in FUnits.                                                                |
| UFWORD       | 16-bit unsigned integer (USHORT) that describes a quantity in FUnits.                                                             |
| F2DOT14      | 16-bit signed fixed number with the low 14 bits of fraction (2.14).                                                               |
| LONGDATETIME | Date represented in number of seconds since 12:00 midnight, January 1, 1904. The value is represented as a signed 64-bit integer. |
| Tag          | Array of four uint8s (length = 32 bits) used to identify a script, language system, feature, or baseline                          |
| GlyphID      | Glyph index number, same as uint16 (length = 16 bits)                                                                             |
| Offset       | Offset to a table, same as uint16 (length = 16 bits), NULL offset = 0x0000                                                        |

The F2DOT14 format consists of a signed, 2's complement mantissa and an
unsigned fraction. To compute the actual value, take the mantissa and
add the fraction. Examples of 2.14 values are:

| Decimal Value | Hex Value | Mantissa | Fraction    |
| ------------- | --------- | -------- | ----------- |
| 1.999939      | 0x7fff    | 1        | 16383/16384 |
| 1.75          | 0x7000    | 1        | 12288/16384 |
| 0.000061      | 0x0001    | 0        | 1/16384     |
| 0.0           | 0x0000    | 0        | 0/16384     |
| \-0.000061    | 0xffff    | \-1      | 16383/16384 |
| \-2.0         | 0x8000    | \-2      | 0/16384     |

### Annotation

A number of synonyms are used for throughout the specification. They
should be documented, and may be even replace the type above, as their
names are more useful:

|        |        |
| ------ | ------ |
| uint8  | BYTE   |
| int8   | CHAR   |
| uint16 | USHORT |
| int16  | SHORT  |
| uint32 | ULONG  |
| int32  | LONG   |

## Version Numbers

### Specification

Most tables have version numbers, and the version number for the entire
font is contained in the Table Directory. Note that there are two
different table version number types, each with its own numbering
scheme. USHORT version numbers always start at zero (0). Fixed version
numbers always start at one (1.0 or 0x00010000), except where noted
([EBDT](#chapter.EBDT), [EBLC](#chapter.EBLC) and [EBSC](#chapter.EBSC)
tables).

Implementations reading tables must include code to check version
numbers so that if and when the format and therefore the version number
changes, older implementations will reject newer versions gracefully, if
the changes are incompatible.

When a Fixed number is used as a version, the upper 16 bits comprise a
major version number, and the lower 16 bits a minor. Tables with
non-zero minor version numbers always specify the literal value of the
version number since the normal representation of Fixed numbers is not
necessarily followed. For example, the version number of
[maxp](#chapter.maxp) table version 0.5 is 0x00005000, and that of
[vhea](#chapter.vhea) table version 1.1 is 0x00011000. If an
implementation understands a major version number, then it can safely
proceed reading the table. The minor version number indicates extensions
to the format that are undetectable by implementations that do not
support them.

The only exception to this is the Offset Table's sfnt version. This
serves solely to identify whether the OpenType font contains TrueType
outlines (a value of 1.0) or CFF data (the tag 'OTTO'), as described in
the section below, [Organization of an OpenType font](#organization).

When a USHORT number is used to indicate version, it should be treated
as though it were a minor version number; i.e., all format changes are
compatible extensions.

## Organization of an OpenType Font

### Specification

A key characteristic of the OpenType format is the TrueType sfnt
"wrapper", which provides organization for a collection of tables in a
general and extensible manner.

The OpenType font file begins with the Offset Table. If the font file
contains only one font, the Offset Table will begin at byte 0 of the
file. If the font file is a TrueType collection, the beginning point of
the Offset Table for each font is indicated in the TTCHeader.

| Type   | Name          | Description                              |
| ------ | ------------- | ---------------------------------------- |
| Fixed  | sfnt version  | 0x00010000 for version 1.0.              |
| USHORT | numTables     | Number of tables.                        |
| USHORT | searchRange   | (Maximum power of 2 \<= numTables) x 16. |
| USHORT | entrySelector | Log2(maximum power of 2 \<= numTables).  |
| USHORT | rangeShift    | NumTables x 16-searchRange.              |

Offset Table

OpenType fonts that contain TrueType outlines should use the value of
1.0 for the sfnt version. OpenType fonts containing CFF data should use
the tag 'OTTO' as the sfnt version number.

Note: The Apple specification for TrueType fonts allows for 'true' and
'typ1' for sfnt version. These version tags should not be used for fonts
which contain OpenType tables.

The Offset Table is followed immediately by the Table Directory entries.
Entries in the Table Directory must be sorted in ascending order by tag.
Offset values in the Table Directory are measured from the start of the
font file.

| Type  | Name     | Description                                  |
| ----- | -------- | -------------------------------------------- |
| ULONG | tag      | 4 -byte identifier.                          |
| ULONG | checkSum | CheckSum for this table.                     |
| ULONG | offset   | Offset from beginning of TrueType font file. |
| ULONG | length   | Length of this table.                        |

Table Directory

The Table Directory makes it possible for a given font to contain only
those tables it actually needs. As a result there is no standard value
for numTables.

Tags are the names given to tables in the OpenType font file. All tag
names consist of four characters. Names with less than four letters are
allowed if followed by the necessary trailing spaces. All tag names
defined within a font (e.g., table names, feature tags, language tags)
must be built from printing characters represented by ASCII values
32-126

### Annotation

For clarity, is may be worth to add "or 'OTTO'" to the description of
the field snft version in the first table. I realize that the paragraph
following the table makes that clear, but users of the specification
familiar with it are likely to look at the tables only.

The type of the tag field in the second table should probably be 'Tag'.

### Validation

When validating a table, we want to make sure that there is are no
"dead" pieces in it, and that we don't have pointers in the middle. Here
are some helper methods:

``` 
  ==
      
  class Range {
    public String s;
    public int from;
    public int size;
    public boolean exclusive;

    public Range (String s, int from, int size, boolean exclusive) {
      this.s = s;
      this.from = from;
      this.size = size;
      this.exclusive = exclusive;
    }};

  private int nbRanges = 0;
  private Range[] ranges = null;

  public boolean claim (String s, int from, int size) {
    return claim (s, from, size, true);
  }

  public boolean claim (String s, int from, int size, boolean exclusive) {
    if (data.length < from + size) {
      System.out.println ("cannot claim " + size + " bytes from 0x"
                          + Integer.toHexString (from) + " for " + s);
      return false; }

    if (ranges == null) {
      ranges = new Range [100]; }

    if (nbRanges == ranges.length) {
      Range[] temp = new Range [nbRanges + 100];
      System.arraycopy (ranges, 0, temp, 0, nbRanges);
      ranges = temp; }

    ranges [nbRanges++] = new Range (s, from, size, exclusive);

    return true;
  }

  public void reportError (String s) {
    System.out.println ("Error: " + s);
  }

  public void reportMistake (String s) {
    System.out.println ("Mistake: " + s);
  }

  public void reportWarning (String s) {
    System.out.println ("Warning: " + s);
  }

  public void report () {
    String[] mask = new String [data.length];
    boolean[] exclusive = new boolean [data.length];

    for (int b = 0; b < mask.length; b++) {
      mask [b] = null; }

    for (int r = 0; r < nbRanges; r++) {
      for (int b = ranges [r].from; b < ranges [r].from + ranges [r].size; b++) {

        if (mask [b] != null) {
          if (exclusive [b] || ranges[r].exclusive) {
            System.out.println ("byte 0x" + Integer.toHexString (b)
                                + " claimed by both '"
                                + mask[b] + "' and '" + ranges[r].s); }}
        else {
          mask [b] = ranges [r].s;
          exclusive [b] = ranges [r].exclusive; }}}

    for (int b = 0; b < mask.length; b++) {
      if (mask[b] == null) {
        System.out.println ("byte 0x" + Integer.toHexString (b)
                            + " not claimed"); }}
  }
```

## Calculating Checksums

### Specification

Table checksums are the unsigned sum of the longs of a given table. In
C, the following function can be used to determine a checksum:

    ULONG
    CalcTableChecksum(ULONG *Table, ULONG Length)
    {
    ULONG Sum = 0L;
    ULONG *Endptr = Table+((Length+3) & ~3) / sizeof(ULONG);
    
    while (Table < EndPtr)
            Sum += *Table++;
    return Sum;
    }

> Note: This function implies that the length of a table must be a
> multiple of four bytes. In fact, a font is not considered structurally
> proper without the correct padding. All tables must begin on four byte
> boundries, and any remaining space between tables is padded with
> zeros. The length of all tables should be recorded in the table
> directory with their actual length (not their padded length).

To calculate the checkSum for the [head](#chapter.head) table which
itself includes the checkSumAdjustment entry for the entire font, do the
following:

1.  Set the checkSumAdjustment to 0.

2.  Calculate the checksum for all the tables including the
    [head](#chapter.head) table and enter that value into the table
    directory.

3.  Calculate the checksum for the entire font.

4.  Subtract that value from the hex value B1B0AFBA.

5.  Store the result in checkSumAdjustment.

The checkSum for the head table which includes the checkSumAdjustment
entry for the entire font is now incorrect. That is not a problem. Do
not change it. An application attempting to verify that the
[head](#chapter.head) table has not changed should calculate the
checkSum for that table by not including the checkSumAdjustment value,
and compare the result with the entry in the table directory.

## TrueType Collections

### Specification

A TrueType Collection (TTC) is a means of delivering multiple OpenType
fonts in a single file structure. TrueType Collections are most useful
when the fonts to be delivered together share many glyphs in common. By
allowing multiple fonts to share glyph sets, TTCs can result in a
significant saving of file space.

For example, a group of Japanese fonts may each have their own designs
for the kana glyphs, but share identical designs for the kanji. With
ordinary OpenType font files, the only way to include the common kanji
glyphs is to copy their glyph data into each font. Since the kanji
represent much more data than the kana, this results in a great deal of
wasteful duplication of glyph data. TTCs were defined to solve this
problem.

The CFF rasterizer does not currently support TTC files.

## The TTC File Structure

### Specification

A TrueType Collection file consists of a single TTC Header table, one or
more Offset Tables with Table Directories, and a number of OpenType
tables. The TTC Header must be located at the beginning of the TTC file.

Each OpenType table in a TTC file is referenced through the Offset Table
and Table Directories of each font which uses that table. Some of the
OpenType tables must appear multiple times, once for each font included
in the TTC; while other tables should be shared by multiple fonts in the
TTC.

As an example, consider a TTC file which combines two Japanese fonts
(Font1 and Font2). The fonts have different kana designs (Kana1 and
Kana2) but use the same design for kanji. The TTC file contains a single
[glyf](#chapter.glyf) table which includes both designs of kana together
with the kanji; both fonts' Table Directories point to this
[glyf](#chapter.glyf) table. But each font's Table Directory points to a
different [cmap](#chapter.cmap) table, which identifies the glyph set to
use. Font1's [cmap](#chapter.cmap) table points to the Kana1 region of
the [loca](#chapter.loca) and [glyf](#chapter.glyf) tables for kana
glyphs, and to the kanji region for the kanji. Font2's
[cmap](#chapter.cmap) table points to the Kana2 region of the
[loca](#chapter.loca) and [glyf](#chapter.glyf) tables for kana glyphs,
and to the same kanji region for the kanji.

The tables that should have a unique copy per font are those that are
used by the system in identifying the font and its character mapping,
including [cmap](#chapter.cmap), [name](#chapter.name), and
[OS/2](#chapter.OS2). The tables that should be shared by fonts in the
TTC are those that define glyph and instruction data or use glyph
indices to access data: [glyf](#chapter.glyf), [loca](#chapter.loca),
[hmtx](#chapter.hmtx), [hdmx](#chapter.hdmx), [LTSH](#chapter.LTSH),
[cvt](#chapter.cvt%20), [fpgm](#chapter.fpgm), [prep](#chapter.prep),
[EBLC](#chapter.EBLC), [EBDT](#chapter.EBDT), [EBSC](#chapter.EBSC),
[maxp](#chapter.maxp), and so on. In practice, any tables which have
identical data for two or more fonts may be shared.

A tool is available from Microsoft to help build .TTC files. The process
involves paying close attention the issue of glyph renumbering in a font
and the side effects that can result, in the [cmap](#chapter.cmap) table
and elsewhere. The fonts to be merged must also have compatible TrueType
instructions-that is, their preprograms, function definitions, and
control values must not conflict.

TrueType Collection files use the filename suffix .TTC.

## TTC Header

### Specification

There are two versions of the TTC Header: Version 1.0 has been used for
TTC files without digital signatures. Version 2.0 can be used for TTC
files with or without digital signatures ’ if there's no signature, then
the last three fields of the version 2.0 header are left null

If a digital signature is used, the DSIG table for the file must be the
last table in the TTC file. Signatures in a TTC file are expected to be
Format 1 signatures

The purpose of the TTC Header table is to locate the different Offset
Tables within a TTC file. The TTC Header is located at the beginning of
the TTC file (offset = 0). It consists of an identification tag, a
version number, a count of the number of OpenType fonts (Table
Directories) in the file, and an array of offsets to each Offset Table.

| Type  | Name                     | Description                                                                                       |
| ----- | ------------------------ | ------------------------------------------------------------------------------------------------- |
| TAG   | TTCTag                   | TrueType Collection ID string: 'ttcf'                                                             |
| ULONG | Version                  | Version of the TTC Header (1.0), 0x00010000                                                       |
| ULONG | numFonts                 | Number of fonts in the TTC                                                                        |
| ULONG | OffsetTable \[numFonts\] | Array of offsets to Offset Table for each font from the beginning of the file                     |
| ULONG | ulDsigTag                | Tag indicating that a DSIG table exists. This tag should equal 0x44534947 ([DSIG](#chapter.DSIG)) |
| ULONG | ulDsigLength             | The length (in bytes) of the DSIG table                                                           |
| ULONG | ulDsigOffset             | The offset (in bytes) of the DSIG table from the beginning of the TTC file                        |

TTC Header Version 1.0

| Type  | Name                     | Description                                                                                        |
| ----- | ------------------------ | -------------------------------------------------------------------------------------------------- |
| TAG   | TTCTag                   | TrueType Collection ID string: 'ttcf'                                                              |
| ULONG | Version                  | Version of the TTC Header (2.0), 0x00020000                                                        |
| ULONG | numFonts                 | Number of fonts in TTC                                                                             |
| ULONG | OffsetTable \[numFonts\] | Array of offsets to Offset Table for each font from the beginning of the file                      |
| ULONG | ulDsigTag                | Tag indicating that a DSIG table exists, 0x44534947 ([DSIG](#chapter.DSIG)) (null if no signature) |
| ULONG | ulDsigLength             | The length (in bytes) of the DSIG table (null if no signature)                                     |
| ULONG | ulDsigOffset             | The offset (in bytes) of the DSIG table from the beginning of the TTC file (null if no signature)  |

TTC Header Version 2.0

### Annotation

The type of the TTCTag field in both format should probably be 'Tag'
instead of 'TAG'.

The value of the Version field in both tables seems to be wrong; it's
missing a 0 at the end.

The description of the difference between version 1.0 and version 2.0
seems to contradict the content of the version 1.0 table. If a version
1.0 table is for files without a digital signature, what is the meaning
of the fields ulDsigTag, ulDsigLength and ulDsigOffset?

## Font Tables

### Specification

The rasterizer has a much easier time traversing tables if they are
padded so that each table begins on a 4-byte boundary. It is highly
recommended that all tables be long-aligned and padded with zeroes.

