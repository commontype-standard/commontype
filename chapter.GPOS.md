<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.GPOS"></a>Chapter 24. GPOS - The Glyph Positioning Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80795724000"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.1.1"></a>Specification</h3></div></div></div><p role="">The Glyph Positioning table (<a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>)
          provides precise control over glyph placement for
          sophisticated text layout and rendering in each script and
          language system that a font supports.</p><p role="">Complex glyph positioning becomes an issue in writing
          systems, such as Vietnamese, that use diacritical and other
          marks to modify the sound or meaning of characters. These
          writing systems require controlled placement of all marks in
          relation to one another for legibility and linguistic
          accuracy.</p><div class="figure"><a name="idm80795720432"></a><p class="title"><strong>Figure 24.1. Figure 4a. Vietnamese words with marks.</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4a.gif" alt="Figure 4a. Vietnamese words with marks."/></div></div></div><br class="figure-break"/><p role="">Other writing systems require sophisticated glyph
          positioning for correct typographic composition. For
          instance, Urdu glyphs are calligraphic and connect to one
          another along a descending, diagonal text line that proceeds
          from right to left. To properly render Urdu, a
          text-processing client must modify both the horizontal (X)
          and vertical (Y) positions of each glyph.</p><div class="figure"><a name="idm80803813344"></a><p class="title"><strong>Figure 24.2. Figure 4b. Urdu layout requires glyph positioning
            control, as well as contextual substitution</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4b.gif" alt="Figure 4b. Urdu layout requires glyph positioning control, as well as contextual substitution"/></div></div></div><br class="figure-break"/><p role="">With the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, a font developer
          can define a complete set of positioning adjustment features
          in an OpenType font. <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> data,
          organized by script and language system, is easy for a
          text-processing client to use to position glyphs.</p><p role="">Positioning Glyphs with TrueType 1.0</p><p role="">Glyph positioning in TrueType uses only two values,
          placement and advance, to specify a glyph's position for
          text layout. If glyphs are positioned with respect to a
          virtual "pen point" that moves along a line of text,
          placement describes the glyph's position with respect to the
          current pen point, and advance describes where to move the
          pen point to position the next glyph (see Figure 4c). For
          horizontal text, placement corresponds to the left side
          bearing, and advance corresponds to the advance
          width.</p><div class="figure"><a name="idm80803807920"></a><p class="title"><strong>Figure 24.3. Figure 4c. Glyph positioning with TrueType</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4c.gif" alt="Figure 4c. Glyph positioning with TrueType"/></div></div></div><br class="figure-break"/><p role="">TrueType specifies placement and advance only in the X
          direction for horizontal layout and only in the Y direction
          for vertical layout. For simple Latin text layout, these two
          values may be adequate to position glyphs correctly. But,
          for texts that require more sophisticated layout, the values
          must cover a richer range. Placement and advance may need
          adjustment vertically, as well as horizontally.</p><p role="">The only positioning adjustment defined in TrueType is
          pair kerning, which modifies the horizontal spacing between
          two glyphs. A typical kerning table lists pairs of glyphs
          and specifies how much space a text-processing client should
          add or remove between the glyphs to properly display each
          pair. It does not provide specific information about how to
          adjust the glyphs in each pair, and cannot adjust contexts
          of more than two glyphs.</p><p role="">Positioning Glyphs with OpenType</p><p role="">OpenType fonts allow excellent control and flexibility
          for positioning a single glyph and for positioning multiple
          glyphs in relation to one another. By using both X and Y
          values that the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table defines for
          placement and advance and by using glyph attachment points,
          a client can more precisely adjust the position of a
          glyph.</p><p role="">In addition, the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table can
          reference a Device table to define subtle, device-dependent
          adjustments to any placement or advance value at any font
          size and device resolution. For example, a Device table can
          specify adjustments at 51 pixels per em (ppem) that do not
          occur at 50 ppem.</p><p role="">X and Y values specified in OpenType fonts for placement
          operations are always within the typical Cartesian
          coordinate system (origin at the baseline of the left side),
          regardless of the writing direction. Additionally, all
          values specified are done so in font unit measurements. This
          is especially convenient for font designers, since glyphs
          are drawn in the same coordinate system. However, it's
          important to note that the meaning of "advance width"
          changes, depending on the writing direction.</p><p role="">For example, in left-to-right scripts, if the first
          glyph has an advance width of 100, then the second glyph
          begins at 100,0. In right-to-left scripts, if the first
          glyph has an advance width of 100, then the second glyph
          begins at -100,0. For a top-to-bottom feature, to increase
          the advance height of a glyph by 100, the YAdvance = 100.
          For any feature, regardless of writing direction, to lower
          the dieresis over an 'o' by 10 units, set the YPlacement =
          -10.</p><p role="">Other <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> features can define
          attachment points to combine glyphs and position them with
          respect to one another. A glyph might have multiple
          attachment points. The point used will depend on the glyph
          to be attached. For instance, a base glyph could have
          attachment points for different diacritical marks.</p><div class="figure"><a name="idm80803797728"></a><p class="title"><strong>Figure 24.4. Base glyph with multiple attachment points.</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/attach.gif" alt="Base glyph with multiple attachment points."/></div></div></div><br class="figure-break"/><p role="">To reduce the size of the font file, a base glyph may
          use the same attachment point for all mark glyphs assigned
          to a particular class. For example, a base glyph could have
          two attachment points, one above and one below the glyph.
          Then all marks that attach above glyphs would be attached at
          the high point, and all marks that attach below glyphs would
          be attached at the low point. Attachment points are useful
          in scripts, such as Arabic, that combine numerous glyphs
          with vowel marks.</p><p role="">Attachment points also are useful for connecting
          cursive-style glyphs. Glyphs in cursive fonts can be
          designed to attach or overlap when rendered. Alternatively,
          the font developer can use OpenType to create a cursive
          attachment feature and define explicit exit and entry
          attachment points for each glyph (see Figure 4d).</p><div class="figure"><a name="idm80803794432"></a><p class="title"><strong>Figure 24.5. Figure 4d. Entry and exit points marked on contextual
            Urdu glyph variations</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4d.gif" alt="Figure 4d. Entry and exit points marked on contextual Urdu glyph variations"/></div></div></div><br class="figure-break"/><p role="">The <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table supports eight types
          of actions for positioning and attaching glyphs:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>single adjustment</em></span> positions
              one glyph, such as a superscript or subscript.</p></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>pair adjustment</em></span> positions two
              glyphs with respect to one another. Kerning is an
              example of pair adjustment.</p></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>cursive attachment</em></span> describes
              cursive scripts and other glyphs that are connected with
              attachment points when rendered.</p></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>MarkToBase attachment</em></span>
              positions combining marks with respect to base glyphs,
              as when positioning vowels, diacritical marks, or tone
              marks in Arabic, Hebrew, and Vietnamese.</p></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>MarkToLigature attachment</em></span>
              positions combining marks with respect to ligature
              glyphs. Because ligatures may have multiple points for
              attaching marks, the font developer needs to associate
              each mark with one of the ligature glyph's
              components.</p></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>MarkToMark attachment</em></span>
              positions one mark relative to another, as when
              positioning tone marks with respect to vowel diacritical
              marks in Vietnamese.</p></li><li role="" class="listitem"><p role=""><span role="" class="emphasis"><em>Contextual positioning</em></span>
              describes how to position one or more glyphs in context,
              within an identifiable sequence of specific glyphs,
              glyph classes, or varied sets of glyphs. One or more
              positioning operations may be performed on "input"
              context sequences. Figure 4e illustrates a context for
              positioning adjustments.</p></li><li role="" class="listitem"><p role=""><span role="" class="emphasis"><em>Chaining Contextual positioning</em></span>
              describes how to position one or more glyphs in a
              chained context, within an identifiable sequence of
              specific glyphs, glyph classes, or varied sets of
              glyphs. One or more positioning operations may be
              performed on "input" context sequences.</p></li></ul></div><div class="figure"><a name="idm80803779904"></a><p class="title"><strong>Figure 24.6. Figure 4e. Contextual positioning lowered the accent
            over a vowel glyph that followed an overhanging uppercase
            glyph</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4e.gif" alt="Figure 4e. Contextual positioning lowered the accent over a vowel glyph that followed an overhanging uppercase glyph"/></div></div></div><br class="figure-break"/><p role="">Table Organization</p><p role="">The <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table begins with a header
          that defines offsets to a ScriptList, a FeatureList, and a
          LookupList (see Figure 4f):</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The ScriptList identifies all the scripts and
              language systems in the font that use glyph
              positioning.</p></li><li role="" class="listitem"><p role="">The FeatureList defines all the glyph positioning
              features required to render these scripts and language
              systems.</p></li><li role="" class="listitem"><p role="">The LookupList contains all the lookup data needed
              to implement each glyph positioning feature.</p></li></ul></div><p role="">For a detailed discussion of ScriptLists, FeatureLists,
          and LookupLists, see the chapter, Common Table Formats. The
          following discussion summarizes how the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table
          works.</p><div class="figure"><a name="idm80803771856"></a><p class="title"><strong>Figure 24.7. Figure 4f. High-level organization of <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
            table</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig4f.gif" alt="Figure 4f. High-level organization of GPOS table"/></div></div></div><br class="figure-break"/><p role="">The <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table is organized so text
          processing clients can easily locate the features and
          lookups that apply to a particular script or language
          system. To access <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> information,
          clients should use the following procedure:</p><div role="" class="orderedlist"><ol class="orderedlist" type="1"><li role="" class="listitem"><p role="">Locate the current script in the
              <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> ScriptList table.</p></li><li role="" class="listitem"><p role="">If the language system is known, search the script
              for the correct LangSys table; otherwise, use the
              script's default language system (DefaultLangSys
              table).</p></li><li role="" class="listitem"><p role="">The LangSys table provides index numbers into the
              <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> FeatureList table to access a
              required feature and a number of additional
              features.</p></li><li role="" class="listitem"><p role="">Inspect the FeatureTag of each feature, and select
              the features to apply to an input glyph string.</p></li><li role="" class="listitem"><p role="">Each feature provides an array of index numbers into
              the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> LookupList table. Lookup
              data is defined in one or more subtables that contain
              information about specific glyphs and the kinds of
              operations to be performed on them.</p></li><li role="" class="listitem"><p role="">Assemble all lookups from the set of chosen
              features, and apply the lookups in the order given in
              the LookupList table.</p></li></ol></div><p role="">A lookup uses subtables to define the specific
          conditions, type, and results of a positioning action used
          to implement a feature. All subtables in a lookup must be of
          the same LookupType, as listed in the LookupType Enumeration
          table:</p><div class="table"><a name="idm80803758672"></a><p class="title"><strong>Table 24.1. LookupType Enumeration table for glyph
            positioning</strong></p><div class="table-contents"><table role="" class="table" summary="LookupType Enumeration table for glyph&#10;            positioning" border="1"><colgroup><col width="3pc"/><col width="11pc"/><col width="16pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Type</th><th role="">Description</th></tr></thead><tbody><tr><td role="">1</td><td role="">Single adjustment</td><td role="">Adjust position of a single glyph</td></tr><tr><td role="">2</td><td role="">Pair adjustment</td><td role="">Adjust position of a pair of glyphs</td></tr><tr><td role="">3</td><td role="">Cursive attachment</td><td role="">Attach cursive glyphs</td></tr><tr><td role="">4</td><td role="">MarkToBase attachment</td><td role="">Attach a combining mark to a base glyph</td></tr><tr><td role="">5</td><td role="">MarkToLigature attachment</td><td role="">Attach a combining mark to a ligature</td></tr><tr><td role="">6</td><td role="">MarkToMark attachment</td><td role="">Attach a combining mark to another mark</td></tr><tr><td role="">7</td><td role="">Context positioning</td><td role="">Position one or more glyphs in context</td></tr><tr><td role="">8</td><td role="">Chained Context positioning</td><td role="">Position one or more glyphs in chained
                  context</td></tr><tr><td role="">9</td><td role="">Extension positioning</td><td role="">Extension mechanism for other positionings</td></tr><tr><td role="">10+</td><td role="">Reserved</td><td role="">For future use</td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each LookupType is defined by one or more subtables,
          whose format depends on the type of positioning operation
          and the resulting storage efficiency. When glyph information
          is best presented in more than one format, a single lookup
          may define more than one subtable, as long as all the
          subtables are of the same LookupType. For example, within a
          given lookup, a glyph index array format may best represent
          one set of target glyphs, whereas a glyph index range format
          may be better for another set.</p><p role="">A series of positioning operations on the same glyph or
          string requires multiple lookups, one for each separate
          action. The values in the ValueRecords are accumulated in
          these cases. Each lookup is given a different array number
          in the LookupList table and is applied in the LookupList
          order.</p><p role="">During text processing, a client applies a lookup to
          each glyph in the string before moving to the next lookup. A
          lookup is finished for a glyph after the client locates the
          target glyph or glyph context and performs a positioning, if
          specified. To move to the "next" glyph, the client will
          typically skip all the glyphs that participated in the
          lookup operation: glyphs that were positioned as well as any
          other glyphs that formed a context for the operation.</p><p role="">There is just one exception: the "next" glyph in a
          sequence may be one of those that formed a context for the
          operation just performed. For example, in the case of pair
          positioning operations (i.e., kerning), if the position
          value record for the second glyph is null, that glyph is
          treated as the "next" glyph in the sequence.</p><p role="">This rest of this chapter describes the
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> header and the subtables defined for
          each LookupType. Several <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables
          share other tables: ValueRecords, Anchor tables, and
          MarkArrays. For easy reference, the shared tables are
          described at the end of this chapter.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803731424"></a>GPOS Header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.2.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table begins with a header
          that contains a version number (Version) initially set to
          1.0 (0x00010000) and offsets to three tables: ScriptList,
          FeatureList, and LookupList. For descriptions of these
          tables, see the chapter, Common Table Formats. Example 1 at
          the end of this chapter shows a <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          Header table definition.</p><div class="table"><a name="idm80803727536"></a><p class="title"><strong>Table 24.2. GPOS Header</strong></p><div class="table-contents"><table role="" class="table" summary="GPOS Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">Version</td><td role="">Version of the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
              table-initially = 0x00010000</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ScriptList</td><td role="">Offset to ScriptList table-from beginning of
              <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">FeatureList</td><td role="">Offset to FeatureList table-from beginning of
              <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table </td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LookupList</td><td role="">Offset to LookupList table-from beginning of
              <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.2.2"></a>Annotation</h3></div></div></div><p role="">Nothing to note.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803714368"></a>Lookup Type 1: Single Adjustment Positioning Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.3.1"></a>Specification</h3></div></div></div><p role="">A single adjustment positioning subtable (SinglePos) is
          used to adjust the position of a single glyph, such as a
          subscript or superscript. In addition, a SinglePos subtable
          is commonly used to implement lookup data for contextual
          positioning.</p><p role="">A SinglePos subtable will have one of two formats: one
          that applies the same adjustment to a series of glyphs, or
          one that applies a different adjustment for each unique
          glyph.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.3.2"></a>Annotation</h3></div></div></div><p role="">None</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803709040"></a>Single Adjustment Positioning: Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.4.1"></a>Specification</h3></div></div></div><p role="">A SinglePosFormat1 subtable applies the same positioning
          value or values to each glyph listed in its Coverage table.
          For instance, when a font uses old-style numerals, this
          format could be applied to uniformly lower the position of
          all math operator glyphs.</p><p role="">The Format 1 subtable consists of a format identifier
	  (PosFormat), an offset to a Coverage table that defines the
	  glyphs to be adjusted by the positioning values (Coverage),
	  and the format identifier (ValueFormat) that describes the
	  amount and kinds of data in the ValueRecord.</p><p role="">The ValueRecord specifies one or more positioning values
	  to be applied to all covered glyphs (Value). For example, if
	  all glyphs in the Coverage table require both horizontal and
	  vertical adjustments, the ValueRecord will specify values
	  for both XPlacement and Yplacement.</p><p role="">Example 2 at the end of this chapter shows a
	  SinglePosFormat1 subtable used to adjust the placement of
	  subscript glyphs.</p><div class="table"><a name="idm80803704640"></a><p class="title"><strong>Table 24.3. SinglePosFormat1 subtable: Single positioning value</strong></p><div class="table-contents"><table role="" class="table" summary="SinglePosFormat1 subtable: Single positioning value" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              SinglePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat</td><td role="">Defines the types of data in the
              ValueRecord</td><td class="auto-generated"> </td></tr><tr><td role="">ValueRecord</td><td role="">Value</td><td role="">Defines positioning value(s) – applied to all
              glyphs in the Coverage table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.4.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to adjust the glyph
	  matched by C by {ValueFormat, Value}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803692128"></a>Single Adjustment Positioning: Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.5.1"></a>Specification</h3></div></div></div><p role="">A SinglePosFormat2 subtable provides an array of
          ValueRecords that contains one positioning value for each
          glyph in the Coverage table. This format is more flexible
          than Format 1, but it requires more space in the font
          file.</p><p role="">For example, assume that the Cyrillic script will be
          used in left-justified text. For all glyphs, Format 2 could
          define position adjustments for left side bearings to align
          the left edges of the paragraphs. To achieve this, the
          Coverage table would list every glyph in the script, and the
          SinglePosFormat2 subtable would define a ValueRecord for
          each covered glyph. Correspondingly, each ValueRecord would
          specify an XPlacement adjustment value for the left side
          bearing.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: All ValueRecords defined in a SinglePos subtable
            must have the same ValueFormat. In this example, if
            XPlacement is the only value that a ValueRecord needs to
            optically align the glyphs, then XPlacement will be the
            only value specified in the ValueFormat of the
            subtable.</p></blockquote></div><p role="">As in Format 1, the Format 2 subtable consists of a
          format identifier (PosFormat), an offset to a Coverage table
          that defines the glyphs to be adjusted by the positioning
          values (Coverage), and the format identifier (ValueFormat)
          that describes the amount and kinds of data in the
          ValueRecords. In addition, the Format 2 subtable
          includes:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">A count of the ValueRecords (ValueCount). One
              ValueRecord is defined for each glyph in the Coverage
              table.</p></li><li role="" class="listitem"><p role="">An array of ValueRecords that specify positioning
              values (Value). Because the array follows the Coverage
              Index order, the first ValueRecord applies to the first
              glyph listed in the Coverage table, and so on.</p></li></ul></div><p role="">Example 3 at the end of this chapter shows how to adjust
          the spacing of three dash glyphs with a SinglePosFormat2
          subtable.</p><div class="table"><a name="idm80803683936"></a><p class="title"><strong>Table 24.4. SinglePosFormat2 subtable: Array of positioning values</strong></p><div class="table-contents"><table role="" class="table" summary="SinglePosFormat2 subtable: Array of positioning values" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier – format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              SinglePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat</td><td role="">Defines the types of data in the
              ValueRecord</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueCount</td><td role="">Number of ValueRecords</td><td class="auto-generated"> </td></tr><tr><td role="">ValueRecord</td><td role="">Value [ValueCount]</td><td role="">Array of ValueRecords – positioning values
              applied to glyphs</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.5.2"></a>Annotation</h3></div></div></div><p role="">It is unclear whether ValueCount must equal the number of covered
          glyphs. We assume that is must be equal.</p><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to adjust the glyph
	  matched by C by {ValueFormat, Value [Coverage[g]]}, where g
	  is the glyph id of the matched glyph.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803669392"></a>Lookup Type 2: Pair Adjustment Positioning Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.6.1"></a>Specification</h3></div></div></div><p role="">A pair adjustment positioning subtable (PairPos) is used
          to adjust the positions of two glyphs in relation to one
          another-for instance, to specify kerning data for pairs of
          glyphs. Compared to a typical kerning table, however, a
          PairPos subtable offers more flexiblity and precise control
          over glyph positioning. The PairPos subtable can adjust each
          glyph in a pair independently in both the X and Y
          directions, and it can explicitly describe the particular
          type of adjustment applied to each glyph. In addition, a
          PairPos subtable can use Device tables to subtly adjust
          glyph positions at each font size and device
          resolution.</p><p role="">PairPos subtables can be either of two formats: one that
          identifies glyphs individually by index (Format 1), or one
          that identifies glyphs by class (Format 2).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803665984"></a>Pair Positioning Adjustment: Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.7.1"></a>Specification</h3></div></div></div><p role="">Format 1 uses glyph indices to access positioning data
          for one or more specific pairs of glyphs. All pairs are
          specified in the order determined by the layout direction of
          the text.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: For text written from right to left, the
            right-most glyph will be the first glyph in a pair;
            conversely, for text written from left to right, the
            left-most glyph will be first.</p></blockquote></div><p role="">A PairPosFormat1 subtable contains a format identifier
          (PosFormat) and two ValueFormats:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">ValueFormat1 applies to the ValueRecord of the first
              glyph in each pair. ValueRecords for all first glyphs
              must use ValueFormat1. If ValueFormat1 is set to zero
              (0), the corresponding glyph has no ValueRecord and,
              therefore, should not be repositioned.</p></li><li role="" class="listitem"><p role="">ValueFormat2 applies to the ValueRecord of the
              second glyph in each pair. ValueRecords for all second
              glyphs must use ValueFormat2. If ValueFormat2 is set to
              null, then the second glyph of the pair is the "next"
              glyph for which a lookup should be performed.</p></li></ul></div><p role="">A PairPos subtable also defines an offset to a Coverage
          table (Coverage) that lists the indices of the first glyphs
          in each pair. More than one pair can have the same first
          glyph, but the Coverage table will list that glyph only
          once.</p><p role="">The subtable also contains an array of offsets to
          PairSet tables (PairSet) and a count of the defined tables
          (PairSetCount). The PairSet array contains one offset for
          each glyph listed in the Coverage table and uses the same
          order as the Coverage Index.</p><div class="table"><a name="idm80803658160"></a><p class="title"><strong>Table 24.5. PairPosFormat1 subtable: Adjustments for glyph pairs</strong></p><div class="table-contents"><table role="" class="table" summary="PairPosFormat1 subtable: Adjustments for glyph pairs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
              PairPos subtable - only the first glyph in each
              pair</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat1</td><td role="">Defines the types of data in ValueRecord1 - for
              the first glyph in the pair - may be zero
              (0)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat2</td><td role="">Defines the types of data in ValueRecord2 - for
              the second glyph in the pair - may be zero
              (0)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PairSetCount</td><td role="">Number of PairSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">PairSetOffset [PairSetCount]</td><td role="">Array of offsets to PairSet tables - from
              beginning of PairPos subtable - ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A PairSet table enumerates all the glyph pairs that
          begin with a covered glyph. An array of PairValueRecords
          (PairValueRecord) contains one record for each pair and
          lists the records sorted by the GlyphID of the second glyph
          in each pair. PairValueCount specifies the number of
          PairValueRecords in the set.</p><div class="table"><a name="idm80803645808"></a><p class="title"><strong>Table 24.6. PairSet table</strong></p><div class="table-contents"><table role="" class="table" summary="PairSet table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PairValueCount</td><td role="">Number of PairValueRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PairValueRecord
              [PairValueCount]</td><td role="">Array of PairValueRecords - ordered by GlyphID
              of the second glyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A PairValueRecord specifies the second glyph in a pair
          (SecondGlyph) and defines a ValueRecord for each glyph
          (Value1 and Value2). If ValueFormat1 is set to zero (0) in
          the PairPos subtable, ValueRecord1 will be empty; similarly,
          if ValueFormat2 is 0, Value2 will be empty.</p><p role="">Example 4 at the end of this chapter shows a
          PairPosFormat1 subtable that defines two cases of pair
          kerning.</p><div class="table"><a name="idm80803639216"></a><p class="title"><strong>Table 24.7. PairValueRecord</strong></p><div class="table-contents"><table role="" class="table" summary="PairValueRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">GlyphID</td><td role="">SecondGlyph</td><td role="">GlyphID of second glyph in the pair-first
              glyph is listed in the Coverage table</td><td class="auto-generated"> </td></tr><tr><td role="">ValueRecord</td><td role="">Value1</td><td role="">Positioning data for the first glyph in the
              pair</td><td class="auto-generated"> </td></tr><tr><td role="">ValueRecord</td><td role="">Value2</td><td role="">Positioning data for the second glyph in the
              pair</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.7.2"></a>Annotation</h3></div></div></div><p role="">The type of the last field in PairPosFormat1 is wrong; it
          should be Offset.</p><p role="">It is unclear whether PairSetCount must equal the number of
          covered glyphs. We assume that it must.</p><p role="">It is unclear whether a PairSet entry can be null. We
	  assume that none can be.</p><p role="">It is unclear whether a PairValueRecord can be null. We
	  assume that none can be.</p><p role="">It is unclear whether ValueFormat1 and ValueFormat2 can
	  be both 0 at the same time. We assume they can be.</p><p role="">If ValueFormat2 ≠ 0, the pattern matched by the
	PairValueRecord r = PairSet [m].PairValueRecord [n] is
	▶ I<sub>0</sub> L*
	I<sub>1</sub> ◀, where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">I<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>1</sub> is {r.SecondGlyph}
	      ∖ LookupFlag</p></li></ul></div><p role="">
	  If ValueFormat2 = 0, the pattern matched by that record is
	  ▶ I<sub>0</sub> ◀ L*
	  I<sub>1</sub>.</p><p role="">The action of this subtable is to adjust the glyph
	  matched by I<sub>0</sub> by {ValueFormat1,
	  r.Value1} and then the glyph matched by
	  I<sub>1</sub> by {ValueFormat2,
	  r.Value2}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803621488"></a>Pair Positioning Adjustment: Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.8.1"></a>Specification</h3></div></div></div><p role="">Format 2 defines a pair as a set of two glyph classes
          and modifies the positions of all the glyphs in a class. For
          example, this format is useful in Japanese scripts that
          apply specific kerning operations to all glyph pairs that
          contain punctuation glyphs. One class would be defined as
          all glyphs that may be coupled with punctuation marks, and
          the other classes would be groups of similar punctuation
          glyphs.</p><p role="">The PairPos Format2 subtable begins with a format
          identifier (PosFormat) and an offset to a Coverage table
          (Coverage), measured from the beginning of the PairPos
          subtable. The Coverage table lists the indices of the first
          glyphs that may appear in each glyph pair. More than one
          pair may begin with the same glyph, but the Coverage table
          lists the glyph index only once.</p><p role="">A PairPosFormat2 subtable also includes two
          ValueFormats:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">ValueFormat1 applies to the ValueRecord of the first
              glyph in each pair. ValueRecords for all first glyphs
              must use ValueFormat1. If ValueFormat1 is set to zero
              (0), the corresponding glyph has no ValueRecord and,
              therefore, should not be repositioned.</p></li><li role="" class="listitem"><p role="">ValueFormat2 applies to the ValueRecord of the
	      second glyph in each pair. ValueRecords for all second
	      glyphs must use ValueFormat2. If ValueFormat2 is set to
	      null, then the second glyph of the pair is the "next"
	      glyph for which a lookup should be performed.</p></li></ul></div><p role="">PairPosFormat2 requires that each glyph in all pairs be
          assigned to a class, which is identified by an integer
          called a class value. (For details about classes, see the
          chapter, Common Table Formats.) Pairs are then represented
          in a two-dimensional array as sequences of two class values.
          Multiple pairs can be represented in one Format 2
          subtable.</p><p role="">A PairPosFormat2 subtable contains offsets to two class
          definition tables: one that assigns class values to all the
          first glyphs in all pairs (ClassDef1), and one that assigns
          class values to all the second glyphs in all pairs
          (ClassDef2). If both glyphs in a pair use the same class
          definition, the offset value will be the same for ClassDef1
          and ClassDef2. The subtable also specifies the number of
          glyph classes defined in ClassDef1 (Class1Count) and in
          ClassDef2 (Class2Count), including Class0.</p><p role="">For each class identified in the ClassDef1 table, a
          Class1Record enumerates all pairs that contain a particular
          class as a first component. The Class1Record array stores
          all Class1Records according to class value.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Class1Records are not tagged with a class value
            identifier. Instead, the index value of a Class1Record in
            the array defines the class value represented by the
            record. For example, the first Class1Record enumerates
            pairs that begin with a Class 0 glyph, the second
            Class1Record enumerates pairs that begin with a Class1
            glyph, and so on.</p></blockquote></div><div class="table"><a name="idm80803611360"></a><p class="title"><strong>Table 24.8. PairPosFormat2 subtable: Class pair adjustment</strong></p><div class="table-contents"><table role="" class="table" summary="PairPosFormat2 subtable: Class pair adjustment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
              PairPos subtable - for the first glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat1</td><td role="">ValueRecord definition - for the first glyph of
              the pair - may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ValueFormat2</td><td role="">ValueRecord definition - for the second glyph
              of the pair - may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ClassDef1</td><td role="">Offset to ClassDef table - from beginning of
              PairPos subtable - for the first glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ClassDef2</td><td role="">Offset to ClassDef table - from beginning of
              PairPos subtable - for the second glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Class1Count</td><td role="">Number of classes in ClassDef1 table - includes
              Class0</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Class2Count</td><td role="">Number of classes in ClassDef2 table - includes
              Class0</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">Class1Record [Class1Count]</td><td role="">Array of Class1 records - ordered by
              Class1</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each Class1Record contains an array of Class2Records
          (Class2Record), which also are ordered by class value. One
          Class2Record must be declared for each class in the
          ClassDef2 table, including Class 0.</p><div class="table"><a name="idm80803594576"></a><p class="title"><strong>Table 24.9. Class1Record</strong></p><div class="table-contents"><table role="" class="table" summary="Class1Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">struct</td><td role="">Class2Record [Class2Count]</td><td role="">Array of Class2 records - ordered by
              Class2</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A Class2Record consists of two ValueRecords, one for the
          first glyph in a class pair (Value1) and one for the second
          glyph (Value2). If the PairPos subtable has a value of zero
          (0) for ValueFormat1 or ValueFormat2, the corresponding
          record (ValueRecord1 or ValueRecord2) will be empty.</p><p role="">Example 5 at the end of this chapter demonstrates pair
          kerning with glyph classes in a PairPosFormat2
          subtable.</p><div class="table"><a name="idm80803589488"></a><p class="title"><strong>Table 24.10. Class2Record</strong></p><div class="table-contents"><table role="" class="table" summary="Class2Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ValueRecord</td><td role="">Value1</td><td role="">Positioning for first glyph - empty if
              ValueFormat1 = 0</td><td class="auto-generated"> </td></tr><tr><td role="">ValueRecord</td><td role="">Value2</td><td role="">Positioning for second glyph - empty if
              ValueFormat2 = 0</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.8.2"></a>Annotation</h3></div></div></div><p role="">It is unclear whether ValueFormat1 and ValueFormat2 can
	  be both 0 at the same time. We assume they can be.</p><p role="">If ValueFormat2 ≠ 0, the pattern matched by the
	Class2Record r = Class1Record
	[m].Class2Record [n] is ▶ I<sub>0</sub> L*
	I<sub>1</sub> ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">I<sub>0</sub> is ClassDef1[m] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>1</sub> is ClassDef2[n] ∖ LookupFlag</p></li></ul></div><p role="">
	  If ValueFormat2 = 0, the pattern is ▶
	  I<sub>0</sub> ◀ L* I<sub>1</sub>.</p><p role="">The action of r is to adjust the glyph matched by
	I<sub>0</sub> by {ValueFormat1, r.Value1} and then
	the glyph matched by I<sub>1</sub> by
	{ValueFormat2, r.Value2}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80803575360"></a>Lookup Type 3: Cursive Attachment Positioning Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.9.1"></a>Specification</h3></div></div></div><p role="">Some cursive fonts are designed so that adjacent glyphs
          join when rendered with their default positioning. However,
          if positioning adjustments are needed to join the glyphs, a
          cursive attachment positioning (CursivePos) subtable can
          describe how to connect the glyphs by aligning two anchor
          points: the designated exit point of a glyph, and the
          designated entry point of the following glyph.</p><p role="">The subtable has one format: CursivePosFormat1. It
          begins with a format identifier (PosFormat) and an offset to
          a Coverage table (Coverage), which lists all the glyphs that
          define cursive attachment data.</p><p role="">In addition, the subtable contains one EntryExitRecord
          for each glyph listed in the Coverage table, a count of
          those records (EntryExitCount), and an array of those
          records in the same order as the Coverage Index
          (EntryExitRecord).</p><div class="table"><a name="idm80803571376"></a><p class="title"><strong>Table 24.11. CursivePosFormat1 subtable: Cursive attachment</strong></p><div class="table-contents"><table role="" class="table" summary="CursivePosFormat1 subtable: Cursive attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
              CursivePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">EntryExitCount</td><td role="">Number of EntryExit records</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">EntryExitRecord [EntryExitCount]</td><td role="">Array of EntryExit records - in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each EntryExitRecord consists of two offsets: one to an
          Anchor table that identifies the entry point on the glyph
          (EntryAnchor), and an offset to an Anchor table that
          identifies the exit point on the glyph (ExitAnchor). (For a
          complete description of the Anchor table, see the end of
          this chapter.)</p><p role="">To position glyphs using the CursivePosFormat1 subtable,
          a text-processing client aligns the ExitAnchor point of a
          glyph with the EntryAnchor point of the following glyph. If
          no corresponding anchor point exists, either the EntryAnchor
          or ExitAnchor offset may be NULL.</p><p role="">At the end of this chapter, Example 6 describes cursive
          glyph attachment in the Urdu language.</p><div class="table"><a name="idm80803560720"></a><p class="title"><strong>Table 24.12. EntryExitRecord</strong></p><div class="table-contents"><table role="" class="table" summary="EntryExitRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">EntryAnchor</td><td role="">Offset to EntryAnchor table-from beginning of
              CursivePos subtable-may be NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ExitAnchor</td><td role="">Offset to ExitAnchor table-from beginning of
              CursivePos subtable-may be NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.9.2"></a>Annotation</h3></div></div></div><p role="">The specification indicates that under some
          circumstances, the ExitAnchor point of one glyph is aligned
          with the EntryAnchor of another. But it does not define
          “align” in any way: does it mean the two
          points are made to coincide, or that they are made to be on
          the same horizontal or vertical line? And what is moved to
          achieve that: the first glyph, the second glyph, both? What
          about the glyphs following the second one? The example may
          help those of you familiar with Urdu, but is otherwise
          unhelpful.</p><p role="">In this implementation, we assume that the second glyph
	  is moved such that the anchors coincide, and none of the
	  glyphs following the second glyph, nor any of the glyphs
	  skipped by lookupFlag between the first and second glyph
	  are moved.</p><p role="">We also assume that the input context is the first
	  glyph, meaning that the next glyph to process is the glyph
	  following the first glyph. The alternative is to make both
	  glyphs in the input context, but that would mean that the
	  second glyph could not be the first component of another
	  cursive attachment.</p><p role="">[All this is obviously wrong, but I need more work to
	  figure out how this lookup type really works.]</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80795145440"></a>Lookup Type 4: MarkToBase Attachment Positioning Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.10.1"></a>Specification</h3></div></div></div><p role="">The MarkToBase attachment (MarkBasePos) subtable is used
          to position combining mark glyphs with respect to base
          glyphs. For example, the Arabic, Hebrew, and Thai scripts
          combine vowels, diacritical marks, and tone marks with base
          glyphs.</p><p role="">In the MarkBasePos subtable, every mark glyph has an
          anchor point and is associated with a class of marks. Each
          base glyph then defines an anchor point for each class of
          marks it uses.</p><p role="">For example, assume two mark classes: all marks
          positioned above base glyphs (Class 0), and all marks
          positioned below base glyphs (Class 1). In this case, each
          base glyph that uses these marks would define two anchor
          points, one for attaching the mark glyphs listed in Class 0,
          and one for attaching the mark glyphs listed in Class
          1.</p><p role="">To identify the base glyph that combines with a mark,
          the text-processing client must look backward in the glyph
          string from the mark to the preceding base glyph. To combine
          the mark and base glyph, the client aligns their attachment
          points, positioning the mark with respect to the final pen
          point (advance) position of the base glyph.</p><p role="">The MarkToBase Attachment subtable has one format:
          MarkBasePosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables:
          one that lists all the mark glyphs referenced in the
          subtable (MarkCoverage), and one that lists all the base
          glyphs referenced in the subtable (BaseCoverage).</p><p role="">For each mark glyph in the MarkCoverage table, a record
          specifies its class and an offset to the Anchor table that
          describes the mark's attachment point (MarkRecord). A mark
          class is identified by a specific integer, called a class
          value. ClassCount specifies the total number of distinct
          mark classes defined in all the MarkRecords.</p><p role="">The MarkBasePosFormat1 subtable also contains an offset
          to a MarkArray table, which contains all the MarkRecords
          stored in an array (MarkRecord) by MarkCoverage Index. A
          MarkArray table also contains a count of the defined
          MarkRecords (MarkCount). (For details about MarkArrays and
          MarkRecords, see the end of this chapter.)</p><p role="">The MarkBasePosFormat1 subtable also contains an offset
          to a BaseArray table (BaseArray).</p><div class="table"><a name="idm80795137936"></a><p class="title"><strong>Table 24.13. MarkBasePosFormat1 subtable: MarkToBase attachment point</strong></p><div class="table-contents"><table role="" class="table" summary="MarkBasePosFormat1 subtable: MarkToBase attachment point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier –format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkCoverage</td><td role="">Offset to MarkCoverage table – from beginning
              of MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BaseCoverage</td><td role="">Offset to BaseCoverage table – from beginning
              of MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ClassCount</td><td role="">Number of classes defined for
              marks</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkArray</td><td role="">Offset to MarkArray table – from beginning of
              MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BaseArray</td><td role="">Offset to BaseArray table – from beginning of
              MarkBasePos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The BaseArray table consists of an array (BaseRecord)
          and count (BaseCount) of BaseRecords. The array stores the
          BaseRecords in the same order as the BaseCoverage Index.
          Each base glyph in the BaseCoverage table has a
          BaseRecord.</p><div class="table"><a name="idm80795125440"></a><p class="title"><strong>Table 24.14. BaseArray table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseCount</td><td role="">Number of BaseRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">BaseRecord [BaseCount]</td><td role="">Array of BaseRecords – in order of BaseCoverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A BaseRecord declares one Anchor table for each mark
          class (including Class 0) identified in the MarkRecords of
          the MarkArray. Each Anchor table specifies one attachment
          point used to attach all the marks in a particular class to
          the base glyph. A BaseRecord contains an array of offsets to
          Anchor tables (BaseAnchor). The zero-based array of offsets
          defines the entire set of attachment points each base glyph
          uses to attach marks. The offsets to Anchor tables are
          ordered by mark class.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Anchor tables are not tagged with class value
            identifiers. Instead, the index value of an Anchor table
            in the array defines the class value represented by the
            Anchor table.</p></blockquote></div><p role="">Example 7 at the end of this chapter defines mark
          positioning above and below base glyphs with a
          MarkBasePosFormat1 subtable.</p><div class="table"><a name="idm80795117552"></a><p class="title"><strong>Table 24.15. BaseRecord</strong></p><div class="table-contents"><table role="" class="table" summary="BaseRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">BaseAnchor [ClassCount]</td><td role="">Array of offsets (one per class) to Anchor
              tables – from beginning of BaseArray table
	      – ordered by class – zero-based</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.10.2"></a>Annotation</h3></div></div></div><p role="">The 'text-processing' client refered to in the fourth
          paragraph is misleading. What is really meant here is "the
          virtual machine that executes the GPOS program".</p><p role="">The pointer to the details of MarkArrays and MarkRecords
	  should be hyperlinked.</p><p role="">It is important to realize that a MarkToBase subtable
          applies to the mark glyph, not to the base glyph; the
          subtable will apply at a position in a glyph run only if the
          glyph occurrence at that position is covered by the
          MarkCoverage.</p><p role="">It is unclear whether the mark glyph must also be
          defined as a mark glyph in GlyphClassDef in
          <a role="" class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>. The specification of GDEF says that
          the GDEF is optional, and hints that its content can be
          recreated from the GSUB and GPOS tables. Doing so opens a
          can of worms: it seems that all the glyphs listed in
          MarkCoverage of a MarkToBase subtable should be made part of
          class 3, and that all the BaseCoverage glyphs should be made
          part of class 1 or 2; but what if a glyph appears in the
          MarkCoverage of one subtable and in the BaseCoverage of
          another? The safest road seems to impose the presence of a
          GDEF table (at least whenever there is a MarkToBase table),
          the presence of a GlyphClassDef in it, and the constraint
          that all the glyphs in MarkCoverage be in class 3.</p><p role="">The same question applies to the glyphs listed in the
          BaseCoverage. Again, we suggest that those glyphs should be
          required to be in class 1 or 2 in GlyphClassDef.</p><p role="">The determination of the base glyph needs to be
          elaborated a little bit. In this document, we assume that
          the following was intended:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">The base glyph occurrence which may combine with the
            mark glyph occurrence is the closest preceeding occurrence
            of a glyph which does not belong to class 3 under the
            <a role="" class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> GlyphClassDef. To determine the
            base glyph occurrence, the MarkCoverage and BaseCoverage
            are not used (it is possible that this subtable is
            concerned only with some pairs of base/mark glyphs; that
            should not affect the determination of the base glyph to
            which the mark applies). If there is no base
            glyph occurrence before the current position (because
            there the current position is the first one in the glyph
            run, or all the preceeding occurrences are of mark
            glyphs), the lookup subtable does not apply. Having so
            determined the base glyph, the lookup subtable applies
            only if that base glyph is covered by BaseCoverage;
            otherwise processing continues with the next subtable in
            the lookup.</p></blockquote></div><p role="">The change to the glyph run should also be elaborated a
          bit. In this document, we assume that the following was
          intended:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">When it has been determined that the subtable applies
            to a base glyph occurrence and a mark glyph occurrence, the
            position of mark glyph occurrence is changed so that the
            anchor point of the mark glyph occurrence coincides with
            the relevant anchor point of the base glyph occurrence
            (that is, the anchor point for the mark class to which the
            mark glyph belongs). The positions of the other glyphs
            (including the glyph occurrences between the base glyph
            occurrence and the mark glyph occurrence) are
            unchanged.</p></blockquote></div><p role="">It is worth noting that the adjustement to the position
          of the mark glyph occurrence is a one-time deal. In other
          words, the coincidence of the anchor points is established
          at the time the lookup subtable is applied, but is not
          necessarily preserved by other lookps applied after this
          one.</p><p role="">The case of multiple mark glyphs on a single base glyphs
          could be noted:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Consider a typical case of Latin diacritics,
            where the combining accents are mark glyphs, the letters
            are base glyphs, and a MarkToBase lookup is coded to place
            the accents just above the letters. For simplicity, we
            assume that there is a single class of mark glyphs. If the
            glyph run contains multiple accents that applies to a
            single letter, the net effect of the MarkToBase lookup is to
            move all the accents such that the letter anchor and all
            accents anchors coincide; the accents will
            visually collide. Typically, the font will also contain a
            MarkToMark feature, which will then space apart the
            accents, to achieve the desired result.</p></blockquote></div><p role="">The pattern matched by this subtable is B (L|NB)*
	  ▶ M ◀, where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">B is {x | x ∈ BaseCoverage ∧
		GDEF.GlyphClassDef (x) ≠ 3} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">NB is {x | GDEF.GlyphClassDef (x) = 3}</p></li><li role="" class="listitem"><p role="">M is MarkCoverage ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">The action is to move the glyph matched by M. More
	  precisely, if m is the glyph matched by M and b is the glyph
	  matched by B, then m is moved such that its anchor
	  MarkArray.MarkRecord[MarkCoverage [m]].MarkAnchor coincides
	  with the anchor BaseArray.BaseRecord [BaseCoverage
	  [b]].BaseAnchor [MarkArray.MarkRecord[m].Class] of b.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80795094800"></a>Lookup Type 5: MarkToLigature Attachment Positioning
        Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.11.1"></a>Specification</h3></div></div></div><p role="">The MarkToLigature attachment (MarkLigPos) subtable is
          used to position combining mark glyphs with respect to
          ligature base glyphs. With MarkToBase attachment, described
          previously, a single base glyph defines an attachment point
          for each class of marks. In contrast, MarkToLigature
          attachment describes ligature glyphs composed of several
          components that can each define an attachment point for each
          class of marks.</p><p role="">As a result, a ligature glyph may have multiple base
          attachment points for one class of marks. The specific
          attachment point for a mark is defined by the ligature
          component that the subtable associates with the mark.</p><p role="">The MarkLigPos subtable can be used to define multiple
          mark-to-ligature attachments. In the subtable, every mark
          glyph has an anchor point and is associated with a class of
          marks. Every ligature glyph specifies a two-dimensional
          array of data: each component in a ligature defines an array
          of anchor points, one for each class of marks.</p><p role="">For example, assume two mark classes: all marks
          positioned above base glyphs (Class 0), and all marks
          positioned below base glyphs (Class 1). In this case, each
          component of a base ligature glyph may define two anchor
          points, one for attaching the mark glyphs listed in Class 0,
          and one for attaching the mark glyphs listed in Class 1.
          Alternatively, if the language system does not allow marks
          on the second component, the first ligature component may
          define two anchor points, one for each class of marks, and
          the second ligature component may define no anchor
          points.</p><p role="">To position a combining mark using a MarkToLigature
          attachment subtable, the text-processing client must work
          backward from the mark to the preceding ligature glyph. To
          correctly access the subtables, the client must keep track
          of the component associated with the mark. Aligning the
          attachment points combines the mark and ligature.</p><p role="">The MarkToLigature attachment subtable has one format:
          MarkLigPosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables
          that list all the mark glyphs (MarkCoverage) and Ligature
          glyphs (LigatureCoverage) referenced in the subtable.</p><p role="">For each glyph in the MarkCoverage table, a MarkRecord
          specifies its class and an offset to the Anchor table that
          describes the mark's attachment point. A mark class is
          identified by a specific integer, called a class value.
          ClassCount records the total number of distinct mark classes
          defined in all MarkRecords.</p><p role="">The MarkLigPosFormat1 subtable contains an offset,
          measured from the beginning of the subtable, to a MarkArray
          table, which contains all MarkRecords stored in an array
          (MarkRecord) by MarkCoverage Index. (For details about
          MarkArrays and MarkRecords, see the end of this
          chapter.)</p><p role="">The MarkLigPosFormat1 subtable also contains an offset
          to a LigatureArray table (LigatureArray).</p><div class="table"><a name="idm80795086128"></a><p class="title"><strong>Table 24.16. MarkLigPosFormat1 subtable: MarkToLigature attachment</strong></p><div class="table-contents"><table role="" class="table" summary="MarkLigPosFormat1 subtable: MarkToLigature attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkCoverage</td><td role="">Offset to Mark Coverage table – from beginning
              of MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigatureCoverage</td><td role="">Offset to Ligature Coverage table – from
              beginning of MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ClassCount</td><td role="">Number of defined mark classes</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkArray</td><td role="">Offset to MarkArray table – from beginning of
              MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigatureArray</td><td role="">Offset to LigatureArray table – from beginning
              of MarkLigPos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The LigatureArray table contains a count (LigatureCount)
          and an array of offsets (LigatureAttach) to LigatureAttach
          tables. The LigatureAttach array lists the offsets to</p><p role="">LigatureAttach tables, one for each ligature glyph
          listed in the LigatureCoverage table, in the same order as
          the LigatureCoverage Index.</p><div class="table"><a name="idm80795073152"></a><p class="title"><strong>Table 24.17. LigatureArray table</strong></p><div class="table-contents"><table role="" class="table" summary="LigatureArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">LigatureCount</td><td role="">Number of LigatureAttach table
              offsets</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigatureAttach [LigatureCount]</td><td role="">Array of offsets to LigatureAttach
              tables – from beginning of LigatureArray table – ordered by
              LigatureCoverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each LigatureAttach table consists of an array
          (ComponentRecord) and count (ComponentCount) of the
          component glyphs in a ligature. The array stores the
          ComponentRecords in the same order as the components in the
          ligature. The order of the records also corresponds to the
          writing direction of the text. For text written left to
          right, the first component is on the left; for text written
          right to left, the first component is on the right.</p><div class="table"><a name="idm80795066656"></a><p class="title"><strong>Table 24.18. LigatureAttach table</strong></p><div class="table-contents"><table role="" class="table" summary="LigatureAttach table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ComponentCount</td><td role="">Number of ComponentRecords in this
              ligature</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">ComponentRecord [ComponentCount]</td><td role="">Array of Component records – ordered in writing
              direction</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A ComponentRecord, one for each component in the
          ligature, contains an array of offsets to the Anchor tables
          that define all the attachment points used to attach marks
          to the component (LigatureAnchor). For each mark class
          (including Class 0) identified in the MarkArray records, an
          Anchor table specifies the point used to attach all the
          marks in a particular class to the ligature base glyph,
          relative to the component.</p><p role="">In a ComponentRecord, the zero-based LigatureAnchor
          array lists offsets to Anchor tables by mark class. If a
          component does not define an attachment point for a
          particular class of marks, then the offset to the
          corresponding Anchor table will be NULL.</p><p role="">Example 8 at the end of this chapter shows a
          MarkLisPosFormat1 subtable used to attach mark accents to a
          ligature glyph in the Arabic script.</p><div class="table"><a name="idm80795059056"></a><p class="title"><strong>Table 24.19. ComponentRecord</strong></p><div class="table-contents"><table role="" class="table" summary="ComponentRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">LigatureAnchor [ClassCount]</td><td role="">Array of offsets (one per class) to Anchor
            tables – from beginning of LigatureAttach table
            – ordered by class – NULL if a component
            does not have an attachment for a class –
            zero-based array</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.11.2"></a>Annotation</h3></div></div></div><p role="">The 'text-processing' client refered to in the fifth
          paragraph is misleading. What is really meant here is "the
          virtual machine that executes the GPOS program".</p><p role="">It is important to realize that a MarkToLigature subtable
          applies to the mark glyph, not to the ligature glyph; the
          subtable will apply at a position in a glyph run only if the
          glyph occurrence at that position is covered by the
          MarkCoverage.</p><p role="">It is unclear whether the mark glyph must also be
          defined as a mark glyph in GlyphClassDef in
          <a role="" class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>. The specification of GDEF says that
          the GDEF is optional, and hints that its content can be
          recreated from the GSUB and GPOS tables. Doing so opens a
          can of worms: it seems that all the glyphs listed in
          MarkCoverage of a MarkToLigature subtable should be made part of
          class 3, and that all the LigatureCoverage glyphs should be made
          part of class 1 or 2; but what if a glyph appears in the
          MarkCoverage of one subtable and in the LigatureCoverage of
          another? The safest road seems to impose the presence of a
          GDEF table (at least whenever there is a MarkToLigature table),
          the presence of a GlyphClassDef in it, and the constraint
          that all the glyphs in MarkCoverage be in class 3.</p><p role="">The same question applies to the glyphs listed in the
          LigatureCoverage. Again, we suggest that those glyphs should be
          required to be in class 1 or 2 in GlyphClassDef.</p><p role="">The determination of the ligature glyph needs to be
          elaborated a little bit. In this document, we assume that
          the following was intended:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">The ligature glyph occurrence which may combine with the
            mark glyph occurrence is the closest preceeding occurrence
            of a glyph which does not belong to class 3 under the
            <a role="" class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> GlyphClassDef. To determine the
            ligature glyph occurrence, the MarkCoverage and LigatureCoverage
            are not used (it is possible that this subtable is
            concerned only with some pairs of ligature/mark glyphs; that
            should not affect the determination of the ligature glyph to
            which the mark applies).
            If there is no ligature
            glyph occurrence before the current position (because
            there the current position is the first one in the glyph
            run, or all the preceeding occurrences are of mark
            glyphs), the lookup subtable does not apply. Having so
            determined the ligature glyph, the lookup subtable applies
            only if that ligature glyph is covered by LigatureCoverage;
            otherwise processing continues with the next subtable in
            the lookup.</p></blockquote></div><p role="">The change to the glyph run should also be elaborated a
          bit. In this document, we assume that the following was
          intended:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">When it has been determined that the subtable applies
            to a ligature glyph occurrence and a mark glyph occurrence, the
            position of mark glyph occurrence is changed so that the
            anchor point of the mark glyph occurrence coincides with
            the relevant anchor point of the ligature glyph occurrence
            (that is, the anchor point for the mark class to which the
            mark glyph belongs). The positions of the other glyphs
            (including the glyph occurrences between the ligature glyph
            occurrence and the mark glyph occurrence) are
            unchanged.</p></blockquote></div><p role="">It is worth noting that the adjustement to the position
          of the mark glyph occurrence is a one-time deal. In other
          words, the coincidence of the anchor points is established
          at the time the lookup subtable is applied, but is not
          necessarily preserved by other lookps applied after this
          one.</p><p role="">The case of multiple mark glyphs on a single ligature glyphs
          could be noted:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Consider a typical case of Latin diacritics,
            where the combining accents are mark glyphs, the letters
            are ligature glyphs, and a MarkToLigature lookup is coded to place
            the accents just above the letters. For simplicity, we
            assume that there is a single class of mark glyphs. If the
            glyph run contains multiple accents that applies to a
            single letter, the net effect of the MarkToLigature lookup is to
            move all the accents such that the letter anchor and all
            accents anchors coincide; the accents will
            visually collide. Typically, the font will also contain a
            MarkToMark feature, which will then space apart the
            accents, to achieve the desired result.</p></blockquote></div><p role="">The pattern matched by this subtable is B (L|NB)*
	  ▶ M ◀, where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">B is {x | x ∈ LigatureCoverage ∧
		GDEF.GlyphClassDef (x) ≠ 3} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">NB is {x | GDEF.GlyphClassDef (x) = 3}</p></li><li role="" class="listitem"><p role="">M is MarkCoverage ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">The action is to move the glyph matched by M. More
	  precisely, if m is the glyph matched by M, b is the glyph
	  matched by B and c is the ligature component to which the
	  mark should be attached, then m is moved such that its anchor
	  MarkArray.MarkRecord[MarkCoverage [m]].MarkAnchor coincides
	  with the anchor LigatureArray.LigatureAttach [LigatureCoverage
	  [b]].ComponentRecord [c].LigatureAnchor
	  [MarkArray.MarkRecord[m].Class] of b. It is up to the client
	  to determine to which component the mark should be attached.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80795037200"></a>Lookup Type 6: MarkToMark Attachment Positioning
        Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.12.1"></a>Specification</h3></div></div></div><p role="">The MarkToMark attachment (MarkMarkPos) subtable is
          identical in form to the MarkToBase attachment subtable,
          although its function is different. MarkToMark attachment
          defines the position of one mark relative to another mark as
          when, for example, positioning tone marks with respect to
          vowel diacritical marks in Vietnamese.</p><p role="">The attaching mark is Mark1, and the base mark being
          attached to is Mark2. In the MarkMarkPos subtable, every
          Mark1 glyph has an anchor attachment point and is associated
          with a class of marks. Each Mark2 glyph defines an anchor
          point for each class of marks. For example, assume two Mark1
          classes: all marks positioned to the left of Mark2 glyphs
          (Class 0), and all marks positioned to the right of Mark2
          glyphs (Class 1). Each Mark2 glyph that uses these marks
          defines two anchor points: one for attaching the Mark1
          glyphs listed in Class 0, and one for attaching the Mark1
          glyphs listed in Class 1.</p><p role="">The Mark2 glyph that combines with a Mark1 glyph is the
	  glyph preceding the Mark1 glyph in glyph string order
	  (skipping glyphs according to LookupFlag). The subtable
	  applies precisely when that Mark2 glyph is covered by
	  Mark2Coverage. To combine the mark glyphs, the Mark1 glyph
	  is moved such that the relevant attachment points
	  coincide. The input context for MarkToBase, MarkToLigature
	  and MarkToMark positioning tables is the mark that is being
	  positioned. If a sequence contains several marks, a lookup
	  may act on it several times, to position them.</p><p role="">The MarkToMark attachment subtable has one format:
          MarkMarkPosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables:
          one that lists all the Mark1 glyphs referenced in the
          subtable (Mark1Coverage), and one that lists all the Mark2
          glyphs referenced in the subtable (Mark2Coverage).</p><p role="">For each mark glyph in the Mark1Coverage table, a
          MarkRecord specifies its class and an offset to the Anchor
          table that describes the mark's attachment point. A mark
          class is identified by a specific integer, called a class
          value. (For details about classes, see the chapter, Common
          Table Formats.) ClassCount specifies the total number of
          distinct mark classes defined in all the MarkRecords.</p><p role="">The MarkMarkPosFormat1 subtable also contains two
          offsets, measured from the beginning of the subtable, to two
          arrays:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The MarkArray table contains all MarkRecords stored
              by Mark1Coverage Index in an array (MarkRecord). The
              MarkArray table also contains a count of the number of
              defined MarkRecords (MarkCount).</p></li><li role="" class="listitem"><p role="">The Mark2Array table consists of an array
              (Mark2Record) and count (Mark2Count) of
              Mark2Records.</p></li></ul></div><p role="">For details about MarkArrays and MarkRecords, see the
          end of this chapter.</p><div class="table"><a name="idm80795027584"></a><p class="title"><strong>Table 24.20. MarkMarkPosFormat1 subtable: MarkToMark attachment</strong></p><div class="table-contents"><table role="" class="table" summary="MarkMarkPosFormat1 subtable: MarkToMark attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Mark1Coverage</td><td role="">Offset to Combining Mark Coverage table-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Mark2Coverage</td><td role="">Offset to Base Mark Coverage table-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ClassCount</td><td role="">Number of Combining Mark classes
              defined</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Mark1Array</td><td role="">Offset to MarkArray table for Mark1-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Mark2Array</td><td role="">Offset to Mark2Array table for Mark2-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The Mark2Array, shown next, contains one Mark2Record for
          each Mark2 glyph listed in the Mark2Coverage table. It
          stores the records in the same order as the Mark2Coverage
          Index.</p><div class="table"><a name="idm80796766272"></a><p class="title"><strong>Table 24.21. Mark2Array table</strong></p><div class="table-contents"><table role="" class="table" summary="Mark2Array table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">Mark2Count</td><td role="">Number of Mark2 records</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">Mark2Record [Mark2Count]</td><td role="">Array of Mark2 records-in Coverage
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each Mark2Record contains an array of offsets to Anchor
          tables (Mark2Anchor). The array of zero-based offsets,
          measured from the beginning of the Mark2Array table, defines
          the entire set of Mark2 attachment points used to attach
          Mark1 glyphs to a specific Mark2 glyph. The Anchor tables in
          the Mark2Anchor array are ordered by Mark1 class
          value.</p><p role="">A Mark2Record declares one Anchor table for each mark
          class (including Class 0) identified in the MarkRecords of
          the MarkArray. Each Anchor table specifies one Mark2
          attachment point used to attach all the Mark1 glyphs in a
          particular class to the Mark2 glyph.</p><p role="">Example 9 at the end of the chapter shows a
          MarkMarkPosFormat1 subtable for attaching one mark to
          another in the Arabic script.</p><div class="table"><a name="idm80796758912"></a><p class="title"><strong>Table 24.22. Mark2Record</strong></p><div class="table-contents"><table role="" class="table" summary="Mark2Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">Mark2Anchor [ClassCount]</td><td role="">Array of offsets (one per class) to Anchor
              tables-from beginning of Mark2Array table-zero-based
              array</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.12.2"></a>Annotation</h3></div></div></div><p role="">The annotation of the Mark2Record field should probably
	  be "... in Mark2Coverage order".</p><p role="">The pattern matched by this subtable is M2 L* ▶
	  M1 ◀, where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">M2 is {x | x ∈ Mark2Coverage ∧
		GDEF.GlyphClassDef (x) = 3} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">M1 is Mark1Coverage ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">The action is to move the glyph matched by M1. More
	  precisely, if m1 is the glyph matched by M1, m2 is the glyph
	  matched by M2, then m1 is moved such that its anchor
	  Mark1Array.MarkRecord [MarkCoverage [m]].MarkAnchor coincides
	  with the anchor Mark2Array.Mark2Record [Mark2Coverage
	  [m2]].Mark2Anchor [Mark1Array.MarkRecord[m].Class] of m2.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796748608"></a>Lookup Type 7: Contextual Positioning Subtables</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.13.1"></a>Specification</h3></div></div></div><p role="">A Contextual Positioning (ContextPos) subtable defines
          the most powerful type of glyph positioning lookup. It
          describes glyph positioning in context so a text-processing
          client can adjust the position of one or more glyphs within
          a certain pattern of glyphs. Each subtable describes one or
          more "input" glyph sequences and one or more positioning
          operations to be performed on that sequence.</p><p role="">ContextPos subtables can have one of three formats,
          which closely mirror the formats used for contextual glyph
          substitution. One format applies to specific glyph sequences
          (Format 1), one defines the context in terms of glyph
          classes (Format 2), and the third format defines the context
          in terms of sets of glyphs (Format 3).</p><p role="">All ContextPos subtables specify positioning data in a
          PosLookupRecord. A description of that record follows.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796744080"></a>PosLookupRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.14.1"></a>Specification</h3></div></div></div><p role="">All contextual positioning subtables specify the
          positioning data in a PosLookupRecord. Each record contains
          a SequenceIndex, which indicates where the positioning
          operation will occur in the glyph sequence. In addition, a
          LookupListIndex identifies the lookup to be applied at the
          glyph position specified by the SequenceIndex.</p><p role="">The order in which lookups are applied to the entire
          glyph sequence, called the "design order," can be
          significant, so PosLookupRecord data should be defined
          accordingly.</p><p role="">The contextual substitution subtables defined in
          Examples 10, 11, and 12 show PosLookupRecords.</p><div class="table"><a name="idm80796740416"></a><p class="title"><strong>Table 24.23. PosLookupRecord</strong></p><div class="table-contents"><table role="" class="table" summary="PosLookupRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SequenceIndex</td><td role="">Index to input glyph sequence-first glyph =
              0</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookupListIndex</td><td role="">Lookup to apply to that
              position-zero-based</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796734528"></a>Context Positioning Subtable: Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.15.1"></a>Specification</h3></div></div></div><p role="">Format 1 defines the context for a glyph positioning
          operation as a particular sequence of glyphs. For example, a
          context could be &lt;To&gt;, &lt;xyzabc&gt;, &lt;!?*#@&gt;, or any
          other glyph sequence.</p><p role="">Within the context, Format 1 identifies particular glyph
          positions (not glyph indices) as the targets for specific
          adjustments. When a text-processing client locates a context
          in a string of text, it makes the adjustment by applying the
          lookup data defined for a targeted position at that
          location.</p><p role="">For example, suppose that accent mark glyphs above
          lowercase x-height vowel glyphs must be lowered when an
          overhanging capital letter glyph precedes the vowel. When
          the client locates this context in the text, the subtable
          identifies the position of the accent mark and a lookup
          index. A lookup specifies a positioning action that lowers
          the accent mark over the vowel so that it does not collide
          with the overhanging capital.</p><p role="">ContextPosFormat1 defines the context in two places. A
          Coverage table specifies the first glyph in the input
          sequence, and a PosRule table identifies the remaining
          glyphs. To describe the context used in the previous
          example, the Coverage table lists the glyph index of the
          first component of the sequence (the overhanging capital),
          and a PosRule table defines indices for the lowercase
          x-height vowel glyph and the accent mark.</p><p role="">A single ContextPosFormat1 subtable may define more than
          one context glyph sequence. If different context sequences
          begin with the same glyph, then the Coverage table should
          list the glyph only once because all first glyphs in the
          table must be unique. For example, if three contexts each
          start with an "s" and two start with a "t," then the
          Coverage table will list one "s" and one "t."</p><p role="">For each context, a PosRule table lists all the glyphs,
          in order, that follow the first glyph. The table also
          contains an array of PosLookupRecords that specify the
          positioning lookup data for each glyph position (including
          the first glyph position) in the context.</p><p role="">All the PosRule tables defining contexts that begin with
          the same first glyph are grouped together and defined in a
          PosRuleSet table. For example, the PosRule tables that
          define the three contexts that begin with an "s" are grouped
          in one PosRuleSet table, and the PosRule tables that define
          the two contexts that begin with a "t" are grouped in a
          second PosRuleSet table. Each unique glyph listed in the
          Coverage table must have a PosRuleSet table that defines all
          the PosRule tables for a covered glyph.</p><p role="">To locate a context glyph sequence, the text-processing
          client searches the Coverage table each time it encounters a
          new text glyph. If the glyph is covered, the client reads
          the corresponding PosRuleSet table and examines each PosRule
          table in the set to determine whether the rest of the
          context defined there matches the subsequent glyphs in the
          text. If the context and text string match, the client finds
          the target glyph position, applies the lookup for that
          position, and completes the positioning action.</p><p role="">A ContextPosFormat1 subtable contains a format
          identifier (PosFormat), an offset to a Coverage table
          (Coverage), a count of the number of PosRuleSets that are
          defined (PosRuleSetCount), and an array of offsets to the
          PosRuleSet tables (PosRuleSet). As mentioned, one PosRuleSet
          table must be defined for each glyph listed in the Coverage
          table.</p><p role="">In the PosRuleSet array, the PosRuleSet tables are
          ordered in the Coverage Index order. The first PosRuleSet in
          the array applies to the first GlyphID listed in the
          Coverage table, the second PosRuleSet in the array applies
          to the second GlyphID listed in the Coverage table, and so
          on.</p><div class="table"><a name="idm80796724416"></a><p class="title"><strong>Table 24.24. ContextPosFormat1 subtable: Simple context positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ContextPosFormat1 subtable: Simple context positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosRuleSetCount</td><td role="">Number of PosRuleSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">PosRuleSet [PosRuleSetCount]</td><td role="">Array of offsets to PosRuleSet tables-from
              beginning of ContextPos subtable-ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A PosRuleSet table consists of an array of offsets to
          PosRule tables (PosRule), ordered by preference, and a count
          of the PosRule tables defined in the set
          (PosRuleCount).</p><div class="table"><a name="idm80796715392"></a><p class="title"><strong>Table 24.25. PosRuleSet table: All contexts beginning with the
            same glyph</strong></p><div class="table-contents"><table role="" class="table" summary="PosRuleSet table: All contexts beginning with the&#10;            same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosRuleCount</td><td role="">Number of PosRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">PosRule [PosRuleCount]</td><td role="">Array of offsets to PosRule tables-from
              beginning of PosRuleSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A PosRule table consists of a count of the glyphs to be
          matched in the input context sequence (GlyphCount),
          including the first glyph in the sequence, and an array of
          glyph indices that describe the context (Input). The
          Coverage table specifies the index of the first glyph in the
          context, and the Input array begins with the second glyph in
          the context sequence. As a result, the first index position
          in the array is specified with the number one (1), not zero
          (0). The Input array lists the indices in the order the
          corresponding glyphs appear in the text. For text written
          from right to left, the right-most glyph will be first;
          conversely, for text written from left to right, the
          left-most glyph will be first.</p><p role="">A PosRule table also contains a count of the positioning
          operations to be performed on the input glyph sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord). Each record specifies a position in the
          input glyph sequence and a LookupList index to the
          positioning lookup to be applied there. The array should
          list records in design order, or the order the lookups
          should be applied to the entire glyph sequence.</p><p role="">Example 10 at the end of this chapter demonstrates glyph
          kerning in context with a ContextPosFormat1 subtable.</p><div class="table"><a name="idm80796707328"></a><p class="title"><strong>Table 24.26. PosRule subtable</strong></p><div class="table-contents"><table role="" class="table" summary="PosRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs in the Input glyph
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Input [GlyphCount-1]</td><td role="">Array of input GlyphIDs-starting with the
              second glyph</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [PosCount]</td><td role="">Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.15.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by the PosRule table t = PosRuleSet
	  [m].PosRule [n] is ▶
	  I<sub>0</sub> L* I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is t.GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is {t.Input [k-1]}
	      ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A PosRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796690512"></a>Context Positioning Subtable: Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.16.1"></a>Specification</h3></div></div></div><p role="">Format 2, more flexible than Format 1, describes
          class-based context positioning. For this format, a specific
          integer, called a class value, must be assigned to each
          glyph in all context glyph sequences. Contexts are then
          defined as sequences of class values. This subtable may
          define more than one context.</p><p role="">To clarify the notion of class-based context rules,
          suppose that certain sequences of three glyphs need special
          kerning. The glyph sequences consist of an uppercase glyph
          that overhangs on the right side, a punctuation mark glyph,
          and then a quote glyph. In this case, the set of uppercase
          glyphs would constitute one glyph class (Class1), the set of
          punctuation mark glyphs would constitute a second glyph
          class (Class 2), and the set of quote mark glyphs would
          constitute a third glyph class (Class 3). The input context
          might be specified with a context rule (PosClassRule) that
          describes "the set of glyph strings that form a sequence of
          three glyph classes, one glyph from Class 1, followed by one
          glyph from Class 2, followed by one glyph from Class
          3."</p><p role="">Each ContextPosFormat2 subtable contains an offset to a
          class definition table (ClassDef), which defines the class
          values of all glyphs in the input contexts that the subtable
          describes. Generally, a unique ClassDef will be declared in
          each instance of the ContextPosFormat2 subtable that is
          included in a font, even though several Format 2 subtables
          may share ClassDef tables. Classes are exclusive sets; a
          glyph cannot be in more than one class at a time. The output
          glyphs that replace the glyphs in the context sequence do
          not need class values because they are specified elsewhere
          by GlyphID.</p><p role="">The ContextPosFormat2 subtable also contains a format
          identifier (PosFormat) and defines an offset to a Coverage
          table (Coverage). For this format, the Coverage table lists
          indices for the complete set of glyphs (not glyph classes)
          that may appear as the first glyph of any class-based
          context. In other words, the Coverage table contains the
          list of glyph indices for all the glyphs in all classes that
          may be first in any of the context class sequences. For
          example, if the contexts begin with a Class 1 or Class 2
          glyph, then the Coverage table will list the indices of all
          Class 1 and Class 2 glyphs.</p><p role="">A ContextPosFormat2 subtable also defines an array of
          offsets to the PosClassSet tables (PosClassSet), along with
          a count (including Class0) of the PosClassSet tables
          (PosClassSetCnt). In the array, the PosClassSet tables are
          ordered by ascending class value (from 0 to PosClassSetCnt -
          1).</p><p role="">A PosClassSet array contains one offset for each glyph
          class, including Class 0. PosClassSets are not explicitly
          tagged with a class value; rather, the index value of the
          PosClassSet in the PosClassSet array defines the class that
          a PosClassSet represents.</p><p role="">For example, the first PosClassSet listed in the array
          contains all the PosClassRules that define contexts
          beginning with Class 0 glyphs, the second PosClassSet
          contains all PosClassRules that define contexts beginning
          with Class 1 glyphs, and so on. If no PosClassRules begin
          with a particular class (that is, if a PosClassSet contains
          no PosClassRules), then the offset to that particular
          PosClassSet in the PosClassSet array will be set to
          NULL.</p><div class="table"><a name="idm80796682720"></a><p class="title"><strong>Table 24.27. ContextPosFormat2 subtable: Class-based context glyph positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ContextPosFormat2 subtable: Class-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ClassDef</td><td role="">Offset to ClassDef table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosClassSetCnt</td><td role="">Number of PosClassSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">PosClassSet [PosClassSetCnt]</td><td role="">Array of offsets to PosClassSet tables-from
              beginning of ContextPos subtable-ordered by class-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">All the PosClassRules that define contexts beginning
          with the same class are grouped together and defined in a
          PosClassSet table. Consequently, the PosClassSet table
          identifies the class of a context's first component.</p><p role="">A PosClassSet enumerates all the PosClassRules that
          begin with a particular glyph class. For instance,
          PosClassSet0 represents all the PosClassRules that describe
          contexts starting with Class 0 glyphs, and PosClassSet1
          represents all the PosClassRules that define contexts
          starting with Class 1 glyphs.</p><p role="">Each PosClassSet table consists of a count of the
          PosClassRules defined in the PosClassSet (PosClassRuleCnt)
          and an array of offsets to PosClassRule tables
          (PosClassRule). The PosClassRule tables are ordered by
          preference in the PosClassRule array of the
          PosClassSet.</p><div class="table"><a name="idm80796670752"></a><p class="title"><strong>Table 24.28. PosClassSet table: All contexts beginning with the same class</strong></p><div class="table-contents"><table role="" class="table" summary="PosClassSet table: All contexts beginning with the same class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosClassRuleCnt</td><td role="">Number of PosClassRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">PosClassRule [PosClassRuleCnt]</td><td role="">Array of offsets to PosClassRule tables-from
              beginning of PosClassSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">For each context, a PosClassRule table contains a count
          of the glyph classes in a given context (GlyphCount),
          including the first class in the context sequence. A class
          array lists the classes, beginning with the second class,
          that follow the first class in the context. The first class
          listed indicates the second position in the context
          sequence.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Text order depends on the writing direction of
            the text. For text written from right to left, the
            right-most glyph will be first. Conversely, for text
            written from left to right, the left-most glyph will be
            first.</p></blockquote></div><p role="">The values specified in the Class array are those
          defined in the ClassDef table. For example, consider a
          context consisting of the sequence: Class 2, Class 7, Class
          5, Class 0. The Class array will read: Class[0] = 7,
          Class[1] = 5, and Class[2] = 0. The first class in the
          sequence, Class 2, is defined by the index into the
          PosClassSet array of offsets. The total number and sequence
          of glyph classes listed in the Class array must match the
          total number and sequence of glyph classes contained in the
          input context.</p><p role="">A PosClassRule also contains a count of the positioning
          operations to be performed on the context (PosCount) and an
          array of PosLookupRecords (PosLookupRecord) that supply the
          positioning data. For each position in the context that
          requires a positioning operation, a PosLookupRecord
          specifies a LookupList index and a position in the input
          glyph class sequence where the lookup is applied. The
          PosLookupRecord array lists PosLookupRecords in design
          order, or the order in which lookups are applied to the
          entire glyph sequence.</p><p role="">Example 11 at the end of this chapter demonstrates a
          ContextPosFormat2 subtable that uses glyph classes to modify
          accent positions in glyph strings.</p><div class="table"><a name="idm80796660928"></a><p class="title"><strong>Table 24.29. PosClassRule table: One class context definition</strong></p><div class="table-contents"><table role="" class="table" summary="PosClassRule table: One class context definition" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs to be matched</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Class [GlyphCount-1]</td><td role="">Array of classes-beginning with the second
              class-to be matched to the input glyph
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [PosCount]</td><td role="">Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.16.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by the PosClassRule table t = PosClassSet
	  [m].PosClassRule [n] is
	  ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is t.GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is (Coverage ∩
	      ClassDef [m]) ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is ClassDef [t.Class
	      [k-1]] ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubClassRule table does not directly modify the glyph
	run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796643984"></a>Context Positioning Subtable: Format 3</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.17.1"></a>Specification</h3></div></div></div><p role="">Format 3, coverage-based context positioning, defines a
          context rule as a sequence of coverages. Each position in
          the sequence may specify a different Coverage table for the
          set of glyphs that matches the context pattern. With Format
          3, the glyph sets defined in the different Coverage tables
          may intersect, unlike Format 2 which specifies fixed class
          assignments for the lookup (they cannot be changed at each
          position in the context sequence) and exclusive classes (a
          glyph cannot be in more than one class at a time).</p><p role="">For example, consider an input context that contains an
          uppercase glyph (position 0), followed by any narrow
          uppercase glyph (position 1), and then another uppercase
          glyph (position 2). This context requires three Coverage
          tables, one for each position:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">In position 0, the first position, the Coverage
              table lists the set of all uppercase glyphs.</p></li><li role="" class="listitem"><p role="">In position 1, the second position, the Coverage
              table lists the set of all narrow uppercase glyphs,
              which is a subset of the glyphs listed in the Coverage
              table for position 0. </p></li><li role="" class="listitem"><p role="">In position 2, the Coverage table lists the set of
              all uppercase glyphs again.</p></li></ul></div><p role="">Note: Both position 0 and position 2 can use the same
          Coverage table.</p><p role="">Unlike Formats 1 and 2, this format defines only one
          context rule at a time. It consists of a format identifier
          (PosFormat), a count of the number of glyphs in the sequence
          to be matched (GlyphCount), and an array of Coverage offsets
          that describe the input context sequence (Coverage).</p><p role="">Note: The Coverage tables listed in the Coverage array
          must be listed in text order according to the writing
          direction. For text written from right to left, the
          right-most glyph will be first. Conversely, for text written
          from left to right, the left-most glyph will be
          first.</p><p role="">The subtable also contains a count of the positioning
          operations to be performed on the input Coverage sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord) in design order, or the order in which
          lookups are applied to the entire glyph sequence.</p><p role="">Example 12 at the end of this chapter changes the
          positions of math sign glyphs in math equations with a
          ContextPosFormat3 subtable.</p><div class="table"><a name="idm80796634208"></a><p class="title"><strong>Table 24.30. ContextPosFormat3 subtable: Coverage-based context glyph positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ContextPosFormat3 subtable: Coverage-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs in the input
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [GlyphCount]</td><td role="">Array of offsets to Coverage tables-from
              beginning of ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [PosCount]</td><td role="">Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.17.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by this subtable is ▶
	  I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>i</sub> is
		Coverage [i] ∖ LookupFlag.</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">This table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796617200"></a>Lookup Type 8: Chaining Contextual Positioning Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.18.1"></a>Specification</h3></div></div></div><p role="">A Chaining Contextual Positioning
          subtable(ChainContextPos)describes glyph positioning in
          context with an ability to look back and/or look ahead in
          the sequence of glyphs. The design of the Chaining
          Contextual Positioning subtable is parallel to that of the
          Contextual Positioning subtable, including the availability
          of three formats.</p><p role="">To specify the context, the coverage table lists the
          first glyph in the input sequence, and the ChainPosRule
          subtable defines the rest. Once a covered glyph is found at
          position i, the client reads the corresponding
          ChainPosRuleSet table and examines each table to determine
          if it matches the surrounding glyphs in the text. There is a
          match if the string &lt;backtrack sequence&gt;+&lt;input
          sequence&gt;+&lt;input sequence&gt;+&lt;lookahead sequence&gt; matches
          with the glyphs at position i - BacktrackGlyphCount in the
          text.</p><p role="">If there is a match, then the client finds the target
          glyphs for positioning and performs the operations. Please
          note that (just like in the ContextPosFormat1 subtable)
          these lookups are required to operate within the range of
          text from the covered glyph to the end of the input
          sequence. No positioning operations can be defined for the
          backtracking sequence or the lookahead sequence.</p><p role="">To clarify the ordering of glyph arrays for input,
	  backtrack and lookahead sequences, the following
	  illustration is provided. Input sequence match begins at i
	  where the input sequence match begins. The backtrack
	  sequence is ordered beginning at i-1 and increases in offset
	  value as one moves away from i. The lookahead sequence
	  begins after the input sequence and increases in logical
	  order.</p><div role="" class="literallayout"><p><br/>
