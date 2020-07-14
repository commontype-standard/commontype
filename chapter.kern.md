<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.kern"></a>Chapter 34. kern - Kerning</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm416419698544"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.35.1.1"></a>Specification</h4></div></div></div><p>Note: Apple has extended the definition of the
	<a class="link" href="chapter.kern.html" title="Chapter 34. kern - Kerning">kern</a> table to provide additional
	functionality. The Apple extensions are not supported on
	Windows. Fonts intended for cross-platform use or for the
	Windows platform in general should conform to the
	<a class="link" href="chapter.kern.html" title="Chapter 34. kern - Kerning">kern</a> table format specified here.</p><p>The kerning table contains the values that control the
        intercharacter spacing for the glyphs in a font. There is
        currently no system level support for kerning (other than
        returning the kern pairs and kern values). CommonType fonts
        containing CFF outlines are not supported by the
        <a class="link" href="chapter.kern.html" title="Chapter 34. kern - Kerning">kern</a> table and must use the
        <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> CommonType Layout table.</p><p>Each subtable varies in format, and can contain
        information for vertical or horizontal text, and can contain
        kerning values or minimum values. Kerning values are used to
        adjust inter-character spacing, and minimum values are used to
        limit the amount of adjustment that the scaler applies by the
        combination of kerning and tracking. Because the adjustments
        are additive, the order of the subtables containing kerning
        values is not important. However, tables containing minimum
        values should usually be placed last, so that they can be used
        to limit the total effect of other subtables.</p><p>The kerning table in the CommonType font file has a
        header, which contains the format number and the number of
        subtables present, and the subtables themselves.</p><div class="table"><a name="idm416419691824"></a><p class="title"><strong>Table 34.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Table version number (starts at
              0)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>nTables</td><td>Number of subtables in the kerning
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Kerning subtables will share the same header format.
        This header is used to identify the format of the subtable and
        the kind of information it contains:</p><div class="table"><a name="idm416419686224"></a><p class="title"><strong>Table 34.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Kern subtable version number</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>Length of the subtable, in bytes (including
              this header). </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>coverage</td><td>What type of information is contained in this
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The coverage field is divided into the following
        sub-fields, with sizes given in bits:</p><div class="table"><a name="idm416419679184"></a><p class="title"><strong>Table 34.3. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>0</td><td>1</td><td>1 if table has horizontal data, 0 if
              vertical.</td><td class="auto-generated"> </td></tr><tr><td>1</td><td>1</td><td>If this bit is set to 1, the table has
              minimum values. If set to 0, the table has kerning
              values.</td><td class="auto-generated"> </td></tr><tr><td>2</td><td>1</td><td>
            <p>If set to 1, kerning is perpendicular to the flow
		of the text.</p>
            <p>If the text is normally written horizontally,
		kerning will be done in the up and down directions. If
		kerning values are positive, the text will be kerned
		upwards; if they are negative, the text will be kerned
		downwards.</p>
            <p>If the text is normally written vertically,
		kerning will be done in the left and right
		directions. If kerning values are positive, the text
		will be kerned to the right; if they are negative, the
		text will be kerned to the left.</p>
            <p>The
		value 0x8000 in the kerning data resets the
		cross-stream kerning back to 0.</p>
          </td><td class="auto-generated"> </td></tr><tr><td>3</td><td>1</td><td>If this bit is set to 1 the value in this
              table should replace the value currently being
              accumulated.</td><td class="auto-generated"> </td></tr><tr><td>4-7</td><td>4</td><td>Reserved. This should be set to
              zero.</td><td class="auto-generated"> </td></tr><tr><td>8-15</td><td>8</td><td>Format of the subtable. Only formats 0 and 2
              have been defined. Formats 1 and 3 through 255 are
              reserved for future use.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm416419665360"></a>Format 0</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.35.2.1"></a>Specification</h4></div></div></div><p>This is the only format that will be properly
          interpreted by Windows and OS/2.</p><p>This subtable is a sorted list of kerning pairs and
          values. The list is preceded by information which makes it
          possible to make an efficient binary search of the
          list:</p><div class="table"><a name="idm416419662480"></a><p class="title"><strong>Table 34.4. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>nPairs</td><td>This gives the number of kerning pairs in the
              table.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>searchRange</td><td>The largest power of two less than or equal
              to the value of nPairs, multiplied by the size in bytes
              of an entry in the table.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entrySelector</td><td>This is calculated as log2 of the largest
              power of two less than or equal to the value of nPairs.
              This value indicates how many iterations of the search
              loop will have to be made. (For example, in a list of
              eight items, there would have to be three iterations of
              the loop).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>rangeShift</td><td>The value of nPairs minus the largest power
              of two less than or equal to nPairs, and then multiplied
              by the size in bytes of an entry in the
              table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is followed by the list of kerning pairs and
          values. Each has the following format:</p><div class="table"><a name="idm416419653392"></a><p class="title"><strong>Table 34.5. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>left</td><td>The glyph index for the left-hand glyph in
              the kerning pair.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>right</td><td>The glyph index for the right-hand glyph in
              the kerning pair. </td><td class="auto-generated"> </td></tr><tr><td>FWORD</td><td>value</td><td>The kerning value for the above pair, in
              <em class="glossterm">font unit</em>s. If this value is greater than zero, the
              characters will be moved apart. If this value is less
              than zero, the character will be moved closer
              together.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The left and right halves of the kerning pair make an
	unsigned 32-bit number, which is then used to order the
	kerning pairs numerically.</p><p>A binary search is most efficiently coded if the search
	range is a power of two. The search range can be reduced by
	half by shifting instead of dividing. In general, the number
	of kerning pairs, nPairs, will not be a power of two. The
	value of the search range, searchRange, should be the largest
	power of two less than or equal to nPairs. The number of pairs
	not covered by searchRange (that is, nPairs - searchRange) is
	the value rangeShift.</p><p>Windows v3.1 does not make use of the
        <a class="link" href="chapter.kern.html" title="Chapter 34. kern - Kerning">kern</a> data other than to expose it to
        applications through the GetFontData() API.Format 2 </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm416419626832"></a>Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.35.3.1"></a>Specification</h4></div></div></div><p>This subtable is a two-dimensional array of kerning
          values. The glyphs are mapped to classes, using a different
          mapping for left- and right-hand glyphs. This allows glyphs
          that have similar right- or left-side shapes to be handled
          together. Each similar right- or left-hand shape is said to
          be single class.</p><p>Each row in the kerning array represents one left-hand
          glyph class, each column represents one right-hand glyph
          class, and each cell contains a kerning value. Row and
          column 0 always represent glyphs that do not kern and
          contain all zeros.</p><p>The values in the right class table are stored
          pre-multiplied by the number of bytes in a single kerning
          value, and the values in the left class table are stored
          pre-multiplied by the number of bytes in one row. This
          eliminates needing to multiply the row and column values
          together to determine the location of the kerning value. The
          array can be indexed by doing the right- and left-hand class
          mappings, adding the class values to the address of the
          array, and fetching the kerning value to which the new
          address points.</p><p>The header for the simple array has the following
          format:</p><div class="table"><a name="idm416419622128"></a><p class="title"><strong>Table 34.6. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>rowWidth</td><td>The width, in bytes, of a row in the
              table.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>leftClassTable</td><td>Offset from beginning of this subtable to
              left-hand class table.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>rightClassTable</td><td>Offset from beginning of this subtable to
              right-hand class table. </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>array</td><td>Offset from beginning of this subtable to the
              start of the kerning array. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each class table has the following header:</p><div class="table"><a name="idm416419613552"></a><p class="title"><strong>Table 34.7. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>firstGlyph</td><td>First glyph in class range.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>nGlyphs</td><td>Number of glyph in class range.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This header is followed by nGlyphs number of class
          values, which are in USHORT format. Entries for glyphs that
          don't participate in kerning should point to the row or
          column at position zero.</p><p>The array itself is a left by right array of kerning
          values, which are FWords, where left is the number of
          left-hand classes and R is the number of right-hand classes.
          The array is stored by row.</p><p>Note that this format is the quickest to process since
          each lookup requires only a few index operations. The table
          can be quite large since it will contain the number of cells
          equal to the product of the number of right-hand classes and
          the number of left-hand classes, even though many of these
          classes do not kern with each other.</p></div></div></div>