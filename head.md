# head - Font Header

## Introduction

### Specification

This table gives global information about the font. The bounding box
values should be computed using *only* glyphs that have contours. Glyphs
with no contours should be ignored for the purposes of these
calculations.

| Type         | Name                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed        | Table version number | 0x00010000 for version 1.0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Fixed        | fontRevision         | Set by font manufacturer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ULONG        | checkSumAdjustment   | To compute: set it to 0, sum the entire font as ULONG, then store 0xB1B0AFBA - sum.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ULONG        | magicNumber          | Set to 0x5F0F3CF5.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| USHORT       | flags                | Bit 0: baseline for font at y=0;, Bit 1: left sidebearing at x=0;, Bit 2: instructions may depend on point size;, Bit 3: force ppem to integer values for all internal scaler math; may use fractional ppem sizes if this bit is clear;, Bit 4: instructions may alter advance width (the advance widths might not scale linearly);, Bits 5-10: These should be set according to [Apple's specification](http://developer.apple.com/fonts/TTRefMan/RM06/Chap6head.html). However, they are not implemented in OpenType., Bit 11: font data is 'lossless,' as a result of having been compressed and decompressed with the Agfa MicroType Express engine., Bit 12: font converted (produce compatible metrics)., Bit 13: Font optimized for ClearType., Bit 14: Reserved, set to 0., Bit 15: Reserved, set to 0. |
| USHORT       | unitsPerEm           | Valid range is from 16 to 16384. This value should be a power of 2 for fonts that have TrueType outlines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| LONGDATETIME | created              | Number of seconds since 12:00 midnight, January 1, 1904. 64-bit integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| LONGDATETIME | modified             | Number of seconds since 12:00 midnight, January 1, 1904. 64-bit integer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SHORT        | xMin                 | For all glyph bounding boxes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SHORT        | yMin                 | For all glyph bounding boxes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SHORT        | xMax                 | For all glyph bounding boxes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SHORT        | yMax                 | For all glyph bounding boxes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| USHORT       | macStyle             | Bit 0: Bold (if set to 1);, Bit 1: Italic (if set to 1), Bit 2: Underline (if set to 1), Bit 3: Outline (if set to 1), Bit 4: Shadow (if set to 1), Bit 5: Condensed (if set to 1), Bit 6: Extended (if set to 1), Bits 7-15: Reserved (set to 0)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| USHORT       | lowestRecPPEM        | Smallest readable size in pixels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| SHORT        | fontDirectionHint    | 0: Fully mixed directional glyphs;, 1: Only strongly left to right;, 2: Like 1 but also contains neutrals;, -1: Only strongly right to left;, -2: Like -1 but also contains neutrals\[1\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| SHORT        | indexToLocFormat     | 0 for short offsets, 1 for long.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SHORT        | glyphDataFormat      | 0 for current format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

Note that macStyle bits must agree with the [OS/2](#chapter.OS2) table
fsSelection bits. The fsSelection bits are used over the macStyle bits
in Microsoft Windows. The PANOSE values and [post](#chapter.post) table
values are ignored for determining bold or italic fonts.

For historical reasons, the fontRevision value contained in this table
is not used by Windows to determine the version of a font. Instead,
Windows evaluates the version string (id 5) in the [name](#chapter.name)
table.

### Annotation

It seems that Table version number is set to 'OTTO' for CFF based fonts.

### XML Representation

    head =
      element head {
        attribute major { text },
        attribute minor { text },
        element fontRevision {
          attribute major { text },
          attribute minor { text }
        },
        element flags {
          attribute baseline_at_0 { yesOrNo },
          attribute lsb_at_0 { yesOrNo },
          attribute instructions_vary_with_point_size { yesOrNo },
          attribute use_integral_ppem { yesOrNo },
          attribute instructions_alter_advance_width { yesOrNo },
          attribute lossless { yesOrNo },
          attribute converted { yesOrNo },
          attribute optimized_for_cleartype { yesOrNo }
        },
        element unitsPerEm {
          attribute v { text }
        },
        element dates {
          attribute created { text },
          attribute modified { text }
        },
        element bbox {
          attribute xMin { text },
          attribute yMin { text },
          attribute xMax { text },
          attribute yMax { text }
        },
        element macStyle {
          attribute bold { yesOrNo },
          attribute italic { yesOrNo }
        },
        element lowestRecPPEM {
          attribute v { text }
        },
        element fontDirectionHint {
          attribute v { text }
        },
        element indexToLocFormat {
          attribute v { text }
        }
      }

