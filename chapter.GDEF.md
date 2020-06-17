<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.GDEF"></a>Chapter 23. GDEF - The Glyph Definition Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639381312"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.1.1"></a>Specification</h3></div></div></div><p role="">The Glyph Definition (<a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>) table
          contains three types of information in three independent
          tables:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The <span role="" class="emphasis"><em>GlyphClassDef</em></span> table
              classifies the different types of glyphs in the
              font.</p></li><li role="" class="listitem"><p role="">The <span role="" class="emphasis"><em>AttachmentList</em></span> table
              identifies all attachment points on the glyphs, which
              streamlines data access and bitmap caching.</p></li><li role="" class="listitem"><p role="">The <span role="" class="emphasis"><em>LigatureCaretList</em></span> table
              contains positioning data for ligature carets, which the
              text-processing client uses on screen to select and
              highlight the individual components of a ligature
              glyph.</p></li><li role="" class="listitem"><p role="">The <span role="" class="emphasis"><em>MarkAttachClassDef</em></span> table
              classifies mark glyphs, to help group together marks
              that are positioned similarly.</p></li></ul></div><p role="">Both the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables reference the
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table information to supplement
          their own data for substituting and positioning glyphs. Even
          so, a <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table is optional for a font,
          included at the discretion of the font developer. Without a
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table, however, the text-processing
          client may have to define and maintain the
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> information on its own when
          substituting and positioning glyphs.</p><p role="">A client may use any one or more of the three
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables during text processing. This
          overview explains how each of the three tables are organized
          and used (See Figure 7a). The rest of this chapter describes
          the individual <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables and the tables
          that they reference.</p><div class="figure"><a name="idm114639366528"></a><p class="title"><strong>Figure 23.1. Figure 7a. High-level organization of <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>
          table</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig7a.gif" alt="Figure 7a. High-level organization of GDEF table"/></div></div></div><br class="figure-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.1.2"></a>Annotation</h3></div></div></div><p role="">First sentence, both occurrences of 'three' should be
	  replaced by 'four'.</p><p role="">Last two sentences of paragraph after the bullet list: I
          am not sure that this comment applies to GlyphClassDef for
          example. There does not seem to be any mandatory data in
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> that
          would indicate the class of a glyph. Suppose that there is
          only a <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table, no
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> and no <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>; that
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> contains only one SingleSubstitution
          lookup with LookupFlag set to ignoreBaseGlyphs. What glyphs
          should be ignored by this lookup? Or is this font
          illegal?</p><p role="">Last paragraph: both occurrences of 'three' should be
	  replaced by 'four'.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639356672"></a>Glyph Class Definition Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.2.1"></a>Specification</h3></div></div></div><p role="">The Glyph Class Definition (GlyphClassDef) table
          identifies four types of glyphs in a font: base glyphs,
          ligature glyphs, combining mark glyphs, and glyph components
          (see Figure 7b). <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookups define and use these glyph
          classes to differentiate the types of glyphs in a string.
          For example, <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> uses the glyph classes
          to distinguish between a simple base glyph and the mark
          glyph that follows it.</p><div class="figure"><a name="idm114639352240"></a><p class="title"><strong>Figure 23.2. Figure 7b. A base glyph, ligature glyph, mark
            glyph, and glyph components</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig7b.gif" alt="Figure 7b. A base glyph, ligature glyph, mark glyph, and glyph components"/></div></div></div><br class="figure-break"/><p role="">In addition, a client uses class definitions to apply
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          LookupFlag data correctly. For example, a LookupFlag may
          specify ignoring ligatures and marks during a glyph
          operation. If the font does not include a GlyphClassDef
          table, the client must define and maintain this information
          when using the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.2.2"></a>Annotation</h3></div></div></div><p role="">First sentence: shouldn’t “glyph
        components” be replaced by “component
        glyphs”? Similarly in the figure’s title.</p><p role="">Last sentence: How can the client figure out the class
        of a glyph from a font lacking a GlyphClassDef table?</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639344016"></a>Attachment Point List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.3.1"></a>Specification</h3></div></div></div><p role="">The Attachment Point List table (AttachmentList)
          identifies all the attachment points defined in the
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table and their associated glyphs so
          a client can quickly access coordinates for each glyph's
          attachment points. As a result, the client can cache
          coordinates for attachment points along with glyph bitmaps
          and avoid recalculating the attachment points each time it
          displays a glyph. Without this table, processing speed would
          be slower because the client would have to decode the
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookups that define attachment
          points and compile the points in a list.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639339440"></a>Ligature Caret List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.4.1"></a>Specification</h3></div></div></div><p role="">The Ligature Caret List table (LigatureCaretList),
          particularly useful in Arabic and other scripts with many
          ligatures, specifies coordinates for positioning carets on
          all ligatures in a font. The client uses this data to select
          and highlight ligature components in displayed text (see
          Figure 7c).</p><div class="figure"><a name="idm114639336960"></a><p class="title"><strong>Figure 23.3. Figure 7c. Proper ligature caret postioning</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig7c.gif" alt="Figure 7c. Proper ligature caret postioning"/></div></div></div><br class="figure-break"/><p role="">Each ligature can have more than one caret position,
          with each position defined as an X or Y value on the
          baseline according to the writing direction of the script or
          language system. The font developer can use any of three
          formats to represent a caret coordinate value. One format
          represents values in design units only, another fine-tunes a
          value based on a designated contour point, and the third
          uses a Device table to adjust values at specific font
          sizes.</p><p role="">Without a Ligature Caret List table, the client would
          have to define caret positions without knowing the positions
          of the ligature components. The resulting highlighting or
          hit-testing might be ambiguous. For example, suppose a
          client places a caret at the midpoint position along the
          width of a hyphothetical "wi" ligature. Because the "w" is
          wider than the "i," that position would not clearly indicate
          which component is selected. Instead, for accurate
          selection, the caret should be moved to the right so that
          either the "w" or "i" could be clearly highlighted.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639332976"></a>GDEF Header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.5.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table begins with a header
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
          information in these fields.</p><p role="">Example 1 at the end of this chapter shows a
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> Header table.</p><div class="table"><a name="idm114639328480"></a><p class="title"><strong>Table 23.1. GDEF Header</strong></p><div class="table-contents"><table role="" class="table" summary="GDEF Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">Version</td><td role="">Version of the <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>
              table-initially 0x00010000</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">GlyphClassDef</td><td role="">Offset to class definition table for glyph
              type-from beginning of <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> header
              (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">AttachList</td><td role="">Offset to list of glyphs with attachment
              points-from beginning of <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> header
              (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigCaretList</td><td role="">Offset to list of positioning points for
              ligature carets-from beginning of
              <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> header (may be
              NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkAttachClassDef</td><td role="">Offset to class definition table for mark
              attachment type-from beginning of
              <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> header (may  be
              NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639314960"></a>Glyph Class Definition Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.6.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          tables use the Glyph Class Definition table (GlyphClassDef)
          to identify which glyph classes to adjust with
          lookups.</p><p role="">The table uses the same format as the Class Definition
          table (for details, see the chapter, Common Table
          Formats). However, the GlyphClassDef table uses class values
          already defined in the GlyphClassDef Enumeration
          list:</p><div class="table"><a name="idm114639310688"></a><p class="title"><strong>Table 23.2. GlyphClassDef Enumeration List</strong></p><div class="table-contents"><table role="" class="table" summary="GlyphClassDef Enumeration List" border="1"><colgroup><col width="6pc"/><col width="24pc"/></colgroup><thead><tr><th role="">Class</th><th role="">Description</th></tr></thead><tbody><tr><td role="">1</td><td role="">Base glyph (single character, spacing glyph)</td></tr><tr><td role="">2</td><td role="">Ligature glyph (multiple character, spacing
                  glyph)</td></tr><tr><td role="">3</td><td role="">Mark glyph (non-spacing combining glyph)</td></tr><tr><td role="">4</td><td role="">Component glyph (part of single character,
                  spacing glyph)</td></tr></tbody></table></div></div><br class="table-break"/><p role="">The font developer does not have to classify every glyph
        in the font, but any glyph not assigned a class value falls
        into Class zero (0). For instance, class values might be
        useful for the Arabic glyphs in a font, but not for the Latin
        glyphs. Then the GlyphClassDef table will list only Arabic
        glyphs, and-by default-the Latin glyphs will be assigned to
        Class 0. Component glyphs can be put together to generate
        ligatures. A ligature can be generated by creating a glyph in
        the font that references the component glyphs, or outputting
        the component glyphs in the desired sequence.  Component
        glyphs are not used in defining any <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
        <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> formats.</p><p role="">Example 2 at the end of this chapter defines a
          GlyphClassDef table with a sample glyph for each of the
          assigned classes.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639297984"></a>Attachment List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.7.1"></a>Specification</h3></div></div></div><p role="">The Attachment List table (AttachList) may be used to
          cache attachment point coordinates along with glyph
          bitmaps.</p><p role="">The table consists of an offset to a Coverage table
        (Coverage) listing all glyphs that define attachment points in
        the <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, a count of the glyphs with
        attachment points (GlyphCount), and an array of offsets to
        AttachPoint tables (AttachPoint). The array lists the
        AttachPoint tables, one for each glyph in the Coverage table,
        in the same order as the Coverage Index.</p><div class="table"><a name="idm114639294176"></a><p class="title"><strong>Table 23.3. AttachList table</strong></p><div class="table-contents"><table role="" class="table" summary="AttachList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
              AttachList table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs with attachment
              points</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">AttachPoint [GlyphCount]</td><td role="">Array of offsets to AttachPoint tables-from
              beginning of AttachList table-in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">An AttachPoint table consists of a count of the
          attachment points on a single glyph (PointCount) and an
          array of contour indices of those points (PointIndex),
          listed in increasing numerical order.</p><p role="">Example 3 at the end of the chapter demonstrates an
          AttachList table that defines attachment points for two
          glyphs.</p><div class="table"><a name="idm114639286080"></a><p class="title"><strong>Table 23.4. AttachPoint table</strong></p><div class="table-contents"><table role="" class="table" summary="AttachPoint table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PointCount</td><td role="">Number of attachment points on this
              glyph</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PointIndex [PointCount]</td><td role="">Array of contour point indices -in increasing
              numerical order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639280144"></a>Ligature Caret List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.8.1"></a>Specification</h3></div></div></div><p role="">The Ligature Caret List table (LigCaretList) defines
          caret positions for all the ligatures in a font. The table
          consists of an offset to a Coverage table that lists all the
          ligature glyphs (Coverage), a count of the defined ligatures
          (LigGlyphCount), and an array of offsets to LigGlyph tables
          (LigGlyph). The array lists the LigGlyph tables, one for
          each ligature in the Coverage table, in the same order as
          the Coverage Index.</p><p role="">Example 4 at the end of this chapter shows a
          LigCaretList table.</p><div class="table"><a name="idm114639276960"></a><p class="title"><strong>Table 23.5. LigCaretList table</strong></p><div class="table-contents"><table role="" class="table" summary="LigCaretList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
              LigCaretList table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LigGlyphCount</td><td role="">Number of ligature glyphs</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigGlyph [LigGlyphCount]</td><td role="">Array of offsets to LigGlyph tables-from
              beginning of LigCaretList table-in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639269488"></a>Ligature Glyph Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.9.1"></a>Specification</h3></div></div></div><p role="">A Ligature Glyph table (LigGlyph) contains the caret
          coordinates for a single ligature glyph. The number of
          coordinate values, each defined in a separate CaretValue
          table, equals the number of components in the ligature minus
          one (1).</p><p role="">The LigGlyph table consists of a count of the number of
          CaretValue tables defined for the ligature (CaretCount) and
          an array of offsets to CaretValue tables
          (CaretValue).</p><p role="">Example 4 at the end of the chapter shows a LigGlyph
          table.</p><div class="table"><a name="idm114639265936"></a><p class="title"><strong>Table 23.6. LigGlyph table</strong></p><div class="table-contents"><table role="" class="table" summary="LigGlyph table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CaretCount</td><td role="">Number of CaretValues for this ligature
              (components - 1)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">CaretValue [CaretCount]</td><td role="">Array of offsets to CaretValue tables-from
              beginning of LigGlyph table-in increasing coordinate
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639259936"></a>Caret Values Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.10.1"></a>Specification</h3></div></div></div><p role="">A Caret Values table (CaretValues), which defines caret
          positions for a ligature, can be any of three possible
          formats. One format uses design units to define the caret
          position. The other two formats use a contour point or
          Device table to fine-tune a caret's position at specific
          font sizes and device resolutions. Caret coordinates are
          either X or Y values, depending upon the text
          direction.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639256688"></a>CaretValue Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.11.1"></a>Specification</h3></div></div></div><p role="">The first format (CaretValueFormat1) consists of a
          format identifier (CaretValueFormat), followed by a single
          coordinate for the caret position (Coordinate). The
          Coordinate is in design units.</p><p role="">This format has the benefits of small size and
          simplicity, but the Coordinate value cannot be hinted for
          fine adjustments at different device resolutions.</p><p role="">Exampel 4 at the end of this chapter shows a
          CaretValueFormat1 table.</p><div class="table"><a name="idm114639253232"></a><p class="title"><strong>Table 23.7. CaretValueFormat1 table: Design units only</strong></p><div class="table-contents"><table role="" class="table" summary="CaretValueFormat1 table: Design units only" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CaretValueFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">Coordinate</td><td role="">X or Y value, in design units</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639247360"></a>CaretValue Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.12.1"></a>Specification</h3></div></div></div><p role="">The second format (CaretValueFormat2) specifies the
          caret coordinate in terms of a contour point index on a
          specific glyph. During font hinting, the contour point on
          the glyph outline may move. The point's final position after
          hinting provides the final value for rendering a given font
          size.</p><p role="">The table contains a format identifier
          (CaretValueFormat) and a contour point index
          (CaretValuePoint).</p><p role="">Example 5 at the end of this chapter demonstrates a
          CaretValueFormat2 table.</p><div class="table"><a name="idm114639243808"></a><p class="title"><strong>Table 23.8. CaretValueFormat2 table: Contour point</strong></p><div class="table-contents"><table role="" class="table" summary="CaretValueFormat2 table: Contour point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CaretValueFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">CaretValuePoint</td><td role="">Contour point index on glyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639237936"></a>CaretValue Format 3</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.13.1"></a>Specification</h3></div></div></div><p role="">The third format (CaretValueFormat3) also specifies the
          value in design units, but it uses a Device table rather
          than a contour point to adjust the value. This format offers
          the advantage of fine-tuning the Coordinate value for any
          device resolution. (For more information about Device
          tables, see the chapter, Common Table Formats.)</p><p role="">The format consists of a format identifier
          (CaretValueFormat), an X or Y value (Coordinate), and an
          offset to a Device table (DeviceTable).</p><p role="">Example 6 at the end of this chapter shows a
          CaretValueFormat3 table.</p><div class="table"><a name="idm114639234336"></a><p class="title"><strong>Table 23.9. CaretValueFormat3 table: Design units plus Device table</strong></p><div class="table-contents"><table role="" class="table" summary="CaretValueFormat3 table: Design units plus Device table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CaretValueFormat</td><td role="">Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">Coordinate</td><td role="">X or Y value, in design units</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">DeviceTable</td><td role="">Offset to Device table for X or Y value-from
              beginning of CaretValue table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639226912"></a>Mark Attachment Class Definition Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.14.1"></a>Specification</h3></div></div></div><p role="">A Mark Attachment Class Definition Table defines the
          class to which a mark glyph may belong. This table uses the
          same format as the Class Definition table (for details, see
          the chapter, Common Table Formats ).</p><p role="">Example 7 in this document shows a MarkAttachClassDef
        table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639223424"></a>GDEF Table Examples</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.15.1"></a>Specification</h3></div></div></div><p role="">The rest of this chapter describes examples of all the
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table formats. All the examples reflect unique
          parameters described below, but the samples provide a useful
          reference for building tables specific to other
          situations.</p><p role="">The examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639219248"></a>Example 1: GDEF Header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.16.1"></a>Specification</h3></div></div></div><p role="">Example 1 shows a <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> Header
          definition with offsets to each of the main tables in
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>.</p><div class="table"><a name="idm114639215632"></a><p class="title"><strong>Table 23.10. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">GDEFHeader</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheGDEFHeader</td><td role="">GDEFHeader table
                  definition</td></tr><tr><td role="">00010000</td><td role="">0x00010000</td><td role="">Version</td></tr><tr><td role="">000A</td><td role="">GlyphClassDefTable</td><td role="">offset to GlyphClassDef table</td></tr><tr><td role="">0026</td><td role="">AttachListTable</td><td role="">offset to AttachList table</td></tr><tr><td role="">0040</td><td role="">LigCaretListTable</td><td role="">offset to LigCaretList table</td></tr><tr><td role="">005A</td><td role="">MarkAttachClassDefTable</td><td role="">offset to Mark Attachment Class Definition
                  Table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639202800"></a>Example 2: GlyphClassDef Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.17.1"></a>Specification</h3></div></div></div><p role="">The GlyphClassDef table in Example 2 specifies a glyph
          for the each of the glyph classes predefined in the
          GlyphClassDef Enumeration List.</p><div class="table"><a name="idm114639200432"></a><p class="title"><strong>Table 23.11. Example 2</strong></p><div class="table-contents"><table role="" class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">GlyphClassDefTable</td><td role="">ClassDef table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassFormat</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">ClassRangeCount ClassRangeRecord[0</td></tr><tr><td role="">0024</td><td role="">iGlyphID</td><td role="">Start</td></tr><tr><td role="">0024</td><td role="">iGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, 1 = base glyphs
                  ClassRangeRecord[1]</td></tr><tr><td role="">009F</td><td role="">ffiLigGlyphID</td><td role="">Start</td></tr><tr><td role="">009F</td><td role="">ffiLigGlyphID</td><td role="">End</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class, 2 = ligature glyphs
                  ClassRangeRecord[2]</td></tr><tr><td role="">0058</td><td role="">umlautAccentGlyphID</td><td role="">Start</td></tr><tr><td role="">0058</td><td role="">umlautAccentGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class, 3 = mark glyphs
                  ClassRangeRecord[3]</td></tr><tr><td role="">018F</td><td role="">CurvedTailComponentGlyphID</td><td role="">Start</td></tr><tr><td role="">018F</td><td role="">CurvedTailComponentGlyphID</td><td role="">End</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">Class, 4 = component glyphs</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639174528"></a>Example 3: AttachList Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.18.1"></a>Specification</h3></div></div></div><p role="">In Example 3, the AttachList table enumerates the
          attachment points defined for two glyphs. The GlyphCoverage
          table identifies the glyphs: "a" and "e." For each covered
          glyph, an AttachPoint table specifies the attachment point
          count and point indices: one point for the "a" glyph and two
          for the "e" glyph.</p><div class="table"><a name="idm114639171952"></a><p class="title"><strong>Table 23.12. Example 3</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">AttachList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AttachListTable</td><td role="">AttachList table
                  definition</td></tr><tr><td role="">0012</td><td role="">GlyphCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0008</td><td role="">aAttachPoint</td><td role="">AttachPoint[0]</td></tr><tr><td role="">000C</td><td role="">eAttachPoint</td><td role="">AttachPoint[1</td></tr><tr><td role=""> </td><td role="">AttachPoint</td><td role=""> </td></tr><tr><td role=""> </td><td role="">aAttachPoint</td><td role="">AttachPoint table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PointCount</td></tr><tr><td role="">0012</td><td role="">18</td><td role="">PointIndex[0</td></tr><tr><td role=""> </td><td role="">AttachPoint</td><td role=""> </td></tr><tr><td role=""> </td><td role="">eAttachPoint</td><td role="">AttachPoint table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">PointCount</td></tr><tr><td role="">000E</td><td role="">14</td><td role="">PointIndex[0]</td></tr><tr><td role="">0017</td><td role="">23</td><td role="">PointIndex[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">GlyphCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">001C</td><td role="">aGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0020</td><td role="">eGlyphID</td><td role="">GlyphArray[1]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639140224"></a>Example 4: LigCaretList Table, LigGlyph Table and
        CaretValueFormat1 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.19.1"></a>Specification</h3></div></div></div><p role="">Example 4 defines a list of ligature carets. The
          LigCoverage table lists all the ligature glyphs that define
          caret positions. In this example, two ligatures are covered,
          "ffi" and "fi." For each covered glyph, a LigGlyph table
          specifies the number of carets for the ligature and their
          coordinate values. The "fi" ligature defines one caret,
          positioned between the "f" and "i" components; the "ffi"
          ligature defines two, one positioned between the two "f"
          components and the other positioned between the "f" and "i."
          The CaretValue tables shown here use Format1, where values
          are specified in design units only.</p><div class="table"><a name="idm114639137232"></a><p class="title"><strong>Table 23.13. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">LigCaretList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigCaretListTable</td><td role="">LigCaretList table
                  definition</td></tr><tr><td role="">0008</td><td role="">LigCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LigGlyphCount</td></tr><tr><td role="">0010</td><td role="">fiLigGlyph</td><td role="">offset to LigGlyph table[0]</td></tr><tr><td role="">0014</td><td role="">ffiLigGlyph</td><td role="">offset to LigGlyph table[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">009F</td><td role="">ffiLigGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">00A5</td><td role="">fiLigGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">LigGlyph</td><td role=""> </td></tr><tr><td role=""> </td><td role="">fiLigGlyph</td><td role="">LigGlyph table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CaretCount, equals the number of components -
                  1</td></tr><tr><td role="">000E</td><td role="">CaretFI</td><td role="">CaretValue[0</td></tr><tr><td role=""> </td><td role="">LigGlyph</td><td role=""> </td></tr><tr><td role=""> </td><td role="">ffiLigGlyph</td><td role="">LigGlyph table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CaretCount, equals the number of components -
                  1</td></tr><tr><td role="">0006</td><td role="">CaretFFI1</td><td role="">CaretValue[0]</td></tr><tr><td role="">000E</td><td role="">CaretFFI2</td><td role="">CaretValue[1</td></tr><tr><td role=""> </td><td role="">CaretValueFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">CaretFI</td><td role="">CaretValue table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CaretValueFormat design units only</td></tr><tr><td role="">025B</td><td role="">603</td><td role="">Coordinate X or Y valu</td></tr><tr><td role=""> </td><td role="">CaretValueFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">CaretFFI1</td><td role="">CaretValue table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CaretValueFormat design units only</td></tr><tr><td role="">025B</td><td role="">603</td><td role="">Coordinate X or Y valu</td></tr><tr><td role=""> </td><td role="">CaretValueFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">CaretFFI2</td><td role="">CaretValue table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CaretValueFormat design units only</td></tr><tr><td role="">04B6</td><td role="">1206</td><td role="">Coordinate X or Y value</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639088976"></a>Example 5: CaretValueFormat2 Table </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.20.1"></a>Specification</h3></div></div></div><p role="">Example 5 shows a CaretValueFormat2 table that specifies
          a ligature caret coordinate in terms of a contour point
          index on a specific glyph. The final position of the caret
          depends on the location of the contour point on the glyph
          after hinting.</p><div class="table"><a name="idm114639086464"></a><p class="title"><strong>Table 23.14. Example 5</strong></p><div class="table-contents"><table role="" class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">CaretValueFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Caret1</td><td role="">CaretValue table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CaretValueFormat contour point</td></tr><tr><td role="">000D</td><td role="">13</td><td role="">CaretValuePoint contour point index</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639078144"></a>Example 6: CaretValueFormat3 Table </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.21.1"></a>Specification</h3></div></div></div><p role="">In Example 6, the CaretValueFormat3 table defines a
          caret position in design units, but includes a Device table
          to adjust the X or Y coordinate for the point size and
          resolution of the output font. Here, the Device table
          specifies pixel adjustments for font sizes from 12 ppem to
          17 ppem.</p><div class="table"><a name="idm114639075568"></a><p class="title"><strong>Table 23.15. Example 6</strong></p><div class="table-contents"><table role="" class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">CaretValueFormat3</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Caret3</td><td role="">CaretValue table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">CaretValueFormat design units plus Device
                  table</td></tr><tr><td role="">04B6</td><td role="">1206</td><td role="">Coordinate X or Y value, design units</td></tr><tr><td role="">0006</td><td role="">CaretDevice</td><td role="">offset to Device tabl</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">CaretDevice</td><td role="">Device Table definition</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">StartSize</td></tr><tr><td role="">0011</td><td role="">17</td><td role="">EndSize</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">DeltaFormat</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppm by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppm by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppm by 1 pixel</td></tr><tr><td role="">1111</td><td role="">1</td><td role="">increase 15ppm by 1 pixel</td></tr><tr><td role=""> </td><td role="">2</td><td role="">increase 16ppm by 2 pixel</td></tr><tr><td role="">2200</td><td role="">2</td><td role="">increase 17ppm by 2 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639050720"></a>Example 7: MarkAttachClassDef Table </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.23.22.1"></a>Specification</h3></div></div></div><p role="">In Example 7, the MarkAttachClassDef table specifies an
          attachment class for the each of the glyph ranges predefined
          in the GlyphClassDef Enumeration List as marks.</p><div class="table"><a name="idm114639048304"></a><p class="title"><strong>Table 23.16. Example 7</strong></p><div class="table-contents"><table role="" class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">theMarkAttachClassDefTable</td><td role="">ClassDef table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassFormat</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">ClassRangeCount ClassRangeRecord[0] </td></tr><tr><td role="">0268</td><td role="">graveAccentGlyphID</td><td role="">Start </td></tr><tr><td role="">026A</td><td role="">circumflexAccentGlyphID</td><td role="">End </td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, 1 = top marks ClassRangeRecord[1]
                </td></tr><tr><td role="">0270</td><td role="">diaeresisAccentGlyphID</td><td role="">Start </td></tr><tr><td role="">0272</td><td role="">acuteAccentGlyphID</td><td role="">End </td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, 1 = top marks ClassRangeRecord[2]
                </td></tr><tr><td role="">028C</td><td role="">diaeresisBelowGlyphID</td><td role="">Start </td></tr><tr><td role="">028F</td><td role="">cedillaGlyphID</td><td role="">End </td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class, 2 = bottom marks ClassRangeRecord[3]
                </td></tr><tr><td role="">0295</td><td role="">circumflexBelowGlyphID</td><td role="">Start </td></tr><tr><td role="">0295</td><td role="">circumflexBelowGlyphID</td><td role="">End </td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class, 2 = bottom marks </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>