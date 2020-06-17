<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.GSUB"></a>Chapter 25. GSUB - The Glyph Substitution Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383060828704"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.1.1"></a>Specification</h3></div></div></div><p role="">The Glyph Substitution table (<a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>)
          contains information for substituting glyphs to render the
          scripts and language systems supported in a font. Many
          language systems require glyph substitutes. For example, in
          the Arabic script, the glyph shape that depicts a particular
          character varies according to its position in a word or text
          string (see figure 1). In other language systems, glyph
          substitutes are aesthetic options for the user, such as the
          use of ligature glyphs in the English language (see Figure
          2)</p><div class="figure"><a name="idm383051371920"></a><p class="title"><strong>Figure 25.1. Figure 1: Isolated, initial, medial, and final forms
            of the Arabic character HAH</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3a.gif" alt="Figure 1: Isolated, initial, medial, and final forms of the Arabic character HAH"/></div></div></div><br class="figure-break"/><div class="figure"><a name="idm383051369776"></a><p class="title"><strong>Figure 25.2. Figure 2. Two Latin glyphs and their associated
            ligature</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3b.gif" alt="Figure 2. Two Latin glyphs and their associated ligature"/></div></div></div><br class="figure-break"/><p role="">Many fonts use limited character encoding standards that
          map glyphs to characters one-to-one, assigning a glyph to
          each character code value in a font. Multiple character
          codes cannot be mapped to a single glyph, as needed for
          ligature glyphs, and multiple glyphs cannot be mapped to a
          single character code, as needed to decompose a ligature
          into its component glyphs.</p><p role="">To supply glyph substitutes, font developers must assign
          different character codes to the glyphs, or they must create
          additional fonts or character sets. To access these glyphs,
          users must bear the burden of switching between character
          codes, character sets, or fonts.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.1.2"></a>Annotation</h3></div></div></div><p role="">The term "limited character encoding standards" in the
          first sentence is somewhat misleading. Unicode for example
          can hardly be considered a "limited" standard. May a better
          formulation for the first sentence may be: "Character
          standards typically encode characters but not glyphs; at the
          same time, fonts typically map from one character to one
          glyph."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051363536"></a>Substituting Glyphs with OpenType</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.2.1"></a>Specification</h3></div></div></div><p role="">The OpenType <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table fully
          supports glyph substitution. To access glyph substitutes,
          <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> maps from the glyph index or indices
          defined in a cmap table to the glyph index or indices of the
          glyph substitutes. For example, if a font has three
          alternative forms of an ampersand glyph, the cmap table
          associates the ampersand's character code with only one of
          these glyphs. In <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, the indices of the
          other ampersand glyphs are then referenced by this one
          index.</p><p role="">The text-processing client uses the
          <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> data to manage glyph substitution
          actions. <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> identifies the glyphs that
          are input to and output from each glyph substitution action,
          specifies how and where the client uses glyph substitutes,
          and regulates the order of glyph substitution operations.
          Any number of substitutions can be defined for each script
          or language system represented in a font.</p><p role="">The <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table supports six types of glyph
          substitutions that are widely used in international
          typography:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>single substitution</em></span> replaces
              a single glyph with another single glyph. This is used
              to render positional glyph variants in Arabic and
              vertical text in the Far East (see Figure 3)</p><div class="figure"><a name="idm383051354000"></a><p class="title"><strong>Figure 25.3. Figure 3. Alternative forms of parentheses used
                when positioning Kanji vertically</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3c.gif" alt="Figure 3. Alternative forms of parentheses used when positioning Kanji vertically"/></div></div></div><br class="figure-break"/></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>multiple substitution</em></span>
              replaces a single glyph with more than one glyph. This
              is used to specify actions such as ligature
              decomposition (see Figure 4)</p><div class="figure"><a name="idm383051350480"></a><p class="title"><strong>Figure 25.4. Figure 4. Decomposing a Latin ligature glyph into
                its individual glyph components</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3d.gif" alt="Figure 4. Decomposing a Latin ligature glyph into its individual glyph components"/></div></div></div><br class="figure-break"/></li><li role="" class="listitem"><p role="">An <span role="" class="emphasis"><em>alternate substitution</em></span>
              identifies functionally equivalent but different looking
              forms of a glyph. These glyphs are often referred to as
              aesthetic alternatives. For example, a font might have
              five different glyphs for the ampersand symbol, but one
              would have a default glyph index in the cmap table. The
              client could use the default glyph or substitute any of
              the four alternatives (see Figure 5)</p><div class="figure"><a name="idm383051346624"></a><p class="title"><strong>Figure 25.5. Figure 5. Alternative ampersand glyphs in a
                font</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3e.gif" alt="Figure 5. Alternative ampersand glyphs in a font"/></div></div></div><br class="figure-break"/></li><li role="" class="listitem"><p role="">A <span role="" class="emphasis"><em>ligature substitution</em></span>
              replaces several glyph indices with a single glyph
              index, as when an Arabic ligature glyph replaces a
              string of separate glyphs (see Figure 6). When a string
              of glyphs can be replaced with a single ligature glyph,
              the first glyph is substituted with the ligature. The
              remaining glyphs in the string are deleted, this
              includes those glyphs that are skipped as a result of
              lookup flags.</p><div class="figure"><a name="idm383051342304"></a><p class="title"><strong>Figure 25.6. Figure 6. Three Arabic glyphs and their
                associated ligature glyph</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3f.gif" alt="Figure 6. Three Arabic glyphs and their associated ligature glyph"/></div></div></div><br class="figure-break"/></li><li role="" class="listitem"><p role=""><span role="" class="emphasis"><em>Contextual substitution</em></span>, the
              most powerful type, describes glyph substitutions in
              context – that is, a substitution of one or more glyphs
              within a certain pattern of glyphs. Each substitution
              describes one or more input glyph sequences and one or
              more substitutions to be performed on that sequence.
              Contextual substitutions can be applied to specific
              glyph sequences, glyph classes, or sets of
              glyphs.</p></li><li role="" class="listitem"><p role=""><span role="" class="emphasis"><em>Chaining contextual
                substitution</em></span>, extends the capabilities of
              contextual substitution. With this, one or more
              substitutions can be performed on one or more glyphs
              within a pattern of glyphs (input sequence), by chaining
              the input sequence to a 'backtrack' and/or 'lookahead'
              sequence. Each such substitution can be applied in three
              formats to handle glyphs, glyph classes or glyph sets in
              the input sequence. Each of these formats can describe
              one or more of the backtrack, input and lookahead
              sequences.</p></li><li role="" class="listitem"><p role=""><span role="" class="emphasis"><em>Reverse Chaining contextual single
		substitution</em></span>, allows one glyph to be
		substituted with another by chaining input glyph to a
		backtrack and/or lookahead sequence. The
		difference between this and other lookup types is that
		processing of input glyph sequence goes from end to
		start.</p></li></ul></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.2.2"></a>Annotation</h3></div></div></div><p role="">The model presented in the first paragraph is too
          restrictive; it suggests that only glyphs which are the
          target of cmap tables can be substituted. The proposed
          change is replace the second sentence by: "After characters
          have been mapped to glyphs through the cmap table, the glyph
          run are modified using data in the GSUB table."</p><p role="">After the list of supported glyph substitutions, it may
          be worth adding a paragraph: "A seventh type of glyph
          substitution (<span role="" class="emphasis"><em>extension substitution</em></span>)
          does not increase the functionality but is sometimes
          necessary for large GSUB tables.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051331360"></a>Table Organization</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.3.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table begins with a header
          that defines offsets to a ScriptList, a FeatureList, and a
          LookupList (see Figure 3g):</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The ScriptList identifies all the scripts and
              language systems in the font that use glyph
              substitutes.</p></li><li role="" class="listitem"><p role="">The FeatureList defines all the glyph substitution
              features required to render these scripts and language
              systems.</p></li><li role="" class="listitem"><p role="">The LookupList contains all the lookup data needed
              to implement each glyph substitution feature.</p></li></ul></div><p role="">For a detailed discussion of ScriptLists, FeatureLists,
          and LookupLists, see the chapter Common Table Formats</p><div class="figure"><a name="idm383051324752"></a><p class="title"><strong>Figure 25.7. Figure 7. High-level organization of <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          table</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig3g.gif" alt="Figure 7. High-level organization of GSUB table"/></div></div></div><br class="figure-break"/><p role="">This organization helps text-processing clients to
          easily locate the features and lookups that apply to a
          particular script or language system. To access <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          information, clients should use the following
          procedure:</p><div role="" class="orderedlist"><ol class="orderedlist" type="1"><li role="" class="listitem"><p role="">Locate the current script in the
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> ScriptList table.</p></li><li role="" class="listitem"><p role="">If the language system is known, search the script
              for the correct LangSys table; otherwise, use the
              script's default language system (DefaultLangSys
              table).</p></li><li role="" class="listitem"><p role="">The LangSys table provides index numbers into the
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> FeatureList table to access a
              required feature and a number of additional
              features.</p></li><li role="" class="listitem"><p role="">Inspect the FeatureTag of each feature, and select
              the features to apply to an input glyph string. Each
              feature provides an array of index numbers into the
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> LookupList table.</p></li><li role="" class="listitem"><p role="">Assemble all lookups from the set of chosen
              features, and apply the lookups in the order given in
              the LookupList table.</p></li></ol></div><p role="">Lookup data is defined in one or more subtables that
          define the specific conditions, type, and results of a
          substitution action used to implement a feature. All
          subtables in a lookup must be of the same LookupType, as
          listed in the LookupType Enumeration table:</p><div class="table"><a name="idm383051312976"></a><p class="title"><strong>Table 25.1. LookupType Enumeration table for glyph
            substitution</strong></p><div class="table-contents"><table role="" class="table" summary="LookupType Enumeration table for glyph&#10;            substitution" border="1"><colgroup><col width="3pc"/><col width="11pc"/><col width="16pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Type</th><th role="">Description</th></tr></thead><tbody><tr><td role="">1</td><td role="">Single</td><td role="">Replace one glyph with one glyph </td></tr><tr><td role="">2</td><td role="">Multiple</td><td role="">Replace one glyph with more than one
                  glyph</td></tr><tr><td role="">3</td><td role="">Alternate</td><td role="">Replace one glyph with one of many
                  glyphs</td></tr><tr><td role="">4</td><td role="">Ligature</td><td role="">Replace multiple glyphs with one glyph</td></tr><tr><td role="">5</td><td role="">Context</td><td role="">Replace one or more glyphs in context</td></tr><tr><td role="">6</td><td role="">Chaining Context</td><td role="">Replace one or more glyphs in chained
                  context</td></tr><tr><td role="">7</td><td role="">Extension Substitution</td><td role="">Extension mechanism for other substitutions
                  (i.e. this excludes the Extension type substitution
                  itself)</td></tr><tr><td role="">8</td><td role="">Reverse chaining context single</td><td role="">Applied in reverse order, replace single glyph
		in chaining context</td></tr><tr><td role="">9+</td><td role="">Reserved</td><td role="">For future use</td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each LookupType subtable has one or more formats. The
          "best" format depends on the type of substitution and the
          resulting storage efficiency. When glyph information is best
          presented in more than one format, a single lookup may
          define more than one subtable, as long as all the subtables
          are for the same LookupType. For example, within a given
          lookup, a glyph index array format may best represent one
          set of target glyphs, whereas a glyph index range format may
          be better for another set.</p><p role="">A series of substitution operations on the same glyph or
          string requires multiple lookups, one for each separate
          action. Each lookup is given a different array number in the
          LookupList table and is applied in the LookupList
          order.</p><p role="">During text processing, a client applies a lookup to
          each glyph in the string before moving to the next lookup. A
          lookup is finished for a glyph after the client locates the
          target glyph or glyph context and performs a substitution,
          if specified. To move to the "next" glyph, the client will
          typically skip all the glyphs that participated in the
          lookup operation: glyphs that were substituted as well as
          any other glyphs that formed a context for the
          operation.</p><p role="">In the case of chained contextual lookups, glyphs
          comprising backtrack and lookahead sequences may participate
          in more than one context.</p><p role="">The rest of this chapter describes the
          <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> header and the subtables defined for
          each <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> LookupType. Examples at the end
          of this page illustrate each of the five LookupTypes,
          including the three formats available for contextual
          substitutions.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.3.2"></a>Annotation</h3></div></div></div><p role="">Last sentence: the occurrence of 'five' should be
          replaced by 'seven'.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051285760"></a>GSUB header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.4.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table begins with a header
          that contains a version number for the table (Version) and
          offsets to a three tables: ScriptList, FeatureList, and
          LookupList. For descriptions of each of these tables, see
          the chapter, Common Table Formats. Example 1 at the end of
          this chapter shows a <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> Header table
          definition.</p><div class="table"><a name="idm383051281888"></a><p class="title"><strong>Table 25.2. GSUB Header</strong></p><div class="table-contents"><table role="" class="table" summary="GSUB Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">Version</td><td role="">Version of the <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
              table – initially set to 0x00010000</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ScriptList</td><td role="">Offset to ScriptList table – from beginning of
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">FeatureList</td><td role="">Offset to FeatureList table – from beginning of
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LookupList</td><td role="">Offset to LookupList table – from beginning of
              <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.4.2"></a>Annotation</h3></div></div></div><p role="">There is a typo in the first sentence "... to a three
          tables:..."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051268400"></a>Lookup Type 1: Single Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.5.1"></a>Specification</h3></div></div></div><p role="">Single substitution (SingleSubst) subtables tell a
          client to replace a single glyph with another glyph. The
          subtables can be either of two formats. Both formats require
          two distinct sets of glyph indices: one that defines input
          glyphs (specified in the Coverage table), and one that
          defines the output glyphs. Format 1 requires less space than
          Format 2, but it is less flexible.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.5.2"></a>Annotation</h3></div></div></div><p role="">None.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051263520"></a>Single Substitution Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.6.1"></a>Specification</h3></div></div></div><p role="">Format 1 calculates the indices of the output glyphs,
          which are not explicitly defined in the subtable. To
          calculate an output glyph index, Format 1 adds a constant
          delta value to the input glyph index. For the substitutions
          to occur properly, the glyph indices in the input and output
          ranges must be in the same order. This format does not use
          the Coverage Index that is returned from the Coverage
          table.</p><p role="">The SingleSubstFormat1 subtable begins with a format
          identifier (SubstFormat) of 1. An offset references a
          Coverage table that specifies the indices of the input
          glyphs. DeltaGlyphID is the constant value added to each
          input glyph index to calculate the index of the
          corresponding output glyph.</p><p role="">Example 2 at the end of this chapter uses Format 1 to
          replace standard numerals with lining numerals.</p><div class="table"><a name="idm383051259600"></a><p class="title"><strong>Table 25.3. SingleSubstFormat1 subtable: Calculated output glyph
            indices</strong></p><div class="table-contents"><table role="" class="table" summary="SingleSubstFormat1 subtable: Calculated output glyph&#10;            indices" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">DeltaGlyphID</td><td role="">Add to original GlyphID to get substitute
              GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.6.2"></a>Annotation</h3></div></div></div><p role="">I cannot figure out what the third sentence of the first
          paragraph really says. It it phrased as a requirement on the
          way the lookup is built, yet it seems to describe a property
          that follows from the nature of GSUB 1/1
          lookups. Recommendation: remove it for the
          specification.</p><p role="">In the spirit of cmaps subtable format 4, the arithmetic
          on the glyph index should probably be performed modulo
          65536. Recommendation: make that explicit.</p><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to replace the glyph
	  matched by C; if the id of that glyph is g, then the
	  replacement glyph has id (g+DeltaGlyphId) % 0xffff.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051247344"></a>Single Substitution Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.7.1"></a>Specification</h3></div></div></div><p role="">Format 2 is more flexible than Format 1, but requires
          more space. It provides an array of output glyph indices
          (Substitute) explicitly matched to the input glyph indices
          specified in the Coverage table.</p><p role="">The SingleSubstFormat2 subtable specifies a format
          identifier (SubstFormat), an offset to a Coverage table that
          defines the input glyph indices, a count of output glyph
          indices in the Substitute array (GlyphCount), and a list of
          the output glyph indices in the Substitute array
          (Substitute).</p><p role="">The Substitute array must contain the same number of
          glyph indices as the Coverage table. To locate the
          corresponding output glyph index in the Substitute array,
          this format uses the Coverage Index returned from the
          Coverage table.</p><p role="">Example 3 at the end of this chapter uses Format 2 to
          substitute vertically oriented glyphs for horizontally
          oriented glyphs.</p><div class="table"><a name="idm383051242960"></a><p class="title"><strong>Table 25.4. SingleSubstFormat2 subtable: Specified output glyph
            indices</strong></p><div class="table-contents"><table role="" class="table" summary="SingleSubstFormat2 subtable: Specified output glyph&#10;            indices" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of GlyphIDs in the Substitute
              array</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Substitute [GlyphCount]</td><td role="">Array of substitute GlyphIDs – ordered by
              Coverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.7.2"></a>Annotation</h3></div></div></div><p role="">To adopt a consistent language, the third paragraph should
          be changed to "The Coverage index of the input glyph is used to
          index the Susbtitute array and GlyphCount must equal the number of
          covered glyphs."</p><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to replace the glyph
	  matched by C by the corresponding glyph in the Substitute
	  array.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051229792"></a>LookupType 2: Multiple Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.8.1"></a>Specification</h3></div></div></div><p role="">A Multiple Substitution (MultipleSubst) subtable
          replaces a single glyph with more than one glyph, as when
          multiple glyphs replace a single ligature. The subtable has
          a single format: MultipleSubstFormat1. The subtable
          specifies a format identifier (SubstFormat), an offset to a
          Coverage table that defines the input glyph indices, a count
          of offsets in the Sequence array (SequenceCount), and an
          array of offsets to Sequence tables that define the output
          glyph indices (Sequence). The Sequence table offsets are
          ordered by the Coverage Index of the input glyphs. </p><p role="">For each input glyph listed in the Coverage table, a
          Sequence table defines the output glyphs. Each Sequence
          table contains a count of the glyphs in the output glyph
          sequence (GlyphCount) and an array of output glyph indices
          (Substitute).</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: The order of the output glyph indices depends on
            the writing direction of the text. For text written left
            to right, the left-most glyph will be first glyph in the
            sequence. Conversely, for text written right to left, the
            right-most glyph will be first. </p></blockquote></div><p role="">The use of multiple substitution for deletion of an
          input glyph is prohibited. GlyphCount should always be
          greater than 0.</p><p role="">Example 4 at the end of this chapter shows how to
          replace a single ligature with three glyphs.</p><div class="table"><a name="idm383051224128"></a><p class="title"><strong>Table 25.5. MultipleSubstFormat1 subtable: Multiple output glyphs</strong></p><div class="table-contents"><table role="" class="table" summary="MultipleSubstFormat1 subtable: Multiple output glyphs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SequenceCount</td><td role="">Number of Sequence table offsets in the
              Sequence array</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Sequence [SequenceCount]</td><td role="">Array of offsets to Sequence tables – from
              beginning of Substitution table – ordered by Coverage
              Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383051215392"></a><p class="title"><strong>Table 25.6. Sequence table</strong></p><div class="table-contents"><table role="" class="table" summary="Sequence table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of GlyphIDs in the Substitute array.
              This should always be greater than 0.</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Substitute [GlyphCount]</td><td role="">String of GlyphIDs to
              substitute</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.8.2"></a>Annotation</h3></div></div></div><p role="">To adopt a consistent language, the last sentence of the
          first paragraph should be changed to: "The Coverage index of
          the input glyph is used to index the Sequence array and
          SequenceCount must equal the number of covered glyphs. The
          entries in the Sequence array cannot be NULL."</p><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to replace the glyph
	  matched by C by the Substitute sequence of glyphs in the
	  corresponding Sequence table, in the order in which they
	  appear in that array.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051205328"></a>LookupType 3: Alternate Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.9.1"></a>Specification</h3></div></div></div><p role="">An Alternate Substitution (AlternateSubst) subtable
        identifies any number of aesthetic alternatives from which a
        user can choose a glyph variant to replace the input
        glyph. For example, if a font contains four variants of the
        ampersand symbol, the cmap table will specify the index of one
        of the four glyphs as the default glyph index, and an
        AlternateSubst subtable will list the indices of the other
        three glyphs as alternatives. A text-processing client would
        then have the option of replacing the default glyph with any
        of the three alternatives. </p><p role="">The subtable has one format: AlternateSubstFormat1. The
        subtable contains a format identifier (SubstFormat), an offset
        to a Coverage table containing the indices of glyphs with
        alternative forms (Coverage), a count of offsets to
        AlternateSet tables (AlternateSetCount), and an array of
        offsets to AlternateSet tables (AlternateSet).</p><p role="">For each glyph, an AlternateSet subtable contains a
        count of the alternative glyphs (GlyphCount) and an array of
        their glyph indices (Alternate). Because all the glyphs are
        functionally equivalent, they can be in any order in the
        array.</p><p role="">Example 5 at the end of this chapter shows how to
        replace the default ampersand glyph with alternative
        glyphs.</p><div class="table"><a name="idm383051200544"></a><p class="title"><strong>Table 25.7. AlternateSubstFormat1 subtable: Alternative output
          glyphs</strong></p><div class="table-contents"><table role="" class="table" summary="AlternateSubstFormat1 subtable: Alternative output&#10;          glyphs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">AlternateSetCount</td><td role="">Number of AlternateSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">AlternateSet
            [AlternateSetCount]</td><td role="">Array of
            offsets to AlternateSet tables – from beginning of
            Substitution table – ordered by Coverage
            Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm383051191776"></a><p class="title"><strong>Table 25.8. AlternateSet table</strong></p><div class="table-contents"><table role="" class="table" summary="AlternateSet table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of GlyphIDs in the Alternate
              array</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Alternate [GlyphCount]</td><td role="">Array of alternate GlyphIDs – in arbitrary
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.9.2"></a>Annotation</h3></div></div></div><p role="">To adopt a consistent language, the following should be added
          to the second paragraph: "The Coverage index of the input glyph is
          used to index the AlternateSet array and AlternateSetCount must
          equal the number of glyphs covered by Coverage."</p><p role="">The specification fails to say if an element of the
          AlternateSet array can be null. We assume it cannot. This can be
          added after the sentence above: "The entries in the AlternateSet
          array cannot be NULL."</p><p role="">The specification fails to say if the GlyphCount of an
          AlternateSet table can be 0. We assume it cannot, and this
          can be made clear by adding this sentence to the third paragraph:
          "GlyphCount cannot be 0."</p><p role="">The pattern matched by this subtable is ▶ C
	  ◀ where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">C is Coverage ∖ LookupFlag</p></li></ul></div><p role="">The action of this subtable is to replace the glyph
	  matched by C by one of the glyphs in the Alternate array
	  corresponding to the replaced glyph. The mechanism by which
	  the client indicates which of those glyphs is used is not
	  specified.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383051180384"></a>LookupType 4: Ligature Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.10.1"></a>Specification</h3></div></div></div><p role="">A Ligature Substitution (LigatureSubst) subtable
          identifies ligature substitutions where a single glyph
          replaces multiple glyphs. One LigatureSubst subtable can
          specify any number of ligature substitutions.</p><p role="">The subtable uses a single format: LigatureSubstFormat1.
          It contains a format identifier (SubstFormat), a Coverage
          table offset (Coverage), a count of the ligature sets
          defined in this table (LigSetCount), and an array of offsets
          to LigatureSet tables (LigatureSet). The Coverage table
          specifies only the index of the first glyph component of
          each ligature set.</p><div class="table"><a name="idm383051177104"></a><p class="title"><strong>Table 25.9. LigatureSubstFormat1 subtable: All ligature
            substitutions in a script</strong></p><div class="table-contents"><table role="" class="table" summary="LigatureSubstFormat1 subtable: All ligature&#10;            substitutions in a script" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LigSetCount</td><td role="">Number of LigatureSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LigatureSet [LigSetCount]</td><td role="">Array of offsets to LigatureSet tables
              – from beginning of Substitution table –
              ordered by Coverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A LigatureSet table, one for each covered glyph,
          specifies all the ligature strings that begin with the
          covered glyph. For example, if the Coverage table lists the
          glyph index for a lowercase “f,” then a
          LigatureSet table will define the “ffl,”
          “fl,” “ffi,” “fi,”
          and “ff” ligatures. If the Coverage table also
          lists the glyph index for a lowercase “e,”
          then a different LigatureSet table will define the
          “etc” ligature.</p><p role="">A LigatureSet table consists of a count of the ligatures
          that begin with the covered glyph (LigatureCount) and an
          array of offsets to Ligature tables, which define the glyphs
          in each ligature (Ligature). The order in the Ligature
          offset array defines the preference for using the ligatures.
          For example, if the “ffl” ligature is
          preferable to the “ff” ligature, then the
          Ligature array would list the offset to the
          “ffl” Ligature table before the offset to the
          “ff” Ligature table. </p><div class="table"><a name="idm383051167376"></a><p class="title"><strong>Table 25.10. LigatureSet table: All ligatures beginning with the
          same glyph</strong></p><div class="table-contents"><table role="" class="table" summary="LigatureSet table: All ligatures beginning with the&#10;          same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">LigatureCount</td><td role="">Number of Ligature tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Ligature [LigatureCount]</td><td role="">Array of offsets to Ligature tables –
              from beginning of LigatureSet table – ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">For each ligature in the set, a Ligature table specifies
          the GlyphID of the output ligature glyph (LigGlyph); a count
          of the total number of component glyphs in the ligature,
          including the first component (CompCount); and an array of
          GlyphIDs for the components (Component). The array starts
          with the second component glyph (array index = 1) in the
          ligature because the first component glyph is specified in
          the Coverage table.</p><p role="">Note: The Component array lists GlyphIDs according to
        the writing direction of the text. For text written right to
        left, the right-most glyph will be first. Conversely, for text
        written left to right, the left-most glyph will be
        first.</p><p role="">Example 6 at the end of this chapter shows how to
        replace a string of glyphs with a single ligature.</p><div class="table"><a name="idm383055062400"></a><p class="title"><strong>Table 25.11. Ligature table: Glyph components for one
          ligature</strong></p><div class="table-contents"><table role="" class="table" summary="Ligature table: Glyph components for one&#10;          ligature" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">GlyphID</td><td role="">LigGlyph</td><td role="">GlyphID of ligature to
              substitute</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">CompCount</td><td role="">Number of components in the
              ligature</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Component [CompCount-1]</td><td role="">Array of component GlyphIDs – start with the
              second component – ordered in writing
              direction</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.10.2"></a>Annotation</h3></div></div></div><p role="">To adopt a consistent language, the last sentence of the
          second paragraph should be replaced by: "The Coverage index of the
          first input glyph is used to index the LigatureSet array and
          LigSetCount must equal the number of glyphs covered by
          Coverage."</p><p role="">The specification fails to say if an element of the
          LigatureSet array can be null. We assume it cannot. This can be
          added after the sentence above: "The entries in the LigatureSet
          array cannot be NULL."</p><p role="">It is unclear whether the LigatureCount of a LigatureSet
          table can be 0. We assume that
          LigatureCount must be at least 1 and recommend that it be spelled
          out in the specification.</p><p role="">It is unclear whether the CompCount of a Ligature table can
          be 0 or 1. The value 0 is most certainly illegal (since a
          Ligature table is used in the context of a first glyph
          match). While the value 1 could be accepted, this would amount to
          a one for one substitution, which is probably better handled by a
          Single Substitution lookup. Therefore, we assume that CompCount
          must be 2 or more, and recommend that it be spelled out in the
          specification.</p><p role="">The pattern matched by the Ligature table t = LigatureSet
	  [m].Ligature [n] is ▶ L<sub>0</sub> L*
	  L<sub>1</sub> L* ... L*
	  L<sub>i-1</sub> ◀, where:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is t.CompCount</p></li><li role="" class="listitem"><p role="">L<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L<sub>k</sub> is {t.Component [k-1]} ∖ LookupFlag,
	      for k &gt; 0</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">The action of this Ligature table is to replace the entire
	  input sequence by the glyph t.LigGlyph.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383055044064"></a>LookupType 5: Contextual Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.11.1"></a>Specification</h3></div></div></div><p role="">A Contextual Substitution (ContextSubst) subtable
          defines the most powerful type of glyph substitution lookup:
          it describes glyph substitutions in context that replace one
          or more glyphs within a certain pattern of glyphs.</p><p role="">ContextSubst subtables can be any of three formats that
          define a context in terms of a specific sequence of glyphs,
          glyph classes, or glyph sets. Each format can describe one
          or more input glyph sequences and one or more substitutions
          for each sequence.</p><p role="">All three formats of ContextSubst subtables specify
          substitution data in a SubstLookupRecord. A description of
          that record follows.</p><div class="table"><a name="idm383055040352"></a><p class="title"><strong>Table 25.12. SubstLookupRecord</strong></p><div class="table-contents"><table role="" class="table" summary="SubstLookupRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SequenceIndex</td><td role="">Index into current glyph sequence – first glyph
              = 0</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookupListIndex</td><td role="">Lookup to apply to that
              position – zero-based</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The SequenceIndex in a SubstLookupRecord must take into
          consideration the order in which lookups are applied to the
          entire glyph sequence. Because multiple substitutions may
          occur per context, the SequenceIndex and LookupListIndex
          refer to the glyph sequence after the text-processing client
          has applied any previous lookups. In other words, the
          SequenceIndex identifies the location for the substitution
          at the time that the lookup is to be applied. For example,
          consider an input glyph sequence of four glyphs. The first
          glyph does not have a substitute, but the middle two glyphs
          will be replaced with a ligature, and a single glyph will
          replace the fourth glyph:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The first glyph is in position 0. No lookups will be
            applied at position 0, so no SubstLookupRecord is
            defined.</p></li><li role="" class="listitem"><p role="">The SubstLookupRecord defined for the ligature
            substitution specifies the SequenceIndex as position 1,
            which is the position of the first-glyph component in the
            ligature string. After the ligature replaces the glyphs in
            positions 1 and 2, however, the input glyph sequence
            consists of only three glyphs, not the original
            four.</p></li><li role="" class="listitem"><p role="">To replace the last glyph in the sequence, the
            SubstLookupRecord defines the SequenceIndex as position 2
            instead of position 3. This position reflects the effect
            of the ligature substitution applied before this single
            substitution. </p></li></ul></div><p role="">Note: this example assumes that the LookupList
          specifies the ligature substitution lookup before the single
          substitution lookup.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.11.2"></a>Annotation</h3></div></div></div><p role="">Contextual Lookup are fundamentally the same thing in
	GSUB and GPOS. The only differences are the numeric values of
	the types (5 in GSUB, 7 in GPOS), and the LookupList against
	which the lookup indices in the SubstLookupRecord are
	resolved. It would be a great simplification for the users of
	the specification if there was a single descrription of
	Contextual subtables. The same applies to Chaining Contextual
	subtables.</p><p role="">The interaction between the LookupFlag of a contextual
	lookup and the LookupFlag of the lookup(s) it invokes is not
	very well defined. For example, if the contextual lookup does
	not skip other any glyphs, but it invokes a lookup that
	ignores some glyphs, should those be ignored?</p><p role="">The description of the SubstLookupRecord used to be in
        another place in version 1.25, after the description of
        lookups 5 and 6, I believe. As it stands, it is parts of the
        LookupType 5 description, which is a bit misleading since
        it’s also used in type 6. Recommendation: restore it in
        its own section.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383055025248"></a>Context Substitution Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.12.1"></a>Specification</h3></div></div></div><p role="">Format 1 defines the context for a glyph substitution
          as a particular sequence of glyphs. For example, a context
          could be &lt;xyz&gt;, &lt;holiday&gt;, &lt;!?*#@&gt;, or any other glyph
          sequence.</p><p role="">Within a context sequence, Format 1 identifies
          particular glyph positions (not glyph indices) as the
          targets for specific substitutions. When a text-processing
          client locates a context in a string of text, it finds the
          lookup data for a targeted position and makes a substitution
          by applying the lookup data at that location.</p><p role="">For example, if a client is to replace the glyph string
          &lt;abc&gt; with its reverse glyph string &lt;cba&gt;, the input
          context is defined as the glyph sequence, &lt;abc&gt;, and the
          lookups defined for the context are (1) “a” to
          “c” and (2) “c” to
          “a”. When a client encounters the context
          &lt;abc&gt;, the lookups are performed in the order stored.
          First, “c” is substituted for
          “a” resulting in &lt;cbc&gt;. Second,
          “a” is substituted for the “c”
          that has not yet been touched, resulting in &lt;cba&gt;.</p><p role="">To specify a context, a Coverage table lists the first
          glyph in the sequence, and a SubRule table identifies the
          remaining glyphs. To describe the &gt;abc&lt; context used in
          the previous example, the Coverage table lists the glyph
          index of the first component of the sequence ߝ the
          “a” glyph. A SubRule table defines indices for
          the “b” and “c” glyphs. </p><p role="">A single ContextSubstFormat1 subtable may define more
          than one context glyph sequence. If different context
          sequences begin with the same glyph, then the Coverage table
          should list the glyph only once because all glyphs in the
          table must be unique. For example, if three contexts each
          start with an “s” and two start with a
          “t,” then the Coverage table will list one
          “s” and one “t.”</p><p role="">For each context, a SubRule table lists all the glyphs
          that follow the first glyph. The table also contains an
          array of SubstLookupRecords that specify the substitution
          lookup data for each glyph position (including the first
          glyph position) in the context.</p><p role="">All of the SubRule tables defining contexts that begin
          with the same first glyph are grouped together and defined
          in a SubRuleSet table. For example, the SubRule tables that
          define the three contexts that begin with an
          “s” are grouped in one SubRuleSet table, and
          the SubRule tables that define the two contexts that begin
          with a “t” are grouped in a second SubRuleSet
          table. Each glyph listed in the Coverage table must have a
          SubRuleSet table defining all the SubRule tables that apply
          to a covered glyph.</p><p role="">To locate a context glyph sequence, the
          text-processing client searches the Coverage table each time
          it encounters a new text glyph. If the glyph is covered, the
          client reads the corresponding SubRuleSet table and examines
          each SubRule table in the set to determine whether the rest
          of the context matches the subsequent glyphs in the text. If
          the context and text string match, the client finds the
          target glyph positions, applies the lookups for those
          positions, and completes the substitutions.</p><p role="">A ContextSubstFormat1 subtable contains a format
          identifier (SubstFormat), an offset to a Coverage table
          (Coverage), a count of defined SubRuleSets
          (SubRuleSetCount), and an array of offsets to the SubRuleSet
          tables (SubRuleSet). As mentioned, one SubRuleSet table must
          be defined for each glyph listed in the Coverage
          table.</p><p role="">In the SubRuleSet array, the SubRuleSet table offsets
          are ordered in the Coverage Index order. The first
          SubRuleSet in the array applies to the first GlyphID listed
          in the Coverage table, the second SubRuleSet in the array
          applies to the second GlyphID listed in the Coverage table,
          and so on.</p><div class="table"><a name="idm383055014464"></a><p class="title"><strong>Table 25.13. ContextSubstFormat1 subtable: Simple context glyph
            substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ContextSubstFormat1 subtable: Simple context glyph&#10;            substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubRuleSetCount</td><td role="">Number of SubRuleSet tables – must equal
              GlyphCount in Coverage table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">SubRuleSet [SubRuleSetCount]</td><td role="">Array of offsets to SubRuleSet tables
              – from beginning of Substitution table – ordered by
              Coverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A SubRuleSet table consists of an array of offsets to
          SubRule tables (SubRule), ordered by preference, and a count
          of the SubRule tables defined in the set (SubRuleCount). The
          order in the SubRule array can be critical. Consider two
          contexts, &lt;abc&gt; and &lt;abcd&gt;. If &lt;abc&gt; is first in
          the SubRule array, all instances of &lt;abc&gt; in the
          text – including all instances of &lt;abcd&gt; – will be
          changed. If &lt;abcd&gt; comes first in the array, however,
          only &lt;abcd&gt; sequences will be changed, without affecting
          any instances of &lt;abc&gt;.</p><div class="table"><a name="idm383055005232"></a><p class="title"><strong>Table 25.14. SubRuleSet table: All contexts beginning with the
            same glyph</strong></p><div class="table-contents"><table role="" class="table" summary="SubRuleSet table: All contexts beginning with the&#10;            same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubRuleCount</td><td role="">Number of SubRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">SubRule [SubRuleCount]</td><td role="">Array of offsets to SubRule tables – from
              beginning of SubRuleSet table – ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A SubRule table consists of a count of the glyphs to
          be matched in the input context sequence (GlyphCount),
          including the first glyph in the sequence, and an array of
          glyph indices that describe the context (Input). The
          Coverage table specifies the index of the first glyph in the
          context, and the Input array begins with the second glyph
          (array index = 1) in the context sequence.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: The Input array lists the indices in the order
            the corresponding glyphs appear in the text. For text
            written from right to left, the right-most glyph will be
            first; conversely, for text written from left to right,
            the left-most glyph will be first.</p></blockquote></div><p role="">A SubRule table also contains a count of the
          substitutions to be performed on the input glyph sequence
          (SubstCount) and an array of SubstitutionLookupRecords
          (SubstLookupRecord). Each record specifies a position in the
          input glyph sequence and a LookupListIndex to the
          substitution lookup that is applied at that position. The
          array should list records in design order, or the order the
          lookups should be applied to the entire glyph
          sequence.</p><div class="table"><a name="idm383054997376"></a><p class="title"><strong>Table 25.15. SubRule table: One simple context definition</strong></p><div class="table-contents"><table role="" class="table" summary="SubRule table: One simple context definition" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Total number of glyphs in input glyph
              sequence – includes the first glyph</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Input [GlyphCount-1]</td><td role="">Array of input GlyphIDs – start with second
              glyph</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of SubstLookupRecords – in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Example 7 at the end of the chapter shows how to use
          the ContextSubstFormat1 subtable to replace a sequence of
          three glyphs with a sequence preferred for the French
          language system.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.12.2"></a>Annotation</h3></div></div></div><p role="">Second paragraph: "... locates a context in a string of
          text, ..." shoud be replaced by "... locates a context in a
          string of glyphs, ...".</p><p role="">In the fourth paragraph the '&lt;' and '&gt;' around the
          first literal context are inverted.</p><p role="">To adopt a consistent language, the last paragraph
          before the ContextSubtFormat1 table, and the last sentence
          of the previous paragraph, should be replaced by: "The
          Coverage index of the first input glyph is used to index the
          SubRuleSet array and SubRuleSetCount must equal the number
          of glyphs covered by Coverage. The entries in the SubRuleSet
          array cannot be NULL."</p><p role="">It is unclear whether the SubRuleCount of a SubRuleSet
          table can be 0. We assume that SubRuleCount must be at least
          1 and recommend that it be spelled out in the
          specification.</p><p role="">It is unclear whether the GlyphCount of a SubRule can be
          0 or 1. The value 0 is most certainly illegal (since a
          SubRule table is used in the context of a first glyph
          match). We assume that the value 1 is legal (because it
          makes sense for a similar LookupType 6 subtable), eventhough
          it is difficult to exhibit an interesting use of that
          case.</p><p role="">It is unclear whether the SubstCount of a SubRule can be
          0. At first it seems that such a SubRule could be removed,
          since it does nothing. On the other hand, this could be
          useful to prevent the activation of following SubRules; e.g.
          if one wanted the sequence &lt;abc&gt; modified, but not the
          sequence &lt;abcd&gt;. The recommendation is to explicitly
          mention that case as permitted.</p><p role="">The pattern matched by the SubRule table t = SubRuleSet
	  [m].SubRule [n] is ▶
	  I<sub>0</sub> L* I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is t.GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is {Coverage[m]}
	      ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is {t.Input [k-1]}
	      ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubRule table does not directly modify the glyph
	run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054975312"></a>Context Substitution Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.13.1"></a>Specification</h3></div></div></div><p role="">Format 2, a more flexible format than Format 1,
          describes class-based context substitution. For this format,
          a specific integer, called a class value, must be assigned
          to each glyph component in all context glyph
          sequences. Contexts are then defined as sequences of glyph
          class values. More than one context may be defined at a
          time.</p><p role="">For example, suppose that a swash capital glyph should
          replace each uppercase letter glyph that is preceded by a
          space glyph and followed by a lowercase letter glyph (a
          glyph sequence of space – uppercase –
          lowercase). The set of uppercase glyphs would constitute one
          glyph class (Class 1), the set of lowercase glyphs would
          constitute a second class (Class 2), and the space glyph
          would constitute a third class (Class 3). The input context
          might be specified with a context rule (called a
          SubClassRule) that describes “the set of glyph strings that
          form a sequence of three glyph classes, one glyph from Class
          3, followed by one glyph from Class 1, followed by one glyph
          from Class 2.”</p><p role="">Each ContextSubstFormat2 subtable contains an offset
          to a class definition table (ClassDef), which defines the
          glyph class values of all input contexts. Generally, a
          unique ClassDef table will be declared in each instance of
          the ContextSubstFormat2 table that is included in a font,
          even though several Format 2 tables could share ClassDef
          tables. Class assignments are fixed (the same for each
          position in the context), and classes are exclusive (a glyph
          cannot be in more than one class at a time). The output
          glyphs that replace the glyphs in the context sequences do
          not need class values because they are specified elsewhere
          by GlyphID.</p><p role="">The ContextSubstFormat2 subtable also contains a
          format identifier (SubstFormat) and defines an offset to a
          Coverage table (Coverage). For this format, the Coverage
          table lists indices for the complete set of unique glyphs
          (not glyph classes) that may appear as the first glyph of
          any class-based context. In other words, the Coverage table
          contains the list of glyph indices for all the glyphs in all
          classes that may be first in any of the context class
          sequences. For example, if the contexts begin with a Class 1
          or Class 2 glyph, then the Coverage table will list the
          indices of all Class 1 and Class 2 glyphs.</p><p role="">A ContextSubstFormat2 subtable also defines an array
          of offsets to the SubClassSet tables (SubClassSet) and a
          count of the SubClassSet tables (SubClassSetCnt). The array
          contains one offset for each class (including Class 0) in
          the ClassDef table. In the array, the class value defines an
          offset's index position, and the SubClassSet offsets are
          ordered by ascending class value (from 0 to SubClassSetCnt -
          1).</p><p role="">For example, the first SubClassSet listed in the array
          contains all contexts beginning with Class 0 glyphs, the
          second SubClassSet contains all contexts beginning with
          Class 1 glyphs, and so on. If no contexts begin with a
          particular class (that is, if a SubClassSet contains no
          SubClassRule tables), then the offset to that particular
          SubClassSet in the SubClassSet array will be set to
          NULL.</p><div class="table"><a name="idm383054968128"></a><p class="title"><strong>Table 25.16. ContextSubstFormat2 subtable: Class-based context
            glyph substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ContextSubstFormat2 subtable: Class-based context&#10;            glyph substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ClassDef</td><td role="">Offset to glyph ClassDef table – from beginning
              of Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubClassSetCnt</td><td role="">Number of SubClassSet tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">SubClassSet [SubClassSetCnt]</td><td role="">Array of offsets to SubClassSet tables
              – from beginning of Substitution table –
              ordered by class – may be NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each context is defined in a SubClassRule table, and
          all SubClassRules that specify contexts beginning with the
          same class value are grouped in a SubClassSet
          table. Consequently, the SubClassSet containing a context
          identifies a context's first class component.</p><p role="">Each SubClassSet table consists of a count of the
          SubClassRule tables defined in the SubClassSet
          (SubClassRuleCnt) and an array of offsets to SubClassRule
          tables (SubClassRule). The SubClassRule tables are ordered
          by preference in the SubClassRule array of the
          SubClassSet.</p><div class="table"><a name="idm383054956352"></a><p class="title"><strong>Table 25.17. SubClassSet subtable</strong></p><div class="table-contents"><table role="" class="table" summary="SubClassSet subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubClassRuleCnt</td><td role="">Number of SubClassRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">SubClassRule [SubClassRuleCount]</td><td role="">Array of offsets to SubClassRule tables – from
              beginning of SubClassSet – ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">For each context, a SubClassRule table contains a
          count of the glyph classes in the context sequence
          (GlyphCount), including the first class. A Class array lists
          the classes, beginning with the second class (array index =
          1), that follow the first class in the context.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Text order depends on the writing direction of
            the text. For text written from right to left, the
            right-most class will be first. Conversely, for text
            written from left to right, the left-most class will be
            first.</p></blockquote></div><p role="">The values specified in the Class array are the values
          defined in the ClassDef table. For example, a context
          consisting of the sequence “Class 2, Class 7, Class 5, Class
          0” will produce a Class array of 7,5,0. The first class in
          the sequence, Class 2, is identified in the
          ContextSubstFormat2 table by the SubClassSet array index of
          the corresponding SubClassSet.</p><p role="">A SubClassRule also contains a count of the
          substitutions to be performed on the context (SubstCount)
          and an array of SubstLookupRecords (SubstLookupRecord) that
          supply the substitution data. For each position in the
          context that requires a substitution, a SubstLookupRecord
          specifies a LookupList index and a position in the input
          glyph sequence where the lookup is applied. The
          SubstLookupRecord array lists SubstLookupRecords in design
          order – that is, the order in which lookups should be applied
          to the entire glyph sequence.</p><div class="table"><a name="idm383054947440"></a><p class="title"><strong>Table 25.18. SubClassRule table: Context definition for one
            class</strong></p><div class="table-contents"><table role="" class="table" summary="SubClassRule table: Context definition for one&#10;            class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Total number of classes specified for the
              context in the rule – includes the first
              class</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Class [GlyphCount-1]</td><td role="">Array of classes – beginning with the second
              class – to be matched to the input glyph class
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of Substitution lookups – in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Example 8 at the end of this chapter uses Format 2 to
          substitute Arabic mark glyphs for base glyphs of different
          heights.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.13.2"></a>Annotation</h3></div></div></div><p role="">In the third paragraph, the possibility of sharing of a
          class definition is too restrictive: a class definition
          could be used in a LookupType 6, for example. The
          recommendation is to replace "Generally" by "Typically", and
          the part of the sentence starting with "even though" by
          "but in general, a class definition can be used in multiple
          lookups."</p><p role="">In the description of the Coverage in the fourth
          paragraph, the sentences starting with "In other words," are
          a bit misleading: the coverage may contain more or less than
          the union of the classes that have non-NULL SubClassSet
          offsets. This can be useful when the class definition is
          shared by multiple lookups. The recommendation is to replace
          the fouth paragraph by: "The ContextSubstFormat2 subtable
          also contains a format identifier (SubstFormat) and defines
          an offset to a Coverage table (Coverage). The lookup will
          apply only if the current glyph is covered by Coverage.
          Typically, the coverage is the union of the classes that
          appear as the first class of any context; for example, if
          the contexts begin with classes 1 and 2, then the Coverage
          will be exactly the glyphs in classes 1 and 2. However, this
          is not mandatory; in particular, it may be useful to have a
          Coverage which is a subset of those glyphs."</p><p role="">To adopt a more consistent language, in the fifth
          paragraph, the sentences following the first should be
          replaced by: "The class of the first input glyph under
          ClassDef is used to index the SubClassSet array and
          SubClassSetCnt must equal the number of classes defined by
          ClassDef (including class 0)."</p><p role="">It is unclear whether the SubClassRuleCnt of a
          SubClassSet table can be 0. We assume that SubRuleCount must
          be at least 1 and recommend that it be spelled out in the
          specification.</p><p role="">It is unclear whether the GlyphCount of a SubClassRule
          can be 0 or 1. The value 0 is most certainly illegal (since
          a SubClassRule table is used in the context of a first glyph
          match). We assume that the value 1 is legal (because it
          makes sense for a similar LookupType 6 subtable), eventhough
          it is difficult to exhibit an interesting use of that
          case.</p><p role="">It is unclear whether the SubstCount of a SubClassRule
          can be 0. At first it seems that such a SubClassRule could
          be removed, since it does nothing. On the other hand, this
          could be useful to prevent the activation of following
          SubClassRules; e.g. if one wanted the sequence &lt;1 2 3&gt;
          modified, but not the sequence &lt;1 2 3 4&gt;. The
          recommendation is to explicitly mention that case as
          permitted.</p><p role="">The pattern matched by the SubClassRule table t = SubClassSet
	  [m].SubClassRule [n] is
	  ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is t.GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is (Coverage ∩
	      ClassDef [m]) ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is ClassDef [t.Class
	      [k-1]] ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubClassRule table does not directly modify the glyph
	run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054925408"></a>Context Substitution Format 3</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.14.1"></a>Specification</h3></div></div></div><p role="">Format 3, coverage-based context substitution, defines
          a context rule as a sequence of coverage tables. Each
          position in the sequence may define a different Coverage
          table for the set of glyphs that matches the context
          pattern. With Format 3, the glyph sets defined in the
          different Coverage tables may intersect, unlike Format 2
          which specifies fixed class assignments (identical for each
          position in the context sequence) and exclusive classes (a
          glyph cannot be in more than one class at a time).</p><p role="">For example, consider an input context that contains a
          lowercase glyph (position 0), followed by an uppercase glyph
          (position 1), either a lowercase or numeral glyph (position
          2), and then either a lowercase or uppercase vowel (position
          3). This context requires four Coverage tables, one for each
          position:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">In position 0, the Coverage table lists the set of
              lowercase glyphs.</p></li><li role="" class="listitem"><p role="">In position 1, the Coverage table lists the set of
              uppercase glyphs.</p></li><li role="" class="listitem"><p role="">In position 2, the Coverage table lists the set of
              lowercase and numeral glyphs, a superset of the glyphs
              defined in the Coverage table for position 0.</p></li><li role="" class="listitem"><p role="">In position 3, the Coverage table lists the set of
              lowercase and uppercase vowels, a subset of the glyphs
              defined in the Coverage tables for both positions 0 and
              1.</p></li></ul></div><p role="">Unlike Formats 1 and 2, this format defines only one
          context rule at a time. It consists of a format identifier
          (SubstFormat), a count of the glyphs in the sequence to be
          matched (GlyphCount), and an array of Coverage offsets that
          describe the input context sequence (Coverage).</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: The order of the Coverage tables listed in the
            Coverage array must follow the writing direction. For text
            written from right to left, then the right-most glyph will
            be first. Conversely, for text written from left to right,
            the left-most glyph will be first.</p></blockquote></div><p role="">The subtable also contains a count of the
          substitutions to be performed on the input Coverage sequence
          (SubstCount) and an array of SubstLookupRecords
          (SubstLookupRecord) in design order – that is, the order in
          which lookups should be applied to the entire glyph
          sequence.</p><p role="">Example 9 at the end of this chapter substitutes swash
          glyphs for two out of three glyphs in a sequence.</p><div class="table"><a name="idm383054914464"></a><p class="title"><strong>Table 25.19. ChainContextSubstFormat3 subtable: Coverage-based
            context glyph substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextSubstFormat3 subtable: Coverage-based&#10;            context glyph substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs in the input glyph
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [GlyphCount]</td><td role="">Array of offsets to Coverage table – from
              beginning of Substitution table – in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of SubstLookupRecords – in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.14.2"></a>Annotation</h3></div></div></div><p role="">It's probably worth noting that GlyphCount should be
          non-zero.</p><p role="">It is unclear whether the SubstCount can be 0. At first
          it seems that such a subtable is not interesting, since it
          does nothing. On the other hand, this could be useful to
          prevent the activation of following subtables. The
          recommendation is to explicitly mention that case as
          permitted.</p><p role="">The pattern matched by this subtable is ▶
	  I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">i is GlyphCount</p></li><li role="" class="listitem"><p role="">I<sub>i</sub> is
		Coverage [i] ∖ LookupFlag.</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">This table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054895952"></a>Lookup Type 6: Chaining Contextual Substitution Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.15.1"></a>Specification</h3></div></div></div><p role="">A Chaining Contextual Substitution subtable
          (ChainContextSubst) describes glyph substitutions in context
          with an ability to look back and/or look ahead in the
          sequence of glyphs. The design of the Chaining Contextual
          Substitution subtable is parallel to that of the Contextual
          Substitution subtable, including the availability of three
          formats for handling sequences of glyphs, glyph classes, or
          glyph sets. Each format can describe one or more backtrack,
          input, and lookahead sequences and one or more substitutions
          for each sequence.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.15.2"></a>Annotation</h3></div></div></div><p role="">In all three formats, the sequences are represented by
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
	  LookaheadGlyphCount - 1</em></span>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054887792"></a>Chaining Context Substitution Format 1: Simple Chaining
        Context Glyph Substitution</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.16.1"></a>Specification</h3></div></div></div><p role="">Format 1 defines the context for a glyph substitution
          as a particular sequence of glyphs. For example, a context
          could be &lt;xyz&gt;, &lt;holiday&gt;, &lt;!?*#@&gt;, or any other glyph
          sequence.</p><p role="">Within a context sequence, Format 1 identifies
          particular glyph positions (not glyph indices) as the
          targets for specific substitutions. When a text-processing
          client locates a context in a string of text, it finds the
          lookup data for a targeted position and makes a substitution
          by applying the lookup data at that location.</p><p role="">To specify the context, the coverage table lists the
          first glyph in the input sequence, and the ChainSubRule
          subtable defines the rest. Once a covered glyph is found at
          position i, the client reads the corresponding
          ChainSubRuleSet table and examines each table to determine
          if it matches the surrounding glyphs in the text. There is a
          match if the string &lt;backtrack sequence&gt; + &lt;covered
          glyph&gt; + &lt;input sequence&gt;+&lt;lookahead sequence&gt; matches
          with the glyphs at position i - BacktrackGlyphCount in the
          text.</p><p role="">To clarify the ordering of glyph arrays for input,
	  backtrack and lookahead sequences, the following
	  illustration is provided. Input sequence match begins at i
	  where the input sequence match begins. The backtrack
	  sequence is ordered beginning at i - 1 and increases in
	  offset value as one moves away from i. The lookahead
	  sequence begins after the input sequence and increases in
	  logical order.</p><div role="" class="literallayout"><p><br/>
