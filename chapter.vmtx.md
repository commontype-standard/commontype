<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vmtx"></a>Chapter 39. vmtx - Vertical Metrics Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm20496"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.1.1"></a>Specification</h4></div></div></div><p>The vertical metrics table allows you to specify the
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vmtx"></a>Chapter 39. vmtx - Vertical Metrics Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189291936672"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.1.1"></a>Specification</h4></div></div></div><p>The vertical metrics table allows you to specify the
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vmtx"></a>Chapter 39. vmtx - Vertical Metrics Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62722865232"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.1.1"></a>Specification</h4></div></div></div><p>The vertical metrics table allows you to specify the
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vmtx"></a>Chapter 39. vmtx - Vertical Metrics Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465834439776"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.1.1"></a>Specification</h4></div></div></div><p>The vertical metrics table allows you to specify the
>>>>>>> Rebuild
          vertical spacing for each glyph in a vertical font. This
          table consists of either one or two arrays that contain
          metric information (the advance heights and top
          sidebearings) for the vertical layout of each of the glyphs
          in the font. The vertical metrics coordinate system is shown
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          below.</p><div class="figure"><a name="idm20501"></a><p class="title"><strong>Figure 39.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
=======
          below.</p><div class="figure"><a name="idm189291934160"></a><p class="title"><strong>Figure 39.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
>>>>>>> Rebuild
=======
          below.</p><div class="figure"><a name="idm62722862720"></a><p class="title"><strong>Figure 39.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
>>>>>>> Rebuild
=======
          below.</p><div class="figure"><a name="idm465834437264"></a><p class="title"><strong>Figure 39.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
>>>>>>> Rebuild
            scripts</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../img00287.gif" alt="Figure 2a. Glyphs in the Latin, Kanji, and Arabic scripts"/></div></div></div><br class="figure-break"/><p>CommonType vertical fonts require both a vertical
          header table (<a class="link" href="chapter.vhea.html" title="Chapter 38. vhea - Vertical Header Table">vhea</a>) and the vertical metrics table
          discussed below. The vertical header table contains
          information that is general to the font as a whole. The
          vertical metrics table contains information that pertains to
          specific glyphs. The formats of these tables are similar to
          those for horizontal metrics (hhea and hmtx).</p><p>See the section "CommonType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm20509"></a>Vertical Origin and Advance Height</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.2.1"></a>Specification</h4></div></div></div><p>The y coordinate of a glyph's vertical origin is
=======
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189291929456"></a>Vertical Origin and Advance Height</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.2.1"></a>Specification</h4></div></div></div><p>The y coordinate of a glyph's vertical origin is
>>>>>>> Rebuild
=======
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62722858016"></a>Vertical Origin and Advance Height</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.2.1"></a>Specification</h4></div></div></div><p>The y coordinate of a glyph's vertical origin is
>>>>>>> Rebuild
=======
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465834432560"></a>Vertical Origin and Advance Height</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.2.1"></a>Specification</h4></div></div></div><p>The y coordinate of a glyph's vertical origin is
>>>>>>> Rebuild
          specified as the sum of the glyph's top side bearing
          (recorded in the <a class="link" href="chapter.vmtx.html" title="Chapter 39. vmtx - Vertical Metrics Table">vmtx</a> table) and the top (i.e. maximum y)
          of the glyph’s bounding box.</p><p>TrueType CommonType fonts contain glyph bounding box
          information in the Glyph Data (<a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a>)
          table. CFF CommonType fonts do not contain glyph bounding box
          information, and so for these fonts the top of the glyph's
          bounding box must be calculated from the charstring data in
          the Compact Font Format (<a class="link" href="chapter.CFF.html" title="Chapter 19. CFF - PostScript font program (Compact Font Format) table">CFF</a>) table.</p><p>CommonType 1.3 introduced the optional Vertical Origin
          (<a class="link" href="chapter.VORG.html" title="Chapter 40. VORG - Vertical Origin Table">VORG</a>) table for CFF CommonType fonts,
          which records the y coordinate of glyphs' vertical origins
          directly, thus obviating the need to calculate bounding
          boxes as an intermediate step. This improves accuracy and
          efficiency for CFF CommonType clients.</p><p>The x coordinate of a glyph's vertical origin is not
          specified in the <a class="link" href="chapter.vmtx.html" title="Chapter 39. vmtx - Vertical Metrics Table">vmtx</a> table. Vertical writing
          implementions may make use of the baseline values in the
          Baseline (<a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>) table, if present, in
          order to align the glyphs in the x direction as appropriate
          to the desired vertical baseline.</p><p>The advance height of a glyph starts from the y
          coordinate of the glyph’s vertical origin and advances
          downwards. Its endpoint is at the y coordinate of the
          vertical origin of the next glyph in the run, by default.
          Metric-adjustment CommonType layout features such as Vertical
          Kerning ('vkrn') could modify the vertical advances in a
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          manner similar to kerning in horizontal mode.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm20524"></a>Vertical Metrics Table Format</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.3.1"></a>Specification</h4></div></div></div><p>The overall structure of the vertical metrics table
=======
          manner similar to kerning in horizontal mode.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189291919136"></a>Vertical Metrics Table Format</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.3.1"></a>Specification</h4></div></div></div><p>The overall structure of the vertical metrics table
