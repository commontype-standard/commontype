<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.EBLC"></a>Chapter 28. EBLC - Embedded Bitmap Location Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383050256128"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.28.1.1"></a>Specification</h3></div></div></div><p role="">Three tables are used to embed bitmaps in OpenType
          fonts. They are the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table for embedded bitmap
          locators, the 'EBDT' table for embedded bitmap data, and the
          <a role="" class="link" href="chapter.EBSC.html" title="Chapter 29. EBSC - Embedded Bitmap Scaling Table">EBSC</a> table for embedded bitmap scaling information.
          OpenType embedded bitmaps are called 'sbits' (for "scaler
          bitmaps"). A set of bitmaps for a face at a given size is
          called a strike.</p><p role="">The <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table identifies the sizes and glyph ranges
          of the sbits, and keeps offsets to glyph bitmap data in
          indexSubTables. The 'EBDT' table then stores the glyph
          bitmap data, also in a number of different possible formats.
          Glyph metrics information may be stored in either the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a>
          or 'EBDT' table, depending upon the indexSubTable and glyph
          bitmap formats. The <a role="" class="link" href="chapter.EBSC.html" title="Chapter 29. EBSC - Embedded Bitmap Scaling Table">EBSC</a> table identifies sizes that will
          be handled by scaling up or scaling down other sbit
          sizes.</p><p role="">The <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table uses the same format as Apple's AAT
          (Apple Advanced Typography) 'bloc' table.</p><p role="">The <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table begins with a header containing the
          table version and number of strikes. An OpenType font may
          have one or more strikes embedded in the 'EBDT'
          table.</p><div class="table"><a name="idm383050247088"></a><p class="title"><strong>Table 28.1. eblcHeader</strong></p><div class="table-contents"><table role="" class="table" summary="eblcHeader" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">FIXED</td><td role="">version</td><td role="">initially defined as 0x00020000</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numSizes</td><td role="">Number of bitmapSizeTables</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The eblcHeader is followed immediately by the
          bitmapSizeTable array(s). The numSizes in the eblcHeader
          indicates the number of bitmapSizeTables in the array. Each
          strike is defined by one bitmapSizeTable.</p><div class="table"><a name="idm383050241200"></a><p class="title"><strong>Table 28.2. bitmapSizeTable</strong></p><div class="table-contents"><table role="" class="table" summary="bitmapSizeTable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">indexSubTableArrayOffset</td><td role="">offset to index subtable from beginning of
              EBLC.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">indexTablesSize</td><td role="">number of bytes in corresponding index
              subtables and array</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numberOfIndexSubTables</td><td role="">an index subtable for each range or format
              change</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">colorRef</td><td role="">not used; set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">sbitLineMetrics</td><td role="">hori</td><td role="">line metrics for text rendered
              horizontally</td><td class="auto-generated"> </td></tr><tr><td role="">sbitLineMetrics</td><td role="">vert</td><td role="">line metrics for text rendered
              vertically</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">startGlyphIndex</td><td role="">lowest glyph index for this
              size</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">endGlyphIndex</td><td role="">highest glyph index for this
              size</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">ppemX</td><td role="">horizontal pixels per Em</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">ppemY</td><td role="">vertical pixels per Em</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">bitDepth</td><td role="">the Microsoft rasterizer v.1.7 or greater
              supports the following bitDepth values, as described
              below: 1, 2, 4, and 8.</td><td class="auto-generated"> </td></tr><tr><td role="">CHAR</td><td role="">flags</td><td role="">vertical or horizontal (see
              bitmapFlags)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The indexSubTableArrayOffset is the offset from the
          beginning of the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table to the indexSubTableArray.
          Each strike has one of these arrays to support various
          formats and discontiguous ranges of bitmaps. The
          indexTablesSize is the total number of bytes in the
          indexSubTableArray and the associated indexSubTables. The
          numberOfIndexSubTables is a count of the indexSubTables for
          this strike.</p><p role="">The horizontal and vertical line metrics contain the
          ascender, descender, linegap, and advance information for
          the strike. The line metrics format is described in the
          following table:</p><div class="table"><a name="idm383050218720"></a><p class="title"><strong>Table 28.3. sbitLineMetrics</strong></p><div class="table-contents"><table role="" class="table" summary="sbitLineMetrics" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th></tr></thead><tbody><tr><td role="">CHAR</td><td role="">ascender</td></tr><tr><td role="">CHAR</td><td role="">descender</td></tr><tr><td role="">BYTE</td><td role="">widthMax</td></tr><tr><td role="">CHAR</td><td role="">caretSlopeNumerator</td></tr><tr><td role="">CHAR</td><td role="">caretSlopeDenominator</td></tr><tr><td role="">CHAR</td><td role="">caretOffset</td></tr><tr><td role="">CHAR</td><td role="">minOriginSB</td></tr><tr><td role="">CHAR</td><td role="">minAdvanceSB</td></tr><tr><td role="">CHAR</td><td role="">maxBeforeBL</td></tr><tr><td role="">CHAR</td><td role="">minAfterBL</td></tr><tr><td role="">CHAR</td><td role="">pad1</td></tr><tr><td role="">CHAR</td><td role="">pad2</td></tr></tbody></table></div></div><br class="table-break"/><p role="">The caret slope determines the angle at which the caret
          is drawn, and the offset is the number of pixels (+ or -) to
          move the caret. This is a signed char since we are dealing
          with integer metrics. The minOriginSB, minAdvanceSB ,
          maxBeforeBL, and minAfterBL are described in the diagrams
          below. The main need for these numbers is for scalers that
          may need to pre-allocate memory and/or need more metric
          information to position glyphs. All of the line metrics are
          one byte in length. The line metrics are not used directly
          by the rasterizer, but are available to clients who want to
          parse the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table.</p><p role="">The startGlyphIndex and endGlyphIndex describe the
          minimum and maximum glyph codes in the strike, but a strike
          does not necessarily contain bitmaps for all glyph codes in
          this range. The indexSubTables determine which glyphs are
          actually present in the 'EBDT' table.</p><p role="">The ppemX and ppemY fields describe the size of the
          strike in pixels per Em. The ppem measurement is equivalent
          to point size on a 72 dots per inch device. Typically, ppemX
          will be equal to ppemY for devices with 'square pixels'. To
          accommodate devices with rectangular pixels, and to allow
          for bitmaps with other aspect ratios, ppemX and ppemY may
          differ.</p><p role="">The bitDepth field is used to specify the number of
          levels of gray used in the embedded bitmaps. The Microsoft
          rasterizer v.1.7 or greater support the following
          values.</p><div class="table"><a name="idm383050196944"></a><p class="title"><strong>Table 28.4. bitDepth</strong></p><div class="table-contents"><table role="" class="table" summary="bitDepth" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th></tr></thead><tbody><tr><td role="">1</td><td role="">black/white</td></tr><tr><td role="">2</td><td role="">4 levels of gray</td></tr><tr><td role="">4</td><td role="">16 levels of gray</td></tr><tr><td role="">8</td><td role="">256 levels of gray</td></tr></tbody></table></div></div><br class="table-break"/><p role="">The 'flags' byte contains two bits to indicate the
          direction of small glyph metrics: horizontal or vertical.
          The remaining bits are reserved.</p><div class="table"><a name="idm383050187424"></a><p class="title"><strong>Table 28.5. Bitmap Flags</strong></p><div class="table-contents"><table role="" class="table" summary="Bitmap Flags" border="1"><colgroup><col width="3cm"/><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th></tr></thead><tbody><tr><td role="">CHAR</td><td role="">0x01</td><td role="">Horizontal</td></tr><tr><td role="">CHAR</td><td role="">0x02</td><td role="">Vertical</td></tr></tbody></table></div></div><br class="table-break"/><p role="">The colorRef and bitDepth fields are reserved for future
          enhancements. For monochrome bitmaps they should have the
          values colorRef=0 and bitDepth=1.</p><div class="figure"><a name="idm383050178528"></a><p class="title"><strong>Figure 28.1. Horizontal text</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/img00283.gif" alt="Horizontal text"/></div></div></div><br class="figure-break"/><div class="figure"><a name="idm383050176464"></a><p class="title"><strong>Figure 28.2. Vertical text</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/img00284.gif" alt="Vertical text"/></div></div></div><br class="figure-break"/><p role="">Associated with the image data for every glyph in a
          strike is a set of glyph metrics. These glyph metrics
          describe bounding box height and width, as well as side
          bearing and advance width information. The glyph metrics can
          be found in one of two places. For ranges of glyphs (not
          necessarily the whole strike) whose metrics may be different
          for each glyph, the glyph metrics are stored along with the
          glyph image data in the 'EBDT' table. Details of how this is
          done is described in the 'EBDT' section of this document.
          For ranges of glyphs whose metrics are identical for every
          glyph, we save significant space by storing a single copy of
          the glyph metrics in the indexSubTable in the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a>.</p><p role="">There are also two different formats for glyph metrics:
          big glyph metrics and small glyph metrics. Big glyph metrics
          define metrics information for both horizontal and vertical
          layouts. This is important in fonts (such as Kanji) where
          both types of layout may be used. Small glyph metrics define
          metrics information for one layout direction only. Which
          direction applies, horizontal or vertical, is determined by
          the 'flags' field in the bitmapSizeTable.</p><div class="table"><a name="idm383050172384"></a><p class="title"><strong>Table 28.6. bigGlyphMetrics</strong></p><div class="table-contents"><table role="" class="table" summary="bigGlyphMetrics" border="1"><colgroup><col width="3cm"/><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Offset</th><th role="">Type</th><th role="">Name</th></tr></thead><tbody><tr><td role="">0</td><td role="">BYTE</td><td role="">height</td></tr><tr><td role="">1</td><td role="">BYTE</td><td role="">width</td></tr><tr><td role="">2</td><td role="">CHAR</td><td role="">horiBearingX</td></tr><tr><td role="">3</td><td role="">CHAR</td><td role="">horiBearingY</td></tr><tr><td role="">4</td><td role="">BYTE</td><td role="">horiAdvance</td></tr><tr><td role="">5</td><td role="">CHAR</td><td role="">vertBearingX</td></tr><tr><td role="">6</td><td role="">CHAR</td><td role="">vertBearingY</td></tr><tr><td role="">7</td><td role="">BYTE</td><td role="">vertAdvance</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383050154736"></a><p class="title"><strong>Table 28.7. smallGlyphMetrics</strong></p><div class="table-contents"><table role="" class="table" summary="smallGlyphMetrics" border="1"><colgroup><col width="3cm"/><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Offset</th><th role="">Type</th><th role="">Name</th></tr></thead><tbody><tr><td role="">0</td><td role="">BYTE</td><td role="">height</td></tr><tr><td role="">1</td><td role="">BYTE</td><td role="">width</td></tr><tr><td role="">2</td><td role="">CHAR</td><td role="">BearingX</td></tr><tr><td role="">3</td><td role="">CHAR</td><td role="">BearingY</td></tr><tr><td role="">4</td><td role="">BYTE</td><td role="">Advance</td></tr></tbody></table></div></div><br class="table-break"/><p role="">The following diagram illustrates the meaning of the
          glyph metrics.</p><div class="informalfigure"><div role="" class="mediaobject"><img src="src/images/img00285.gif"/></div></div><p role="">The bitmapSizeTable for each strike contains the offset
          to an array of indexSubTableArray elements. Each element
          describes a glyph code range and an offset to the
          indexSubTable for that range. This allows a strike to
          contain multiple glyph code ranges and to be represented in
          multiple index formats if desirable.</p><div class="table"><a name="idm383050138784"></a><p class="title"><strong>Table 28.8. indexSubTableArray</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTableArray" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">firstGlyphIndex</td><td role="">first glyph code of this range</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">lastGlyphIndex</td><td role="">last glyph code of this range
              (inclusive)</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">additionalOffsetToIndexSubtable</td><td role="">add to indexSubTableArrayOffset to get offset
              from beginning of <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a></td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">After determining the strike, the rasterizer searches
          this array for the range containing the given glyph code.
          When the range is found, the additionalOffsetToIndexSubtable
          is added to the indexSubTableArrayOffset to get the offset
          of the indexSubTable in the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a>.</p><p role="">The first indexSubTableArray is located after the last
          bitmapSizeSubTable entry. Then the indexSubTables for the
          strike follow. Another indexSubTableArray (if more than one
          strike) and its indexSubTables are next. The <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a>
          continues with an array and indexSubTables for each
          strike.</p><p role="">We now have the offset to the indexSubTable. All
          indexSubTable formats begin with an indexSubHeader which
          identifies the indexSubTable format, the format of the
          'EBDT' image data, and the offset from the beginning of the
          'EBDT' table to the beginning of the image data for this
          range.</p><div class="table"><a name="idm383050128000"></a><p class="title"><strong>Table 28.9. indexSubHeader</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubHeader" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">indexFormat</td><td role="">format of this indexSubTable</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">imageFormat</td><td role="">format of 'EBDT' image data</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">imageDataOffset</td><td role="">offset to image data in 'EBDT'
              table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">There are currently five different formats used for the
          indexSubTable, depending upon the size and type of bitmap
          data in the glyph code range. Apple 'bloc' tables support
          only formats 1 through 3.</p><p role="">The choice of which indexSubTable format to use is up to
          the font manufacturer, but should be made with the aim of
          minimizing the size of the font file. Ranges of glyphs with
          variable metrics - that is, where glyphs may differ from
          each other in bounding box height, width, side bearings or
          advance - must use format 1, 3 or 4. Ranges of glyphs with
          constant metrics can save space by using format 2 or 5,
          which keep a single copy of the metrics information in the
          indexSubTable rather than a copy per glyph in the 'EBDT'
          table. In some monospaced fonts it makes sense to store
          extra white space around some of the glyphs to keep all
          metrics identical, thus permitting the use of format 2 or
          5.</p><p role="">Structures for each indexSubTable format are listed
          below.</p><div class="table"><a name="idm383050119728"></a><p class="title"><strong>Table 28.10. indexSubTable1: variable metrics glyphs with 4 byte
            offsets</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTable1: variable metrics glyphs with 4 byte&#10;            offsets" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">indexSubHeader</td><td role="">header</td><td role="">header info</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">offsetArray []</td><td role="">offsetArray[glyphIndex] + imageDataOffset =
              glyphData sizeOfArray = (lastGlyph-firstGlyph+1)+1+1 pad
              if needed </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383050114336"></a><p class="title"><strong>Table 28.11. indexSubTable2: all glyphs have identical
            metrics</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTable2: all glyphs have identical&#10;            metrics" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">indexSubHeader</td><td role="">header</td><td role="">header info</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">imageSize</td><td role="">all the glyphs are of the same
              size</td><td class="auto-generated"> </td></tr><tr><td role="">bigGlyphMetrics</td><td role="">bigMetrics</td><td role="">all glyphs have the same metrics; glyph data
              may be compressed, byte-aligned, or
              bit-aligned</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383050107440"></a><p class="title"><strong>Table 28.12. indexSubTable3: variable metrics glyphs with 2 byte
            offsets</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTable3: variable metrics glyphs with 2 byte&#10;            offsets" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">indexSubHeader</td><td role="">header</td><td role="">header info</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">offsetArray []</td><td role="">offsetArray[glyphIndex] + imageDataOffset =
              glyphData sizeOfArray = (lastGlyph-firstGlyph+1)+1+1 pad
              if needed  </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383050102016"></a><p class="title"><strong>Table 28.13. indexSubTable4: variable metrics glyphs with sparse
            glyph codes</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTable4: variable metrics glyphs with sparse&#10;            glyph codes" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">indexSubHeader</td><td role="">header</td><td role="">header info</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numGlyphs</td><td role="">array length</td><td class="auto-generated"> </td></tr><tr><td role="">codeOffsetPair</td><td role="">glyphArray []</td><td role="">one per glyph;
              sizeOfArray=numGlyphs+1</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">codeOffsetPair: used by indexSubTable4</p><div class="table"><a name="idm383050094784"></a><p class="title"><strong>Table 28.14. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">glyphCode</td><td role="">code of glyph present</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">offset</td><td role="">location in EBDT</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383050089792"></a><p class="title"><strong>Table 28.15. indexSubTable5: constant metrics glyphs with sparse
            glyph codes</strong></p><div class="table-contents"><table role="" class="table" summary="indexSubTable5: constant metrics glyphs with sparse&#10;            glyph codes" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">indexSubHeader</td><td role="">header</td><td role="">header info</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">imageSize</td><td role="">all glyphs have the same data
              size</td><td class="auto-generated"> </td></tr><tr><td role="">bigGlyphMetrics</td><td role="">bigMetrics</td><td role="">all glyphs have the same
              metrics</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numGlyphs</td><td role="">array length</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphCodeArray []</td><td role="">one per glyph, sorted by glyph code;
              sizeOfArray=numGlyphs</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The size of the 'EBDT' image data can be calculated from
          the indexSubTable information. For the constant metrics
          formats (2 and 5) the image data size is constant, and is
          given in the imageSize field. For the variable metrics
          formats (1, 3, and 4) image data must be stored contiguously
          and in glyph code order, so the image data size may be
          calculated by subtracting the offset for the current glyph
          from the offset of the next glyph. Because of this, it is
          necessary to store one extra element in the offsetArray
          pointing just past the end of the range's image data. This
          will allow the correct calculation of the image data size
          for the last glyph in the range.</p><p role="">Contiguous, or nearly contiguous, ranges of glyph codes
          are handled best by formats 1, 2, and 3 which store an
          offset for every glyph code in the range. Very sparse ranges
          of glyph codes should use format 4 or 5 which explicitly
          call out the glyph codes represented in the range. A small
          number of missing glyphs can be efficiently represented in
          formats 1 or 3 by having the offset for the missing glyph be
          followed by the same offset for the next glyph, thus
          indicating a data size of zero.</p><p role="">The only difference between formats 1 and 3 is the size
          of the offsetArray elements: format 1 uses ULONG's while
          format 3 uses USHORT's. Therefore format 1 can cover a
          greater range (&gt; 64k bytes) while format 3 saves more space
          in the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table. Since the offsetArray elements are
          added to the imageDataOffset base address in the
          indexSubHeader, a very large set of glyph bitmap data could
          be addressed by splitting it into multiple ranges, each less
          than 64k bytes in size, allowing the use of the more
          efficient format 3.</p><p role="">The <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table specification requires double word
          (ULONG) alignment for all subtables. This occurs naturally
          for indexSubTable formats 1, 2, and 4, but may not for
          formats 3 and 5, since they include arrays of type USHORT.
          When there is an odd number of elements in these arrays it
          is necessary to add an extra padding element to maintain
          proper alignment.</p></div></div></div>