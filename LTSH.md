# LTSH - Linear Threshold

## Overview

### Specification

The [LTSH](#chapter.LTSH) table relates to OpenType fonts containing
TrueType outlines. There are noticeable improvements to fonts on the
screen when instructions are carefully applied to the sidebearings. The
gain in readability is offset by the necessity for the OS to grid fit
the glyphs in order to find the actual advance width for the glyphs
(since instructions may be moving the sidebearing points). The TrueType
outline format already has two mechanisms to side step the speed issues:
the [hdmx](#chapter.hdmx) table, where precomputed advance widths may be
saved for selected ppem sizes, and the 'vdmx' table, where precomputed
vertical advance widths may be saved for selected ppem sizes. The
[LTSH](#chapter.LTSH) table (Linear ThreSHold) is a second,
complementary method.

The LTSH table defines the point at which it is reasonable to assume
linearly scaled advance widths on a glyph-by-glyph basis. This table
should not be included unless bit 4 of the "flags" field in the
[head](#chapter.head) table is set. The criteria for linear scaling is:

  - (ppem size is \>= 50) AND (difference between the rounded linear
    width and the rounded instructed width \<= 2% of the rounded linear
    width)

  - Linear width == Instructed width

The LTSH table records the ppem for each glyph at which the scaling
becomes linear again, despite instructions effecting the advance width.
It is a requirement that, at and above the recorded threshold size, the
glyph remain linear in its scaling (i.e., not legal to set threshold at
55 ppem if glyph becomes nonlinear again at 90 ppem). The format for the
table is:

| Type   | Name                | Description                                                                                        |
| ------ | ------------------- | -------------------------------------------------------------------------------------------------- |
| USHORT | version             | Version number (starts at 0).                                                                      |
| USHORT | numGlyphs           | Number of glyphs (from "numGlyphs" in [maxp](#chapter.maxp) table).                                |
| BYTE   | yPels \[numGlyphs\] | The vertical pel height at which the glyph can be assumed to scale linearly. On a per glyph basis. |

Note that glyphs which do not have instructions on their sidebearings
should have yPels = 1; i.e., always scales linearly.

