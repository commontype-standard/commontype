<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VORG"></a>Chapter 39. VORG - Vertical Origin Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383050912656"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.39.1.1"></a>Specification</h3></div></div></div><p role="">This table specifies the y coordinate of the vertical
          origin of every glyph in the font.</p><p role="">This table may be optionally present only in CFF
          OpenType fonts. If present in TrueType OpenType fonts it
          must be ignored by font clients, just as any other
          unrecognized table would be. This is because this table is
          not needed for TrueType OpenType fonts: the Vertical Metrics
          (<a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a>) and Glyph Data
          (<a role="" class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a>) tables in TrueType OpenType fonts
          provide all the information necessary to accurately
          calculate the y coordinate of a glyph's vertical origin. See
          the "Vertical Origin and Advance Height" section in the
          <a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> table specification for more
          details.</p><p role="">This table was added to version 1.3 of the OpenType
          specification. Note that the <a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> and
          Vertical Header (<a role="" class="link" href="chapter.vhea.html" title="Chapter 37. vhea - Vertical Header Table">vhea</a>) tables continue to
          be required for all OpenType fonts that support vertical
          writing. Advance heights must continue to be obtained from
          the <a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> table; that is the only place
          they are stored.</p><p role="">If a <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a> table is present in a CFF
          OpenType font, a font client may choose to obtain the y
          coordinate of a glyph’s vertical origin either:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">directly from the <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a>, or:</p></li><li role="" class="listitem"><p role=""> by first calculating the top of the glyph's
              bounding box from the CFF charstring data and then
              adding to it the glyph's top side bearing from the
              <a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a> table.</p></li></ul></div><p role="">The former method offers the advantage of increased
          accuracy and efficiency, since bounding box results
          calculated from the CFF charstring as in the latter method
          can differ depending on the rounding decisions and data
          types of the bounding box algorithm. The latter method
          provides compatibility for font clients who are either
          unaware of or choose not to support the <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a>.</p><p role="">Thus, the <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a> doesn't add any new font metric values
          per se; it simply improves accuracy and efficiency for CFF
          OpenType font clients, since the intermediate step of
          calculating bounding boxes from the CFF charstring is
          rendered unnecessary.</p><p role="">See the section "OpenType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
          Korean) fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383050896080"></a>Vertical Origin Table Format</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.39.2.1"></a>Specification</h3></div></div></div><div class="table"><a name="idm383050894256"></a><p class="title"><strong>Table 39.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">majorVersion</td><td role="">Major version (starting at 1). Set to
              1.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">minorVersion</td><td role="">Minor version (starting at 0). Set to
              0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">defaultVertOriginY</td><td role="">The y coordinate of a glyph's vertical
              origin, in the font's design coordinate system, to be
              used if no entry is present for the glyph in the
              vertOriginYMetrics array.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numVertOriginYMetrics</td><td role="">Number of elements in the vertOriginYMetrics
              array.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is immediately followed by the vertOriginYMetrics
          array (if numVertOriginYMetrics is non-zero), which has
          numVertOriginYMetrics elements of the following
          format:</p><div class="table"><a name="idm383050885392"></a><p class="title"><strong>Table 39.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">glyphIndex</td><td role=""> Glyph index.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">vertOriginY</td><td role="">Y coordinate, in the font's design coordinate
              system, of the vertical origin of glyph with index
              glyphIndex.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This array must be sorted by increasing glyphIndex, and
          must not have more than one element with the same
          glyphIndex. In a size-optimized implementation, glyphs whose
          vertical origin's y coordinate equals defaultVertOriginY
          will not have an entry in this array.</p><p role="">If all glyphs in a font share the same
          defaultVertOriginY value, the length of the <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a> table
          will be 8 bytes in a size-optimized implementation, since
          the vertOriginYMetrics array will be absent.</p><p role="">Typically only the full-width Latin glyphs in an East
          Asian font will have entries in the vertOriginYMetrics
          array. Glyphs rotated for vertical writing, as used in the
          Vertical Alternates and Rotation ('vrt2') feature, for
          example, can take advantage of the default value if they are
          designed appropriately.</p><p role="">In the following example of a complete <a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a> table for
          a 1000-unit-em font, every glyph in the font is specified as
          having a vertOriginY of 880 except for glyphs with glyph
          indexes 10, 12, and 13:</p><div role="" class="literallayout"><p><br/>
<br/>
majorVersion         =1<br/>
minorVersion         =0<br/>
defaultVertOriginY   =880<br/>
numVertOriginYMetrics=3<br/>
--- vertOriginYMetrics[index]=(glyphIndex,vertOriginY)<br/>
[0]=(10,889)<br/>
[1]=(12,861)<br/>
[2]=(13,849)<br/>
<br/>
</p></div></div></div></div>