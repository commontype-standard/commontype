<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vmtx"></a>Chapter 38. vmtx - Vertical Metrics Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320128070048"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.38.1.1"></a>Specification</h3></div></div></div><p role="">The vertical metrics table allows you to specify the
          vertical spacing for each glyph in a vertical font. This
          table consists of either one or two arrays that contain
          metric information (the advance heights and top
          sidebearings) for the vertical layout of each of the glyphs
          in the font. The vertical metrics coordinate system is shown
          below.</p><div class="figure"><a name="idm320128067536"></a><p class="title"><strong>Figure 38.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
            scripts</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/img00287.gif" alt="Figure 2a. Glyphs in the Latin, Kanji, and Arabic scripts"/></div></div></div><br class="figure-break"/><p role="">OpenType vertical fonts require both a vertical
          header table (<a role="" class="link" href="chapter.vhea.md" title="Chapter 37. vhea - Vertical Header Table">vhea</a>) and the vertical metrics table
          discussed below. The vertical header table contains
          information that is general to the font as a whole. The
          vertical metrics table contains information that pertains to
          specific glyphs. The formats of these tables are similar to
          those for horizontal metrics (hhea and hmtx).</p><p role="">See the section "OpenType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320128062832"></a>Vertical Origin and Advance Height</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.38.2.1"></a>Specification</h3></div></div></div><p role="">The y coordinate of a glyph's vertical origin is
          specified as the sum of the glyph's top side bearing
          (recorded in the <a role="" class="link" href="chapter.vmtx.md" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> table) and the top (i.e. maximum y)
          of the glyph’s bounding box.</p><p role="">TrueType OpenType fonts contain glyph bounding box
          information in the Glyph Data (<a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a>)
          table. CFF OpenType fonts do not contain glyph bounding box
          information, and so for these fonts the top of the glyph's
          bounding box must be calculated from the charstring data in
          the Compact Font Format (<a role="" class="link" href="chapter.CFF.md" title="Chapter 19. CFF - PostScript font program (Compact Font Format) table">CFF</a>) table.</p><p role="">OpenType 1.3 introduced the optional Vertical Origin
          (<a role="" class="link" href="chapter.VORG.md" title="Chapter 39. VORG - Vertical Origin Table">VORG</a>) table for CFF OpenType fonts,
          which records the y coordinate of glyphs' vertical origins
          directly, thus obviating the need to calculate bounding
          boxes as an intermediate step. This improves accuracy and
          efficiency for CFF OpenType clients.</p><p role="">The x coordinate of a glyph's vertical origin is not
          specified in the <a role="" class="link" href="chapter.vmtx.md" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> table. Vertical writing
          implementions may make use of the baseline values in the
          Baseline (<a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>) table, if present, in
          order to align the glyphs in the x direction as appropriate
          to the desired vertical baseline.</p><p role="">The advance height of a glyph starts from the y
          coordinate of the glyph’s vertical origin and advances
          downwards. Its endpoint is at the y coordinate of the
          vertical origin of the next glyph in the run, by default.
          Metric-adjustment OpenType layout features such as Vertical
          Kerning ('vkrn') could modify the vertical advances in a
          manner similar to kerning in horizontal mode.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320128052512"></a>Vertical Metrics Table Format</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.38.3.1"></a>Specification</h3></div></div></div><p role="">The overall structure of the vertical metrics table
          consists of two arrays shown below: the vMetrics array
          followed by an array of top side bearings. The top side
          bearing is measured relative to the top of the origin of
          glyphs, for vertical composition of ideographic
          glyphs.</p><p role="">This table does not have a header, but does require that
          the number of glyphs included in the two arrays equals the
          total number of glyphs in the font.</p><p role="">The number of entries in the vMetrics array is
          determined by the value of the numOfLongVerMetrics field of
          the vertical header table.</p><p role="">The vMetrics array contains two values for each entry.
          These are the advance height and the top sidebearing for
          each glyph included in the array.</p><p role="">In monospaced fonts, such as Courier or Kanji, all
          glyphs have the same advance height. If the font is
          monospaced, only one entry need be in the first array, but
          that one entry is required.</p><p role="">The format of an entry in the vertical metrics array is
          given below.</p><div class="table"><a name="idm320128047232"></a><p class="title"><strong>Table 38.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">advanceHeight</td><td role="">The advance height of the glyph. Unsigned
              integer in FUnits </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">topSideBearing</td><td role="">The top sidebearing of the glyph. Signed
              integer in FUnits.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The second array is optional and generally is used for a
          run of monospaced glyphs in the font. Only one such run is
          allowed per font, and it must be located at the end of the
          font. This array contains the top sidebearings of glyphs not
          represented in the first array, and all the glyphs in this
          array must have the same advance height as the last entry in
          the vMetrics array. All entries in this array are therefore
          monospaced.</p><p role="">The number of entries in this array is calculated by
          subtracting the value of numOfLongVerMetrics from the number
          of glyphs in the font. The sum of glyphs represented in the
          first array plus the glyphs represented in the second array
          therefore equals the number of glyphs in the font. The
          format of the top sidebearing array is given below.</p><div class="table"><a name="idm320128040464"></a><p class="title"><strong>Table 38.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">SHORT</td><td role="">topSideBearing []</td><td role="">The top sidebearing of the glyph. Signed
              integer in FUnits. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>