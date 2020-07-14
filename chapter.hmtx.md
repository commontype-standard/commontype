<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.hmtx"></a>Chapter 8. hmtx - Horizontal Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239471405440"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.9.1.1"></a>Specification</h4></div></div></div><p>The type longHorMetric is defined as an array where each
          element has two parts: the advance width, which is of type
          USHORT, and the left side bearing, which is of type SHORT.
          Or, more formally:</p><div class="literallayout"><p><br/>
typedef struct  _longHorMetric {<br/>
     USHORT advanceWidth;<br/>
     SHORT  lsb;<br/>
}  longHorMetric;<br/>
</p></div><div class="table"><a name="idm239471402560"></a><p class="title"><strong>Table 8.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>longHorMetric [numberOfHMetrics]</td><td>hMetrics</td><td>Paired advance width and left side bearing
              values for each glyph. The value numOfHMetrics comes
              from the <a class="link" href="chapter.hhea.html" title="Chapter 7. hhea - Horizontal Header">hhea</a> table. If the font is
              monospaced, only one entry need be in the array, but
              that entry is required. The last entry applies to all
              subsequent glyphs.</td><td class="auto-generated"> </td></tr><tr><td>FWord [ ]</td><td>leftSideBearing</td><td>Here the advanceWidth is assumed to be the
              same as the advanceWidth for the last entry above. The
              number of entries in this array is derived from
              numGlyphs (from <a class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a> table) minus
              numberOfHMetrics. This generally is used with a run of
              monospaced glyphs (e.g., Kanji fonts or Courier fonts).
              Only one run is allowed and it must be at the end. This
              allows a monospaced font to vary the left side bearing
              values for each glyph.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>In CFF CommonType fonts, every glyph's advanceWidth as
          recorded in the <a class="link" href="chapter.hmtx.html" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a> table must be identical to its x
          width in the <a class="link" href="chapter.CFF.html" title="Chapter 19. CFF - PostScript font program (Compact Font Format) table">CFF</a> table.</p><p>For any glyph, xmax and xmin are given in
          <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> table, lsb and aw are given in
          <a class="link" href="chapter.hmtx.html" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a> table. rsb is calculated as
          follows:</p><div class="literallayout"><p><br/>
rsb = aw - (lsb + xmax - xmin)<br/>
</p></div><p>If pp1 and pp2 are phantom points used to control lsb
          and rsb, their initial position in x is calculated as
          follows:</p><div class="literallayout"><p><br/>
pp1 = xmin - lsb<br/>
pp2 = pp1 + aw<br/>
</p></div></div></div></div>