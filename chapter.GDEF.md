<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.GDEF"></a>Chapter 22. GDEF - The Glyph Definition Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763773920"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.1.1"></a>Specification</h4></div></div></div><p>The Glyph Definition (<a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>) table
          contains three types of information in three independent
          tables:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The <span class="emphasis"><em>GlyphClassDef</em></span> table
              classifies the different types of glyphs in the
              font.</p></li><li class="listitem"><p>The <span class="emphasis"><em>AttachmentList</em></span> table
              identifies all attachment points on the glyphs, which
              streamlines data access and bitmap caching.</p></li><li class="listitem"><p>The <span class="emphasis"><em>LigatureCaretList</em></span> table
              contains positioning data for ligature carets, which the
              text-processing client uses on screen to select and
              highlight the individual components of a ligature
              glyph.</p></li><li class="listitem"><p>The <span class="emphasis"><em>MarkAttachClassDef</em></span> table
              classifies mark glyphs, to help group together marks
              that are positioned similarly.</p></li></ul></div><p>Both the <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> tables reference the
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> table information to supplement
          their own data for substituting and positioning glyphs. Even
          so, a <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> table is optional for a font,
          included at the discretion of the font developer. Without a
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> table, however, the text-processing
          client may have to define and maintain the
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> information on its own when
          substituting and positioning glyphs.</p><p>A client may use any one or more of the three
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> tables during text processing. This
          overview explains how each of the three tables are organized
          and used (See Figure 7a). The rest of this chapter describes
          the individual <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> tables and the tables
          that they reference.</p><div class="figure"><a name="idm363763584112"></a><p class="title"><strong>Figure 22.1. Figure 7a. High-level organization of <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>
          table</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig7a.gif" alt="Figure 7a. High-level organization of GDEF table"/></div></div></div><br class="figure-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.1.2"></a>Annotation</h4></div></div></div><p>First sentence, both occurrences of 'three' should be
	  replaced by 'four'.</p><p>Last two sentences of paragraph after the bullet list: I
          am not sure that this comment applies to GlyphClassDef for
          example. There does not seem to be any mandatory data in
          <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> or <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> that
          would indicate the class of a glyph. Suppose that there is
          only a <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> table, no
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> and no <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>; that
          <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> contains only one SingleSubstitution
          lookup with LookupFlag set to ignoreBaseGlyphs. What glyphs
          should be ignored by this lookup? Or is this font
          illegal?</p><p>Last paragraph: both occurrences of 'three' should be
	  replaced by 'four'.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763574400"></a>Glyph Class Definition Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.2.1"></a>Specification</h4></div></div></div><p>The Glyph Class Definition (GlyphClassDef) table
          identifies four types of glyphs in a font: base glyphs,
          ligature glyphs, combining mark glyphs, and glyph components
          (see Figure 7b). <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> lookups define and use these glyph
          classes to differentiate the types of glyphs in a string.
          For example, <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> uses the glyph classes
          to distinguish between a simple base glyph and the mark
          glyph that follows it.</p><div class="figure"><a name="idm363763569968"></a><p class="title"><strong>Figure 22.2. Figure 7b. A base glyph, ligature glyph, mark
            glyph, and glyph components</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig7b.gif" alt="Figure 7b. A base glyph, ligature glyph, mark glyph, and glyph components"/></div></div></div><br class="figure-break"/><p>In addition, a client uses class definitions to apply
          <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> and <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a>
          LookupFlag data correctly. For example, a LookupFlag may
          specify ignoring ligatures and marks during a glyph
          operation. If the font does not include a GlyphClassDef
          table, the client must define and maintain this information
          when using the <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> tables.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.2.2"></a>Annotation</h4></div></div></div><p>First sentence: shouldn’t “glyph
        components” be replaced by “component
        glyphs”? Similarly in the figure’s title.</p><p>Last sentence: How can the client figure out the class
        of a glyph from a font lacking a GlyphClassDef table?</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763561744"></a>Attachment Point List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.3.1"></a>Specification</h4></div></div></div><p>The Attachment Point List table (AttachmentList)
          identifies all the attachment points defined in the
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> table and their associated glyphs so
          a client can quickly access coordinates for each glyph's
          attachment points. As a result, the client can cache
          coordinates for attachment points along with glyph bitmaps
          and avoid recalculating the attachment points each time it
          displays a glyph. Without this table, processing speed would
          be slower because the client would have to decode the
          <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> lookups that define attachment
          points and compile the points in a list.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763557168"></a>Ligature Caret List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.4.1"></a>Specification</h4></div></div></div><p>The Ligature Caret List table (LigatureCaretList),
          particularly useful in Arabic and other scripts with many
          ligatures, specifies coordinates for positioning carets on
          all ligatures in a font. The client uses this data to select
          and highlight ligature components in displayed text (see
          Figure 7c).</p><div class="figure"><a name="idm363763554688"></a><p class="title"><strong>Figure 22.3. Figure 7c. Proper ligature caret postioning</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig7c.gif" alt="Figure 7c. Proper ligature caret postioning"/></div></div></div><br class="figure-break"/><p>Each ligature can have more than one caret position,
          with each position defined as an X or Y value on the
          baseline according to the writing direction of the script or
          language system. The font developer can use any of three
          formats to represent a caret coordinate value. One format
          represents values in design units only, another fine-tunes a
          value based on a designated contour point, and the third
          uses a Device table to adjust values at specific font
          sizes.</p><p>Without a Ligature Caret List table, the client would
          have to define caret positions without knowing the positions
          of the ligature components. The resulting highlighting or
          hit-testing might be ambiguous. For example, suppose a
          client places a caret at the midpoint position along the
          width of a hyphothetical "wi" ligature. Because the "w" is
          wider than the "i," that position would not clearly indicate
          which component is selected. Instead, for accurate
          selection, the caret should be moved to the right so that
          either the "w" or "i" could be clearly highlighted.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763550112"></a>GDEF Header</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.5.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> table begins with a header
          that consists of a version number (Version), initially set
          to 0x00010000, an offset to a table defining the types of
          glyphs in the font (GlyphClassDef), an offset to a list
          defining attachment points on the glyphs(AttachList), an
          offset to a ligature caret list (LigCaretList) and an offset
          to a list defining types of marks that can be attached
          (MarkAttachClassDef). The format used for the
          MarkAttachClassDef is the same as that for GlyphClassDef.
          Please refer the 'LookupFlag bit enumeration' section in the
          Common Table Formats for more on using lookup flags with the
          information in these fields.</p><p>Example 1 at the end of this chapter shows a
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> Header table.</p><div class="table"><a name="idm363763545568"></a><p class="title"><strong>Table 22.1. GDEF Header</strong></p><div class="table-contents"><table class="table" summary="GDEF Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Fixed</td><td>Version</td><td>Version of the <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>
              table-initially 0x00010000</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>GlyphClassDef</td><td>Offset to class definition table for glyph
              type-from beginning of <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> header
              (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>AttachList</td><td>Offset to list of glyphs with attachment
              points-from beginning of <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> header
              (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LigCaretList</td><td>Offset to list of positioning points for
              ligature carets-from beginning of
              <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> header (may be
              NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkAttachClassDef</td><td>Offset to class definition table for mark
              attachment type-from beginning of
              <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> header (may  be
              NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763532048"></a>Glyph Class Definition Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.6.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> and <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a>
          tables use the Glyph Class Definition table (GlyphClassDef)
          to identify which glyph classes to adjust with
          lookups.</p><p>The table uses the same format as the Class Definition
          table (for details, see the chapter, Common Table
          Formats). However, the GlyphClassDef table uses class values
          already defined in the GlyphClassDef Enumeration
          list:</p><div class="table"><a name="idm363763527888"></a><p class="title"><strong>Table 22.2. GlyphClassDef Enumeration List</strong></p><div class="table-contents"><table class="table" summary="GlyphClassDef Enumeration List" border="1"><colgroup><col width="6pc"/><col width="24pc"/></colgroup><thead><tr><th>Class</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Base glyph (single character, spacing glyph)</td></tr><tr><td>2</td><td>Ligature glyph (multiple character, spacing
                  glyph)</td></tr><tr><td>3</td><td>Mark glyph (non-spacing combining glyph)</td></tr><tr><td>4</td><td>Component glyph (part of single character,
                  spacing glyph)</td></tr></tbody></table></div></div><br class="table-break"/><p>The font developer does not have to classify every glyph
        in the font, but any glyph not assigned a class value falls
        into Class zero (0). For instance, class values might be
        useful for the Arabic glyphs in a font, but not for the Latin
        glyphs. Then the GlyphClassDef table will list only Arabic
        glyphs, and-by default-the Latin glyphs will be assigned to
        Class 0. Component glyphs can be put together to generate
        ligatures. A ligature can be generated by creating a glyph in
        the font that references the component glyphs, or outputting
        the component glyphs in the desired sequence.  Component
        glyphs are not used in defining any <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a> or
        <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> formats.</p><p>Example 2 at the end of this chapter defines a
          GlyphClassDef table with a sample glyph for each of the
          assigned classes.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763515376"></a>Attachment List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.7.1"></a>Specification</h4></div></div></div><p>The Attachment List table (AttachList) may be used to
          cache attachment point coordinates along with glyph
          bitmaps.</p><p>The table consists of an offset to a Coverage table
        (Coverage) listing all glyphs that define attachment points in
        the <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a> table, a count of the glyphs with
        attachment points (GlyphCount), and an array of offsets to
        AttachPoint tables (AttachPoint). The array lists the
        AttachPoint tables, one for each glyph in the Coverage table,
        in the same order as the Coverage Index.</p><div class="table"><a name="idm363763511680"></a><p class="title"><strong>Table 22.3. AttachList table</strong></p><div class="table-contents"><table class="table" summary="AttachList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table - from beginning of
              AttachList table</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GlyphCount</td><td>Number of glyphs with attachment
              points</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>AttachPoint [GlyphCount]</td><td>Array of offsets to AttachPoint tables-from
              beginning of AttachList table-in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>An AttachPoint table consists of a count of the
          attachment points on a single glyph (PointCount) and an
          array of contour indices of those points (PointIndex),
          listed in increasing numerical order.</p><p>Example 3 at the end of the chapter demonstrates an
          AttachList table that defines attachment points for two
          glyphs.</p><div class="table"><a name="idm363763503792"></a><p class="title"><strong>Table 22.4. AttachPoint table</strong></p><div class="table-contents"><table class="table" summary="AttachPoint table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PointCount</td><td>Number of attachment points on this
              glyph</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PointIndex [PointCount]</td><td>Array of contour point indices -in increasing
              numerical order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763498048"></a>Ligature Caret List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.8.1"></a>Specification</h4></div></div></div><p>The Ligature Caret List table (LigCaretList) defines
          caret positions for all the ligatures in a font. The table
          consists of an offset to a Coverage table that lists all the
          ligature glyphs (Coverage), a count of the defined ligatures
          (LigGlyphCount), and an array of offsets to LigGlyph tables
          (LigGlyph). The array lists the LigGlyph tables, one for
          each ligature in the Coverage table, in the same order as
          the Coverage Index.</p><p>Example 4 at the end of this chapter shows a
          LigCaretList table.</p><div class="table"><a name="idm363763494944"></a><p class="title"><strong>Table 22.5. LigCaretList table</strong></p><div class="table-contents"><table class="table" summary="LigCaretList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table - from beginning of
              LigCaretList table</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LigGlyphCount</td><td>Number of ligature glyphs</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LigGlyph [LigGlyphCount]</td><td>Array of offsets to LigGlyph tables-from
              beginning of LigCaretList table-in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763487728"></a>Ligature Glyph Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.9.1"></a>Specification</h4></div></div></div><p>A Ligature Glyph table (LigGlyph) contains the caret
          coordinates for a single ligature glyph. The number of
          coordinate values, each defined in a separate CaretValue
          table, equals the number of components in the ligature minus
          one (1).</p><p>The LigGlyph table consists of a count of the number of
          CaretValue tables defined for the ligature (CaretCount) and
          an array of offsets to CaretValue tables
          (CaretValue).</p><p>Example 4 at the end of the chapter shows a LigGlyph
          table.</p><div class="table"><a name="idm363763484256"></a><p class="title"><strong>Table 22.6. LigGlyph table</strong></p><div class="table-contents"><table class="table" summary="LigGlyph table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CaretCount</td><td>Number of CaretValues for this ligature
              (components - 1)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>CaretValue [CaretCount]</td><td>Array of offsets to CaretValue tables-from
              beginning of LigGlyph table-in increasing coordinate
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763478432"></a>Caret Values Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.10.1"></a>Specification</h4></div></div></div><p>A Caret Values table (CaretValues), which defines caret
          positions for a ligature, can be any of three possible
          formats. One format uses design units to define the caret
          position. The other two formats use a contour point or
          Device table to fine-tune a caret's position at specific
          font sizes and device resolutions. Caret coordinates are
          either X or Y values, depending upon the text
          direction.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763475280"></a>CaretValue Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.11.1"></a>Specification</h4></div></div></div><p>The first format (CaretValueFormat1) consists of a
          format identifier (CaretValueFormat), followed by a single
          coordinate for the caret position (Coordinate). The
          Coordinate is in design units.</p><p>This format has the benefits of small size and
          simplicity, but the Coordinate value cannot be hinted for
          fine adjustments at different device resolutions.</p><p>Exampel 4 at the end of this chapter shows a
          CaretValueFormat1 table.</p><div class="table"><a name="idm363763471904"></a><p class="title"><strong>Table 22.7. CaretValueFormat1 table: Design units only</strong></p><div class="table-contents"><table class="table" summary="CaretValueFormat1 table: Design units only" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CaretValueFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>Coordinate</td><td>X or Y value, in design units</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763466256"></a>CaretValue Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.12.1"></a>Specification</h4></div></div></div><p>The second format (CaretValueFormat2) specifies the
          caret coordinate in terms of a contour point index on a
          specific glyph. During font hinting, the contour point on
          the glyph outline may move. The point's final position after
          hinting provides the final value for rendering a given font
          size.</p><p>The table contains a format identifier
          (CaretValueFormat) and a contour point index
          (CaretValuePoint).</p><p>Example 5 at the end of this chapter demonstrates a
          CaretValueFormat2 table.</p><div class="table"><a name="idm363763462784"></a><p class="title"><strong>Table 22.8. CaretValueFormat2 table: Contour point</strong></p><div class="table-contents"><table class="table" summary="CaretValueFormat2 table: Contour point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CaretValueFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>CaretValuePoint</td><td>Contour point index on glyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763457136"></a>CaretValue Format 3</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.13.1"></a>Specification</h4></div></div></div><p>The third format (CaretValueFormat3) also specifies the
          value in design units, but it uses a Device table rather
          than a contour point to adjust the value. This format offers
          the advantage of fine-tuning the Coordinate value for any
          device resolution. (For more information about Device
          tables, see the chapter, Common Table Formats.)</p><p>The format consists of a format identifier
          (CaretValueFormat), an X or Y value (Coordinate), and an
          offset to a Device table (DeviceTable).</p><p>Example 6 at the end of this chapter shows a
          CaretValueFormat3 table.</p><div class="table"><a name="idm363763453616"></a><p class="title"><strong>Table 22.9. CaretValueFormat3 table: Design units plus Device table</strong></p><div class="table-contents"><table class="table" summary="CaretValueFormat3 table: Design units plus Device table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CaretValueFormat</td><td>Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>Coordinate</td><td>X or Y value, in design units</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>DeviceTable</td><td>Offset to Device table for X or Y value-from
              beginning of CaretValue table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763446448"></a>Mark Attachment Class Definition Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.14.1"></a>Specification</h4></div></div></div><p>A Mark Attachment Class Definition Table defines the
          class to which a mark glyph may belong. This table uses the
          same format as the Class Definition table (for details, see
          the chapter, Common Table Formats ).</p><p>Example 7 in this document shows a MarkAttachClassDef
        table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763443024"></a>GDEF Table Examples</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.15.1"></a>Specification</h4></div></div></div><p>The rest of this chapter describes examples of all the
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> table formats. All the examples reflect unique
          parameters described below, but the samples provide a useful
          reference for building tables specific to other
          situations.</p><p>The examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763438976"></a>Example 1: GDEF Header</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.16.1"></a>Specification</h4></div></div></div><p>Example 1 shows a <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a> Header
          definition with offsets to each of the main tables in
          <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>.</p><div class="table"><a name="idm363763435536"></a><p class="title"><strong>Table 22.10. Example 1</strong></p><div class="table-contents"><table class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>GDEFHeader</td><td> </td></tr><tr><td> </td><td>TheGDEFHeader</td><td>GDEFHeader table
                  definition</td></tr><tr><td>00010000</td><td>0x00010000</td><td>Version</td></tr><tr><td>000A</td><td>GlyphClassDefTable</td><td>offset to GlyphClassDef table</td></tr><tr><td>0026</td><td>AttachListTable</td><td>offset to AttachList table</td></tr><tr><td>0040</td><td>LigCaretListTable</td><td>offset to LigCaretList table</td></tr><tr><td>005A</td><td>MarkAttachClassDefTable</td><td>offset to Mark Attachment Class Definition
                  Table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763423152"></a>Example 2: GlyphClassDef Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.17.1"></a>Specification</h4></div></div></div><p>The GlyphClassDef table in Example 2 specifies a glyph
          for the each of the glyph classes predefined in the
          GlyphClassDef Enumeration List.</p><div class="table"><a name="idm363763420864"></a><p class="title"><strong>Table 22.11. Example 2</strong></p><div class="table-contents"><table class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>GlyphClassDefTable</td><td>ClassDef table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>ClassFormat</td></tr><tr><td>0004</td><td>4</td><td>ClassRangeCount ClassRangeRecord[0</td></tr><tr><td>0024</td><td>iGlyphID</td><td>Start</td></tr><tr><td>0024</td><td>iGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Class, 1 = base glyphs
                  ClassRangeRecord[1]</td></tr><tr><td>009F</td><td>ffiLigGlyphID</td><td>Start</td></tr><tr><td>009F</td><td>ffiLigGlyphID</td><td>End</td></tr><tr><td>0002</td><td>2</td><td>Class, 2 = ligature glyphs
                  ClassRangeRecord[2]</td></tr><tr><td>0058</td><td>umlautAccentGlyphID</td><td>Start</td></tr><tr><td>0058</td><td>umlautAccentGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class, 3 = mark glyphs
                  ClassRangeRecord[3]</td></tr><tr><td>018F</td><td>CurvedTailComponentGlyphID</td><td>Start</td></tr><tr><td>018F</td><td>CurvedTailComponentGlyphID</td><td>End</td></tr><tr><td>0004</td><td>4</td><td>Class, 4 = component glyphs</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763395632"></a>Example 3: AttachList Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.18.1"></a>Specification</h4></div></div></div><p>In Example 3, the AttachList table enumerates the
          attachment points defined for two glyphs. The GlyphCoverage
          table identifies the glyphs: "a" and "e." For each covered
          glyph, an AttachPoint table specifies the attachment point
          count and point indices: one point for the "a" glyph and two
          for the "e" glyph.</p><div class="table"><a name="idm363763393136"></a><p class="title"><strong>Table 22.12. Example 3</strong></p><div class="table-contents"><table class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>AttachList</td><td> </td></tr><tr><td> </td><td>AttachListTable</td><td>AttachList table
                  definition</td></tr><tr><td>0012</td><td>GlyphCoverage</td><td>offset to Coverage table</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>0008</td><td>aAttachPoint</td><td>AttachPoint[0]</td></tr><tr><td>000C</td><td>eAttachPoint</td><td>AttachPoint[1</td></tr><tr><td> </td><td>AttachPoint</td><td> </td></tr><tr><td> </td><td>aAttachPoint</td><td>AttachPoint table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PointCount</td></tr><tr><td>0012</td><td>18</td><td>PointIndex[0</td></tr><tr><td> </td><td>AttachPoint</td><td> </td></tr><tr><td> </td><td>eAttachPoint</td><td>AttachPoint table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>PointCount</td></tr><tr><td>000E</td><td>14</td><td>PointIndex[0]</td></tr><tr><td>0017</td><td>23</td><td>PointIndex[1</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>GlyphCoverage</td><td>Coverage table definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>001C</td><td>aGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0020</td><td>eGlyphID</td><td>GlyphArray[1]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763362176"></a>Example 4: LigCaretList Table, LigGlyph Table and
        CaretValueFormat1 Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.19.1"></a>Specification</h4></div></div></div><p>Example 4 defines a list of ligature carets. The
          LigCoverage table lists all the ligature glyphs that define
          caret positions. In this example, two ligatures are covered,
          "ffi" and "fi." For each covered glyph, a LigGlyph table
          specifies the number of carets for the ligature and their
          coordinate values. The "fi" ligature defines one caret,
          positioned between the "f" and "i" components; the "ffi"
          ligature defines two, one positioned between the two "f"
          components and the other positioned between the "f" and "i."
          The CaretValue tables shown here use Format1, where values
          are specified in design units only.</p><div class="table"><a name="idm363763359232"></a><p class="title"><strong>Table 22.13. Example 1</strong></p><div class="table-contents"><table class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>LigCaretList</td><td> </td></tr><tr><td> </td><td>LigCaretListTable</td><td>LigCaretList table
                  definition</td></tr><tr><td>0008</td><td>LigCoverage</td><td>offset to Coverage table</td></tr><tr><td>0002</td><td>2</td><td>LigGlyphCount</td></tr><tr><td>0010</td><td>fiLigGlyph</td><td>offset to LigGlyph table[0]</td></tr><tr><td>0014</td><td>ffiLigGlyph</td><td>offset to LigGlyph table[1</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>LigCoverage</td><td>Coverage table definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>009F</td><td>ffiLigGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>00A5</td><td>fiLigGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>LigGlyph</td><td> </td></tr><tr><td> </td><td>fiLigGlyph</td><td>LigGlyph table definition</td></tr><tr><td>0001</td><td>1</td><td>CaretCount, equals the number of components -
                  1</td></tr><tr><td>000E</td><td>CaretFI</td><td>CaretValue[0</td></tr><tr><td> </td><td>LigGlyph</td><td> </td></tr><tr><td> </td><td>ffiLigGlyph</td><td>LigGlyph table definition</td></tr><tr><td>0002</td><td>2</td><td>CaretCount, equals the number of components -
                  1</td></tr><tr><td>0006</td><td>CaretFFI1</td><td>CaretValue[0]</td></tr><tr><td>000E</td><td>CaretFFI2</td><td>CaretValue[1</td></tr><tr><td> </td><td>CaretValueFormat1</td><td> </td></tr><tr><td> </td><td>CaretFI</td><td>CaretValue table definition</td></tr><tr><td>0001</td><td>1</td><td>CaretValueFormat design units only</td></tr><tr><td>025B</td><td>603</td><td>Coordinate X or Y valu</td></tr><tr><td> </td><td>CaretValueFormat1</td><td> </td></tr><tr><td> </td><td>CaretFFI1</td><td>CaretValue table definition</td></tr><tr><td>0001</td><td>1</td><td>CaretValueFormat design units only</td></tr><tr><td>025B</td><td>603</td><td>Coordinate X or Y valu</td></tr><tr><td> </td><td>CaretValueFormat1</td><td> </td></tr><tr><td> </td><td>CaretFFI2</td><td>CaretValue table definition</td></tr><tr><td>0001</td><td>1</td><td>CaretValueFormat design units only</td></tr><tr><td>04B6</td><td>1206</td><td>Coordinate X or Y value</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763312320"></a>Example 5: CaretValueFormat2 Table </h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.20.1"></a>Specification</h4></div></div></div><p>Example 5 shows a CaretValueFormat2 table that specifies
          a ligature caret coordinate in terms of a contour point
          index on a specific glyph. The final position of the caret
          depends on the location of the contour point on the glyph
          after hinting.</p><div class="table"><a name="idm363763309856"></a><p class="title"><strong>Table 22.14. Example 5</strong></p><div class="table-contents"><table class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>CaretValueFormat2</td><td> </td></tr><tr><td> </td><td>Caret1</td><td>CaretValue table definition</td></tr><tr><td>0002</td><td>2</td><td>CaretValueFormat contour point</td></tr><tr><td>000D</td><td>13</td><td>CaretValuePoint contour point index</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763301776"></a>Example 6: CaretValueFormat3 Table </h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.21.1"></a>Specification</h4></div></div></div><p>In Example 6, the CaretValueFormat3 table defines a
          caret position in design units, but includes a Device table
          to adjust the X or Y coordinate for the point size and
          resolution of the output font. Here, the Device table
          specifies pixel adjustments for font sizes from 12 ppem to
          17 ppem.</p><div class="table"><a name="idm363763299248"></a><p class="title"><strong>Table 22.15. Example 6</strong></p><div class="table-contents"><table class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>CaretValueFormat3</td><td> </td></tr><tr><td> </td><td>Caret3</td><td>CaretValue table definition</td></tr><tr><td>0003</td><td>3</td><td>CaretValueFormat design units plus Device
                  table</td></tr><tr><td>04B6</td><td>1206</td><td>Coordinate X or Y value, design units</td></tr><tr><td>0006</td><td>CaretDevice</td><td>offset to Device tabl</td></tr><tr><td> </td><td>DeviceTableFormat2</td><td> </td></tr><tr><td> </td><td>CaretDevice</td><td>Device Table definition</td></tr><tr><td>000C</td><td>12</td><td>StartSize</td></tr><tr><td>0011</td><td>17</td><td>EndSize</td></tr><tr><td>0002</td><td>2</td><td>DeltaFormat</td></tr><tr><td> </td><td>1</td><td>increase 12ppm by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppm by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppm by 1 pixel</td></tr><tr><td>1111</td><td>1</td><td>increase 15ppm by 1 pixel</td></tr><tr><td> </td><td>2</td><td>increase 16ppm by 2 pixel</td></tr><tr><td>2200</td><td>2</td><td>increase 17ppm by 2 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363763275088"></a>Example 7: MarkAttachClassDef Table </h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.23.22.1"></a>Specification</h4></div></div></div><p>In Example 7, the MarkAttachClassDef table specifies an
          attachment class for the each of the glyph ranges predefined
          in the GlyphClassDef Enumeration List as marks.</p><div class="table"><a name="idm363763272720"></a><p class="title"><strong>Table 22.16. Example 7</strong></p><div class="table-contents"><table class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>theMarkAttachClassDefTable</td><td>ClassDef table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>ClassFormat</td></tr><tr><td>0004</td><td>4</td><td>ClassRangeCount ClassRangeRecord[0] </td></tr><tr><td>0268</td><td>graveAccentGlyphID</td><td>Start </td></tr><tr><td>026A</td><td>circumflexAccentGlyphID</td><td>End </td></tr><tr><td>0001</td><td>1</td><td>Class, 1 = top marks ClassRangeRecord[1]
                </td></tr><tr><td>0270</td><td>diaeresisAccentGlyphID</td><td>Start </td></tr><tr><td>0272</td><td>acuteAccentGlyphID</td><td>End </td></tr><tr><td>0001</td><td>1</td><td>Class, 1 = top marks ClassRangeRecord[2]
                </td></tr><tr><td>028C</td><td>diaeresisBelowGlyphID</td><td>Start </td></tr><tr><td>028F</td><td>cedillaGlyphID</td><td>End </td></tr><tr><td>0002</td><td>2</td><td>Class, 2 = bottom marks ClassRangeRecord[3]
                </td></tr><tr><td>0295</td><td>circumflexBelowGlyphID</td><td>Start </td></tr><tr><td>0295</td><td>circumflexBelowGlyphID</td><td>End </td></tr><tr><td>0002</td><td>2</td><td>Class, 2 = bottom marks </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>