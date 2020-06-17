# maxp - Maximum Profile

## Introduction

### Specification

This table establishes the memory requirements for this font. Fonts with
CFF data must use Version 0.5 of this table, specifying only the
numGlyphs field. Fonts with TrueType outlines must use Version 1.0 of
this table, where all data is required. Both formats of OpenType require
a [maxp](#chapter.maxp) table because a number of applications call the
Windows GetFontData( ) API on the [maxp](#chapter.maxp) table to
determine the number of glyphs in the font.

| Type   | Name      | Description                                                                                                                            |
| ------ | --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed  | Table     | version number 0x00005000 for version 0.5 (Note the difference in the representation of a non-zero fractional part, in Fixed numbers.) |
| USHORT | numGlyphs | The number of glyphs in the font.                                                                                                      |

Version 0.5

| Type   | Name                  | Description                                                                                                            |
| ------ | --------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Fixed  | Table                 | version number 0x00010000 for version 1.0.                                                                             |
| USHORT | numGlyphs             | The number of glyphs in the font.                                                                                      |
| USHORT | maxPoints             | Maximum points in a non-composite glyph.                                                                               |
| USHORT | maxContours           | Maximum contours in a non-composite glyph.                                                                             |
| USHORT | maxCompositePoints    | Maximum points in a composite glyph.                                                                                   |
| USHORT | maxCompositeContours  | Maximum contours in a composite glyph.                                                                                 |
| USHORT | maxZones              | 1 if instructions do not use the twilight zone (Z0), or 2 if instructions do use Z0; should be set to 2 in most cases. |
| USHORT | maxTwilightPoints     | Maximum points used in Z0.                                                                                             |
| USHORT | maxStorage            | Number of Storage Area locations.                                                                                      |
| USHORT | maxFunctionDefs       | Number of FDEFs.                                                                                                       |
| USHORT | maxInstructionDefs    | Number of IDEFs.                                                                                                       |
| USHORT | maxStackElements      | Maximum stack depth\[2\].                                                                                              |
| USHORT | maxSizeOfInstructions | Maximum byte count for glyph instructions.                                                                             |
| USHORT | maxComponentElements  | Maximum number of components referenced at "top level" for any composite glyph.                                        |
| USHORT | maxComponentDepth     | Maximum levels of recursion; 1 for simple components.                                                                  |

Version 1.0

### XML Representation

    ?? ==
          
    maxp |=
      element maxp {
        attribute major { "0" },
        attribute minor { "5" },
        element numGlyphs {
          attribute v { text }
        }
      }
    maxp |=
      element maxp {
        attribute major { "1" },
        attribute minor { "0" },
        element numGlyphs {
          attribute v { text }
        },
        element maxPoints {
          attribute v { text }
        },
        element maxContours {
          attribute v { text }
        },
        element maxCompositePoints {
          attribute v { text }
        },
        element maxCompositeContours {
          attribute v { text }
        },
        element maxZones {
          attribute v { text }
        },
        element maxTwilightPoints {
          attribute v { text }
        },
        element maxStorage {
          attribute v { text }
        },
        element maxFunctionDefs {
          attribute v { text }
        },
        element maxInstructionDefs {
          attribute v { text }
        },
        element maxStackElements {
          attribute v { text }
        },
        element maxSizeOfInstructions {
          attribute v { text }
        },
        element maxComponentElements {
          attribute v { text }
        },
        element maxComponentDepth {
          attribute v { text }
        }
      }

