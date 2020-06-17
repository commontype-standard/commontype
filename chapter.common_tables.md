<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.common_tables"></a>Chapter 21. OpenType Layout Common Table Formats</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132572000"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.1.1"></a>Specification</h3></div></div></div><p role="">OpenType Layout consists of five tables: the Glyph
          Substitution table (<a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>), the Glyph
          Positioning table (<a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>), the Baseline
          table (<a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>), the Justification table
          (<a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a>), and the Glyph Definition table
          (<a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>). These tables use some of the same
          data formats.</p><p role="">This chapter explains the conventions used in all
          OpenType Layout tables, and it describes the common table
          formats. Separate chapters provide complete details about
          the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>,
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>, <a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a>, and
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables.</p><p role="">The OpenType Layout tables provide typographic
          information for properly positioning and substituting
          glyphs, operations that are required for accurate typography
          in many language environments. OpenType Layout data is
          organized by script, language system, typographic feature,
          and lookup.</p><p role="">Scripts are defined at the top level. A script is a
          collection of glyphs used to represent one or more languages
          in written form (see Figure 2a). For instance, a single
          script-Latin-is used to write English, French, German, and
          many other languages. In contrast, three scripts-Hiragana,
          Katakana, and Kanji-are used to write Japanese. With
          OpenType Layout, multiple scripts may be supported by a
          single font.</p><div class="figure"><a name="idm320132560912"></a><p class="title"><strong>Figure 21.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
          scripts</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig2a.gif" alt="Figure 2a. Glyphs in the Latin, Kanji, and Arabic scripts"/></div></div></div><br class="figure-break"/><p role="">A language system may modify the functions or appearance
          of glyphs in a script to represent a particular
          language. For example, the eszet ligature is used in the
          German language system, but not in French or English (see
          Figure 2b). And the Arabic script contains different glyphs
          for writing the Farsi and Urdu languages. In OpenType
          Layout, language systems are defined within scripts.</p><div class="figure"><a name="idm320132557952"></a><p class="title"><strong>Figure 21.2. Figure 2b. Differences in the English, French, and
          German language systems</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig2b.gif" alt="Figure 2b. Differences in the English, French, and German language systems"/></div></div></div><br class="figure-break"/><p role="">A language system defines features, which are
          typographic rules for using glyphs to represent a
          language. Sample features are a "vert" feature that
          substitutes vertical glyphs in Japanese, a "liga" feature
          for using ligatures in place of separate glyphs, and a
          "mark" feature that positions diacritical marks with respect
          to base glyphs in Arabic (see Figure 2c). In the absence of
          language-specific rules, default language system features
          apply to the entire script. For instance, a default language
          system feature for the Arabic script substitutes initial,
          medial, and final glyph forms based on a glyph's position in
          a word.</p><div class="figure"><a name="idm320132554672"></a><p class="title"><strong>Figure 21.3. Figure 2c. A ligature glyph feature substitutes the
          &lt;etc&gt; ligature for individual glyphs, and a mark
          feature positions diacritical marks above an Arabic ligature
          glyph.</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig2c.gif" alt="Figure 2c. A ligature glyph feature substitutes the &lt;etc&gt; ligature for individual glyphs, and a mark feature positions diacritical marks above an Arabic ligature glyph."/></div></div></div><br class="figure-break"/><p role="">Features are implemented with lookup data that the
          text-processing client uses to substitute and position
          glyphs. Lookups describe the glyphs affected by an
          operation, the type of operation to be applied to these
          glyphs, and the resulting glyph output.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132550848"></a>Table Organization</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.2.1"></a>Specification</h3></div></div></div><p role="">Two OpenType Layout tables, <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, use the same data formats to
          describe the typographic functions of glyphs and the
          languages and scripts that they support: a ScriptList table,
          a FeatureList table, and a LookupList table. In
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, the tables define glyph
          substitution data. In <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, they define
          glyph positioning data. This chapter describes these common
          table formats.</p><p role="">The ScriptList identifies the scripts in a font, each of
          which is represented by a Script table that contains script
          and language-system data. Language system tables reference
          features, which are defined in the FeatureList. Each feature
          table references the lookup data defined in the LookupList
          that describes how, when, and where to implement the
          feature</p><div class="figure"><a name="idm320132544800"></a><p class="title"><strong>Figure 21.4. Figure 2d. The relationship of scripts, language
          systems, features, and lookups for substitution and
          positioning tables</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig2d.gif" alt="Figure 2d. The relationship of scripts, language systems, features, and lookups for substitution and positioning tables"/></div></div></div><br class="figure-break"/><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: The data in the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> and
            <a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a> tables also is organized by script
            and language system. However, the data formats differ from
            those in <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
            <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, and they do not include a
            FeatureList or LookupList. The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> and
            <a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a> data formats are described in the
            <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> and <a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a>
            chapters.</p></blockquote></div><p role="">The information used to substitute and position glyphs
          is defined in Lookup subtables. Each subtable supplies one
          type of information, depending upon whether the lookup is
          part of a <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          table. For instance, a <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> lookup might
          specify the glyphs to be substituted and the context in
          which a substitution occurs, and a <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          lookup might specify glyph position adjustments for kerning.
          OpenType Layout has seven types of <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          lookups (described in the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> chapter)
          and nine types of <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookups (described
          in the <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> chapter).</p><p role="">Each subtable (except for an Extension LookupType
          subtable) includes a Coverage table that lists the
          "covered" glyphs that will result in a glyph substitution or
          positioning operation. The Coverage table formats are
          described in this chapter.</p><p role="">Some substitution or positioning operations may apply to
          groups, or classes, of glyphs. <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> Lookup subtables use the Class
          Definition table to assign glyphs to classes. This chapter
          includes a description of the Class Definition table
          formats.</p><p role="">Lookup subtables also may contain device tables,
          described in this chapter, to adjust scaled contour glyph
          coordinates for particular output sizes and
          resolutions. This chapter also describes the data types used
          in OpenType Layout. Sample tables and lists that illustrate
          the common data formats are supplied at the end of this
          chapter.</p><p role="">Scripts and Languages</p><p role="">Three tables and their associated records apply to
          scripts and languages: the Script List table (ScriptList)
          and its script record (ScriptRecord), the Script table and
          its language system record (LangSysRecord), and the Language
          System table (LangSys).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132524960"></a>Script List Table and Script Record</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.3.1"></a>Specification</h3></div></div></div><p role="">OpenType Layout fonts may contain one or more groups of
          glyphs used to render various scripts, which are enumerated
          in a ScriptList table. Both the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables define Script List tables
          (ScriptList):</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table uses the
              ScriptList table to access the glyph substitution
              features that apply to a script. For details, see the
              chapter, The Glyph Substitution Table
              (<a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>).</p></li><li role="" class="listitem"><p role="">The <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses the
              ScriptList table to access the glyph positioning
              features that apply to a script. For details, see the
              chapter, The Glyph Positioning Table
              (<a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>).</p></li></ul></div><p role="">A ScriptList table consists of a count of the scripts
          represented by the glyphs in the font (ScriptCount) and an
          array of records (ScriptRecord), one for each script for
          which the font defines script-specific features (a script
          without script-specific features does not need a
          ScriptRecord).</p><p role="">If a Script table with the script tag 'DFLT' (default)
	  is present in the ScriptList table, it must have a non-NULL
	  DefaultLangSys and LangSysCount must be equal to 0. The 'DFLT'
	  Script table should be used if there is not an explicit entry
	  for the script being formatted.</p><p role="">The ScriptRecord array stores the records alphabetically
          by a ScriptTag that identifies the script. Each ScriptRecord
          consists of a ScriptTag and an offset to a Script
          table.</p><p role="">Example 1 at the end of this chapter shows a ScriptList
          table and ScriptRecords for a Japanese font that uses three
          scripts.</p><div class="table"><a name="idm320132513696"></a><p class="title"><strong>Table 21.1. ScriptList table</strong></p><div class="table-contents"><table role="" class="table" summary="ScriptList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ScriptCount</td><td role="">Number of ScriptRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">ScriptRecord [ScriptCount]</td><td role="">Array of ScriptRecords - listed
              alphabetically by ScriptTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320132508352"></a><p class="title"><strong>Table 21.2. ScriptRecord</strong></p><div class="table-contents"><table role="" class="table" summary="ScriptRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">ScriptTag</td><td role="">4-byte ScriptTag identifier</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Script</td><td role="">Offset to Script table-from beginning of
              ScriptList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132502496"></a>Script Table and Language System Record</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.4.1"></a>Specification</h3></div></div></div><p role="">A Script table identifies each language system that
          defines how to use the glyphs in a script for a particular
          language. It also references a default language system that
          defines how to use the script's glyphs in the absence of
          language-specific knowledge.</p><p role="">A Script table begins with an offset to the Default
          Language System table (DefaultLangSys), which defines the
          set of features that regulate the default behavior of the
          script. Next, Language System Count (LangSysCount) defines
          the number of language systems (excluding the
          DefaultLangSys) that use the script. In addition, an array
          of Language System Records (LangSysRecord) defines each
          language system (excluding the default) with an
          identification tag (LangSysTag) and an offset to a Language
          System table (LangSys). The LangSysRecord array stores the
          records alphabetically by LangSysTag.</p><p role="">If no language-specific script behavior is defined, the
          LangSysCount is set to zero (0), and no LangSysRecords are
          allocated.</p><div class="table"><a name="idm320132499024"></a><p class="title"><strong>Table 21.3. Script table</strong></p><div class="table-contents"><table role="" class="table" summary="Script table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">DefaultLangSys</td><td role="">Offset to DefaultLangSys table-from beginning
              of Script table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LangSysCount</td><td role="">Number of LangSysRecords for this
              script-excluding the DefaultLangSys</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">LangSysRecord [LangSysCount]</td><td role="">Array of LangSysRecords-listed alphabetically
              by LangSysTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320132492112"></a><p class="title"><strong>Table 21.4. LangSysRecord</strong></p><div class="table-contents"><table role="" class="table" summary="LangSysRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">LangSysTag</td><td role="">4-byte LangSysTag identifier</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">LangSys</td><td role="">Offset to LangSys table-from beginning of
              Script table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132486256"></a>Language System Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.5.1"></a>Specification</h3></div></div></div><p role="">The Language System table (LangSys) identifies
          language-system features used to render the glyphs in a
          script. (The LookupOrder offset is reserved for future
          use.)</p><p role="">Optionally, a LangSys table may define a Required
          Feature Index (ReqFeatureIndex) to specify one feature as
          required within the context of a particular language
          system. For example, in the Cyrillic script, the Serbian
          language system always renders certain glyphs differently
          than the Russian language system.</p><p role="">Only one feature index value can be tagged as the
          ReqFeatureIndex. This is not a functional limitation,
          however, because the feature and lookup definitions in
          OpenType Layout are structured so that one feature table can
          reference many glyph substitution and positioning
          lookups. When no required features are defined, then the
          ReqFeatureIndex is set to 0xFFFF.</p><p role="">All other features are optional. For each optional
          feature, a zero-based index value references a record
          (FeatureRecord) in the FeatureRecord array, which is stored
          in a Feature List table (FeatureList). The feature indices
          themselves (excluding the ReqFeatureIndex) are stored in
          arbitrary order in the FeatureIndex array. The FeatureCount
          specifies the total number of features listed in the
          FeatureIndex array.</p><p role="">Features are specified in full in the FeatureList table,
          FeatureRecord, and Feature table, which are described later
          in this chapter. Example 2 at the end of this chapter shows
          a Script table, LangSysRecord, and LangSys table used for
          contextual positioning in the Arabic script.</p><div class="table"><a name="idm320132480688"></a><p class="title"><strong>Table 21.5. LangSys table</strong></p><div class="table-contents"><table role="" class="table" summary="LangSys table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">LookupOrder</td><td role="">= NULL (reserved for an offset to a
              reordering table)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ReqFeatureIndex</td><td role="">Index of a feature required for this language
              system- if no required features = 0xFFFF</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">FeatureCount</td><td role="">Number of FeatureIndex values for this
              language system-excludes the required
              feature</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">FeatureIndex [FeatureCount]</td><td role="">Array of indices into the FeatureList-in
              arbitrary order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132471632"></a>Features and Lookups</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.6.1"></a>Specification</h3></div></div></div><p role="">Features define the functionality of an OpenType Layout
          font and they are named to convey meaning to the
          text-processing client. Consider a feature named "liga" to
          create ligatures. Because of its name, the client knows what
          the feature does and can decide whether to apply it. For
          more information, see the <a role="" class="ulink" href="http://www.microsoft.com/typography/otspec/TTOREG.htm" target="_top">OpenType
            Layout Registered Features</a> chapter. Font
          developers can use these features, as well as create their
          own.</p><p role="">After choosing which features to use, the client
          assembles all lookups from the selected features. Multiple
          lookups may be needed to define the data required for
          different substitution and positioning actions, as well as
          to control the sequencing and effects of those
          actions.</p><p role="">To implement features, a client applies the lookups in
          the order the lookup definitions occur in the LookupList. As
          a result, within the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, lookups from several
          different features may be interleaved during text
          processing. A lookup is finished when the client locates a
          target glyph or glyph context and performs a substitution
          (if specified) or a positioning (if specified).</p><p role="">Note: The substitution (<a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>) lookups
          always occur before the positioning
          (<a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>) lookups. The lookup sequencing
          mechanism in TrueType relies on the font to determine the
          proper order of text-processing operations.</p><p role="">Lookup data is defined in one or more subtables that
          contain information about specific glyphs and the operations
          to be performe on them. Each type of lookup has one or more
          corresponding subtable definitions. The choice of a subtable
          format depends upon two factors: the precise content of the
          information being applied to an operation, and the required
          storage efficiency. (For complete definitions of all lookup
          types and subtables, see the the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> chapters of this document.)</p><p role="">OpenType Layout features define information that is
          specific to the layout of the glyphs in a font. They do not
          encode information that is constant within the conventions
          of a particular language or the typography of a particular
          script. Information that would be replicated across all
          fonts in a given language belongs in the text-processing
          application for that language, not in the fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132459792"></a>Feature List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.7.1"></a>Specification</h3></div></div></div><p role="">The headers of the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables contain offsets to Feature
          List tables (FeatureList) that enumerate all the features in
          a font. Features in a particular FeatureList are not limited
          to any single script. A FeatureList contains the entire list
          of either the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> features that are used to render the
          glyphs in all the scripts in the font.</p><p role="">The FeatureList table enumerates features in an array of
          records (FeatureRecord) and specifies the total number of
          features (FeatureCount). Every feature must have a
          FeatureRecord, which consists of a FeatureTag that
          identifies the feature and an offset to a Feature table
          (described next). The FeatureRecord array is arranged
          alphabetically by FeatureTag names.</p><p role="">Note: The values stored in the FeatureIndex array of a
          LangSys table are used to locate records in the
          FeatureRecord array of a FeatureList table.</p><div class="table"><a name="idm320132453200"></a><p class="title"><strong>Table 21.6. FeatureList table</strong></p><div class="table-contents"><table role="" class="table" summary="FeatureList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">FeatureCount</td><td role="">Number of FeatureRecords in this
              table</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">FeatureRecord [FeatureCount]</td><td role="">Array of FeatureRecords-zero-based (first
              feature has FeatureIndex = 0)-listed alphabetically by
              FeatureTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320132447760"></a><p class="title"><strong>Table 21.7. FeatureRecord</strong></p><div class="table-contents"><table role="" class="table" summary="FeatureRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">FeatureTag</td><td role="">4-byte feature identification
              tag</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Feature</td><td role="">Offset to Feature table-from beginning of
              FeatureList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320133033872"></a>Feature Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.8.1"></a>Specification</h3></div></div></div><p role="">A Feature table defines a feature with one or more
          lookups. The client uses the lookups to substitute or
          position glyphs.</p><p role="">Feature tables defined within the
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table contain references to glyph
          substitution lookups, and feature tables defined within the
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table contain references to glyph
          positioning lookups. If a text-processing operation requires
          both glyph substitution and positioning, then both the
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables
          must each define a Feature table, and the tables must use
          the same FeatureTags.</p><p role="">A Feature table consists of an offset to a Feature
          Parameters (FeatureParams) table (if one has been defined
          for this feature - see note in the following paragraph), a
          count of the lookups listed for the feature (LookupCount),
          and an arbitrarily ordered array of indices into a
          LookupList (LookupListIndex). The LookupList indices are
          references into an array of offsets to Lookup tables.</p><p role="">The format of the Feature Parameters table is specific
          to a particular feature, and must be specified in the
          feature's entry in the Feature Tags section of the OpenType
          Layout Tag Registry. The length of the Feature Parameters
          table must be implicitly or explicitly specified in the
          Feature Parameters table itself. The FeatureParams field in
          the Feature Table records the offset relative to the
          beginning of the Feature Table. If a Feature Parameters
          table is not needed, the FeatureParams field must be set to
          NULL.</p><p role="">To identify the features in a <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, a text-processing client
          reads the FeatureTag of each FeatureRecord referenced in a
          given LangSys table. Then the client selects the features it
          wants to implement and uses the LookupList to retrieve the
          Lookup indices of the chosen features. Next, the client
          arranges the indices in the LookupList order. Finally, the
          client applies the lookup data to substitute or position
          glyphs.</p><p role="">Example 3 at the end of this chapter shows the
          FeatureList and Feature tables used to substitute ligatures
          in two languages.</p><div class="table"><a name="idm320133023536"></a><p class="title"><strong>Table 21.8. Feature table</strong></p><div class="table-contents"><table role="" class="table" summary="Feature table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">FeatureParams</td><td role="">= NULL (reserved for offset to
              FeatureParams)</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookupCount</td><td role="">Number of LookupList indices for this
              feature</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookupListIndex [LookupCount]</td><td role="">Array of LookupList indices for this feature
              -zero-based (first lookup is LookupListIndex =
              0)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.8.2"></a>Annotation</h3></div></div></div><p role="">The description of the FeatureParams field used to be in
          v1.25: "Offset to Feature Parameters table (if one has been
          defined for the feature), relative to the beginning of the
          Feature Table; = NULL if not required". It is unclear why it
          has been changed and in fact the old version is better,
          since there are font with feature params.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320133014032"></a>Lookup List Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.9.1"></a>Specification</h3></div></div></div><p role="">The headers of the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables contain offsets to Lookup
          List tables (LookupList) for glyph substitution
          (<a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table) and glyph positioning
          (<a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table). The LookupList table
          contains an array of offsets to Lookup tables (Lookup). The
          font developer defines the Lookup sequence in the Lookup
          array to control the order in which a text-processing client
          applies lookup data to glyph substitution and positioning
          operations. LookupCount specifies the total number of Lookup
          table offsets in the array.</p><p role="">Example 4 at the end of this chapter shows three
          ligature lookups in the LookupList table.</p><div class="table"><a name="idm320133008144"></a><p class="title"><strong>Table 21.9. LookupList table</strong></p><div class="table-contents"><table role="" class="table" summary="LookupList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">LookupCount</td><td role="">Number of lookups in this table</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">Lookup [LookupCount]</td><td role="">Array of offsets to Lookup tables-from
              beginning of LookupList -zero based (first lookup is
              Lookup index = 0)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320133002176"></a>Lookup Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.10.1"></a>Specification</h3></div></div></div><p role="">A Lookup table (Lookup) defines the specific conditions,
          type, and results of a substitution or positioning action
          that is used to implement a feature. For example, a
          substitution operation requires a list of target glyph
          indices to be replaced, a list of replacement glyph indices,
          and a description of the type of substitution action.</p><p role="">Each Lookup table may contain only one type of
          information (LookupType), determined by whether the lookup
          is part of a <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          supports five LookupTypes, and <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          supports seven LookupTypes (for details about LookupTypes,
          see the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          chapters of the document).</p><p role="">Each LookupType is defined with one or more subtables,
          and each subtable definition provides a different
          representation format. The format is determined by the
          content of the information required for an operation and by
          required storage efficiency. When glyph information is best
          presented in more than one format, a single lookup may
          contain more than one subtable, as long as all the subtables
          are the same LookupType. For example, within a given lookup,
          a glyph index array format may best represent one set of
          target glyphs, whereas a glyph index range format may be
          better for another set of target glyphs.</p><p role="">During text processing, a client applies a lookup to
          each glyph in the string before moving to the next lookup. A
          lookup is finished for a glyph after the client makes the
          substitution/positioning operation. To move to the "next"
          glyph, the client will typically skip all the glyphs that
          participated in the lookup operation: glyphs that were
          substituted/positioned as well as any other glyphs that
          formed a context for the operation. However, in the case of
          pair positioning operations (i.e., kerning), the "next"
          glyph in a sequence may be the second glyph of the
          positioned pair (see pair positioning lookup for
          details).</p><p role="">A Lookup table contains a LookupType, specified as an
          integer, that defines the type of information stored in the
          lookup. The LookupFlag specifies lookup qualifiers that
          assist a text-processing client in substituting or
          positioning glyphs. The SubTableCount specifies the total
          number of SubTables. The SubTable array specifies offsets,
          measured from the beginning of the Lookup table, to each
          SubTable enumerated in the SubTable array.</p><div class="table"><a name="idm320132992560"></a><p class="title"><strong>Table 21.10. Lookup table</strong></p><div class="table-contents"><table role="" class="table" summary="Lookup table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">LookupType</td><td role="">Different enumerations for
              <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
              <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a></td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">LookupFlag</td><td role="">Lookup qualifiers</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">SubTableCount</td><td role="">Number of SubTables for this
              lookup</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">SubTable [SubTableCount]</td><td role="">Array of offsets to SubTables-from beginning
              of Lookup table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The LookupFlag uses four bits and one byte:

          </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Each of the first four bits can be set in order to
                specify additional instructions for applying a lookup
                to a glyph string. The LookUpFlag bit enumeration
                table provides details about the use of these bits.
              </p></li><li role="" class="listitem"><p role="">The high byte is set to specify the type of mark
                attachment.</p></li></ul></div><p role="">
        </p><div class="table"><a name="idm320135111072"></a><p class="title"><strong>Table 21.11. LookupFlag bit enumeration</strong></p><div class="table-contents"><table role="" class="table" summary="LookupFlag bit enumeration" border="1"><colgroup><col width="6pc"/><col width="10pc"/><col width="14pc"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0x0001</td><td role="">RightToLeft</td><td role="">
                  <p role="">This bit relates only to the correct
                    processing of the cursive attachment lookup type
                    (GPOS lookup type 3). When this bit is set, the
                    last glyph in a given sequence to which the
                    cursive attachment lookup is applied, will be
                    positioned on the baseline.</p>
                  <p role=""><span role="" class="emphasis"><em>Note: Setting of this bit is not
                      intended to be used by operating systems or
                      applications to determine text
                      direction.</em></span></p>
                </td></tr><tr><td role="">0x0002</td><td role="">IgnoreBaseGlyphs</td><td role="">If set, skips over base glyphs</td></tr><tr><td role="">0x0004</td><td role="">IgnoreLigatures</td><td role="">If set, skips over ligatures</td></tr><tr><td role="">0x0008</td><td role="">IgnoreMarks</td><td role="">If set, skips over combining marks</td></tr><tr><td role="">0x00F0</td><td role="">Reserved</td><td role="">For future use</td></tr><tr><td role="">0xFF00</td><td role="">MarkAttachmentType</td><td role="">If not zero, skips over all marks of attachment
                  type different from specified.</td></tr></tbody></table></div></div><br class="table-break"/><p role="">For example, in Arabic text, a character string might
          have the pattern &lt;base character - mark character - base
          character&gt;. That string could be converted into a ligature
          composed of two components, one for each base character,
          with the combining mark glyph over the first component. To
          produce this ligature, the font developer would set the
          IgnoreMarks bit to tell the client to ignore the mark,
          substitute the ligature glyph first, and then position the
          mark glyph over the ligature. Alternatively, a lookup which
          did not set the IgnoreMarks bit could be used to describe a
          three-component ligature glyph, composed of the first base
          glyph, the mark glyph, and the second base glyph. Here's
          another example: A lookup which creates a ligature of a base
          glyph with a top mark may skip over all bottom marks by
          specifying the mark attachment type as top marks. You can
          define attachment types of marks in the MarkAttachClassDef
          subtable in the <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.10.2"></a>Annotation</h3></div></div></div><p role="">Second paragraph, should read: "... GSUB supports seven
	LookupTypes and GPOS supports nine LookupTypes..."</p><p role="">In general, each lookup subtable can be described by:
	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">a pattern that the glyph string must match (at the
	      current position)</p></li><li role="" class="listitem"><p role="">transformations that must performed
	      on the glyph string, if the pattern is matched.</p></li></ul></div><p role="">It is useful to describe each lookup subtable in those
	terms, and to do so using a somewhat formalized notation. This
	goes a long way toward resolving the inherent ambiguity of the
	English language.</p><p role="">To describe patterns, we will use the usual regular
	expression notation: ‘*’ for 0 or more
	occurrences, ‘+’ for 1 or more occurrences. Each
	pattern consists of three parts, in that order: the backtrack
	part, the input part and the lookahead part. We indicate those
	parts by bracketing the input part with
	‘▶’ and ‘◀’.  The
	basic alphabet on which those regular expressions are built
	are sets of glyph IDs. The set L is the set of LookupFlag
	glyphs, that is the set of glyphs which need to be skipped
	according to LookupFlag. The other sets in the basic alphabet
	are introduced in the description of each lookup subtable
	format; all such sets are to be understood as excluding the
	glyphs in the set L. If a set is empty, then the pattern does
	not match any string.</p><p role="">For example, the pattern matched by a Ligature table in
	a Ligature Substitution in format 1 is:</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">▶ L<sub>0</sub> L*
	  L<sub>1</sub> L* … L*
	  L<sub>ComponentCount-1</sub> ◀</p></blockquote></div><p role="">where L<sub>0</sub> = {glyph ID to which
	this Ligature table corresponds} - L, and
	L<sub>i</sub> = {Component [i-1]} - L for i &gt;
	0.</p><p role="">The pattern matched by a Ligature Substitution is the
	union of the patterns matched by its subtables.</p><p role="">Last sentence: “You <span role="" class="emphasis"><em>can</em></span>
	define...” seems a bit weak, since there does not seem
	to be any other place where this data can be found. In other
	words: “The attachment type of the glyphs are found in
	the GDEF table.”</p><p role="">MarkAttachementType: A common use of this mechanism is
	when ligating a base character and a mark. The problem to
	solve handle is that there could be an intervening,
	non-interacting mark, as in the sequence &lt;base, mark_below,
	mark_above&gt;. (The canonical ordering of the combining classes
	in Unicode is irrelevant – just reverse the mark above
	and the mark below). We want to ligate the base and the mark
	above, so we have to skip the mark below. We cannot set
	ignoreMarks in lookupFlag, as to would force the mark above to
	be ignored as well! However, we cannot ignore base glyphs
	either; consider &lt;base, other_base, mark_above&gt;, in which
	case we do not want to ligate. So the seemingly trivial
	“skip over all <span role="" class="emphasis"><em>marks</em></span> of attachment
	type different from specified” is actually quite
	strong: only the <span role="" class="emphasis"><em>marks</em></span> of the appropriate
	attachment type have to be skipped. This means that the test
	to determine if a glyph should be skipped cannot look just at
	the mark attachment class definition, it must also look at the
	glyph class definition.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135080816"></a>Coverage Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.11.1"></a>Specification</h3></div></div></div><p role="">Each subtable (except an Extension LookupType subtable)
          in a lookup references a Coverage table (Coverage), which
          specifies all the glyphs affected by a substitution or
          positioning operation described in the subtable. The
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, and
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables rely on this notion of
          coverage. If a glyph does not appear in a Coverage table,
          the client can skip that subtable and move immediately to
          the next subtable.</p><p role="">A Coverage table identifies glyphs by glyph indices
          (GlyphIDs) either of two ways:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">As a list of individual glyph indices in the glyph
              set.</p></li><li role="" class="listitem"><p role="">As ranges of consecutive indices. The range format
              gives a number of start-glyph and end-glyph index pairs
              to denote the consecutive glyphs covered by the
              table.</p></li></ul></div><p role="">In a Coverage table, a format code (CoverageFormat)
          specifies the format as an integer: 1 = lists, and 2 =
          ranges.</p><p role="">A Coverage table defines a unique index value (Coverage
          Index) for each covered glyph. This unique value specifies
          the position of the covered glyph in the Coverage table. The
          client uses the Coverage Index to look up values in the
          subtable for each glyph.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.11.2"></a>Annotation</h3></div></div></div><p role="">The specification does not mention a fairly interesting
          property of the existing subtable formats: A coverage is
          really a subset of n glyphs of the font, and those glyphs
          are enumerated in glyph index order by the Coverage Index
          (i.e. CI(0) is the glyph with the smallest glyph id in that
          subset, CI(1) is the next, and so on to CI(n-1) which is the
          glyph with the largest glyph id).</p><p role="">It is possible that a new coverage be defined for which
          this property does not hold. However, this seems unlikely,
          and we will assume that the property will always
          hold. Recommendation: make that clear in the
          specification.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135068704"></a>Coverage Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.12.1"></a>Specification</h3></div></div></div><p role="">Coverage Format 1 consists of a format code
          (CoverageFormat) and a count of covered glyphs (GlyphCount),
          followed by an array of glyph indices (GlyphArray). The
          glyph indices must be in numerical order for binary
          searching of the list. When a glyph is found in the Coverage
          table, its position in the GlyphArray determines the
          Coverage Index that is returned-the first glyph has a
          Coverage Index = 0, and the last glyph has a Coverage Index
          = GlyphCount -1.</p><p role="">Example 5 at the end of this chapter shows a Coverage
          table that uses Format 1 to list the GlyphIDs of all
          lowercase descender glyphs in a font.</p><div class="table"><a name="idm320135065392"></a><p class="title"><strong>Table 21.12. CoverageFormat1 table: Individual glyph
          indices</strong></p><div class="table-contents"><table role="" class="table" summary="CoverageFormat1 table: Individual glyph&#10;          indices" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CoverageFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Number of glyphs in the
              GlyphArray</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">GlyphArray [GlyphCount]</td><td role="">Array of GlyphIDs-in numerical
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135057968"></a>Coverage Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.13.1"></a>Specification</h3></div></div></div><p role="">Format 2 consists of a format code (CoverageFormat) and
          a count of glyph index ranges (RangeCount), followed by an
          array of records (RangeRecords). Each RangeRecord consists
          of a start glyph index (Start), an end glyph index (End),
          and the Coverage Index associated with the range's Start
          glyph. Ranges must be in GlyphID order, and they must be
          distinct, with no overlapping.</p><p role="">The Coverage Indexes for the first range begin with zero
          (0), and the Start Coverage Indexes for each succeeding
          range are determined by adding the length of the preceding
          range (End GlyphID - Start GlyphID + 1) to the array Index.
          This allows for a quick calculation of the Coverage Index
          for any glyph in any range using the formula: Coverage Index
          (GlyphID) = StartCoverageIndex + GlyphID - Start
          GlyphID.</p><p role="">Example 6 at the end of this chapter shows a Coverage
          table that uses Format 2 to identify a range of numeral
          glyphs in a font.</p><div class="table"><a name="idm320135053904"></a><p class="title"><strong>Table 21.13. CoverageFormat2 table: Range of glyphs</strong></p><div class="table-contents"><table role="" class="table" summary="CoverageFormat2 table: Range of glyphs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">CoverageFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">RangeCount</td><td role="">Number of RangeRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">RangeRecord [RangeCount]</td><td role="">Array of glyph ranges-ordered by Start
              GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320135047088"></a><p class="title"><strong>Table 21.14. RangeRecord</strong></p><div class="table-contents"><table role="" class="table" summary="RangeRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">GlyphID</td><td role="">Start</td><td role="">First GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">End</td><td role="">Last GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">StartCoverageIndex</td><td role="">Coverage Index of first GlyphID in
              range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135039760"></a>Class Definition Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.14.1"></a>Specification</h3></div></div></div><p role="">In OpenType Layout, index values identify glyphs. For
          efficiency and ease of representation, a font developer can
          group glyph indices to form glyph classes. Class assignments
          vary in meaning from one lookup subtable to another. For
          example, in the <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables, classes are used to describe
          glyph contexts. <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables also use the
          idea of glyph classes.</p><p role="">Consider a substitution action that replaces only the
          lowercase ascender glyphs in a glyph string. To more easily
          describe the appropriate context for the substitution, the
          font developer might divide the font's lowercase glyphs into
          two classes, one that contains the ascenders and one that
          contains the glyphs without ascenders.</p><p role="">A font developer can assign any glyph to any class, each
          identified with an integer called a class value. A Class
          Definition table (ClassDef) groups glyph indices by class,
          beginning with Class 1, then Class 2, and so on. All glyphs
          not assigned to a class fall into Class 0. Within a given
          class definition table, each glyph in the font belongs to
          exactly one class.</p><p role="">The ClassDef table can have either of two formats: one
          that assigns a range of consecutive glyph indices to
          different classes, or one that puts groups of consecutive
          glyph indices into the same class.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135032400"></a>Class Definition Table Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.15.1"></a>Specification</h3></div></div></div><p role="">The first class definition format (ClassDefFormat1)
          specifies a range of consecutive glyph indices and a list of
          corresponding glyph class values. This table is useful for
          assigning each glyph to a different class because the glyph
          indices in each class are not grouped together.</p><p role="">A ClassDef Format 1 table begins with a format
          identifier (ClassFormat). The range of glyph indices
          (GlyphIDs) covered by the table is identified by two values:
          the GlyphID of the first glyph (StartGlyph), and the number
          of consecutive GlyphIDs (including the first one) that will
          be assigned class values (GlyphCount). The ClassValueArray
          lists the class value assigned to each GlyphID, starting
          with the class value for StartGlyph and following the same
          order as the GlyphIDs. Any glyph not included in the range
          of covered GlyphIDs automatically belongs to Class 0.</p><p role="">Example 7 at the end of this chapter uses Format 1 to
          assign class values to the lowercase, x-height, ascender,
          and descender glyphs in a font.</p><div class="table"><a name="idm320135028256"></a><p class="title"><strong>Table 21.15. ClassDefFormat1 table: Class array</strong></p><div class="table-contents"><table role="" class="table" summary="ClassDefFormat1 table: Class array" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ClassFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">StartGlyph</td><td role="">First GlyphID of the ClassValueArray</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">GlyphCount</td><td role="">Size of the ClassValueArray</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ClassValueArray [GlyphCount]</td><td role="">Array of Class Values-one per GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135019408"></a>Class Definition Table Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.16.1"></a>Specification</h3></div></div></div><p role="">The second class definition format (ClassDefFormat2)
          defines multiple groups of glyph indices that belong to the
          same class. Each group consists of a discrete range of glyph
          indices in consecutive order (ranges cannot overlap).</p><p role="">The ClassDef Format 2 table contains a format identifier
          (ClassFormat), a count of ClassRangeRecords that define the
          groups and assign class values (ClassRangeCount), and an
          array of ClassRangeRecords ordered by the GlyphID of the
          first glyph in each record (ClassRangeRecord).</p><p role="">Each ClassRangeRecord consists of a Start glyph index,
          an End glyph index, and a Class value. All GlyphIDs in a
          range, from Start to End inclusive, constitute the class
          identified by the Class value. Any glyph not covered by a
          ClassRangeRecord is assumed to belong to Class 0.</p><p role="">Example 8 at the end of this chapter uses Format 2 to
          assign class values to four types of glyphs in the Arabic
          script.</p><div class="table"><a name="idm320135014992"></a><p class="title"><strong>Table 21.16. ClassDefFormat2 table: Class ranges</strong></p><div class="table-contents"><table role="" class="table" summary="ClassDefFormat2 table: Class ranges" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">ClassFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">ClassRangeCount</td><td role="">Number of ClassRangeRecords</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">ClassRangeRecord
              [ClassRangeCount]</td><td role="">Array of ClassRangeRecords-ordered by Start
              GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320135008128"></a><p class="title"><strong>Table 21.17. ClassRangeRecord</strong></p><div class="table-contents"><table role="" class="table" summary="ClassRangeRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">GlyphID</td><td role="">Start</td><td role="">First GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">End</td><td role="">Last GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">Class</td><td role="">Applied to all glyphs in the
              range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135000800"></a>Device Tables</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.17.1"></a>Specification</h3></div></div></div><p role="">Glyphs in a font are defined in design units specified
          by the font developer. Font scaling increases or decreases a
          glyph's size and rounds it to the nearest whole
          pixel. However, precise glyph positioning often requires
          adjustment of these scaled and rounded values. Hinting,
          applied to points in the glyph outline, is an effective
          solution to this problem, but it may require the font
          developer to redesign or re-hint glyphs.</p><p role="">Another solution-used by the <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>,
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>, <a role="" class="link" href="chapter.JSTF.md" title="Chapter 26. JSTF - The Justification Table">JSTF</a>, and
          <a role="" class="link" href="chapter.GDEF.md" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables-is to use a Device table to
          specify correction values to adjust the scaled design
          units. A Device table applies the correction values to the
          range of sizes identified by StartSize and EndSize, which
          specify the smallest and largest pixel-per-em (ppem) sizes
          needing adjustment.</p><p role="">Because the adjustments often are very small (a pixel or
          two), the correction can be compressed into a 2-, 4-, or
          8-bit representation per size. Two bits can represent a
          number in the range {-2, -1, 0, or 1}, four bits can
          represent a number in the range {-8 to 7}, and eight bits
          can represent a number in the range {-128 to 127}. The
          Device table identifies one of three data formats-signed 2-,
          4,- or 8-bit values-for the adjustment values
          (DeltaFormat). A single Device table provides delta
          information for one coordinate at a range of sizes.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="8pc"/><col width="8pc"/><col width="14pc"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th></tr></thead><tbody><tr><td role="">1</td><td role="">2</td><td role="">Signed 2-bit value, 8 values per uint16</td></tr><tr><td role="">2</td><td role="">4</td><td role="">Signed 4-bit value, 4 values per uint16</td></tr><tr><td role="">3</td><td role="">8</td><td role="">Signed 8-bit value, 2 values per uint16</td></tr></tbody></table></div><p role="">The 2-, 4-, or 8-bit signed values are packed into
          uint16's most significant bits first. For example, using a
          DeltaFormat of 2 (4-bit values), an array of values equal to
          {1, 2, 3, -1} would be represented by the DeltaValue
          0x123F.</p><p role="">The DeltaValue array lists the number of pixels to
          adjust specified points on the glyph, or the entire glyph,
          at each ppem size in the targeted range. In the array, the
          first index position specifies the number of pixels to add
          or subtract from the coordinate at the smallest ppem size
          that needs correction, the second index position specifies
          the number of pixels to add or subtract from the coordinate
          at the next ppem size, and so on for each ppem size in the
          range.</p><p role="">Example 9 at the end of this chapter uses a Device table
          to define the minimum extent value for a math script.</p><div class="table"><a name="idm320134982048"></a><p class="title"><strong>Table 21.18. Device table</strong></p><div class="table-contents"><table role="" class="table" summary="Device table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">StartSize</td><td role="">Smallest size to correct-in
              ppem</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">EndSize</td><td role="">Largest size to correct-in ppem</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">DeltaFormat</td><td role="">Format of DeltaValue array data: 1, 2, or
              3</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">DeltaValue []</td><td role="">Array of compressed data</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320134973232"></a>Common Table Examples</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.18.1"></a>Specification</h3></div></div></div><p role="">The rest of this chapter describes and illustrates
          examples of all the common table formats. All the examples
          reflect unique parameters, but the samples provide a useful
          reference for building tables specific to other
          situations.</p><p role="">The examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320134969712"></a>Example 1: ScriptList Table and ScriptRecords</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.19.1"></a>Specification</h3></div></div></div><p role="">Example 1 illustrates a ScriptList table and
          ScriptRecord definitions for a Japanese font with multiple
          scripts: Han Ideographic, Kana, and Latin. Each script has
          script-specific behavior.</p><div class="table"><a name="idm320134967264"></a><p class="title"><strong>Table 21.19. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ScriptList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheScriptList</td><td role="">ScriptList table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ScriptCount. ScriptRecord[0],in alphabetical
                  order by ScriptTag</td></tr><tr><td role="">68616E69</td><td role="">"hani"</td><td role="">ScriptTag, Han Ideographic script</td></tr><tr><td role="">0014</td><td role="">HanIScriptTable</td><td role="">offset to Script table ScriptRecord[1]</td></tr><tr><td role="">6B616E61</td><td role="">"kana"</td><td role="">ScriptTag, Hiragana and Katakana
                  scripts</td></tr><tr><td role="">0018</td><td role="">KanaScriptTable</td><td role="">offset to Script table ScriptRecord[2]</td></tr><tr><td role="">6C61746E</td><td role="">"latn"</td><td role="">ScriptTag, Latin script</td></tr><tr><td role="">001C</td><td role="">LatinScriptTable</td><td role="">offset to Script table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320134951440"></a>Example 2: Script Table, LangSysRecord, and LangSys Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.20.1"></a>Specification</h3></div></div></div><p role="">Example 2 illustrates the Script table, LangSysRecord,
          and LangSys table definitions for the Arabic script and the
          Urdu language system. The default LangSys table defines
          three default Arabic script features used to replace certain
          glyphs in words with their proper initial, medial, and final
          glyph forms. These contextual substitutions are invariant
          and occur in all language systems that use the Arabic
          script.</p><p role="">Many alternative glyphs in the Arabic script have
          language-specific uses. For instance, the Arabic, Farsi, and
          Urdu language systems use different glyphs for numerals. To
          maintain character-set compatibility, the Unicode standard
          includes separate character codes for the Arabic and Farsi
          numeral glyphs. However, the standard uses the same
          character codes for Farsi and Urdu numerals, even though
          three of the Urdu glyphs (4, 6, and 7) differ from the Farsi
          glyphs. To access and display the proper glyphs for the Urdu
          numerals, users of the text-processing client must enter the
          character codes for the Farsi numerals. Then the
          text-processing client uses a required OpenType Layout glyph
          substitution feature, defined in the Urdu LangSys table, to
          access the correct Urdu glyphs for the 4, 6, and 7
          numerals.</p><p role="">Note that the Urdu LangSys table repeats the default
          script features. This repetition is necessary because the
          Urdu language system also uses alternative glyphs in the
          initial, medial, and final glyph positions in words.</p><div class="table"><a name="idm320134946720"></a><p class="title"><strong>Table 21.20. Example 2</strong></p><div class="table-contents"><table role="" class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">Script</td><td role=""> </td></tr><tr><td role=""> </td><td role="">ArabicScriptTable</td><td role="">Script table definition</td></tr><tr><td role="">000A</td><td role="">DefLangSys</td><td role="">offset to DefaultLangSys table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LangSysCount LangSysRecord[0], in alphabetical
                  order by LangSysTag</td></tr><tr><td role="">55524420</td><td role="">"URD "</td><td role="">LangSysTag, Urdu language</td></tr><tr><td role="">0016</td><td role="">UrduLangSys</td><td role="">offset to LangSys table for Urdu</td></tr><tr><td role=""> </td><td role="">LangSys</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DefLangSys</td><td role="">default LangSys table definition</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">LookupOrder, reserved, null</td></tr><tr><td role="">FFFF</td><td role="">0xFFFF</td><td role="">ReqFeatureIndex, no required features</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">FeatureCount</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">FeatureIndex[0], in arbitrary order "init"
                  feature (initial glyph)</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">FeatureIndex[1], "fina" feature (final
                  glyph)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">FeatureIndex[2], for "medi" feature (medial
                  glyph)</td></tr><tr><td role=""> </td><td role="">LangSys</td><td role=""> </td></tr><tr><td role=""> </td><td role="">UrduLangSys</td><td role="">LangSys table definition</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">LookupOrder, reserved, null</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ReqFeatureIndex, numeral subsitution in
                  Urdu</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">FeatureCount</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">FeatureIndex[0], in arbitrary order "init"
                  feature (initial glyph)</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">FeatureIndex[1], "fina" feature (final
                  glyph)</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">FeatureIndex[2], "medi" feature (medial
                  glyph)</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320134912544"></a>Example 3: FeatureList Table and Feature Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.21.1"></a>Specification</h3></div></div></div><p role="">Example 3 shows the FeatureList and Feature table
          definitions for ligatures in the Latin script. The
          FeatureList has three features, all optional and named
          "liga." One feature, also a default, implements ligatures in
          Latin if no language-specific feature specifies other
          ligatures. Two other features implement ligatures in the
          Turkish and German languages, respectively.</p><p role="">Three lookups define glyph substitutions for rendering
          ligatures in this font. The first lookup produces the "ffi"
          and "fi" ligatures; the second produces the "ffl," "fl," and
          "ff" ligatures; and the third produces the eszet
          ligature.</p><p role="">The ligatures that begin with an "f" are separated into
          two sets because Turkish has a dotless "i" glyph and so does
          not use "ffi" and "fi" ligatures. However, Turkish does use
          the "ffl," "fl," and "ff" ligatures, and the
          TurkishLigatures feature table lists this one lookup.</p><p role="">Only the German language system uses the eszet ligature,
          so the GermanLigatures feature table includes a lookup for
          rendering that ligature.</p><p role="">Because the Latin script can use both sets of ligatures,
          the DefaultLigatures feature table defines two LookupList
          indices: one for the "ffi" and "fi" ligatures, and one for
          the "ffl," "fl," and "ff" ligatures. If the text-processing
          client selects this feature, then the font applies both
          lookups.</p><p role="">Note that the TurkishLigatures and DefaultLigatures
          feature tables both list a LookupListIndex of one (1) for
          the "ffl," "fl," and "ff" ligatures lookup. This is because
          language-specific lookups override all default
          language-system lookups, and a language-system feature table
          must explicitly list all lookups that apply to the
          language.</p><div class="table"><a name="idm320134906432"></a><p class="title"><strong>Table 21.21. Example 3</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">FeatureList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheFeatureList</td><td role="">FeatureList table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">FeatureCount FeatureRecord[0]</td></tr><tr><td role="">6C696761</td><td role="">"liga"</td><td role="">FeatureTag</td></tr><tr><td role="">0014</td><td role="">TurkishLigatures</td><td role="">offset to Feature table, FflFfFlLiga
                  FeatureRecord[1]</td></tr><tr><td role="">6C696761</td><td role="">"liga"</td><td role="">FeatureTag</td></tr><tr><td role="">001A</td><td role="">DefaultLigatures</td><td role="">offset to Feature table, FfiFiLiga, FflFfFlLiga
                  FeatureRecord[2]</td></tr><tr><td role="">6C696761</td><td role="">"liga"</td><td role="">FeatureTag</td></tr><tr><td role="">0022</td><td role="">GermanLigatures</td><td role="">offset to Feature table, EszetLiga</td></tr><tr><td role=""> </td><td role="">Feature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TurkishLigatures</td><td role="">Feature table definition</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">FeatureParams, reserved, null</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupCount</td></tr><tr><td role="">0000</td><td role="">1</td><td role="">LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td role=""> </td><td role="">Feature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DefaultLigatures</td><td role="">Feature table definition</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">FeatureParams - reserved, null</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LookupCount</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">LookupListIndex[0], in arbitrary order, ffi, fi
                  ligatures</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td role=""> </td><td role="">Feature</td><td role=""> </td></tr><tr><td role=""> </td><td role="">GermanLigatures</td><td role="">Feature table definition</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">FeatureParams - reserved, null</td></tr><tr><td role="">0001</td><td role="">3</td><td role="">LookupCount</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">LookupListIndex[0], in arbitrary order, ffi, fi
                  ligatures</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">LookupListIndex[2], eszet ligature substitution
                  Lookup</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320136301504"></a>Example 4: LookupList Table and Lookup Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.22.1"></a>Specification</h3></div></div></div><p role="">A continuation of Example 3, Example 4 shows three
          ligature lookups in the LookupList table. The first
          generates the "ffi" and "fi" ligatures; the second produces
          the "ffl," "fl," and "ff" ligatures; and the third generates
          the eszet ligature. Each lookup table defines an offset to a
          subtable that contains data for the ligature
          substitution.</p><div class="table"><a name="idm320136299008"></a><p class="title"><strong>Table 21.22. Example 4</strong></p><div class="table-contents"><table role="" class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">LookupList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheLookupList</td><td role="">LookupList table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">LookupCount</td></tr><tr><td role="">0008</td><td role="">FfiFiLookup</td><td role="">Offset to Lookup[0] table, in design
                  order</td></tr><tr><td role="">0010</td><td role="">FflFlFfLookup</td><td role="">offset to Lookup[1] table</td></tr><tr><td role="">0018</td><td role="">EszetLookup</td><td role="">offset to Lookup[2] table</td></tr><tr><td role=""> </td><td role="">Lookup</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FfiFiLookup</td><td role="">Lookup[0] table definition</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">LookupType, ligature subst</td></tr><tr><td role="">000C</td><td role="">0x000C</td><td role="">LookupFlag, IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubTableCount</td></tr><tr><td role="">0018</td><td role="">FfiFiSubtable</td><td role="">offset to FfiFi ligature substitution
                  subtable</td></tr><tr><td role=""> </td><td role="">Lookup</td><td role=""> </td></tr><tr><td role=""> </td><td role="">FflFlFfLookup</td><td role="">Lookup[1] table definition</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">LookupType ligature subst</td></tr><tr><td role="">000C</td><td role="">0x000C</td><td role="">LookupFlag- IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubTableCount</td></tr><tr><td role="">0028</td><td role="">FflFlFfSubtable</td><td role="">offset to FflFlFf ligature substitution
                  subtable</td></tr><tr><td role=""> </td><td role="">Lookup</td><td role=""> </td></tr><tr><td role=""> </td><td role="">EszetLookup</td><td role="">Lookup[2] table definition</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">LookupType- ligature subst</td></tr><tr><td role="">000C</td><td role="">0x000C</td><td role="">LookupFlag- IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">SubTableCount</td></tr><tr><td role="">0038</td><td role="">EszetSubtable</td><td role="">offset to Eszet ligature substitution
                  subtable</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320136265920"></a>Example 5: CoverageFormat1 Table (GlyphID List)</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.23.1"></a>Specification</h3></div></div></div><p role="">Example 5 illustrates a Coverage table that lists the
          GlyphIDs of all lowercase descender glyphs in a font. The
          table uses the list format instead of the range format
          because the GlyphIDs for the descender glyphs are not
          consecutively ordered.</p><div class="table"><a name="idm320136263552"></a><p class="title"><strong>Table 21.23. Example 5</strong></p><div class="table-contents"><table role="" class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">CoverageFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">DescenderCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">CoverageFormat lists</td></tr><tr><td role="">0005</td><td role="">5</td><td role="">GlyphCount</td></tr><tr><td role="">0038</td><td role="">gGlyphID</td><td role="">GlyphArray[0], in GlyphID order</td></tr><tr><td role="">003B</td><td role="">jGlyphID</td><td role="">GlyphArray[1]</td></tr><tr><td role="">0041</td><td role="">pGlyphID</td><td role="">GlyphArray[2]</td></tr><tr><td role="">0042</td><td role="">qGlyphID</td><td role="">GlyphArray[3]</td></tr><tr><td role="">004A</td><td role="">yGlyphID</td><td role="">GlyphArray[4]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320136248560"></a>Example 6: CoverageFormat2 Table (GlyphID Ranges)</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.24.1"></a>Specification</h3></div></div></div><p role="">Example 6 shows a Coverage table that defines ten
          numeral glyphs (0 through 9). The table uses the range
          format instead of the list format because the GlyphIDs are
          ordered consecutively in the font. The StartCoverageIndex of
          zero (0) indicates that the first GlyphID, for the zero
          glyph, returns a Coverage Index of 0. The second GlyphID,
          for the numeral one (1) glyph, returns a Coverage Index of
          1, and so on.</p><div class="table"><a name="idm320136245920"></a><p class="title"><strong>Table 21.24. Example 6</strong></p><div class="table-contents"><table role="" class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">CoverageFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">NumeralCoverage</td><td role="">Coverage table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">CoverageFormat, GlyphID ranges</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">RangeCount RangeRecord[0]</td></tr><tr><td role="">004E</td><td role="">0glyphID</td><td role="">Start GlyphID</td></tr><tr><td role="">0057</td><td role="">9glyphID</td><td role="">End GlyphID</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">StartCoverageIndex, first CoverageIndex =
                  0</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320136233664"></a>Example 7: ClassDefFormat1 Table (Class Array)</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.25.1"></a>Specification</h3></div></div></div><p role="">The ClassDef table in Example 7 assigns class values to
          the lowercase glyphs in a font. The x-height glyphs are in
          Class 0, the ascender glyphs are in Class 1, and the
          descender glyphs are in Class 2. The array begins with the
          index for the lowercase "a" glyph.</p><div class="table"><a name="idm320136231280"></a><p class="title"><strong>Table 21.25. Example 7</strong></p><div class="table-contents"><table role="" class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ClassDefFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">LowercaseClassDef</td><td role="">ClassDef table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">ClassFormat</td></tr><tr><td role="">0032</td><td role="">aGlyphID</td><td role="">StartGlyph</td></tr><tr><td role="">001A</td><td role="">26</td><td role="">GlyphCount</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">aGlyph, Xheight Class 0</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">bGlyph, Ascender Class 1</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">cGlyph, Xheight Class 0</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">dGlyph, Ascender Class 1</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">eGlyph, Xheight Class 0</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">fGlyph, Ascender Class 1</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">gGlyph, Descender Class 2</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">hGlyph, Ascender Class 1</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">iGlyph, Ascender Class 1</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">jGlyph, Descender Class 2</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">kGlyph, Ascender Class 1</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">lGlyph, Ascender Class 1</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">mGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">nGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">oGlyph, Xheight Class 0</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">pGlyph, Descender Class 2</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">qGlyph, Descender Class 2</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">rGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">sGlyph, Xheight Class 0</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">tGlyph, Ascender Class 1</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">uGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">vGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">wGlyph, Xheight Class 0</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">xGlyph, Xheight Class 0</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">yGlyph, Descender Class 2</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">zGlyph, Xheight Class 0</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320136184528"></a>Example 8: ClassDefFormat2 Table (Class Ranges)</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.26.1"></a>Specification</h3></div></div></div><p role="">In Example 8, the ClassDef table assigns class values to
          four types of glyphs in the Arabic script: medium-height
          base glyphs, high base glyphs, very high base glyphs, and
          default mark glyphs. The table lists only Class 1, Class 2,
          and Class 3; all glyphs not explicitly assigned a class fall
          into Class 0.</p><p role="">The table uses the range format because the GlyphIDs in
          each class are ordered consecutively in the font. In the
          ClassRange array, ClassRange definitions are ordered by the
          Start glyph index in each range. The indices of the high
          base glyphs, defined in ClassRange[0], are first in the font
          and have a class value of 2. ClassRange[1] defines all the
          very high base glyphs and assigns a class value of 3.
          ClassRange[2] contains all default mark glyphs; the class
          value is 1. Class 0 consists of all the medium-height base
          glyphs, which are not explicitly assigned a class
          value.</p><div class="table"><a name="idm320136180880"></a><p class="title"><strong>Table 21.26. Example 8</strong></p><div class="table-contents"><table role="" class="table" summary="Example 8" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">ClassDefFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">GlyphHeightClassDef</td><td role="">Class table definition</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class Format ranges</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">ClassRangeCount ClassRange[0], ordered by
                  StartGlyphID</td></tr><tr><td role="">0030</td><td role="">tahGlyphID</td><td role="">Start first GlyphID in the range</td></tr><tr><td role="">0031</td><td role="">dhahGlyphID</td><td role="">End Last GlyphID in the range</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">Class, high base glyphs, ClassRange[1]</td></tr><tr><td role="">0040</td><td role="">cafGlyphID</td><td role="">Start, first GlyphID in the range</td></tr><tr><td role="">0041</td><td role=""> gafGlyphID</td><td role="">End, Last GlyphID in the range</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">Class, very high base glyphs,
                  ClassRange[2]</td></tr><tr><td role="">00D2</td><td role="">fathatanDefaultGlyphID</td><td role="">Start, first GlyphID in the range</td></tr><tr><td role="">00D3</td><td role="">dammatanDefaultGlyphID</td><td role="">End, Last GlyphID in the range</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">Class default marks</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320132428704"></a>Example 9: Device Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.21.27.1"></a>Specification</h3></div></div></div><p role="">Example 9 defines the minimum extent value for a math
          script, using a Device table to adjust the value according
          to the size of the output font. Here, the Device table
          defines single-pixel adjustments for font sizes from 11 ppem
          to 15 ppem. The DeltaFormat is 1, which signifies a packed
          array of signed 2-bit values, eight values per
          uint16.</p><div class="table"><a name="idm320132426080"></a><p class="title"><strong>Table 21.27. Example 9</strong></p><div class="table-contents"><table role="" class="table" summary="Example 9" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">DeviceTableFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MinCoordDeviceTable</td><td role="">Device Table definition</td></tr><tr><td role="">000B</td><td role="">11</td><td role="">StartSize, 11 ppem</td></tr><tr><td role="">000F</td><td role="">15</td><td role="">EndSize, 15 ppem</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">DeltaFormat signed 2 bit value, 8 values per
                  uint16</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 11ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">increase 14ppem by 1 pixel</td></tr><tr><td role="">5540</td><td role="">1</td><td role="">increase 15ppem by 1 pixel </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>