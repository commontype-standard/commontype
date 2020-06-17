# VORG - Vertical Origin Table

## Overview

### Specification

This table specifies the y coordinate of the vertical origin of every
glyph in the font.

This table may be optionally present only in CFF OpenType fonts. If
present in TrueType OpenType fonts it must be ignored by font clients,
just as any other unrecognized table would be. This is because this
table is not needed for TrueType OpenType fonts: the Vertical Metrics
([vmtx](#chapter.vmtx)) and Glyph Data ([glyf](#chapter.glyf)) tables in
TrueType OpenType fonts provide all the information necessary to
accurately calculate the y coordinate of a glyph's vertical origin. See
the "Vertical Origin and Advance Height" section in the
[vmtx](#chapter.vmtx) table specification for more details.

This table was added to version 1.3 of the OpenType specification. Note
that the [vmtx](#chapter.vmtx) and Vertical Header
([vhea](#chapter.vhea)) tables continue to be required for all OpenType
fonts that support vertical writing. Advance heights must continue to be
obtained from the [vmtx](#chapter.vmtx) table; that is the only place
they are stored.

If a [VORG](#chapter.VORG) table is present in a CFF OpenType font, a
font client may choose to obtain the y coordinate of a glyph’s vertical
origin either:

  - directly from the [VORG](#chapter.VORG), or:

  - by first calculating the top of the glyph's bounding box from the
    CFF charstring data and then adding to it the glyph's top side
    bearing from the [vmtx](#chapter.vmtx) table.

The former method offers the advantage of increased accuracy and
efficiency, since bounding box results calculated from the CFF
charstring as in the latter method can differ depending on the rounding
decisions and data types of the bounding box algorithm. The latter
method provides compatibility for font clients who are either unaware of
or choose not to support the [VORG](#chapter.VORG).

Thus, the [VORG](#chapter.VORG) doesn't add any new font metric values
per se; it simply improves accuracy and efficiency for CFF OpenType font
clients, since the intermediate step of calculating bounding boxes from
the CFF charstring is rendered unnecessary.

See the section "OpenType CJK Font Guidelines" for more information
about constructing CJK (Chinese, Japanese, and Korean) fonts.

## Vertical Origin Table Format

### Specification

| Type   | Name                  | Description                                                                                                                                                             |
| ------ | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USHORT | majorVersion          | Major version (starting at 1). Set to 1.                                                                                                                                |
| USHORT | minorVersion          | Minor version (starting at 0). Set to 0.                                                                                                                                |
| SHORT  | defaultVertOriginY    | The y coordinate of a glyph's vertical origin, in the font's design coordinate system, to be used if no entry is present for the glyph in the vertOriginYMetrics array. |
| USHORT | numVertOriginYMetrics | Number of elements in the vertOriginYMetrics array.                                                                                                                     |

This is immediately followed by the vertOriginYMetrics array (if
numVertOriginYMetrics is non-zero), which has numVertOriginYMetrics
elements of the following format:

| Type   | Name        | Description                                                                                                  |
| ------ | ----------- | ------------------------------------------------------------------------------------------------------------ |
| USHORT | glyphIndex  | Glyph index.                                                                                                 |
| SHORT  | vertOriginY | Y coordinate, in the font's design coordinate system, of the vertical origin of glyph with index glyphIndex. |

This array must be sorted by increasing glyphIndex, and must not have
more than one element with the same glyphIndex. In a size-optimized
implementation, glyphs whose vertical origin's y coordinate equals
defaultVertOriginY will not have an entry in this array.

If all glyphs in a font share the same defaultVertOriginY value, the
length of the [VORG](#chapter.VORG) table will be 8 bytes in a
size-optimized implementation, since the vertOriginYMetrics array will
be absent.

Typically only the full-width Latin glyphs in an East Asian font will
have entries in the vertOriginYMetrics array. Glyphs rotated for
vertical writing, as used in the Vertical Alternates and Rotation
('vrt2') feature, for example, can take advantage of the default value
if they are designed appropriately.

In the following example of a complete [VORG](#chapter.VORG) table for a
1000-unit-em font, every glyph in the font is specified as having a
vertOriginY of 880 except for glyphs with glyph indexes 10, 12, and 13:

    majorVersion         =1
    minorVersion         =0
    defaultVertOriginY   =880
    numVertOriginYMetrics=3
    --- vertOriginYMetrics[index]=(glyphIndex,vertOriginY)
    [0]=(10,889)
    [1]=(12,861)
    [2]=(13,849)

### XML Representation

    ?? ==
          
    VORG =
      element VORG {
        attribute major { "1" },
        attribute minor { "0" },
        attribute defaultVertOriginY { text },
    
        element vMetric {
          attribute gid { text },
          attribute vertOriginY { text }
        }*
      }