Logical order      - a  b  c  d  e  f  g  h  i  j<br/>
                                 i<br/>
Input sequence -                 0  1<br/>
Backtrack sequence - 3  2  1  0<br/>
Lookahead sequence -                   0  1  2  3<br/>
</p></div><p role="">If there is a match, then the client finds the target
          glyph positions for substitutions and completes the
          substitutions. Please note that (just like in the
          ContextSubstFormat1 subtable) these lookups are required to
          operate within the range of text from the covered glyph to
          the end of the input sequence. No substitutions can be
          defined for the backtracking sequence or the lookahead
          sequence.</p><p role="">Once the substitutions are complete, the client should
          move to the glyph position <span role="" class="emphasis"><em>immediately following
            the matched input sequence</em></span> and resume the
          lookup process from there.</p><p role="">A single ChainContextSubstFormat1 subtable may define
          more than one context glyph sequence. If different context
          sequences begin with the same glyph, then the Coverage table
          should list the glyph only once because all glyphs in the
          table must be unique. For example, if three contexts each
          start with an "s" and two start with a "t," then the
          Coverage table will list one "s" and one "t."</p><p role="">All of the ChainSubRule tables defining contexts that
          begin with the same first glyph are grouped together and
          defined in a ChainSubRuleSet table. For example, the
          ChainSubRule tables that define the three contexts that
          begin with an "s" are grouped in one ChainSubRuleSet table,
          and the ChainSubRule tables that define the two contexts
          that begin with a "t" are grouped in a second
          ChainSubRuleSet table. Each glyph listed in the Coverage
          table must have a ChainSubRuleSet table defining all the
          ChainSubRule tables that apply to a covered glyph.</p><p role="">A ChainContextSubstFormat1 subtable contains a format
          identifier (SubstFormat), an offset to a Coverage table
          (Coverage), a count of defined ChainSubRuleSets
          (ChainSubRuleSetCount), and an array of offsets to the
          ChainSubRuleSet tables (ChainSubRuleSet). As mentioned, one
          ChainSubRuleSet table must be defined for each glyph listed
          in the Coverage table.</p><p role="">In the ChainSubRuleSet array, the ChainSubRuleSet
          table offsets are ordered in the Coverage Index order. The
          first ChainSubRuleSet in the array applies to the first
          GlyphID listed in the Coverage table, the second
          ChainSubRuleSet in the array applies to the second GlyphID
          listed in the Coverage table, and so on.</p><div class="table"><a name="idm383054876144"></a><p class="title"><strong>Table 25.20. ChainContextSubstFormat1 subtable: Simple context
            glyph substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextSubstFormat1 subtable: Simple context&#10;            glyph substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ChainSubRuleSetCount</td><td role="">Number of ChainSubRuleSet tables – must equal
              GlyphCount in Coverage table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainSubRuleSet [ChainSubRuleSetCount]</td><td role="">Array of offsets to ChainSubRuleSet tables
              – from beginning of Substitution table –
              ordered by Coverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A ChainSubRuleSet table consists of an array of
          offsets to ChainSubRule tables (ChainSubRule), ordered by
          preference, and a count of the ChainSubRule tables defined
          in the set (ChainSubRuleCount).</p><p role="">The order in the ChainSubRule array can be
          critical. Consider two contexts, &lt;abc&gt; and &lt;abcd&gt;. If
          &lt;abc&gt; is first in the ChainSubRule array, all instances
          of &lt;abc&gt; in the text – including all instances of
          &lt;abcd&gt; – will be changed. If &lt;abcd&gt; comes first in the
          array, however, only &lt;abcd&gt; sequences will be changed,
          without affecting any instances of &lt;abc&gt;.</p><div class="table"><a name="idm383054865728"></a><p class="title"><strong>Table 25.21. ChainSubRuleSet table: All contexts beginning with
            the same glyph</strong></p><div class="table-contents"><table role="" class="table" summary="ChainSubRuleSet table: All contexts beginning with&#10;            the same glyph" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ChainSubRuleCount</td><td role="">Number of ChainSubRule tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainSubRule [ChainSubRuleCount]</td><td role="">Array of offsets to ChainSubRule tables – from
              beginning of ChainSubRuleSet table – ordered by
              preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A ChainSubRule table consists of a count of the glyphs
          to be matched in the backtrack, input, and lookahead context
          sequences, including the first glyph in each sequence, and
          an array of glyph indices that describe each portion of the
          contexts. The Coverage table specifies the index of the
          first glyph in each context, and each array begins with the
          second glyph (array index = 1) in the context
          sequence.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: All arrays list the indices in the order the
            corresponding glyphs appear in the text. For text written
            from right to left, the right-most glyph will be first;
            conversely, for text written from left to right, the
            left-most glyph will be first.</p></blockquote></div><p role="">A ChainSubRule table also contains a count of the
          substitutions to be performed on the input glyph sequence
          (SubstCount) and an array of SubstitutionLookupRecords
          (SubstLookupRecord). Each record specifies a position in the
          input glyph sequence and a LookupListIndex to the
          substitution lookup that is applied at that positon. The
          array should list records in design order, or the order the
          lookups should be applied to the entire glyph
          sequence.</p><div class="table"><a name="idm383054857248"></a><p class="title"><strong>Table 25.22. ChainSubRule subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ChainSubRule subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Backtrack [BacktrackGlyphCount]</td><td role="">Array of backtracking GlyphID's (to be
              matched before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Total number of glyphs in the input sequence
              (includes the first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Input [InputGlyphCount-1]</td><td role="">Array of input GlyphIDs (start with second
              glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Total number of glyphs in the look ahead
              sequence (number of glyphs to be matched after the input
              sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">LookAhead [LookAheadGlyphCount]</td><td role="">Array of lookahead GlyphID's (to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of SubstLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.16.2"></a>Annotation</h3></div></div></div><p role="">Second paragraph: "... locates a context in a string of
          text, ..." shoud be replaced by "... locates a context in a
          string of glyphs, ...". Similarly, in the third paragraph,
          replace the last word, "text", by "gyph string".</p><p role="">Third paragraph, second sentence: add "ChainSubRule" in
          "examines each table".</p><p role="">To a consistent language, the last paragraph before the
          ChainContextSubtFormat1 table, and the last sentence of the
          previous paragraph, should be replaced by: "The Coverage
          index of the first input glyph is used to index the
          ChainSubRuleSet array and ChainSubRuleSetCount must equal
          the number of glyphs covered by Coverage. The entries in the
          ChainSubRuleSet array cannot be NULL."</p><p role="">The paragraph describing the impact of the order in the
          ChainSubRule array is a bit misleading. The recommendation
          is to change the last two sentences by "If &lt;abc&gt; is first
          in the ChainSubRule array, the corresponding ChainSubRule
          subtable will be applied first to all instances of &lt;abc&gt;
          in the glyph string – including all instances of
          &lt;abcd&gt; –. If &lt;abcd&gt; comes first in the array,
          the corresponding ChainSubRule subtable will be applied
          applied first to all instances of &lt;abcd&gt;."</p><p role="">It is unclear whether the ChainSubRuleCount of a
          ChainSubRuleSet table can be 0. We assume that
          ChainSubRuleCount must be at least 1 and recommend that it
          be spelled out in the specification.</p><p role="">It is unclear whether the InputGlyphCount of a
          ChainSubRule can be 0 or 1. The value 0 is most certainly
          illegal (since a ChainSubRule table is used in the context
          of a first glyph match). We assume that the value 1 is
          legal, eventhough it is difficult to exhibit an interesting
          use of that case.</p><p role="">It is unclear whether the SubstCount of a SubRule can be
          0. At first it seems that such a SubRule could be removed,
          since it does nothing. On the other hand, this could be
          useful to prevent the activation of following SubRules; e.g.
          if one wanted the sequence &lt;abc&gt; modified, but not the
          sequence &lt;abcd&gt;.  The recommendation is to explicitly
          mention that case as permitted.</p><p role="">There is a little ambiguity about the next glyph to
          process: consider the case where some glyphs captured by
          LookupFlag are present between the input glyphs and the
          lookahead glyphs. Should the processing continue with the
          first glyph following with input glyphs, i.e. with the first
          glyph captured by LookupFlag, or should it continue with the
          first lookahead glyph? Whether this matters depends quite on
          bit whether the LookupFlag of a context substitution is
          inherited (either by definition or by constraint on the
          valid font files), and therefore whether a lookup in
          SubstLookupRecord can or cannot change those glyphs.</p><p role="">The pattern matched by the ChainSubRule table t = ChainSubRuleSet
	  [m].ChainSubRule [n] is

	  B<sub>b-1</sub> L* ... L* B<sub>0</sub>
          ▶ I<sub>0</sub> L*
	  I<sub>1</sub> L* ... L*
	  I<sub>i-1</sub> ◀
          L* A<sub>0</sub> L*
	  ... L* A<sub>a-1</sub>, where:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">b is t.BacktrackGlyphCount</p></li><li role="" class="listitem"><p role="">i is t.InputGlyphCount</p></li><li role="" class="listitem"><p role="">a is t.LookaheadGlyphCount</p></li><li role="" class="listitem"><p role="">B<sub>k</sub> is {t.Backtrack [k]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>0</sub> is {Coverage[m]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">I<sub>k</sub> is {t.Input[k-1]} ∖ LookupFlag, for k &gt; 0</p></li><li role="" class="listitem"><p role="">A<sub>k</sub> is {t.LookAhead[k]} ∖ LookupFlag</p></li><li role="" class="listitem"><p role="">L is LookupFlag</p></li></ul></div><p role="">A SubRule table does not directly modify the glyph
	  run. Instead, it invokes other lookups at the current
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054821888"></a>Chaining Context Substitution Format 2: Class-based Chaining
        Context Glyph Substitution</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.17.1"></a>Specification</h3></div></div></div><p role="">Format 2 describes class-based chaining context
          substitution. For this format, a specific integer, called a
          class value, must be assigned to each glyph component in all
          context glyph sequences. Contexts are then defined as
          sequences of glyph class values. More than one context may
          be defined at a time.</p><p role="">To chain contexts, three classes are used in the glyph
          ClassDef table: Backtrack ClassDef, Input ClassDef, and
          Lookahead ClassDef.</p><p role="">The ChainContextSubstFormat2 subtable also contains a
          format identifier (SubstFormat) and defines an offset to a
          Coverage table (Coverage). For this format, the Coverage
          table lists indices for the complete set of unique glyphs
          (not glyph classes) that may appear as the first glyph of
          any class-based context. In other words, the Coverage table
          contains the list of glyph indices for all the glyphs in all
          classes that may be first in any of the context class
          sequences. For example, if the contexts begin with a Class 1
          or Class 2 glyph, then the Coverage table will list the
          indices of all Class 1 and Class 2 glyphs.</p><p role="">A ChainContextSubstFormat2 subtable also defines an
          array of offsets to the ChainSubClassSet tables
          (ChainSubClassSet) and a count of the ChainSubClassSet
          tables (ChainSubClassSetCnt). The array contains one offset
          for each class (including Class 0) in the ClassDef table. In
          the array, the class value defines an offset's index
          position, and the ChainSubClassSet offsets are ordered by
          ascending class value (from 0 to ChainSubClassSetCnt -
          1).</p><p role="">If no contexts begin with a particular class (that is,
          if a ChainSubClassSet contains no ChainSubClassRule tables),
          then the offset to that particular ChainSubClassSet in the
          ChainSubClassSet array will be set to NULL.</p><div class="table"><a name="idm383054816544"></a><p class="title"><strong>Table 25.23. ChainContextSubstFormat2 subtable: Class-based
            chaining context glyph substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextSubstFormat2 subtable: Class-based&#10;            chaining context glyph substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table – from beginning of
              Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BacktrackClassDef</td><td role="">Offset to glyph ClassDef table containing
              backtrack sequence data – from beginning of Substitution
              table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">InputClassDef</td><td role="">Offset to glyph ClassDef table containing
              input sequence data – from beginning of Substitution
              table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LookaheadClassDef</td><td role="">Offset to glyph ClassDef table containing
              lookahead sequence data – from beginning of Substitution
              table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ChainSubClassSetCnt</td><td role="">Number of ChainSubClassSet
              tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainSubClassSet [ChainSubClassSetCnt]</td><td role="">Array of offsets to ChainSubClassSet tables
              – from beginning of Substitution table –
              ordered by input class – may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each context is defined in a ChainSubClassRule table,
          and all ChainSubClassRules that specify contexts beginning
          with the same class value are grouped in a ChainSubClassSet
          table. Consequently, the ChainSubClassSet containing a
          context identifies a context's first class component.</p><p role="">Each ChainSubClassSet table consists of a count of the
          ChainSubClassRule tables defined in the ChainSubClassSet
          (ChainSubClassRuleCnt) and an array of offsets to
          ChainSubClassRule tables (ChainSubClassRule). The
          ChainSubClassRule tables are ordered by preference in the
          ChainSubClassRule array of the ChainSubClassSet.</p><div class="table"><a name="idm383054801056"></a><p class="title"><strong>Table 25.24. ChainSubClassSet subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ChainSubClassSet subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ChainSubClassRuleCnt</td><td role="">Number of ChainSubClassRule
              tables</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">ChainSubClassRule [ChainSubClassRuleCount]</td><td role="">Array of offsets to ChainSubClassRule tables
              – from beginning of ChainSubClassSet –
              ordered by preference</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">For each context, a ChainSubClassRule table contains a
          count of the glyph classes in the context sequence
          (GlyphCount), including the first class. A Class array lists
          the classes, beginning with the second class (array index =
          1), that follow the first class in the context.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Text order depends on the writing direction of
            the text. For text written from right to left, the
            right-most class will be first. Conversely, for text
            written from left to right, the left-most class will be
            first.</p></blockquote></div><p role="">The values specified in the Class array are the values
          defined in the ClassDef table. The first class in the
          sequence, Class 2, is identified in the
          ChainContextSubstFormat2 table by the ChainSubClassSet array
          index of the corresponding ChainSubClassSet.</p><p role="">A ChainSubClassRule also contains a count of the
          substitutions to be performed on the context (SubstCount)
          and an array of SubstLookupRecords (SubstLookupRecord) that
          supply the substitution data. For each position in the
          context that requires a substitution, a SubstLookupRecord
          specifies a LookupList index and a position in the input
          glyph sequence where the lookup is applied. The
          SubstLookupRecord array lists SubstLookupRecords in design
          order – that is, the order in which lookups should be applied
          to the entire glyph sequence.</p><div class="table"><a name="idm383054792624"></a><p class="title"><strong>Table 25.25. ChainSubClassRule table: Chaining context definition
            for one class</strong></p><div class="table-contents"><table role="" class="table" summary="ChainSubClassRule table: Chaining context definition&#10;            for one class" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Total number of glyphs in the backtrack
              sequence (number of glyphs to be matched before the
              first glyph)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Backtrack [BacktrackGlyphCount]</td><td role="">Array of backtracking classes(to be matched
              before the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Total number of classes in the input sequence
              (includes the first class)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Input [InputGlyphCount-1]</td><td role="">Array of input classes(start with second
              class; to be matched with the input glyph
              sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Total number of classes in the look ahead
              sequence (number of classes to be matched after the
              input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookAhead [LookAheadGlyphCount]</td><td role="">Array of lookahead classes(to be matched
              after the input sequence)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of SubstLookupRecords (in design
              order)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.17.2"></a>Annotation</h3></div></div></div><p role="">The first two paragraphs are somewhat contradictory. The
          recommendation is to replace them by "Format 2 describes
          class-based chaining context substitution. Three class
          definitions are used: one for backtrack sequences
          (BacktrackClassDef), one for input sequences
          (InputClassDef), and one for lookahead sequences
          (LookaheadClassDef). Contexts are then defined as sequences
          of glyph class values, interpreted with respect to the
          corresponding class definitions. More than one context may
          be defined at a time."</p><p role="">In the description of the Coverage in the third
          paragraph, the sentences starting with "In other words," are
          a bit misleading: the coverage may contain more or less than
          the union of the classes that have non-NULL ChainSubClassSet
          offsets. This can be useful when the class definition is
          shared by multiple lookups. The recommendation is to replace
          the third paragraph by: "The ChainContextSubstFormat2
          subtable also contains a format identifier (SubstFormat) and
          defines an offset to a Coverage table (Coverage). The lookup
          will apply only if the current glyph is covered by Coverage.
          Typically, the coverage is the union of the classes that
          appear as the first class of the input sequence of any
          context; for example, if the input sequences of the contexts
          begin with classes 1 and 2, then the Coverage will be
          exactly the glyphs in classes 1 and 2. However, this is not
          mandatory; in particular, it may be useful to have a
          Coverage which is a subset of those glyphs."</p><p role="">To adopt a more consistent language, in the fourth
          paragraph, the sentences following the first should be
          replaced by: "The class of the first input glyph under
          InputClassDef is used to index the ChainSubClassSet array and
          ChainSubClassSetCnt must equal the number of classes defined by
          InputClassDef (including class 0)."</p><p role="">It is unclear whether the ChainSubClassRuleCnt of a
          ChainSubClassSet table can be 0. We assume that
          ChainSubRuleCount must be at least 1 and recommend that it
          be spelled out in the specification.</p><p role="">It is unclear whether the InputGlyphCount of a ChainSubClassRule
          can be 0 or 1. The value 0 is most certainly illegal (since
          a SubClassRule table is used in the context of a first glyph
          match). We assume that the value 1 is legal (because it
          makes sense for a similar LookupType 6 subtable), eventhough
          it is difficult to exhibit an interesting use of that
          case.</p><p role="">It is unclear whether the BacktrackGlyphCount and
          Lookaheadglyphcount can be 0. We assume they can be, and
          recommend it be spelled out in the specification.</p><p role="">It is unclear whether the SubstCount of a ChainSubClassRule
          can be 0. At first it seems that such a ChainSubClassRule could
          be removed, since it does nothing. On the other hand, this
          could be useful to prevent the activation of following
          ChainSubClassRules; e.g. if one wanted the sequence &lt;1 2 3&gt;
          modified, but not the sequence &lt;1 2 3 4&gt;. The
          recommendation is to explicitly mention that case as
          permitted.</p><p role="">The pattern matched by the ChainSubClassRule table t = ChainSubClassSet [m].ChainSubRule [n] is

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
	  position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054758368"></a>Chaining Context Substitution Format 3: Coverage-based Chaining
        Context Glyph Substitution</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.18.1"></a>Specification</h3></div></div></div><p role="">Format 3 defines a chaining context rule as a sequence
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
            the left-most glyph will be first.</p></blockquote></div><p role="">The subtable also contains a count of the
          substitutions to be performed on the input Coverage sequence
          (SubstCount) and an array of SubstLookupRecords
          (SubstLookupRecord) in design order: that is, the order in
          which lookups should be applied to the entire glyph
          sequence. (SubstLookupRecords are described next.)</p><div class="table"><a name="idm383054753664"></a><p class="title"><strong>Table 25.26. ChainContextSubstFormat3 subtable: Coverage-based
            chaining context glyph substitution</strong></p><div class="table-contents"><table role="" class="table" summary="ChainContextSubstFormat3 subtable: Coverage-based&#10;            chaining context glyph substitution" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier – format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Number of glyphs in the backtracking
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [BacktrackGlyphCount]</td><td role="">Array of offsets to coverage tables in
              backtracking sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">InputGlyphCount</td><td role="">Number of glyphs in input
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [InputGlyphCount]</td><td role="">Array of offsets to coverage tables in input
              sequence, in glyph sequence order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Number of glyphs in lookahead
              sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [LookaheadGlyphCount]</td><td role="">Array of offsets to coverage tables in
              lookahead sequence, in glyph sequence
              order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubstCount</td><td role="">Number of SubstLookupRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">SubstLookupRecord [SubstCount]</td><td role="">Array of SubstLookupRecords, in design
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.18.2"></a>Annotation</h3></div></div></div><p role="">It is probably worth noting that InputGlyphCount should
          be non-zero, and that BacktrackGlyphCount and
          LookaheadGlyphCount can be zero.</p><p role="">It is unclear whether the SubstCount can be 0. At first
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
	  run. Instead, it invokes other lookups at the current position.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054722896"></a>LookupType 7: Extension Substitution</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.19.1"></a>Specification</h3></div></div></div><p role="">This lookup provides a mechanism whereby any other
          lookup type's subtables are stored at a 32-bit offset
          location in the <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table. This is
          needed if the total size of the subtables exceeds the 16-bit
          limits of the various other offsets in the
          <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table. In this specification, the
          subtable stored at the 32-bit offset location is termed the
          “extension” subtable.</p><div class="table"><a name="idm383054718800"></a><p class="title"><strong>Table 25.27. ExtensionSubstFormat1 subtable</strong></p><div class="table-contents"><table role="" class="table" summary="ExtensionSubstFormat1 subtable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">SubstFormat</td><td role="">Format identifier. Set to 1.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">ExtensionLookupType</td><td role="">Lookup type of subtable referenced by
              ExtensionOffset (i.e. the extension
              subtable).</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ExtensionOffset</td><td role="">Offset to the extension subtable, of lookup
              type ExtensionLookupType, relative to the start of the
              ExtensionSubstFormat1 subtable.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">ExtensionLookupType must be set to any lookup type other
          than 7. All subtables in a LookupType 7 lookup must have the
          same ExtensionLookupType. All offsets in the extension
          subtables are set in the usual way, i.e. relative to the
          extension subtables themselves.</p><p role="">When an OpenType layout engine encounters a LookupType 7
          Lookup table, it shall:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Proceed as though the Lookup table's LookupType
              field were set to the ExtensionLookupType of the
              subtables.</p></li><li role="" class="listitem"><p role="">Proceed as though each extension subtable referenced
              by ExtensionOffset replaced the LookupType 7 subtable
              that referenced it.</p></li></ul></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.19.2"></a>Annotation</h3></div></div></div><p role="">This subtable does not match a pattern by itself, nor
	  does it have an action by itself.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054706128"></a>Lookup Type 8: Reverse Chaining Contextual Single
	Substitution</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.20.1"></a>Specification</h3></div></div></div><p role="">Reverse Chaining Contextual Single Substitution subtable
	  (ReverseChainSingleSubst) describes single glyph
	  substitutions in context with an ability to look back and/or
	  look ahead in the sequence of glyphs. The major difference
	  between this and other lookup types is that processing of
	  input glyph sequence goes from end to start. Comparing to
	  Chaining Contextual Sustitution this format is restricted to
	  only coverage based subtable format, input sequence could
	  contain only single glyph and only single substitution
	  allowed on this glyph. This substitution rule is integrated
	  into subtable format.</p><p role="">This lookup type is designed specifically for the Arabic
	  script writing styles, like nastaliq, where the shape of the
	  glyph is determined by the following glyph, beginning at the
	  last glyph of the "joor", or set of connected glyphs. An
	  example of this lookup type is defined in Example 10 at the
	  end of this chapter.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054701968"></a>Reverse Chaining Contextual Single Substitution Format 1:
	Coverage Based Reverse Chaining Contextual Single Glyph
	Substitution.</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.21.1"></a>Specification</h3></div></div></div><p role="">Format 1 defines a chaining context rule as a sequence
	  of Coverage tables. Each position in the sequence may define
	  a different Coverage table for the set of glyphs that
	  matches the context pattern. With Format 1, the glyph sets
	  defined in the different Coverage tables may
	  intersect.</p><p role="">Note: Despite reverse order processing, the order of the
	  Coverage tables listed in the Coverage array must be in
	  logical order (follow the writing direction). The backtrack
	  sequence is as illustrated in the LookupType 6: Chaining
	  Contextual Substitution subtable. The input sequence is one
	  glyph located at i in the logical string. The backtrack
	  begins at i - 1 and increases in offset value as one moves
	  toward the logical beginning of the string. The lookahead
	  sequence begins at i + 1 and increases in offset value as
	  one moves toward the logical end of the string. In the
	  reverse chaining process i began at the logical end of the
	  string and moves to the beginning.</p><p role="">The subtable contains Coverage table for input glyph and
	  Coverage table arrays for lookahead and backtrack sequences,
	  also count of output glyph indices in the Substitute array
	  (GlyphCount), and a list of the output glyph indices
	  (Substitute array). The Substitute array must contain the
	  same number of glyph indices as the Coverage table. To
	  locate the corresponding output glyph index in the
	  Substitute array, this format uses the Coverage Index
	  returned from the Coverage table.</p><div class="table"><a name="idm383054697360"></a><p class="title"><strong>Table 25.28. ReverseChainSingleSubstFormat1 subtable:
	    Coverage-based Reverse Chaining Contextual Single Glyph
	    substitution.</strong></p><div class="table-contents"><table role="" class="table" summary="ReverseChainSingleSubstFormat1 subtable:&#10;&#9;    Coverage-based Reverse Chaining Contextual Single Glyph&#10;&#9;    substitution." border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">SubstFormat</td><td role="">Format identifier ’ format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage</td><td role="">Offset to Coverage table - from beginning of
	      Substitution table</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BacktrackGlyphCount</td><td role="">Number of glyphs in the backtracking
	      sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage [BacktrackGlyphCount]</td><td role="">Array of offsets to coverage tables in
	      backtracking sequence, in glyph sequence order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookaheadGlyphCount</td><td role="">Number of glyphs in lookahead sequence</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Coverage[LookaheadGlyphCount]</td><td role="">Array of offsets to coverage tables in
	      lookahead sequence, in glyph sequence order</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of GlyphIDs in the Substitute array</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">Substitute[GlyphCount]</td><td role="">Array of substitute GlyphIDs-ordered by
	      Coverage Index</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383054682192"></a>Substitution Lookup Record</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.22.1"></a>Specification</h3></div></div></div><p role="">All contextual substitution subtables specify the
          substitution data in a Substitution Lookup Record
          (SubstLookupRecord). Each record contains a SequenceIndex,
          which indicates the position where the substitution will
          occur in the glyph sequence. In addition, a LookupListIndex
          identifies the lookup to be applied at the glyph position
          specified by the SequenceIndex.</p><p role="">The contextual substitution subtables defined in
          Examples 7, 8, and 9 at the end of this chapter show
          SubstLookupRecords.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.22.2"></a>Annotation</h3></div></div></div><p role="">As noted earlier, the description of a SubstLookupRecord
          should be moved back in this section.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053375344"></a>GSUB Subtable Examples</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.23.1"></a>Specification</h3></div></div></div><p role="">The rest of this chapter describes and illustrates
          examples of all the <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> subtables,
          including each of the three formats available for contextual
          substitutions. All the examples reflect unique parameters
          described below, but the samples provide a useful reference
          for building subtables specific to other situations.</p><p role="">All the examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053370992"></a>Example 1: GSUB Header Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.24.1"></a>Specification</h3></div></div></div><p role="">Example 1 shows a typical <a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> Header table
          definition.</p><div class="table"><a name="idm383053368064"></a><p class="title"><strong>Table 25.29. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">GSUBHeader</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheGSUBHeader</td><td role="">GSUBHeader table
                  definition</td></tr><tr><td role="">00010000</td><td role="">0x00010000</td><td role="">version</td></tr><tr><td role="">000A</td><td role="">TheScriptList</td><td role="">offset to ScriptList table</td></tr><tr><td role="">001E</td><td role="">TheFeatureList</td><td role="">offset to FeatureList table</td></tr><tr><td role="">002C</td><td role="">TheLookupList</td><td role="">offset to LookupList table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053356800"></a>Example 2: SingleSubstFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.25.1"></a>Specification</h3></div></div></div><p role="">Example 2 illustrates the SingleSubstFormat1 subtable,
          which uses ranges to replace single input glyphs with their
          corresponding output glyphs. The indices of the output
          glyphs are calculated by adding a constant delta value to
          the indices of the input glyphs. In this example, the
          Coverage table has a format identifier of 1 to indicate the
          range format, which is used because the input glyph indices
          are in consecutive order in the font. The Coverage table
          specifies one range that contains a StartGlyphID for the "0"
          (zero) glyph and an EndGlyphID for the "9" glyph.</p><div class="table"><a name="idm383053353904"></a><p class="title"><strong>Table 25.30. Example 2</strong></p><div class="table-contents"><table role="" class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">SingleSubstFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LiningNumeralSubtable</td><td role="">SingleSubst subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat, ranges</td></tr><tr><td role="">0006</td><td role="">LiningNumeralCoverage</td><td role="">offset to Coverage table for input
                  glyphs</td></tr><tr><td role="">00C0</td><td role="">192</td><td role="">DeltaGlyphID = 192, add to each input glyph
                  index to produce output glyph inde</td></tr><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LiningNumeralCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat, ranges   1 RangeCount
                  RangeRecord[0]</td></tr><tr><td role="">004E</td><td role="">78</td><td role="">Start GlyphID for numeral zero glyph</td></tr><tr><td role="">0058</td><td role="">87</td><td role="">End GlyphID for numeral nine glyph</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageIndex first CoverageIndex =
                  0</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053335488"></a>Example 3: SingleSubstFormat2 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.26.1"></a>Specification</h3></div></div></div><p role="">Example 3 uses the SingleSubstFormat2 subtable for lists
          to substitute punctuation glyphs in Japanese text that is
          written vertically. Horizontally oriented parentheses and
          square brackets (the input glyphs) are replaced with
          vertically oriented parentheses and square brackets (the
          output glyphs).</p><p role="">The Coverage table, Format 1, identifies each input
          glyph index. The number of input glyph indices listed in the
          Coverage table matches the number of output glyph indices
          listed in the subtable. For correct substitution, the order
          of the glyph indices in the Coverage table (input glyphs)
          must match the order in the Substitute array (output
          glyphs).</p><div class="table"><a name="idm383053332112"></a><p class="title"><strong>Table 25.31. Example 3</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">SingleSubstFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">VerticalPunctuationSubtable</td><td role="">SingleSubst
                  subtable definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SubstFormat lists</td></tr><tr><td role="">000E</td><td role="">VerticalPunctuationCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">GlyphCount, equals GlyphCount in Coverage
                  table</td></tr><tr><td role="">0131</td><td role="">VerticalOpenBracketGlyph</td><td role="">Substitute[0], ordered by Coverage
                  Index</td></tr><tr><td role="">0135</td><td role="">VerticalClosedBracketGlyph</td><td role="">Substitute[1]</td></tr><tr><td role="">013E</td><td role="">VerticalOpenParenthesisGlyph</td><td role="">Substitute[2]</td></tr><tr><td role="">0143</td><td role="">VerticalClosedParenthesisGlyph</td><td role="">Substitute[3</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">VerticalPunctuationCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat lists</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">GlyphCount</td></tr><tr><td role="">003C</td><td role="">HorizontalOpenBracketGlyph</td><td role="">GlyphArray[0], ordered by GlyphID</td></tr><tr><td role="">0040</td><td role="">HorizontalClosedBracketGlyph</td><td role="">GlyphArray[1]</td></tr><tr><td role="">004B</td><td role="">HorizontalOpenParenthesisGlyph</td><td role="">GlyphArray[2]</td></tr><tr><td role="">004F</td><td role="">HorizontalClosedParenthesisGlyph</td><td role="">GlyphArray[3]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053304928"></a>Example 4: MultipleSubstFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.27.1"></a>Specification</h3></div></div></div><p role="">Example 4 uses a MultipleSubstFormat1 subtable to
          replace a single "ffi" ligature with three individual glyphs
          that form the string &lt;ffi&gt;. The subtable defines a format
          identifier of 1, an offset to a Coverage table that
          specifies the glyph index of the "ffi" ligature (the input
          glyph), an offset to a Sequence table that specifies the
          sequence of glyph indices for the &lt;ffi&gt; string in its
          substitute array (the output glyph sequence), and a count of
          Sequence table offsets.</p><div class="table"><a name="idm383053302704"></a><p class="title"><strong>Table 25.32. Example 4</strong></p><div class="table-contents"><table role="" class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MultipleSubstFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FfiDecompSubtable</td><td role="">MultipleSubst subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat</td></tr><tr><td role="">0008</td><td role="">FfiDecompCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceCount, equals GlyphCount in Coverage
                  table</td></tr><tr><td role="">000E</td><td role="">FfiDecompSequence</td><td role="">offset to Sequence[0] tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FfiDecompCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat lists</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">00F1</td><td role="">ffiGlyphID</td><td role="">ligature glyp</td></tr><tr><td role=""> </td><td role="">Sequence</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FfiDecompSequence</td><td role="">Sequence table
                  definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount</td></tr><tr><td role="">001A</td><td role="">fGlyphID</td><td role="">first glyph in sequence order</td></tr><tr><td role="">001A</td><td role="">fGlyphID</td><td role="">second glyph</td></tr><tr><td role="">001D</td><td role="">iGlyphID</td><td role="">third glyph</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053276112"></a>Example 5: AlternateSubstFormat 1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.28.1"></a>Specification</h3></div></div></div><p role="">Example 5 uses the AlternateSubstFormat1 subtable to
          replace the default ampersand glyph (input glyph) with one
          of two alternative ampersand glyphs (output glyph).</p><p role="">In this case, the Coverage table specifies the index of
          a single glyph, the default ampersand, because it is the
          only glyph covered by this lookup. The AlternateSet table
          for this covered glyph identifies the alternative glyphs:
          AltAmpersand1GlyphID and AltAmpersand2GlyphID.</p><p role="">In Example 5, the index position of the AlternateSet
          table offset in the AlternateSet array is zero (0), which
          correlates with the index position (also zero) of the
          default ampersand glyph in the Coverage table.</p><div class="table"><a name="idm383053272352"></a><p class="title"><strong>Table 25.33. Example 5</strong></p><div class="table-contents"><table role="" class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">AlternateSubstFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AltAmpersandSubtable</td><td role="">AlternateSubstFormat1
                  subtable definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat</td></tr><tr><td role="">0008</td><td role="">AltAmpersandCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">AlternateSetCnt, equals GlyphCount in Coverage
                  table</td></tr><tr><td role="">000E</td><td role="">AltAmpersandSet</td><td role="">offset to AlternateSet[0] tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AltAmpersandCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">GlyphCount</td></tr><tr><td role="">003A</td><td role="">DefaultAmpersandGlyphID</td><td role="">GlyphArray[0</td></tr><tr><td role=""> </td><td role="">AlternateSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AltAmpersandSet</td><td role="">AlternateSet table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">00C9</td><td role="">AltAmpersand1GlyphID</td><td role="">offset to Alternate[0], in arbitrary
                  order</td></tr><tr><td role="">00CA</td><td role="">AltAmpersand2GlyphID</td><td role="">offset to Alternate[1]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053247168"></a>Example 6: LigatureSubstFormat1 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.29.1"></a>Specification</h3></div></div></div><p role="">Example 6 shows a LigatureSubstFormat1 subtable that
          defines data to replace a string of glyphs with a single
          ligature glyph. Because a LigatureSubstFormat1 subtable can
          specify glyph substitutions for more than one ligature, this
          subtable defines three ligatures: "etc," "ffi," and "fi."
        </p><p role="">The sample subtable contains a format identifier (4) and
          an offset to a Coverage table. The Coverage table, which
          lists an index for each first glyph in the ligatures, lists
          indices for the "e" and "f" glyphs. The Coverage table range
          format is used here because the "e" and "f" glyph indices
          are numbered consecutively.</p><p role="">In the LigatureSubst subtable, LigSetCount specifies two
          LigatureSet tables, one for each covered glyph, and the
          LigatureSet array stores offsets to them. In this array, the
          "e" LigatureSet precedes the "f" LigatureSet, matching the
          order of the corresponding first-glyph components in the
          Coverage table.</p><p role="">Each LigatureSet table identifies all ligatures that
          begin with a covered glyph. The sample LigatureSet table
          defined for the "e" glyph contains only one ligature, "etc."
          A LigatureSet table defined for the "f" glyph contains two
          ligatures, "ffi" and "fi."</p><p role="">The sample FLigaturesSet table has offsets to two
          Ligature tables, one for "ffi" and one for "fi." The
          Ligature array lists the "ffi" Ligature table first to
          indicate that the "ffi" ligature is preferred to the "fi"
          ligature.</p><div class="table"><a name="idm383053241728"></a><p class="title"><strong>Table 25.34. Example 6</strong></p><div class="table-contents"><table role="" class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">LigatureSubstFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigaturesSubtable</td><td role="">LigatureSubstFormat1 subtable
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat</td></tr><tr><td role="">000A</td><td role="">LigaturesCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LigSetCount</td></tr><tr><td role="">0014</td><td role="">ELigaturesSet</td><td role="">offset to LigatureSet[0] table in Coverage
                  Index order</td></tr><tr><td role="">0020</td><td role="">FLigaturesSet</td><td role="">offset to LigatureSet[1] tabl</td></tr><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LigaturesCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat, ranges</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">RangeCount RangeRecord[0]</td></tr><tr><td role="">0019</td><td role="">eGlyphID</td><td role="">Start, first GlyphID</td></tr><tr><td role="">001A</td><td role="">fGlyphID</td><td role="">End, last GlyphID in range</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageIndex, coverage index of start
                  glyphI</td></tr><tr><td role=""> </td><td role="">LigatureSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">ELigaturesSet</td><td role="">LigatureSet table definition all
                  ligatures that start with e</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LigatureCount</td></tr><tr><td role="">0004</td><td role="">etcLigature</td><td role="">offset to Ligature[0] tabl</td></tr><tr><td role=""> </td><td role="">Ligature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">etcLigature</td><td role="">Ligature table definition</td></tr><tr><td role="">015B</td><td role="">etcGlyphID</td><td role="">LigGlyph, output GlyphID</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">CompCount number of components</td></tr><tr><td role="">0028</td><td role="">tGlyphID</td><td role="">Component[1], second component in
                  ligature</td></tr><tr><td role="">0017</td><td role="">cGlyphID</td><td role="">Component[2], third component in
                  ligatur</td></tr><tr><td role=""> </td><td role="">LigatureSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FLigaturesSet</td><td role="">LigatureSet table definition all
                  ligatures start with f</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LigatureCount</td></tr><tr><td role="">0006</td><td role="">ffiLigature</td><td role="">offset to Ligature[0] table, listed first
                  because ffi ligature is preferred to fi
                  ligature</td></tr><tr><td role="">000E</td><td role="">fiLigature</td><td role="">offset to Ligature[1] tabl</td></tr><tr><td role=""> </td><td role="">Ligature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">ffiLigature</td><td role="">Ligature table definitio</td></tr><tr><td role="">00F1</td><td role="">ffiGlyphID</td><td role="">LigGlyph, output GlyphID</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">CompCount</td></tr><tr><td role="">001A</td><td role="">fGlyphID</td><td role="">Component[1], second component in
                  ligature</td></tr><tr><td role="">001D</td><td role="">iGlyphID</td><td role="">Component[2], third component in
                  ligatur</td></tr><tr><td role=""> </td><td role="">Ligature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">fiLigature</td><td role="">Ligature table definition</td></tr><tr><td role="">00F0</td><td role="">fiGlyphID</td><td role="">LigGlyph, output GlyphID</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CompCount</td></tr><tr><td role="">001D</td><td role="">iGlyphID</td><td role="">Component[1] second component in
                  ligature</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053182800"></a>Example 7: ContextSubstFormat1 Subtable and
        SubstLookupRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.30.1"></a>Specification</h3></div></div></div><p role="">Example 7 uses a ContextSubstFormat1 subtable for glyph
          sequences to replace a string of three glyphs with another
          string. For the French language system, the subtable defines
          a contextual substitution that replaces the input sequence,
          space-dash-space, with the output sequence, thin
          space-dash-thin space.</p><p role="">The contextual substitution, called Dash Lookup in this
          example, contains one ContextSubstFormat1 subtable called
          the DashSubtable. The subtable specifies two contexts: a
          SpaceGlyph followed by a DashGlyph, and a DashGlyph followed
          by a SpaceGlyph. In each sequence, a single substitution
          replaces the SpaceGlyph with a ThinSpaceGlyph.</p><p role="">The Coverage table, labeled DashCoverage, lists two
          GlyphIDs for the first glyphs in the SpaceGlyph and
          DashGlyph sequences. One SubRuleSet table is defined for
          each covered glyph.</p><p role="">SpaceAndDashSubRuleSet lists all the contexts that begin
          with a SpaceGlyph. It contains an offset to one SubRule
          table (SpaceAndDashSubRule), which specifies two glyphs in
          the context sequence, the second of which is a DashGlyph.
          The SubRule table contains an offset to a SubstLookupRecord
          that lists the position in the sequence where the glyph
          substitution should occur (position 0) and the index of the
          SpaceToThinSpaceLookup applied there to replace the
          SpaceGlyph with a ThinSpaceGlyph. DashAndSpaceSubRuleSet
          lists all the contexts that begin with a DashGlyph. An
          offset to a SubRule table (DashAndSpaceSubRule) specifies
          two glyphs in the context sequence, and the second one is a
          SpaceGlyph. The SubRule table contains an offset to a
          SubstLookupRecord, which lists the position in the sequence
          where the glyph substitution should occur, and an index to
          the same lookup used in the SpaceAndDashSubRule. The lookup
          replaces the SpaceGlyph with a ThinSpaceGlyph.</p><div class="table"><a name="idm383053178400"></a><p class="title"><strong>Table 25.35. Example 7</strong></p><div class="table-contents"><table role="" class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextSubstFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashSubtable</td><td role="">ContextSubstFormat1 subtable
                  definition for Lookup[0], DashLookup</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat</td></tr><tr><td role="">000A</td><td role="">DashCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SubRuleSetCount</td></tr><tr><td role="">0012</td><td role="">SpaceAndDashSubRuleSet</td><td role="">offset to SubRuleSet[0], ordered by Coverage
                  Index</td></tr><tr><td role="">0020</td><td role="">DashAndSpaceSubRuleSet</td><td role="">offset to SubRuleSet[1</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat lists</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0028</td><td role="">SpaceGlyph</td><td role="">GlyphArray[0], in numeric order</td></tr><tr><td role="">005D</td><td role="">DashGlyph</td><td role="">GlyphArray[1], dash GlyphI</td></tr><tr><td role=""> </td><td role="">SubRuleSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SpaceAndDashSubRuleSet</td><td role="">SubRuleSet[0] table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubRuleCount</td></tr><tr><td role="">0004</td><td role="">SpaceAndDashSubRule</td><td role="">offset to SubRule[0], ordered by
                  preferenc</td></tr><tr><td role=""> </td><td role="">SubRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SpaceAndDashSubRule</td><td role="">SubRule[0] table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount number in input sequence</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstCount</td></tr><tr><td role="">005D</td><td role="">DashGlyph</td><td role="">Input[1], starting with second glyph SpaceGlyph
                  in Coverage table is first glyph
                  SubstLookupRecord[0]</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">SequenceIndex substitution at first glyph
                  position (0)</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex index for
                  SpaceToThinSpaceLookup in LookupLis</td></tr><tr><td role=""> </td><td role="">SubRuleSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashAndSpaceSubRuleSet</td><td role="">SubRuleSet[0] table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubRuleCount</td></tr><tr><td role="">0004</td><td role="">DashAndSpaceSubRule</td><td role="">offset to SubRule[0], ordered by
                  preferenc</td></tr><tr><td role=""> </td><td role="">SubRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DashAndSpaceSubRule</td><td role="">SubRule[0] table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount number in the input glyph
                  sequence</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstCount</td></tr><tr><td role="">0028</td><td role="">SpaceGlyph</td><td role="">Input[1], starting with second glyph
                  SubstLookupRecord definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceIndex substitution at second glyph
                  position(1)</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex for
                  SpaceToThinSpaceLookup</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053126208"></a>Example 8: ContextSubstFormat2 Subtable </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.31.1"></a>Specification</h3></div></div></div><p role="">Example 8 uses a ContextSubstFormat2 subtable with glyph
          classes to replace default mark glyphs with their
          alternative forms. Glyph alternatives are selected depending
          upon the height of the base glyph that they combine
          with-that is, the mark glyph used above a high base glyph
          differs from the mark glyph above a very high base
          glyph.</p><p role="">In the example, SetMarksHighSubtable contains a Class
          table that defines four glyph classes: medium-height glyphs
          (Class 0), all default mark glyphs (Class 1), high glyphs
          (Class 2), and very high glyphs (Class 3). The subtable also
          contains a Coverage table that lists each base glyph that
          functions as a first component in a context, ordered by
          glyph index.</p><p role="">Two SubClassSets are defined, one for substituting high
          marks and one for very high marks. No SubClassSets are
          specified for Class 0 and Class 1 glyphs because no contexts
          begin with glyphs from these classes. The SubClassSet array
          lists SubClassSets in numerical order, so SubClassSet 2
          precedes SubClassSet 3.</p><p role="">Within each SubClassSet, a SubClassRule is defined. In
          SetMarksHighSubClassSet2, the SubClassRule table specifies
          two glyphs in the context, the first glyph in Class 2 (a
          high glyph) and the second in Class 1 (a mark glyph). The
          SubstLookupRecord specifies applying
          SubstituteHighMarkLookup at the second position in the
          sequence-that is, a high mark glyph will replace the default
          mark glyph.</p><p role="">In SetMarksVeryHighSubClassSet3, the SubClassRule
          specifies two glyphs in the context, the first in Class 3 (a
          very high glyph) and the second in Class 1 (a mark glyph).
          The SubstLookupRecord specifies applying
          SubstituteVeryHighMarkLookup at the second position in the
          sequence-that is, a very high mark glyph will replace the
          default mark glyph.</p><div class="table"><a name="idm383053120368"></a><p class="title"><strong>Table 25.36. Example 8</strong></p><div class="table-contents"><table role="" class="table" summary="Example 8" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextSubstFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksHighSubtable</td><td role="">ContextSubstFormat2
                  subtable definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SubstFormat</td></tr><tr><td role="">0010</td><td role="">SetMarksHighCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">001C</td><td role="">SetMarksHighClassDef</td><td role="">offset to Class Def table</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">SubClassSetCnt</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to SubClassSet[0] table, no contexts
                  that begin with Class 0 glyphs are defined</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to SubClassSet[1] table no contexts that
                  begin with Class 1 glyphs are defined</td></tr><tr><td role="">0032</td><td role="">SetMarksHighSubClassSet2</td><td role="">offset to SubClassSet[2] table for contexts
                  that begin with Class 2 glyphs (high base
                  glyphs)</td></tr><tr><td role="">0040</td><td role="">SetMarksVeryHighSubClassSet3</td><td role="">offset to SubClassSet[3] table for contexts
                  that begin with Class 3 glyphs (very high base
                  glyphs</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksHighCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">GlyphCount</td></tr><tr><td role="">0030</td><td role="">tahGlyphID</td><td role="">GlyphArray[0], high base glyph</td></tr><tr><td role="">0031</td><td role="">dhahGlyphID</td><td role="">GlyphArray[1], high base glyph</td></tr><tr><td role="">0040</td><td role="">cafGlyphID</td><td role="">GlyphArray[2], very high base glyph</td></tr><tr><td role="">0041</td><td role="">gafGlyphID</td><td role="">GlyphArray[3], very high base glyp</td></tr><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksHighClassDef</td><td role="">Class table
                  definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class Format, ranges</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ClassRangeCount ClassRange[0] ordered by
                  StartGlyphID for Class 2, high base glyphs</td></tr><tr><td role="">0030</td><td role="">tahGlyphID</td><td role="">Start, first Glyph ID in range</td></tr><tr><td role="">0031</td><td role="">dhahGlyphID</td><td role="">End, last Glyph ID in range</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class ClassRange[1] for Class 3, very high base
                  glyphs</td></tr><tr><td role="">0040</td><td role="">cafGlyphID</td><td role="">Start, first Glyph ID in the range</td></tr><tr><td role="">0041</td><td role="">gafGlyphID</td><td role="">End, last Glyph ID in the range</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class ClassRange[2] for Class 1, mark
                  gyphs</td></tr><tr><td role="">00D2</td><td role="">fathatanDefaultGlyphID</td><td role="">Start, first Glyph ID in range default fathatan
                  mark</td></tr><tr><td role="">00D3</td><td role="">dammatanDefaultGlyphID</td><td role="">End, last Glyph ID in the range default
                  dammatan mark</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Clas</td></tr><tr><td role=""> </td><td role="">SubClassSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksHighSubClassSet2</td><td role="">SubClassSet[2] table
                  definition all contexts that begin with Class 2
                  glyphs</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubClassRuleCnt</td></tr><tr><td role="">0004</td><td role="">SetMarksHighSubClassRule2</td><td role="">offset to SubClassRule[0] table ordered by
                  preferenc</td></tr><tr><td role=""> </td><td role="">SubClassRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksHighSubClassRule2</td><td role="">SubClassRule[0] table
                  definition, Class 2 glyph (high base) glyph followed
                  by a Class 1 glyph (mark)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">offset to Class[1], beginning with the second
                  Class in the context sequence (mark = Class 1) begin
                  SubstLookupRecord array in design order
                  SubstLookupRecord[0]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceIndex, apply substitution to position
                  2, a mark</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex</td></tr><tr><td role=""> </td><td role="">SubClassSet</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksVeryHighSubClassSet3</td><td role="">SubClassSet[3]
                  table definition all contexts that begin with Class
                  3 glyphs</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubClassRuleCnt</td></tr><tr><td role="">0004</td><td role="">SetMarksVeryHighSubClassRule3</td><td role="">offset to SubClassRule[0] table ordered by
                  preferenc</td></tr><tr><td role=""> </td><td role="">SubClassRule</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SetMarksVeryHighSubClassRule3</td><td role="">SubClassRule[0]
                  table definition Class 3 glyph (very high base
                  glyph) followed by a Class 1 glyph (mark)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">GlyphCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstCount</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">offset to Class[1], beginning with the second
                  Class in the context sequence = marks, Class 1 begin
                  SubstLookupRecord array in design order
                  SubstLookupRecord[0]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SequenceIndex, apply substitution to position
                  2, second glyph class (mark)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LookupListIndex</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383053041152"></a>Example 9: ContextualSubstFormat3 Subtable</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.32.1"></a>Specification</h3></div></div></div><p role="">Example 9 uses the ContextSubstFormat3 subtable with
          Coverage tables to describe a context sequence of three
          lowercase glyphs in the pattern: any ascender or descender
          glyph in position 0 (zero), any x-height glyph in position
          1, and any descender glyph in position 2. The overlapping
          sets of covered glyphs for positions 0 and 2 make Format 3
          better for this context than the class-based Format
          2.</p><p role="">In positions 0 and 2, swash versions of the glyphs
          replace the default glyphs. The contextual-substitution
          lookup is SwashLookup (LookupList index = 0), and its
          subtable is SwashSubtable. The SwashSubtable defines three
          Coverage tables: AscenderDescenderCoverage, XheightCoverage,
          and DescenderCoverage-one for each glyph position in the
          context sequence, respectively.</p><p role="">The SwashSubtable also defines two SubstLookupRecords:
          one that applies to position 0, and one for position 2. (No
          substitutions are applied to position 1.) The record for
          position 0 uses a single substitution lookup called
          AscDescSwashLookup to replace the current ascender or
          descender glyph with a swash ascender or descender glyph.
          The record for position 2 uses a single substitution lookup
          called DescSwashLookup to replace the current descender
          glyph with a swash descender glyph.</p><div class="table"><a name="idm383053036672"></a><p class="title"><strong>Table 25.37. Example 9</strong></p><div class="table-contents"><table role="" class="table" summary="Example 9" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ContextSubstFormat3</td><td role=""> </td></tr><tr><td role=""> </td><td role="">SwashSubtable</td><td role="">ContextSubstFormat3 subtable
                  definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">SubstFormat</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">GlyphCount in input glyph sequence</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SubstCount</td></tr><tr><td role="">0030</td><td role="">AscenderDescenderCoverage</td><td role="">offset to Coverage[0] table in context sequence
                  order</td></tr><tr><td role="">004C</td><td role="">XheightCoverage</td><td role="">offset to Coverage[1] table</td></tr><tr><td role="">006E</td><td role="">DescenderCoverage</td><td role="">offset to Coverage[2] table
                  SubstLookupRecord[0] in glyph position order</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">SequenceIndex</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex, single substitution to output
                  ascender or descender swash
                  SubstLookupRecord[1]</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">SequenceIndex</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LookupListIndex single substitution to output
                  descender swas</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">AscenderDescenderCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">GlyphCount</td></tr><tr><td role="">0033</td><td role="">bGlyphID</td><td role="">GlyphArray[0] in GlyphID order</td></tr><tr><td role="">0035</td><td role="">dGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0037</td><td role="">fGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">0038</td><td role="">gGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">0039</td><td role="">hGlyphID</td><td role="">GlyphArray[4]</td></tr><tr><td role="">003B</td><td role="">jGlyphID</td><td role="">GlyphArray[5]</td></tr><tr><td role="">003C</td><td role="">kGlyphID</td><td role="">GlyphArray[6]</td></tr><tr><td role="">003D</td><td role="">lGlyphID</td><td role="">GlyphArray[7]</td></tr><tr><td role="">0041</td><td role="">pGlyphID</td><td role="">GlyphArray[8]</td></tr><tr><td role="">0042</td><td role="">qGlyphID</td><td role="">GlyphArray[9]</td></tr><tr><td role="">0045</td><td role="">tGlyphID</td><td role="">GlyphArray[10]</td></tr><tr><td role="">004A</td><td role="">yGlyphID</td><td role="">GlyphArray[11</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">XheightCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">000F</td><td role="">15</td><td role="">GlyphCount</td></tr><tr><td role="">0032</td><td role="">aGlyphID</td><td role="">GlyphArray[0] in GlyphID order</td></tr><tr><td role="">0034</td><td role="">cGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0036</td><td role="">eGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">003A</td><td role="">iGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">003E</td><td role="">mGlyphID</td><td role="">GlyphArray[4]</td></tr><tr><td role="">003F</td><td role="">nGlyphID</td><td role="">GlyphArray[5]</td></tr><tr><td role="">0040</td><td role="">oGlyphID</td><td role="">GlyphArray[6]</td></tr><tr><td role="">0043</td><td role="">rGlyphID</td><td role="">GlyphArray[7]</td></tr><tr><td role="">0044</td><td role="">sGlyphID</td><td role="">GlyphArray[8]</td></tr><tr><td role="">0045</td><td role="">tGlyphID</td><td role="">GlyphArray[9]</td></tr><tr><td role="">0046</td><td role="">uGlyphID</td><td role="">GlyphArray[10]</td></tr><tr><td role="">0047</td><td role="">vGlyphID</td><td role="">GlyphArray[11]</td></tr><tr><td role="">0048</td><td role="">wGlyphID</td><td role="">GlyphArray[12]</td></tr><tr><td role="">0049</td><td role="">xGlyphID</td><td role="">GlyphArray[13]</td></tr><tr><td role="">004B</td><td role="">zGlyphID</td><td role="">GlyphArray[14</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DescenderCoverage</td><td role="">Coverage table
                  definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">0005</td><td role="">5</td><td role="">GlyphCount</td></tr><tr><td role="">0038</td><td role="">gGlyphID</td><td role="">GlyphArray[0] in GlyphID order</td></tr><tr><td role="">003B</td><td role="">jGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0041</td><td role="">pGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">0042</td><td role="">qGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">004A</td><td role="">yGlyphID</td><td role="">GlyphArray[4]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm383052953488"></a>Example 10: ReverseChainSingleSubstFormat1 Subtable
	and SubstLookupRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.25.33.1"></a>Specification</h3></div></div></div><p role="">Example 10 uses a ReverseChainSingleSubstFormat1
	  subtable for glyph sequences to glyph with the correct form
	  that has a thick connection to the left (thick exit). This
	  allow the glyph to correctly connect to the letter form to
	  the left of it.</p><p role="">The ThickExitCoverage table is the listing of glyphs to
	  be matched for substitution.</p><p role="">The LookaheadCoverage table, labeled ThickEntryCoverage,
	  lists four GlyphIDs for the glyph following a substitution
	  coverage glyph. This lookahead coverage attempts to match
	  the context that will cause the substitution to take
	  place.</p><p role="">The Substitute table maps the glyphs to replace those in
	  the ThickConnectCoverage table.</p><div class="table"><a name="idm383052949376"></a><p class="title"><strong>Table 25.38. Example 10</strong></p><div class="table-contents"><table role="" class="table" summary="Example 10" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ReverseChainSingleSubstFormat1</td><td role=""> </td></tr><tr><td role="">ThickConnect</td><td role="">ReverseChainSingleSubstFormat1</td><td role="">subtable definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubstFormat</td></tr><tr><td role="">0068</td><td role="">ThickExitCoverage</td><td role="">offset to Coverage table</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">BacktrackGlyphCount</td></tr><tr><td role="">0000</td><td role="">null</td><td role="">not used offset to BacktrackCoverage[0]</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookaheadGlyphCount</td></tr><tr><td role="">0026</td><td role="">ThickEntryCoverage</td><td role="">offset to LookaheadCoverage[0]</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">GlyphCount</td></tr><tr><td role="">00A7</td><td role="">BEm2</td><td role="">Substitute[0], ordered by Coverage Index</td></tr><tr><td role="">00B9</td><td role="">BEi3</td><td role="">Substitute[1]</td></tr><tr><td role="">00C5</td><td role="">JIMm3</td><td role="">Substitute[2]</td></tr><tr><td role="">00D4</td><td role="">JIMi2</td><td role="">Substitute[3]</td></tr><tr><td role="">00EA</td><td role="">SINm2</td><td role="">Substitute[4]</td></tr><tr><td role="">00F2</td><td role="">SINi2</td><td role="">Substitute[5]</td></tr><tr><td role="">00FD</td><td role="">SADm2</td><td role="">Substitute[6]</td></tr><tr><td role="">010D</td><td role="">SADi2</td><td role="">Substitute[7]</td></tr><tr><td role="">011B</td><td role="">TOEm3</td><td role="">Substitute[8]</td></tr><tr><td role="">012B</td><td role="">TOEi3</td><td role="">Substitute[9]</td></tr><tr><td role="">013B</td><td role="">AINm2</td><td role="">Substitute[10]</td></tr><tr><td role="">0141</td><td role="">AINi2</td><td role="">Substitute[11]</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role="">ThickEntryCoverage</td><td role="">Coverage</td><td role="">table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">001F</td><td role="">31</td><td role="">GlyphCount</td></tr><tr><td role="">00A5</td><td role="">ALEFf1</td><td role="">GlyphArray[0], in GlyphID order</td></tr><tr><td role="">00A9</td><td role="">BEm4</td><td role="">GlyphArray[1]</td></tr><tr><td role="">00AA</td><td role="">BEm5</td><td role="">GlyphArray[2]</td></tr><tr><td role="">00E2</td><td role="">DALf1</td><td role="">GlyphArray[3]</td></tr><tr><td role="">0167</td><td role="">KAFf1</td><td role="">GlyphArray[4]</td></tr><tr><td role="">0168</td><td role="">KAFfs1</td><td role="">GlyphArray[5]</td></tr><tr><td role="">0169</td><td role="">KAFm1</td><td role="">GlyphArray[6]</td></tr><tr><td role="">016D</td><td role="">KAFm5</td><td role="">GlyphArray[7]</td></tr><tr><td role="">016E</td><td role="">KAFm6</td><td role="">GlyphArray[8]</td></tr><tr><td role="">0170</td><td role="">KAFm8</td><td role="">GlyphArray[9]</td></tr><tr><td role="">0183</td><td role="">GAFf1</td><td role="">GlyphArray[10]</td></tr><tr><td role="">0184</td><td role="">GAFfs1</td><td role="">GlyphArray[11]</td></tr><tr><td role="">0185</td><td role="">GAFm1</td><td role="">GlyphArray[12]</td></tr><tr><td role="">0189</td><td role="">GAFm5</td><td role="">GlyphArray[13]</td></tr><tr><td role="">018A</td><td role="">GAFm6</td><td role="">GlyphArray[14]</td></tr><tr><td role="">018C</td><td role="">GAFm8</td><td role="">GlyphArray[15]</td></tr><tr><td role="">019F</td><td role="">LAMf1</td><td role="">GlyphArray[16]</td></tr><tr><td role="">01A0</td><td role="">LAMm1</td><td role="">GlyphArray[17]</td></tr><tr><td role="">01A1</td><td role="">LAMm2</td><td role="">GlyphArray[18]</td></tr><tr><td role="">01A2</td><td role="">LAMm3</td><td role="">GlyphArray[19]</td></tr><tr><td role="">01A3</td><td role="">LAMm4</td><td role="">GlyphArray[20]</td></tr><tr><td role="">01A4</td><td role="">LAMm5</td><td role="">GlyphArray[21]</td></tr><tr><td role="">01A5</td><td role="">LAMm6</td><td role="">GlyphArray[22]</td></tr><tr><td role="">01A6</td><td role="">LAMm7</td><td role="">GlyphArray[23]</td></tr><tr><td role="">01A7</td><td role="">LAMm8</td><td role="">GlyphArray[24]</td></tr><tr><td role="">01A8</td><td role="">LAMm9</td><td role="">GlyphArray[25]</td></tr><tr><td role="">01A9</td><td role="">LAMm10</td><td role="">GlyphArray[26]</td></tr><tr><td role="">01AA</td><td role="">LAMm11</td><td role="">GlyphArray[27]</td></tr><tr><td role="">01AB</td><td role="">LAMm12</td><td role="">GlyphArray[28]</td></tr><tr><td role="">01AC</td><td role="">LAMm13</td><td role="">GlyphArray[29]</td></tr><tr><td role="">01EC</td><td role="">HAYf2</td><td role="">GlyphArray[30]</td></tr><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role="">ThickExitCoverage</td><td role="">Coverage</td><td role="">table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat, lists</td></tr><tr><td role="">000C</td><td role="">12</td><td role="">GlyphCount</td></tr><tr><td role="">00A6</td><td role="">BEm1</td><td role="">GlyphArray[0], ordered by GlyphID</td></tr><tr><td role="">00B7</td><td role="">BEi1</td><td role="">GlyphArray[1]</td></tr><tr><td role="">00C3</td><td role="">JIMm1</td><td role="">GlyphArray[2]</td></tr><tr><td role="">00D2</td><td role="">JIMi1</td><td role="">GlyphArray[3]</td></tr><tr><td role="">00E9</td><td role="">SINm1</td><td role="">GlyphArray[4]</td></tr><tr><td role="">00F1</td><td role="">SINi1</td><td role="">GlyphArray[5]</td></tr><tr><td role="">00FC</td><td role="">SADm1</td><td role="">GlyphArray[6]</td></tr><tr><td role="">010C</td><td role="">SADi1</td><td role="">GlyphArray[7]</td></tr><tr><td role="">0119</td><td role="">TOEm1</td><td role="">GlyphArray[8]</td></tr><tr><td role="">0129</td><td role="">TOEi1</td><td role="">GlyphArray[9]</td></tr><tr><td role="">013A</td><td role="">AINm1</td><td role="">GlyphArray[10]</td></tr><tr><td role="">0140</td><td role="">AINi1</td><td role="">GlyphArray[11]</td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>