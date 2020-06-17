# gasp - Grid-fitting And Scan-conversion Procedure

## Overview

### Specification

This table contains information which describes the preferred
rasterization techniques for the typeface when it is rendered on
grayscale-capable devices. This table also has some use for monochrome
devices, which may use the table to turn off hinting at very large or
small sizes, to improve performance.

At very small sizes, the best appearance on grayscale devices can
usually be achieved by rendering the glyphs in grayscale without using
hints. At intermediate sizes, hinting and monochrome rendering will
usually produce the best appearance. At large sizes, the combination of
hinting and grayscale rendering will typically produce the best
appearance.

If the [gasp](#chapter.gasp) table is not present in a typeface, the
rasterizer may apply default rules to decide how to render the glyphs on
grayscale devices.

The [gasp](#chapter.gasp) table consists of a header followed by
groupings of [gasp](#chapter.gasp) records:

| Type      | Name                    | Description                 |
| --------- | ----------------------- | --------------------------- |
| USHORT    | version                 | Version number (set to 0)   |
| USHORT    | numRanges               | Number of records to follow |
| GASPRANGE | gaspRange \[numRanges\] | Sorted by ppem              |

gasp Table

Each GASPRANGE record looks like this:

| Type   | Name              | Description                                   |
| ------ | ----------------- | --------------------------------------------- |
| USHORT | rangeMaxPPEM      | Upper limit of range, in PPEM                 |
| USHORT | rangeGaspBehavior | Flags describing desired rasterizer behavior. |

There are two flags for the rangeGaspBehavior flags:

| Flag          | Meaning                 |
| ------------- | ----------------------- |
| GASP\_GRIDFIT | Use gridfitting         |
| GASP\_DOGRAY  | Use grayscale rendering |

The set of bit flags may be extended in the future.The four currently
defined values of rangeGaspBehavior would have the following uses:

| Flag                       | Value  | Meaning                                             |
| -------------------------- | ------ | --------------------------------------------------- |
| GASP\_DOGRAY               | 0x0002 | small sizes, typically ppem\<9                      |
| GASP\_GRIDFIT              | 0x0001 | medium sizes, typically 9\<=ppem\<=16               |
| GASP\_DOGRAY|GASP\_GRIDFIT | 0x0003 | large sizes, typically ppem\>16                     |
| (neither)                  | 0x0000 | optional for very large sizes, typically ppem\>2048 |

The records in the gaspRange\[\] array must be sorted in order of
increasing rangeMaxPPEM value. The last record should use 0xFFFF as a
sentinel value for rangeMaxPPEM and should describe the behavior desired
at all sizes larger than the previous record's upper limit. If the only
entry in [gasp](#chapter.gasp) is the 0xFFFF sentinel value, the
behavior described will be used for all sizes.

**Sample [gasp](#chapter.gasp) table**

| Flag             | Value         | Meaning                           |
| ---------------- | ------------- | --------------------------------- |
| version          | 0x0000        |                                   |
| numRanges        | 0x0003        |                                   |
| Range\[0\], Flag | 0x0008 0x0002 | ppem \<= 8, grayscale only        |
| Range\[1\], Flag | 0x0010 0x0001 | 9\<=ppem \<= 16, gridfit only     |
| Range\[2\], Flag | 0xFFFF 0x0003 | 16 \< ppem, gridfit and grayscale |

