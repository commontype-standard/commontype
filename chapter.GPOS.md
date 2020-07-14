<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.GPOS"></a>Chapter 24. GPOS - The Glyph Positioning Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466591664"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.1.1"></a>Specification</h4></div></div></div><p>The Glyph Positioning table (<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>)
          provides precise control over glyph placement for
          sophisticated text layout and rendering in each script and
          language system that a font supports.</p><p>Complex glyph positioning becomes an issue in writing
          systems, such as Vietnamese, that use diacritical and other
          marks to modify the sound or meaning of characters. These
          writing systems require controlled placement of all marks in
          relation to one another for legibility and linguistic
          accuracy.</p><div class="figure"><a name="idm239466587968"></a><p class="title"><strong>Figure 24.1. Figure 4a. Vietnamese words with marks.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4a.gif" alt="Figure 4a. Vietnamese words with marks."/></div></div></div><br class="figure-break"/><p>Other writing systems require sophisticated glyph
          positioning for correct typographic composition. For
          instance, Urdu glyphs are calligraphic and connect to one
          another along a descending, diagonal text line that proceeds
          from right to left. To properly render Urdu, a
          text-processing client must modify both the horizontal (X)
          and vertical (Y) positions of each glyph.</p><div class="figure"><a name="idm239466584624"></a><p class="title"><strong>Figure 24.2. Figure 4b. Urdu layout requires glyph positioning
            control, as well as contextual substitution</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4b.gif" alt="Figure 4b. Urdu layout requires glyph positioning control, as well as contextual substitution"/></div></div></div><br class="figure-break"/><p>With the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, a font developer
          can define a complete set of positioning adjustment features
          in an CommonType font. <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> data,
          organized by script and language system, is easy for a
          text-processing client to use to position glyphs.</p><p>Positioning Glyphs with TrueType 1.0</p><p>Glyph positioning in TrueType uses only two values,
          placement and advance, to specify a glyph's position for
          text layout. If glyphs are positioned with respect to a
          virtual "pen point" that moves along a line of text,
          placement describes the glyph's position with respect to the
          current pen point, and advance describes where to move the
          pen point to position the next glyph (see Figure 4c). For
          horizontal text, placement corresponds to the left side
          bearing, and advance corresponds to the advance
          width.</p><div class="figure"><a name="idm239466579072"></a><p class="title"><strong>Figure 24.3. Figure 4c. Glyph positioning with TrueType</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4c.gif" alt="Figure 4c. Glyph positioning with TrueType"/></div></div></div><br class="figure-break"/><p>TrueType specifies placement and advance only in the X
          direction for horizontal layout and only in the Y direction
          for vertical layout. For simple Latin text layout, these two
          values may be adequate to position glyphs correctly. But,
          for texts that require more sophisticated layout, the values
          must cover a richer range. Placement and advance may need
          adjustment vertically, as well as horizontally.</p><p>The only positioning adjustment defined in TrueType is
          pair kerning, which modifies the horizontal spacing between
          two glyphs. A typical kerning table lists pairs of glyphs
          and specifies how much space a text-processing client should
          add or remove between the glyphs to properly display each
          pair. It does not provide specific information about how to
          adjust the glyphs in each pair, and cannot adjust contexts
          of more than two glyphs.</p><p>Positioning Glyphs with CommonType</p><p>CommonType fonts allow excellent control and flexibility
          for positioning a single glyph and for positioning multiple
          glyphs in relation to one another. By using both X and Y
          values that the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table defines for
          placement and advance and by using glyph attachment points,
          a client can more precisely adjust the position of a
          glyph.</p><p>In addition, the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table can
          reference a Device table to define subtle, device-dependent
          adjustments to any placement or advance value at any font
          size and device resolution. For example, a Device table can
          specify adjustments at 51 pixels per em (ppem) that do not
          occur at 50 ppem.</p><p>X and Y values specified in CommonType fonts for placement
          operations are always within the typical Cartesian
          coordinate system (origin at the baseline of the left side),
          regardless of the writing direction. Additionally, all
          values specified are done so in font unit measurements. This
          is especially convenient for font designers, since glyphs
          are drawn in the same coordinate system. However, it's
          important to note that the meaning of "advance width"
          changes, depending on the writing direction.</p><p>For example, in left-to-right scripts, if the first
          glyph has an advance width of 100, then the second glyph
          begins at 100,0. In right-to-left scripts, if the first
          glyph has an advance width of 100, then the second glyph
          begins at -100,0. For a top-to-bottom feature, to increase
          the advance height of a glyph by 100, the YAdvance = 100.
          For any feature, regardless of writing direction, to lower
          the dieresis over an 'o' by 10 units, set the YPlacement =
          -10.</p><p>Other <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> features can define
          attachment points to combine glyphs and position them with
          respect to one another. A glyph might have multiple
          attachment points. The point used will depend on the glyph
          to be attached. For instance, a base glyph could have
          attachment points for different diacritical marks.</p><div class="figure"><a name="idm239466569280"></a><p class="title"><strong>Figure 24.4. Base glyph with multiple attachment points.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../attach.gif" alt="Base glyph with multiple attachment points."/></div></div></div><br class="figure-break"/><p>To reduce the size of the font file, a base glyph may
          use the same attachment point for all mark glyphs assigned
          to a particular class. For example, a base glyph could have
          two attachment points, one above and one below the glyph.
          Then all marks that attach above glyphs would be attached at
          the high point, and all marks that attach below glyphs would
          be attached at the low point. Attachment points are useful
          in scripts, such as Arabic, that combine numerous glyphs
          with vowel marks.</p><p>Attachment points also are useful for connecting
          cursive-style glyphs. Glyphs in cursive fonts can be
          designed to attach or overlap when rendered. Alternatively,
          the font developer can use CommonType to create a cursive
          attachment feature and define explicit exit and entry
          attachment points for each glyph (see Figure 4d).</p><div class="figure"><a name="idm239466565456"></a><p class="title"><strong>Figure 24.5. Figure 4d. Entry and exit points marked on contextual
            Urdu glyph variations</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4d.gif" alt="Figure 4d. Entry and exit points marked on contextual Urdu glyph variations"/></div></div></div><br class="figure-break"/><p>The <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table supports eight types
          of actions for positioning and attaching glyphs:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>A <span class="emphasis"><em>single adjustment</em></span> positions
              one glyph, such as a superscript or subscript.</p></li><li class="listitem"><p>A <span class="emphasis"><em>pair adjustment</em></span> positions two
              glyphs with respect to one another. Kerning is an
              example of pair adjustment.</p></li><li class="listitem"><p>A <span class="emphasis"><em>cursive attachment</em></span> describes
              cursive scripts and other glyphs that are connected with
              attachment points when rendered.</p></li><li class="listitem"><p>A <span class="emphasis"><em>MarkToBase attachment</em></span>
              positions combining marks with respect to base glyphs,
              as when positioning vowels, diacritical marks, or tone
              marks in Arabic, Hebrew, and Vietnamese.</p></li><li class="listitem"><p>A <span class="emphasis"><em>MarkToLigature attachment</em></span>
              positions combining marks with respect to ligature
              glyphs. Because ligatures may have multiple points for
              attaching marks, the font developer needs to associate
              each mark with one of the ligature glyph's
              components.</p></li><li class="listitem"><p>A <span class="emphasis"><em>MarkToMark attachment</em></span>
              positions one mark relative to another, as when
              positioning tone marks with respect to vowel diacritical
              marks in Vietnamese.</p></li><li class="listitem"><p>
            <span class="emphasis"><em>Contextual positioning</em></span>
              describes how to position one or more glyphs in context,
              within an identifiable sequence of specific glyphs,
              glyph classes, or varied sets of glyphs. One or more
              positioning operations may be performed on "input"
              context sequences. Figure 4e illustrates a context for
              positioning adjustments.</p></li><li class="listitem"><p>
            <span class="emphasis"><em>Chaining Contextual positioning</em></span>
              describes how to position one or more glyphs in a
              chained context, within an identifiable sequence of
              specific glyphs, glyph classes, or varied sets of
              glyphs. One or more positioning operations may be
              performed on "input" context sequences.</p></li></ul></div><div class="figure"><a name="idm239466550624"></a><p class="title"><strong>Figure 24.6. Figure 4e. Contextual positioning lowered the accent
            over a vowel glyph that followed an overhanging uppercase
            glyph</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4e.gif" alt="Figure 4e. Contextual positioning lowered the accent over a vowel glyph that followed an overhanging uppercase glyph"/></div></div></div><br class="figure-break"/><p>Table Organization</p><p>The <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table begins with a header
          that defines offsets to a ScriptList, a FeatureList, and a
          LookupList (see Figure 4f):</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The ScriptList identifies all the scripts and
              language systems in the font that use glyph
              positioning.</p></li><li class="listitem"><p>The FeatureList defines all the glyph positioning
              features required to render these scripts and language
              systems.</p></li><li class="listitem"><p>The LookupList contains all the lookup data needed
              to implement each glyph positioning feature.</p></li></ul></div><p>For a detailed discussion of ScriptLists, FeatureLists,
          and LookupLists, see the chapter, Common Table Formats. The
          following discussion summarizes how the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table
          works.</p><div class="figure"><a name="idm239466542496"></a><p class="title"><strong>Figure 24.7. Figure 4f. High-level organization of <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
            table</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig4f.gif" alt="Figure 4f. High-level organization of GPOS table"/></div></div></div><br class="figure-break"/><p>The <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table is organized so text
          processing clients can easily locate the features and
          lookups that apply to a particular script or language
          system. To access <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> information,
          clients should use the following procedure:</p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>Locate the current script in the
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> ScriptList table.</p></li><li class="listitem"><p>If the language system is known, search the script
              for the correct LangSys table; otherwise, use the
              script's default language system (DefaultLangSys
              table).</p></li><li class="listitem"><p>The LangSys table provides index numbers into the
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> FeatureList table to access a
              required feature and a number of additional
              features.</p></li><li class="listitem"><p>Inspect the FeatureTag of each feature, and select
              the features to apply to an input glyph string.</p></li><li class="listitem"><p>Each feature provides an array of index numbers into
              the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> LookupList table. Lookup
              data is defined in one or more subtables that contain
              information about specific glyphs and the kinds of
              operations to be performed on them.</p></li><li class="listitem"><p>Assemble all lookups from the set of chosen
              features, and apply the lookups in the order given in
              the LookupList table.</p></li></ol></div><p>A lookup uses subtables to define the specific
          conditions, type, and results of a positioning action used
          to implement a feature. All subtables in a lookup must be of
          the same LookupType, as listed in the LookupType Enumeration
          table:</p><div class="table"><a name="idm239466529104"></a><p class="title"><strong>Table 24.1. LookupType Enumeration table for glyph
            positioning</strong></p><div class="table-contents"><table class="table" summary="LookupType Enumeration table for glyph&#10;            positioning" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Value</th><th>Type</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>Single adjustment</td><td>Adjust position of a single glyph</td></tr><tr><td>2</td><td>Pair adjustment</td><td>Adjust position of a pair of glyphs</td></tr><tr><td>3</td><td>Cursive attachment</td><td>Attach cursive glyphs</td></tr><tr><td>4</td><td>MarkToBase attachment</td><td>Attach a combining mark to a base glyph</td></tr><tr><td>5</td><td>MarkToLigature attachment</td><td>Attach a combining mark to a ligature</td></tr><tr><td>6</td><td>MarkToMark attachment</td><td>Attach a combining mark to another mark</td></tr><tr><td>7</td><td>Context positioning</td><td>Position one or more glyphs in context</td></tr><tr><td>8</td><td>Chained Context positioning</td><td>Position one or more glyphs in chained
                  context</td></tr><tr><td>9</td><td>Extension positioning</td><td>Extension mechanism for other positionings</td></tr><tr><td>10+</td><td>Reserved</td><td>For future use</td></tr></tbody></table></div></div><br class="table-break"/><p>Each LookupType is defined by one or more subtables,
          whose format depends on the type of positioning operation
          and the resulting storage efficiency. When glyph information
          is best presented in more than one format, a single lookup
          may define more than one subtable, as long as all the
          subtables are of the same LookupType. For example, within a
          given lookup, a glyph index array format may best represent
          one set of target glyphs, whereas a glyph index range format
          may be better for another set.</p><p>A series of positioning operations on the same glyph or
          string requires multiple lookups, one for each separate
          action. The values in the ValueRecords are accumulated in
          these cases. Each lookup is given a different array number
          in the LookupList table and is applied in the LookupList
          order.</p><p>During text processing, a client applies a lookup to
          each glyph in the string before moving to the next lookup. A
          lookup is finished for a glyph after the client locates the
          target glyph or glyph context and performs a positioning, if
          specified. To move to the "next" glyph, the client will
          typically skip all the glyphs that participated in the
          lookup operation: glyphs that were positioned as well as any
          other glyphs that formed a context for the operation.</p><p>There is just one exception: the "next" glyph in a
          sequence may be one of those that formed a context for the
          operation just performed. For example, in the case of pair
          positioning operations (i.e., kerning), if the position
          value record for the second glyph is null, that glyph is
          treated as the "next" glyph in the sequence.</p><p>This rest of this chapter describes the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> header and the subtables defined for
          each LookupType. Several <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables
          share other tables: ValueRecords, Anchor tables, and
          MarkArrays. For easy reference, the shared tables are
          described at the end of this chapter.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466503824"></a>GPOS Header</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.2.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table begins with a header
          that contains a version number (Version) initially set to
          1.0 (0x00010000) and offsets to three tables: ScriptList,
          FeatureList, and LookupList. For descriptions of these
          tables, see the chapter, Common Table Formats. Example 1 at
          the end of this chapter shows a <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          Header table definition.</p><div class="table"><a name="idm239466499936"></a><p class="title"><strong>Table 24.2. GPOS Header</strong></p><div class="table-contents"><table class="table" summary="GPOS Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Fixed</td><td>Version</td><td>Version of the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
              table-initially = 0x00010000</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ScriptList</td><td>Offset to ScriptList table-from beginning of
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>FeatureList</td><td>Offset to FeatureList table-from beginning of
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table </td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LookupList</td><td>Offset to LookupList table-from beginning of
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.2.2"></a>Annotation</h4></div></div></div><p>Nothing to note.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466486768"></a>Lookup Type 1: Single Adjustment Positioning Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.3.1"></a>Specification</h4></div></div></div><p>A single adjustment positioning subtable (SinglePos) is
          used to adjust the position of a single glyph, such as a
          subscript or superscript. In addition, a SinglePos subtable
          is commonly used to implement lookup data for contextual
          positioning.</p><p>A SinglePos subtable will have one of two formats: one
          that applies the same adjustment to a series of glyphs, or
          one that applies a different adjustment for each unique
          glyph.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.3.2"></a>Annotation</h4></div></div></div><p>None</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466481440"></a>Single Adjustment Positioning: Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.4.1"></a>Specification</h4></div></div></div><p>A SinglePosFormat1 subtable applies the same positioning
          value or values to each glyph listed in its Coverage table.
          For instance, when a font uses old-style numerals, this
          format could be applied to uniformly lower the position of
          all math operator glyphs.</p><p>The Format 1 subtable consists of a format identifier
	  (PosFormat), an offset to a Coverage table that defines the
	  glyphs to be adjusted by the positioning values (Coverage),
	  and the format identifier (ValueFormat) that describes the
	  amount and kinds of data in the ValueRecord.</p><p>The ValueRecord specifies one or more positioning values
	  to be applied to all covered glyphs (Value). For example, if
	  all glyphs in the Coverage table require both horizontal and
	  vertical adjustments, the ValueRecord will specify values
	  for both XPlacement and Yplacement.</p><p>Example 2 at the end of this chapter shows a
	  SinglePosFormat1 subtable used to adjust the placement of
	  subscript glyphs.</p><div class="table"><a name="idm239466477040"></a><p class="title"><strong>Table 24.3. SinglePosFormat1 subtable: Single positioning value</strong></p><div class="table-contents"><table class="table" summary="SinglePosFormat1 subtable: Single positioning value" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table – from beginning of
              SinglePos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat</td><td>Defines the types of data in the
              ValueRecord</td><td class="auto-generated"> </td></tr><tr><td>ValueRecord</td><td>Value</td><td>Defines positioning value(s) – applied to all
              glyphs in the Coverage table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.4.2"></a>Annotation</h4></div></div></div><p>The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>C is Coverage ∖ LookupFlag</p></li></ul></div><p>
      </p><p>The action of this subtable is to adjust the glyph
	  matched by C by {ValueFormat, Value}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466464400"></a>Single Adjustment Positioning: Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.5.1"></a>Specification</h4></div></div></div><p>A SinglePosFormat2 subtable provides an array of
          ValueRecords that contains one positioning value for each
          glyph in the Coverage table. This format is more flexible
          than Format 1, but it requires more space in the font
          file.</p><p>For example, assume that the Cyrillic script will be
          used in left-justified text. For all glyphs, Format 2 could
          define position adjustments for left side bearings to align
          the left edges of the paragraphs. To achieve this, the
          Coverage table would list every glyph in the script, and the
          SinglePosFormat2 subtable would define a ValueRecord for
          each covered glyph. Correspondingly, each ValueRecord would
          specify an XPlacement adjustment value for the left side
          bearing.</p><div class="blockquote"><blockquote class="blockquote"><p>Note: All ValueRecords defined in a SinglePos subtable
            must have the same ValueFormat. In this example, if
            XPlacement is the only value that a ValueRecord needs to
            optically align the glyphs, then XPlacement will be the
            only value specified in the ValueFormat of the
            subtable.</p></blockquote></div><p>As in Format 1, the Format 2 subtable consists of a
          format identifier (PosFormat), an offset to a Coverage table
          that defines the glyphs to be adjusted by the positioning
          values (Coverage), and the format identifier (ValueFormat)
          that describes the amount and kinds of data in the
          ValueRecords. In addition, the Format 2 subtable
          includes:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>A count of the ValueRecords (ValueCount). One
              ValueRecord is defined for each glyph in the Coverage
              table.</p></li><li class="listitem"><p>An array of ValueRecords that specify positioning
              values (Value). Because the array follows the Coverage
              Index order, the first ValueRecord applies to the first
              glyph listed in the Coverage table, and so on.</p></li></ul></div><p>Example 3 at the end of this chapter shows how to adjust
          the spacing of three dash glyphs with a SinglePosFormat2
          subtable.</p><div class="table"><a name="idm239466456208"></a><p class="title"><strong>Table 24.4. SinglePosFormat2 subtable: Array of positioning values</strong></p><div class="table-contents"><table class="table" summary="SinglePosFormat2 subtable: Array of positioning values" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier – format = 2</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table – from beginning of
              SinglePos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat</td><td>Defines the types of data in the
              ValueRecord</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueCount</td><td>Number of ValueRecords</td><td class="auto-generated"> </td></tr><tr><td>ValueRecord</td><td>Value [ValueCount]</td><td>Array of ValueRecords – positioning values
              applied to glyphs</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.5.2"></a>Annotation</h4></div></div></div><p>It is unclear whether ValueCount must equal the number of covered
          glyphs. We assume that is must be equal.</p><p>The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>C is Coverage ∖ LookupFlag</p></li></ul></div><p>
      </p><p>The action of this subtable is to adjust the glyph
	  matched by C by {ValueFormat, Value [Coverage[g]]}, where g
	  is the glyph id of the matched glyph.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466441536"></a>Lookup Type 2: Pair Adjustment Positioning Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.6.1"></a>Specification</h4></div></div></div><p>A pair adjustment positioning subtable (PairPos) is used
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
          resolution.</p><p>PairPos subtables can be either of two formats: one that
          identifies glyphs individually by index (Format 1), or one
          that identifies glyphs by class (Format 2).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466437408"></a>Pair Positioning Adjustment: Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.7.1"></a>Specification</h4></div></div></div><p>Format 1 uses glyph indices to access positioning data
          for one or more specific pairs of glyphs. All pairs are
          specified in the order determined by the layout direction of
          the text.</p><div class="blockquote"><blockquote class="blockquote"><p>Note: For text written from right to left, the
            right-most glyph will be the first glyph in a pair;
            conversely, for text written from left to right, the
            left-most glyph will be first.</p></blockquote></div><p>A PairPosFormat1 subtable contains a format identifier
          (PosFormat) and two ValueFormats:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>ValueFormat1 applies to the ValueRecord of the first
              glyph in each pair. ValueRecords for all first glyphs
              must use ValueFormat1. If ValueFormat1 is set to zero
              (0), the corresponding glyph has no ValueRecord and,
              therefore, should not be repositioned.</p></li><li class="listitem"><p>ValueFormat2 applies to the ValueRecord of the
              second glyph in each pair. ValueRecords for all second
              glyphs must use ValueFormat2. If ValueFormat2 is set to
              null, then the second glyph of the pair is the "next"
              glyph for which a lookup should be performed.</p></li></ul></div><p>A PairPos subtable also defines an offset to a Coverage
          table (Coverage) that lists the indices of the first glyphs
          in each pair. More than one pair can have the same first
          glyph, but the Coverage table will list that glyph only
          once.</p><p>The subtable also contains an array of offsets to
          PairSet tables (PairSet) and a count of the defined tables
          (PairSetCount). The PairSet array contains one offset for
          each glyph listed in the Coverage table and uses the same
          order as the Coverage Index.</p><div class="table"><a name="idm239466429552"></a><p class="title"><strong>Table 24.5. PairPosFormat1 subtable: Adjustments for glyph pairs</strong></p><div class="table-contents"><table class="table" summary="PairPosFormat1 subtable: Adjustments for glyph pairs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table - from beginning of
              PairPos subtable - only the first glyph in each
              pair</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat1</td><td>Defines the types of data in ValueRecord1 - for
              the first glyph in the pair - may be zero
              (0)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat2</td><td>Defines the types of data in ValueRecord2 - for
              the second glyph in the pair - may be zero
              (0)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PairSetCount</td><td>Number of PairSet tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>PairSetOffset [PairSetCount]</td><td>Array of offsets to PairSet tables - from
              beginning of PairPos subtable - ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A PairSet table enumerates all the glyph pairs that
          begin with a covered glyph. An array of PairValueRecords
          (PairValueRecord) contains one record for each pair and
          lists the records sorted by the GlyphID of the second glyph
          in each pair. PairValueCount specifies the number of
          PairValueRecords in the set.</p><div class="table"><a name="idm239466417200"></a><p class="title"><strong>Table 24.6. PairSet table</strong></p><div class="table-contents"><table class="table" summary="PairSet table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PairValueCount</td><td>Number of PairValueRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PairValueRecord
              [PairValueCount]</td><td>Array of PairValueRecords - ordered by GlyphID
              of the second glyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A PairValueRecord specifies the second glyph in a pair
          (SecondGlyph) and defines a ValueRecord for each glyph
          (Value1 and Value2). If ValueFormat1 is set to zero (0) in
          the PairPos subtable, ValueRecord1 will be empty; similarly,
          if ValueFormat2 is 0, Value2 will be empty.</p><p>Example 4 at the end of this chapter shows a
          PairPosFormat1 subtable that defines two cases of pair
          kerning.</p><div class="table"><a name="idm239466410608"></a><p class="title"><strong>Table 24.7. PairValueRecord</strong></p><div class="table-contents"><table class="table" summary="PairValueRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>GlyphID</td><td>SecondGlyph</td><td>GlyphID of second glyph in the pair-first
              glyph is listed in the Coverage table</td><td class="auto-generated"> </td></tr><tr><td>ValueRecord</td><td>Value1</td><td>Positioning data for the first glyph in the
              pair</td><td class="auto-generated"> </td></tr><tr><td>ValueRecord</td><td>Value2</td><td>Positioning data for the second glyph in the
              pair</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.7.2"></a>Annotation</h4></div></div></div><p>The type of the last field in PairPosFormat1 is wrong; it
          should be Offset.</p><p>It is unclear whether PairSetCount must equal the number of
          covered glyphs. We assume that it must.</p><p>It is unclear whether a PairSet entry can be null. We
	  assume that none can be.</p><p>It is unclear whether a PairValueRecord can be null. We
	  assume that none can be.</p><p>It is unclear whether ValueFormat1 and ValueFormat2 can
	  be both 0 at the same time. We assume they can be.</p><p>If ValueFormat2 ≠ 0, the pattern matched by the
	PairValueRecord r = PairSet [m].PairValueRecord [n] is
	▶ I<sub>0</sub> L*
	I<sub>1</sub> ◀, where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>I<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>1</sub> is {r.SecondGlyph}
	      ∖ LookupFlag</p></li></ul></div><p>
	  If ValueFormat2 = 0, the pattern matched by that record is
	  ▶ I<sub>0</sub> ◀ L*
	  I<sub>1</sub>.</p><p>The action of this subtable is to adjust the glyph
	  matched by I<sub>0</sub> by {ValueFormat1,
	  r.Value1} and then the glyph matched by
	  I<sub>1</sub> by {ValueFormat2,
	  r.Value2}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466392848"></a>Pair Positioning Adjustment: Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.8.1"></a>Specification</h4></div></div></div><p>Format 2 defines a pair as a set of two glyph classes
          and modifies the positions of all the glyphs in a class. For
          example, this format is useful in Japanese scripts that
          apply specific kerning operations to all glyph pairs that
          contain punctuation glyphs. One class would be defined as
          all glyphs that may be coupled with punctuation marks, and
          the other classes would be groups of similar punctuation
          glyphs.</p><p>The PairPos Format2 subtable begins with a format
          identifier (PosFormat) and an offset to a Coverage table
          (Coverage), measured from the beginning of the PairPos
          subtable. The Coverage table lists the indices of the first
          glyphs that may appear in each glyph pair. More than one
          pair may begin with the same glyph, but the Coverage table
          lists the glyph index only once.</p><p>A PairPosFormat2 subtable also includes two
          ValueFormats:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>ValueFormat1 applies to the ValueRecord of the first
              glyph in each pair. ValueRecords for all first glyphs
              must use ValueFormat1. If ValueFormat1 is set to zero
              (0), the corresponding glyph has no ValueRecord and,
              therefore, should not be repositioned.</p></li><li class="listitem"><p>ValueFormat2 applies to the ValueRecord of the
	      second glyph in each pair. ValueRecords for all second
	      glyphs must use ValueFormat2. If ValueFormat2 is set to
	      null, then the second glyph of the pair is the "next"
	      glyph for which a lookup should be performed.</p></li></ul></div><p>PairPosFormat2 requires that each glyph in all pairs be
          assigned to a class, which is identified by an integer
          called a class value. (For details about classes, see the
          chapter, Common Table Formats.) Pairs are then represented
          in a two-dimensional array as sequences of two class values.
          Multiple pairs can be represented in one Format 2
          subtable.</p><p>A PairPosFormat2 subtable contains offsets to two class
          definition tables: one that assigns class values to all the
          first glyphs in all pairs (ClassDef1), and one that assigns
          class values to all the second glyphs in all pairs
          (ClassDef2). If both glyphs in a pair use the same class
          definition, the offset value will be the same for ClassDef1
          and ClassDef2. The subtable also specifies the number of
          glyph classes defined in ClassDef1 (Class1Count) and in
          ClassDef2 (Class2Count), including Class0.</p><p>For each class identified in the ClassDef1 table, a
          Class1Record enumerates all pairs that contain a particular
          class as a first component. The Class1Record array stores
          all Class1Records according to class value.</p><div class="blockquote"><blockquote class="blockquote"><p>Note: Class1Records are not tagged with a class value
            identifier. Instead, the index value of a Class1Record in
            the array defines the class value represented by the
            record. For example, the first Class1Record enumerates
            pairs that begin with a Class 0 glyph, the second
            Class1Record enumerates pairs that begin with a Class1
            glyph, and so on.</p></blockquote></div><div class="table"><a name="idm239466382720"></a><p class="title"><strong>Table 24.8. PairPosFormat2 subtable: Class pair adjustment</strong></p><div class="table-contents"><table class="table" summary="PairPosFormat2 subtable: Class pair adjustment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table - from beginning of
              PairPos subtable - for the first glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat1</td><td>ValueRecord definition - for the first glyph of
              the pair - may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ValueFormat2</td><td>ValueRecord definition - for the second glyph
              of the pair - may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ClassDef1</td><td>Offset to ClassDef table - from beginning of
              PairPos subtable - for the first glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ClassDef2</td><td>Offset to ClassDef table - from beginning of
              PairPos subtable - for the second glyph of the
              pair</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Class1Count</td><td>Number of classes in ClassDef1 table - includes
              Class0</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Class2Count</td><td>Number of classes in ClassDef2 table - includes
              Class0</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>Class1Record [Class1Count]</td><td>Array of Class1 records - ordered by
              Class1</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each Class1Record contains an array of Class2Records
          (Class2Record), which also are ordered by class value. One
          Class2Record must be declared for each class in the
          ClassDef2 table, including Class 0.</p><div class="table"><a name="idm239466365936"></a><p class="title"><strong>Table 24.9. Class1Record</strong></p><div class="table-contents"><table class="table" summary="Class1Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>struct</td><td>Class2Record [Class2Count]</td><td>Array of Class2 records - ordered by
              Class2</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A Class2Record consists of two ValueRecords, one for the
          first glyph in a class pair (Value1) and one for the second
          glyph (Value2). If the PairPos subtable has a value of zero
          (0) for ValueFormat1 or ValueFormat2, the corresponding
          record (ValueRecord1 or ValueRecord2) will be empty.</p><p>Example 5 at the end of this chapter demonstrates pair
          kerning with glyph classes in a PairPosFormat2
          subtable.</p><div class="table"><a name="idm239466360848"></a><p class="title"><strong>Table 24.10. Class2Record</strong></p><div class="table-contents"><table class="table" summary="Class2Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ValueRecord</td><td>Value1</td><td>Positioning for first glyph - empty if
              ValueFormat1 = 0</td><td class="auto-generated"> </td></tr><tr><td>ValueRecord</td><td>Value2</td><td>Positioning for second glyph - empty if
              ValueFormat2 = 0</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.8.2"></a>Annotation</h4></div></div></div><p>It is unclear whether ValueFormat1 and ValueFormat2 can
	  be both 0 at the same time. We assume they can be.</p><p>If ValueFormat2 ≠ 0, the pattern matched by the
	Class2Record r = Class1Record
	[m].Class2Record [n] is ▶ I<sub>0</sub> L*
	I<sub>1</sub> ◀ where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>I<sub>0</sub> is ClassDef1[m] ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>1</sub> is ClassDef2[n] ∖ LookupFlag</p></li></ul></div><p>
	  If ValueFormat2 = 0, the pattern is ▶
	  I<sub>0</sub> ◀ L* I<sub>1</sub>.</p><p>The action of r is to adjust the glyph matched by
	I<sub>0</sub> by {ValueFormat1, r.Value1} and then
	the glyph matched by I<sub>1</sub> by
	{ValueFormat2, r.Value2}.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466346720"></a>Lookup Type 3: Cursive Attachment Positioning Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.9.1"></a>Specification</h4></div></div></div><p>Some cursive fonts are designed so that adjacent glyphs
          join when rendered with their default positioning. However,
          if positioning adjustments are needed to join the glyphs, a
          cursive attachment positioning (CursivePos) subtable can
          describe how to connect the glyphs by aligning two anchor
          points: the designated exit point of a glyph, and the
          designated entry point of the following glyph.</p><p>The subtable has one format: CursivePosFormat1. It
          begins with a format identifier (PosFormat) and an offset to
          a Coverage table (Coverage), which lists all the glyphs that
          define cursive attachment data.</p><p>In addition, the subtable contains one EntryExitRecord
          for each glyph listed in the Coverage table, a count of
          those records (EntryExitCount), and an array of those
          records in the same order as the Coverage Index
          (EntryExitRecord).</p><div class="table"><a name="idm239466342736"></a><p class="title"><strong>Table 24.11. CursivePosFormat1 subtable: Cursive attachment</strong></p><div class="table-contents"><table class="table" summary="CursivePosFormat1 subtable: Cursive attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table - from beginning of
              CursivePos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>EntryExitCount</td><td>Number of EntryExit records</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>EntryExitRecord [EntryExitCount]</td><td>Array of EntryExit records - in Coverage Index
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each EntryExitRecord consists of two offsets: one to an
          Anchor table that identifies the entry point on the glyph
          (EntryAnchor), and an offset to an Anchor table that
          identifies the exit point on the glyph (ExitAnchor). (For a
          complete description of the Anchor table, see the end of
          this chapter.)</p><p>To position glyphs using the CursivePosFormat1 subtable,
          a text-processing client aligns the ExitAnchor point of a
          glyph with the EntryAnchor point of the following glyph. If
          no corresponding anchor point exists, either the EntryAnchor
          or ExitAnchor offset may be NULL.</p><p>At the end of this chapter, Example 6 describes cursive
          glyph attachment in the Urdu language.</p><div class="table"><a name="idm239466332432"></a><p class="title"><strong>Table 24.12. EntryExitRecord</strong></p><div class="table-contents"><table class="table" summary="EntryExitRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>EntryAnchor</td><td>Offset to EntryAnchor table-from beginning of
              CursivePos subtable-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExitAnchor</td><td>Offset to ExitAnchor table-from beginning of
              CursivePos subtable-may be NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.9.2"></a>Annotation</h4></div></div></div><p>The specification indicates that under some
          circumstances, the ExitAnchor point of one glyph is aligned
          with the EntryAnchor of another. But it does not define
          “align” in any way: does it mean the two
          points are made to coincide, or that they are made to be on
          the same horizontal or vertical line? And what is moved to
          achieve that: the first glyph, the second glyph, both? What
          about the glyphs following the second one? The example may
          help those of you familiar with Urdu, but is otherwise
          unhelpful.</p><p>In this implementation, we assume that the second glyph
	  is moved such that the anchors coincide, and none of the
	  glyphs following the second glyph, nor any of the glyphs
	  skipped by lookupFlag between the first and second glyph
	  are moved.</p><p>We also assume that the input context is the first
	  glyph, meaning that the next glyph to process is the glyph
	  following the first glyph. The alternative is to make both
	  glyphs in the input context, but that would mean that the
	  second glyph could not be the first component of another
	  cursive attachment.</p><p>[All this is obviously wrong, but I need more work to
	  figure out how this lookup type really works.]</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466322016"></a>Lookup Type 4: MarkToBase Attachment Positioning Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.10.1"></a>Specification</h4></div></div></div><p>The MarkToBase attachment (MarkBasePos) subtable is used
          to position combining mark glyphs with respect to base
          glyphs. For example, the Arabic, Hebrew, and Thai scripts
          combine vowels, diacritical marks, and tone marks with base
          glyphs.</p><p>In the MarkBasePos subtable, every mark glyph has an
          anchor point and is associated with a class of marks. Each
          base glyph then defines an anchor point for each class of
          marks it uses.</p><p>For example, assume two mark classes: all marks
          positioned above base glyphs (Class 0), and all marks
          positioned below base glyphs (Class 1). In this case, each
          base glyph that uses these marks would define two anchor
          points, one for attaching the mark glyphs listed in Class 0,
          and one for attaching the mark glyphs listed in Class
          1.</p><p>To identify the base glyph that combines with a mark,
          the text-processing client must look backward in the glyph
          string from the mark to the preceding base glyph. To combine
          the mark and base glyph, the client aligns their attachment
          points, positioning the mark with respect to the final pen
          point (advance) position of the base glyph.</p><p>The MarkToBase Attachment subtable has one format:
          MarkBasePosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables:
          one that lists all the mark glyphs referenced in the
          subtable (MarkCoverage), and one that lists all the base
          glyphs referenced in the subtable (BaseCoverage).</p><p>For each mark glyph in the MarkCoverage table, a record
          specifies its class and an offset to the Anchor table that
          describes the mark's attachment point (MarkRecord). A mark
          class is identified by a specific integer, called a class
          value. ClassCount specifies the total number of distinct
          mark classes defined in all the MarkRecords.</p><p>The MarkBasePosFormat1 subtable also contains an offset
          to a MarkArray table, which contains all the MarkRecords
          stored in an array (MarkRecord) by MarkCoverage Index. A
          MarkArray table also contains a count of the defined
          MarkRecords (MarkCount). (For details about MarkArrays and
          MarkRecords, see the end of this chapter.)</p><p>The MarkBasePosFormat1 subtable also contains an offset
          to a BaseArray table (BaseArray).</p><div class="table"><a name="idm239466314240"></a><p class="title"><strong>Table 24.13. MarkBasePosFormat1 subtable: MarkToBase attachment point</strong></p><div class="table-contents"><table class="table" summary="MarkBasePosFormat1 subtable: MarkToBase attachment point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier –format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkCoverage</td><td>Offset to MarkCoverage table – from beginning
              of MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>BaseCoverage</td><td>Offset to BaseCoverage table – from beginning
              of MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ClassCount</td><td>Number of classes defined for
              marks</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkArray</td><td>Offset to MarkArray table – from beginning of
              MarkBasePos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>BaseArray</td><td>Offset to BaseArray table – from beginning of
              MarkBasePos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The BaseArray table consists of an array (BaseRecord)
          and count (BaseCount) of BaseRecords. The array stores the
          BaseRecords in the same order as the BaseCoverage Index.
          Each base glyph in the BaseCoverage table has a
          BaseRecord.</p><div class="table"><a name="idm239466301744"></a><p class="title"><strong>Table 24.14. BaseArray table</strong></p><div class="table-contents"><table class="table" summary="BaseArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>BaseCount</td><td>Number of BaseRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>BaseRecord [BaseCount]</td><td>Array of BaseRecords – in order of BaseCoverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A BaseRecord declares one Anchor table for each mark
          class (including Class 0) identified in the MarkRecords of
          the MarkArray. Each Anchor table specifies one attachment
          point used to attach all the marks in a particular class to
          the base glyph. A BaseRecord contains an array of offsets to
          Anchor tables (BaseAnchor). The zero-based array of offsets
          defines the entire set of attachment points each base glyph
          uses to attach marks. The offsets to Anchor tables are
          ordered by mark class.</p><div class="blockquote"><blockquote class="blockquote"><p>Note: Anchor tables are not tagged with class value
            identifiers. Instead, the index value of an Anchor table
            in the array defines the class value represented by the
            Anchor table.</p></blockquote></div><p>Example 7 at the end of this chapter defines mark
          positioning above and below base glyphs with a
          MarkBasePosFormat1 subtable.</p><div class="table"><a name="idm239466293856"></a><p class="title"><strong>Table 24.15. BaseRecord</strong></p><div class="table-contents"><table class="table" summary="BaseRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>BaseAnchor [ClassCount]</td><td>Array of offsets (one per class) to Anchor
              tables – from beginning of BaseArray table
	      – ordered by class – zero-based</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.10.2"></a>Annotation</h4></div></div></div><p>The 'text-processing' client refered to in the fourth
          paragraph is misleading. What is really meant here is "the
          virtual machine that executes the GPOS program".</p><p>The pointer to the details of MarkArrays and MarkRecords
	  should be hyperlinked.</p><p>It is important to realize that a MarkToBase subtable
          applies to the mark glyph, not to the base glyph; the
          subtable will apply at a position in a glyph run only if the
          glyph occurrence at that position is covered by the
          MarkCoverage.</p><p>It is unclear whether the mark glyph must also be
          defined as a mark glyph in GlyphClassDef in
          <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>. The specification of GDEF says that
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
          that all the glyphs in MarkCoverage be in class 3.</p><p>The same question applies to the glyphs listed in the
          BaseCoverage. Again, we suggest that those glyphs should be
          required to be in class 1 or 2 in GlyphClassDef.</p><p>The determination of the base glyph needs to be
          elaborated a little bit. In this document, we assume that
          the following was intended:</p><div class="blockquote"><blockquote class="blockquote"><p>The base glyph occurrence which may combine with the
            mark glyph occurrence is the closest preceeding occurrence
            of a glyph which does not belong to class 3 under the
            <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> GlyphClassDef. To determine the
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
            the lookup.</p></blockquote></div><p>The change to the glyph run should also be elaborated a
          bit. In this document, we assume that the following was
          intended:</p><div class="blockquote"><blockquote class="blockquote"><p>When it has been determined that the subtable applies
            to a base glyph occurrence and a mark glyph occurrence, the
            position of mark glyph occurrence is changed so that the
            anchor point of the mark glyph occurrence coincides with
            the relevant anchor point of the base glyph occurrence
            (that is, the anchor point for the mark class to which the
            mark glyph belongs). The positions of the other glyphs
            (including the glyph occurrences between the base glyph
            occurrence and the mark glyph occurrence) are
            unchanged.</p></blockquote></div><p>It is worth noting that the adjustement to the position
          of the mark glyph occurrence is a one-time deal. In other
          words, the coincidence of the anchor points is established
          at the time the lookup subtable is applied, but is not
          necessarily preserved by other lookps applied after this
          one.</p><p>The case of multiple mark glyphs on a single base glyphs
          could be noted:</p><div class="blockquote"><blockquote class="blockquote"><p>Note: Consider a typical case of Latin diacritics,
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
            accents, to achieve the desired result.</p></blockquote></div><p>The pattern matched by this subtable is B (L|NB)*
	  ▶ M ◀, where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>B is {x | x ∈ BaseCoverage ∧
		GDEF.GlyphClassDef (x) ≠ 3} ∖ LookupFlag</p></li><li class="listitem"><p>NB is {x | GDEF.GlyphClassDef (x) = 3}</p></li><li class="listitem"><p>M is MarkCoverage ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>The action is to move the glyph matched by M. More
	  precisely, if m is the glyph matched by M and b is the glyph
	  matched by B, then m is moved such that its anchor
	  MarkArray.MarkRecord[MarkCoverage [m]].MarkAnchor coincides
	  with the anchor BaseArray.BaseRecord [BaseCoverage
	  [b]].BaseAnchor [MarkArray.MarkRecord[m].Class] of b.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466270976"></a>Lookup Type 5: MarkToLigature Attachment Positioning
        Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.11.1"></a>Specification</h4></div></div></div><p>The MarkToLigature attachment (MarkLigPos) subtable is
          used to position combining mark glyphs with respect to
          ligature base glyphs. With MarkToBase attachment, described
          previously, a single base glyph defines an attachment point
          for each class of marks. In contrast, MarkToLigature
          attachment describes ligature glyphs composed of several
          components that can each define an attachment point for each
          class of marks.</p><p>As a result, a ligature glyph may have multiple base
          attachment points for one class of marks. The specific
          attachment point for a mark is defined by the ligature
          component that the subtable associates with the mark.</p><p>The MarkLigPos subtable can be used to define multiple
          mark-to-ligature attachments. In the subtable, every mark
          glyph has an anchor point and is associated with a class of
          marks. Every ligature glyph specifies a two-dimensional
          array of data: each component in a ligature defines an array
          of anchor points, one for each class of marks.</p><p>For example, assume two mark classes: all marks
          positioned above base glyphs (Class 0), and all marks
          positioned below base glyphs (Class 1). In this case, each
          component of a base ligature glyph may define two anchor
          points, one for attaching the mark glyphs listed in Class 0,
          and one for attaching the mark glyphs listed in Class 1.
          Alternatively, if the language system does not allow marks
          on the second component, the first ligature component may
          define two anchor points, one for each class of marks, and
          the second ligature component may define no anchor
          points.</p><p>To position a combining mark using a MarkToLigature
          attachment subtable, the text-processing client must work
          backward from the mark to the preceding ligature glyph. To
          correctly access the subtables, the client must keep track
          of the component associated with the mark. Aligning the
          attachment points combines the mark and ligature.</p><p>The MarkToLigature attachment subtable has one format:
          MarkLigPosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables
          that list all the mark glyphs (MarkCoverage) and Ligature
          glyphs (LigatureCoverage) referenced in the subtable.</p><p>For each glyph in the MarkCoverage table, a MarkRecord
          specifies its class and an offset to the Anchor table that
          describes the mark's attachment point. A mark class is
          identified by a specific integer, called a class value.
          ClassCount records the total number of distinct mark classes
          defined in all MarkRecords.</p><p>The MarkLigPosFormat1 subtable contains an offset,
          measured from the beginning of the subtable, to a MarkArray
          table, which contains all MarkRecords stored in an array
          (MarkRecord) by MarkCoverage Index. (For details about
          MarkArrays and MarkRecords, see the end of this
          chapter.)</p><p>The MarkLigPosFormat1 subtable also contains an offset
          to a LigatureArray table (LigatureArray).</p><div class="table"><a name="idm239466262304"></a><p class="title"><strong>Table 24.16. MarkLigPosFormat1 subtable: MarkToLigature attachment</strong></p><div class="table-contents"><table class="table" summary="MarkLigPosFormat1 subtable: MarkToLigature attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkCoverage</td><td>Offset to Mark Coverage table – from beginning
              of MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LigatureCoverage</td><td>Offset to Ligature Coverage table – from
              beginning of MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ClassCount</td><td>Number of defined mark classes</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkArray</td><td>Offset to MarkArray table – from beginning of
              MarkLigPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LigatureArray</td><td>Offset to LigatureArray table – from beginning
              of MarkLigPos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The LigatureArray table contains a count (LigatureCount)
          and an array of offsets (LigatureAttach) to LigatureAttach
          tables. The LigatureAttach array lists the offsets to</p><p>LigatureAttach tables, one for each ligature glyph
          listed in the LigatureCoverage table, in the same order as
          the LigatureCoverage Index.</p><div class="table"><a name="idm239466249328"></a><p class="title"><strong>Table 24.17. LigatureArray table</strong></p><div class="table-contents"><table class="table" summary="LigatureArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LigatureCount</td><td>Number of LigatureAttach table
              offsets</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LigatureAttach [LigatureCount]</td><td>Array of offsets to LigatureAttach
              tables – from beginning of LigatureArray table – ordered by
              LigatureCoverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each LigatureAttach table consists of an array
          (ComponentRecord) and count (ComponentCount) of the
          component glyphs in a ligature. The array stores the
          ComponentRecords in the same order as the components in the
          ligature. The order of the records also corresponds to the
          writing direction of the text. For text written left to
          right, the first component is on the left; for text written
          right to left, the first component is on the right.</p><div class="table"><a name="idm239466242832"></a><p class="title"><strong>Table 24.18. LigatureAttach table</strong></p><div class="table-contents"><table class="table" summary="LigatureAttach table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ComponentCount</td><td>Number of ComponentRecords in this
              ligature</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>ComponentRecord [ComponentCount]</td><td>Array of Component records – ordered in writing
              direction</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A ComponentRecord, one for each component in the
          ligature, contains an array of offsets to the Anchor tables
          that define all the attachment points used to attach marks
          to the component (LigatureAnchor). For each mark class
          (including Class 0) identified in the MarkArray records, an
          Anchor table specifies the point used to attach all the
          marks in a particular class to the ligature base glyph,
          relative to the component.</p><p>In a ComponentRecord, the zero-based LigatureAnchor
          array lists offsets to Anchor tables by mark class. If a
          component does not define an attachment point for a
          particular class of marks, then the offset to the
          corresponding Anchor table will be NULL.</p><p>Example 8 at the end of this chapter shows a
          MarkLisPosFormat1 subtable used to attach mark accents to a
          ligature glyph in the Arabic script.</p><div class="table"><a name="idm239466235232"></a><p class="title"><strong>Table 24.19. ComponentRecord</strong></p><div class="table-contents"><table class="table" summary="ComponentRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>LigatureAnchor [ClassCount]</td><td>Array of offsets (one per class) to Anchor
            tables – from beginning of LigatureAttach table
            – ordered by class – NULL if a component
            does not have an attachment for a class –
            zero-based array</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.11.2"></a>Annotation</h4></div></div></div><p>The 'text-processing' client refered to in the fifth
          paragraph is misleading. What is really meant here is "the
          virtual machine that executes the GPOS program".</p><p>It is important to realize that a MarkToLigature subtable
          applies to the mark glyph, not to the ligature glyph; the
          subtable will apply at a position in a glyph run only if the
          glyph occurrence at that position is covered by the
          MarkCoverage.</p><p>It is unclear whether the mark glyph must also be
          defined as a mark glyph in GlyphClassDef in
          <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>. The specification of GDEF says that
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
          that all the glyphs in MarkCoverage be in class 3.</p><p>The same question applies to the glyphs listed in the
          LigatureCoverage. Again, we suggest that those glyphs should be
          required to be in class 1 or 2 in GlyphClassDef.</p><p>The determination of the ligature glyph needs to be
          elaborated a little bit. In this document, we assume that
          the following was intended:</p><div class="blockquote"><blockquote class="blockquote"><p>The ligature glyph occurrence which may combine with the
            mark glyph occurrence is the closest preceeding occurrence
            of a glyph which does not belong to class 3 under the
            <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> GlyphClassDef. To determine the
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
            the lookup.</p></blockquote></div><p>The change to the glyph run should also be elaborated a
          bit. In this document, we assume that the following was
          intended:</p><div class="blockquote"><blockquote class="blockquote"><p>When it has been determined that the subtable applies
            to a ligature glyph occurrence and a mark glyph occurrence, the
            position of mark glyph occurrence is changed so that the
            anchor point of the mark glyph occurrence coincides with
            the relevant anchor point of the ligature glyph occurrence
            (that is, the anchor point for the mark class to which the
            mark glyph belongs). The positions of the other glyphs
            (including the glyph occurrences between the ligature glyph
            occurrence and the mark glyph occurrence) are
            unchanged.</p></blockquote></div><p>It is worth noting that the adjustement to the position
          of the mark glyph occurrence is a one-time deal. In other
          words, the coincidence of the anchor points is established
          at the time the lookup subtable is applied, but is not
          necessarily preserved by other lookps applied after this
          one.</p><p>The case of multiple mark glyphs on a single ligature glyphs
          could be noted:</p><div class="blockquote"><blockquote class="blockquote"><p>Note: Consider a typical case of Latin diacritics,
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
            accents, to achieve the desired result.</p></blockquote></div><p>The pattern matched by this subtable is B (L|NB)*
	  ▶ M ◀, where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>B is {x | x ∈ LigatureCoverage ∧
		GDEF.GlyphClassDef (x) ≠ 3} ∖ LookupFlag</p></li><li class="listitem"><p>NB is {x | GDEF.GlyphClassDef (x) = 3}</p></li><li class="listitem"><p>M is MarkCoverage ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>The action is to move the glyph matched by M. More
	  precisely, if m is the glyph matched by M, b is the glyph
	  matched by B and c is the ligature component to which the
	  mark should be attached, then m is moved such that its anchor
	  MarkArray.MarkRecord[MarkCoverage [m]].MarkAnchor coincides
	  with the anchor LigatureArray.LigatureAttach [LigatureCoverage
	  [b]].ComponentRecord [c].LigatureAnchor
	  [MarkArray.MarkRecord[m].Class] of b. It is up to the client
	  to determine to which component the mark should be attached.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469969552"></a>Lookup Type 6: MarkToMark Attachment Positioning
        Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.12.1"></a>Specification</h4></div></div></div><p>The MarkToMark attachment (MarkMarkPos) subtable is
          identical in form to the MarkToBase attachment subtable,
          although its function is different. MarkToMark attachment
          defines the position of one mark relative to another mark as
          when, for example, positioning tone marks with respect to
          vowel diacritical marks in Vietnamese.</p><p>The attaching mark is Mark1, and the base mark being
          attached to is Mark2. In the MarkMarkPos subtable, every
          Mark1 glyph has an anchor attachment point and is associated
          with a class of marks. Each Mark2 glyph defines an anchor
          point for each class of marks. For example, assume two Mark1
          classes: all marks positioned to the left of Mark2 glyphs
          (Class 0), and all marks positioned to the right of Mark2
          glyphs (Class 1). Each Mark2 glyph that uses these marks
          defines two anchor points: one for attaching the Mark1
          glyphs listed in Class 0, and one for attaching the Mark1
          glyphs listed in Class 1.</p><p>The Mark2 glyph that combines with a Mark1 glyph is the
	  glyph preceding the Mark1 glyph in glyph string order
	  (skipping glyphs according to LookupFlag). The subtable
	  applies precisely when that Mark2 glyph is covered by
	  Mark2Coverage. To combine the mark glyphs, the Mark1 glyph
	  is moved such that the relevant attachment points
	  coincide. The input context for MarkToBase, MarkToLigature
	  and MarkToMark positioning tables is the mark that is being
	  positioned. If a sequence contains several marks, a lookup
	  may act on it several times, to position them.</p><p>The MarkToMark attachment subtable has one format:
          MarkMarkPosFormat1. The subtable begins with a format
          identifier (PosFormat) and offsets to two Coverage tables:
          one that lists all the Mark1 glyphs referenced in the
          subtable (Mark1Coverage), and one that lists all the Mark2
          glyphs referenced in the subtable (Mark2Coverage).</p><p>For each mark glyph in the Mark1Coverage table, a
          MarkRecord specifies its class and an offset to the Anchor
          table that describes the mark's attachment point. A mark
          class is identified by a specific integer, called a class
          value. (For details about classes, see the chapter, Common
          Table Formats.) ClassCount specifies the total number of
          distinct mark classes defined in all the MarkRecords.</p><p>The MarkMarkPosFormat1 subtable also contains two
          offsets, measured from the beginning of the subtable, to two
          arrays:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The MarkArray table contains all MarkRecords stored
              by Mark1Coverage Index in an array (MarkRecord). The
              MarkArray table also contains a count of the number of
              defined MarkRecords (MarkCount).</p></li><li class="listitem"><p>The Mark2Array table consists of an array
              (Mark2Record) and count (Mark2Count) of
              Mark2Records.</p></li></ul></div><p>For details about MarkArrays and MarkRecords, see the
          end of this chapter.</p><div class="table"><a name="idm239469959936"></a><p class="title"><strong>Table 24.20. MarkMarkPosFormat1 subtable: MarkToMark attachment</strong></p><div class="table-contents"><table class="table" summary="MarkMarkPosFormat1 subtable: MarkToMark attachment" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Mark1Coverage</td><td>Offset to Combining Mark Coverage table-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Mark2Coverage</td><td>Offset to Base Mark Coverage table-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ClassCount</td><td>Number of Combining Mark classes
              defined</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Mark1Array</td><td>Offset to MarkArray table for Mark1-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Mark2Array</td><td>Offset to Mark2Array table for Mark2-from
              beginning of MarkMarkPos subtable</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The Mark2Array, shown next, contains one Mark2Record for
          each Mark2 glyph listed in the Mark2Coverage table. It
          stores the records in the same order as the Mark2Coverage
          Index.</p><div class="table"><a name="idm239476853888"></a><p class="title"><strong>Table 24.21. Mark2Array table</strong></p><div class="table-contents"><table class="table" summary="Mark2Array table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>Mark2Count</td><td>Number of Mark2 records</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>Mark2Record [Mark2Count]</td><td>Array of Mark2 records-in Coverage
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each Mark2Record contains an array of offsets to Anchor
          tables (Mark2Anchor). The array of zero-based offsets,
          measured from the beginning of the Mark2Array table, defines
          the entire set of Mark2 attachment points used to attach
          Mark1 glyphs to a specific Mark2 glyph. The Anchor tables in
          the Mark2Anchor array are ordered by Mark1 class
          value.</p><p>A Mark2Record declares one Anchor table for each mark
          class (including Class 0) identified in the MarkRecords of
          the MarkArray. Each Anchor table specifies one Mark2
          attachment point used to attach all the Mark1 glyphs in a
          particular class to the Mark2 glyph.</p><p>Example 9 at the end of the chapter shows a
          MarkMarkPosFormat1 subtable for attaching one mark to
          another in the Arabic script.</p><div class="table"><a name="idm239476846800"></a><p class="title"><strong>Table 24.22. Mark2Record</strong></p><div class="table-contents"><table class="table" summary="Mark2Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>Mark2Anchor [ClassCount]</td><td>Array of offsets (one per class) to Anchor
              tables-from beginning of Mark2Array table-zero-based
              array</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.12.2"></a>Annotation</h4></div></div></div><p>The annotation of the Mark2Record field should probably
	  be "... in Mark2Coverage order".</p><p>The pattern matched by this subtable is M2 L* ▶
	  M1 ◀, where:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>M2 is {x | x ∈ Mark2Coverage ∧
		GDEF.GlyphClassDef (x) = 3} ∖ LookupFlag</p></li><li class="listitem"><p>M1 is Mark1Coverage ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>The action is to move the glyph matched by M1. More
	  precisely, if m1 is the glyph matched by M1, m2 is the glyph
	  matched by M2, then m1 is moved such that its anchor
	  Mark1Array.MarkRecord [MarkCoverage [m]].MarkAnchor coincides
	  with the anchor Mark2Array.Mark2Record [Mark2Coverage
	  [m2]].Mark2Anchor [Mark1Array.MarkRecord[m].Class] of m2.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476836688"></a>Lookup Type 7: Contextual Positioning Subtables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.13.1"></a>Specification</h4></div></div></div><p>A Contextual Positioning (ContextPos) subtable defines
          the most powerful type of glyph positioning lookup. It
          describes glyph positioning in context so a text-processing
          client can adjust the position of one or more glyphs within
          a certain pattern of glyphs. Each subtable describes one or
          more "input" glyph sequences and one or more positioning
          operations to be performed on that sequence.</p><p>ContextPos subtables can have one of three formats,
          which closely mirror the formats used for contextual glyph
          substitution. One format applies to specific glyph sequences
          (Format 1), one defines the context in terms of glyph
          classes (Format 2), and the third format defines the context
          in terms of sets of glyphs (Format 3).</p><p>All ContextPos subtables specify positioning data in a
          PosLookupRecord. A description of that record follows.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476832400"></a>PosLookupRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.14.1"></a>Specification</h4></div></div></div><p>All contextual positioning subtables specify the
          positioning data in a PosLookupRecord. Each record contains
          a SequenceIndex, which indicates where the positioning
          operation will occur in the glyph sequence. In addition, a
          LookupListIndex identifies the lookup to be applied at the
          glyph position specified by the SequenceIndex.</p><p>The order in which lookups are applied to the entire
          glyph sequence, called the "design order," can be
          significant, so PosLookupRecord data should be defined
          accordingly.</p><p>The contextual substitution subtables defined in
          Examples 10, 11, and 12 show PosLookupRecords.</p><div class="table"><a name="idm239476828848"></a><p class="title"><strong>Table 24.23. PosLookupRecord</strong></p><div class="table-contents"><table class="table" summary="PosLookupRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>SequenceIndex</td><td>Index to input glyph sequence-first glyph =
              0</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookupListIndex</td><td>Lookup to apply to that
              position-zero-based</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469952752"></a>Context Positioning Subtable: Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.15.1"></a>Specification</h4></div></div></div><p>Format 1 defines the context for a glyph positioning
          operation as a particular sequence of glyphs. For example, a
          context could be &lt;To&gt;, &lt;xyzabc&gt;, &lt;!?*#@&gt;, or any
          other glyph sequence.</p><p>Within the context, Format 1 identifies particular glyph
          positions (not glyph indices) as the targets for specific
          adjustments. When a text-processing client locates a context
          in a string of text, it makes the adjustment by applying the
          lookup data defined for a targeted position at that
          location.</p><p>For example, suppose that accent mark glyphs above
          lowercase x-height vowel glyphs must be lowered when an
          overhanging capital letter glyph precedes the vowel. When
          the client locates this context in the text, the subtable
          identifies the position of the accent mark and a lookup
          index. A lookup specifies a positioning action that lowers
          the accent mark over the vowel so that it does not collide
          with the overhanging capital.</p><p>ContextPosFormat1 defines the context in two places. A
          Coverage table specifies the first glyph in the input
          sequence, and a PosRule table identifies the remaining
          glyphs. To describe the context used in the previous
          example, the Coverage table lists the glyph index of the
          first component of the sequence (the overhanging capital),
          and a PosRule table defines indices for the lowercase
          x-height vowel glyph and the accent mark.</p><p>A single ContextPosFormat1 subtable may define more than
          one context glyph sequence. If different context sequences
          begin with the same glyph, then the Coverage table should
          list the glyph only once because all first glyphs in the
          table must be unique. For example, if three contexts each
          start with an "s" and two start with a "t," then the
          Coverage table will list one "s" and one "t."</p><p>For each context, a PosRule table lists all the glyphs,
          in order, that follow the first glyph. The table also
          contains an array of PosLookupRecords that specify the
          positioning lookup data for each glyph position (including
          the first glyph position) in the context.</p><p>All the PosRule tables defining contexts that begin with
          the same first glyph are grouped together and defined in a
          PosRuleSet table. For example, the PosRule tables that
          define the three contexts that begin with an "s" are grouped
          in one PosRuleSet table, and the PosRule tables that define
          the two contexts that begin with a "t" are grouped in a
          second PosRuleSet table. Each unique glyph listed in the
          Coverage table must have a PosRuleSet table that defines all
          the PosRule tables for a covered glyph.</p><p>To locate a context glyph sequence, the text-processing
          client searches the Coverage table each time it encounters a
          new text glyph. If the glyph is covered, the client reads
          the corresponding PosRuleSet table and examines each PosRule
          table in the set to determine whether the rest of the
          context defined there matches the subsequent glyphs in the
          text. If the context and text string match, the client finds
          the target glyph position, applies the lookup for that
          position, and completes the positioning action.</p><p>A ContextPosFormat1 subtable contains a format
          identifier (PosFormat), an offset to a Coverage table
          (Coverage), a count of the number of PosRuleSets that are
          defined (PosRuleSetCount), and an array of offsets to the
          PosRuleSet tables (PosRuleSet). As mentioned, one PosRuleSet
          table must be defined for each glyph listed in the Coverage
          table.</p><p>In the PosRuleSet array, the PosRuleSet tables are
          ordered in the Coverage Index order. The first PosRuleSet in
          the array applies to the first GlyphID listed in the
          Coverage table, the second PosRuleSet in the array applies
          to the second GlyphID listed in the Coverage table, and so
          on.</p><div class="table"><a name="idm239476814512"></a><p class="title"><strong>Table 24.24. ContextPosFormat1 subtable: Simple context positioning</strong></p><div class="table-contents"><table class="table" summary="ContextPosFormat1 subtable: Simple context positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosRuleSetCount</td><td>Number of PosRuleSet tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>PosRuleSet [PosRuleSetCount]</td><td>Array of offsets to PosRuleSet tables-from
              beginning of ContextPos subtable-ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A PosRuleSet table consists of an array of offsets to
          PosRule tables (PosRule), ordered by preference, and a count
          of the PosRule tables defined in the set
          (PosRuleCount).</p><div class="table"><a name="idm239476805760"></a><p class="title"><strong>Table 24.25. PosRuleSet table: All contexts beginning with the
            same glyph</strong></p><div class="table-contents"><table class="table" summary="PosRuleSet table: All contexts beginning with the&#10;            same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosRuleCount</td><td>Number of PosRule tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>PosRule [PosRuleCount]</td><td>Array of offsets to PosRule tables-from
              beginning of PosRuleSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A PosRule table consists of a count of the glyphs to be
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
          left-most glyph will be first.</p><p>A PosRule table also contains a count of the positioning
          operations to be performed on the input glyph sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord). Each record specifies a position in the
          input glyph sequence and a LookupList index to the
          positioning lookup to be applied there. The array should
          list records in design order, or the order the lookups
          should be applied to the entire glyph sequence.</p><p>Example 10 at the end of this chapter demonstrates glyph
          kerning in context with a ContextPosFormat1 subtable.</p><div class="table"><a name="idm239476797872"></a><p class="title"><strong>Table 24.26. PosRule subtable</strong></p><div class="table-contents"><table class="table" summary="PosRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>GlyphCount</td><td>Number of glyphs in the Input glyph
              sequence</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>Input [GlyphCount-1]</td><td>Array of input GlyphIDs-starting with the
              second glyph</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [PosCount]</td><td>Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.15.2"></a>Annotation</h4></div></div></div><p>The pattern matched by the PosRule table t = PosRuleSet
	  [m].PosRule [n] is ▶
	  I<sub>0</sub> L* I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>i is t.GlyphCount</p></li><li class="listitem"><p>I<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>k</sub> is {t.Input [k-1]}
	      ∖ LookupFlag, for k &gt; 0</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>A PosRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476781376"></a>Context Positioning Subtable: Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.16.1"></a>Specification</h4></div></div></div><p>Format 2, more flexible than Format 1, describes
          class-based context positioning. For this format, a specific
          integer, called a class value, must be assigned to each
          glyph in all context glyph sequences. Contexts are then
          defined as sequences of class values. This subtable may
          define more than one context.</p><p>To clarify the notion of class-based context rules,
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
          3."</p><p>Each ContextPosFormat2 subtable contains an offset to a
          class definition table (ClassDef), which defines the class
          values of all glyphs in the input contexts that the subtable
          describes. Generally, a unique ClassDef will be declared in
          each instance of the ContextPosFormat2 subtable that is
          included in a font, even though several Format 2 subtables
          may share ClassDef tables. Classes are exclusive sets; a
          glyph cannot be in more than one class at a time. The output
          glyphs that replace the glyphs in the context sequence do
          not need class values because they are specified elsewhere
          by GlyphID.</p><p>The ContextPosFormat2 subtable also contains a format
          identifier (PosFormat) and defines an offset to a Coverage
          table (Coverage). For this format, the Coverage table lists
          indices for the complete set of glyphs (not glyph classes)
          that may appear as the first glyph of any class-based
          context. In other words, the Coverage table contains the
          list of glyph indices for all the glyphs in all classes that
          may be first in any of the context class sequences. For
          example, if the contexts begin with a Class 1 or Class 2
          glyph, then the Coverage table will list the indices of all
          Class 1 and Class 2 glyphs.</p><p>A ContextPosFormat2 subtable also defines an array of
          offsets to the PosClassSet tables (PosClassSet), along with
          a count (including Class0) of the PosClassSet tables
          (PosClassSetCnt). In the array, the PosClassSet tables are
          ordered by ascending class value (from 0 to PosClassSetCnt -
          1).</p><p>A PosClassSet array contains one offset for each glyph
          class, including Class 0. PosClassSets are not explicitly
          tagged with a class value; rather, the index value of the
          PosClassSet in the PosClassSet array defines the class that
          a PosClassSet represents.</p><p>For example, the first PosClassSet listed in the array
          contains all the PosClassRules that define contexts
          beginning with Class 0 glyphs, the second PosClassSet
          contains all PosClassRules that define contexts beginning
          with Class 1 glyphs, and so on. If no PosClassRules begin
          with a particular class (that is, if a PosClassSet contains
          no PosClassRules), then the offset to that particular
          PosClassSet in the PosClassSet array will be set to
          NULL.</p><div class="table"><a name="idm239476773696"></a><p class="title"><strong>Table 24.27. ContextPosFormat2 subtable: Class-based context glyph positioning</strong></p><div class="table-contents"><table class="table" summary="ContextPosFormat2 subtable: Class-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ClassDef</td><td>Offset to ClassDef table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosClassSetCnt</td><td>Number of PosClassSet tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>PosClassSet [PosClassSetCnt]</td><td>Array of offsets to PosClassSet tables-from
              beginning of ContextPos subtable-ordered by class-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>All the PosClassRules that define contexts beginning
          with the same class are grouped together and defined in a
          PosClassSet table. Consequently, the PosClassSet table
          identifies the class of a context's first component.</p><p>A PosClassSet enumerates all the PosClassRules that
          begin with a particular glyph class. For instance,
          PosClassSet0 represents all the PosClassRules that describe
          contexts starting with Class 0 glyphs, and PosClassSet1
          represents all the PosClassRules that define contexts
          starting with Class 1 glyphs.</p><p>Each PosClassSet table consists of a count of the
          PosClassRules defined in the PosClassSet (PosClassRuleCnt)
          and an array of offsets to PosClassRule tables
          (PosClassRule). The PosClassRule tables are ordered by
          preference in the PosClassRule array of the
          PosClassSet.</p><div class="table"><a name="idm239476761936"></a><p class="title"><strong>Table 24.28. PosClassSet table: All contexts beginning with the same class</strong></p><div class="table-contents"><table class="table" summary="PosClassSet table: All contexts beginning with the same class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosClassRuleCnt</td><td>Number of PosClassRule tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>PosClassRule [PosClassRuleCnt]</td><td>Array of offsets to PosClassRule tables-from
              beginning of PosClassSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>For each context, a PosClassRule table contains a count
          of the glyph classes in a given context (GlyphCount),
          including the first class in the context sequence. A class
          array lists the classes, beginning with the second class,
          that follow the first class in the context. The first class
          listed indicates the second position in the context
          sequence.</p><div class="blockquote"><blockquote class="blockquote"><p>Note: Text order depends on the writing direction of
            the text. For text written from right to left, the
            right-most glyph will be first. Conversely, for text
            written from left to right, the left-most glyph will be
            first.</p></blockquote></div><p>The values specified in the Class array are those
          defined in the ClassDef table. For example, consider a
          context consisting of the sequence: Class 2, Class 7, Class
          5, Class 0. The Class array will read: Class[0] = 7,
          Class[1] = 5, and Class[2] = 0. The first class in the
          sequence, Class 2, is defined by the index into the
          PosClassSet array of offsets. The total number and sequence
          of glyph classes listed in the Class array must match the
          total number and sequence of glyph classes contained in the
          input context.</p><p>A PosClassRule also contains a count of the positioning
          operations to be performed on the context (PosCount) and an
          array of PosLookupRecords (PosLookupRecord) that supply the
          positioning data. For each position in the context that
          requires a positioning operation, a PosLookupRecord
          specifies a LookupList index and a position in the input
          glyph class sequence where the lookup is applied. The
          PosLookupRecord array lists PosLookupRecords in design
          order, or the order in which lookups are applied to the
          entire glyph sequence.</p><p>Example 11 at the end of this chapter demonstrates a
          ContextPosFormat2 subtable that uses glyph classes to modify
          accent positions in glyph strings.</p><div class="table"><a name="idm239476752288"></a><p class="title"><strong>Table 24.29. PosClassRule table: One class context definition</strong></p><div class="table-contents"><table class="table" summary="PosClassRule table: One class context definition" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>GlyphCount</td><td>Number of glyphs to be matched</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Class [GlyphCount-1]</td><td>Array of classes-beginning with the second
              class-to be matched to the input glyph
              sequence</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [PosCount]</td><td>Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.16.2"></a>Annotation</h4></div></div></div><p>The pattern matched by the PosClassRule table t = PosClassSet
	  [m].PosClassRule [n] is
	  ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>i is t.GlyphCount</p></li><li class="listitem"><p>I<sub>0</sub> is (Coverage ∩
	      ClassDef [m]) ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>k</sub> is ClassDef [t.Class
	      [k-1]] ∖ LookupFlag, for k &gt; 0</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>A SubClassRule table does not directly modify the glyph
	run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476735664"></a>Context Positioning Subtable: Format 3</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.17.1"></a>Specification</h4></div></div></div><p>Format 3, coverage-based context positioning, defines a
          context rule as a sequence of coverages. Each position in
          the sequence may specify a different Coverage table for the
          set of glyphs that matches the context pattern. With Format
          3, the glyph sets defined in the different Coverage tables
          may intersect, unlike Format 2 which specifies fixed class
          assignments for the lookup (they cannot be changed at each
          position in the context sequence) and exclusive classes (a
          glyph cannot be in more than one class at a time).</p><p>For example, consider an input context that contains an
          uppercase glyph (position 0), followed by any narrow
          uppercase glyph (position 1), and then another uppercase
          glyph (position 2). This context requires three Coverage
          tables, one for each position:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>In position 0, the first position, the Coverage
              table lists the set of all uppercase glyphs.</p></li><li class="listitem"><p>In position 1, the second position, the Coverage
              table lists the set of all narrow uppercase glyphs,
              which is a subset of the glyphs listed in the Coverage
              table for position 0. </p></li><li class="listitem"><p>In position 2, the Coverage table lists the set of
              all uppercase glyphs again.</p></li></ul></div><p>Note: Both position 0 and position 2 can use the same
          Coverage table.</p><p>Unlike Formats 1 and 2, this format defines only one
          context rule at a time. It consists of a format identifier
          (PosFormat), a count of the number of glyphs in the sequence
          to be matched (GlyphCount), and an array of Coverage offsets
          that describe the input context sequence (Coverage).</p><p>Note: The Coverage tables listed in the Coverage array
          must be listed in text order according to the writing
          direction. For text written from right to left, the
          right-most glyph will be first. Conversely, for text written
          from left to right, the left-most glyph will be
          first.</p><p>The subtable also contains a count of the positioning
          operations to be performed on the input Coverage sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord) in design order, or the order in which
          lookups are applied to the entire glyph sequence.</p><p>Example 12 at the end of this chapter changes the
          positions of math sign glyphs in math equations with a
          ContextPosFormat3 subtable.</p><div class="table"><a name="idm239476725936"></a><p class="title"><strong>Table 24.30. ContextPosFormat3 subtable: Coverage-based context glyph positioning</strong></p><div class="table-contents"><table class="table" summary="ContextPosFormat3 subtable: Coverage-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GlyphCount</td><td>Number of glyphs in the input
              sequence</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage [GlyphCount]</td><td>Array of offsets to Coverage tables-from
              beginning of ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [PosCount]</td><td>Array of positioning lookups-in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.17.2"></a>Annotation</h4></div></div></div><p>The pattern matched by this subtable is ▶
	  I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>i is GlyphCount</p></li><li class="listitem"><p>I<sub>i</sub> is
		Coverage [i] ∖ LookupFlag.</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>This table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476710160"></a>Lookup Type 8: Chaining Contextual Positioning Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.18.1"></a>Specification</h4></div></div></div><p>A Chaining Contextual Positioning
          subtable(ChainContextPos)describes glyph positioning in
          context with an ability to look back and/or look ahead in
          the sequence of glyphs. The design of the Chaining
          Contextual Positioning subtable is parallel to that of the
          Contextual Positioning subtable, including the availability
          of three formats.</p><p>To specify the context, the coverage table lists the
          first glyph in the input sequence, and the ChainPosRule
          subtable defines the rest. Once a covered glyph is found at
          position i, the client reads the corresponding
          ChainPosRuleSet table and examines each table to determine
          if it matches the surrounding glyphs in the text. There is a
          match if the string &lt;backtrack sequence&gt;+&lt;input
          sequence&gt;+&lt;input sequence&gt;+&lt;lookahead sequence&gt; matches
          with the glyphs at position i - BacktrackGlyphCount in the
          text.</p><p>If there is a match, then the client finds the target
          glyphs for positioning and performs the operations. Please
          note that (just like in the ContextPosFormat1 subtable)
          these lookups are required to operate within the range of
          text from the covered glyph to the end of the input
          sequence. No positioning operations can be defined for the
          backtracking sequence or the lookahead sequence.</p><p>To clarify the ordering of glyph arrays for input,
	  backtrack and lookahead sequences, the following
	  illustration is provided. Input sequence match begins at i
	  where the input sequence match begins. The backtrack
	  sequence is ordered beginning at i-1 and increases in offset
	  value as one moves away from i. The lookahead sequence
	  begins after the input sequence and increases in logical
	  order.</p><div class="literallayout"><p><br/>
