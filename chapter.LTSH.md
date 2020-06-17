<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.LTSH"></a>Chapter 34. LTSH - Linear Threshold</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80794247136"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.34.1.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.LTSH.html" title="Chapter 34. LTSH - Linear Threshold">LTSH</a> table relates to OpenType
        fonts containing TrueType outlines. There are noticeable
        improvements to fonts on the screen when instructions are
        carefully applied to the sidebearings. The gain in readability
        is offset by the necessity for the OS to grid fit the glyphs
        in order to find the actual advance width for the glyphs
        (since instructions may be moving the sidebearing points). The
        TrueType outline format already has two mechanisms to side
        step the speed issues: the <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> table,
        where precomputed advance widths may be saved for selected
        ppem sizes, and the 'vdmx' table, where precomputed vertical
        advance widths may be saved for selected ppem sizes. The
        <a role="" class="link" href="chapter.LTSH.html" title="Chapter 34. LTSH - Linear Threshold">LTSH</a> table (Linear ThreSHold) is a second,
        complementary method.</p><p role="">The LTSH table defines the point at which it is
        reasonable to assume linearly scaled advance widths on a
        glyph-by-glyph basis. This table should not be included unless
        bit 4 of the "flags" field in the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a>
        table is set. The criteria for linear scaling is:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">(ppem size is &gt;= 50) AND (difference between the
              rounded linear width and the rounded instructed width
              &lt;= 2% of the rounded linear width)</p></li><li role="" class="listitem"><p role="">Linear width == Instructed width</p></li></ul></div><p role="">The LTSH table records the ppem for each glyph at which
          the scaling becomes linear again, despite instructions
          effecting the advance width. It is a requirement that, at
          and above the recorded threshold size, the glyph remain
          linear in its scaling (i.e., not legal to set threshold at
          55 ppem if glyph becomes nonlinear again at 90 ppem). The
          format for the table is:</p><div class="table"><a name="idm80794238384"></a><p class="title"><strong>Table 34.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Version number (starts at 0).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numGlyphs</td><td role="">Number of glyphs (from "numGlyphs" in <a role="" class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a>
              table).</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">yPels [numGlyphs]</td><td role="">The vertical pel height at which the glyph
              can be assumed to scale linearly. On a per glyph
              basis.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Note that glyphs which do not have instructions on their
          sidebearings should have yPels = 1; i.e., always scales
          linearly.</p></div></div></div>