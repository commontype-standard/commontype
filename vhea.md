# vhea - Vertical Header Table

## Overview

### Specification

The vertical header table (tag name: [vhea](#chapter.vhea)) contains
information needed for vertical fonts. The glyphs of vertical fonts are
written either top to bottom or bottom to top. This table contains
information that is general to the font as a whole. Information that
pertains to specific glyphs is given in the vertical metrics table (tag
name: [vmtx](#chapter.vmtx)) described separately. The formats of these
tables are similar to those for horizontal metrics (hhea and hmtx).

Data in the vertical header table must be consistent with data that
appears in the vertical metrics table. The advance height and top
sidebearing values in the vertical metrics table must correspond with
the maximum advance height and minimum bottom sidebearing values in the
vertical header table.

See the section "OpenType CJK Font Guidelines" for more information
about constructing CJK (Chinese, Japanese, and Korean) fonts.

The difference between version 1.0 and version 1.1 is the name and
definition of:

  - ascender becomes vertTypoAscender

  - descender becomes vertTypoDescender

  - lineGap becomes vertTypoLineGap

The vertical header table format follows: Vertical Header Table

| Type   | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed  | version             | Version number of the vertical header table; 0x0001000 for version 1.0                                                                                                                                                                                                                                                                                                                                                            |
| SHORT  | ascent              | Distance in FUnits from the centerline to the previous line’ descent.                                                                                                                                                                                                                                                                                                                                                             |
| SHORT  | descent             | Distance in FUnits from the centerline to the next line’s ascent.                                                                                                                                                                                                                                                                                                                                                                 |
| SHORT  | lineGap             | Reserved; set to 0.                                                                                                                                                                                                                                                                                                                                                                                                               |
| SHORT  | advanceHeightMax    | The maximum advance height measurement — in FUnits — found in the font. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                             |
| SHORT  | minTop              | The minimum top sidebearing measurement found in the font, in FUnits. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                               |
| SHORT  | minBottom           | The minimum bottom sidebearing measurement found in the font, in FUnits. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                            |
| SHORT  | yMaxExtent          | Defined as yMaxExtent=minTopSideBearing + (yMax - yMin)                                                                                                                                                                                                                                                                                                                                                                           |
| SHORT  | caretSlopeRise      | The value of the caretSlopeRise field divided by the value of the caretSlopeRun Field determines the slope of the caret. A value of 0 for the rise and a value of 1 for the run specifies a horizontal caret. A value of 1 for the rise and a value of 0 for the run specifies a vertical caret. Intermediate values are desirable for fonts whose glyphs are oblique or italic. For a vertical font, a horizontal caret is best. |
| SHORT  | caretSlopeRun       | See the caretSlopeRise field. Value=1 for nonslanted vertical fonts.                                                                                                                                                                                                                                                                                                                                                              |
| SHORT  | caretOffset         | The amount by which the highlight on a slanted glyph needs to be shifted away from the glyph in order to produce the best appearance. Set value equal to 0 for nonslanted fonts.                                                                                                                                                                                                                                                  |
| SHORT  | reserved            | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved            | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved            | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved            | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | metricDataFormat    | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| USHORT | numOfLongVerMetrics | Number of advance heights in the vertical metrics table.                                                                                                                                                                                                                                                                                                                                                                          |

Version 1.0

| Type   | Name                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------ | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed  | version              | Version number of the vertical header table; 0x00011000 for version 1.1. Note the representation of a non-zero fractional part, in Fixed numbers.                                                                                                                                                                                                                                                                                 |
| SHORT  | vertTypoAscender     | The vertical typographic ascender for this font. It is the distance in FUnits from the ideographic em-box center baseline for the vertical axis to the right of the ideographic em-box and is usually set to (head.unitsPerEm)/2. For example, a font with an em of 1000 fUnits will set this field to 500. See the baseline section of the OpenType Tag Registry for a description of the ideographic em-box.                    |
| SHORT  | vertTypoDescender    | The vertical typographic descender for this font. It is the distance in FUnits from the ideographic em-box center baseline for the horizontal axis to the left of the ideographic em-box and is usually set to (head.unitsPerEm)/2. For example, a font with an em of 1000 fUnits will set this field to 500.                                                                                                                     |
| SHORT  | vertTypoLineGap      | The vertical typographic gap for this font. An application can determine the recommended line spacing for single spaced vertical text for an OpenType font by the following expression: ideo embox width + vhea.vertTypoLineGap                                                                                                                                                                                                   |
| SHORT  | advanceHeightMax     | The maximum advance height measurement -in FUnits found in the font. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                                |
| SHORT  | minTopSideBearing    | The minimum top sidebearing measurement found in the font, in FUnits. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                               |
| SHORT  | minBottomSideBearing | The minimum bottom sidebearing measurement found in the font, in FUnits. This value must be consistent with the entries in the vertical metrics table.                                                                                                                                                                                                                                                                            |
| SHORT  | yMaxExtent           | Defined as yMaxExtent=minTopSideBearing + (yMax - yMin)                                                                                                                                                                                                                                                                                                                                                                           |
| SHORT  | caretSlopeRise       | The value of the caretSlopeRise field divided by the value of the caretSlopeRun Field determines the slope of the caret. A value of 0 for the rise and a value of 1 for the run specifies a horizontal caret. A value of 1 for the rise and a value of 0 for the run specifies a vertical caret. Intermediate values are desirable for fonts whose glyphs are oblique or italic. For a vertical font, a horizontal caret is best. |
| SHORT  | caretSlopeRun        | See the caretSlopeRise field. Value=1 for nonslanted vertical fonts.                                                                                                                                                                                                                                                                                                                                                              |
| SHORT  | caretOffset          | The amount by which the highlight on a slanted glyph needs to be shifted away from the glyph in order to produce the best appearance. Set value equal to 0 for nonslanted fonts.                                                                                                                                                                                                                                                  |
| SHORT  | reserved             | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved             | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved             | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | reserved             | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SHORT  | metricDataFormat     | Set to 0.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| USHORT | numOfLongVerMetrics  | Number of advance heights in the vertical metrics table.                                                                                                                                                                                                                                                                                                                                                                          |

Version 1.1

Vertical Header Table Example

| Type       | Name                 | Description                                                                                           |
| ---------- | -------------------- | ----------------------------------------------------------------------------------------------------- |
| 0x00011000 | version              | Version number of the vertical header table, in fixed-point format, is 1.1                            |
| 1024       | vertTypoAscender     | Half the em-square height.                                                                            |
| \-1024     | vertTypoDescender    | Minus half the em-square height.                                                                      |
| 0          | vertTypoLineGap      | Typographic line gap is 0 FUnits.                                                                     |
| 2079       | advanceHeightMax     | The maximum advance height measurement found in the font is 2079 FUnits.                              |
| \-342      | minTopSideBearing    | The minimum top sidebearing measurement found in the font is -342 FUnits.                             |
| \-333      | minBottomSideBearing | The minimum bottom sidebearing measurement found in the font is -333 FUnits.                          |
| 2036       | yMaxExtent           | minTopSideBearing + (yMax-yMin)=2036.                                                                 |
| 0          | caretSlopeRise       | The caret slope rise of 0 and a caret slope run of 1 indicate a horizontal caret for a vertical font. |
| 1          | caretSlopeRun        | The caret slope rise of 0 and a caret slope run of 1 indicate a horizontal caret for a vertical font. |
| 0          | caretOffset          | Value set to 0 for nonslanted fonts.                                                                  |
| 0          | reserved             | Set to 0.                                                                                             |
| 0          | reserved             | Set to 0.                                                                                             |
| 0          | reserved             | Set to 0.                                                                                             |
| 0          | reserved             | Set to 0.                                                                                             |
| 0          | metricDataFormat     | Set to 0.                                                                                             |
| 258        | numOfLongVerMetrics  | Number of advance heights in the vertical metrics table is 258.                                       |

### XML Representation

    ?? ==
          
    vhea =
      element vhea {
        attribute major { text },
        attribute minor { text },
        element typo {
          attribute ascender  { text },
          attribute descender { text },
          attribute lineGap   { text }
        },
        element advanceHeightMax {
          attribute v { text }
        },
        element minTopSideBearing {
          attribute v { text }
        },
        element minBottomSideBearing {
          attribute v { text }
        },
        element yMaxExtent {
          attribute v { text }
        },
        element caret {
          attribute slopeRise { text },
          attribute slopeRun { text },
          attribute offset { text }
        },
        element numberOfVMetrics {
          attribute v { text }
        }
      }

