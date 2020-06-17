# hdmx - Horizontal Device Metrics

## Overview

### Specification

The hdmx table relates to OpenType fonts with TrueType outlines. The
Horizontal Device Metrics table stores integer advance widths scaled to
particular pixel sizes. This allows the font manager to build integer
width tables without calling the scaler for each glyph. Typically this
table contains only selected screen sizes. This table is sorted by pixel
size. The checksum for this table applies to both subtables listed.

Note that for non-square pixel grids, the character width (in pixels)
will be used to determine which device record to use. For example, a 12
point character on a device with a resolution of 72x96 would be 12
pixels high, and 16 pixels wide. The hdmx device record for 16 pixel
characters would be used.

When the hdmx table is used, bit 2 of the flag field in the
[head](#chapter.head) table must be set to 1 to indicate that
instructions may depend on point size.

If bit 4 of the flag field in the [head](#chapter.head) table is not
set, then it is assumed that the font scales linearly; in this case an
[hdmx](#chapter.hdmx) table is not necessary and should not be built. If
bit 4 of the flag field is set, then one or more glyphs in the font are
assumed to scale nonlinearly. In this case, performance can be improved
by including the [hdmx](#chapter.hdmx) table with one or more important
DeviceRecord's for important sizes. Please see the chapter
"Recommendations for Windows Fonts" for more detail.

The table begins as follows:

| Type         | Name                  | Description                            |
| ------------ | --------------------- | -------------------------------------- |
| USHORT       | version               | Table version number (0)               |
| SHORT        | numRecords            | Number of device records.              |
| LONG         | sizeDeviceRecord      | Size of a device record, long aligned. |
| DeviceRecord | records\[numRecords\] | Array of device records.               |

hdmx header

Each DeviceRecord for format 0 looks like this.

| Type | Name                 | Description                                                   |
| ---- | -------------------- | ------------------------------------------------------------- |
| BYTE | pixelSize            | Pixel size for following widths (as ppem).                    |
| BYTE | maxWidth             | Maximum width.                                                |
| BYTE | widths \[numGlyphs\] | Array of widths (numGlyphs is from the [maxp](#chapter.maxp)) |

Device Record

Each DeviceRecord is padded with 0's to make it long word aligned.

Each Width value is the width of the particular glyph, in pixels, at the
pixels per em (ppem) size listed at the start of the DeviceRecord.

The ppem sizes are measured along the y axis.

### XML Representation

    ?? ==
          
    hdmx =
      element hdmx {
        attribute version { text },
        element deviceRecord {
          attribute pixelSize { text },
          attribute maxWidth { text },
          element width {
            attribute gid { text },
            attribute v   { text }}* }* }

