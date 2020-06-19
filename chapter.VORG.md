<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VORG"></a>Chapter 38. VORG - Vertical Origin Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300706422000"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.39.1.1"></a>Specification</h4></div></div></div><p>This table specifies the y coordinate of the vertical
          origin of every glyph in the font.</p><p>This table may be optionally present only in CFF
          CommonType fonts. If present in TrueType CommonType fonts it
          must be ignored by font clients, just as any other
          unrecognized table would be. This is because this table is
          not needed for TrueType CommonType fonts: the Vertical Metrics
          (<a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a>) and Glyph Data
          (<a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a>) tables in TrueType CommonType fonts
          provide all the information necessary to accurately
          calculate the y coordinate of a glyph's vertical origin. See
          the "Vertical Origin and Advance Height" section in the
          <a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a> table specification for more
          details.</p><p>This table was added to version 1.3 of the CommonType
          specification. Note that the <a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a> and
          Vertical Header (<a class="link" href="chapter.vhea.html" title="Chapter 36. vhea - Vertical Header Table">vhea</a>) tables continue to
          be required for all CommonType fonts that support vertical
          writing. Advance heights must continue to be obtained from
          the <a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a> table; that is the only place
          they are stored.</p><p>If a <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a> table is present in a CFF
          CommonType font, a font client may choose to obtain the y
          coordinate of a glyph’s vertical origin either:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>directly from the <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a>, or:</p></li><li class="listitem"><p> by first calculating the top of the glyph's
              bounding box from the CFF charstring data and then
              adding to it the glyph's top side bearing from the
              <a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a> table.</p></li></ul></div><p>The former method offers the advantage of increased
          accuracy and efficiency, since bounding box results
          calculated from the CFF charstring as in the latter method
          can differ depending on the rounding decisions and data
          types of the bounding box algorithm. The latter method
          provides compatibility for font clients who are either
          unaware of or choose not to support the <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a>.</p><p>Thus, the <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a> doesn't add any new font metric values
          per se; it simply improves accuracy and efficiency for CFF
          CommonType font clients, since the intermediate step of
          calculating bounding boxes from the CFF charstring is
          rendered unnecessary.</p><p>See the section "CommonType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300706404992"></a>Vertical Origin Table Format</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.39.2.1"></a>Specification</h4></div></div></div><div class="table"><a name="idm300706403168"></a><p class="title"><strong>Table 38.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>majorVersion</td><td>Major version (starting at 1). Set to
              1.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>minorVersion</td><td>Minor version (starting at 0). Set to
              0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>defaultVertOriginY</td><td>The y coordinate of a glyph's vertical
              origin, in the font's design coordinate system, to be
              used if no entry is present for the glyph in the
              vertOriginYMetrics array.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numVertOriginYMetrics</td><td>Number of elements in the vertOriginYMetrics
              array.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is immediately followed by the vertOriginYMetrics
          array (if numVertOriginYMetrics is non-zero), which has
          numVertOriginYMetrics elements of the following
          format:</p><div class="table"><a name="idm300706394304"></a><p class="title"><strong>Table 38.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>glyphIndex</td><td> Glyph index.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>vertOriginY</td><td>Y coordinate, in the font's design coordinate
              system, of the vertical origin of glyph with index
              glyphIndex.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This array must be sorted by increasing glyphIndex, and
          must not have more than one element with the same
          glyphIndex. In a size-optimized implementation, glyphs whose
          vertical origin's y coordinate equals defaultVertOriginY
          will not have an entry in this array.</p><p>If all glyphs in a font share the same
          defaultVertOriginY value, the length of the <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a> table
          will be 8 bytes in a size-optimized implementation, since
          the vertOriginYMetrics array will be absent.</p><p>Typically only the full-width Latin glyphs in an East
          Asian font will have entries in the vertOriginYMetrics
          array. Glyphs rotated for vertical writing, as used in the
          Vertical Alternates and Rotation ('vrt2') feature, for
          example, can take advantage of the default value if they are
          designed appropriately.</p><p>In the following example of a complete <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a> table for
          a 1000-unit-em font, every glyph in the font is specified as
          having a vertOriginY of 880 except for glyphs with glyph
          indexes 10, 12, and 13:</p><div class="literallayout"><p><br/>
majorVersion         =1<br/>
minorVersion         =0<br/>
defaultVertOriginY   =880<br/>
numVertOriginYMetrics=3<br/>
--- vertOriginYMetrics[index]=(glyphIndex,vertOriginY)<br/>
[0]=(10,889)<br/>
[1]=(12,861)<br/>
[2]=(13,849)<br/>
</p></div></div></div></div>