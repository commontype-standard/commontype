<h4 id="post" rel="off-5.2.10+8.22"><dfn>post table</dfn> - PostScript Table</h4>

<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required for font producers, optional for font consumers</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This table describes parameters useful for rendering the font data on PostScript printers.

<pre class=biblio>
  {
    "tt-post": {
    "title": "TrueType Reference Manual: Glyph Name and PostScript Font Table",
    "href": "https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6post.html",
    "publisher": "Apple"
	}
  }
</pre>

<pre class=include>path: idl/postTable.md</pre>

<dl dfn-type=attribute dfn-for=postTableCommon>
  <dt><dfn>italicAngle</dfn></dt>
 	<dd>Italic angle measured in counter-clockwise degrees.</dd>
  <dt><dfn>isFixedPitch</dfn></dt>
  	<dd>If set to non-zero, the renderer may regard this as strictly a fixed pitch font. Discouraged in CommonType; font producers should set to zero.</dd>
</dl>

<dl dfn-type=attribute dfn-for=postTableVersion20>
  <dt><dfn>glyphNameIndex</dfn></dt>
  <dd>Array of {{postTableVersion20/numGlyphs}} glyph name indices. If the index is less than 258, the glyph at this position takes its name from the Macintosh glyph list (see below). Otherwise, 258 is subtracted from the index, and this is used as an index into the {{postTableVersion20/names}} array.</dd>
  <dt><dfn>names</dfn></dt>
  <dd>Array of {{PascalString}}s containing glyph names. The number of elements is determined by the greatest index in the {{postTableVersion20/glyphNameIndex}} array.</dd>
</dl>

<h5 id="avar.in-prod">Implementation notes for font producers</h5>

* The {{minMemType42}}, {{maxMemType42}}, {{minMemType1}} and {{maxMemType1}} fields are discouraged in CommonType. (They were intended to describe memory requirements for downloading the font onto a PostScript printer.) Font producers should set these to zero.

* {{postTableVersion10}} should only be used when the font contains exactly 258 glyph names in Macintosh order; see [[tt-post]] for the glyph names and order. {{postTableVersion25}} is deprecated and should not be used by font producers. Otherwise, {{postTableVersion20}} should be used to specify glyph names, or {{postTableVersion30}} when glyph names are to be omitted.

