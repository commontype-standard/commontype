# EBSC - Embedded Bitmap Scaling Table

## Overview

### Specification

The [EBSC](#chapter.EBSC) table provides a mechanism for describing
embedded bitmaps which are created by scaling other embedded bitmaps.
While this is the sort of thing that outline font technologies were
invented to avoid, there are cases (small sizes of Kanji, for example)
where scaling a bitmap produces a more legible font than scan-converting
an outline. For this reason the [EBSC](#chapter.EBSC) table allows a
font to define a bitmap strike as a scaled version of another strike.

The [EBSC](#chapter.EBSC) table begins with a header containing the
table version and number of strikes.

| Type  | Name     | Description                     |
| ----- | -------- | ------------------------------- |
| FIXED | version  | initially defined as 0x00020000 |
| ULONG | numSizes |                                 |

ebscHeader

The ebscHeader is followed immediately by the bitmapScaleTable array.
The numSizes in the ebscHeader indicates the number of bitmapScaleTables
in the array. Each strike is defined by one bitmapScaleTable.

| Type            | Name            | Description                     |
| --------------- | --------------- | ------------------------------- |
| sbitLineMetrics | hori            | line metrics                    |
| sbitLineMetrics | vert            | line metrics                    |
| BYTE            | ppemX           | target horizontal pixels per Em |
| BYTE            | ppemY           | target vertical pixels per Em   |
| BYTE            | substitutePpemX | use bitmaps of this size        |
| BYTE            | substitutePpemY | use bitmaps of this size        |

bitmapScaleTable

The line metrics have the same meaning as those in the bitmapSizeTable,
and refer to font wide metrics after scaling. The ppemX and ppemY values
describe the size of the font after scaling. The substitutePpemX and
substitutePpemY values describe the size of a strike that exists as an
sbit in the [EBLC](#chapter.EBLC) and 'EBDT', and that will be scaled up
or down to generate the new strike.

Notice that scaling in the x direction is independent of scaling in the
y direction, and their scaling values may differ. A square aspect-ratio
strike could be scaled to a non-square aspect ratio. Glyph metrics are
scaled by the same factor as the pixels per Em (in the appropriate
direction), and are rounded to the nearest integer pixel.

