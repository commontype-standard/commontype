<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.loca"></a>Chapter 17. loca - Index to Location</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114628154464"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.17.1.1"></a>Specification</h3></div></div></div><p role="">The indexToLoc table stores the offsets to the locations
          of the glyphs in the font, relative to the beginning of the
          glyphData table. In order to compute the length of the last
          glyph element, there is an extra entry after the last valid
          index.</p><p role="">By definition, index zero points to the "missing
          character," which is the character that appears if a
          character is not found in the font. The missing character is
          commonly represented by a blank box (such as ) or a space.
          If the font does not contain an outline for the missing
          character, then the first and second offsets should have the
          same value. This also applies to any other character without
          an outline, such as the space character.</p><p role="">Most routines will look at the <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a>
          table to determine the number of glyphs in the font, but the
          value in the <a role="" class="link" href="chapter.loca.md" title="Chapter 17. loca - Index to Location">loca</a> table should
          agree.</p><p role="">There are two versions of this table, the short and the
          long. The version is specified in the indexToLocFormat entry
          in the <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a> table.</p><h4><a name="idm114628148160"></a>Short version</h4><div class="table"><a name="idm114628147760"></a><p class="title"><strong>Table 17.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">offsets [n]</td><td role="">The actual local offset divided by 2 is
              stored. The value of n is numGlyphs + 1. The value for
              numGlyphs is found in the <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a>
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><h4><a name="idm114628143440"></a>Long version</h4><div class="table"><a name="idm114628143040"></a><p class="title"><strong>Table 17.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">offsets [n]</td><td role="">The actual local offset is stored. The value
              of n is numGlyphs + 1. The value for numGlyphs is found
              in the <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a> table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Note that the local offsets should be long-aligned,
          i.e., multiples of 4. Offsets which are not long-aligned may
          seriously degrade performance of some processors.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.17.1.2"></a>Annotation</h3></div></div></div><p role="">We assume that 'indexToLoc' should be replaced by 'loca'
	  and 'glyphData' should be replaced by 'glyph'.</p></div></div></div>