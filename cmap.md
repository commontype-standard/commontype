# cmap - Character to Glyph Index Mapping Table

## Introduction

### Specification

This table defines the mapping of character codes to the glyph index
values used in the font. It may contain more than one subtable, in order
to support more than one character encoding scheme. Character codes that
do not correspond to any glyph in the font should be mapped to glyph
index 0. The glyph at this location must be a special glyph representing
a missing character, commonly known as .notdef.

The table header indicates the character encodings for which subtables
are present. Each subtable is in one of seven possible formats and
begins with a format code indicating the format used.

The platform ID and platform-specific encoding ID in the header entry
(and, in the case of the Macintosh platform, the language field in the
subtable itself) are used to specify a particular [cmap](#chapter.cmap)
encoding.The header entries must be sorted first by platform ID, then by
platform-specific encoding ID, and then by the version field in the
corresponding subtable. Each platform ID, platform-specific encoding ID,
and subtable language combination may appear only once in the
[cmap](#chapter.cmap) table.

When building a Unicode font for Windows, the platform ID should be 3
and the encoding ID should be 1. When building a symbol font for
Windows, the platform ID should be 3 and the encoding ID should be 0.
When building a font that will be used on the Macintosh, the platform ID
should be 1 and the encoding ID should be 0.

All Microsoft Unicode encodings (Platform ID = 3, Encoding ID = 1) must
provide at least a Format 4 [cmap](#chapter.cmap) subtable. If the font
is meant to support supplementary Unicode characters, it will
additionally need a Format 12 subtable with a platform encoding ID 10.
The contents of the Format 12 subtable need to be a superset of the
contents of the Format 4 subtable. Microsoft *strongly* recommends using
a Unicode [cmap](#chapter.cmap) for all fonts. However, some other
encodings that appear in current fonts follow:

| Platform ID | Encoding ID | Description |
| ----------- | ----------- | ----------- |
| 3           | 0           | Symbol      |
| 3           | 1           | Unicode     |
| 3           | 2           | ShiftJIS    |
| 3           | 3           | PRC         |
| 3           | 4           | Big5        |
| 3           | 5           | Wansung     |
| 3           | 6           | Johab       |
| 3           | 7           | Reserved    |
| 3           | 9           | Reserved    |
| 3           | 9           | Reserved    |
| 3           | 10          | UCS-4       |

Microsoft Encodings

Unicode Variation Sequences supported by the font may be specified in
the cmap table under platform ID 0 and encoding ID 5, using a format 14
cmap subtable.

The Character To Glyph Index Mapping Table is organized as follows:

| Type   | Name      | Description                            |
| ------ | --------- | -------------------------------------- |
| USHORT | version   | Table version number (0).              |
| USHORT | numTables | Number of encoding tables that follow. |

cmap Header

The cmap table header is followed by an array of encoding records that
specify the particular encoding and the offset to the subtable for that
encoding. The number of encoding records is numTables. An encoding
record entry looks like:

| Type   | Name       | Description                                                            |
| ------ | ---------- | ---------------------------------------------------------------------- |
| USHORT | platformID | Platform ID.                                                           |
| USHORT | encodingID | Platform-specific encoding ID.                                         |
| ULONG  | offset     | Byte offset from beginning of table to the subtable for this encoding. |

Encoding Record

### Annotation

The first paragraph covers three cases of missing glyphs: (1) there is a
cmap subtable for the encoding but the character code is not covered by
the subtable; (2) there is no subtable for the encoding; (3) there is a
cmap for the encoding, but the format of that subtable is not 0, 2, 4 or
6, 8, 10, or 12 (the currently defined formats). It is quite clear that
the described behaviour applies to the first case, but it is not clear
that this is the mandated behaviour in the second or third case. We
assume it is. Recommendation: make that clear, by rephrasing: "Character
codes that do not correspond to any glyph in the font (either because
there is no subtable for their encoding or or because the subtable in a
format not supported by the application or because the subtable does not
map them) should be mapped to glyph index 0."

The case of unknown formats is a bit more complicated. The
recommendation is to mandate that all characters codes should map to
glyph 0 for subtables in unknown formats.

The descriptions of the fields of this table do not include names for
them, as most other tables do. The recommendation is to include them:
version, numTables, platformID, encodingID, offset.

In the fifth paragraph, "UCS-4 (surrogate) characters" should be
replaced by "Unicode supplemental characters" or "Unicode supplemental
(non-BMP) characters". BMP characters are also UCS-4 characters. And
anyways, UCS-4 is an encoding, not a character collection.

It is legal to have a single subtable which is referenced from multiple
entries? This is useful when a given character encoding is present on
multiple platforms. For example, if there is a Unicode cmap subtable, it
can be referenced from one entry with platformID/encodingID (0, 3), and
from another entry with (3, 1).

### XML Representation

A cmap table is represented by a cmap element, with each entry
represented by a mapping element. Each cmap subtalble will contribute a
bunch of attributes and elements. As usual, those can be attached
directly to the mapping element, or they can be attached to a
cmapsubtable element. In the latter case, the mapping element carries an
IDREF name attribute, and the cmapsubtable carries a corresponding ID id
attribute. This mechanism is useful, e.g. when a cmapsutable is listed
under both Microsoft/Unicode BMP (3/1) and Unicode/BMP (1/0).

We pull the language field of each cmap subtable in the mapping entry,
as it logically belongs there. However, this creates a validity
constraint: if a cmapsubtable is referenced from multiple entries, then
all those entries must have the same language.

When we do not care about the format of a cmap subtable, we set the
format attribute to any and simply list the code point to glyph
correspondance.

Each cmap subtable format is also dual: it can either be expressed
(mostly) as a bunch of mappings, or it can be precise, recording all the
details specific to the format. We need this flexibility, because many
font consumers impose that the subtable for a given platform/encoding be
in a specific format, yet we want to describe the mappings simply.

    cmap table ==
          
      cmap =
        element cmap {
          attribute version { "0" },
          element mapping {
            attribute platformid { text },
            attribute encodingid { text },
            attribute language { text },
            cmapsubtableOffset }*,
    
          standaloneCmapsubtable*
        }
    
      standaloneCmapsubtable =
        element cmapsubtable { attribute id { text }, cmapsubtable }
    
      cmapsubtableOffset = attribute name { text } | cmapsubtable
    
      cmapsubtable |=
        attribute format { "any" },
        element map {
          attribute code { text },
          attribute glyph { text }}*

### Validation

Let's start by verifying the header.

    Validate header and set 'numTables' ==
          
      if (! claim ("cmap header", 0, 4)) {
        return; }
    
      int version = getuint16 (0);
      if (version > 0) {
        reportError ("cmap table version (" + version
                       + ") not part of the specification"); }
    
      int numTables = getuint16 (2);
      if (numTables == 0) {
        reportMistake ("font does not have any cmap subtables"); }

Let's move on to the directory of subtables. We first need to claim the
bytes:

    Validate directory ==
          
      if (! claim ("cmap directory", 4, 8*numTables)) {
        return; }

Another check is to make sure that the subtables are properly ordered:

    Validate directory order ==
          
      int lastPlatformID = -1;
      int lastEncodingID = -1;
    
      for (int st = 0; st < numTables; st++) {
        int platformID = getuint16 (4 + 8*st);
        int encodingID = getuint16 (4 + 8*st + 2);
    
        if (   platformID < lastPlatformID
            || (   platformID == lastPlatformID
                && encodingID <= lastEncodingID)) {
          reportError ("cmap subtables not ordered by (platformID, encodingID)"); }
    
        lastPlatformID = platformID;
        lastEncodingID = encodingID; }

Another check is that there are entries for 3/1 and 0/3, and that they
point ot the same subtable. This is a requirement for Adobe fonts only.

    Check there are 3/1 and 0/3 entries for the same
      subtable ==
          
      int subtable03offset = -1;
      int subtable31offset = -1;
    
      for (int st = 0; st < numTables; st++) {
        int platformID = getuint16 (4 + 8*st);
        int encodingID = getuint16 (4 + 8*st + 2);
    
        if (platformID == 0 && encodingID == 3) {
          subtable03offset = getLOffset (4 + 8*st + 4); }
    
        if (platformID == 3 && encodingID == 1) {
          subtable31offset = getLOffset (4 + 8*st + 4); }}
    
      if (subtable03offset == -1) {
        reportMistake ("no 0_3 subtable defined"); }
      if (subtable31offset == -1) {
        reportMistake ("no 3_1 subtable defined"); }
    
      if (   subtable03offset != subtable31offset
          && subtable03offset != -1
          && subtable31offset != -1) {
        reportMistake ("subtable 0_3 and 3_1 are not the same"); }

We validate each unique subtable on its own.

    Validate each subtable ==
          
      for (int st = 0; st < numTables; st++) {
        String stPrefix = "cmap subtable " + st;
        int stOffset = getLOffset (4 + 8*st + 4);
        boolean checked = false;
        for (int st2 = 0; st2 < st; st2++) {
          int st2Offset = getLOffset (4 + 8*st2 + 4);
          if (st2Offset == stOffset) {
             checked = true; }}
    
        if (checked) {
          continue; }
    
        int format = getuint16 (stOffset);
        switch (format) {
          case 0: { Validate cmap 0 subtable at stOffset; break; }
          case 2: { Validate cmap 2 subtable at stOffset; break; }
          case 4: { Validate cmap 4 subtable at stOffset; break; }
          case 6: { Validate cmap 6 subtable at stOffset; break; }
          default:{
            reportError (stPrefix + " is in an invalid format (" + format + ")");
            break; }}}

Finally, we verify that the Unicode cmap subtable is in the appropriate
format:

    Check the format of the Microsoft Unicode subtable ==
          
      for (int st = 0; st < numTables; st++) {
        int platformID = getuint16 (4 + 8*st);
        int encodingID = getuint16 (4 + 8*st + 2);
    
        if (platformID == 3 && encodingID == 1) {
          int stOffset = getLOffset (4 + 8*st + 4);
          int format = getuint16 (stOffset);
          if (format != 4) {
            reportError ("cmap subtable 3/1 must be in format 4"); }
          break; }}

Time to put everything together:

    Cmap Validation Method ==
          
      public void validate () {
    
        Validate header and set 'numTables'
    
        Validate directory
        Validate directory order
        Check there are 3/1 and 0/3 entries for the same
      subtable
    
        Validate each subtable
        Check the format of the Microsoft Unicode subtable
    
        report ();
      }

## OTF Windows NT compatibility mapping

### Specification

If a platform ID 4 (custom), encoding ID 0-255 (OTF Windows NT
compatibility mapping) [cmap](#chapter.cmap) encoding is present in an
OpenType font with CFF outlines, then the OTF font driver in Windows NT
will: (a) superimpose the glyphs encoded at character codes 0-255 in the
encoding on the corresponding Windows ANSI (code page 1252) Unicode
values in the Unicode encoding it reports to the system; (b) add Windows
ANSI (CharSet 0) to the list of CharSets supported by the font; and (c)
consider the value of the encoding ID to be a Windows CharSet value and
add it to the list of CharSets supported by the font. Note: The
[cmap](#chapter.cmap) subtable must use Format 0 or 6 for its subtable,
and the encoding must be identical to the CFF's encoding.

This [cmap](#chapter.cmap) encoding is not required. It provides a
compatibility mechanism for non-Unicode applications that use the font
as if it were Windows ANSI encoded. Non-Windows ANSI Type 1 fonts, such
as Cyrillic and Central European fonts, that Adobe shipped in the past
had "0" (Windows ANSI) recorded in the CharSet field of the .PFM file;
ATM for Windows 9x ignores the CharSet altogether. Adobe provides this
compatibility [cmap](#chapter.cmap) encoding in every OTF converted from
a Type1 font in which the Encoding is not StandardEncoding.

## Note on the language field in cmap subtables

### Specification

This field must be set to zero for all [cmap](#chapter.cmap) subtables
whose platform IDs are other than Macintosh (platform ID 1). For
[cmap](#chapter.cmap) subtables whose platform IDs are Macintosh, set
this field to the Macintosh language ID of the [cmap](#chapter.cmap)
subtable plus one, or to zero if the [cmap](#chapter.cmap) subtable is
not language-specific. For example, a Mac OS Turkish
[cmap](#chapter.cmap) subtable must set this field to 18, since the
Macintosh language ID for Turkish is 17. A Mac OS Roman
[cmap](#chapter.cmap) subtable must set this field to 0, since Mac OS
Roman is not a language-specific encoding.

## Format 0: Byte encoding table

### Specification

This is the Apple standard character to glyph index mapping table.

| Type   | Name                | Description                                                                                 |
| ------ | ------------------- | ------------------------------------------------------------------------------------------- |
| USHORT | format              | Format number is set to 0.                                                                  |
| USHORT | length              | This is the length in bytes of the subtable.                                                |
| USHORT | language            | Please see [Note on the language field in cmap subtables](#language_note) in this document. |
| BYTE   | glyphIdArray\[256\] | An array that maps character codes to glyph index values.                                   |

This is a simple 1 to 1 mapping of character codes to glyph indices. The
glyph set is limited to 256. Note that if this format is used to index
into a larger glyph set, only the first 256 glyphs will be accessible.

### Annotation

As the declaration stands, the length field seems superfluous, since the
table appears to always be 262 bytes long. This can be explained in one
of two ways:

  - the length field is included to make the first three words of all
    cmap subtables similar; it must always be 262.

  - the glyphIdArray does not need to be always 256 elements long, it
    can be shorter.

In the spirit of "generate conservatively, accept liberally", we
recommend that font designers always put 256 entries in glyphIdArray
(and consequently set length to 262), and that font consumers be ready
to handle fonts where the glyphIdArray contains length - 6 entries (but
no more than 256).

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "0" },
    element map {
      attribute code { text },
      attribute glyph { text }
    }*
```

### Validation

In line with our annotation, the validation code generates a warning if
the glyphIdArray does not have exactly 256 entries.

    Validate cmap 0 subtable at stOffset ==
          
      if (! claim (stPrefix + " header", stOffset, 6)) {
        break; }
    
      int stVersion = getuint16 (stOffset + 4);
      if (stVersion > 0) {
        reportError ("cmap@" + stOffset + " table version (" + stVersion
                     + ") not part of the specification"); }
    
      int size = getuint16 (stOffset + 2);
      if (size < 6) {
        reportError ("cmap subtable at " + stOffset + " has length <  6"); }
      if (size > 6 + 256) {
        reportError ("cmap subtable at " + stOffset
                         + " has more than 256 entries"); }
      if (size < 6 + 256) {
        reportWarning ("cmap subtable at " + stOffset
                       + " has less than 256 entries"); }
      // check that each glyphID in glyphIdArray is a valid glyph
    
      claim (stPrefix + " glyphIDArray", stOffset + 6, size - 6);

## Format 2: High-byte mapping through table

### Specification

This subtable is useful for the national character code standards used
for Japanese, Chinese, and Korean characters. These code standards use a
mixed 8/16-bit encoding, in which certain byte values signal the first
byte of a 2-byte character (but these values are also legal as the
second byte of a 2-byte character).

In addition, even for the 2-byte characters, the mapping of character
codes to glyph index values depends heavily on the first byte.
Consequently, the table begins with an array that maps the first byte to
a 4-word subHeader. For 2-byte character codes, the subHeader is used to
map the second byte's value through a subArray, as described below. When
processing mixed 8/16-bit text, subHeader 0 is special: it is used for
single-byte character codes. When subHeader zero is used, a second byte
is not needed; the single byte value is mapped through the subArray.

| Type           | Name                  | Description                                                                                                  |
| -------------- | --------------------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT         | format                | Format number is set to 2.                                                                                   |
| USHORT         | length                | This is the length in bytes of the subtable.                                                                 |
| USHORT         | language              | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document. |
| USHORT         | subHeaderKeys \[256\] | Array that maps high bytes to subHeaders: value is subHeader index \* 8.                                     |
| 4 words struct | subHeaders \[\]       | Variable-length array of subHeader structures.                                                               |
| USHORT         | glyphIndexArray \[\]  | Variable-length array containing subarrays used for mapping the low byte of 2-byte characters.               |

A subHeader is structured as follows:

| Type   | Name          | Description                                   |
| ------ | ------------- | --------------------------------------------- |
| USHORT | firstCode     | First valid low byte for this subHeader.      |
| USHORT | entryCount    | Number of valid low bytes for this subHeader. |
| SHORT  | idDelta       | See text below.                               |
| USHORT | idRangeOffset | See text below.                               |

The firstCode and entryCount values specify a subrange that begins at
firstCode and has a length equal to the value of entryCount. This
subrange stays within the 0-255 range of the byte being mapped. Bytes
outside of this subrange are mapped to glyph index 0 (missing glyph).
The offset of the byte within this subrange is then used as index into a
corresponding subarray of glyphIndexArray. This subarray is also of
length entryCount. The value of the idRangeOffset is the number of bytes
past the actual location of the idRangeOffset word where the
glyphIndexArray element corresponding to firstCode appears.

Finally, if the value obtained from the subarray is not 0 (which
indicates the missing glyph), you should add idDelta to it in order to
get the glyphIndex. The value idDelta permits the same subarray to be
used for several different subheaders. The idDelta arithmetic is modulo
65536.

### Annotation

How about an intelligible description of the use of this format?
Assuming that it intends to describe the same structure as the Apple
True Type format, simply switching to their version would already be a
vast improvement.

### XML Representation

We do not represent explicitly the subHeaderKeys array. Rather, we
represent the subHeaders structure directly, and collect the
subHeaderKeys from which they are referenced in the subHeaderKeys
attribute. The first

The idRangeOffset field can be interpreted only when one knows its
location in the cmap subtable. Since this datum disappears in our XML
representation, the field idRangeOffset is the index of the first
integer corresponding to the subHeader in the glyphIndexArray.

If we are given only the mapping from code points to glyphs, we have no
way of knowing which code points are represented on one byte, and which
are represented in two bytes. Therefore, this format contributes an
attribute singleBytes to record those. We need this attribute only when
we use the 'bunch of mappings' representation; when we have all the
details, the first subheader element carries the single byte code
points.

    XML representation of format 2 cmap subtables ==
          
      cmapsubtable |=
        attribute format { "2" },
    
        ((element subheader {
            attribute subHeaderKeys { text },
            attribute firstCode { text },
            attribute entryCount { text },
            attribute idDelta { text },
            attribute idRangeOffset { text }
          }*,
    
          element glyphIndex {
            attribute v { text }
          })
        |
         (attribute singleBytes { text },
          element map {
            attribute code { text },
            attribute glyph { text }}*))

### Validation

    Validate cmap 2 subtable at stOffset ==
          
      if (! claim (stPrefix + " header", stOffset + 2, 4)) {
        break; }
    
      int stVersion = getuint16 (stOffset + 4);
      if (stVersion > 0) {
        reportError ("cmap@" + stOffset + " table version (" + stVersion
                     + ") not part of the specification"); }
    
      int length = getuint16 (stOffset + 2);

## Format 4: Segment mapping to delta values

### Specification

This is the Microsoft standard character to glyph index mapping table
for fonts that support Unicode ranges other than the range \[U+D800 -
U+DFFF\] (defined as Surrogates Area, in Unicode v 3.0) which is used
for UCS-4 characters. If a font supports this character range (i.e. in
turn supports the UCS-4 characters) a subtable in this format with a
platform specific encoding ID 1 is yet needed, in addition to a subtable
in format 12 with a platform specific encoding ID 10. Please see details
on format 12 below, for fonts that support UCS-4 characters on Windows.

This format is used when the character codes for the characters
represented by a font fall into several contiguous ranges, possibly with
holes in some or all of the ranges (that is, some of the codes in a
range may not have a representation in the font). The format-dependent
data is divided into three parts, which must occur in the following
order:

1.  A four-word header gives parameters for an optimized search of the
    segment list;

2.  Four parallel arrays describe the segments (one segment for each
    contiguous range of codes);

3.  A variable-length array of glyph IDs (unsigned words).

| Type   | Name                       | Description                                                                                                  |
| ------ | -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT | format                     | Format number is set to 4.                                                                                   |
| USHORT | length                     | This is the length in bytes of the subtable.                                                                 |
| USHORT | language                   | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document. |
| USHORT | segCountX2                 | 2 x segCount.                                                                                                |
| USHORT | searchRange                | 2 x (2\*\*floor(log2(segCount)))                                                                             |
| USHORT | entrySelector              | log2(searchRange/2)                                                                                          |
| USHORT | rangeShift                 | 2 x segCount - searchRange                                                                                   |
| USHORT | endCount \[segCount\]      | End characterCode for each segment, last=0xFFFF.                                                             |
| USHORT | reservedPad                | Set to 0.                                                                                                    |
| USHORT | startCount \[segCount\]    | Start character code for each segment.                                                                       |
| SHORT  | idDelta \[segCount\]       | Delta for all character codes in segment.                                                                    |
| USHORT | idRangeOffset \[segCount\] | Offsets into glyphIdArray or 0                                                                               |
| USHORT | glyphIdArray \[\]          | Glyph index array (arbitrary length)                                                                         |

The number of segments is specified by segCount, which is not explicitly
in the header; however, all of the header parameters are derived from
it. The searchRange value is twice the largest power of 2 that is less
than or equal to segCount. For example, if segCount=39, we have the
following:

|               |    |                                 |
| ------------- | -- | ------------------------------- |
| segCountX2    | 78 |                                 |
| searchRange   | 64 | (2 \* largest power of 2 \<=39) |
| entrySelector | 5  | log2 (32)                       |
| rangeShift    | 14 | 2 x 39 - 64                     |

Each segment is described by a startCode and endCode, along with an
idDelta and an idRangeOffset, which are used for mapping the character
codes in the segment. The segments are sorted in order of increasing
endCode values, and the segment values are specified in four parallel
arrays. You search for the first endCode that is greater than or equal
to the character code you want to map. If the corresponding startCode is
less than or equal to the character code, then you use the corresponding
idDelta and idRangeOffset to map the character code to a glyph index
(otherwise, the missingGlyph is returned). For the search to terminate,
the final endCode value must be 0xFFFF. This segment need not contain
any valid mappings. (It can just map the single character code 0xFFFF to
missingGlyph). However, the segment must be present.

If the idRangeOffset value for the segment is not 0, the mapping of
character codes relies on glyphIdArray. The character code offset from
startCode is added to the idRangeOffset value. This sum is used as an
offset from the current location within idRangeOffset itself to index
out the correct glyphIdArray value. This obscure indexing trick works
because glyphIdArray immediately follows idRangeOffset in the font file.
The C expression that yields the glyph index is:

``` 
  *(idRangeOffset[i]/2
    + (c - startCount[i])
    + &idRangeOffset[i])
    
```

The value c is the character code in question, and i is the segment
index in which c appears. If the value obtained from the indexing
operation is not 0 (which indicates missingGlyph), idDelta\[i\] is added
to it to get the glyph index. The idDelta arithmetic is modulo 65536.

If the idRangeOffset is 0, the idDelta value is added directly to the
character code offset (i.e. idDelta\[i\] + c) to get the corresponding
glyph index. Again, the idDelta arithmetic is modulo 65536.

As an example, the variant part of the table to map characters 10-20,
30-90, and 153-480 onto a contiguous range of glyph indices may look
like this:

|                |     |      |      |        |
| -------------- | --- | ---- | ---- | ------ |
| segCountX2:    | 8   |      |      |        |
| searchRange:   | 8   |      |      |        |
| entrySelector: | 4   |      |      |        |
| rangeShift:    | 0   |      |      |        |
| endCode:       | 20  | 90   | 480  | 0Xffff |
| reservedPad:   | 0   |      |      |        |
| startCode:     | 10  | 30   | 153  | 0Xffff |
| idDelta:       | \-9 | \-18 | \-27 | 1      |
| idRangeOffset: | 0   | 0    | 0    | 0      |

This table performs the following mappings:

    10 -> 10 - 9 = 1
    20 -> 20 - 9 = 11
    30 -> 30 - 18 = 12
    90 -> 90 - 18 = 72
    ...and so on.

Note that the delta values could be reworked so as to reorder the
segments.

### Annotation

The first sentence should probably be changed to "... for fonts that
support Unicode BMP characters".

In the table that describes the fields, it seems that the fields
startCount and endCount should instead be startCode and endCode. These
are better names, and are the names used in the text.

In the example, the idDelta of the third range should probably be -80,
so that the character code 153 is mapped to the glyphID 153-80 = 73.

The meaning of the last sentence escapes me. May be it should be
removed?

It seems a necessary property of this format that the segments be
disjoint, yet it is not mentionned explicitly.

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "4" },

    ((element segment {
        attribute startCode { text },
        attribute endCode { text },
        attribute idDelta { text },
        attribute idRangeOffset { text }}*,

      element glyphIndex {
        attribute v { text }})
    |
     (element map {
        attribute code { text },
        attribute glyph { text }}*))
```

### Validation

    Validate cmap 4 subtable at stOffset ==
          
      if (! claim (stPrefix + " header", stOffset + 2, 12)) {
        break; }
    
      int stVersion = getuint16 (stOffset + 4);
      if (stVersion > 0) {
        reportError ("cmap@" + stOffset + " table version (" + stVersion
                     + ") not part of the specification"); }
    
      int length = getuint16 (stOffset + 2);
    
      int segCountX2 = getuint16 (stOffset + 6);
      if (segCountX2 % 2 != 0) {
        reportError ("cmap@" + stOffset + " segCountX2 is not even");
        break; }
      int segCount = segCountX2 / 2;
    
      int searchRange = getuint16 (stOffset + 8);
      // verify searchRange = 2 x (2 ^ (log2 (segCount)))
    
      int entrySelector = getuint16 (stOffset + 10);
      // verify entrySelector = log2 (searchRange/2)
    
      int rangeShift = getuint16 (stOffset + 12);
      if (rangeShift != segCountX2 - searchRange) {
        reportError ("cmap@" + stOffset + " has wrong rangeShift value"); }
    
      if (! claim (stPrefix + " data 1",
                         stOffset + 14, segCount * 8 + 2)) {
        break; }
    
      int lastEndCount = -1;
      int glyphIdSizeNeeded = 0;
    
      for (int s = 0; s < segCount; s++) {
        int endCount = getuint16 (stOffset + 14 + 2*s);
        int startCount = getuint16 (stOffset + 14 + 2*segCount + 2 + 2*s);
    
        if (startCount > endCount) {
          reportError ("cmap@" + stOffset + ", range " + s
                       + ", startCount>endCount");
          break; }
    
        if (startCount <= lastEndCount) {
          reportError ("cmap@" + stOffset + ", range " + s
                       + ", overlaps with previous range"); }
        lastEndCount = endCount;
    
        int rangeOffset = stOffset + 14 + 6*segCount + 2 + 2*s;
        int range = getuint16 (rangeOffset);
    
        if (range != 0) {
          claim (stPrefix + " range " + s,
                       rangeOffset + range, 2 * (endCount - startCount + 1)); }}
    
      if (lastEndCount != 0xffff) {
        reportError ("cmap@" + stOffset + ", last range does not end at 0xffff"); }

## Format 6: Trimmed table mapping

### Specification

| Type   | Name                        | Description                                                                                                  |
| ------ | --------------------------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT | format                      | Format number is set to 6.                                                                                   |
| USHORT | length                      | This is the length in bytes of the subtable.                                                                 |
| USHORT | language                    | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document. |
| USHORT | firstCode                   | First character code of subrange.                                                                            |
| USHORT | entryCount                  | Number of character codes in subrange.                                                                       |
| USHORT | glyphIdArray \[entryCount\] | Array of glyph index values for character codes in the range.                                                |

The firstCode and entryCount values specify a subrange (beginning at
firstCode, length = entryCount) within the range of possible character
codes. Codes outside of this subrange are mapped to glyph index 0. The
offset of the code (from the first code) within this subrange is used as
index to the glyphIdArray, which provides the glyph index value.

### Annotation

It is unclear whether the entryCount can be 0. We assume it can and
recommend to add a sentence to that effect.

This format is very similar to format 0, in that there is an explicit
list of glyph indices for a contiguous range of character code. However,
there are two intersting properties: the range can be bigger than 256;
and more importantly, the glyph indices are USHORT instead of BYTE. So
this format can be used for byte encodings to reach glyphs other than
the first 256 glyphs.

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "6" },

    element map {
      attribute code { text },
      attribute glyph { text }
    }*
```

### Validation

    Validate cmap 6 subtable at stOffset ==
          
      if (! claim (stPrefix + " header", stOffset + 2, 8)) {
        break; }
    
      int stVersion = getuint16 (stOffset + 4);
      if (stVersion > 0) {
        reportError ("cmap@" + stOffset + " table version (" + stVersion
                     + ") not part of the specification"); }
    
      int length = getuint16 (stOffset + 2);
    
      int firstCode = getuint16 (stOffset + 6);
      int entryCount = getuint16 (stOffset + 8);
    
      if (length != 2*entryCount + 10) {
        reportError ("cmap subtable at " + stOffset + " has wrong length"); }
    
      claim (stPrefix + " glyphIdArray", stOffset + 10, 2*entryCount);

## Supporting 4-byte character codes

### Specification

While the four existing [cmap](#chapter.cmap) subtable formats which
currently exist have served us well, the introduction of the Surrogates
Area in Unicode 2.0 has stressed them past the point of utility. This
section specifies three formats, format 8, 10 and 12; which directly
support 4-byte character codes. A major change introduced with these
three formats is a more pure 32-bit orientation. The
[cmap](#chapter.cmap) table version number will continue to be 0x0000,
for those fonts that make use of these formats.

### Annotation

A better formulation in the first sentence could be "... the
introduction of supplemental characters in Unicode 2.0..."

The semicolon after "12" should be changed to a comma.

## Format 8: mixed 16-bit and 32-bit coverage

### Specification

Format 8 is a bit like format 2, in that it provides for mixed-length
character codes. If a font contains characters from the Unicode
Surrogates Area (U+D800-U+DFFF), which are UCS-4 characters; it's likely
that it will also include other, regular 16-bit Unicodes as well. We
therefore need a format to map a mixture of 16-bit and 32-bit character
codes, just as format 2 allows a mixture of 8-bit and 16-bit codes. A
simplifying assumption is made: namely, that there are no 32-bit
character codes which share the same first 16 bits as any 16-bit
character code. This means that the determination as to whether a
particular 16-bit value is a standalone character code or the start of a
32-bit character code can be made by looking at the 16-bit value
directly, with no further information required.

Here's the format 8 subtable format:

| Type   | Name          | Description                                                                                                                                  |
| ------ | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| USHORT | format        | Subtable format; set to 8.                                                                                                                   |
| USHORT | reserved      | Reserved; set to 0                                                                                                                           |
| ULONG  | length        | Byte length of this subtable (including the header)                                                                                          |
| ULONG  | language      | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document.                                 |
| BYTE   | is32 \[8192\] | Tightly packed array of bits (8K bytes total) indicating whether the particular 16-bit (index) value is the start of a 32-bit character code |
| ULONG  | nGroups       | Number of groupings which follow                                                                                                             |

Here follow the individual groups. Each group has the following format:

| Type  | Name          | Description                                                                                                                                                                                               |
| ----- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ULONG | startCharCode | First character code in this group; note that if this group is for one or more 16-bit character codes (which is determined from the is32 array), this 32-bit value will have the high 16-bits set to zero |
| ULONG | endCharCode   | Last character code in this group; same condition as listed above for the startCharCode                                                                                                                   |
| ULONG | startGlyphID  | Glyph index corresponding to the starting character code                                                                                                                                                  |

A few notes here. The endCharCode is used, rather than a count, because
comparisons for group matching are usually done on an existing character
code, and having the endCharCode be there explicitly saves the necessity
of an addition per group. Groups must be sorted by increasing
startCharCode. A group's endCharCode must be less than the startCharCode
of the following group, if any.

To determine if a particular word (cp) is the first half of 32-bit code
points, one can use an expression such as ( is32\[ cp / 8 \] & ( 1 \<\<
( 7 - ( cp % 8 ) ) ) ). If this is non-zero, then the word is the first
half of a 32-bit code point.

0 is not a special value for the high word of a 32-bit code point. A
font may not have both a glyph for the code point 0x0000 and glyphs for
code points with a high word of 0x0000.

The presence of the packed array of bits indicating whether a particular
16-bit value is the start of a 32-bit character code is useful even when
the font contains no glyphs for a particular 16-bit start value. This is
because the system software often needs to know how many bytes ahead the
next character begins, even if the current character maps to the missing
glyph. By including this information explicitly in this table, no
"secret" knowledge needs to be encoded into the OS.

Although this format might work advantageously on some platforms for
non-Unicode encodings, Microsoft does not support it for Unicode encoded
UCS-4 characters.

### Annotation

First paragraph, second sentence, should be: "If a font maps Unicode
supplemental characters, it's likely to map Unicode BMP characters as
well."

For coherence with the other formats, the description of the format
field should be "Format number is set to 8" and the description of the
length field should be "This is the length in bytes of the subtable."

This format is dubious and would probably best be deprecated. If For
Unicode encodings, it is useful only for UTF-16 (the only version that
has 16 bit code units), so spending 8K bytes to is If the intent is
really for a Unicode encodings, then it is known

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "8" },
    attribute singleWords { text },

    ((element group {
        attribute firstCode { text },
        attribute lastCode { text },
        attribute firstGlyph { text }}*)
    |
     (element map {
        attribute code { text },
        attribute glyph { text }}*))
```

## Format 10: Trimmed array

### Specification

Format 10 is a bit like format 6, in that it defines a trimmed array for
a tight range of 32-bit character codes:

| Type   | Name          | Description                                                                                                  |
| ------ | ------------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT | format        | Subtable format; set to 10.                                                                                  |
| USHORT | reserved      | Reserved; set to 0                                                                                           |
| ULONG  | length        | Byte length of this subtable (including the header)                                                          |
| ULONG  | language      | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document. |
| ULONG  | startCharCode | First character code covered                                                                                 |
| ULONG  | numChars      | Number of character codes covered                                                                            |
| USHORT | glyphs \[\]   | Array of glyph indices for the character codes covered                                                       |

This format is not supported by Microsoft.

### Annotation

For coherence with the other formats, the description of the format
field should be "Format number is set to 10" and the description of the
length field should be "This is the length in bytes of the subtable."

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "10" },

    element map {
      attribute code { text },
      attribute glyph { text }
    }*
```

## Format 12: Segmented coverage

### Specification

This is the Microsoft standard character to glyph index mapping table
for fonts supporting the UCS-4 characters in the Unicode Surrogates Area
(U+D800 - U+DFFF). It is a bit like format 4, in that it defines
segments for sparse representation in 4-byte character space. Here's the
subtable format:

| Type   | Name     | Description                                                                                                  |
| ------ | -------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT | format   | Subtable format; set to 12.                                                                                  |
| USHORT | reserved | Reserved; set to 0                                                                                           |
| ULONG  | length   | Byte length of this subtable (including the header)                                                          |
| ULONG  | language | Please see [Note on the language field in [cmap](#chapter.cmap) subtables](#language_note) in this document. |
| ULONG  | nGroups  | Number of groupings which follow                                                                             |

Fonts providing Unicode encoded UCS-4 character support for Windows 2000
and later, need to have a subtable with platform ID 3, platform specific
encoding ID 1 in format 4; and in addition, need to have a subtable for
platform ID 3, platform specific encoding ID 10 in format 12. Please
note, that the content of format 12 subtable, needs to be a super set of
the content in the format 4 subtable. The format 4 subtable needs to be
in the cmap table to enable backward compatibility needs.

Here follow the individual groups, each of which has the following
format:

| Type  | Name          | Description                                              |
| ----- | ------------- | -------------------------------------------------------- |
| ULONG | startCharCode | First character code in this group                       |
| ULONG | endCharCode   | Last character code in this group                        |
| ULONG | startGlyphID  | Glyph index corresponding to the starting character code |

Groups must be sorted by increasing startCharCode. A group's endCharCode
must be less than the startCharCode of the following group, if any. The
endCharCode is used, rather than a count, because comparisons for group
matching are usually done on an existing character code, and having the
endCharCode be there explicitly saves the necessity of an addition per
group.

### Annotation

First paragraph, first sentence should be reworded: "... for fonts
supporting Unicode supplemental characters." Similarly, second
paragraph, first sentence should be reworded: "Fonts providing support
for Unicode supplemental characters..."

For coherence with the other formats, the description of the format
field should be "Format number is set to 12" and the description of the
length field should be "This is the length in bytes of the subtable."

### XML Representation

``` 
 ==
      
  cmapsubtable |=
    attribute format { "12" },

    ((element map {
        attribute code { text },
        attribute glyph { text },
        attribute count { text }}*)

    |(element map {
        attribute code { text },
        attribute glyph { text }}*))
```

## Format 14: Unicode Variation Sequences

### Specification

Subtable format 14 specifies the Unicode Variation Sequences (UVSes)
supported by the font. A Variation Sequence, according to the Unicode
Standard, comprises a base character followed by a variation selector;
e.g. \<U+82A6, U+E0101\>.

The subtable partitions the UVSes supported by the font into two
categories: “default” and “non-default” UVSes. Given a UVS, if the glyph
obtained by looking up the base character of that sequence in the
Unicode cmap subtable (i.e. the UCS-4 or the BMP cmap subtable) is the
glyph to use for that sequence, then the sequence is a “default” UVS;
otherwise it is a “non-defaultJ=f UVS, and the glyph to use for that
sequence is specified in the format 14 subtable itself.

The example below shows how a font vendor can use format 14 for a
JIS-2004-aware font.

| Type   | Name                  | Description                                         |
| ------ | --------------------- | --------------------------------------------------- |
| USHORT | format                | Subtable format; set to 14.                         |
| ULONG  | length                | Byte length of this subtable (including the header) |
| ULONG  | numVarSelectorRecords | Number of Variation Selector Records                |

Format 14 header

This is immediately followed by 'numVarSelectorRecords' Variation
Selector Records.

| Type   | Name                | Description                                |
| ------ | ------------------- | ------------------------------------------ |
| UINT24 | varSelector         | Variation selector                         |
| ULONG  | defaultUVSOffset    | Offset to Default UVS Table. May be 0.     |
| ULONG  | nonDefaultUVSOffset | Offset to Non-Default UVS Table. May be 0. |

Variation Selector Record

The Variation Selector Records are sorted in increasing order of
'varSelector'. No two records may have the same 'varSelector'. All
offsets in a record are relative to the beginning of the format 14 cmap
subtable.

A Variation Selector Record and the data its offsets point to specify
those UVSes supported by the font for which the variation selector is
the 'varSelector' value of the record. The base characters of the UVSes
are stored in the tables pointed to by the offsets. The UVSes are
partitioned by whether they are default or non-default UVSes.

Glyph IDs to be used for non-default UVSes are specified in the
Non-Default UVS table.

Default UVS Table

A Default UVS Table is simply a range-compressed list of Unicode scalar
values, representing the base characters of the default UVSes which use
the 'varSelector' of the associated Variation Selector Record.

| Type  | Name                  | Description                  |
| ----- | --------------------- | ---------------------------- |
| ULONG | numUnicodeValueRanges | Number of ranges that follow |

Default UVS Table header

This is immediately followed by 'numUnicodeValueRanges' Unicode Value
Ranges, each of which represents a contiguous range of Unicode values.

| Type   | Name              | Description                                 |
| ------ | ----------------- | ------------------------------------------- |
| UINT24 | startUnicodeValue | First value in this range                   |
| BYTE   | additionalCount   | Number of *additional* values in this range |

Unicode Value Range

For example, the range U+4E4D...U+4E4F (3 values) will set
'startUnicodeValue' to 0x004E4D and 'additionalCount' to 2. A singleton
range will set 'additionalCount' to 0.

('startUnicodeValue' + 'additionalCount') must not exceed 0xFFFFFF.

The Unicode Value Ranges are sorted in increasing order of
'startUnicodeValue'. The ranges must not overlap; i.e.,
('startUnicodeValue' + 'additionalCount') must be less than the
'startUnicodeValue' of the following range (if any).

Non-Default UVS Table

A Non-Default UVS Table is a list of pairs of Unicode scalar values and
glyph IDs. The Unicode values represent the base characters of all
non-default UVSes which use the 'varSelector' of the associated
Variation Selector Record, and the glyph IDs specify the glyph IDs to
use for the UVSes.

| Type  | Name           | Description                        |
| ----- | -------------- | ---------------------------------- |
| ULONG | numUVSMappings | Number of UVS Mappings that follow |

Non-Default UVS Table header

This is immediately followed by 'numUVSMappings' UVS Mappings.

| Type   | Name         | Description                   |
| ------ | ------------ | ----------------------------- |
| UINT24 | unicodeValue | Base Unicode value of the UVS |
| USHORT | glyphID      | Glyph ID of the UVS           |

UVS Mapping

The UVS Mappings are sorted in increasing order of 'unicodeValue'. No
two mappings in this table may have the same 'unicodeValue' values.

Example

Here is an example of how a format 14 cmap subtable may be used in a
font that is aware of JIS-2004 variant glyphs. The CIDs (character IDs)
in this example refer to those in the Adobe Character Collection
'Adobe-Japan1', and may be assumed to be identical to the glyph IDs in
the font in our example.

JIS-2004 changed the default glyph variants for some of its code points.
For example:

JIS-90: U+82A6 -\> CID 1142

JIS-2004: U+82A6 -\> CID 7961

Both of these glyph variants are supported through the use of UVSes, as
the following examples from Unicode's UVS registry show:

U+82A6 U+E0100 -\> CID 1142

U+82A6 U+E0101 -\> CID 7961

If the font wants to support the JIS-2004 variants by default, it will:

  - encode glyph ID 7961 at U+82A6 in the Unicode cmap subtable,

  - specify \<U+82A6, U+E0101\> in the UVS cmap subtable's Default UVS
    Table ('varSelector' will be 0x0E0101 and 'defaultUVSOffset' will
    point to data containing a 0x0082A6 Unicode value)

  - specify \<U+82A6, U+E0100\> -\> glyph ID 1142 in the UVS cmap
    subtable's Non-Default UVS Table ('varSelector' will be 0x0E0100 and
    'nonDefaultBaseUVOffset' will point to data containing a
    'unicodeValue' 0x82A6 and 'glyphID' 1142).

If, however, the font wants to support the JIS-90 variants by default,
it will:

  - encode glyph ID 1142 at U+82A6 in the Unicode cmap subtable,
    
    specify \<U+82A6, U+E0100\> in the UVS cmap subtable's Default UVS
    Table

  - specify \<U+82A6, U+E0101\> -\> glyph ID 7961 in the UVS cmap
    subtables Non-Default UVS Table

### XML Representation

``` 
 ==
      

  defaultUVSTable =
    element defaultMappings {
      element range {
        attribute start { text },
        attribute additionalCount { text }}* }

  standaloneDefaultUVS =
    element defaultUVSTable { attribute id { text }, defaultUVSTable }

  defaultUVSOffset = attribute defaultUVSTable { text } | defaultUVSTable


  nonDefaultUVSTable =
    element nonDefaultMappings {
      element map {
        attribute usv { text },
        attribute gid  { text }}* }

  standaloneNonDefaultUVS =
    element nonDefaultUVSSubtable { attribute id { text }, nonDefaultUVSTable }

  nonDefaultUVSOffset = attribute nonDefaultUVSTable { text } | nonDefaultUVSTable

  cmapsubtable |=
    attribute format { "14" },

    element variation-selector {
      attribute vs { text },
      defaultUVSOffset,
      nonDefaultUVSOffset }*
```

## Various test fonts

