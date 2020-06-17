# OpenType Tables

## OpenType Tables

### Specification

Whether TrueType or PostScript outlines are used in an OpenType font,
the following tables are required for the font to function correctly:

| Tag                   | Name                              |
| --------------------- | --------------------------------- |
| [cmap](#chapter.cmap) | Character to glyph mapping        |
| [head](#chapter.head) | Font header                       |
| [hhea](#chapter.hhea) | Horizontal header                 |
| [hmtx](#chapter.hmtx) | Horizontal metrics                |
| [maxp](#chapter.maxp) | Maximum profile                   |
| [name](#chapter.name) | Naming table                      |
| [OS/2](#chapter.OS2)  | OS/2 and Windows specific metrics |
| [post](#chapter.post) | PostScript information            |

Required Tables

For OpenType fonts based on TrueType outlines, the following tables are
used:

| Tag                   | Name                |
| --------------------- | ------------------- |
| [cvt](#chapter.cvt)   | Control Value Table |
| [fpgm](#chapter.fpgm) | Font program        |
| [glyf](#chapter.glyf) | Glyph data          |
| [loca](#chapter.loca) | Index to location   |
| [prep](#chapter.prep) | CVT Program         |

Tables Related to TrueType Outlines

The PostScript font extensions define a new set of tables containing
data specific to PostScript fonts that are used instead of the tables
listed above.

| Tag                   | Name                                          |
| --------------------- | --------------------------------------------- |
| [CFF](#chapter.CFF)   | PostScript font program (compact font format) |
| [VORG](#chapter.VORG) | Vertical Origin                               |

Tables Related to PostScript Outlines

Multiple Master support in OpenType, has been discontinued as of version
1.3 of the specification. The 'fvar', 'MMSD', 'MMFX' tables have hence
been removed.

There are also several optional tables that support vertical layout as
well as other advanced typographic functions:

| Tag                   | Name                    |
| --------------------- | ----------------------- |
| [BASE](#chapter.BASE) | Baseline data           |
| [GDEF](#chapter.GDEF) | Glyph definition data   |
| [GPOS](#chapter.GPOS) | Glyph positioning data  |
| [GSUB](#chapter.GSUB) | Glyph substitution data |
| [JSTF](#chapter.JSTF) | Justification data      |

Advanced Typographic Tables

For information on common table formats, please see [OpenType Layout
Common Table Formats](#common_tables).

OpenType fonts may also contain bitmaps of glyphs, in addition to
outlines. Hand-tuned bitmaps are especially useful in OpenType fonts for
representing complex glyphs at very small sizes. If a bitmap for a
particular size is provided in a font, it will be used by the system
instead of the outline when rendering the glyph. (Note: ATM does not
currently support hinted bitmaps in OpenType fonts.)

| Tag                   | Name                          |
| --------------------- | ----------------------------- |
| [EBDT](#chapter.EBDT) | Embedded bitmap data          |
| [EBLC](#chapter.EBLC) | Embedded bitmap location data |
| [EBSC](#chapter.EBSC) | Embedded bitmap scaling data  |

Tables Related to Bitmap Glyphs

| Tag                   | Name                         |
| --------------------- | ---------------------------- |
| [DSIG](#chapter.DSIG) | Digital signature            |
| [gasp](#chapter.gasp) | Grid-fitting/Scan-conversion |
| [hdmx](#chapter.hdmx) | Horizontal device metrics    |
| [kern](#chapter.kern) | Kerning                      |
| [LTSH](#chapter.LTSH) | Linear threshold data        |
| [PCLT](#chapter.PCLT) | PCL 5 data                   |
| [VDMX](#chapter.VDMX) | Vertical device metrics      |
| [vhea](#chapter.vhea) | Vertical Metrics header      |
| [vmtx](#chapter.vmtx) | Vertical Metrics             |

Other OpenType Tables

### Annotation

The sentence that introduces the tables related to PostScript outlines
should probably be better phrased: "For OpenType fonts based on
PostScript outlines, the following tables are used:" It parallels the
sentence for TT outlines.

The sentence that points to the "OpenType Layout Common Table Formats"
should probably be moved to the paragraph that introduces the Advanced
Typographic Tables. Currently, it is between the paragraph that
introduces bitmap related tables and the list of those tables.

