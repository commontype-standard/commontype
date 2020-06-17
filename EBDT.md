# EBDT - Embedded Bitmap Data Table

## Overview

### Specification

Three tables are used to embed bitmaps in OpenType fonts. They are the
[EBLC](#chapter.EBLC) table for embedded bitmap locators, the
[EBDT](#chapter.EBDT) table for embedded bitmap data, and the
[EBSC](#chapter.EBSC) table for embedded bitmap scaling information.

OpenType embedded bitmaps are also called 'sbits' (for "scaler
bitmaps"). A set of bitmaps for a face at a given size is called a
strike.

The [EBLC](#chapter.EBLC) table identifies the sizes and glyph ranges of
the sbits, and keeps offsets to glyph bitmap data in indexSubTables. The
[EBDT](#chapter.EBDT) table then stores the glyph bitmap data, in a
number of different possible formats. Glyph metrics information may be
stored in either the [EBLC](#chapter.EBLC) or [EBDT](#chapter.EBDT)
table, depending upon the indexSubTable and glyph bitmap data formats.
The [EBSC](#chapter.EBSC) table identifies sizes that will be handled by
scaling up or scaling down other sbit sizes.

The [EBDT](#chapter.EBDT) table is a superset of Apple's AAT (Apple
Advanced Typography) 'bdat' table.

The [EBDT](#chapter.EBDT) table begins with a header containing simply
the table version number.

| Type  | Name    | Description                     |
| ----- | ------- | ------------------------------- |
| FIXED | version | Initially defined as 0x00020000 |

?

The rest of the [EBDT](#chapter.EBDT) table is a collection of bitmap
data. The data can be in a number of possible formats, indicated by
information in the [EBLC](#chapter.EBLC) table. Some of the formats
contain metric information plus image data, and other formats contain
only the image data. Long word alignment is not required for these sub
tables; byte alignment is sufficient.

There are also two different formats for glyph metrics: big glyph
metrics and small glyph metrics. Big glyph metrics define metrics
information for both horizontal and vertical layouts. This is important
in fonts (such as Kanji) where both types of layout may be used. Small
glyph metrics define metrics information for one layout direction only.
Which direction applies, horizontal or vertical, is determined by the
'flags' field in the bitmapSizeTable field of the [EBLC](#chapter.EBLC)
table.

| Type | Name         |
| ---- | ------------ |
| BYTE | height       |
| BYTE | width        |
| CHAR | horiBearingX |
| CHAR | horiBearingY |
| BYTE | horiAdvance  |
| CHAR | vertBearingX |
| CHAR | vertBearingY |
| BYTE | vertAdvance  |

bigGlyphMetrics

| Type | Name     |
| ---- | -------- |
| BYTE | height   |
| BYTE | width    |
| CHAR | BearingX |
| CHAR | BearingY |
| BYTE | Advance  |

smallGlyphMetrics

The nine different formats currently defined for glyph bitmap data are
listed and described below. Different formats are better for different
purposes. Apple 'bdat' tables support only formats 1 through 7.

In all formats, if the bitDepth is greater than 1, all of a pixel's bits
are stored consecutively in memory, and all of a row's pixels are stored
consecutively.

Note: Each of these formats can contain black/white or grayscale bitmaps
depending on the setting of the bitDepth field in the
[EBLC](#chapter.EBLC) table. For performance reasons, we recommend using
a byte-aligned format for embedded bitmaps with bitDepth of 8.

## Format 1: small metrics, byte-aligned data

### Specification

| Type              | Name         | Description                       |
| ----------------- | ------------ | --------------------------------- |
| smallGlyphMetrics | smallMetrics | Metrics information for the glyph |
| VARIABLE          | image data   | Byte-aligned bitmap data          |

Glyph bitmap format 1 consists of small metrics records (either
horizontal or vertical depending on the bitmapSizeTable 'flag' value in
the [EBLC](#chapter.EBLC) table) followed by byte aligned bitmap data.
The bitmap data begins with the most significant bit of the first byte
corresponding to the top-left pixel of the bounding box, proceeding
through succeeding bits moving left to right. The data for each row is
padded to a byte boundary, so the next row begins with the most
significant bit of a new byte. 1 bits correspond to black, and 0 bits to
white.

## Format 2: small metrics, bit-aligned data

### Specification

| Type              | Name         | Description                       |
| ----------------- | ------------ | --------------------------------- |
| smallGlyphMetrics | smallMetrics | Metrics information for the glyph |
| VARIABLE          | image data   | Bit-aligned bitmap data           |

?

Glyph bitmap format 2 is the same as format 1 except that the bitmap
data is bit aligned. This means that the data for a new row will begin
with the bit immediately following the last bit of the previous row. The
start of each glyph must be byte aligned, so the last row of a glyph may
require padding. This format takes a little more time to parse, but
saves file space compared to format 1.

## Format 3: (obsolete)

### Specification

Format 3 is obsolete.

## Format 4: (not supported) metrics in EBLC, compressed data

### Specification

Glyph bitmap format 4 is a compressed format used by Apple in some of
their Far East fonts. MS has not implemented it in our rasterizer.

## Format 5: metrics in EBLC, bit-aligned image data only

### Specification

| Type     | Name       | Description             |
| -------- | ---------- | ----------------------- |
| VARIABLE | image data | Bit-aligned bitmap data |

?

Glyph bitmap format 5 is similar to format 2 except that no metrics
information is included, just the bit aligned data. This format is for
use with [EBLC](#chapter.EBLC) indexSubTable format 2 or format 5, which
will contain the metrics information for all glyphs. It works well for
Kanji fonts.

The rasterizer recalculates sbit metrics for Format 5 bitmap data,
allowing Windows to report correct ABC widths, even if the bitmaps have
white space on either side of the bitmap image. This allows fonts to
store monospaced bitmap glyphs in the efficient Format 5 without
breaking Windows GetABCWidths call.

## Format 6: big metrics, byte-aligned data

### Specification

| Type            | Name       | Description                       |
| --------------- | ---------- | --------------------------------- |
| bigGlyphMetrics | bigMetrics | Metrics information for the glyph |
| VARIABLE        | image data | Byte-aligned bitmap data          |

?

Glyph bitmap format 6 is the same as format 1 except that is uses big
glyph metrics instead of small.

## Format 7: big metrics, bit-aligned data

### Specification

| Type            | Name       | Description                       |
| --------------- | ---------- | --------------------------------- |
| bigGlyphMetrics | bigMetrics | Metrics information for the glyph |
| VARIABLE        | image data | Bit-aligned bitmap data           |

Glyph bitmap format 7 is the same as format 2 except that is uses big
glyph metrics instead of small.

## ebdtComponent; array used by Formats 8 and 9

### Specification

| Type   | Name      | Description                |
| ------ | --------- | -------------------------- |
| USHORT | glyphCode | Component glyph code       |
| CHAR   | xOffset   | Position of component left |
| CHAR   | yOffset   | Position of component top  |

The component array, used by Formats 8 and 9, contains the glyph code of
the component, which can be looked up in the [EBLC](#chapter.EBLC)
table, as well as xOffset and yOffset values which tell where to
position the top-left corner of the component in the composite. Nested
composites (a composite of composites) are allowed, and the number of
nesting levels is determined by implementation stack space.

## Format 8: small metrics, component data

### Specification

| Type              | Name                 | Description                       |
| ----------------- | -------------------- | --------------------------------- |
| smallGlyphMetrics | smallMetrics         | Metrics information for the glyph |
| BYTE              | pad                  | Pad to short boundary             |
| USHORT            | numComponents        | Number of components              |
| ebdtComponent     | componentArray \[n\] | Glyph code, offset array          |

## Format 9: big metrics, component data

### Specification

| Type            | Name                 | Description                       |
| --------------- | -------------------- | --------------------------------- |
| bigGlyphMetrics | bigMetrics           | Metrics information for the glyph |
| USHORT          | numComponents        | Number of components              |
| ebdtComponent   | componentArray \[n\] | Glyph code, offset array          |

Glyph bitmap formats 8 and 9 are used for composite bitmaps. For
accented characters and other composite glyphs it may be more efficient
to store a copy of each component separately, and then use a composite
description to construct the finished glyph. The composite formats allow
for any number of components, and allow the components to be positioned
anywhere in the finished glyph. Format 8 uses small metrics, and format
9 uses big metrics.

