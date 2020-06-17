<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.glyf"></a>Chapter 16. glyf - Glyf Data</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383055450592"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.16.1.1"></a>Specification</h3></div></div></div><p role="">This table contains information that describes the
          glyphs in the font in the TrueType outline format.
          Information regarding the rasterizer (scaler) refers to the
          TrueType rasterizer.</p><p role="">Each glyph begins with the following header:</p><div class="table"><a name="idm383055447840"></a><p class="title"><strong>Table 16.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">SHORT</td><td role="">numberOfContours</td><td role="">If the number of contours is greater than or
              equal to zero, this is a single glyph; if negative, this
              is a composite glyph.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xMin</td><td role="">Minimum x for coordinate data.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMin</td><td role="">Minimum y for coordinate data.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xMax</td><td role="">Maximum x for coordinate data.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMax</td><td role="">Maximum y for coordinate data.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Note that the bounding rectangle from each character is
          defined as the rectangle with a lower left corner of (xMin,
          yMin) and an upper right corner of (xMax, yMax).</p><p role="">Note: The scaler will perform better if the glyph
          coordinates have been created such that the xMin is equal to
          the lsb. For example, if the lsb is 123, then xMin for the
          glyph should be 123. If the lsb is -12 then the xMin should
          be -12. If the lsb is 0 then xMin is 0. If all glyphs are
          done like this, set bit 1 of flags field in the
          <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383055435712"></a>Simple Glyph Description</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.16.2.1"></a>Specification</h3></div></div></div><p role="">This is the table information needed if numberOfContours
          is greater than zero, that is, a glyph is not a
          composite.</p><div class="table"><a name="idm383055433360"></a><p class="title"><strong>Table 16.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">endPtsOfContours [n]</td><td role="">Array of last points of each contour; n is
              the number of contours.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">instructionLength</td><td role="">Total number of bytes for
              instructions.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">instructions [n]</td><td role="">Array of instructions for each glyph; n is
              the number of instructions.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">flags [n]</td><td role="">Array of flags for each coordinate in
              outline; n is the number of flags.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE or SHORT</td><td role="">xCoordinates []</td><td role=""> First coordinates relative to (0,0); others
              are relative to previous point.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE or SHORT</td><td role="">yCoordinates []</td><td role="">First coordinates relative to (0,0); others
              are relative to previous point.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Note: In the <a role="" class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> table, the position
          of a point is not stored in absolute terms but as a vector
          relative to the previous point. The delta-x and delta-y
          vectors represent these (often small) changes in
          position.</p><p role="">Each flag is a single byte. Their meanings are shown
          below.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="1cm"/><col width="10cm"/></colgroup><thead><tr><th role="">Flags</th><th role="">Bit</th><th role="">Description</th></tr></thead><tbody><tr><td role="">On Curve</td><td role="">0</td><td role="">If set, the point is on the curve; otherwise,
                  it is off the curve.</td></tr><tr><td role="">x-Short Vector</td><td role="">1</td><td role="">If set, the corresponding x-coordinate is 1
                  byte long. If not set, 2 bytes.</td></tr><tr><td role="">y-Short Vector</td><td role="">2</td><td role="">If set, the corresponding y-coordinate is 1
                  byte long. If not set, 2 bytes.</td></tr><tr><td role="">Repeat</td><td role="">3</td><td role="">If set, the next byte specifies the number of
                  additional times this set of flags is to be
                  repeated. In this way, the number of flags listed
                  can be smaller than the number of points in a
                  character.</td></tr><tr><td role="">This x is same (Positive x-Short
                  Vector)</td><td role="">4</td><td role="">This flag has two meanings, depending on how
                  the x-Short Vector flag is set. If x-Short Vector is
                  set, this bit describes the sign of the value, with
                  1 equalling positive and 0 negative. If the x-Short
                  Vector bit is not set and this bit is set, then the
                  current x-coordinate is the same as the previous
                  x-coordinate. If the x-Short Vector bit is not set
                  and this bit is also not set, the current
                  x-coordinate is a signed 16-bit delta
                  vector.</td></tr><tr><td role="">This y is same (Positive y-Short
                  Vector)</td><td role="">5</td><td role="">This flag has two meanings, depending on how
                  the y-Short Vector flag is set. If y-Short Vector is
                  set, this bit describes the sign of the value, with
                  1 equalling positive and 0 negative. If the y-Short
                  Vector bit is not set and this bit is set, then the
                  current y-coordinate is the same as the previous
                  y-coordinate. If the y-Short Vector bit is not set
                  and this bit is also not set, the current
                  y-coordinate is a signed 16-bit delta
                  vector.</td></tr><tr><td role="">Reserved</td><td role="">6</td><td role="">This bit is reserved. Set it to zero.</td></tr><tr><td role="">Reserved</td><td role="">7</td><td role="">This bit is reserved. Set it to zero.</td></tr></tbody></table></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383055400608"></a>Composite Glyph Description</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.16.3.1"></a>Specification</h3></div></div></div><p role="">This is the table information needed for composite
          glyphs (numberOfContours is -1). A composite glyph starts
          with two USHORT values ("flags" and "glyphIndex," i.e. the
          index of the first contour in this composite glyph); the
          data then varies according to "flags").</p><div class="table"><a name="idm383055398080"></a><p class="title"><strong>Table 16.3. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">SHORT</td><td role="">flags</td><td role="">component flag</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">glyphIndex</td><td role="">glyph index of component</td><td class="auto-generated"> </td></tr><tr><td role="">VARIABLE</td><td role="">argument1</td><td role="">x-offset for component or point number; type
              depends on bits 0 and 1 in component flags</td><td class="auto-generated"> </td></tr><tr><td role="">VARIABLE</td><td role="">argument2</td><td role="">y-offset for component or point number; type
              depends on bits 0 and 1 in component flags</td><td class="auto-generated"> </td></tr><tr><td role="">Transformation Option</td><td role=""> </td><td role=""> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The C pseudo-code fragment below shows how the composite
          glyph information is stored and parsed; definitions for
          "flags" bits follow this fragment:</p><div role="" class="literallayout"><p><br/>