>>>>>>> Rebuild
=======
          manner similar to kerning in horizontal mode.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62722847696"></a>Vertical Metrics Table Format</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.3.1"></a>Specification</h4></div></div></div><p>The overall structure of the vertical metrics table
>>>>>>> Rebuild
=======
          manner similar to kerning in horizontal mode.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465834422240"></a>Vertical Metrics Table Format</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.40.3.1"></a>Specification</h4></div></div></div><p>The overall structure of the vertical metrics table
>>>>>>> Rebuild
          consists of two arrays shown below: the vMetrics array
          followed by an array of top side bearings. The top side
          bearing is measured relative to the top of the origin of
          glyphs, for vertical composition of ideographic
          glyphs.</p><p>This table does not have a header, but does require that
          the number of glyphs included in the two arrays equals the
          total number of glyphs in the font.</p><p>The number of entries in the vMetrics array is
          determined by the value of the numOfLongVerMetrics field of
          the vertical header table.</p><p>The vMetrics array contains two values for each entry.
          These are the advance height and the top sidebearing for
          each glyph included in the array.</p><p>In monospaced fonts, such as Courier or Kanji, all
          glyphs have the same advance height. If the font is
          monospaced, only one entry need be in the first array, but
          that one entry is required.</p><p>The format of an entry in the vertical metrics array is
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          given below.</p><div class="table"><a name="idm20534"></a><p class="title"><strong>Table 39.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>advanceHeight</td><td>The advance height of the glyph. Unsigned
=======
          given below.</p><div class="table"><a name="idm189291913856"></a><p class="title"><strong>Table 39.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>advanceHeight</td><td>The advance height of the glyph. Unsigned
>>>>>>> Rebuild
=======
          given below.</p><div class="table"><a name="idm62722842416"></a><p class="title"><strong>Table 39.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>advanceHeight</td><td>The advance height of the glyph. Unsigned
>>>>>>> Rebuild
=======
          given below.</p><div class="table"><a name="idm465834416960"></a><p class="title"><strong>Table 39.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>advanceHeight</td><td>The advance height of the glyph. Unsigned
>>>>>>> Rebuild
              integer in <em class="glossterm">font unit</em>s </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>topSideBearing</td><td>The top sidebearing of the glyph. Signed
              integer in <em class="glossterm">font unit</em>s.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The second array is optional and generally is used for a
          run of monospaced glyphs in the font. Only one such run is
          allowed per font, and it must be located at the end of the
          font. This array contains the top sidebearings of glyphs not
          represented in the first array, and all the glyphs in this
          array must have the same advance height as the last entry in
          the vMetrics array. All entries in this array are therefore
          monospaced.</p><p>The number of entries in this array is calculated by
          subtracting the value of numOfLongVerMetrics from the number
          of glyphs in the font. The sum of glyphs represented in the
          first array plus the glyphs represented in the second array
          therefore equals the number of glyphs in the font. The
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          format of the top sidebearing array is given below.</p><div class="table"><a name="idm20554"></a><p class="title"><strong>Table 39.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>SHORT</td><td>topSideBearing []</td><td>The top sidebearing of the glyph. Signed
=======
          format of the top sidebearing array is given below.</p><div class="table"><a name="idm189291906256"></a><p class="title"><strong>Table 39.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>SHORT</td><td>topSideBearing []</td><td>The top sidebearing of the glyph. Signed
>>>>>>> Rebuild
=======
          format of the top sidebearing array is given below.</p><div class="table"><a name="idm62722834816"></a><p class="title"><strong>Table 39.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>SHORT</td><td>topSideBearing []</td><td>The top sidebearing of the glyph. Signed
>>>>>>> Rebuild
=======
          format of the top sidebearing array is given below.</p><div class="table"><a name="idm465834409392"></a><p class="title"><strong>Table 39.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>SHORT</td><td>topSideBearing []</td><td>The top sidebearing of the glyph. Signed
>>>>>>> Rebuild
              integer in <em class="glossterm">font unit</em>s. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>