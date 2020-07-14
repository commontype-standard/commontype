<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.prep"></a>Chapter 18. prep - Control Value Program </h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm421902486816"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.19.1.1"></a>Specification</h4></div></div></div><p>The Control Value Program consists of a set of TrueType
          instructions that will be executed whenever the font or
          point size or transformation matrix change and before each
          glyph is interpreted. Any instruction is legal in the CVT
          Program but since no glyph is associated with it,
          instructions intended to move points within a particular
          glyph outline cannot be used in the CVT Program. The name
          <a class="link" href="chapter.prep.html" title="Chapter 18. prep - Control Value Program">prep</a> is anachronistic.</p><div class="table"><a name="idm421902483744"></a><p class="title"><strong>Table 18.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>BYTE [n]</td><td> </td><td>Set of instructions executed whenever point
	      size or font or transformation change. n is the number
	      of BYTE items that fit in the size of the table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>