# hhea - Horizontal Header

## Introduction

### Specification

This table contains information for horizontal layout. The values in the
minRightSidebearing, minLeftSideBearing and xMaxExtent should be
computed using *only* glyphs that have contours. Glyphs with no contours
should be ignored for the purposes of these calculations. All reserved
areas must be set to 0.

| Type   | Name                | Description                                                                                                                            |
| ------ | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed  | Table               | version number 0x00010000 for version 1.0.                                                                                             |
| FWORD  | Ascender            | Typographic ascent ([Distance from baseline to highest ascender](http://developer.apple.com/fonts/TTRefMan/RM06/Chap6hhea.html))       |
| FWORD  | Descender           | Typographic descent([Distance from baseline to highest ascender](http://developer.apple.com/fonts/TTRefMan/RM06/Chap6hhea.html))       |
| FWORD  | LineGap             | Typographic line gap. Negative LineGap values are treated as zero in Windows 3.1, System 6, and System 7.                              |
| UFWORD | advanceWidthMax     | Maximum advance width value in [hmtx](#chapter.hmtx) table.                                                                            |
| FWORD  | minLeftSideBearing  | Minimum left sidebearing value in [hmtx](#chapter.hmtx) table.                                                                         |
| FWORD  | minRightSideBearing | Minimum right sidebearing value; calculated as Min(aw - lsb - (xMax - xMin)).                                                          |
| FWORD  | xMaxExtent          | Max(lsb + (xMax - xMin)).                                                                                                              |
| SHORT  | caretSlopeRise      | Used to calculate the slope of the cursor (rise/run); 1 for vertical.                                                                  |
| SHORT  | caretSlopeRun       | 0 for vertical.                                                                                                                        |
| SHORT  | caretOffset         | The amount by which a slanted highlight on a glyph needs to be shifted to produce the best appearance. Set to 0 for non-slanted fonts. |
| SHORT  | (reserved)          | set to 0.                                                                                                                              |
| SHORT  | (reserved)          | set to 0.                                                                                                                              |
| SHORT  | (reserved)          | set to 0.                                                                                                                              |
| SHORT  | (reserved)          | set to 0.                                                                                                                              |
| SHORT  | metricDataFormat    | 0 for current format.                                                                                                                  |
| USHORT | numberOfHMetrics    | Number of hMetric entries in [hmtx](#chapter.hmtx) table.                                                                              |

Note: The ascender, descender and linegap values in this table are Apple
specific. Also, see information in the [OS/2](#chapter.OS2) table.

