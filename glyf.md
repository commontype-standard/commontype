# glyf - Glyf Data

## Introduction

### Specification

This table contains information that describes the glyphs in the font in
the TrueType outline format. Information regarding the rasterizer
(scaler) refers to the TrueType rasterizer.

Each glyph begins with the following header:

| Type  | Name             | Description                                                                                                                 |
| ----- | ---------------- | --------------------------------------------------------------------------------------------------------------------------- |
| SHORT | numberOfContours | If the number of contours is greater than or equal to zero, this is a single glyph; if negative, this is a composite glyph. |
| SHORT | xMin             | Minimum x for coordinate data.                                                                                              |
| SHORT | yMin             | Minimum y for coordinate data.                                                                                              |
| SHORT | xMax             | Maximum x for coordinate data.                                                                                              |
| SHORT | yMax             | Maximum y for coordinate data.                                                                                              |

Note that the bounding rectangle from each character is defined as the
rectangle with a lower left corner of (xMin, yMin) and an upper right
corner of (xMax, yMax).

Note: The scaler will perform better if the glyph coordinates have been
created such that the xMin is equal to the lsb. For example, if the lsb
is 123, then xMin for the glyph should be 123. If the lsb is -12 then
the xMin should be -12. If the lsb is 0 then xMin is 0. If all glyphs
are done like this, set bit 1 of flags field in the
[head](#chapter.head) table.

### XML Representation

    Relax Schema for glyf table ==
          
    glyf =
      element glyf {
        ( simple_glyph | empty_glyph | composite_glyph )*
      }
    
    empty_glyph =
      element empty_glyph {
        attribute gid { text } }
    
    glyph_attributes =
      attribute gid { text },
      attribute xMin { text },
      attribute yMin { text },
      attribute xMax { text },
      attribute yMax { text }

## Simple Glyph Description

### Specification

This is the table information needed if numberOfContours is greater than
zero, that is, a glyph is not a composite.

| Type          | Name                   | Description                                                                 |
| ------------- | ---------------------- | --------------------------------------------------------------------------- |
| USHORT        | endPtsOfContours \[n\] | Array of last points of each contour; n is the number of contours.          |
| USHORT        | instructionLength      | Total number of bytes for instructions.                                     |
| BYTE          | instructions \[n\]     | Array of instructions for each glyph; n is the number of instructions.      |
| BYTE          | flags \[n\]            | Array of flags for each coordinate in outline; n is the number of flags.    |
| BYTE or SHORT | xCoordinates \[\]      | First coordinates relative to (0,0); others are relative to previous point. |
| BYTE or SHORT | yCoordinates \[\]      | First coordinates relative to (0,0); others are relative to previous point. |

Note: In the [glyf](#chapter.glyf) table, the position of a point is not
stored in absolute terms but as a vector relative to the previous point.
The delta-x and delta-y vectors represent these (often small) changes in
position.

Each flag is a single byte. Their meanings are shown below.

| Flags                                    | Bit | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------------- | --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| On Curve                                 | 0   | If set, the point is on the curve; otherwise, it is off the curve.                                                                                                                                                                                                                                                                                                                                                                                        |
| x-Short Vector                           | 1   | If set, the corresponding x-coordinate is 1 byte long. If not set, 2 bytes.                                                                                                                                                                                                                                                                                                                                                                               |
| y-Short Vector                           | 2   | If set, the corresponding y-coordinate is 1 byte long. If not set, 2 bytes.                                                                                                                                                                                                                                                                                                                                                                               |
| Repeat                                   | 3   | If set, the next byte specifies the number of additional times this set of flags is to be repeated. In this way, the number of flags listed can be smaller than the number of points in a character.                                                                                                                                                                                                                                                      |
| This x is same (Positive x-Short Vector) | 4   | This flag has two meanings, depending on how the x-Short Vector flag is set. If x-Short Vector is set, this bit describes the sign of the value, with 1 equalling positive and 0 negative. If the x-Short Vector bit is not set and this bit is set, then the current x-coordinate is the same as the previous x-coordinate. If the x-Short Vector bit is not set and this bit is also not set, the current x-coordinate is a signed 16-bit delta vector. |
| This y is same (Positive y-Short Vector) | 5   | This flag has two meanings, depending on how the y-Short Vector flag is set. If y-Short Vector is set, this bit describes the sign of the value, with 1 equalling positive and 0 negative. If the y-Short Vector bit is not set and this bit is set, then the current y-coordinate is the same as the previous y-coordinate. If the y-Short Vector bit is not set and this bit is also not set, the current y-coordinate is a signed 16-bit delta vector. |
| Reserved                                 | 6   | This bit is reserved. Set it to zero.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Reserved                                 | 7   | This bit is reserved. Set it to zero.                                                                                                                                                                                                                                                                                                                                                                                                                     |

### XML Representation

    Relax Schema for glyf table ==
          
    simple_glyph =
      element simple_glyph {
        glyph_attributes,
        element contour {
          element point {
            attribute on_curve { yesOrNo },
            attribute x { text },
            attribute y { text } }+ } +,
    
        element instructions {
          attribute opcodes { text }} ?
      }

## Composite Glyph Description

### Specification

This is the table information needed for composite glyphs
(numberOfContours is -1). A composite glyph starts with two USHORT
values ("flags" and "glyphIndex," i.e. the index of the first contour in
this composite glyph); the data then varies according to "flags").

| Type                  | Name       | Description                                                                             |
| --------------------- | ---------- | --------------------------------------------------------------------------------------- |
| SHORT                 | flags      | component flag                                                                          |
| SHORT                 | glyphIndex | glyph index of component                                                                |
| VARIABLE              | argument1  | x-offset for component or point number; type depends on bits 0 and 1 in component flags |
| VARIABLE              | argument2  | y-offset for component or point number; type depends on bits 0 and 1 in component flags |
| Transformation Option |            |                                                                                         |

The C pseudo-code fragment below shows how the composite glyph
information is stored and parsed; definitions for "flags" bits follow
this fragment:

    do {
            USHORT flags;
            USHORT glyphIndex;
            if ( flags & ARG_1_AND_2_ARE_WORDS) {
            (SHORT or FWord) argument1;
            (SHORT or FWord) argument2;
            } else {
                    USHORT arg1and2; /* (arg1 << 8) | arg2 */
            }
            if ( flags & WE_HAVE_A_SCALE ) {
                    F2Dot14  scale;    /* Format 2.14 */
            } else if ( flags & WE_HAVE_AN_X_AND_Y_SCALE ) {
                    F2Dot14  xscale;    /* Format 2.14 */
                    F2Dot14  yscale;    /* Format 2.14 */
            } else if ( flags & WE_HAVE_A_TWO_BY_TWO ) {
                    F2Dot14  xscale;    /* Format 2.14 */
                    F2Dot14  scale01;   /* Format 2.14 */
                    F2Dot14  scale10;   /* Format 2.14 */
                    F2Dot14  yscale;    /* Format 2.14 */
            }
    } while ( flags & MORE_COMPONENTS )
    if (flags & WE_HAVE_INSTR){
            USHORT numInstr
            BYTE instr[numInstr]

Argument1 and argument2 can be either x and y offsets to be added to the
glyph or two point numbers. In the latter case, the first point number
indicates the point that is to be matched to the new glyph. The second
number indicates the new glyph's "matched" point. Once a glyph is added,
its point numbers begin directly after the last glyphs (endpoint of
first glyph + 1).

When arguments 1 and 2 are an x and a y offset instead of points and the
bit ROUND\_XY\_TO\_GRID is set to 1, the values are rounded to those of
the closest grid lines before they are added to the glyph. X and Y
offsets are described in FUnits.

If the bit WE\_HAVE\_A\_SCALE is set, the scale value is read in 2.14
format-the value can be between -2 to almost +2. The glyph will be
scaled by this value before grid-fitting.

The bit WE\_HAVE\_A\_TWO\_BY\_TWO allows for an interrelationship
between the x and y coordinates. This could be used for 90-degree
rotations, for example.

These are the constants for the flags field:

| Flags                          | Bit | Description                                                                                                                                                  |
| ------------------------------ | --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ARG\_1\_AND\_2\_ARE\_WORDS     | 0   | If this is set, the arguments are words; otherwise, they are bytes.                                                                                          |
| ARGS\_ARE\_XY\_VALUES          | 1   | If this is set, the arguments are xy values; otherwise, they are points.                                                                                     |
| ROUND\_XY\_TO\_GRID            | 2   | For the xy values if the preceding is true.                                                                                                                  |
| WE\_HAVE\_A\_SCALE             | 3   | This indicates that there is a simple scale for the component. Otherwise, scale = 1.0.                                                                       |
| RESERVED                       | 4   | This bit is reserved. Set it to 0.                                                                                                                           |
| MORE\_COMPONENTS               | 5   | Indicates at least one more glyph after this one.                                                                                                            |
| WE\_HAVE\_AN\_X\_AND\_Y\_SCALE | 6   | The x direction will use a different scale from the y direction.                                                                                             |
| WE\_HAVE\_A\_TWO\_BY\_TWO      | 7   | There is a 2 by 2 transformation that will be used to scale the component.                                                                                   |
| WE\_HAVE\_INSTRUCTIONS         | 8   | Following the last component are instructions for the composite character.                                                                                   |
| USE\_MY\_METRICS               | 9   | If set, this forces the aw and lsb (and rsb) for the composite to be equal to those from this original glyph. This works for hinted and unhinted characters. |
| OVERLAP\_COMPOUND              | 10  | Used by Apple in GX fonts.                                                                                                                                   |
| SCALED\_COMPONENT\_OFFSET      | 11  | Composite designed to have the component offset scaled (designed for Apple rasterizer).                                                                      |
| UNSCALED\_COMPONENT\_OFFSET    | 12  | Composite designed not to have the component offset scaled (designed for the Microsoft TrueType rasterizer).                                                 |

The purpose of USE\_MY\_METRICS is to force the lsb and rsb to take on a
desired value. For example, an i-circumflex (U+00EF) is often composed
of the circumflex and a dotless-i. In order to force the composite to
have the same metrics as the dotless-i, set USE\_MY\_METRICS for the
dotless-i component of the composite. Without this bit, the rsb and lsb
would be calculated from the hmtx entry for the composite (or would need
to be explicitly set with TrueType instructions).

Note that the behavior of the USE\_MY\_METRICS operation is undefined
for rotated composite components.

### XML Representation

    Relax Schema for glyf table ==
          
    composite_glyph =
      element composite_glyph {
        glyph_attributes,
        element component {
          attribute flags { text },
          attribute gid { text },
          attribute arg1 { text },
          attribute arg2 { text },
          component_scale? } +,
    
        element instructions {
          attribute opcodes { text }} ?
      }
    
    component_scale |=
       attribute scale { text ? }
    
    component_scale |=
       attribute xscale { text ? },
       attribute yscale { text ? }
    
    component_scale |=
       attribute xscale { text ? },
       attribute scale01 { text ? },
       attribute scale10 { text ? },
       attribute yscale { text ? }

