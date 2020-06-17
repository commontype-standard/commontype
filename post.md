# post - PostScript

## Introduction

### Specification

This table contains additional information needed to use TrueType or
OpenType fonts on PostScript printers. This includes data for the
FontInfo dictionary entry and the PostScript names of all the glyphs.
For more information about PostScript names, see the Adobe document
[Unicode and Glyph
Names](http://partners.adobe.com/asn/developer/typeforum/unicodegm.html).

Versions 1.0, 2.0, and 2.5 refer to TrueType fonts and OpenType fonts
with TrueType data. OpenType fonts with TrueType data may also use
Version 3.0. OpenType fonts with CFF data use Version 3.0 only.

The table begins as follows:

| Type  | Name               | Description                                                                                                                                                                                                                                                                                                                                                                                     |
| ----- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed | Version            | 0x00010000 for version 1.0, 0x00020000 for version 2.0, 0x00025000 for version 2.5 (deprecated), 0x00030000 for version 3.0                                                                                                                                                                                                                                                                     |
| Fixed | italicAngle        | Italic angle in counter-clockwise degrees from the vertical. Zero for upright text, negative for text that leans to the right (forward).                                                                                                                                                                                                                                                        |
| FWord | underlinePosition  | This is the suggested distance of the top of the underline from the baseline (negative values indicate below baseline). The PostScript definition of this FontInfo dictionary key (the y coordinate of the center of the stroke) is not used for historical reasons. The value of the PostScript key may be calculated by subtracting half the underlineThickness from the value of this field. |
| FWord | underlineThickness | Suggested values for the underline thickness.                                                                                                                                                                                                                                                                                                                                                   |
| ULONG | isFixedPitch       | Set to 0 if the font is proportionally spaced, non-zero if the font is not proportionally spaced (i.e. monospaced).                                                                                                                                                                                                                                                                             |
| ULONG | minMemType42       | Minimum memory usage when an OpenType font is downloaded.                                                                                                                                                                                                                                                                                                                                       |
| ULONG | maxMemType42       | Maximum memory usage when an OpenType font is downloaded.                                                                                                                                                                                                                                                                                                                                       |
| ULONG | minMemType1        | Minimum memory usage when an OpenType font is downloaded as a Type 1 font.                                                                                                                                                                                                                                                                                                                      |
| ULONG | maxMemType1        | Maximum memory usage when an OpenType font is downloaded as a Type 1 font.                                                                                                                                                                                                                                                                                                                      |

The last four entries in the table are present because PostScript
drivers can do better memory management if the virtual memory (VM)
requirements of a downloadable OpenType font are known before the font
is downloaded. This information should be supplied if known. If it is
not known, set the value to zero. The driver will still work but will be
less efficient.

Maximum memory usage is minimum memory usage plus maximum runtime memory
use. Maximum runtime memory use depends on the maximum band size of any
bitmap potentially rasterized by the font scaler. Runtime memory usage
could be calculated by rendering characters at different point sizes and
comparing memory use.

If the version is 1.0 or 3.0, the table ends here. The additional
entries for versions 2.0 and 2.5 are shown below. Apple has defined a
version 4.0 for use with Apple's AAT (Apple Advanced Typography), which
is described in their documentation.

**Version 1.0**

This TrueType-based font file contains exactly the 258 glyphs in the
standard Macintosh TrueType font file (see [The WGL4.0 Character
Set](http://www.microsoft.com/typography/otspec/WGL4.htm) chapter for a
list of the Macintosh glyphs). As a result, the glyph names are taken
from the system with no storage required by the font.

**Version 2.0**

This is the version required by TrueType-based fonts to be used on
Windows.

| Type   | Name                         | Description                                                                                           |
| ------ | ---------------------------- | ----------------------------------------------------------------------------------------------------- |
| USHORT | numberOfGlyphs               | Number of glyphs (this should be the same as numGlyphs in [maxp](#chapter.maxp) table).               |
| USHORT | glyphNameIndex \[numGlyphs\] | This is not an offset, but is the ordinal number of the glyph in [post](#chapter.post) string tables. |
| CHAR   | names \[numberNewGlyphs\]    | Glyph names with length bytes \[variable\] (a Pascal string).                                         |

This TrueType-based font file contains glyphs not in the standard
Macintosh set or the ordering of the glyphs in the TrueType font file is
non-standard (again, for the Macintosh). The glyph name array maps the
glyphs in this font to name index. If the name index is between 0 and
257, treat the name index as a glyph index in the Macintosh standard
order. If the name index is between 258 and 32767, then subtract 258 and
use that to index into the list of Pascal strings at the end of the
table. Thus a given font may map some of its glyphs to the standard
glyph names, and some to its own names.

Index numbers 32768 through 65535 are reserved for future use. If you do
not want to associate a PostScript name with a particular glyph, use
index number 0 which points the name .notdef.

**Version 2.5**

This version of the [post](#chapter.post) table has been deprecated as
of OpenType Specification v1.3.

This version provides a space saving table for TrueType-based fonts
which contain a pure subset of, or a simple reordering of, the standard
Macintosh glyph set.

| Type   | Name                 | Description                                                  |
| ------ | -------------------- | ------------------------------------------------------------ |
| USHORT | numberOfGlyphs       | Number of glyphs                                             |
| CHAR   | offset \[numGlyphs\] | Difference between graphic index and standard order of glyph |

This version is useful for TrueType-based font files that contain only
glyphs in the standard Macintosh glyph set but which have those glyphs
arranged in a non-standard order or which are missing some glyphs. The
table contains one byte for each glyph in the font file. The byte is
treated as a signed offset that maps the glyph index used in this font
into the standard glyph index. In other words, assuming that the font
contains the three glyphs A, B, and C which are the 37th, 38th, and 39th
glyphs in the standard ordering, the [post](#chapter.post) table would
contain the bytes +36, +36, +36. This format has been deprecated by
Apple, as of February 2000.

**Version 3.0**

This version is used by OpenType fonts with TrueType or CFF data. The
version makes it possible to create a special font that is not burdened
with a large [post](#chapter.post) table set of glyph names.

This version specifies that no PostScript name information is provided
for the glyphs in this font file. The printing behavior of this version
on PostScript printers is unspecified, except that it should not result
in a fatal or unrecoverable error. Some drivers may print nothing, other
drivers may attempt to print using a default naming scheme.

Windows makes use of the italic angle value in the [post](#chapter.post)
table but does not actually *require* any glyph names to be stored as
Pascal strings.

### XML Representation

    ?? ==
          
    post |=
      element post {
        attribute major { "1" },
        attribute minor { "0" },
        post_common
      }
    
    post |=
      element post {
        attribute major { "2" },
        attribute minor { "0" },
        post_common,
        element glyph {
          attribute id { text },
          attribute name { text }
        }*
      }
    
    post |=
      element post {
        attribute major { "2" },
        attribute minor { "5" },
        post_common,
        element offset {
          attribute v { text }
        }*
      }
    
    post |=
      element post {
        attribute major { "3" },
        attribute minor { "0" },
        post_common
      }
    
    post_common =
      element italicAngle {
        attribute int { text },
        attribute frac { text }
      },
      element underline {
        attribute position { text },
        attribute thickness { text }
      },
      element isFixedPitch {
        attribute v { yesOrNo }
      },
      element memType42 {
        attribute min { text },
        attribute max { text }
      },
      element memType1 {
        attribute min { text },
        attribute max { text }
      }

