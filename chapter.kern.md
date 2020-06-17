<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.kern"></a>Chapter 33. kern - Kerning</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383049890160"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.33.1.1"></a>Specification</h3></div></div></div><p role="">Note: Apple has extended the definition of the
	<a role="" class="link" href="chapter.kern.html" title="Chapter 33. kern - Kerning">kern</a> table to provide additional
	functionality. The Apple extensions are not supported on
	Windows. Fonts intended for cross-platform use or for the
	Windows platform in general should conform to the
	<a role="" class="link" href="chapter.kern.html" title="Chapter 33. kern - Kerning">kern</a> table format specified here.</p><p role="">The kerning table contains the values that control the
        intercharacter spacing for the glyphs in a font. There is
        currently no system level support for kerning (other than
        returning the kern pairs and kern values). OpenType fonts
        containing CFF outlines are not supported by the
        <a role="" class="link" href="chapter.kern.html" title="Chapter 33. kern - Kerning">kern</a> table and must use the
        <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> OpenType Layout table.</p><p role="">Each subtable varies in format, and can contain
        information for vertical or horizontal text, and can contain
        kerning values or minimum values. Kerning values are used to
        adjust inter-character spacing, and minimum values are used to
        limit the amount of adjustment that the scaler applies by the
        combination of kerning and tracking. Because the adjustments
        are additive, the order of the subtables containing kerning
        values is not important. However, tables containing minimum
        values should usually be placed last, so that they can be used
        to limit the total effect of other subtables.</p><p role="">The kerning table in the OpenType font file has a
        header, which contains the format number and the number of
        subtables present, and the subtables themselves.</p><div class="table"><a name="idm383049882800"></a><p class="title"><strong>Table 33.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Table version number (starts at
              0)</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">nTables</td><td role="">Number of subtables in the kerning
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Kerning subtables will share the same header format.
        This header is used to identify the format of the subtable and
        the kind of information it contains:</p><div class="table"><a name="idm383049877184"></a><p class="title"><strong>Table 33.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Kern subtable version number</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">Length of the subtable, in bytes (including
              this header). </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">coverage</td><td role="">What type of information is contained in this
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The coverage field is divided into the following
        sub-fields, with sizes given in bits:</p><div class="table"><a name="idm383049870144"></a><p class="title"><strong>Table 33.3. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">0</td><td role="">1</td><td role="">1 if table has horizontal data, 0 if
              vertical.</td><td class="auto-generated"> </td></tr><tr><td role="">1</td><td role="">1</td><td role="">If this bit is set to 1, the table has
              minimum values. If set to 0, the table has kerning
              values.</td><td class="auto-generated"> </td></tr><tr><td role="">2</td><td role="">1</td><td role="">
	      <p role="">If set to 1, kerning is perpendicular to the flow
		of the text.</p>

	      <p role="">If the text is normally written horizontally,
		kerning will be done in the up and down directions. If
		kerning values are positive, the text will be kerned
		upwards; if they are negative, the text will be kerned
		downwards.</p>

	      <p role="">If the text is normally written vertically,
		kerning will be done in the left and right
		directions. If kerning values are positive, the text
		will be kerned to the right; if they are negative, the
		text will be kerned to the left.</p> <p role="">The
		value 0x8000 in the kerning data resets the
		cross-stream kerning back to 0.</p>
            </td><td class="auto-generated"> </td></tr><tr><td role="">3</td><td role="">1</td><td role="">If this bit is set to 1 the value in this
              table should replace the value currently being
              accumulated.</td><td class="auto-generated"> </td></tr><tr><td role="">4-7</td><td role="">4</td><td role="">Reserved. This should be set to
              zero.</td><td class="auto-generated"> </td></tr><tr><td role="">8-15</td><td role="">8</td><td role="">Format of the subtable. Only formats 0 and 2
              have been defined. Formats 1 and 3 through 255 are
              reserved for future use.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383049856320"></a>Format 0</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.33.2.1"></a>Specification</h3></div></div></div><p role="">This is the only format that will be properly
          interpreted by Windows and OS/2.</p><p role="">This subtable is a sorted list of kerning pairs and
          values. The list is preceded by information which makes it
          possible to make an efficient binary search of the
          list:</p><div class="table"><a name="idm383049853440"></a><p class="title"><strong>Table 33.4. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">nPairs</td><td role="">This gives the number of kerning pairs in the
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">searchRange</td><td role="">The largest power of two less than or equal
              to the value of nPairs, multiplied by the size in bytes
              of an entry in the table.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">entrySelector</td><td role="">This is calculated as log2 of the largest
              power of two less than or equal to the value of nPairs.
              This value indicates how many iterations of the search
              loop will have to be made. (For example, in a list of
              eight items, there would have to be three iterations of
              the loop).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">rangeShift</td><td role="">The value of nPairs minus the largest power
              of two less than or equal to nPairs, and then multiplied
              by the size in bytes of an entry in the
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is followed by the list of kerning pairs and
          values. Each has the following format:</p><div class="table"><a name="idm383049844352"></a><p class="title"><strong>Table 33.5. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">left</td><td role="">The glyph index for the left-hand glyph in
              the kerning pair.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">right</td><td role="">The glyph index for the right-hand glyph in
              the kerning pair. </td><td class="auto-generated"> </td></tr><tr><td role="">FWORD</td><td role="">value</td><td role="">The kerning value for the above pair, in
              FUnits. If this value is greater than zero, the
              characters will be moved apart. If this value is less
              than zero, the character will be moved closer
              together.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The left and right halves of the kerning pair make an
	unsigned 32-bit number, which is then used to order the
	kerning pairs numerically.</p><p role="">A binary search is most efficiently coded if the search
	range is a power of two. The search range can be reduced by
	half by shifting instead of dividing. In general, the number
	of kerning pairs, nPairs, will not be a power of two. The
	value of the search range, searchRange, should be the largest
	power of two less than or equal to nPairs. The number of pairs
	not covered by searchRange (that is, nPairs - searchRange) is
	the value rangeShift.</p><p role="">Windows v3.1 does not make use of the
        <a role="" class="link" href="chapter.kern.html" title="Chapter 33. kern - Kerning">kern</a> data other than to expose it to
        applications through the GetFontData() API.Format 2 </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383049834464"></a>Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.33.3.1"></a>Specification</h3></div></div></div><p role="">This subtable is a two-dimensional array of kerning
          values. The glyphs are mapped to classes, using a different
          mapping for left- and right-hand glyphs. This allows glyphs
          that have similar right- or left-side shapes to be handled
          together. Each similar right- or left-hand shape is said to
          be single class.</p><p role="">Each row in the kerning array represents one left-hand
          glyph class, each column represents one right-hand glyph
          class, and each cell contains a kerning value. Row and
          column 0 always represent glyphs that do not kern and
          contain all zeros.</p><p role="">The values in the right class table are stored
          pre-multiplied by the number of bytes in a single kerning
          value, and the values in the left class table are stored
          pre-multiplied by the number of bytes in one row. This
          eliminates needing to multiply the row and column values
          together to determine the location of the kerning value. The
          array can be indexed by doing the right- and left-hand class
          mappings, adding the class values to the address of the
          array, and fetching the kerning value to which the new
          address points.</p><p role="">The header for the simple array has the following
          format:</p><div class="table"><a name="idm383049830368"></a><p class="title"><strong>Table 33.6. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">rowWidth</td><td role="">The width, in bytes, of a row in the
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">leftClassTable</td><td role="">Offset from beginning of this subtable to
              left-hand class table.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">rightClassTable</td><td role="">Offset from beginning of this subtable to
              right-hand class table. </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">array</td><td role="">Offset from beginning of this subtable to the
              start of the kerning array. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each class table has the following header:</p><div class="table"><a name="idm383049821808"></a><p class="title"><strong>Table 33.7. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">firstGlyph</td><td role="">First glyph in class range.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">nGlyphs</td><td role="">Number of glyph in class range.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This header is followed by nGlyphs number of class
          values, which are in USHORT format. Entries for glyphs that
          don't participate in kerning should point to the row or
          column at position zero.</p><p role="">The array itself is a left by right array of kerning
          values, which are FWords, where left is the number of
          left-hand classes and R is the number of right-hand classes.
          The array is stored by row.</p><p role="">Note that this format is the quickest to process since
          each lookup requires only a few index operations. The table
          can be quite large since it will contain the number of cells
          equal to the product of the number of right-hand classes and
          the number of left-hand classes, even though many of these
          classes do not kern with each other.</p></div></div></div>