Logical order        a   b   c   d   e   f   g   h   i   j<br/>
                                     i<br/>
Input sequence                       0   1<br/>
Backtrack sequence   3   2   1   0<br/>
Lookahead sequence                           0   1   2   3<br/>
</p></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.18.2"></a>Annotation</h3></div></div></div><p role="">In all three formats, the sequences are represented by
	  arrays. The order in those arrays is <span role="" class="emphasis"><em>away from the
	  current position</em></span>. In other words, if
	  <span role="" class="emphasis"><em>i</em></span> is the current position, then the
	  first element of the backtrack array is matched against the
	  glyph at position <span role="" class="emphasis"><em>i-1</em></span> (ignoring glyphs
	  covered by LookupFlag, as usual), and the last element of
	  the backtrack array is matched against the glyph at position
	  <span role="" class="emphasis"><em>i - BacktrackGlyphCount</em></span>. The first
	  element of the lookahead array is matched against the glyph
	  at position <span role="" class="emphasis"><em>i + InputGlyphCount</em></span>, and
	  the last element in that array is matched against the glyph
	  as position <span role="" class="emphasis"><em>i + InputGlyphCount +
	  LookaheadGlyphCount - 1</em></span>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796605376"></a>Chaining Context Positioning Format 1: Simple Chaining
        Context Glyph Positioning</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.19.1"></a>Specification</h3></div></div></div><p role="">This Format is identical to Format 1 of Context
          Positioning lookup except that the PosRule table is replaced
          with a ChainPosRule table. (Correspondingly, the
          ChainPosRuleSet table differs from the PosRuleSet table only
          in that it lists offsets to ChainPosRule subtables instead
          of PosRule tables; and the ChainContextPosFormat1 subtable
          lists offsets to ChainPosRuleSet subtables instead of
          PosRuleSet subtables.)</p><div class="table"><a name="idm80796602608"></a><p class="title"><strong>Table 24.31. ChainContextPosFormat1 subtable: Simple context
            positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextPosFormat1 subtable: Simple context&#10;            positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ChainPosRuleSetCount</td><td role="">Number of ChainPosRuleSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainPosRuleSet [ChainPosRuleSetCount]</td><td role="">Array of offsets to ChainPosRuleSet tables-from
              beginning of ContextPos subtable-ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A ChainPosRuleSet table consists of an array of offsets
          to ChainPosRule tables (ChainPosRule), ordered by
          preference, and a count of the ChainPosRule tables defined
          in the set (ChainPosRuleCount).</p><div class="table"><a name="idm80796593488"></a><p class="title"><strong>Table 24.32. ChainPosRuleSet table: All contexts beginning with
            the same glyph</strong></p><div class="table-contents"><table role="" class="table" summary="ChainPosRuleSet table: All contexts beginning with&#10;            the same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ChainPosRuleCount</td><td role="">Number of ChainPosRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainPosRule [ChainPosRuleCount]</td><td role="">Array of offsets to ChainPosRule tables-from
              beginning of ChainPosRuleSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80796588016"></a><p class="title"><strong>Table 24.33. ChainPosRule subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ChainPosRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Backtrack [BacktrackGlyphCount]</td><td role="">Array of backtracking GlyphID's (to be
              matched before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Total number of glyphs in the input sequence
              (includes the first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Input [InputGlyphCount-1]</td><td role="">Array of input GlyphIDs (start with second
              glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Total number of glyphs in the look ahead
              sequence (number of glyphs to be matched after the input
              sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">LookAhead [LookAheadGlyphCount]</td><td role="">Array of lookahead GlyphID's (to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [PosCount]</td><td role="">Array of PosLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.19.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by the ChainPosRule table t = ChainPosRuleSet
	  [m].ChainPosRule [n] is

	  B<sub>b-1</sub> L* ... L* B<sub>0</sub>
          ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L*
	  ... L* A<sub>a-1</sub>, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">b is t.BacktrackGlyphCount</p></li><li role="" class="listitem"><p role="">i is t.InputGlyphCount</p></li><li role="" class="listitem"><p role="">a is t.LookaheadGlyphCount</p></li><li role="" class="listitem"><p role="">B<sub>k</sub> is {t.Backtrack [k]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is {Coverage[m]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is {t.Input[k-1]} ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">A<sub>k</sub> is {t.LookAhead[k]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796559168"></a>Chaining Context Positioning Format 2: Class-based
        Chaining Context Glyph Positioning</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.20.1"></a>Specification</h3></div></div></div><p role="">This lookup Format is parallel to the Context
          Positioning format 2, with PosClassSet subtable changed to
          ChainPosClassSet subtable, and PosClassRule subtable changed
          to ChainPosClassRule subtable.</p><p role="">To chain contexts, three classes are used in the glyph
          ClassDef table: Backtrack ClassDef, Input ClassDef, and
          Lookahead ClassDef.</p><div class="table"><a name="idm80796556112"></a><p class="title"><strong>Table 24.34. ChainContextPosFormat2 subtable: Chaining class-based context glyph positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextPosFormat2 subtable: Chaining class-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table-from beginning of
              ChainContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BacktrackClassDef</td><td role="">Offset to ClassDef table containing backtrack
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">InputClassDef</td><td role="">Offset to ClassDef table containing input
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LookaheadClassDef</td><td role="">Offset to ClassDef table containing lookahead
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ChainPosClassSetCnt</td><td role="">Number of ChainPosClassSet
              tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainPosClassSet [ChainPosClassSetCnt]</td><td role="">Array of offsets to ChainPosClassSet
              tables-from beginning of ChainContextPos
              subtable-ordered by input class-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">All the ChainPosClassRules that define contexts
          beginning with the same class are grouped together and
          defined in a ChainPosClassSet table. Consequently, the
          ChainPosClassSet table identifies the class of a context's
          first component.</p><div class="table"><a name="idm80796542112"></a><p class="title"><strong>Table 24.35. ChainPosClassSet table: All contexts beginning with the same class</strong></p><div class="table-contents"><table role="" class="table" summary="ChainPosClassSet table: All contexts beginning with the same class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ChainPosClassRuleCnt</td><td role="">Number of ChainPosClassRule
              tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainPosClassRule [ChainPosClassRuleCnt]</td><td role="">Array of offsets to ChainPosClassRule
              tables-from beginning of ChainPosClassSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80796536592"></a><p class="title"><strong>Table 24.36. ChainPosClassRule subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ChainPosClassRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Backtrack [BacktrackGlyphCount]</td><td role="">Array of backtracking classes(to be matched
              before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Total number of classes in the input sequence
              (includes the first class)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Input [InputGlyphCount-1]</td><td role="">Array of input classes(start with second
              class; to be matched with the input glyph
              sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Total number of classes in the look ahead
              sequence (number of classes to be matched after the
              input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookAhead [LookAheadGlyphCount]</td><td role="">Array of lookahead classes(to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [ChainPosCount]</td><td role="">Array of PosLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.20.2"></a>Annotation</h3></div></div></div><p role="">The pattern matched by the ChainPosClassRule table t = ChainPosClassSet [m].ChainPosRule [n] is

	  B<sub>b-1</sub> L* ... L* B<sub>0</sub>
          ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L*
	  ... L* A<sub>a-1</sub>, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">b is t.BacktrackGlyphCount</p></li><li role="" class="listitem"><p role="">i is t.InputGlyphCount</p></li><li role="" class="listitem"><p role="">a is t.LookaheadGlyphCount</p></li><li role="" class="listitem"><p role="">B<sub>k</sub> is BacktrackClassDef
	      [t.Backtrack [k]] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is (Coverage ∩
	      InputClassDef [m]) ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is InputClassDef
	      [t.Input [k-1]] ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">A<sub>k</sub> is LookAheadClassDef
	      [t.LookAhead [k]] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796507600"></a>Chaining Context Positioning Format 3: Coverage-based Chaining
        Context Glyph Positioning</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.21.1"></a>Specification</h3></div></div></div><p role="">Format 3 defines a chaining context rule as a sequence
          of Coverage tables. Each position in the sequence may define
          a different Coverage table for the set of glyphs that
          matches the context pattern. With Format 3, the glyph sets
          defined in the different Coverage tables may intersect,
          unlike Format 2 which specifies fixed class assignments
          (identical for each position in the backtrack, input, or
          lookahead sequence) and exclusive classes (a glyph cannot be
          in more than one class at a time).</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: The order of the Coverage tables listed in the
            Coverage array must follow the writing direction. For text
            written from right to left, then the right-most glyph will
            be first. Conversely, for text written from left to right,
            the left-most glyph will be first.</p></blockquote></div><p role="">The subtable also contains a count of the positioning
          operations to be performed on the input Coverage sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord) in design order: that is, the order in
          which lookups should be applied to the entire glyph
          sequence.</p><div class="table"><a name="idm80796502928"></a><p class="title"><strong>Table 24.37. ChainContextPosFormat3 subtable: Coverage-based chaining context glyph positioning</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextPosFormat3 subtable: Coverage-based chaining context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">PosFormat</td><td role="">Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Number of glyphs in the backtracking
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [BacktrackGlyphCount]</td><td role="">Array of offsets to coverage tables in
              backtracking sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Number of glyphs in input
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [InputGlyphCount]</td><td role="">Array of offsets to coverage tables in input
              sequence, in glyph sequence order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Number of glyphs in lookahead
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [LookaheadGlyphCount]</td><td role="">Array of offsets to coverage tables in
              lookahead sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">PosCount</td><td role="">Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">PosLookupRecord [PosCount]</td><td role="">Array of PosLookupRecords, in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.21.2"></a>Annotation</h3></div></div></div><p role="">It is probably worth noting that InputGlyphCount should
          be non-zero, and that BacktrackGlyphCount and
          LookaheadGlyphCount can be zero.</p><p role="">It is unclear whether the PosCount can be 0. At first
          it seems that such a subtable is not interesting, since it
          does nothing. On the other hand, this could be useful to
          prevent the activation of following subtables. The
          recommendation is to explicitly mention that case as
          permitted.</p><p role="">The three fields that hold arrays of offsets to
	  coverages have the same name. We assume that their names are
	  Backtrack, Input and Lookahead.</p><p role="">The pattern matched by this subtable is
          B<sub>b-1</sub> L* ... L*
          B<sub>0</sub> L* ▶
	  I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L* ... L*
          A<sub>a-1</sub>, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">b is BacktrackGlyphCount</p></li><li role="" class="listitem"><p role="">i is InputGlyphCount</p></li><li role="" class="listitem"><p role="">a is LookaheadGlyphCount</p></li><li role="" class="listitem"><p role="">B<sub>k</sub> is Backtrack
	      [k] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is
		Input [k] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">A<sub>k</sub> is Lookahead
	      [k] ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">This table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796472240"></a>Lookup Type 9: Extension Positioning</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.22.1"></a>Specification</h3></div></div></div><p role="">This lookup provides a mechanism whereby any other
          lookup type's subtables are stored at a 32-bit offset
          location in the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. This is
          needed if the total size of the subtables exceeds the 16-bit
          limits of the various other offsets in the
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. In this specification, the
          subtable stored at the 32-bit offset location is termed the
          "extension" subtable.</p><div class="table"><a name="idm80796468288"></a><p class="title"><strong>Table 24.38. ExtensionPosFormat1 subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ExtensionPosFormat1 subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">PosFormat</td><td role="">Format identifier. Set to 1.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">ExtensionLookupType</td><td role="">Lookup type of subtable referenced by
              ExtensionOffset (i.e. the extension
              subtable).</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ExtensionOffset</td><td role="">Offset to the extension subtable, of lookup
              type ExtensionLookupType, relative to the start of the
              ExtensionPosFormat1 subtable.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">ExtensionLookupType must be set to any lookup type other
          than 9. All subtables in a LookupType 9 lookup must have the
          same ExtensionLookupType. All offsets in the extension
          subtables are set in the usual way, i.e. relative to the
          extension subtables themselves</p><p role="">When an OpenType layout engine encounters a LookupType 9
          Lookup table, it shall:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Proceed as though the Lookup table's LookupType
              field were set to the ExtensionLookupType of the
              subtables.</p></li><li role="" class="listitem"><p role="">Proceed as though each extension subtable referenced
              by ExtensionOffset replaced the LookupType 9 subtable
              that referenced it.</p></li></ul></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.22.2"></a>Annotation</h3></div></div></div><p role="">This subtable does not match a pattern by itself, nor
	  does it have an action by itself.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796455616"></a>Shared Tables: ValueRecord, Anchor Table, and MarkArray</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.23.1"></a>Specification</h3></div></div></div><p role="">Several lookup subtables described earlier in this
          chapter refer to one or more of the same tables for
          positioning data: ValueRecord, Anchor table, and MarkArray.
          For easy reference, those shared tables are described
          here.</p><p role="">Example 14 at the end of the chapter uses a ValueFormat
          table and ValueRecord to specify positioning values in
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796451376"></a>ValueRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.24.1"></a>Specification</h3></div></div></div><p role=""><a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables use ValueRecords to
          describe all the variables and values used to adjust the
          position of a glyph or set of glyphs. A ValueRecord may
          define any combination of X and Y values (in design units)
          to add to (positive values) or subtract from (negative
          values) the placement and advance values provided in the
          font. A ValueRecord also may contain an offset to a Device
          table for each of the specified values. If a ValueRecord
          specifies more than one value, the values should be listed
          in the order shown in the ValueRecord definition.</p><p role="">The text-processing client must be aware of the flexible
          and multi-dimensional nature of ValueRecords in the
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. Because the
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses ValueRecords for many
          purposes, the sizes and contents of ValueRecords may vary
          from subtable to subtable.</p><div class="table"><a name="idm80796446048"></a><p class="title"><strong>Table 24.39. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">int16</td><td role="">XPlacement</td><td role="">Horizontal adjustment for placement-in design
                  units</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">YPlacement</td><td role="">Vertical adjustment for placement-in design
                  units</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">XAdvance</td><td role="">Horizontal adjustment for advance-in design
                  units (only used for horizontal writing)</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">YAdvance</td><td role="">Vertical adjustment for advance-in design units
                  (only used for vertical writing)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">XPlaDevice</td><td role="">Offset to Device table for horizontal
                  placement-measured from beginning of PosTable (may
                  be NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">YPlaDevice</td><td role="">Offset to Device table for vertical
                  placement-measured from beginning of PosTable (may
                  be NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">XAdvDevice</td><td role="">Offset to Device table for horizontal
                  advance-measured from beginning of PosTable (may be
                  NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">YAdvDevice</td><td role="">Offset to Device table for vertical
                  advance-measured from beginning of PosTable (may be
                  NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A data format (ValueFormat), usually declared at the
          beginning of each <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable, defines
          the types of positioning adjustment data that ValueRecords
          specify. Usually, the same ValueFormat applies to every
          ValueRecord defined in the particular
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable.</p><p role="">The ValueFormat determines whether the
          ValueRecords:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Apply to placement, advance, or both.</p></li><li role="" class="listitem"><p role="">Apply to the horizontal position (X coordinate), the
              vertical position (Y coordinate), or both.</p></li><li role="" class="listitem"><p role="">May refer to one or more Device tables for any of
              the specified values.</p></li></ul></div><p role="">Each one-bit in the ValueFormat corresponds to a field
          in the ValueRecord and increases the size of the ValueRecord
          by 2 bytes. A ValueFormat of 0x0000 corresponds to an empty
          ValueRecord, which indicates no positioning changes.</p><p role="">To identify the fields in each ValueRecord, the
          ValueFormat uses the bit settings shown below. To specify
          multiple fields with a ValueFormat, the bit settings of the
          relevant fields are added with a logical OR
          operation.</p><p role="">For example, to adjust the left-side bearing of a glyph,
          the ValueFormat will be 0x0001, and the ValueRecord will
          define the XPlacement value. To adjust the advance width of
          a different glyph, the ValueFormat will be 0x0004, and the
          ValueRecord will describe the XAdvance value. To adjust both
          the XPlacement and XAdvance of a set of glyphs, the
          ValueFormat will be 0x0005, and the ValueRecord will specify
          both values in the order they are listed in the ValueRecord
          definition.</p><div class="table"><a name="idm80796423872"></a><p class="title"><strong>Table 24.40. ValueFormat bit enumeration (indicates which fields
            are present)</strong></p><div class="table-contents"><table role="" class="table" summary="ValueFormat bit enumeration (indicates which fields&#10;            are present)" border="1"><colgroup><col width="7pc"/><col width="9pc"/><col width="14pc"/></colgroup><thead><tr><th role="">Mask</th><th role="">Name</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0x0001</td><td role="">XPlacement</td><td role="">Includes horizontal adjustment for
                  placement</td></tr><tr><td role="">0x0002</td><td role="">YPlacement</td><td role="">Includes vertical adjustment for
                  placement</td></tr><tr><td role="">0x0004</td><td role="">XAdvance</td><td role="">Includes horizontal adjustment for
                  advance</td></tr><tr><td role="">0x0008</td><td role="">YAdvance</td><td role="">Includes vertical adjustment for
                  advance</td></tr><tr><td role="">0x0010</td><td role="">XPlaDevice</td><td role="">Includes horizontal Device table for
                  placement</td></tr><tr><td role="">0x0020</td><td role="">YPlaDevice</td><td role="">Includes vertical Device table for
                  placement</td></tr><tr><td role="">0x0040</td><td role="">XAdvDevice</td><td role="">Includes horizontal Device table for
                  advance</td></tr><tr><td role="">0x0080</td><td role="">YAdvDevice</td><td role="">Includes vertical Device table for
                  advance</td></tr><tr><td role="">0xF000</td><td role="">Reserved</td><td role="">For future use</td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.24.2"></a>Annotation</h3></div></div></div><p role="">None</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796401680"></a>Anchor Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.25.1"></a>Specification</h3></div></div></div><p role="">A <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses anchor points to
        position one glyph with respect to another. Each glyph defines
        an anchor point, and the text-processing client attaches the
        glyphs by aligning their corresponding anchor points.</p><p role="">To describe an anchor point, an Anchor table can use one
        of three formats. The first format uses design units to
        specify a location for the anchor point. The other two formats
        refine the location of the anchor point using contour points
        (Format 2) or Device tables (Format 3).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796397344"></a>Anchor Table: Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.26.1"></a>Specification</h3></div></div></div><p role="">AnchorFormat1 consists of a format identifier
          (AnchorFormat) and a pair of design unit coordinates
          (XCoordinate and YCoordinate) that specify the location of
          the anchor point. This format has the benefits of small size
          and simplicity, but the anchor point cannot be hinted to
          adjust its position for different device resolutions.</p><p role="">Example 15 at the end of this chapter uses
          AnchorFormat1.</p><div class="table"><a name="idm80796394288"></a><p class="title"><strong>Table 24.41. AnchorFormat1 table: Design units only</strong></p><div class="table-contents"><table role="" class="table" summary="AnchorFormat1 table: Design units only" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">AnchorFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">XCoordinate</td><td role="">Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">YCoordinate</td><td role="">Vertical value-in design units</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796386944"></a>Anchor Table: Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.27.1"></a>Specification</h3></div></div></div><p role="">Like AnchorFormat1, AnchorFormat2 specifies a format
          identifier (AnchorFormat) and a pair of design unit
          coordinates for the anchor point (Xcoordinate and
          Ycoordinate).</p><p role="">For fine-tuning the location of the anchor point,
          AnchorFormat2 also provides an index to a glyph contour
          point (AnchorPoint) that is on the outline of a glyph
          (AnchorPoint). Hinting can be used to move the AnchorPoint.
          In the rendered text, the AnchorPoint will provide the final
          positioning data for a given ppem size.</p><p role="">Example 16 at the end of this chapter uses
          AnchorFormat2.</p><div class="table"><a name="idm80796383296"></a><p class="title"><strong>Table 24.42. AnchorFormat2 table: Design units plus contour
            point</strong></p><div class="table-contents"><table role="" class="table" summary="AnchorFormat2 table: Design units plus contour&#10;            point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">AnchorFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">XCoordinate</td><td role="">Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">YCoordinate</td><td role="">Vertical value-in design units</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">AnchorPoint</td><td role="">Index to glyph contour point</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796374448"></a>Anchor Table: Format 3</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.28.1"></a>Specification</h3></div></div></div><p role="">Like AnchorFormat1, AnchorFormat3 specifies a format
          identifier (AnchorFormat) and locates an anchor point
          (Xcoordinate and Ycoordinate). And, like AnchorFormat 2, it
          permits fine adjustments to the coordinate values. However,
          AnchorFormat3 uses Device tables, rather than a contour
          point, for this adjustment.</p><p role="">With a Device table, a client can adjust the position of
          the anchor point for any font size and device resolution.
          AnchorFormat3 can specify offsets to Device tables for the
          the X coordinate (XDeviceTable) and the Y coordinate
          (YDeviceTable). If only one coordinate requires adjustment,
          the offset to the Device table may be set to NULL for the
          other coordinate.</p><p role="">Example 17 at the end of the chapter shows an
          AnchorFormat3 table.</p><div class="table"><a name="idm80796370592"></a><p class="title"><strong>Table 24.43. AnchorFormat3 table: Design units plus Device
            tables</strong></p><div class="table-contents"><table role="" class="table" summary="AnchorFormat3 table: Design units plus Device&#10;            tables" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">AnchorFormat</td><td role="">Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">XCoordinate</td><td role="">Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">YCoordinate</td><td role="">Vertical value-in design units</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">XDeviceTable</td><td role="">Offset to Device table for X coordinate- from
              beginning of Anchor table (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">YDeviceTable</td><td role="">Offset to Device table for Y coordinate- from
              beginning of Anchor table (may be NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796360112"></a>Mark Array</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.29.1"></a>Specification</h3></div></div></div><p role="">The MarkArray table defines the class and the anchor
          point for a mark glyph. Three <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          subtables – MarkToBase, MarkToLigature, and
          MarkToMark Attachment – use the MarkArray table to
          specify data for attaching marks.</p><p role="">The MarkArray table contains a count of the number of
          mark records (MarkCount) and an array of those records
          (MarkRecord). Each mark record defines the class of the mark
          and an offset to the Anchor table that contains data for the
          mark.</p><p role="">A class value can be 0 (zero), but the MarkRecord must
          explicitly assign that class value (this differs from the
          ClassDef table, in which all glyphs not assigned class
          values automatically belong to Class 0). The
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables that refer to MarkArray
          tables use the class assignments for indexing zero-based
          arrays that contain data for each mark class.</p><p role="">In Example 18 at the end of the chapter, a MarkArray
          table and two MarkRecords define two mark classes.</p><div class="table"><a name="idm80796354224"></a><p class="title"><strong>Table 24.44. MarkArray table</strong></p><div class="table-contents"><table role="" class="table" summary="MarkArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">MarkCount</td><td role="">Number of MarkRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">MarkRecord [MarkCount]</td><td role="">Array of MarkRecords – in Coverage
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80796348848"></a><p class="title"><strong>Table 24.45. MarkRecord</strong></p><div class="table-contents"><table role="" class="table" summary="MarkRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">Class</td><td role="">Class defined for this mark</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MarkAnchor</td><td role="">Offset to Anchor table – from beginning of
              MarkArray table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796342896"></a>GPOS Subtable Examples</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.30.1"></a>Specification</h3></div></div></div><p role="">The rest of this chapter describes examples of all the
          <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable formats, including each of
          the three formats available for contextual positioning. All
          the examples reflect unique parameters described below, but
          the samples provide a useful reference for building
          subtables specific to other situations.</p><p role="">All the examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796338624"></a>Example 1: GPOS Header Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.31.1"></a>Specification</h3></div></div></div><p role="">Example 1 shows a typical <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> Header
          table definition with offsets to a ScriptList, FeatureList,
          and LookupList.</p><div class="table"><a name="idm80796335632"></a><p class="title"><strong>Table 24.46. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">GPOSHeader</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheGPOSHeader</td><td role="">GPOSHeader table
                  definition</td></tr><tr><td role="">00010000</td><td role="">0x00010000</td><td role="">Version</td></tr><tr><td role="">000A</td><td role="">TheScriptList</td><td role="">offset to ScriptList table</td></tr><tr><td role="">001E</td><td role="">TheFeatureList</td><td role="">offset to FeatureList table</td></tr><tr><td role="">002C</td><td role="">TheLookupList</td><td role="">offset to LookupList table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796324368"></a>Example 2: SinglePosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.32.1"></a>Specification</h3></div></div></div><p role="">Example 2 uses the SinglePosFormat1 subtable to lower
          the Y placement of subscript glyphs in a font. The
          LowerSubscriptsSubTable defines one Coverage table, called
          LowerSubscriptsCoverage, which lists one range of glyph
          indices for the numeral/numeric subscript glyphs. The
          subtable's ValueFormat setting indicates that the
          ValueRecord specifies only the YPlacement value, lowering
          each subscript glyph by 80 design units.</p><div class="table"><a name="idm80796321648"></a><p class="title"><strong>Table 24.47. Example 2</strong></p><div class="table-contents"><table role="" class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">SinglePosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LowerSubscriptsSubTable</td><td role="">SinglePos subtable definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">0008</td><td role="">LowerSubscriptsCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">0x0002</td><td role="">ValueFormat, YPlacement,Value[0], move Y
                  position down</td></tr><tr><td role="">FFB0</td><td role="">-80</td><td role=""> </td></tr><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LowerSubscriptsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">RangeCount RangeRecord[0]</td></tr><tr><td role="">01B3</td><td role="">ZeroSubscriptGlyphID</td><td role="">Start, first glyphID</td></tr><tr><td role="">01BC</td><td role="">NineSubscriptGlyphID</td><td role="">End, last glyphID</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796300640"></a>Example 3: SinglePosFormat2 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.33.1"></a>Specification</h3></div></div></div><p role="">This example uses a SinglePosFormat2 subtable to adjust
          the spacing of three dash glyphs by different amounts. The
          em dash spacing changes by 10 units, the en dash spacing
          changes by 25 units, and spacing of the standard dash
          changes by 50 units.</p><p role="">The DashSpacingSubTable contains one Coverage table with
          three dash glyph indices, plus an array of ValueRecords, one
          for each covered glyph. The ValueRecords use the same
          ValueFormat to modify the XPlacement and XAdvance values of
          each glyph. The ValueFormat bit setting of 0x0005 is
          produced by adding the XPlacement and XAdvance bit
          settings.</p><div class="table"><a name="idm80796297328"></a><p class="title"><strong>Table 24.48. Example 3</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">SinglePosFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashSpacingSubTable</td><td role="">SinglePos subtable
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">PosFormat</td></tr><tr><td role="">0014</td><td role="">DashSpacingCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0005</td><td role="">0x0005</td><td role="">ValueFormat for XPlacement and XAdvance</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ValueCount Value[0], for dash glyph</td></tr><tr><td role="">0032</td><td role="">50</td><td role="">XPlacement</td></tr><tr><td role="">0032</td><td role="">50</td><td role="">XAdvance Value[1], for en dash glyph</td></tr><tr><td role="">0019</td><td role="">25</td><td role="">XPlacement</td></tr><tr><td role="">0019</td><td role="">25</td><td role="">XAdvance Value[2], for em dash glyph</td></tr><tr><td role="">000A</td><td role="">10</td><td role="">XPlacement</td></tr><tr><td role="">000A</td><td role="">10</td><td role="">XAdvanc</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashSpacingCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">004F</td><td role="">DashGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0125</td><td role="">EnDashGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0129</td><td role="">EmDashGlyphID</td><td role="">GlyphArray[2]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796267536"></a>Example 4: PairPosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.34.1"></a>Specification</h3></div></div></div><p role="">Example 4 uses a PairPosFormat1 subtable to kern two
          glyph pairs - "Po" and "To" - by adjusting the XAdvance of
          the first glyph and the XPlacement of the second glyph. Two
          ValueFormats are defined, one for each glyph. The subtable
          contains a Coverage table that lists the index of the first
          glyph in each pair. It also contains an offset to a PairSet
          table for each covered glyph.</p><p role="">A PairSet table defines an array of PairValueRecords to
          specify all the glyph pairs that contain a covered glyph as
          their first component. In this example, the PPairSet table
          has one PairValueRecord that identifies the second glyph in
          the "Po" pair and two ValueRecords, one for the first glyph
          and one for the second. The TPairSet table also has one
          PairValueRecord that lists the second glyph in the "To" pair
          and two ValueRecords, one for each glyph.</p><div class="table"><a name="idm80796263952"></a><p class="title"><strong>Table 24.49. Example 4</strong></p><div class="table-contents"><table role="" class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">PairPosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PairKerningSubTable</td><td role="">PairPos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">001E</td><td role="">PairKerningCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0004</td><td role="">0x0004</td><td role="">ValueFormat1 XAdvance only</td></tr><tr><td role="">0001</td><td role="">0x0001</td><td role="">ValueFormat2 XPlacement only</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">PairSetCount</td></tr><tr><td role="">000E</td><td role="">PPairSetTable</td><td role="">PairSet[0]</td></tr><tr><td role="">0016</td><td role="">TPairSetTable</td><td role="">PairSet[1</td></tr><tr><td role=""> </td><td role="">PairSetTable</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PPairSetTable</td><td role="">PairSet table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PairValueCount, one pair in set
                  PairValueRecord[0]</td></tr><tr><td role="">0059</td><td role="">LowercaseOGlyphID</td><td role="">SecondGlyph</td></tr><tr><td role="">FFE2</td><td role="">-30</td><td role="">Value 1, XAdvance adjustment for first
                  glyph</td></tr><tr><td role="">FFEC</td><td role="">-20</td><td role="">Value 2, XPlacement adjustment for second
                  glyp</td></tr><tr><td role=""> </td><td role="">PairSetTable</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PairSetTable</td><td role="">PairSet table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PairValueCount one pair in set
                  PairValueRecord[0]</td></tr><tr><td role="">0059</td><td role="">LowercaseOGlyphID</td><td role="">SecondGlyph</td></tr><tr><td role="">FFD8</td><td role="">-40</td><td role="">Value1 XAdvance adjustment for first
                  glyph</td></tr><tr><td role="">FFE7</td><td role="">-25</td><td role="">Value 2 XPlacement adjustment for second
                  glyp</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PairKerningCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">002D</td><td role="">UppercasePGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0031</td><td role="">UppercaseTGlyphID</td><td role="">GlyphArray[1]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80796223056"></a>Example 5: PairPosFormat2 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.35.1"></a>Specification</h3></div></div></div><p role="">The PairPosFormat2 subtable in this example defines
          pairs composed of two glyph classes. Two ClassDef tables are
          defined, one for each glyph class. The first glyph in each
          pair is in a class of lowercase glyphs with diagonal shapes
          (v, w, y), defined Class1 in the LowercaseClassDef table.
          The second glyph in each pair is in a class of punctuation
          glyphs (comma and period), defined in Class1 in the
          PunctuationClassDef table. The Coverage table only lists the
          indices of the glyphs in the LowercaseClassDef table since
          they occupy the first position in the pairs.</p><p role="">The subtable defines two Class1Records for the classes
          defined in LowecaseClassDef, including Class0. Each record,
          in turn, defines a Class2Record for each class defined in
          PunctuationClassDef, including Class0. The Class2Records
          specify the positioning adjustments for the glyphs.</p><p role="">The pairs are kerned by reducing the XAdvance of the
          first glyph by 50 design units. Because no positioning
          change applies to the second glyph, its ValueFormat2 is set
          to 0, to indicate that Value2 is empty for each pair.</p><p role="">Since no pairs begin with Class0 or Class2 glyphs, all
          the ValueRecords referenced in Class1Record[0] contain
          values of 0 or are empty. However, Class1Record[1] does
          define an XAdvance value in its Class2Record[1] for kerning
          all pairs that contain a Class1 glyph followed by a Class2
          glyph.</p><div class="table"><a name="idm80796218080"></a><p class="title"><strong>Table 24.50. Example 5</strong></p><div class="table-contents"><table role="" class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">PairPosFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PunctKerningSubTable</td><td role="">PairPos subtable
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">PosFormat</td></tr><tr><td role="">0018</td><td role="">PunctKerningCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0004</td><td role="">0x0004</td><td role="">ValueFormat1 XAdvance only</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">ValueFormat2 no ValueRecord for second
                  glyph</td></tr><tr><td role="">0022</td><td role="">LowercaseClassDef</td><td role="">offset to ClassDef1 table for first class in
                  pair</td></tr><tr><td role="">0032</td><td role="">PunctuationClassDef</td><td role="">offset to ClassDef2 table for second class in
                  pair</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class1Count</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class2Count Class1Record[0], no contexts begin
                  with Class0 Class2Record[0]</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Value1- no change for first glyph, Value2 no
                  ValueRecord for second glyph Class2Record[1]</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Value1- no change for first glyph, Value2 no
                  ValueRecord for second glyph Class1Record[1], for
                  contexts beginning with Class1 Class2Record[0] no
                  contexts with Class0 as second glyph</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Value1-no change for first glyph, Value2-no
                  ValueRecord for second glyph Class2Record[1]contexts
                  with Class1 as second glyph</td></tr><tr><td role="">FFCE</td><td role="">-50</td><td role="">Value1- move punctuation glyph left, Value2- no
                  ValueRecord for second glyp</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PunctKerningCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">0046</td><td role="">LowercaseVGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0047</td><td role="">LowercaseWGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0049</td><td role="">LowercaseYGlyphID</td><td role="">GlyphArray[2</td></tr><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LowercaseClassDef</td><td role="">ClassDef table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td role="">0046</td><td role="">LowercaseVGlyphID</td><td role="">Start</td></tr><tr><td role="">0047</td><td role="">LowercaseWGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class ClassRangeRecord[1]</td></tr><tr><td role="">0049</td><td role="">LowercaseYGlyphID</td><td role="">Start</td></tr><tr><td role="">0049</td><td role="">LowercaseYGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Clas</td></tr><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PunctuationClassDef</td><td role="">ClassDef table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td role="">006A</td><td role="">PeriodPunctGlyphID</td><td role="">Start</td></tr><tr><td role="">006B</td><td role="">CommaPunctGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80794047152"></a>Example 6: CursivePosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.36.1"></a>Specification</h3></div></div></div><p role="">In Example 6, the Urdu language system uses a
          CursivePosFormat1 subtable to attach glyphs along a diagonal
          baseline that descends from right to left. Two glyphs are
          defined with attachment data and listed in the Coverage
          table-the Kaf and Ha glyphs. For each glyph, the subtable
          contains an EntryExitRecord that defines offsets to two
          Anchor tables, an entry attachment point, and an exit
          attachment point. Each Anchor table defines X and Y
          coordinate values. To render Urdu down and diagonally, the
          entry point's Y coordinate is above the baseline and the
          exit point's Y coordinate is located below the
          baseline.</p><div class="table"><a name="idm80794044192"></a><p class="title"><strong>Table 24.51. Example 6</strong></p><div class="table-contents"><table role="" class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">CursivePosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DiagonalWritingSubTable</td><td role="">CursivePos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">000E</td><td role="">DiagonalWritingCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">EntryExitCount EntryExitRecord[0] for Kaf
                  glyph</td></tr><tr><td role="">0016</td><td role="">KafEntryAnchor</td><td role="">offset to EntryAnchor table</td></tr><tr><td role="">001C</td><td role="">KafExitAnchor</td><td role="">offset to ExitAnchor table EntryExitRecord[1]
                  for Ha glyph</td></tr><tr><td role="">0022</td><td role="">HaEntryAnchor</td><td role="">offset to EntryAnchor table</td></tr><tr><td role="">0028</td><td role="">HaExitAnchor</td><td role="">offset to ExitAnchor tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DiagonalWritingCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0203</td><td role="">KafGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">027E</td><td role="">HaGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">KafEntryAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">05DC</td><td role="">1500</td><td role="">XCoordinate</td></tr><tr><td role="">002C</td><td role="">44</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role="">KafExitAnchor</td><td role="">Anchor</td><td role="">table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">XCoordinate</td></tr><tr><td role="">FFEC</td><td role="">-20</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HaEntryAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">05DC</td><td role="">1500</td><td role="">XCoordinate</td></tr><tr><td role="">002C</td><td role="">44</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HaExitAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">XCoordinate</td></tr><tr><td role="">FFEC</td><td role="">-20</td><td role="">Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793992624"></a>Example 7: MarkBasePosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.37.1"></a>Specification</h3></div></div></div><p role="">The MarkBasePosFormat1 subtable in Example 7 defines one
          Arabic base glyph, Tah, and two Arabic mark glyphs: a
          fathatan mark above the base glyph, and a kasra mark below
          the base glyph. The BaseGlyphsCoverage table lists the base
          glyph, and the MarkGlyphsCoverage table lists the mark
          glyphs.</p><p role="">Each mark is also listed in the MarkArray, along with
          its attachment point data and a mark Class value. The
          MarkArray defines two mark classes: Class0 consists of marks
          located above base glyphs, and Class1 consists of marks
          located below base glyphs.</p><p role="">The BaseArray defines attachment data for base glyphs.
          In this array, one BaseRecord is defined for the Tah glyph
          with offsets to two BaseAnchor tables, one for each class of
          marks. AboveBaseAnchor defines an attachment point for marks
          placed above the Tah base glyph, and BelowBaseAnchor defines
          an attachment point for marks placed below it.</p><div class="table"><a name="idm80793988576"></a><p class="title"><strong>Table 24.52. Example 7</strong></p><div class="table-contents"><table role="" class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MarkBasePosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkBaseAttachSubTable</td><td role="">MarkBasePos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">000C</td><td role="">MarkGlyphsCoverage</td><td role="">offset to MarkCoverage table</td></tr><tr><td role="">0014</td><td role="">BaseGlyphsCoverage</td><td role="">offset to BaseCoverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassCount</td></tr><tr><td role="">001A</td><td role="">MarkGlyphsArray</td><td role="">offset to MarkArray table</td></tr><tr><td role="">0030</td><td role="">BaseGlyphsArray</td><td role="">offset to BaseArray tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkGlyphsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0333</td><td role="">fathatanMarkGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">033F</td><td role="">kasraMarkGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">BaseGlyphsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">0190</td><td role="">tahBaseGlyphID</td><td role="">GlyphArray[0</td></tr><tr><td role=""> </td><td role="">MarkArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkGlyphsArray</td><td role="">MarkArray table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Class, for marks over base</td></tr><tr><td role="">000A</td><td role="">fathatanMarkAnchor</td><td role="">offset to Anchor table MarkRecord[1]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, for marks under</td></tr><tr><td role="">0010</td><td role="">kasraMarkAnchor</td><td role="">offset to Anchor tabl</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">fathatanMarkAnchor</td><td role="">Anchor table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">015A</td><td role="">346</td><td role="">XCoordinate</td></tr><tr><td role="">FF9E</td><td role="">-98</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">kasraMarkAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0105</td><td role="">261</td><td role="">XCoordinate</td></tr><tr><td role="">0058</td><td role="">88</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">BaseArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">BaseGlyphsArray</td><td role="">BaseArray table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCount BaseRecord[0]</td></tr><tr><td role="">0006</td><td role="">AboveBaseAnchor</td><td role="">BaseAnchor[0]</td></tr><tr><td role="">000C</td><td role="">BelowBaseAnchor</td><td role="">BaseAnchor[1]</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AboveBaseAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">033E</td><td role="">830</td><td role="">XCoordinate</td></tr><tr><td role="">0640</td><td role="">1600</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">BelowBaseAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">033E</td><td role="">830</td><td role="">XCoordinate</td></tr><tr><td role="">FFAD</td><td role="">-83</td><td role="">Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793914992"></a>Example 8: MarkLigPosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.38.1"></a>Specification</h3></div></div></div><p role="">Example 8 uses the MarkLigPosFormat1 subtable to attach
          marks to a ligature glyph in the Arabic script. The
          hypothetical ligature is composed of three glyph components:
          a Lam (initial form), a meem (medial form), and a jeem
          (medial form). Accent marks are defined for the first two
          components: the sukun accent is positioned above lam, and
          the kasratan accent is placed below meem.</p><p role="">The LigGlyphsCoverage table lists the ligature glyph and
          the MarkGlyphsCoverage table lists the two accent marks.
          Each mark is also listed in the MarkArray, along with its
          attachment point data and a mark Class value. The MarkArray
          defines two mark classes: Class0 consists of marks located
          above base glyphs, and Class1 consists of marks located
          below base glyphs.</p><p role="">The LigGlyphsArray has an offset to one LigatureAttach
          table for the covered ligature glyph. This table, called
          LamWithMeemWithJeemLigAttach, defines a count and array of
          the component glyphs in the ligature. Each ComponentRecord
          defines offsets to two Anchor tables, one for each mark
          class.</p><p role="">In the example, the first glyph component, lam,
          specifies a high attachment point for positioning accents
          above, but does not specify a low attachment point for
          placing accents below. The second glyph component, meem,
          defines a low attachment point for placing accents below,
          but not above. The third component, jeem, has no attachment
          points since the example defines no accents for it.</p><div class="table"><a name="idm80793909488"></a><p class="title"><strong>Table 24.53. Example 8</strong></p><div class="table-contents"><table role="" class="table" summary="Example 8" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MarkLigPosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkLigAttachSubTable</td><td role="">MarkLigPos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">000C</td><td role="">MarkGlyphsCoverage</td><td role="">offset to MarkCoverage table</td></tr><tr><td role="">0014</td><td role="">LigGlyphsCoverage</td><td role="">offset to LigatureCoverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassCount</td></tr><tr><td role="">001A</td><td role="">MarkGlyphsArray</td><td role="">offset to MarkArray table</td></tr><tr><td role="">0030</td><td role="">LigGlyphsArray</td><td role="">offset to LigatureArray tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkGlyphsCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">033C</td><td role="">sukunMarkGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">033F</td><td role="">kasratanMarkGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigGlyphsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">0234</td><td role="">LamWithMeemWithJeem</td><td role="">LigatureGlyphID GlyphArray[0</td></tr><tr><td role=""> </td><td role="">MarkArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkGlyphsArray</td><td role="">MarkArray table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Class, for marks above components</td></tr><tr><td role="">000A</td><td role="">sukunMarkAnchor</td><td role="">offset to Anchor table MarkRecord[1]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, for marks below components</td></tr><tr><td role="">0010</td><td role="">kasratanMarkAnchor</td><td role="">offset to Anchor tabl</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">sukunMarkAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">015A</td><td role="">346</td><td role="">XCoordinate</td></tr><tr><td role="">FF9E</td><td role="">-98</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">kasratanMarkAnchor</td><td role="">Anchor table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0105</td><td role="">261</td><td role="">XCoordinate</td></tr><tr><td role="">01E8</td><td role="">488</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">LigatureArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigGlyphsArray</td><td role="">LigatureArray table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LigatureCount</td></tr><tr><td role="">0004</td><td role="">LamWithMeemWithJeemLigAttach</td><td role="">offset to LigatureAttach tabl</td></tr><tr><td role=""> </td><td role="">LigatureAttach</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LamWithMeemWithJeemLigAttach</td><td role="">LigatureAttach
                  table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ComponentCount ComponentRecord[0] Right-to-Left
                  text order</td></tr><tr><td role="">000E</td><td role="">AboveLamAnchor</td><td role="">offset to LigatureAnchor table ordered by mark
                  class value for Class0 marks (above)</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to LigatureAnchor table no attachment
                  points for Class1 marks ComponentRecor[1]</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to LigatureAnchor table no attachment
                  points for Class0 marks</td></tr><tr><td role="">0014</td><td role="">BelowMeemAnchor</td><td role="">offset to LigatureAnchor table for Class1 marks
                  (below) ComponentRecord[2]</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to LigatureAnchor table no attachment
                  points for Class0 marks</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to LigatureAnchor table no attachment
                  points for Class1 mark</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AboveLamAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0271</td><td role="">625</td><td role="">XCoordinate</td></tr><tr><td role="">0708</td><td role="">1800</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">BelowMeemAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">0178</td><td role="">376</td><td role="">XCoordinate</td></tr><tr><td role="">FE90</td><td role="">-368</td><td role="">Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793823952"></a>Example 9: MarkMarkPosFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.39.1"></a>Specification</h3></div></div></div><p role="">The MarkMarkPosFormat1 subtable in Example 9 defines two
          Arabic marks glyphs. The hanza mark, the base mark (Mark2),
          is identified in the Mark2GlyphsCoverage table. The damma
          mark, the attaching mark (Mark1), is defined in the
          Mark1GlyphsCoverage table.</p><p role="">Each Mark1 glyph is also listed in the Mark1Array, along
          with its attachment point data and a mark Class value. The
          Mark1GlyphsArray defines one mark class, Class0, that
          consists of marks located above Mark2 base glyphs. The
          Mark1GlyphsArray contains an offset to a dammaMarkAnchor
          table to specify the coordinate of the damma mark's
          attachment point.</p><p role="">The Mark2GlyphsArray table defines a count and an array
          of Mark2Records, one for each covered Mark2 base glyph. Each
          record contains an offset to a Mark2Anchor table for each
          Mark1 class. One Anchor table, AboveMark2Anchor, specifies a
          coordinate value for attaching the damma mark above the
          hanza base mark.</p><div class="table"><a name="idm80793819872"></a><p class="title"><strong>Table 24.54. Example 9</strong></p><div class="table-contents"><table role="" class="table" summary="Example 9" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MarkMarkPosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkMarkAttachSubTable</td><td role="">MarkMarkPos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">000C</td><td role="">Mark1GlyphsCoverage</td><td role="">offset to Mark1Coverage table</td></tr><tr><td role="">0012</td><td role="">Mark2GlyphsCoverage</td><td role="">offset to Mark2Coverage table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">ClassCount</td></tr><tr><td role="">0018</td><td role="">Mark1GlyphsArray</td><td role="">offset to Mark1Array table</td></tr><tr><td role="">0024</td><td role="">Mark2GlyphsArray</td><td role="">offset to Mark2Array tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Mark1GlyphsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">0296</td><td role="">dammaMarkGlyphID</td><td role="">GlyphArray[0</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Mark2GlyphsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">0289</td><td role="">hanzaMarkGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">MarkArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Mark1GlyphsArray</td><td role="">MarkArray table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Class for marks above base mark</td></tr><tr><td role="">0006</td><td role="">dammaMarkAnchor</td><td role="">offset to Anchor tabl</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">dammaMarkAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">00BD</td><td role="">189</td><td role="">XCoordinate</td></tr><tr><td role="">FF99</td><td role="">-103</td><td role="">YCoordinat</td></tr><tr><td role=""> </td><td role="">Mark2Array</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Mark2GlyphsArray</td><td role="">Mark2Array table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Mark2Count Mark2Record[0]</td></tr><tr><td role="">0004</td><td role="">AboveMark2Anchor</td><td role="">offset to Anchor table[0</td></tr><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AboveMark2Anchor</td><td role="">Anchor table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">00DD</td><td role="">221</td><td role="">XCoordinate</td></tr><tr><td role="">012D</td><td role="">301</td><td role="">Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793765696"></a>Example 10: ContextPosFormat1 Subtable and
        PosLookupRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.40.1"></a>Specification</h3></div></div></div><p role="">Example 10 uses a ContextPosFormat1 subtable to adjust
          the spacing between three Arabic glyphs in a word. The
          context is the glyph sequence (from right to left): heh
          (initial form), thal (final form), and heh (isolated form).
          In the rendered word, the first two glyphs are connected,
          but the last glyph (the isolated form of heh), is separate.
          This subtable reduces the amount of space between the last
          glyph and the rest of the word.</p><p role="">The subtable contains a WordCoverage table that lists
          the first glyph in the word, heh (initial), and one
          PosRuleSet table, called WordPosRuleSet, that defines all
          contexts beginning with this covered glyph.</p><p role="">The WordPosRuleSet contains one PosRule that describes a
          word context of three glyphs and identifies the second and
          third glyphs (the first glyph is identified by the
          WordPosRuleSet). When a text-processing client locates this
          context in text, it applies a SinglePos lookup (not shown in
          the example) at position 2 to reduce the spacing between the
          glyphs.</p><div class="table"><a name="idm80793761488"></a><p class="title"><strong>Table 24.55. Example 10</strong></p><div class="table-contents"><table role="" class="table" summary="Example 10" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextPosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MoveHehInSubtable</td><td role="">ContextPos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">0008</td><td role="">WordCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosRuleSetCount</td></tr><tr><td role="">000E</td><td role="">WordPosRuleSet</td><td role="">offset to PosRuleSet[0] tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">WordCoverage</td><td role="">Coverage table offset</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">02A6</td><td role="">hehInitialGlyphID</td><td role="">GlyphArray[0</td></tr><tr><td role=""> </td><td role="">PosRuleSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">WordPosRuleSet</td><td role="">PosRuleSet table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosRuleCount</td></tr><tr><td role="">0004</td><td role="">WordPosRule</td><td role="">Offset to PosRule[0] tabl</td></tr><tr><td role=""> </td><td role="">PosRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">WordPosRule</td><td role="">PosRule table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosCount</td></tr><tr><td role="">02DD</td><td role="">thalFinalGlyphID</td><td role="">Input[1]</td></tr><tr><td role="">02C6</td><td role="">hehIsolatedGlyphID</td><td role="">Input[0] PosLookupRecord[0]</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SequenceIndex</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793726736"></a>Example 11: ContextPosFormat2 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.41.1"></a>Specification</h3></div></div></div><p role="">The ContextPosFormat2 subtable in Example 11 defines
          context strings for five glyph classes: Class1 consists of
          uppercase glyphs that overhang and create a wide open space
          on their right side; Class2 consists of uppercase glyphs
          that overhang and create a narrow space on their right side;
          Class3 contains lowercase x-height vowels; and Class4
          contains accent glyphs placed over the lowercase vowels. The
          rest of the glyphs in the font fall into Class0.</p><p role="">The MoveAccentsSubtable defines two similar context
          strings. The first consists of a Class1 uppercase glyph
          followed by a Class3 lowercase vowel glyph with a Class4
          accent glyph over the vowel. When this context is found in
          the text, the client lowers the accent glyph over the vowel
          so that it does not collide with the overhanging glyph
          shape. The second context consists of a Class2 uppercase
          glyph, followed by a Class3 lowercase vowel glyph with a
          Class4 accent glyph over the vowel. When this context is
          found in the text, the client increases the advance width of
          the uppercase glyph to expand the space between it and the
          accented vowel.</p><p role="">The MoveAccents subtable defines a MoveAccentsCoverage
          table that identifies the first glyphs in the two contexts
          and offsets to five PosClassSet tables, one for each class
          defined in the ClassDef table. Since no contexts begin with
          Class0, Class3, or Class4 glyphs, the offsets to the
          PosClassSet tables for these classes are NULL.
          PosClassSet[1] defines all contexts beginning with Class1
          glyphs; it is called UCWideOverhangPosClass1Set.
          PosClassSet[2] defines all contexts beginning with Class2
          glyphs, and it is called
          UCNarrowOverhangPosClass1Set.</p><p role="">Each PosClassSet defines one PosClassRule. The
          UCWideOverhangPosClass1Set uses the
          UCWideOverhangPosClassRule to specify the first context. The
          first class in this context string is identified by the
          PosClassSet that includes a PosClassRule, in this case
          Class1. The PosClassRule table lists the second and third
          classes in the context as Class3 and Class4. A SinglePos
          Lookup (not shown) lowers the accent glyph in position 3 in
          the context string.</p><p role="">The UCNarrowOverhangPosClass1Set defines the
          UCNarrowOverhangPosClassRule for the second context. This
          PosClassRule is identical to the UCWideOverhangPosClassRule,
          except that the first class in the context string is a
          Class2 lowercase glyph. A SinglePos Lookup (not shown)
          increases the advance width of the overhanging uppercase
          glyph in position 0 in the context string.</p><div class="table"><a name="idm80793720512"></a><p class="title"><strong>Table 24.56. Example 11</strong></p><div class="table-contents"><table role="" class="table" summary="Example 11" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextPosFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MoveAccentsSubtable</td><td role="">ContextPos subtable
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">PosFormat</td></tr><tr><td role="">0012</td><td role="">MoveAccentsCoverage</td><td role="">Offset to Coverage table</td></tr><tr><td role="">0020</td><td role="">MoveAccentsClassDef</td><td role="">Offset to ClassDef</td></tr><tr><td role="">0005</td><td role="">5</td><td role="">PosClassSetCnt</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">PosClassSet[0], no contexts begin with Class0
                  glyphs</td></tr><tr><td role="">0060</td><td role="">UCWideOverhangPosClass1Set</td><td role="">PosClassSet[1] contexts beginning with Class1
                  glyphs</td></tr><tr><td role="">0070</td><td role="">UCNarrowOverhangPosClass2Set</td><td role="">PosClassSet[2] context beginning with Class2
                  glyphs</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">PosClassSet[3], no contexts begin with Class3
                  glyphs</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">PosClassSet[4], no contexts begin with Class4
                  glyph</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MoveAccentsCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0005</td><td role="">5</td><td role="">GlyphCount</td></tr><tr><td role="">0029</td><td role="">UppercaseFGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0033</td><td role="">UppercasePGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0037</td><td role="">UppercaseTGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">0039</td><td role="">UppercaseVGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">003A</td><td role="">UppercaseWGlyphID</td><td role="">GlyphArray[4</td></tr><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MoveAccentsClassDef</td><td role="">ClassDef table definition defines five classes = 0 (all
                  else), 1 (T, V, W: UCUnderhang), 2 (F, P:
                  UCOverhang), 3 (a, e, I, o, u: LCVowels), 4 (tilde,
                  umlaut)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">ClassFormat, ranges</td></tr><tr><td role="">000A</td><td role="">10</td><td role="">ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td role="">0029</td><td role="">UppercaseFGlyphID</td><td role="">Start</td></tr><tr><td role="">0029</td><td role="">UppercaseFGlyphID</td><td role="">End</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class ClassRangeRecord[1]</td></tr><tr><td role="">0033</td><td role="">UppercasePGlyphID</td><td role="">Start</td></tr><tr><td role="">0033</td><td role="">UppercasePGlyphID</td><td role="">End</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class ClassRangeRecord[2]</td></tr><tr><td role="">0037</td><td role="">UppercaseTGlyphID</td><td role="">Start</td></tr><tr><td role="">0037</td><td role="">UppercaseTGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class ClassRangeRecord[3]</td></tr><tr><td role="">0039</td><td role="">UppercaseVGlyphID</td><td role="">Start</td></tr><tr><td role="">003A</td><td role="">UppercaseWGlyphID</td><td role="">End</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class ClassRangeRecord[4]</td></tr><tr><td role="">0042</td><td role="">LowercaseAGlyphID</td><td role="">Start</td></tr><tr><td role="">0042</td><td role="">LowercaseAGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRangeRecord[5]</td></tr><tr><td role="">0046</td><td role="">LowercaseEGlyphID</td><td role="">Start</td></tr><tr><td role="">0046</td><td role="">LowercaseEGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRangeRecord[6]</td></tr><tr><td role="">004A</td><td role="">LowercaseIGlyphID</td><td role="">Start</td></tr><tr><td role="">004A</td><td role="">LowercaseIGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRangeRecord[7]</td></tr><tr><td role="">0051</td><td role="">LowercaseOGlyphID</td><td role="">Start</td></tr><tr><td role="">0051</td><td role="">LowercaseOGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRangeRecord[8]</td></tr><tr><td role="">0056</td><td role="">LowercaseUGlyphID</td><td role="">Start</td></tr><tr><td role="">0056</td><td role="">LowercaseUGlyphID</td><td role="">End</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRangeRecord[9]</td></tr><tr><td role="">00F5</td><td role="">TildeAccentGlyphID</td><td role="">Start</td></tr><tr><td role="">00F6</td><td role="">UmlautAccentGlyphID</td><td role="">End</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">Clas</td></tr><tr><td role=""> </td><td role="">PosClassSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">UCWideOverhangPosClass1Set</td><td role="">PosClassSet table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosClassRuleCnt</td></tr><tr><td role="">0004</td><td role="">UCWideOverhangPosClassRule</td><td role="">PosClassRule[0</td></tr><tr><td role=""> </td><td role="">PosClassRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">UCWideOverhangPosClassRule</td><td role="">PosClassRule table
                  definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosCount</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class[1], lowercase vowel</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">Class[2], accent PosLookupRecord[0]</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SequenceIndex</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex, lower the accen</td></tr><tr><td role=""> </td><td role="">PosClassSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">UCNarrowOverhangPosClass2Set</td><td role="">PosClassSet table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosClassRuleCnt</td></tr><tr><td role="">0004</td><td role="">UCNarrowOverhangPosClassRule</td><td role="">PosClassRule[0</td></tr><tr><td role=""> </td><td role="">PosClassRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">UCNarrowOverhangPosClassRule</td><td role="">PosClassRule table
                  definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosCount</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class[1], lowercase vowel</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">Class[2], accent PosLookupRecord[0]</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">SequenceIndex</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LookupListIndex increase overhang advance
                  width</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793606016"></a>Example 12: ContextPosFormat3 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.42.1"></a>Specification</h3></div></div></div><p role="">Example 12 uses a ContextPosFormat3 subtable to lower
          the position of math signs in math equations consisting of a
          lowercase descender or x-height glyph, a math sign glyph,
          and any lowercase glyph. Format3 is better to use for this
          context than the class-based Format2 because the sets of
          covered glyphs for positions 0 and 2 overlap.</p><p role="">The LowerMathSignsSubtable contains offsets to three
          Coverage tables (XhtDescLCCoverage, MathSignCoverage, and
          LCCoverage), one for each position in the context glyph
          string. When the client finds the context in the text
          stream, it applies the PosLookupRecord data at position 1
          and repositions the math sign.</p><div class="table"><a name="idm80793602640"></a><p class="title"><strong>Table 24.57. Example 12</strong></p><div class="table-contents"><table role="" class="table" summary="Example 12" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextPosFormat3</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LowerMathSignsSubtable</td><td role="">ContextPos subtable
                  definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">PosFormat</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosLookup</td></tr><tr><td role="">0010</td><td role="">XhtDescLCCoverage</td><td role="">Offset to Coverage[0] table</td></tr><tr><td role="">003C</td><td role="">MathSignCoverage</td><td role="">Offset to Coverage[1] table</td></tr><tr><td role="">0044</td><td role="">LCCoverage</td><td role="">Offset to Coverage[2] table
                  PosLookupRecord[0]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceIndex</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListInde</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">XhtDescLCCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0014</td><td role="">20</td><td role="">GlyphCount</td></tr><tr><td role="">0033</td><td role="">LCaGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">0035</td><td role="">LCcGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0037</td><td role="">LCeGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">0039</td><td role="">LCgGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">003B</td><td role="">LCiGlyphID</td><td role="">GlyphArray[4]</td></tr><tr><td role="">003C</td><td role="">LCjGlyphID</td><td role="">GlyphArray[5]</td></tr><tr><td role="">003F</td><td role="">LCmGlyphID</td><td role="">GlyphArray[6]</td></tr><tr><td role="">0040</td><td role="">LCnGlyphID</td><td role="">GlyphArray[7]</td></tr><tr><td role="">0041</td><td role="">LCoGlyphID</td><td role="">GlyphArray[8]</td></tr><tr><td role="">0042</td><td role="">LCpGlyphID</td><td role="">GlyphArray[9]</td></tr><tr><td role="">0043</td><td role="">LCqGlyphID</td><td role="">GlyphArray[10]</td></tr><tr><td role="">0044</td><td role="">LCrGlyphID</td><td role="">GlyphArray[11]</td></tr><tr><td role="">0045</td><td role="">LCsGlyphID</td><td role="">GlyphArray[12]</td></tr><tr><td role="">0046</td><td role="">LCtGlyphID</td><td role="">GlyphArray[13]</td></tr><tr><td role="">0047</td><td role="">LCuGlyphID</td><td role="">GlyphArray[14]</td></tr><tr><td role="">0048</td><td role="">LCvGlyphID</td><td role="">GlyphArray[15]</td></tr><tr><td role="">0049</td><td role="">LCwGlyphID</td><td role="">GlyphArray[16]</td></tr><tr><td role="">004A</td><td role="">LCxGlyphID</td><td role="">GlyphArray[17]</td></tr><tr><td role="">004B</td><td role="">LCyGlyphID</td><td role="">GlyphArray[18]</td></tr><tr><td role="">004C</td><td role="">LCzGlyphID</td><td role="">GlyphArray[19</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MathSignCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">011E</td><td role="">EqualsSignGlyphID</td><td role="">GlyphArray[0]</td></tr><tr><td role="">012D</td><td role="">PlusSignGlyphID</td><td role="">GlyphArray[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LCCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">RangeCount RangeRecord[0]</td></tr><tr><td role="">0033</td><td role="">LCaGlyphID</td><td role="">Start</td></tr><tr><td role="">004C</td><td role="">LCzGlyphID</td><td role="">End</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793532896"></a>Example 13: PosLookupRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.43.1"></a>Specification</h3></div></div></div><p role="">The PosLookupRecord in Example 13 identifies a lookup to
          apply at the second glyph position in a context glyph
          string.</p><div class="table"><a name="idm80793530544"></a><p class="title"><strong>Table 24.58. Example 13</strong></p><div class="table-contents"><table role="" class="table" summary="Example 13" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">PosLookupRecord</td><td role=""> </td></tr><tr><td role=""> </td><td role="">PosLookupRecord</td><td role="">0] PosLookupRecord
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceIndex for second glyph position</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex, apply this lookup to second
                  glyph position</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793522176"></a>Example 14: ValueFormat Table and ValueRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.44.1"></a>Specification</h3></div></div></div><p role="">Example 14 demonstrates how to specify positioning
          values in the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. Here, a
          SinglePosFormat1 subtable defines the ValueFormat and
          ValueRecord. The ValueFormat bit setting of 0x0099 says that
          the corresponding ValueRecord contains values for a glyph's
          XPlacement and YAdvance. Device tables specify pixel
          adjustments for these values at font sizes from 11 ppem to
          15 ppem.</p><div class="table"><a name="idm80793518848"></a><p class="title"><strong>Table 24.59. Example 14</strong></p><div class="table-contents"><table role="" class="table" summary="Example 14" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">SinglePosFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">OnesSubtable</td><td role="">SinglePos subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">PosFormat</td></tr><tr><td role="">000E</td><td role="">Cov</td><td role="">Offset to Coverage table</td></tr><tr><td role="">0099</td><td role="">0x0099</td><td role="">ValueFormat, for XPlacement, YAdvance,
                  XPlaDevice, YAdvaDevice Value</td></tr><tr><td role="">0050</td><td role="">80</td><td role="">Xplacement value</td></tr><tr><td role="">00D2</td><td role="">210</td><td role="">Yadvance value</td></tr><tr><td role="">0018</td><td role="">XPlaDeviceTable</td><td role="">Offset to XPlaDevice table</td></tr><tr><td role="">0020</td><td role="">YAdvDeviceTable</td><td role="">Offset to YAdvDevice tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">Cov</td><td role="">Coverage table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">RangeCount RangeRecord[0]</td></tr><tr><td role="">00C8</td><td role="">200</td><td role="">Start, first glyph ID in range</td></tr><tr><td role="">00D1</td><td role="">209</td><td role="">End, last glyph ID in range</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageInde</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">XPlaDeviceTable</td><td role="">Device Table definition</td></tr><tr><td role="">000B</td><td role="">11</td><td role="">StartSize</td></tr><tr><td role="">000F</td><td role="">15</td><td role="">EndSize</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">DeltaFormat</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 11ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppem by 1 pixel</td></tr><tr><td role="">5540</td><td role="">1</td><td role="">increase 15ppem by 1 pixe</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">YAdvDeviceTable</td><td role="">Device Table definition</td></tr><tr><td role="">000B</td><td role="">11</td><td role="">StartSize</td></tr><tr><td role="">000F</td><td role="">15</td><td role="">EndSize</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">DeltaFormat</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 11ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppem by 1 pixel</td></tr><tr><td role="">5540</td><td role="">1</td><td role="">increase 15ppem by 1 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793466320"></a>Example 15: AnchorFormat1 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.45.1"></a>Specification</h3></div></div></div><p role="">Example 15 illustrates an Anchor table for the damma
          mark glyph in the Arabic script. Format1 is used to specify
          X and Y coordinate values in design units.</p><div class="table"><a name="idm80793463936"></a><p class="title"><strong>Table 24.60. Example 15</strong></p><div class="table-contents"><table role="" class="table" summary="Example 15" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">AnchorFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">dammaMarkAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AnchorFormat</td></tr><tr><td role="">00BD</td><td role="">189</td><td role="">XCoordinate</td></tr><tr><td role="">FF99</td><td role="">-103</td><td role="">YCoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793454224"></a>Example 16: AnchorFormat2 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.46.1"></a>Specification</h3></div></div></div><p role="">Example 16 shows an AnchorFormat2 table for an
          attachment point placed above a base glyph. With this
          format, the coordinate value for the Anchor depends on the
          final position of a specific contour point on the base glyph
          after hinting. The coordinates are specified in design
          units.</p><div class="table"><a name="idm80793451680"></a><p class="title"><strong>Table 24.61. Example 16</strong></p><div class="table-contents"><table role="" class="table" summary="Example 16" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">AnchorFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AboveBaseAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">AnchorFormat</td></tr><tr><td role="">0142</td><td role="">322</td><td role="">XCoordinate</td></tr><tr><td role="">0384</td><td role="">900</td><td role="">Ycoordinate</td></tr><tr><td role="">000D</td><td role="">13</td><td role="">AnchorPoint glyph contour point index</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793440512"></a>Example 17: AnchorFormat3 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.47.1"></a>Specification</h3></div></div></div><p role="">Example 17 shows an AnchorFormat3 table that specifies
          an attachment point above a base glyph. Device tables modify
          the X and Y coordinates of the Anchor for the point size and
          resolution of the output font. Here, the Device tables
          define pixel adjustments for font sizes from 12 ppem to 17
          ppem.</p><div class="table"><a name="idm80793437952"></a><p class="title"><strong>Table 24.62. Example 17</strong></p><div class="table-contents"><table role="" class="table" summary="Example 17" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">AnchorFormat3</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AboveBaseAnchor</td><td role="">Anchor table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">AnchorFormat</td></tr><tr><td role="">0117</td><td role="">279</td><td role="">XCoordinate</td></tr><tr><td role="">0515</td><td role="">1301</td><td role="">YCoordinate</td></tr><tr><td role="">000A</td><td role="">XDevice</td><td role="">offset to DeviceTable for X coordinate (may be
                  NULL)</td></tr><tr><td role="">0014</td><td role="">YDevice</td><td role="">offset to Device table for Y coordinate (may be
                  NULL</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">XDevice</td><td role="">Device Table definition</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">StartSize</td></tr><tr><td role="">0011</td><td role="">17</td><td role="">EndSize</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">DeltaFormat</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppem by 1 pixel</td></tr><tr><td role="">1111</td><td role="">1</td><td role="">increase 15ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">2</td><td role="">increase 16ppem by 1 pixel</td></tr><tr><td role="">2200</td><td role="">2</td><td role="">increase 17ppem by 1 pixe</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">YDevice</td><td role="">Device Table definition</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">StartSize</td></tr><tr><td role="">0011</td><td role="">17</td><td role="">EndSize</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">DeltaFormat</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppem by 1 pixel</td></tr><tr><td role="">1111</td><td role="">1</td><td role="">increase 15ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">2</td><td role="">increase 16ppem by 1 pixel</td></tr><tr><td role="">2200</td><td role="">2</td><td role="">increase 17ppem by 1 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80793395216"></a>Example 18: MarkArray Table and MarkRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.24.48.1"></a>Specification</h3></div></div></div><p role="">Example 18 shows a MarkArray table with class and
          attachment point data for two accent marks, a grave and a
          cedilla. Two MarkRecords are defined, one for each covered
          mark glyph. The first MarkRecord assigns a mark class value
          of 0 to accents placed above base glyphs, such as the grave,
          and has an offset to a graveMarkAnchor table. The second
          MarkRecord assigns a mark class value of 1 for all accents
          positioned below base glyphs, such as the cedilla, and has
          an offset to a cedillaMarkAnchor table.</p><div class="table"><a name="idm80793392400"></a><p class="title"><strong>Table 24.63. Example 18</strong></p><div class="table-contents"><table role="" class="table" summary="Example 18" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MarkArray</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MarkGlyphsArray</td><td role="">MarkArray table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">MarkCount MarkRecord[0] for first mark in
                  MarkCoverage table, grave</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Class, for marks placed above base
                  glyphs</td></tr><tr><td role="">000A</td><td role="">graveMarkAnchor</td><td role="">offset to Anchor table MarkRecord[1] for second
                  mark in MarkCoverage table = cedilla</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class, for marks placed below base
                  glyphs</td></tr><tr><td role="">0010</td><td role="">cedillaMarkAnchor</td><td role="">offset to Anchor table</td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>