Logical order        a   b   c   d   e   f   g   h   i   j<br/>
                                     i<br/>
Input sequence                       0   1<br/>
Backtrack sequence   3   2   1   0<br/>
Lookahead sequence                           0   1   2   3<br/>
</p></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.18.2"></a>Annotation</h4></div></div></div><p>In all three formats, the sequences are represented by
	  arrays. The order in those arrays is <span class="emphasis"><em>away from the
	  current position</em></span>. In other words, if
	  <span class="emphasis"><em>i</em></span> is the current position, then the
	  first element of the backtrack array is matched against the
	  glyph at position <span class="emphasis"><em>i-1</em></span> (ignoring glyphs
	  covered by LookupFlag, as usual), and the last element of
	  the backtrack array is matched against the glyph at position
	  <span class="emphasis"><em>i - BacktrackGlyphCount</em></span>. The first
	  element of the lookahead array is matched against the glyph
	  at position <span class="emphasis"><em>i + InputGlyphCount</em></span>, and
	  the last element in that array is matched against the glyph
	  as position <span class="emphasis"><em>i + InputGlyphCount +
	  LookaheadGlyphCount - 1</em></span>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476698976"></a>Chaining Context Positioning Format 1: Simple Chaining
        Context Glyph Positioning</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.19.1"></a>Specification</h4></div></div></div><p>This Format is identical to Format 1 of Context
          Positioning lookup except that the PosRule table is replaced
          with a ChainPosRule table. (Correspondingly, the
          ChainPosRuleSet table differs from the PosRuleSet table only
          in that it lists offsets to ChainPosRule subtables instead
          of PosRule tables; and the ChainContextPosFormat1 subtable
          lists offsets to ChainPosRuleSet subtables instead of
          PosRuleSet subtables.)</p><div class="table"><a name="idm239476696256"></a><p class="title"><strong>Table 24.31. ChainContextPosFormat1 subtable: Simple context
            positioning</strong></p><div class="table-contents"><table class="table" summary="ChainContextPosFormat1 subtable: Simple context&#10;            positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table-from beginning of
              ContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ChainPosRuleSetCount</td><td>Number of ChainPosRuleSet tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ChainPosRuleSet [ChainPosRuleSetCount]</td><td>Array of offsets to ChainPosRuleSet tables-from
              beginning of ContextPos subtable-ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A ChainPosRuleSet table consists of an array of offsets
          to ChainPosRule tables (ChainPosRule), ordered by
          preference, and a count of the ChainPosRule tables defined
          in the set (ChainPosRuleCount).</p><div class="table"><a name="idm239476692544"></a><p class="title"><strong>Table 24.32. ChainPosRuleSet table: All contexts beginning with
            the same glyph</strong></p><div class="table-contents"><table class="table" summary="ChainPosRuleSet table: All contexts beginning with&#10;            the same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ChainPosRuleCount</td><td>Number of ChainPosRule tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ChainPosRule [ChainPosRuleCount]</td><td>Array of offsets to ChainPosRule tables-from
              beginning of ChainPosRuleSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm239476687232"></a><p class="title"><strong>Table 24.33. ChainPosRule subtable</strong></p><div class="table-contents"><table class="table" summary="ChainPosRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>BacktrackGlyphCount</td><td>Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>Backtrack [BacktrackGlyphCount]</td><td>Array of backtracking GlyphID's (to be
              matched before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>InputGlyphCount</td><td>Total number of glyphs in the input sequence
              (includes the first glyph)</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>Input [InputGlyphCount-1]</td><td>Array of input GlyphIDs (start with second
              glyph)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookaheadGlyphCount</td><td>Total number of glyphs in the look ahead
              sequence (number of glyphs to be matched after the input
              sequence)</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>LookAhead [LookAheadGlyphCount]</td><td>Array of lookahead GlyphID's (to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [PosCount]</td><td>Array of PosLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.19.2"></a>Annotation</h4></div></div></div><p>The pattern matched by the ChainPosRule table t = ChainPosRuleSet
	  [m].ChainPosRule [n] is

	  B<sub>b-1</sub> L* ... L* B<sub>0</sub>
          ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L*
	  ... L* A<sub>a-1</sub>, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>b is t.BacktrackGlyphCount</p></li><li class="listitem"><p>i is t.InputGlyphCount</p></li><li class="listitem"><p>a is t.LookaheadGlyphCount</p></li><li class="listitem"><p>B<sub>k</sub> is {t.Backtrack [k]} ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>0</sub> is {Coverage[m]} ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>k</sub> is {t.Input[k-1]} ∖ LookupFlag, for k &gt; 0</p></li><li class="listitem"><p>A<sub>k</sub> is {t.LookAhead[k]} ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>A SubRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239476659104"></a>Chaining Context Positioning Format 2: Class-based
        Chaining Context Glyph Positioning</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.20.1"></a>Specification</h4></div></div></div><p>This lookup Format is parallel to the Context
          Positioning format 2, with PosClassSet subtable changed to
          ChainPosClassSet subtable, and PosClassRule subtable changed
          to ChainPosClassRule subtable.</p><p>To chain contexts, three classes are used in the glyph
          ClassDef table: Backtrack ClassDef, Input ClassDef, and
          Lookahead ClassDef.</p><div class="table"><a name="idm239476656096"></a><p class="title"><strong>Table 24.34. ChainContextPosFormat2 subtable: Chaining class-based context glyph positioning</strong></p><div class="table-contents"><table class="table" summary="ChainContextPosFormat2 subtable: Chaining class-based context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage</td><td>Offset to Coverage table-from beginning of
              ChainContextPos subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>BacktrackClassDef</td><td>Offset to ClassDef table containing backtrack
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>InputClassDef</td><td>Offset to ClassDef table containing input
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LookaheadClassDef</td><td>Offset to ClassDef table containing lookahead
              sequence context-from beginning of ChainContextPos
              subtable</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ChainPosClassSetCnt</td><td>Number of ChainPosClassSet
              tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ChainPosClassSet [ChainPosClassSetCnt]</td><td>Array of offsets to ChainPosClassSet
              tables-from beginning of ChainContextPos
              subtable-ordered by input class-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>All the ChainPosClassRules that define contexts
          beginning with the same class are grouped together and
          defined in a ChainPosClassSet table. Consequently, the
          ChainPosClassSet table identifies the class of a context's
          first component.</p><div class="table"><a name="idm239469943472"></a><p class="title"><strong>Table 24.35. ChainPosClassSet table: All contexts beginning with the same class</strong></p><div class="table-contents"><table class="table" summary="ChainPosClassSet table: All contexts beginning with the same class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ChainPosClassRuleCnt</td><td>Number of ChainPosClassRule
              tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ChainPosClassRule [ChainPosClassRuleCnt]</td><td>Array of offsets to ChainPosClassRule
              tables-from beginning of ChainPosClassSet-ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm239469937952"></a><p class="title"><strong>Table 24.36. ChainPosClassRule subtable</strong></p><div class="table-contents"><table class="table" summary="ChainPosClassRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>BacktrackGlyphCount</td><td>Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Backtrack [BacktrackGlyphCount]</td><td>Array of backtracking classes(to be matched
              before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>InputGlyphCount</td><td>Total number of classes in the input sequence
              (includes the first class)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Input [InputGlyphCount-1]</td><td>Array of input classes(start with second
              class; to be matched with the input glyph
              sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookaheadGlyphCount</td><td>Total number of classes in the look ahead
              sequence (number of classes to be matched after the
              input sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookAhead [LookAheadGlyphCount]</td><td>Array of lookahead classes(to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [ChainPosCount]</td><td>Array of PosLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.20.2"></a>Annotation</h4></div></div></div><p>The pattern matched by the ChainPosClassRule table t = ChainPosClassSet [m].ChainPosRule [n] is

	  B<sub>b-1</sub> L* ... L* B<sub>0</sub>
          ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L*
	  ... L* A<sub>a-1</sub>, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>b is t.BacktrackGlyphCount</p></li><li class="listitem"><p>i is t.InputGlyphCount</p></li><li class="listitem"><p>a is t.LookaheadGlyphCount</p></li><li class="listitem"><p>B<sub>k</sub> is BacktrackClassDef
	      [t.Backtrack [k]] ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>0</sub> is (Coverage ∩
	      InputClassDef [m]) ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>k</sub> is InputClassDef
	      [t.Input [k-1]] ∖ LookupFlag, for k &gt; 0</p></li><li class="listitem"><p>A<sub>k</sub> is LookAheadClassDef
	      [t.LookAhead [k]] ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>A SubRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469908832"></a>Chaining Context Positioning Format 3: Coverage-based Chaining
        Context Glyph Positioning</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.21.1"></a>Specification</h4></div></div></div><p>Format 3 defines a chaining context rule as a sequence
          of Coverage tables. Each position in the sequence may define
          a different Coverage table for the set of glyphs that
          matches the context pattern. With Format 3, the glyph sets
          defined in the different Coverage tables may intersect,
          unlike Format 2 which specifies fixed class assignments
          (identical for each position in the backtrack, input, or
          lookahead sequence) and exclusive classes (a glyph cannot be
          in more than one class at a time).</p><div class="blockquote"><blockquote class="blockquote"><p>Note: The order of the Coverage tables listed in the
            Coverage array must follow the writing direction. For text
            written from right to left, then the right-most glyph will
            be first. Conversely, for text written from left to right,
            the left-most glyph will be first.</p></blockquote></div><p>The subtable also contains a count of the positioning
          operations to be performed on the input Coverage sequence
          (PosCount) and an array of PosLookupRecords
          (PosLookupRecord) in design order: that is, the order in
          which lookups should be applied to the entire glyph
          sequence.</p><div class="table"><a name="idm239476643040"></a><p class="title"><strong>Table 24.37. ChainContextPosFormat3 subtable: Coverage-based chaining context glyph positioning</strong></p><div class="table-contents"><table class="table" summary="ChainContextPosFormat3 subtable: Coverage-based chaining context glyph positioning" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>PosFormat</td><td>Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>BacktrackGlyphCount</td><td>Number of glyphs in the backtracking
              sequence</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage [BacktrackGlyphCount]</td><td>Array of offsets to coverage tables in
              backtracking sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>InputGlyphCount</td><td>Number of glyphs in input
              sequence</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage [InputGlyphCount]</td><td>Array of offsets to coverage tables in input
              sequence, in glyph sequence order</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookaheadGlyphCount</td><td>Number of glyphs in lookahead
              sequence</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Coverage [LookaheadGlyphCount]</td><td>Array of offsets to coverage tables in
              lookahead sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>PosCount</td><td>Number of PosLookupRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>PosLookupRecord [PosCount]</td><td>Array of PosLookupRecords, in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.21.2"></a>Annotation</h4></div></div></div><p>It is probably worth noting that InputGlyphCount should
          be non-zero, and that BacktrackGlyphCount and
          LookaheadGlyphCount can be zero.</p><p>It is unclear whether the PosCount can be 0. At first
          it seems that such a subtable is not interesting, since it
          does nothing. On the other hand, this could be useful to
          prevent the activation of following subtables. The
          recommendation is to explicitly mention that case as
          permitted.</p><p>The three fields that hold arrays of offsets to
	  coverages have the same name. We assume that their names are
	  Backtrack, Input and Lookahead.</p><p>The pattern matched by this subtable is
          B<sub>b-1</sub> L* ... L*
          B<sub>0</sub> L* ▶
	  I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L* ... L*
          A<sub>a-1</sub>, where:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>b is BacktrackGlyphCount</p></li><li class="listitem"><p>i is InputGlyphCount</p></li><li class="listitem"><p>a is LookaheadGlyphCount</p></li><li class="listitem"><p>B<sub>k</sub> is Backtrack
	      [k] ∖ LookupFlag</p></li><li class="listitem"><p>I<sub>k</sub> is
		Input [k] ∖ LookupFlag</p></li><li class="listitem"><p>A<sub>k</sub> is Lookahead
	      [k] ∖ LookupFlag</p></li><li class="listitem"><p>L is LookupFlag</p></li></ul></div><p>
      </p><p>This table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466213600"></a>Lookup Type 9: Extension Positioning</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.22.1"></a>Specification</h4></div></div></div><p>This lookup provides a mechanism whereby any other
          lookup type's subtables are stored at a 32-bit offset
          location in the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. This is
          needed if the total size of the subtables exceeds the 16-bit
          limits of the various other offsets in the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. In this specification, the
          subtable stored at the 32-bit offset location is termed the
          "extension" subtable.</p><div class="table"><a name="idm239466209648"></a><p class="title"><strong>Table 24.38. ExtensionPosFormat1 subtable</strong></p><div class="table-contents"><table class="table" summary="ExtensionPosFormat1 subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>PosFormat</td><td>Format identifier. Set to 1.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>ExtensionLookupType</td><td>Lookup type of subtable referenced by
              ExtensionOffset (i.e. the extension
              subtable).</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ExtensionOffset</td><td>Offset to the extension subtable, of lookup
              type ExtensionLookupType, relative to the start of the
              ExtensionPosFormat1 subtable.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>ExtensionLookupType must be set to any lookup type other
          than 9. All subtables in a LookupType 9 lookup must have the
          same ExtensionLookupType. All offsets in the extension
          subtables are set in the usual way, i.e. relative to the
          extension subtables themselves</p><p>When an CommonType layout engine encounters a LookupType 9
          Lookup table, it shall:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Proceed as though the Lookup table's LookupType
              field were set to the ExtensionLookupType of the
              subtables.</p></li><li class="listitem"><p>Proceed as though each extension subtable referenced
              by ExtensionOffset replaced the LookupType 9 subtable
              that referenced it.</p></li></ul></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.22.2"></a>Annotation</h4></div></div></div><p>This subtable does not match a pattern by itself, nor
	  does it have an action by itself.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466196976"></a>Shared Tables: ValueRecord, Anchor Table, and MarkArray</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.23.1"></a>Specification</h4></div></div></div><p>Several lookup subtables described earlier in this
          chapter refer to one or more of the same tables for
          positioning data: ValueRecord, Anchor table, and MarkArray.
          For easy reference, those shared tables are described
          here.</p><p>Example 14 at the end of the chapter uses a ValueFormat
          table and ValueRecord to specify positioning values in
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466192736"></a>ValueRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.24.1"></a>Specification</h4></div></div></div><p>
        <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables use ValueRecords to
          describe all the variables and values used to adjust the
          position of a glyph or set of glyphs. A ValueRecord may
          define any combination of X and Y values (in design units)
          to add to (positive values) or subtract from (negative
          values) the placement and advance values provided in the
          font. A ValueRecord also may contain an offset to a Device
          table for each of the specified values. If a ValueRecord
          specifies more than one value, the values should be listed
          in the order shown in the ValueRecord definition.</p><p>The text-processing client must be aware of the flexible
          and multi-dimensional nature of ValueRecords in the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. Because the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses ValueRecords for many
          purposes, the sizes and contents of ValueRecords may vary
          from subtable to subtable.</p><div class="table"><a name="idm239466187280"></a><p class="title"><strong>Table 24.39. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>int16</td><td>XPlacement</td><td>Horizontal adjustment for placement-in design
                  units</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>YPlacement</td><td>Vertical adjustment for placement-in design
                  units</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>XAdvance</td><td>Horizontal adjustment for advance-in design
                  units (only used for horizontal writing)</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>YAdvance</td><td>Vertical adjustment for advance-in design units
                  (only used for vertical writing)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>XPlaDevice</td><td>Offset to Device table for horizontal
                  placement-measured from beginning of PosTable (may
                  be NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>YPlaDevice</td><td>Offset to Device table for vertical
                  placement-measured from beginning of PosTable (may
                  be NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>XAdvDevice</td><td>Offset to Device table for horizontal
                  advance-measured from beginning of PosTable (may be
                  NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>YAdvDevice</td><td>Offset to Device table for vertical
                  advance-measured from beginning of PosTable (may be
                  NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A data format (ValueFormat), usually declared at the
          beginning of each <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable, defines
          the types of positioning adjustment data that ValueRecords
          specify. Usually, the same ValueFormat applies to every
          ValueRecord defined in the particular
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable.</p><p>The ValueFormat determines whether the
          ValueRecords:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Apply to placement, advance, or both.</p></li><li class="listitem"><p>Apply to the horizontal position (X coordinate), the
              vertical position (Y coordinate), or both.</p></li><li class="listitem"><p>May refer to one or more Device tables for any of
              the specified values.</p></li></ul></div><p>Each one-bit in the ValueFormat corresponds to a field
          in the ValueRecord and increases the size of the ValueRecord
          by 2 bytes. A ValueFormat of 0x0000 corresponds to an empty
          ValueRecord, which indicates no positioning changes.</p><p>To identify the fields in each ValueRecord, the
          ValueFormat uses the bit settings shown below. To specify
          multiple fields with a ValueFormat, the bit settings of the
          relevant fields are added with a logical OR
          operation.</p><p>For example, to adjust the left-side bearing of a glyph,
          the ValueFormat will be 0x0001, and the ValueRecord will
          define the XPlacement value. To adjust the advance width of
          a different glyph, the ValueFormat will be 0x0004, and the
          ValueRecord will describe the XAdvance value. To adjust both
          the XPlacement and XAdvance of a set of glyphs, the
          ValueFormat will be 0x0005, and the ValueRecord will specify
          both values in the order they are listed in the ValueRecord
          definition.</p><div class="table"><a name="idm239466165104"></a><p class="title"><strong>Table 24.40. ValueFormat bit enumeration (indicates which fields
            are present)</strong></p><div class="table-contents"><table class="table" summary="ValueFormat bit enumeration (indicates which fields&#10;            are present)" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Mask</th><th>Name</th><th>Description</th></tr></thead><tbody><tr><td>0x0001</td><td>XPlacement</td><td>Includes horizontal adjustment for
                  placement</td></tr><tr><td>0x0002</td><td>YPlacement</td><td>Includes vertical adjustment for
                  placement</td></tr><tr><td>0x0004</td><td>XAdvance</td><td>Includes horizontal adjustment for
                  advance</td></tr><tr><td>0x0008</td><td>YAdvance</td><td>Includes vertical adjustment for
                  advance</td></tr><tr><td>0x0010</td><td>XPlaDevice</td><td>Includes horizontal Device table for
                  placement</td></tr><tr><td>0x0020</td><td>YPlaDevice</td><td>Includes vertical Device table for
                  placement</td></tr><tr><td>0x0040</td><td>XAdvDevice</td><td>Includes horizontal Device table for
                  advance</td></tr><tr><td>0x0080</td><td>YAdvDevice</td><td>Includes vertical Device table for
                  advance</td></tr><tr><td>0xF000</td><td>Reserved</td><td>For future use</td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.24.2"></a>Annotation</h4></div></div></div><p>None</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239465079600"></a>Anchor Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.25.1"></a>Specification</h4></div></div></div><p>A <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses anchor points to
        position one glyph with respect to another. Each glyph defines
        an anchor point, and the text-processing client attaches the
        glyphs by aligning their corresponding anchor points.</p><p>To describe an anchor point, an Anchor table can use one
        of three formats. The first format uses design units to
        specify a location for the anchor point. The other two formats
        refine the location of the anchor point using contour points
        (Format 2) or Device tables (Format 3).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239465075264"></a>Anchor Table: Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.26.1"></a>Specification</h4></div></div></div><p>AnchorFormat1 consists of a format identifier
          (AnchorFormat) and a pair of design unit coordinates
          (XCoordinate and YCoordinate) that specify the location of
          the anchor point. This format has the benefits of small size
          and simplicity, but the anchor point cannot be hinted to
          adjust its position for different device resolutions.</p><p>Example 15 at the end of this chapter uses
          AnchorFormat1.</p><div class="table"><a name="idm239465072208"></a><p class="title"><strong>Table 24.41. AnchorFormat1 table: Design units only</strong></p><div class="table-contents"><table class="table" summary="AnchorFormat1 table: Design units only" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>AnchorFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>XCoordinate</td><td>Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>YCoordinate</td><td>Vertical value-in design units</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469899232"></a>Anchor Table: Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.27.1"></a>Specification</h4></div></div></div><p>Like AnchorFormat1, AnchorFormat2 specifies a format
          identifier (AnchorFormat) and a pair of design unit
          coordinates for the anchor point (Xcoordinate and
          Ycoordinate).</p><p>For fine-tuning the location of the anchor point,
          AnchorFormat2 also provides an index to a glyph contour
          point (AnchorPoint) that is on the outline of a glyph
          (AnchorPoint). Hinting can be used to move the AnchorPoint.
          In the rendered text, the AnchorPoint will provide the final
          positioning data for a given ppem size.</p><p>Example 16 at the end of this chapter uses
          AnchorFormat2.</p><div class="table"><a name="idm239466122048"></a><p class="title"><strong>Table 24.42. AnchorFormat2 table: Design units plus contour
            point</strong></p><div class="table-contents"><table class="table" summary="AnchorFormat2 table: Design units plus contour&#10;            point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>AnchorFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>XCoordinate</td><td>Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>YCoordinate</td><td>Vertical value-in design units</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>AnchorPoint</td><td>Index to glyph contour point</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466113504"></a>Anchor Table: Format 3</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.28.1"></a>Specification</h4></div></div></div><p>Like AnchorFormat1, AnchorFormat3 specifies a format
          identifier (AnchorFormat) and locates an anchor point
          (Xcoordinate and Ycoordinate). And, like AnchorFormat 2, it
          permits fine adjustments to the coordinate values. However,
          AnchorFormat3 uses Device tables, rather than a contour
          point, for this adjustment.</p><p>With a Device table, a client can adjust the position of
          the anchor point for any font size and device resolution.
          AnchorFormat3 can specify offsets to Device tables for the
          the X coordinate (XDeviceTable) and the Y coordinate
          (YDeviceTable). If only one coordinate requires adjustment,
          the offset to the Device table may be set to NULL for the
          other coordinate.</p><p>Example 17 at the end of the chapter shows an
          AnchorFormat3 table.</p><div class="table"><a name="idm239466109728"></a><p class="title"><strong>Table 24.43. AnchorFormat3 table: Design units plus Device
            tables</strong></p><div class="table-contents"><table class="table" summary="AnchorFormat3 table: Design units plus Device&#10;            tables" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>AnchorFormat</td><td>Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>XCoordinate</td><td>Horizontal value-in design
              units</td><td class="auto-generated"> </td></tr><tr><td>int16</td><td>YCoordinate</td><td>Vertical value-in design units</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>XDeviceTable</td><td>Offset to Device table for X coordinate- from
              beginning of Anchor table (may be NULL)</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>YDeviceTable</td><td>Offset to Device table for Y coordinate- from
              beginning of Anchor table (may be NULL)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466099552"></a>Mark Array</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.29.1"></a>Specification</h4></div></div></div><p>The MarkArray table defines the class and the anchor
          point for a mark glyph. Three <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          subtables – MarkToBase, MarkToLigature, and
          MarkToMark Attachment – use the MarkArray table to
          specify data for attaching marks.</p><p>The MarkArray table contains a count of the number of
          mark records (MarkCount) and an array of those records
          (MarkRecord). Each mark record defines the class of the mark
          and an offset to the Anchor table that contains data for the
          mark.</p><p>A class value can be 0 (zero), but the MarkRecord must
          explicitly assign that class value (this differs from the
          ClassDef table, in which all glyphs not assigned class
          values automatically belong to Class 0). The
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtables that refer to MarkArray
          tables use the class assignments for indexing zero-based
          arrays that contain data for each mark class.</p><p>In Example 18 at the end of the chapter, a MarkArray
          table and two MarkRecords define two mark classes.</p><div class="table"><a name="idm239466093792"></a><p class="title"><strong>Table 24.44. MarkArray table</strong></p><div class="table-contents"><table class="table" summary="MarkArray table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>MarkCount</td><td>Number of MarkRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>MarkRecord [MarkCount]</td><td>Array of MarkRecords – in Coverage
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm239466088608"></a><p class="title"><strong>Table 24.45. MarkRecord</strong></p><div class="table-contents"><table class="table" summary="MarkRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>Class</td><td>Class defined for this mark</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>MarkAnchor</td><td>Offset to Anchor table – from beginning of
              MarkArray table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466082848"></a>GPOS Subtable Examples</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.30.1"></a>Specification</h4></div></div></div><p>The rest of this chapter describes examples of all the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> subtable formats, including each of
          the three formats available for contextual positioning. All
          the examples reflect unique parameters described below, but
          the samples provide a useful reference for building
          subtables specific to other situations.</p><p>All the examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466078704"></a>Example 1: GPOS Header Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.31.1"></a>Specification</h4></div></div></div><p>Example 1 shows a typical <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> Header
          table definition with offsets to a ScriptList, FeatureList,
          and LookupList.</p><div class="table"><a name="idm239466075856"></a><p class="title"><strong>Table 24.46. Example 1</strong></p><div class="table-contents"><table class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>GPOSHeader</td><td> </td></tr><tr><td> </td><td>TheGPOSHeader</td><td>GPOSHeader table
                  definition</td></tr><tr><td>00010000</td><td>0x00010000</td><td>Version</td></tr><tr><td>000A</td><td>TheScriptList</td><td>offset to ScriptList table</td></tr><tr><td>001E</td><td>TheFeatureList</td><td>offset to FeatureList table</td></tr><tr><td>002C</td><td>TheLookupList</td><td>offset to LookupList table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466064960"></a>Example 2: SinglePosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.32.1"></a>Specification</h4></div></div></div><p>Example 2 uses the SinglePosFormat1 subtable to lower
          the Y placement of subscript glyphs in a font. The
          LowerSubscriptsSubTable defines one Coverage table, called
          LowerSubscriptsCoverage, which lists one range of glyph
          indices for the numeral/numeric subscript glyphs. The
          subtable's ValueFormat setting indicates that the
          ValueRecord specifies only the YPlacement value, lowering
          each subscript glyph by 80 design units.</p><div class="table"><a name="idm239466062288"></a><p class="title"><strong>Table 24.47. Example 2</strong></p><div class="table-contents"><table class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>SinglePosFormat1</td><td> </td></tr><tr><td> </td><td>LowerSubscriptsSubTable</td><td>SinglePos subtable definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>0008</td><td>LowerSubscriptsCoverage</td><td>offset to Coverage table</td></tr><tr><td>0002</td><td>0x0002</td><td>ValueFormat, YPlacement,Value[0], move Y
                  position down</td></tr><tr><td>FFB0</td><td>-80</td><td> </td></tr><tr><td> </td><td>CoverageFormat2</td><td> </td></tr><tr><td> </td><td>LowerSubscriptsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>RangeCount RangeRecord[0]</td></tr><tr><td>01B3</td><td>ZeroSubscriptGlyphID</td><td>Start, first glyphID</td></tr><tr><td>01BC</td><td>NineSubscriptGlyphID</td><td>End, last glyphID</td></tr><tr><td>0000</td><td>0</td><td>StartCoverageIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239466041968"></a>Example 3: SinglePosFormat2 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.33.1"></a>Specification</h4></div></div></div><p>This example uses a SinglePosFormat2 subtable to adjust
          the spacing of three dash glyphs by different amounts. The
          em dash spacing changes by 10 units, the en dash spacing
          changes by 25 units, and spacing of the standard dash
          changes by 50 units.</p><p>The DashSpacingSubTable contains one Coverage table with
          three dash glyph indices, plus an array of ValueRecords, one
          for each covered glyph. The ValueRecords use the same
          ValueFormat to modify the XPlacement and XAdvance values of
          each glyph. The ValueFormat bit setting of 0x0005 is
          produced by adding the XPlacement and XAdvance bit
          settings.</p><div class="table"><a name="idm239466038304"></a><p class="title"><strong>Table 24.48. Example 3</strong></p><div class="table-contents"><table class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>SinglePosFormat2</td><td> </td></tr><tr><td> </td><td>DashSpacingSubTable</td><td>SinglePos subtable
                  definition</td></tr><tr><td>0002</td><td>2</td><td>PosFormat</td></tr><tr><td>0014</td><td>DashSpacingCoverage</td><td>offset to Coverage table</td></tr><tr><td>0005</td><td>0x0005</td><td>ValueFormat for XPlacement and XAdvance</td></tr><tr><td>0003</td><td>3</td><td>ValueCount Value[0], for dash glyph</td></tr><tr><td>0032</td><td>50</td><td>XPlacement</td></tr><tr><td>0032</td><td>50</td><td>XAdvance Value[1], for en dash glyph</td></tr><tr><td>0019</td><td>25</td><td>XPlacement</td></tr><tr><td>0019</td><td>25</td><td>XAdvance Value[2], for em dash glyph</td></tr><tr><td>000A</td><td>10</td><td>XPlacement</td></tr><tr><td>000A</td><td>10</td><td>XAdvanc</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>DashSpacingCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>004F</td><td>DashGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0125</td><td>EnDashGlyphID</td><td>GlyphArray[1]</td></tr><tr><td>0129</td><td>EmDashGlyphID</td><td>GlyphArray[2]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469871344"></a>Example 4: PairPosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.34.1"></a>Specification</h4></div></div></div><p>Example 4 uses a PairPosFormat1 subtable to kern two
          glyph pairs - "Po" and "To" - by adjusting the XAdvance of
          the first glyph and the XPlacement of the second glyph. Two
          ValueFormats are defined, one for each glyph. The subtable
          contains a Coverage table that lists the index of the first
          glyph in each pair. It also contains an offset to a PairSet
          table for each covered glyph.</p><p>A PairSet table defines an array of PairValueRecords to
          specify all the glyph pairs that contain a covered glyph as
          their first component. In this example, the PPairSet table
          has one PairValueRecord that identifies the second glyph in
          the "Po" pair and two ValueRecords, one for the first glyph
          and one for the second. The TPairSet table also has one
          PairValueRecord that lists the second glyph in the "To" pair
          and two ValueRecords, one for each glyph.</p><div class="table"><a name="idm239469867856"></a><p class="title"><strong>Table 24.49. Example 4</strong></p><div class="table-contents"><table class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>PairPosFormat1</td><td> </td></tr><tr><td> </td><td>PairKerningSubTable</td><td>PairPos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>001E</td><td>PairKerningCoverage</td><td>offset to Coverage table</td></tr><tr><td>0004</td><td>0x0004</td><td>ValueFormat1 XAdvance only</td></tr><tr><td>0001</td><td>0x0001</td><td>ValueFormat2 XPlacement only</td></tr><tr><td>0002</td><td>2</td><td>PairSetCount</td></tr><tr><td>000E</td><td>PPairSetTable</td><td>PairSet[0]</td></tr><tr><td>0016</td><td>TPairSetTable</td><td>PairSet[1</td></tr><tr><td> </td><td>PairSetTable</td><td> </td></tr><tr><td> </td><td>PPairSetTable</td><td>PairSet table definition</td></tr><tr><td>0001</td><td>1</td><td>PairValueCount, one pair in set
                  PairValueRecord[0]</td></tr><tr><td>0059</td><td>LowercaseOGlyphID</td><td>SecondGlyph</td></tr><tr><td>FFE2</td><td>-30</td><td>Value 1, XAdvance adjustment for first
                  glyph</td></tr><tr><td>FFEC</td><td>-20</td><td>Value 2, XPlacement adjustment for second
                  glyp</td></tr><tr><td> </td><td>PairSetTable</td><td> </td></tr><tr><td> </td><td>PairSetTable</td><td>PairSet table definition</td></tr><tr><td>0001</td><td>1</td><td>PairValueCount one pair in set
                  PairValueRecord[0]</td></tr><tr><td>0059</td><td>LowercaseOGlyphID</td><td>SecondGlyph</td></tr><tr><td>FFD8</td><td>-40</td><td>Value1 XAdvance adjustment for first
                  glyph</td></tr><tr><td>FFE7</td><td>-25</td><td>Value 2 XPlacement adjustment for second
                  glyp</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>PairKerningCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>002D</td><td>UppercasePGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0031</td><td>UppercaseTGlyphID</td><td>GlyphArray[1]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469826896"></a>Example 5: PairPosFormat2 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.35.1"></a>Specification</h4></div></div></div><p>The PairPosFormat2 subtable in this example defines
          pairs composed of two glyph classes. Two ClassDef tables are
          defined, one for each glyph class. The first glyph in each
          pair is in a class of lowercase glyphs with diagonal shapes
          (v, w, y), defined Class1 in the LowercaseClassDef table.
          The second glyph in each pair is in a class of punctuation
          glyphs (comma and period), defined in Class1 in the
          PunctuationClassDef table. The Coverage table only lists the
          indices of the glyphs in the LowercaseClassDef table since
          they occupy the first position in the pairs.</p><p>The subtable defines two Class1Records for the classes
          defined in LowecaseClassDef, including Class0. Each record,
          in turn, defines a Class2Record for each class defined in
          PunctuationClassDef, including Class0. The Class2Records
          specify the positioning adjustments for the glyphs.</p><p>The pairs are kerned by reducing the XAdvance of the
          first glyph by 50 design units. Because no positioning
          change applies to the second glyph, its ValueFormat2 is set
          to 0, to indicate that Value2 is empty for each pair.</p><p>Since no pairs begin with Class0 or Class2 glyphs, all
          the ValueRecords referenced in Class1Record[0] contain
          values of 0 or are empty. However, Class1Record[1] does
          define an XAdvance value in its Class2Record[1] for kerning
          all pairs that contain a Class1 glyph followed by a Class2
          glyph.</p><div class="table"><a name="idm239469821920"></a><p class="title"><strong>Table 24.50. Example 5</strong></p><div class="table-contents"><table class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>PairPosFormat2</td><td> </td></tr><tr><td> </td><td>PunctKerningSubTable</td><td>PairPos subtable
                  definition</td></tr><tr><td>0002</td><td>2</td><td>PosFormat</td></tr><tr><td>0018</td><td>PunctKerningCoverage</td><td>offset to Coverage table</td></tr><tr><td>0004</td><td>0x0004</td><td>ValueFormat1 XAdvance only</td></tr><tr><td>0000</td><td>0</td><td>ValueFormat2 no ValueRecord for second
                  glyph</td></tr><tr><td>0022</td><td>LowercaseClassDef</td><td>offset to ClassDef1 table for first class in
                  pair</td></tr><tr><td>0032</td><td>PunctuationClassDef</td><td>offset to ClassDef2 table for second class in
                  pair</td></tr><tr><td>0002</td><td>2</td><td>Class1Count</td></tr><tr><td>0002</td><td>2</td><td>Class2Count Class1Record[0], no contexts begin
                  with Class0 Class2Record[0]</td></tr><tr><td>0000</td><td>0</td><td>Value1- no change for first glyph, Value2 no
                  ValueRecord for second glyph Class2Record[1]</td></tr><tr><td>0000</td><td>0</td><td>Value1- no change for first glyph, Value2 no
                  ValueRecord for second glyph Class1Record[1], for
                  contexts beginning with Class1 Class2Record[0] no
                  contexts with Class0 as second glyph</td></tr><tr><td>0000</td><td>0</td><td>Value1-no change for first glyph, Value2-no
                  ValueRecord for second glyph Class2Record[1]contexts
                  with Class1 as second glyph</td></tr><tr><td>FFCE</td><td>-50</td><td>Value1- move punctuation glyph left, Value2- no
                  ValueRecord for second glyp</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>PunctKerningCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat, lists</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>0046</td><td>LowercaseVGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0047</td><td>LowercaseWGlyphID</td><td>GlyphArray[1]</td></tr><tr><td>0049</td><td>LowercaseYGlyphID</td><td>GlyphArray[2</td></tr><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>LowercaseClassDef</td><td>ClassDef table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>ClassFormat</td></tr><tr><td>0002</td><td>2</td><td>ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td>0046</td><td>LowercaseVGlyphID</td><td>Start</td></tr><tr><td>0047</td><td>LowercaseWGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Class ClassRangeRecord[1]</td></tr><tr><td>0049</td><td>LowercaseYGlyphID</td><td>Start</td></tr><tr><td>0049</td><td>LowercaseYGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Clas</td></tr><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>PunctuationClassDef</td><td>ClassDef table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>ClassFormat</td></tr><tr><td>0001</td><td>1</td><td>ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td>006A</td><td>PeriodPunctGlyphID</td><td>Start</td></tr><tr><td>006B</td><td>CommaPunctGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Class</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469764400"></a>Example 6: CursivePosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.36.1"></a>Specification</h4></div></div></div><p>In Example 6, the Urdu language system uses a
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
          baseline.</p><div class="table"><a name="idm239469761440"></a><p class="title"><strong>Table 24.51. Example 6</strong></p><div class="table-contents"><table class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>CursivePosFormat1</td><td> </td></tr><tr><td> </td><td>DiagonalWritingSubTable</td><td>CursivePos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>000E</td><td>DiagonalWritingCoverage</td><td>offset to Coverage table</td></tr><tr><td>0002</td><td>2</td><td>EntryExitCount EntryExitRecord[0] for Kaf
                  glyph</td></tr><tr><td>0016</td><td>KafEntryAnchor</td><td>offset to EntryAnchor table</td></tr><tr><td>001C</td><td>KafExitAnchor</td><td>offset to ExitAnchor table EntryExitRecord[1]
                  for Ha glyph</td></tr><tr><td>0022</td><td>HaEntryAnchor</td><td>offset to EntryAnchor table</td></tr><tr><td>0028</td><td>HaExitAnchor</td><td>offset to ExitAnchor tabl</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>DiagonalWritingCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>0203</td><td>KafGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>027E</td><td>HaGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>KafEntryAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>05DC</td><td>1500</td><td>XCoordinate</td></tr><tr><td>002C</td><td>44</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td>KafExitAnchor</td><td>Anchor</td><td>table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0000</td><td>0</td><td>XCoordinate</td></tr><tr><td>FFEC</td><td>-20</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>HaEntryAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>05DC</td><td>1500</td><td>XCoordinate</td></tr><tr><td>002C</td><td>44</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>HaExitAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0000</td><td>0</td><td>XCoordinate</td></tr><tr><td>FFEC</td><td>-20</td><td>Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469709872"></a>Example 7: MarkBasePosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.37.1"></a>Specification</h4></div></div></div><p>The MarkBasePosFormat1 subtable in Example 7 defines one
          Arabic base glyph, Tah, and two Arabic mark glyphs: a
          fathatan mark above the base glyph, and a kasra mark below
          the base glyph. The BaseGlyphsCoverage table lists the base
          glyph, and the MarkGlyphsCoverage table lists the mark
          glyphs.</p><p>Each mark is also listed in the MarkArray, along with
          its attachment point data and a mark Class value. The
          MarkArray defines two mark classes: Class0 consists of marks
          located above base glyphs, and Class1 consists of marks
          located below base glyphs.</p><p>The BaseArray defines attachment data for base glyphs.
          In this array, one BaseRecord is defined for the Tah glyph
          with offsets to two BaseAnchor tables, one for each class of
          marks. AboveBaseAnchor defines an attachment point for marks
          placed above the Tah base glyph, and BelowBaseAnchor defines
          an attachment point for marks placed below it.</p><div class="table"><a name="idm239469705824"></a><p class="title"><strong>Table 24.52. Example 7</strong></p><div class="table-contents"><table class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>MarkBasePosFormat1</td><td> </td></tr><tr><td> </td><td>MarkBaseAttachSubTable</td><td>MarkBasePos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>000C</td><td>MarkGlyphsCoverage</td><td>offset to MarkCoverage table</td></tr><tr><td>0014</td><td>BaseGlyphsCoverage</td><td>offset to BaseCoverage table</td></tr><tr><td>0002</td><td>2</td><td>ClassCount</td></tr><tr><td>001A</td><td>MarkGlyphsArray</td><td>offset to MarkArray table</td></tr><tr><td>0030</td><td>BaseGlyphsArray</td><td>offset to BaseArray tabl</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>MarkGlyphsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>0333</td><td>fathatanMarkGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>033F</td><td>kasraMarkGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>BaseGlyphsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>0190</td><td>tahBaseGlyphID</td><td>GlyphArray[0</td></tr><tr><td> </td><td>MarkArray</td><td> </td></tr><tr><td> </td><td>MarkGlyphsArray</td><td>MarkArray table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td>0000</td><td>0</td><td>Class, for marks over base</td></tr><tr><td>000A</td><td>fathatanMarkAnchor</td><td>offset to Anchor table MarkRecord[1]</td></tr><tr><td>0001</td><td>1</td><td>Class, for marks under</td></tr><tr><td>0010</td><td>kasraMarkAnchor</td><td>offset to Anchor tabl</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>fathatanMarkAnchor</td><td>Anchor table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>015A</td><td>346</td><td>XCoordinate</td></tr><tr><td>FF9E</td><td>-98</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>kasraMarkAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0105</td><td>261</td><td>XCoordinate</td></tr><tr><td>0058</td><td>88</td><td>YCoordinat</td></tr><tr><td> </td><td>BaseArray</td><td> </td></tr><tr><td> </td><td>BaseGlyphsArray</td><td>BaseArray table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>BaseCount BaseRecord[0]</td></tr><tr><td>0006</td><td>AboveBaseAnchor</td><td>BaseAnchor[0]</td></tr><tr><td>000C</td><td>BelowBaseAnchor</td><td>BaseAnchor[1]</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>AboveBaseAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>033E</td><td>830</td><td>XCoordinate</td></tr><tr><td>0640</td><td>1600</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>BelowBaseAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>033E</td><td>830</td><td>XCoordinate</td></tr><tr><td>FFAD</td><td>-83</td><td>Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239465015616"></a>Example 8: MarkLigPosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.38.1"></a>Specification</h4></div></div></div><p>Example 8 uses the MarkLigPosFormat1 subtable to attach
          marks to a ligature glyph in the Arabic script. The
          hypothetical ligature is composed of three glyph components:
          a Lam (initial form), a meem (medial form), and a jeem
          (medial form). Accent marks are defined for the first two
          components: the sukun accent is positioned above lam, and
          the kasratan accent is placed below meem.</p><p>The LigGlyphsCoverage table lists the ligature glyph and
          the MarkGlyphsCoverage table lists the two accent marks.
          Each mark is also listed in the MarkArray, along with its
          attachment point data and a mark Class value. The MarkArray
          defines two mark classes: Class0 consists of marks located
          above base glyphs, and Class1 consists of marks located
          below base glyphs.</p><p>The LigGlyphsArray has an offset to one LigatureAttach
          table for the covered ligature glyph. This table, called
          LamWithMeemWithJeemLigAttach, defines a count and array of
          the component glyphs in the ligature. Each ComponentRecord
          defines offsets to two Anchor tables, one for each mark
          class.</p><p>In the example, the first glyph component, lam,
          specifies a high attachment point for positioning accents
          above, but does not specify a low attachment point for
          placing accents below. The second glyph component, meem,
          defines a low attachment point for placing accents below,
          but not above. The third component, jeem, has no attachment
          points since the example defines no accents for it.</p><div class="table"><a name="idm239465010560"></a><p class="title"><strong>Table 24.53. Example 8</strong></p><div class="table-contents"><table class="table" summary="Example 8" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>MarkLigPosFormat1</td><td> </td></tr><tr><td> </td><td>MarkLigAttachSubTable</td><td>MarkLigPos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>000C</td><td>MarkGlyphsCoverage</td><td>offset to MarkCoverage table</td></tr><tr><td>0014</td><td>LigGlyphsCoverage</td><td>offset to LigatureCoverage table</td></tr><tr><td>0002</td><td>2</td><td>ClassCount</td></tr><tr><td>001A</td><td>MarkGlyphsArray</td><td>offset to MarkArray table</td></tr><tr><td>0030</td><td>LigGlyphsArray</td><td>offset to LigatureArray tabl</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>MarkGlyphsCoverage</td><td>Coverage table definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>033C</td><td>sukunMarkGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>033F</td><td>kasratanMarkGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>LigGlyphsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>0234</td><td>LamWithMeemWithJeem</td><td>LigatureGlyphID GlyphArray[0</td></tr><tr><td> </td><td>MarkArray</td><td> </td></tr><tr><td> </td><td>MarkGlyphsArray</td><td>MarkArray table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td>0000</td><td>0</td><td>Class, for marks above components</td></tr><tr><td>000A</td><td>sukunMarkAnchor</td><td>offset to Anchor table MarkRecord[1]</td></tr><tr><td>0001</td><td>1</td><td>Class, for marks below components</td></tr><tr><td>0010</td><td>kasratanMarkAnchor</td><td>offset to Anchor tabl</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>sukunMarkAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>015A</td><td>346</td><td>XCoordinate</td></tr><tr><td>FF9E</td><td>-98</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>kasratanMarkAnchor</td><td>Anchor table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0105</td><td>261</td><td>XCoordinate</td></tr><tr><td>01E8</td><td>488</td><td>YCoordinat</td></tr><tr><td> </td><td>LigatureArray</td><td> </td></tr><tr><td> </td><td>LigGlyphsArray</td><td>LigatureArray table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>LigatureCount</td></tr><tr><td>0004</td><td>LamWithMeemWithJeemLigAttach</td><td>offset to LigatureAttach tabl</td></tr><tr><td> </td><td>LigatureAttach</td><td> </td></tr><tr><td> </td><td>LamWithMeemWithJeemLigAttach</td><td>LigatureAttach
                  table definition</td></tr><tr><td>0003</td><td>3</td><td>ComponentCount ComponentRecord[0] Right-to-Left
                  text order</td></tr><tr><td>000E</td><td>AboveLamAnchor</td><td>offset to LigatureAnchor table ordered by mark
                  class value for Class0 marks (above)</td></tr><tr><td>0000</td><td>NULL</td><td>offset to LigatureAnchor table no attachment
                  points for Class1 marks ComponentRecor[1]</td></tr><tr><td>0000</td><td>NULL</td><td>offset to LigatureAnchor table no attachment
                  points for Class0 marks</td></tr><tr><td>0014</td><td>BelowMeemAnchor</td><td>offset to LigatureAnchor table for Class1 marks
                  (below) ComponentRecord[2]</td></tr><tr><td>0000</td><td>NULL</td><td>offset to LigatureAnchor table no attachment
                  points for Class0 marks</td></tr><tr><td>0000</td><td>NULL</td><td>offset to LigatureAnchor table no attachment
                  points for Class1 mark</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>AboveLamAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0271</td><td>625</td><td>XCoordinate</td></tr><tr><td>0708</td><td>1800</td><td>YCoordinat</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>BelowMeemAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>0178</td><td>376</td><td>XCoordinate</td></tr><tr><td>FE90</td><td>-368</td><td>Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239464974160"></a>Example 9: MarkMarkPosFormat1 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.39.1"></a>Specification</h4></div></div></div><p>The MarkMarkPosFormat1 subtable in Example 9 defines two
          Arabic marks glyphs. The hanza mark, the base mark (Mark2),
          is identified in the Mark2GlyphsCoverage table. The damma
          mark, the attaching mark (Mark1), is defined in the
          Mark1GlyphsCoverage table.</p><p>Each Mark1 glyph is also listed in the Mark1Array, along
          with its attachment point data and a mark Class value. The
          Mark1GlyphsArray defines one mark class, Class0, that
          consists of marks located above Mark2 base glyphs. The
          Mark1GlyphsArray contains an offset to a dammaMarkAnchor
          table to specify the coordinate of the damma mark's
          attachment point.</p><p>The Mark2GlyphsArray table defines a count and an array
          of Mark2Records, one for each covered Mark2 base glyph. Each
          record contains an offset to a Mark2Anchor table for each
          Mark1 class. One Anchor table, AboveMark2Anchor, specifies a
          coordinate value for attaching the damma mark above the
          hanza base mark.</p><div class="table"><a name="idm239464969664"></a><p class="title"><strong>Table 24.54. Example 9</strong></p><div class="table-contents"><table class="table" summary="Example 9" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>MarkMarkPosFormat1</td><td> </td></tr><tr><td> </td><td>MarkMarkAttachSubTable</td><td>MarkMarkPos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>000C</td><td>Mark1GlyphsCoverage</td><td>offset to Mark1Coverage table</td></tr><tr><td>0012</td><td>Mark2GlyphsCoverage</td><td>offset to Mark2Coverage table</td></tr><tr><td>0001</td><td>1</td><td>ClassCount</td></tr><tr><td>0018</td><td>Mark1GlyphsArray</td><td>offset to Mark1Array table</td></tr><tr><td>0024</td><td>Mark2GlyphsArray</td><td>offset to Mark2Array tabl</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>Mark1GlyphsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>0296</td><td>dammaMarkGlyphID</td><td>GlyphArray[0</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>Mark2GlyphsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>0289</td><td>hanzaMarkGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>MarkArray</td><td> </td></tr><tr><td> </td><td>Mark1GlyphsArray</td><td>MarkArray table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>MarkCount MarkRecord[0] in CoverageIndex
                  order</td></tr><tr><td>0000</td><td>0</td><td>Class for marks above base mark</td></tr><tr><td>0006</td><td>dammaMarkAnchor</td><td>offset to Anchor tabl</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>dammaMarkAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>00BD</td><td>189</td><td>XCoordinate</td></tr><tr><td>FF99</td><td>-103</td><td>YCoordinat</td></tr><tr><td> </td><td>Mark2Array</td><td> </td></tr><tr><td> </td><td>Mark2GlyphsArray</td><td>Mark2Array table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>Mark2Count Mark2Record[0]</td></tr><tr><td>0004</td><td>AboveMark2Anchor</td><td>offset to Anchor table[0</td></tr><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>AboveMark2Anchor</td><td>Anchor table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>00DD</td><td>221</td><td>XCoordinate</td></tr><tr><td>012D</td><td>301</td><td>Ycoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239464915488"></a>Example 10: ContextPosFormat1 Subtable and
        PosLookupRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.40.1"></a>Specification</h4></div></div></div><p>Example 10 uses a ContextPosFormat1 subtable to adjust
          the spacing between three Arabic glyphs in a word. The
          context is the glyph sequence (from right to left): heh
          (initial form), thal (final form), and heh (isolated form).
          In the rendered word, the first two glyphs are connected,
          but the last glyph (the isolated form of heh), is separate.
          This subtable reduces the amount of space between the last
          glyph and the rest of the word.</p><p>The subtable contains a WordCoverage table that lists
          the first glyph in the word, heh (initial), and one
          PosRuleSet table, called WordPosRuleSet, that defines all
          contexts beginning with this covered glyph.</p><p>The WordPosRuleSet contains one PosRule that describes a
          word context of three glyphs and identifies the second and
          third glyphs (the first glyph is identified by the
          WordPosRuleSet). When a text-processing client locates this
          context in text, it applies a SinglePos lookup (not shown in
          the example) at position 2 to reduce the spacing between the
          glyphs.</p><div class="table"><a name="idm239464911280"></a><p class="title"><strong>Table 24.55. Example 10</strong></p><div class="table-contents"><table class="table" summary="Example 10" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ContextPosFormat1</td><td> </td></tr><tr><td> </td><td>MoveHehInSubtable</td><td>ContextPos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>0008</td><td>WordCoverage</td><td>offset to Coverage table</td></tr><tr><td>0001</td><td>1</td><td>PosRuleSetCount</td></tr><tr><td>000E</td><td>WordPosRuleSet</td><td>offset to PosRuleSet[0] tabl</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>WordCoverage</td><td>Coverage table offset</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>02A6</td><td>hehInitialGlyphID</td><td>GlyphArray[0</td></tr><tr><td> </td><td>PosRuleSet</td><td> </td></tr><tr><td> </td><td>WordPosRuleSet</td><td>PosRuleSet table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosRuleCount</td></tr><tr><td>0004</td><td>WordPosRule</td><td>Offset to PosRule[0] tabl</td></tr><tr><td> </td><td>PosRule</td><td> </td></tr><tr><td> </td><td>WordPosRule</td><td>PosRule table definition</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>0001</td><td>1</td><td>PosCount</td></tr><tr><td>02DD</td><td>thalFinalGlyphID</td><td>Input[1]</td></tr><tr><td>02C6</td><td>hehIsolatedGlyphID</td><td>Input[0] PosLookupRecord[0]</td></tr><tr><td>0002</td><td>2</td><td>SequenceIndex</td></tr><tr><td>0001</td><td>1</td><td>LookupListIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239464876528"></a>Example 11: ContextPosFormat2 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.41.1"></a>Specification</h4></div></div></div><p>The ContextPosFormat2 subtable in Example 11 defines
          context strings for five glyph classes: Class1 consists of
          uppercase glyphs that overhang and create a wide open space
          on their right side; Class2 consists of uppercase glyphs
          that overhang and create a narrow space on their right side;
          Class3 contains lowercase x-height vowels; and Class4
          contains accent glyphs placed over the lowercase vowels. The
          rest of the glyphs in the font fall into Class0.</p><p>The MoveAccentsSubtable defines two similar context
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
          accented vowel.</p><p>The MoveAccents subtable defines a MoveAccentsCoverage
          table that identifies the first glyphs in the two contexts
          and offsets to five PosClassSet tables, one for each class
          defined in the ClassDef table. Since no contexts begin with
          Class0, Class3, or Class4 glyphs, the offsets to the
          PosClassSet tables for these classes are NULL.
          PosClassSet[1] defines all contexts beginning with Class1
          glyphs; it is called UCWideOverhangPosClass1Set.
          PosClassSet[2] defines all contexts beginning with Class2
          glyphs, and it is called
          UCNarrowOverhangPosClass1Set.</p><p>Each PosClassSet defines one PosClassRule. The
          UCWideOverhangPosClass1Set uses the
          UCWideOverhangPosClassRule to specify the first context. The
          first class in this context string is identified by the
          PosClassSet that includes a PosClassRule, in this case
          Class1. The PosClassRule table lists the second and third
          classes in the context as Class3 and Class4. A SinglePos
          Lookup (not shown) lowers the accent glyph in position 3 in
          the context string.</p><p>The UCNarrowOverhangPosClass1Set defines the
          UCNarrowOverhangPosClassRule for the second context. This
          PosClassRule is identical to the UCWideOverhangPosClassRule,
          except that the first class in the context string is a
          Class2 lowercase glyph. A SinglePos Lookup (not shown)
          increases the advance width of the overhanging uppercase
          glyph in position 0 in the context string.</p><div class="table"><a name="idm239464870432"></a><p class="title"><strong>Table 24.56. Example 11</strong></p><div class="table-contents"><table class="table" summary="Example 11" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ContextPosFormat2</td><td> </td></tr><tr><td> </td><td>MoveAccentsSubtable</td><td>ContextPos subtable
                  definition</td></tr><tr><td>0002</td><td>2</td><td>PosFormat</td></tr><tr><td>0012</td><td>MoveAccentsCoverage</td><td>Offset to Coverage table</td></tr><tr><td>0020</td><td>MoveAccentsClassDef</td><td>Offset to ClassDef</td></tr><tr><td>0005</td><td>5</td><td>PosClassSetCnt</td></tr><tr><td>0000</td><td>NULL</td><td>PosClassSet[0], no contexts begin with Class0
                  glyphs</td></tr><tr><td>0060</td><td>UCWideOverhangPosClass1Set</td><td>PosClassSet[1] contexts beginning with Class1
                  glyphs</td></tr><tr><td>0070</td><td>UCNarrowOverhangPosClass2Set</td><td>PosClassSet[2] context beginning with Class2
                  glyphs</td></tr><tr><td>0000</td><td>NULL</td><td>PosClassSet[3], no contexts begin with Class3
                  glyphs</td></tr><tr><td>0000</td><td>NULL</td><td>PosClassSet[4], no contexts begin with Class4
                  glyph</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>MoveAccentsCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0005</td><td>5</td><td>GlyphCount</td></tr><tr><td>0029</td><td>UppercaseFGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0033</td><td>UppercasePGlyphID</td><td>GlyphArray[1]</td></tr><tr><td>0037</td><td>UppercaseTGlyphID</td><td>GlyphArray[2]</td></tr><tr><td>0039</td><td>UppercaseVGlyphID</td><td>GlyphArray[3]</td></tr><tr><td>003A</td><td>UppercaseWGlyphID</td><td>GlyphArray[4</td></tr><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>MoveAccentsClassDef</td><td>ClassDef table definition defines five classes = 0 (all
                  else), 1 (T, V, W: UCUnderhang), 2 (F, P:
                  UCOverhang), 3 (a, e, I, o, u: LCVowels), 4 (tilde,
                  umlaut)</td></tr><tr><td>0002</td><td>2</td><td>ClassFormat, ranges</td></tr><tr><td>000A</td><td>10</td><td>ClassRangeCount ClassRangeRecord[0]</td></tr><tr><td>0029</td><td>UppercaseFGlyphID</td><td>Start</td></tr><tr><td>0029</td><td>UppercaseFGlyphID</td><td>End</td></tr><tr><td>0002</td><td>2</td><td>Class ClassRangeRecord[1]</td></tr><tr><td>0033</td><td>UppercasePGlyphID</td><td>Start</td></tr><tr><td>0033</td><td>UppercasePGlyphID</td><td>End</td></tr><tr><td>0002</td><td>2</td><td>Class ClassRangeRecord[2]</td></tr><tr><td>0037</td><td>UppercaseTGlyphID</td><td>Start</td></tr><tr><td>0037</td><td>UppercaseTGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Class ClassRangeRecord[3]</td></tr><tr><td>0039</td><td>UppercaseVGlyphID</td><td>Start</td></tr><tr><td>003A</td><td>UppercaseWGlyphID</td><td>End</td></tr><tr><td>0001</td><td>1</td><td>Class ClassRangeRecord[4]</td></tr><tr><td>0042</td><td>LowercaseAGlyphID</td><td>Start</td></tr><tr><td>0042</td><td>LowercaseAGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class ClassRangeRecord[5]</td></tr><tr><td>0046</td><td>LowercaseEGlyphID</td><td>Start</td></tr><tr><td>0046</td><td>LowercaseEGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class ClassRangeRecord[6]</td></tr><tr><td>004A</td><td>LowercaseIGlyphID</td><td>Start</td></tr><tr><td>004A</td><td>LowercaseIGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class ClassRangeRecord[7]</td></tr><tr><td>0051</td><td>LowercaseOGlyphID</td><td>Start</td></tr><tr><td>0051</td><td>LowercaseOGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class ClassRangeRecord[8]</td></tr><tr><td>0056</td><td>LowercaseUGlyphID</td><td>Start</td></tr><tr><td>0056</td><td>LowercaseUGlyphID</td><td>End</td></tr><tr><td>0003</td><td>3</td><td>Class ClassRangeRecord[9]</td></tr><tr><td>00F5</td><td>TildeAccentGlyphID</td><td>Start</td></tr><tr><td>00F6</td><td>UmlautAccentGlyphID</td><td>End</td></tr><tr><td>0004</td><td>4</td><td>Clas</td></tr><tr><td> </td><td>PosClassSet</td><td> </td></tr><tr><td> </td><td>UCWideOverhangPosClass1Set</td><td>PosClassSet table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosClassRuleCnt</td></tr><tr><td>0004</td><td>UCWideOverhangPosClassRule</td><td>PosClassRule[0</td></tr><tr><td> </td><td>PosClassRule</td><td> </td></tr><tr><td> </td><td>UCWideOverhangPosClassRule</td><td>PosClassRule table
                  definition</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>0001</td><td>1</td><td>PosCount</td></tr><tr><td>0003</td><td>3</td><td>Class[1], lowercase vowel</td></tr><tr><td>0004</td><td>4</td><td>Class[2], accent PosLookupRecord[0]</td></tr><tr><td>0002</td><td>2</td><td>SequenceIndex</td></tr><tr><td>0001</td><td>1</td><td>LookupListIndex, lower the accen</td></tr><tr><td> </td><td>PosClassSet</td><td> </td></tr><tr><td> </td><td>UCNarrowOverhangPosClass2Set</td><td>PosClassSet table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosClassRuleCnt</td></tr><tr><td>0004</td><td>UCNarrowOverhangPosClassRule</td><td>PosClassRule[0</td></tr><tr><td> </td><td>PosClassRule</td><td> </td></tr><tr><td> </td><td>UCNarrowOverhangPosClassRule</td><td>PosClassRule table
                  definition</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>0001</td><td>1</td><td>PosCount</td></tr><tr><td>0003</td><td>3</td><td>Class[1], lowercase vowel</td></tr><tr><td>0004</td><td>4</td><td>Class[2], accent PosLookupRecord[0]</td></tr><tr><td>0000</td><td>0</td><td>SequenceIndex</td></tr><tr><td>0002</td><td>2</td><td>LookupListIndex increase overhang advance
                  width</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469529440"></a>Example 12: ContextPosFormat3 Subtable</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.42.1"></a>Specification</h4></div></div></div><p>Example 12 uses a ContextPosFormat3 subtable to lower
          the position of math signs in math equations consisting of a
          lowercase descender or x-height glyph, a math sign glyph,
          and any lowercase glyph. Format3 is better to use for this
          context than the class-based Format2 because the sets of
          covered glyphs for positions 0 and 2 overlap.</p><p>The LowerMathSignsSubtable contains offsets to three
          Coverage tables (XhtDescLCCoverage, MathSignCoverage, and
          LCCoverage), one for each position in the context glyph
          string. When the client finds the context in the text
          stream, it applies the PosLookupRecord data at position 1
          and repositions the math sign.</p><div class="table"><a name="idm239469526064"></a><p class="title"><strong>Table 24.57. Example 12</strong></p><div class="table-contents"><table class="table" summary="Example 12" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ContextPosFormat3</td><td> </td></tr><tr><td> </td><td>LowerMathSignsSubtable</td><td>ContextPos subtable
                  definition</td></tr><tr><td>0003</td><td>3</td><td>PosFormat</td></tr><tr><td>0003</td><td>3</td><td>GlyphCount</td></tr><tr><td>0001</td><td>1</td><td>PosLookup</td></tr><tr><td>0010</td><td>XhtDescLCCoverage</td><td>Offset to Coverage[0] table</td></tr><tr><td>003C</td><td>MathSignCoverage</td><td>Offset to Coverage[1] table</td></tr><tr><td>0044</td><td>LCCoverage</td><td>Offset to Coverage[2] table
                  PosLookupRecord[0]</td></tr><tr><td>0001</td><td>1</td><td>SequenceIndex</td></tr><tr><td>0001</td><td>1</td><td>LookupListInde</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>XhtDescLCCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0014</td><td>20</td><td>GlyphCount</td></tr><tr><td>0033</td><td>LCaGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>0035</td><td>LCcGlyphID</td><td>GlyphArray[1]</td></tr><tr><td>0037</td><td>LCeGlyphID</td><td>GlyphArray[2]</td></tr><tr><td>0039</td><td>LCgGlyphID</td><td>GlyphArray[3]</td></tr><tr><td>003B</td><td>LCiGlyphID</td><td>GlyphArray[4]</td></tr><tr><td>003C</td><td>LCjGlyphID</td><td>GlyphArray[5]</td></tr><tr><td>003F</td><td>LCmGlyphID</td><td>GlyphArray[6]</td></tr><tr><td>0040</td><td>LCnGlyphID</td><td>GlyphArray[7]</td></tr><tr><td>0041</td><td>LCoGlyphID</td><td>GlyphArray[8]</td></tr><tr><td>0042</td><td>LCpGlyphID</td><td>GlyphArray[9]</td></tr><tr><td>0043</td><td>LCqGlyphID</td><td>GlyphArray[10]</td></tr><tr><td>0044</td><td>LCrGlyphID</td><td>GlyphArray[11]</td></tr><tr><td>0045</td><td>LCsGlyphID</td><td>GlyphArray[12]</td></tr><tr><td>0046</td><td>LCtGlyphID</td><td>GlyphArray[13]</td></tr><tr><td>0047</td><td>LCuGlyphID</td><td>GlyphArray[14]</td></tr><tr><td>0048</td><td>LCvGlyphID</td><td>GlyphArray[15]</td></tr><tr><td>0049</td><td>LCwGlyphID</td><td>GlyphArray[16]</td></tr><tr><td>004A</td><td>LCxGlyphID</td><td>GlyphArray[17]</td></tr><tr><td>004B</td><td>LCyGlyphID</td><td>GlyphArray[18]</td></tr><tr><td>004C</td><td>LCzGlyphID</td><td>GlyphArray[19</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>MathSignCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>011E</td><td>EqualsSignGlyphID</td><td>GlyphArray[0]</td></tr><tr><td>012D</td><td>PlusSignGlyphID</td><td>GlyphArray[1</td></tr><tr><td> </td><td>CoverageFormat2</td><td> </td></tr><tr><td> </td><td>LCCoverage</td><td>Coverage table definition</td></tr><tr><td>0002</td><td>2</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>RangeCount RangeRecord[0]</td></tr><tr><td>0033</td><td>LCaGlyphID</td><td>Start</td></tr><tr><td>004C</td><td>LCzGlyphID</td><td>End</td></tr><tr><td>0000</td><td>0</td><td>StartCoverageIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469456320"></a>Example 13: PosLookupRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.43.1"></a>Specification</h4></div></div></div><p>The PosLookupRecord in Example 13 identifies a lookup to
          apply at the second glyph position in a context glyph
          string.</p><div class="table"><a name="idm239469453968"></a><p class="title"><strong>Table 24.58. Example 13</strong></p><div class="table-contents"><table class="table" summary="Example 13" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>PosLookupRecord</td><td> </td></tr><tr><td> </td><td>PosLookupRecord</td><td>0] PosLookupRecord
                  definition</td></tr><tr><td>0001</td><td>1</td><td>SequenceIndex for second glyph position</td></tr><tr><td>0001</td><td>1</td><td>LookupListIndex, apply this lookup to second
                  glyph position</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469445600"></a>Example 14: ValueFormat Table and ValueRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.44.1"></a>Specification</h4></div></div></div><p>Example 14 demonstrates how to specify positioning
          values in the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. Here, a
          SinglePosFormat1 subtable defines the ValueFormat and
          ValueRecord. The ValueFormat bit setting of 0x0099 says that
          the corresponding ValueRecord contains values for a glyph's
          XPlacement and YAdvance. Device tables specify pixel
          adjustments for these values at font sizes from 11 ppem to
          15 ppem.</p><div class="table"><a name="idm239469442272"></a><p class="title"><strong>Table 24.59. Example 14</strong></p><div class="table-contents"><table class="table" summary="Example 14" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>SinglePosFormat1</td><td> </td></tr><tr><td> </td><td>OnesSubtable</td><td>SinglePos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>000E</td><td>Cov</td><td>Offset to Coverage table</td></tr><tr><td>0099</td><td>0x0099</td><td>ValueFormat, for XPlacement, YAdvance,
                  XPlaDevice, YAdvaDevice Value</td></tr><tr><td>0050</td><td>80</td><td>Xplacement value</td></tr><tr><td>00D2</td><td>210</td><td>Yadvance value</td></tr><tr><td>0018</td><td>XPlaDeviceTable</td><td>Offset to XPlaDevice table</td></tr><tr><td>0020</td><td>YAdvDeviceTable</td><td>Offset to YAdvDevice tabl</td></tr><tr><td> </td><td>CoverageFormat2</td><td> </td></tr><tr><td> </td><td>Cov</td><td>Coverage table definition</td></tr><tr><td>0002</td><td>2</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>RangeCount RangeRecord[0]</td></tr><tr><td>00C8</td><td>200</td><td>Start, first glyph ID in range</td></tr><tr><td>00D1</td><td>209</td><td>End, last glyph ID in range</td></tr><tr><td>0000</td><td>0</td><td>StartCoverageInde</td></tr><tr><td> </td><td>DeviceTableFormat1</td><td> </td></tr><tr><td> </td><td>XPlaDeviceTable</td><td>Device Table definition</td></tr><tr><td>000B</td><td>11</td><td>StartSize</td></tr><tr><td>000F</td><td>15</td><td>EndSize</td></tr><tr><td>0001</td><td>1</td><td>DeltaFormat</td></tr><tr><td> </td><td>1</td><td>increase 11ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 12ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppem by 1 pixel</td></tr><tr><td>5540</td><td>1</td><td>increase 15ppem by 1 pixe</td></tr><tr><td> </td><td>DeviceTableFormat1</td><td> </td></tr><tr><td> </td><td>YAdvDeviceTable</td><td>Device Table definition</td></tr><tr><td>000B</td><td>11</td><td>StartSize</td></tr><tr><td>000F</td><td>15</td><td>EndSize</td></tr><tr><td>0001</td><td>1</td><td>DeltaFormat</td></tr><tr><td> </td><td>1</td><td>increase 11ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 12ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppem by 1 pixel</td></tr><tr><td>5540</td><td>1</td><td>increase 15ppem by 1 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469389744"></a>Example 15: AnchorFormat1 Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.45.1"></a>Specification</h4></div></div></div><p>Example 15 illustrates an Anchor table for the damma
          mark glyph in the Arabic script. Format1 is used to specify
          X and Y coordinate values in design units.</p><div class="table"><a name="idm239469387360"></a><p class="title"><strong>Table 24.60. Example 15</strong></p><div class="table-contents"><table class="table" summary="Example 15" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>AnchorFormat1</td><td> </td></tr><tr><td> </td><td>dammaMarkAnchor</td><td>Anchor table definition</td></tr><tr><td>0001</td><td>1</td><td>AnchorFormat</td></tr><tr><td>00BD</td><td>189</td><td>XCoordinate</td></tr><tr><td>FF99</td><td>-103</td><td>YCoordinate</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469377648"></a>Example 16: AnchorFormat2 Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.46.1"></a>Specification</h4></div></div></div><p>Example 16 shows an AnchorFormat2 table for an
          attachment point placed above a base glyph. With this
          format, the coordinate value for the Anchor depends on the
          final position of a specific contour point on the base glyph
          after hinting. The coordinates are specified in design
          units.</p><div class="table"><a name="idm239469375104"></a><p class="title"><strong>Table 24.61. Example 16</strong></p><div class="table-contents"><table class="table" summary="Example 16" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>AnchorFormat2</td><td> </td></tr><tr><td> </td><td>AboveBaseAnchor</td><td>Anchor table definition</td></tr><tr><td>0002</td><td>2</td><td>AnchorFormat</td></tr><tr><td>0142</td><td>322</td><td>XCoordinate</td></tr><tr><td>0384</td><td>900</td><td>Ycoordinate</td></tr><tr><td>000D</td><td>13</td><td>AnchorPoint glyph contour point index</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469363904"></a>Example 17: AnchorFormat3 Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.47.1"></a>Specification</h4></div></div></div><p>Example 17 shows an AnchorFormat3 table that specifies
          an attachment point above a base glyph. Device tables modify
          the X and Y coordinates of the Anchor for the point size and
          resolution of the output font. Here, the Device tables
          define pixel adjustments for font sizes from 12 ppem to 17
          ppem.</p><div class="table"><a name="idm239469361344"></a><p class="title"><strong>Table 24.62. Example 17</strong></p><div class="table-contents"><table class="table" summary="Example 17" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>AnchorFormat3</td><td> </td></tr><tr><td> </td><td>AboveBaseAnchor</td><td>Anchor table definition</td></tr><tr><td>0003</td><td>3</td><td>AnchorFormat</td></tr><tr><td>0117</td><td>279</td><td>XCoordinate</td></tr><tr><td>0515</td><td>1301</td><td>YCoordinate</td></tr><tr><td>000A</td><td>XDevice</td><td>offset to DeviceTable for X coordinate (may be
                  NULL)</td></tr><tr><td>0014</td><td>YDevice</td><td>offset to Device table for Y coordinate (may be
                  NULL</td></tr><tr><td> </td><td>DeviceTableFormat2</td><td> </td></tr><tr><td> </td><td>XDevice</td><td>Device Table definition</td></tr><tr><td>000C</td><td>12</td><td>StartSize</td></tr><tr><td>0011</td><td>17</td><td>EndSize</td></tr><tr><td>0002</td><td>2</td><td>DeltaFormat</td></tr><tr><td> </td><td>1</td><td>increase 12ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppem by 1 pixel</td></tr><tr><td>1111</td><td>1</td><td>increase 15ppem by 1 pixel</td></tr><tr><td> </td><td>2</td><td>increase 16ppem by 1 pixel</td></tr><tr><td>2200</td><td>2</td><td>increase 17ppem by 1 pixe</td></tr><tr><td> </td><td>DeviceTableFormat2</td><td> </td></tr><tr><td> </td><td>YDevice</td><td>Device Table definition</td></tr><tr><td>000C</td><td>12</td><td>StartSize</td></tr><tr><td>0011</td><td>17</td><td>EndSize</td></tr><tr><td>0002</td><td>2</td><td>DeltaFormat</td></tr><tr><td> </td><td>1</td><td>increase 12ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppem by 1 pixel</td></tr><tr><td>1111</td><td>1</td><td>increase 15ppem by 1 pixel</td></tr><tr><td> </td><td>2</td><td>increase 16ppem by 1 pixel</td></tr><tr><td>2200</td><td>2</td><td>increase 17ppem by 1 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239469318608"></a>Example 18: MarkArray Table and MarkRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.25.48.1"></a>Specification</h4></div></div></div><p>Example 18 shows a MarkArray table with class and
          attachment point data for two accent marks, a grave and a
          cedilla. Two MarkRecords are defined, one for each covered
          mark glyph. The first MarkRecord assigns a mark class value
          of 0 to accents placed above base glyphs, such as the grave,
          and has an offset to a graveMarkAnchor table. The second
          MarkRecord assigns a mark class value of 1 for all accents
          positioned below base glyphs, such as the cedilla, and has
          an offset to a cedillaMarkAnchor table.</p><div class="table"><a name="idm239469315792"></a><p class="title"><strong>Table 24.63. Example 18</strong></p><div class="table-contents"><table class="table" summary="Example 18" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>MarkArray</td><td> </td></tr><tr><td> </td><td>MarkGlyphsArray</td><td>MarkArray table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>MarkCount MarkRecord[0] for first mark in
                  MarkCoverage table, grave</td></tr><tr><td>0000</td><td>0</td><td>Class, for marks placed above base
                  glyphs</td></tr><tr><td>000A</td><td>graveMarkAnchor</td><td>offset to Anchor table MarkRecord[1] for second
                  mark in MarkCoverage table = cedilla</td></tr><tr><td>0001</td><td>1</td><td>Class, for marks placed below base
                  glyphs</td></tr><tr><td>0010</td><td>cedillaMarkAnchor</td><td>offset to Anchor table</td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>