<br/>
do {<br/>
        USHORT flags;<br/>
        USHORT glyphIndex;<br/>
        if ( flags &amp; ARG_1_AND_2_ARE_WORDS) {<br/>
        (SHORT or FWord) argument1;<br/>
        (SHORT or FWord) argument2;<br/>
        } else {<br/>
                USHORT arg1and2; /* (arg1 &lt;&lt; 8) | arg2 */<br/>
        }<br/>
        if ( flags &amp; WE_HAVE_A_SCALE ) {<br/>
                F2Dot14  scale;    /* Format 2.14 */<br/>
        } else if ( flags &amp; WE_HAVE_AN_X_AND_Y_SCALE ) {<br/>
                F2Dot14  xscale;    /* Format 2.14 */<br/>
                F2Dot14  yscale;    /* Format 2.14 */<br/>
        } else if ( flags &amp; WE_HAVE_A_TWO_BY_TWO ) {<br/>
                F2Dot14  xscale;    /* Format 2.14 */<br/>
                F2Dot14  scale01;   /* Format 2.14 */<br/>
                F2Dot14  scale10;   /* Format 2.14 */<br/>
                F2Dot14  yscale;    /* Format 2.14 */<br/>
        }<br/>
} while ( flags &amp; MORE_COMPONENTS )<br/>
if (flags &amp; WE_HAVE_INSTR){<br/>
        USHORT numInstr<br/>
        BYTE instr[numInstr]<br/>
<br/>
</p></div><p role="">Argument1 and argument2 can be either x and y offsets to
          be added to the glyph or two point numbers. In the latter
          case, the first point number indicates the point that is to
          be matched to the new glyph. The second number indicates the
          new glyph's "matched" point. Once a glyph is added, its
          point numbers begin directly after the last glyphs (endpoint
          of first glyph + 1).</p><p role="">When arguments 1 and 2 are an x and a y offset instead
          of points and the bit ROUND_XY_TO_GRID is set to 1, the
          values are rounded to those of the closest grid lines before
          they are added to the glyph. X and Y offsets are described
          in FUnits.</p><p role="">If the bit WE_HAVE_A_SCALE is set, the scale value is
          read in 2.14 format-the value can be between -2 to almost
          +2. The glyph will be scaled by this value before
          grid-fitting.</p><p role="">The bit WE_HAVE_A_TWO_BY_TWO allows for an
          interrelationship between the x and y coordinates. This
          could be used for 90-degree rotations, for example.</p><p role="">These are the constants for the flags field:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="13pc"/><col width="2pc"/><col width="15pc"/></colgroup><thead><tr><th role="">Flags</th><th role="">Bit</th><th role="">Description</th></tr></thead><tbody><tr><td role="">ARG_1_AND_2_ARE_WORDS</td><td role="">0</td><td role="">If this is set, the arguments are words;
                  otherwise, they are bytes.</td></tr><tr><td role="">ARGS_ARE_XY_VALUES</td><td role="">1</td><td role="">If this is set, the arguments are xy values;
                  otherwise, they are points.</td></tr><tr><td role="">ROUND_XY_TO_GRID</td><td role="">2</td><td role="">For the xy values if the preceding is
                  true.</td></tr><tr><td role="">WE_HAVE_A_SCALE</td><td role="">3</td><td role="">This indicates that there is a simple scale for
                  the component. Otherwise, scale = 1.0.</td></tr><tr><td role="">RESERVED</td><td role="">4</td><td role="">This bit is reserved. Set it to 0.</td></tr><tr><td role="">MORE_COMPONENTS</td><td role="">5</td><td role="">Indicates at least one more glyph after this
                  one.</td></tr><tr><td role="">WE_HAVE_AN_X_AND_Y_SCALE</td><td role="">6</td><td role="">The x direction will use a different scale from
                  the y direction.</td></tr><tr><td role="">WE_HAVE_A_TWO_BY_TWO</td><td role="">7</td><td role="">There is a 2 by 2 transformation that will be
                  used to scale the component.</td></tr><tr><td role="">WE_HAVE_INSTRUCTIONS</td><td role="">8</td><td role="">Following the last component are instructions
                  for the composite character.</td></tr><tr><td role="">USE_MY_METRICS</td><td role="">9</td><td role="">If set, this forces the aw and lsb (and rsb)
                  for the composite to be equal to those from this
                  original glyph. This works for hinted and unhinted
                  characters.</td></tr><tr><td role="">OVERLAP_COMPOUND</td><td role="">10</td><td role="">Used by Apple in GX fonts.</td></tr><tr><td role="">SCALED_COMPONENT_OFFSET</td><td role="">11</td><td role="">Composite designed to have the component offset
                  scaled (designed for Apple rasterizer).</td></tr><tr><td role="">UNSCALED_COMPONENT_OFFSET</td><td role="">12</td><td role="">Composite designed not to have the component
                  offset scaled (designed for the Microsoft TrueType
                  rasterizer).</td></tr></tbody></table></div><p role="">The purpose of USE_MY_METRICS is to force the lsb and
          rsb to take on a desired value. For example, an i-circumflex
          (U+00EF) is often composed of the circumflex and a
          dotless-i. In order to force the composite to have the same
          metrics as the dotless-i, set USE_MY_METRICS for the
          dotless-i component of the composite. Without this bit, the
          rsb and lsb would be calculated from the hmtx entry for the
          composite (or would need to be explicitly set with TrueType
          instructions).</p><p role="">Note that the behavior of the USE_MY_METRICS operation
          is undefined for rotated composite components.</p></div></div></div>