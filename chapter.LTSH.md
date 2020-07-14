<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.LTSH"></a>Chapter 35. LTSH - Linear Threshold</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm237274154064"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.36.1.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.LTSH.html" title="Chapter 35. LTSH - Linear Threshold">LTSH</a> table relates to CommonType
        fonts containing TrueType outlines. There are noticeable
        improvements to fonts on the screen when instructions are
        carefully applied to the sidebearings. The gain in readability
        is offset by the necessity for the OS to grid fit the glyphs
        in order to find the actual advance width for the glyphs
        (since instructions may be moving the sidebearing points). The
        TrueType outline format already has two mechanisms to side
        step the speed issues: the <a class="link" href="chapter.hdmx.html" title="Chapter 33. hdmx - Horizontal Device Metrics">hdmx</a> table,
        where precomputed advance widths may be saved for selected
        ppem sizes, and the 'vdmx' table, where precomputed vertical
        advance widths may be saved for selected ppem sizes. The
        <a class="link" href="chapter.LTSH.html" title="Chapter 35. LTSH - Linear Threshold">LTSH</a> table (Linear ThreSHold) is a second,
        complementary method.</p><p>The LTSH table defines the point at which it is
        reasonable to assume linearly scaled advance widths on a
        glyph-by-glyph basis. This table should not be included unless
        bit 4 of the "flags" field in the <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a>
        table is set. The criteria for linear scaling is:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>(ppem size is &gt;= 50) AND (difference between the
              rounded linear width and the rounded instructed width
              &lt;= 2% of the rounded linear width)</p></li><li class="listitem"><p>Linear width == Instructed width</p></li></ul></div><p>The LTSH table records the ppem for each glyph at which
          the scaling becomes linear again, despite instructions
          effecting the advance width. It is a requirement that, at
          and above the recorded threshold size, the glyph remain
          linear in its scaling (i.e., not legal to set threshold at
          55 ppem if glyph becomes nonlinear again at 90 ppem). The
          format for the table is:</p><div class="table"><a name="idm237274144768"></a><p class="title"><strong>Table 35.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Version number (starts at 0).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numGlyphs</td><td>Number of glyphs (from "numGlyphs" in <a class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a>
              table).</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yPels [numGlyphs]</td><td>The vertical pel height at which the glyph
              can be assumed to scale linearly. On a per glyph
              basis.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Note that glyphs which do not have instructions on their
          sidebearings should have yPels = 1; i.e., always scales
          linearly.</p></div></div></div>