<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.common_tables"></a>Chapter 21. CommonType Layout Common Table Formats</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6616"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.1.1"></a>Specification</h4></div></div></div><p>CommonType Layout consists of five tables: the Glyph
          Substitution table (<a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>), the Glyph
          Positioning table (<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>), the Baseline
          table (<a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>), the Justification table
          (<a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>), and the Glyph Definition table
          (<a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a>). These tables use some of the same
          data formats.</p><p>This chapter explains the conventions used in all
          CommonType Layout tables, and it describes the common table
          formats. Separate chapters provide complete details about
          the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>,
          <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>, <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>, and
          <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables.</p><p>The CommonType Layout tables provide typographic
          information for properly positioning and substituting
          glyphs, operations that are required for accurate typography
          in many language environments. CommonType Layout data is
          organized by script, language system, typographic feature,
          and lookup.</p><p>Scripts are defined at the top level. A script is a
          collection of glyphs used to represent one or more languages
          in written form (see Figure 2a). For instance, a single
          script-Latin-is used to write English, French, German, and
          many other languages. In contrast, three scripts-Hiragana,
          Katakana, and Kanji-are used to write Japanese. With
          CommonType Layout, multiple scripts may be supported by a
          single font.</p><div class="figure"><a name="idm6634"></a><p class="title"><strong>Figure 21.1. Figure 2a. Glyphs in the Latin, Kanji, and Arabic
          scripts</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig2a.gif" alt="Figure 2a. Glyphs in the Latin, Kanji, and Arabic scripts"/></div></div></div><br class="figure-break"/><p>A language system may modify the functions or appearance
          of glyphs in a script to represent a particular
          language. For example, the eszet ligature is used in the
          German language system, but not in French or English (see
          Figure 2b). And the Arabic script contains different glyphs
          for writing the Farsi and Urdu languages. In CommonType
          Layout, language systems are defined within scripts.</p><div class="figure"><a name="idm6640"></a><p class="title"><strong>Figure 21.2. Figure 2b. Differences in the English, French, and
          German language systems</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig2b.gif" alt="Figure 2b. Differences in the English, French, and German language systems"/></div></div></div><br class="figure-break"/><p>A language system defines features, which are
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
          a word.</p><div class="figure"><a name="idm6646"></a><p class="title"><strong>Figure 21.3. Figure 2c. A ligature glyph feature substitutes the
          &lt;etc&gt; ligature for individual glyphs, and a mark
          feature positions diacritical marks above an Arabic ligature
          glyph.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig2c.gif" alt="Figure 2c. A ligature glyph feature substitutes the &lt;etc&gt; ligature for individual glyphs, and a mark feature positions diacritical marks above an Arabic ligature glyph."/></div></div></div><br class="figure-break"/><p>Features are implemented with lookup data that the
          text-processing client uses to substitute and position
          glyphs. Lookups describe the glyphs affected by an
          operation, the type of operation to be applied to these
          glyphs, and the resulting glyph output.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6652"></a>Table Organization</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.2.1"></a>Specification</h4></div></div></div><p>Two CommonType Layout tables, <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, use the same data formats to
          describe the typographic functions of glyphs and the
          languages and scripts that they support: a ScriptList table,
          a FeatureList table, and a LookupList table. In
          <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, the tables define glyph
          substitution data. In <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, they define
          glyph positioning data. This chapter describes these common
          table formats.</p><p>The ScriptList identifies the scripts in a font, each of
          which is represented by a Script table that contains script
          and language-system data. Language system tables reference
          features, which are defined in the FeatureList. Each feature
          table references the lookup data defined in the LookupList
          that describes how, when, and where to implement the
          feature</p><div class="figure"><a name="idm6662"></a><p class="title"><strong>Figure 21.4. Figure 2d. The relationship of scripts, language
          systems, features, and lookups for substitution and
          positioning tables</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig2d.gif" alt="Figure 2d. The relationship of scripts, language systems, features, and lookups for substitution and positioning tables"/></div></div></div><br class="figure-break"/><div class="blockquote"><blockquote class="blockquote"><p>Note: The data in the <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> and
            <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> tables also is organized by script
            and language system. However, the data formats differ from
            those in <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
            <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, and they do not include a
            FeatureList or LookupList. The <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> and
            <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> data formats are described in the
            <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> and <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>
            chapters.</p></blockquote></div><p>The information used to substitute and position glyphs
          is defined in Lookup subtables. Each subtable supplies one
          type of information, depending upon whether the lookup is
          part of a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          table. For instance, a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> lookup might
          specify the glyphs to be substituted and the context in
          which a substitution occurs, and a <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          lookup might specify glyph position adjustments for kerning.
          CommonType Layout has seven types of <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          lookups (described in the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> chapter)
          and nine types of <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookups (described
          in the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> chapter).</p><p>Each subtable (except for an Extension LookupType
          subtable) includes a Coverage table that lists the
          "covered" glyphs that will result in a glyph substitution or
          positioning operation. The Coverage table formats are
          described in this chapter.</p><p>Some substitution or positioning operations may apply to
          groups, or classes, of glyphs. <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> Lookup subtables use the Class
          Definition table to assign glyphs to classes. This chapter
          includes a description of the Class Definition table
          formats.</p><p>Lookup subtables also may contain device tables,
          described in this chapter, to adjust scaled contour glyph
          coordinates for particular output sizes and
          resolutions. This chapter also describes the data types used
          in CommonType Layout. Sample tables and lists that illustrate
          the common data formats are supplied at the end of this
          chapter.</p><p>Scripts and Languages</p><p>Three tables and their associated records apply to
          scripts and languages: the Script List table (ScriptList)
          and its script record (ScriptRecord), the Script table and
          its language system record (LangSysRecord), and the Language
          System table (LangSys).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6693"></a>Script List Table and Script Record</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.3.1"></a>Specification</h4></div></div></div><p>CommonType Layout fonts may contain one or more groups of
          glyphs used to render various scripts, which are enumerated
          in a ScriptList table. Both the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables define Script List tables
          (ScriptList):</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table uses the
              ScriptList table to access the glyph substitution
              features that apply to a script. For details, see the
              chapter, The Glyph Substitution Table
              (<a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>).</p></li><li class="listitem"><p>The <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table uses the
              ScriptList table to access the glyph positioning
              features that apply to a script. For details, see the
              chapter, The Glyph Positioning Table
              (<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>).</p></li></ul></div><p>A ScriptList table consists of a count of the scripts
          represented by the glyphs in the font (ScriptCount) and an
          array of records (ScriptRecord), one for each script for
          which the font defines script-specific features (a script
          without script-specific features does not need a
          ScriptRecord).</p><p>If a Script table with the script tag 'DFLT' (default)
	  is present in the ScriptList table, it must have a non-NULL
	  DefaultLangSys and LangSysCount must be equal to 0. The 'DFLT'
	  Script table should be used if there is not an explicit entry
	  for the script being formatted.</p><p>The ScriptRecord array stores the records alphabetically
          by a ScriptTag that identifies the script. Each ScriptRecord
          consists of a ScriptTag and an offset to a Script
          table.</p><p>Example 1 at the end of this chapter shows a ScriptList
          table and ScriptRecords for a Japanese font that uses three
          scripts.</p><div class="table"><a name="idm6713"></a><p class="title"><strong>Table 21.1. ScriptList table</strong></p><div class="table-contents"><table class="table" summary="ScriptList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ScriptCount</td><td>Number of ScriptRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>ScriptRecord [ScriptCount]</td><td>Array of ScriptRecords - listed
              alphabetically by ScriptTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm6730"></a><p class="title"><strong>Table 21.2. ScriptRecord</strong></p><div class="table-contents"><table class="table" summary="ScriptRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>ScriptTag</td><td>4-byte ScriptTag identifier</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Script</td><td>Offset to Script table-from beginning of
              ScriptList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6747"></a>Script Table and Language System Record</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.4.1"></a>Specification</h4></div></div></div><p>A Script table identifies each language system that
          defines how to use the glyphs in a script for a particular
          language. It also references a default language system that
          defines how to use the script's glyphs in the absence of
          language-specific knowledge.</p><p>A Script table begins with an offset to the Default
          Language System table (DefaultLangSys), which defines the
          set of features that regulate the default behavior of the
          script. Next, Language System Count (LangSysCount) defines
          the number of language systems (excluding the
          DefaultLangSys) that use the script. In addition, an array
          of Language System Records (LangSysRecord) defines each
          language system (excluding the default) with an
          identification tag (LangSysTag) and an offset to a Language
          System table (LangSys). The LangSysRecord array stores the
          records alphabetically by LangSysTag.</p><p>If no language-specific script behavior is defined, the
          LangSysCount is set to zero (0), and no LangSysRecords are
          allocated.</p><div class="table"><a name="idm6754"></a><p class="title"><strong>Table 21.3. Script table</strong></p><div class="table-contents"><table class="table" summary="Script table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>DefaultLangSys</td><td>Offset to DefaultLangSys table-from beginning
              of Script table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LangSysCount</td><td>Number of LangSysRecords for this
              script-excluding the DefaultLangSys</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>LangSysRecord [LangSysCount]</td><td>Array of LangSysRecords-listed alphabetically
              by LangSysTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm6775"></a><p class="title"><strong>Table 21.4. LangSysRecord</strong></p><div class="table-contents"><table class="table" summary="LangSysRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>LangSysTag</td><td>4-byte LangSysTag identifier</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>LangSys</td><td>Offset to LangSys table-from beginning of
              Script table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6792"></a>Language System Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.5.1"></a>Specification</h4></div></div></div><p>The Language System table (LangSys) identifies
          language-system features used to render the glyphs in a
          script. (The LookupOrder offset is reserved for future
          use.)</p><p>Optionally, a LangSys table may define a Required
          Feature Index (ReqFeatureIndex) to specify one feature as
          required within the context of a particular language
          system. For example, in the Cyrillic script, the Serbian
          language system always renders certain glyphs differently
          than the Russian language system.</p><p>Only one feature index value can be tagged as the
          ReqFeatureIndex. This is not a functional limitation,
          however, because the feature and lookup definitions in
          CommonType Layout are structured so that one feature table can
          reference many glyph substitution and positioning
          lookups. When no required features are defined, then the
          ReqFeatureIndex is set to 0xFFFF.</p><p>All other features are optional. For each optional
          feature, a zero-based index value references a record
          (FeatureRecord) in the FeatureRecord array, which is stored
          in a Feature List table (FeatureList). The feature indices
          themselves (excluding the ReqFeatureIndex) are stored in
          arbitrary order in the FeatureIndex array. The FeatureCount
          specifies the total number of features listed in the
          FeatureIndex array.</p><p>Features are specified in full in the FeatureList table,
          FeatureRecord, and Feature table, which are described later
          in this chapter. Example 2 at the end of this chapter shows
          a Script table, LangSysRecord, and LangSys table used for
          contextual positioning in the Arabic script.</p><div class="table"><a name="idm6801"></a><p class="title"><strong>Table 21.5. LangSys table</strong></p><div class="table-contents"><table class="table" summary="LangSys table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>LookupOrder</td><td>= NULL (reserved for an offset to a
              reordering table)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ReqFeatureIndex</td><td>Index of a feature required for this language
              system- if no required features = 0xFFFF</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>FeatureCount</td><td>Number of FeatureIndex values for this
              language system-excludes the required
              feature</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>FeatureIndex [FeatureCount]</td><td>Array of indices into the FeatureList-in
              arbitrary order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6826"></a>Features and Lookups</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.6.1"></a>Specification</h4></div></div></div><p>Features define the functionality of an CommonType Layout
          font and they are named to convey meaning to the
          text-processing client. Consider a feature named "liga" to
          create ligatures. Because of its name, the client knows what
          the feature does and can decide whether to apply it. For
          more information, see the <a class="ulink" href="http://www.microsoft.com/typography/otspec/TTOREG.htm" target="_top">CommonType
            Layout Registered Features</a> chapter. Font
          developers can use these features, as well as create their
          own.</p><p>After choosing which features to use, the client
          assembles all lookups from the selected features. Multiple
          lookups may be needed to define the data required for
          different substitution and positioning actions, as well as
          to control the sequencing and effects of those
          actions.</p><p>To implement features, a client applies the lookups in
          the order the lookup definitions occur in the LookupList. As
          a result, within the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, lookups from several
          different features may be interleaved during text
          processing. A lookup is finished when the client locates a
          target glyph or glyph context and performs a substitution
          (if specified) or a positioning (if specified).</p><p>Note: The substitution (<a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>) lookups
          always occur before the positioning
          (<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>) lookups. The lookup sequencing
          mechanism in TrueType relies on the font to determine the
          proper order of text-processing operations.</p><p>Lookup data is defined in one or more subtables that
          contain information about specific glyphs and the operations
          to be performe on them. Each type of lookup has one or more
          corresponding subtable definitions. The choice of a subtable
          format depends upon two factors: the precise content of the
          information being applied to an operation, and the required
          storage efficiency. (For complete definitions of all lookup
          types and subtables, see the the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> chapters of this document.)</p><p>CommonType Layout features define information that is
          specific to the layout of the glyphs in a font. They do not
          encode information that is constant within the conventions
          of a particular language or the typography of a particular
          script. Information that would be replicated across all
          fonts in a given language belongs in the text-processing
          application for that language, not in the fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6843"></a>Feature List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.7.1"></a>Specification</h4></div></div></div><p>The headers of the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables contain offsets to Feature
          List tables (FeatureList) that enumerate all the features in
          a font. Features in a particular FeatureList are not limited
          to any single script. A FeatureList contains the entire list
          of either the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> features that are used to render the
          glyphs in all the scripts in the font.</p><p>The FeatureList table enumerates features in an array of
          records (FeatureRecord) and specifies the total number of
          features (FeatureCount). Every feature must have a
          FeatureRecord, which consists of a FeatureTag that
          identifies the feature and an offset to a Feature table
          (described next). The FeatureRecord array is arranged
          alphabetically by FeatureTag names.</p><p>Note: The values stored in the FeatureIndex array of a
          LangSys table are used to locate records in the
          FeatureRecord array of a FeatureList table.</p><div class="table"><a name="idm6854"></a><p class="title"><strong>Table 21.6. FeatureList table</strong></p><div class="table-contents"><table class="table" summary="FeatureList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>FeatureCount</td><td>Number of FeatureRecords in this
              table</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>FeatureRecord [FeatureCount]</td><td>Array of FeatureRecords-zero-based (first
              feature has FeatureIndex = 0)-listed alphabetically by
              FeatureTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm6871"></a><p class="title"><strong>Table 21.7. FeatureRecord</strong></p><div class="table-contents"><table class="table" summary="FeatureRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>FeatureTag</td><td>4-byte feature identification
              tag</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Feature</td><td>Offset to Feature table-from beginning of
              FeatureList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6888"></a>Feature Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.8.1"></a>Specification</h4></div></div></div><p>A Feature table defines a feature with one or more
          lookups. The client uses the lookups to substitute or
          position glyphs.</p><p>Feature tables defined within the
          <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table contain references to glyph
          substitution lookups, and feature tables defined within the
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table contain references to glyph
          positioning lookups. If a text-processing operation requires
          both glyph substitution and positioning, then both the
          <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables
          must each define a Feature table, and the tables must use
          the same FeatureTags.</p><p>A Feature table consists of an offset to a Feature
          Parameters (FeatureParams) table (if one has been defined
          for this feature - see note in the following paragraph), a
          count of the lookups listed for the feature (LookupCount),
          and an arbitrarily ordered array of indices into a
          LookupList (LookupListIndex). The LookupList indices are
          references into an array of offsets to Lookup tables.</p><p>The format of the Feature Parameters table is specific
          to a particular feature, and must be specified in the
          feature's entry in the Feature Tags section of the CommonType
          Layout Tag Registry. The length of the Feature Parameters
          table must be implicitly or explicitly specified in the
          Feature Parameters table itself. The FeatureParams field in
          the Feature Table records the offset relative to the
          beginning of the Feature Table. If a Feature Parameters
          table is not needed, the FeatureParams field must be set to
          NULL.</p><p>To identify the features in a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, a text-processing client
          reads the FeatureTag of each FeatureRecord referenced in a
          given LangSys table. Then the client selects the features it
          wants to implement and uses the LookupList to retrieve the
          Lookup indices of the chosen features. Next, the client
          arranges the indices in the LookupList order. Finally, the
          client applies the lookup data to substitute or position
          glyphs.</p><p>Example 3 at the end of this chapter shows the
          FeatureList and Feature tables used to substitute ligatures
          in two languages.</p><div class="table"><a name="idm6904"></a><p class="title"><strong>Table 21.8. Feature table</strong></p><div class="table-contents"><table class="table" summary="Feature table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>FeatureParams</td><td>= NULL (reserved for offset to
              FeatureParams)</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookupCount</td><td>Number of LookupList indices for this
              feature</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookupListIndex [LookupCount]</td><td>Array of LookupList indices for this feature
              -zero-based (first lookup is LookupListIndex =
              0)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.8.2"></a>Annotation</h4></div></div></div><p>The description of the FeatureParams field used to be in
          v1.25: "Offset to Feature Parameters table (if one has been
          defined for the feature), relative to the beginning of the
          Feature Table; = NULL if not required". It is unclear why it
          has been changed and in fact the old version is better,
          since there are font with feature params.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6928"></a>Lookup List Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.9.1"></a>Specification</h4></div></div></div><p>The headers of the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables contain offsets to Lookup
          List tables (LookupList) for glyph substitution
          (<a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> table) and glyph positioning
          (<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table). The LookupList table
          contains an array of offsets to Lookup tables (Lookup). The
          font developer defines the Lookup sequence in the Lookup
          array to control the order in which a text-processing client
          applies lookup data to glyph substitution and positioning
          operations. LookupCount specifies the total number of Lookup
          table offsets in the array.</p><p>Example 4 at the end of this chapter shows three
          ligature lookups in the LookupList table.</p><div class="table"><a name="idm6938"></a><p class="title"><strong>Table 21.9. LookupList table</strong></p><div class="table-contents"><table class="table" summary="LookupList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LookupCount</td><td>Number of lookups in this table</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Lookup [LookupCount]</td><td>Array of offsets to Lookup tables-from
              beginning of LookupList -zero based (first lookup is
              Lookup index = 0)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6955"></a>Lookup Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.10.1"></a>Specification</h4></div></div></div><p>A Lookup table (Lookup) defines the specific conditions,
          type, and results of a substitution or positioning action
          that is used to implement a feature. For example, a
          substitution operation requires a list of target glyph
          indices to be replaced, a list of replacement glyph indices,
          and a description of the type of substitution action.</p><p>Each Lookup table may contain only one type of
          information (LookupType), determined by whether the lookup
          is part of a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table. <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
          supports five LookupTypes, and <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          supports seven LookupTypes (for details about LookupTypes,
          see the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          chapters of the document).</p><p>Each LookupType is defined with one or more subtables,
          and each subtable definition provides a different
          representation format. The format is determined by the
          content of the information required for an operation and by
          required storage efficiency. When glyph information is best
          presented in more than one format, a single lookup may
          contain more than one subtable, as long as all the subtables
          are the same LookupType. For example, within a given lookup,
          a glyph index array format may best represent one set of
          target glyphs, whereas a glyph index range format may be
          better for another set of target glyphs.</p><p>During text processing, a client applies a lookup to
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
          details).</p><p>A Lookup table contains a LookupType, specified as an
          integer, that defines the type of information stored in the
          lookup. The LookupFlag specifies lookup qualifiers that
          assist a text-processing client in substituting or
          positioning glyphs. The SubTableCount specifies the total
          number of SubTables. The SubTable array specifies offsets,
          measured from the beginning of the Lookup table, to each
          SubTable enumerated in the SubTable array.</p><div class="table"><a name="idm6970"></a><p class="title"><strong>Table 21.10. Lookup table</strong></p><div class="table-contents"><table class="table" summary="Lookup table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LookupType</td><td>Different enumerations for
              <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          </td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>LookupFlag</td><td>Lookup qualifiers</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>SubTableCount</td><td>Number of SubTables for this
              lookup</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>SubTable [SubTableCount]</td><td>Array of offsets to SubTables-from beginning
              of Lookup table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The LookupFlag uses four bits and one byte:

          </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Each of the first four bits can be set in order to
                specify additional instructions for applying a lookup
                to a glyph string. The LookUpFlag bit enumeration
                table provides details about the use of these bits.
              </p></li><li class="listitem"><p>The high byte is set to specify the type of mark
                attachment.</p></li></ul></div><p>
      </p><div class="table"><a name="idm7003"></a><p class="title"><strong>Table 21.11. LookupFlag bit enumeration</strong></p><div class="table-contents"><table class="table" summary="LookupFlag bit enumeration" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th></tr></thead><tbody><tr><td>0x0001</td><td>RightToLeft</td><td>
                <p>This bit relates only to the correct
                    processing of the cursive attachment lookup type
                    (GPOS lookup type 3). When this bit is set, the
                    last glyph in a given sequence to which the
                    cursive attachment lookup is applied, will be
                    positioned on the baseline.</p>
                <p>
                  <span class="emphasis"><em>Note: Setting of this bit is not
                      intended to be used by operating systems or
                      applications to determine text
                      direction.</em></span>
                </p>
              </td></tr><tr><td>0x0002</td><td>IgnoreBaseGlyphs</td><td>If set, skips over base glyphs</td></tr><tr><td>0x0004</td><td>IgnoreLigatures</td><td>If set, skips over ligatures</td></tr><tr><td>0x0008</td><td>IgnoreMarks</td><td>If set, skips over combining marks</td></tr><tr><td>0x00F0</td><td>Reserved</td><td>For future use</td></tr><tr><td>0xFF00</td><td>MarkAttachmentType</td><td>If not zero, skips over all marks of attachment
                  type different from specified.</td></tr></tbody></table></div></div><br class="table-break"/><p>For example, in Arabic text, a character string might
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
          subtable in the <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> table.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.10.2"></a>Annotation</h4></div></div></div><p>Second paragraph, should read: "... GSUB supports seven
	LookupTypes and GPOS supports nine LookupTypes..."</p><p>In general, each lookup subtable can be described by:
	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>a pattern that the glyph string must match (at the
	      current position)</p></li><li class="listitem"><p>transformations that must performed
	      on the glyph string, if the pattern is matched.</p></li></ul></div><p>
      </p><p>It is useful to describe each lookup subtable in those
	terms, and to do so using a somewhat formalized notation. This
	goes a long way toward resolving the inherent ambiguity of the
	English language.</p><p>To describe patterns, we will use the usual regular
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
	not match any string.</p><p>For example, the pattern matched by a Ligature table in
	a Ligature Substitution in format 1 is:</p><div class="blockquote"><blockquote class="blockquote"><p>▶ L<sub>0</sub> L*
	  L<sub>1</sub> L* … L*
	  L<sub>ComponentCount-1</sub> ◀</p></blockquote></div><p>where L<sub>0</sub> = {glyph ID to which
	this Ligature table corresponds} - L, and
	L<sub>i</sub> = {Component [i-1]} - L for i &gt;
	0.</p><p>The pattern matched by a Ligature Substitution is the
	union of the patterns matched by its subtables.</p><p>Last sentence: “You <span class="emphasis"><em>can</em></span>
	define...” seems a bit weak, since there does not seem
	to be any other place where this data can be found. In other
	words: “The attachment type of the glyphs are found in
	the GDEF table.”</p><p>MarkAttachementType: A common use of this mechanism is
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
	“skip over all <span class="emphasis"><em>marks</em></span> of attachment
	type different from specified” is actually quite
	strong: only the <span class="emphasis"><em>marks</em></span> of the appropriate
	attachment type have to be skipped. This means that the test
	to determine if a glyph should be skipped cannot look just at
	the mark attachment class definition, it must also look at the
	glyph class definition.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7067"></a>Coverage Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.11.1"></a>Specification</h4></div></div></div><p>Each subtable (except an Extension LookupType subtable)
          in a lookup references a Coverage table (Coverage), which
          specifies all the glyphs affected by a substitution or
          positioning operation described in the subtable. The
          <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>, <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>, and
          <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables rely on this notion of
          coverage. If a glyph does not appear in a Coverage table,
          the client can skip that subtable and move immediately to
          the next subtable.</p><p>A Coverage table identifies glyphs by glyph indices
          (GlyphIDs) either of two ways:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>As a list of individual glyph indices in the glyph
              set.</p></li><li class="listitem"><p>As ranges of consecutive indices. The range format
              gives a number of start-glyph and end-glyph index pairs
              to denote the consecutive glyphs covered by the
              table.</p></li></ul></div><p>In a Coverage table, a format code (CoverageFormat)
          specifies the format as an integer: 1 = lists, and 2 =
          ranges.</p><p>A Coverage table defines a unique index value (Coverage
          Index) for each covered glyph. This unique value specifies
          the position of the covered glyph in the Coverage table. The
          client uses the Coverage Index to look up values in the
          subtable for each glyph.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.11.2"></a>Annotation</h4></div></div></div><p>The specification does not mention a fairly interesting
          property of the existing subtable formats: A coverage is
          really a subset of n glyphs of the font, and those glyphs
          are enumerated in glyph index order by the Coverage Index
          (i.e. CI(0) is the glyph with the smallest glyph id in that
          subset, CI(1) is the next, and so on to CI(n-1) which is the
          glyph with the largest glyph id).</p><p>It is possible that a new coverage be defined for which
          this property does not hold. However, this seems unlikely,
          and we will assume that the property will always
          hold. Recommendation: make that clear in the
          specification.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7087"></a>Coverage Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.12.1"></a>Specification</h4></div></div></div><p>Coverage Format 1 consists of a format code
          (CoverageFormat) and a count of covered glyphs (GlyphCount),
          followed by an array of glyph indices (GlyphArray). The
          glyph indices must be in numerical order for binary
          searching of the list. When a glyph is found in the Coverage
          table, its position in the GlyphArray determines the
          Coverage Index that is returned-the first glyph has a
          Coverage Index = 0, and the last glyph has a Coverage Index
          = GlyphCount -1.</p><p>Example 5 at the end of this chapter shows a Coverage
          table that uses Format 1 to list the GlyphIDs of all
          lowercase descender glyphs in a font.</p><div class="table"><a name="idm7093"></a><p class="title"><strong>Table 21.12. CoverageFormat1 table: Individual glyph
          indices</strong></p><div class="table-contents"><table class="table" summary="CoverageFormat1 table: Individual glyph&#10;          indices" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CoverageFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GlyphCount</td><td>Number of glyphs in the
              GlyphArray</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>GlyphArray [GlyphCount]</td><td>Array of GlyphIDs-in numerical
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7114"></a>Coverage Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.13.1"></a>Specification</h4></div></div></div><p>Format 2 consists of a format code (CoverageFormat) and
          a count of glyph index ranges (RangeCount), followed by an
          array of records (RangeRecords). Each RangeRecord consists
          of a start glyph index (Start), an end glyph index (End),
          and the Coverage Index associated with the range's Start
          glyph. Ranges must be in GlyphID order, and they must be
          distinct, with no overlapping.</p><p>The Coverage Indexes for the first range begin with zero
          (0), and the Start Coverage Indexes for each succeeding
          range are determined by adding the length of the preceding
          range (End GlyphID - Start GlyphID + 1) to the array Index.
          This allows for a quick calculation of the Coverage Index
          for any glyph in any range using the formula: Coverage Index
          (GlyphID) = StartCoverageIndex + GlyphID - Start
          GlyphID.</p><p>Example 6 at the end of this chapter shows a Coverage
          table that uses Format 2 to identify a range of numeral
          glyphs in a font.</p><div class="table"><a name="idm7121"></a><p class="title"><strong>Table 21.13. CoverageFormat2 table: Range of glyphs</strong></p><div class="table-contents"><table class="table" summary="CoverageFormat2 table: Range of glyphs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>CoverageFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>RangeCount</td><td>Number of RangeRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>RangeRecord [RangeCount]</td><td>Array of glyph ranges-ordered by Start
              GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm7142"></a><p class="title"><strong>Table 21.14. RangeRecord</strong></p><div class="table-contents"><table class="table" summary="RangeRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>GlyphID</td><td>Start</td><td>First GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>End</td><td>Last GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>StartCoverageIndex</td><td>Coverage Index of first GlyphID in
              range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7163"></a>Class Definition Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.14.1"></a>Specification</h4></div></div></div><p>In CommonType Layout, index values identify glyphs. For
          efficiency and ease of representation, a font developer can
          group glyph indices to form glyph classes. Class assignments
          vary in meaning from one lookup subtable to another. For
          example, in the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables, classes are used to describe
          glyph contexts. <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables also use the
          idea of glyph classes.</p><p>Consider a substitution action that replaces only the
          lowercase ascender glyphs in a glyph string. To more easily
          describe the appropriate context for the substitution, the
          font developer might divide the font's lowercase glyphs into
          two classes, one that contains the ascenders and one that
          contains the glyphs without ascenders.</p><p>A font developer can assign any glyph to any class, each
          identified with an integer called a class value. A Class
          Definition table (ClassDef) groups glyph indices by class,
          beginning with Class 1, then Class 2, and so on. All glyphs
          not assigned to a class fall into Class 0. Within a given
          class definition table, each glyph in the font belongs to
          exactly one class.</p><p>The ClassDef table can have either of two formats: one
          that assigns a range of consecutive glyph indices to
          different classes, or one that puts groups of consecutive
          glyph indices into the same class.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7174"></a>Class Definition Table Format 1</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.15.1"></a>Specification</h4></div></div></div><p>The first class definition format (ClassDefFormat1)
          specifies a range of consecutive glyph indices and a list of
          corresponding glyph class values. This table is useful for
          assigning each glyph to a different class because the glyph
          indices in each class are not grouped together.</p><p>A ClassDef Format 1 table begins with a format
          identifier (ClassFormat). The range of glyph indices
          (GlyphIDs) covered by the table is identified by two values:
          the GlyphID of the first glyph (StartGlyph), and the number
          of consecutive GlyphIDs (including the first one) that will
          be assigned class values (GlyphCount). The ClassValueArray
          lists the class value assigned to each GlyphID, starting
          with the class value for StartGlyph and following the same
          order as the GlyphIDs. Any glyph not included in the range
          of covered GlyphIDs automatically belongs to Class 0.</p><p>Example 7 at the end of this chapter uses Format 1 to
          assign class values to the lowercase, x-height, ascender,
          and descender glyphs in a font.</p><div class="table"><a name="idm7181"></a><p class="title"><strong>Table 21.15. ClassDefFormat1 table: Class array</strong></p><div class="table-contents"><table class="table" summary="ClassDefFormat1 table: Class array" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ClassFormat</td><td>Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>StartGlyph</td><td>First GlyphID of the ClassValueArray</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GlyphCount</td><td>Size of the ClassValueArray</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ClassValueArray [GlyphCount]</td><td>Array of Class Values-one per GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7206"></a>Class Definition Table Format 2</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.16.1"></a>Specification</h4></div></div></div><p>The second class definition format (ClassDefFormat2)
          defines multiple groups of glyph indices that belong to the
          same class. Each group consists of a discrete range of glyph
          indices in consecutive order (ranges cannot overlap).</p><p>The ClassDef Format 2 table contains a format identifier
          (ClassFormat), a count of ClassRangeRecords that define the
          groups and assign class values (ClassRangeCount), and an
          array of ClassRangeRecords ordered by the GlyphID of the
          first glyph in each record (ClassRangeRecord).</p><p>Each ClassRangeRecord consists of a Start glyph index,
          an End glyph index, and a Class value. All GlyphIDs in a
          range, from Start to End inclusive, constitute the class
          identified by the Class value. Any glyph not covered by a
          ClassRangeRecord is assumed to belong to Class 0.</p><p>Example 8 at the end of this chapter uses Format 2 to
          assign class values to four types of glyphs in the Arabic
          script.</p><div class="table"><a name="idm7214"></a><p class="title"><strong>Table 21.16. ClassDefFormat2 table: Class ranges</strong></p><div class="table-contents"><table class="table" summary="ClassDefFormat2 table: Class ranges" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>ClassFormat</td><td>Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>ClassRangeCount</td><td>Number of ClassRangeRecords</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>ClassRangeRecord
              [ClassRangeCount]</td><td>Array of ClassRangeRecords-ordered by Start
              GlyphID</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm7235"></a><p class="title"><strong>Table 21.17. ClassRangeRecord</strong></p><div class="table-contents"><table class="table" summary="ClassRangeRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>GlyphID</td><td>Start</td><td>First GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>End</td><td>Last GlyphID in the range</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>Class</td><td>Applied to all glyphs in the
              range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7256"></a>Device Tables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.17.1"></a>Specification</h4></div></div></div><p>Glyphs in a font are defined in design units specified
          by the font developer. Font scaling increases or decreases a
          glyph's size and rounds it to the nearest whole
          pixel. However, precise glyph positioning often requires
          adjustment of these scaled and rounded values. Hinting,
          applied to points in the glyph outline, is an effective
          solution to this problem, but it may require the font
          developer to redesign or re-hint glyphs.</p><p>Another solution-used by the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>,
          <a class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>, <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>, and
          <a class="link" href="chapter.GDEF.html" title="Chapter 23. GDEF - The Glyph Definition Table">GDEF</a> tables-is to use a Device table to
          specify correction values to adjust the scaled design
          units. A Device table applies the correction values to the
          range of sizes identified by StartSize and EndSize, which
          specify the smallest and largest pixel-per-em (ppem) sizes
          needing adjustment.</p><p>Because the adjustments often are very small (a pixel or
          two), the correction can be compressed into a 2-, 4-, or
          8-bit representation per size. Two bits can represent a
          number in the range {-2, -1, 0, or 1}, four bits can
          represent a number in the range {-8 to 7}, and eight bits
          can represent a number in the range {-128 to 127}. The
          Device table identifies one of three data formats-signed 2-,
          4,- or 8-bit values-for the adjustment values
          (DeltaFormat). A single Device table provides delta
          information for one coordinate at a range of sizes.</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th></tr></thead><tbody><tr><td>1</td><td>2</td><td>Signed 2-bit value, 8 values per uint16</td></tr><tr><td>2</td><td>4</td><td>Signed 4-bit value, 4 values per uint16</td></tr><tr><td>3</td><td>8</td><td>Signed 8-bit value, 2 values per uint16</td></tr></tbody></table></div><p>The 2-, 4-, or 8-bit signed values are packed into
          uint16's most significant bits first. For example, using a
          DeltaFormat of 2 (4-bit values), an array of values equal to
          {1, 2, 3, -1} would be represented by the DeltaValue
          0x123F.</p><p>The DeltaValue array lists the number of pixels to
          adjust specified points on the glyph, or the entire glyph,
          at each ppem size in the targeted range. In the array, the
          first index position specifies the number of pixels to add
          or subtract from the coordinate at the smallest ppem size
          that needs correction, the second index position specifies
          the number of pixels to add or subtract from the coordinate
          at the next ppem size, and so on for each ppem size in the
          range.</p><p>Example 9 at the end of this chapter uses a Device table
          to define the minimum extent value for a math script.</p><div class="table"><a name="idm7290"></a><p class="title"><strong>Table 21.18. Device table</strong></p><div class="table-contents"><table class="table" summary="Device table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>StartSize</td><td>Smallest size to correct-in
              ppem</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>EndSize</td><td>Largest size to correct-in ppem</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>DeltaFormat</td><td>Format of DeltaValue array data: 1, 2, or
              3</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>DeltaValue []</td><td>Array of compressed data</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7315"></a>Common Table Examples</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.18.1"></a>Specification</h4></div></div></div><p>The rest of this chapter describes and illustrates
          examples of all the common table formats. All the examples
          reflect unique parameters, but the samples provide a useful
          reference for building tables specific to other
          situations.</p><p>The examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7321"></a>Example 1: ScriptList Table and ScriptRecords</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.19.1"></a>Specification</h4></div></div></div><p>Example 1 illustrates a ScriptList table and
          ScriptRecord definitions for a Japanese font with multiple
          scripts: Han Ideographic, Kana, and Latin. Each script has
          script-specific behavior.</p><div class="table"><a name="idm7326"></a><p class="title"><strong>Table 21.19. Example 1</strong></p><div class="table-contents"><table class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ScriptList</td><td> </td></tr><tr><td> </td><td>TheScriptList</td><td>ScriptList table definition</td></tr><tr><td>0003</td><td>3</td><td>ScriptCount. ScriptRecord[0],in alphabetical
                  order by ScriptTag</td></tr><tr><td>68616E69</td><td>"hani"</td><td>ScriptTag, Han Ideographic script</td></tr><tr><td>0014</td><td>HanIScriptTable</td><td>offset to Script table ScriptRecord[1]</td></tr><tr><td>6B616E61</td><td>"kana"</td><td>ScriptTag, Hiragana and Katakana
                  scripts</td></tr><tr><td>0018</td><td>KanaScriptTable</td><td>offset to Script table ScriptRecord[2]</td></tr><tr><td>6C61746E</td><td>"latn"</td><td>ScriptTag, Latin script</td></tr><tr><td>001C</td><td>LatinScriptTable</td><td>offset to Script table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7371"></a>Example 2: Script Table, LangSysRecord, and LangSys Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.20.1"></a>Specification</h4></div></div></div><p>Example 2 illustrates the Script table, LangSysRecord,
          and LangSys table definitions for the Arabic script and the
          Urdu language system. The default LangSys table defines
          three default Arabic script features used to replace certain
          glyphs in words with their proper initial, medial, and final
          glyph forms. These contextual substitutions are invariant
          and occur in all language systems that use the Arabic
          script.</p><p>Many alternative glyphs in the Arabic script have
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
          text-processing client uses a required CommonType Layout glyph
          substitution feature, defined in the Urdu LangSys table, to
          access the correct Urdu glyphs for the 4, 6, and 7
          numerals.</p><p>Note that the Urdu LangSys table repeats the default
          script features. This repetition is necessary because the
          Urdu language system also uses alternative glyphs in the
          initial, medial, and final glyph positions in words.</p><div class="table"><a name="idm7378"></a><p class="title"><strong>Table 21.20. Example 2</strong></p><div class="table-contents"><table class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>Script</td><td> </td></tr><tr><td> </td><td>ArabicScriptTable</td><td>Script table definition</td></tr><tr><td>000A</td><td>DefLangSys</td><td>offset to DefaultLangSys table</td></tr><tr><td>0001</td><td>1</td><td>LangSysCount LangSysRecord[0], in alphabetical
                  order by LangSysTag</td></tr><tr><td>55524420</td><td>"URD "</td><td>LangSysTag, Urdu language</td></tr><tr><td>0016</td><td>UrduLangSys</td><td>offset to LangSys table for Urdu</td></tr><tr><td> </td><td>LangSys</td><td> </td></tr><tr><td> </td><td>DefLangSys</td><td>default LangSys table definition</td></tr><tr><td>0000</td><td>NULL</td><td>LookupOrder, reserved, null</td></tr><tr><td>FFFF</td><td>0xFFFF</td><td>ReqFeatureIndex, no required features</td></tr><tr><td>0003</td><td>3</td><td>FeatureCount</td></tr><tr><td>0000</td><td>0</td><td>FeatureIndex[0], in arbitrary order "init"
                  feature (initial glyph)</td></tr><tr><td>0001</td><td>1</td><td>FeatureIndex[1], "fina" feature (final
                  glyph)</td></tr><tr><td>0002</td><td>2</td><td>FeatureIndex[2], for "medi" feature (medial
                  glyph)</td></tr><tr><td> </td><td>LangSys</td><td> </td></tr><tr><td> </td><td>UrduLangSys</td><td>LangSys table definition</td></tr><tr><td>0000</td><td>NULL</td><td>LookupOrder, reserved, null</td></tr><tr><td>0003</td><td>3</td><td>ReqFeatureIndex, numeral subsitution in
                  Urdu</td></tr><tr><td>0003</td><td>3</td><td>FeatureCount</td></tr><tr><td>0000</td><td>0</td><td>FeatureIndex[0], in arbitrary order "init"
                  feature (initial glyph)</td></tr><tr><td>0001</td><td>1</td><td>FeatureIndex[1], "fina" feature (final
                  glyph)</td></tr><tr><td>0002</td><td>2</td><td>FeatureIndex[2], "medi" feature (medial
                  glyph)</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7475"></a>Example 3: FeatureList Table and Feature Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.21.1"></a>Specification</h4></div></div></div><p>Example 3 shows the FeatureList and Feature table
          definitions for ligatures in the Latin script. The
          FeatureList has three features, all optional and named
          "liga." One feature, also a default, implements ligatures in
          Latin if no language-specific feature specifies other
          ligatures. Two other features implement ligatures in the
          Turkish and German languages, respectively.</p><p>Three lookups define glyph substitutions for rendering
          ligatures in this font. The first lookup produces the "ffi"
          and "fi" ligatures; the second produces the "ffl," "fl," and
          "ff" ligatures; and the third produces the eszet
          ligature.</p><p>The ligatures that begin with an "f" are separated into
          two sets because Turkish has a dotless "i" glyph and so does
          not use "ffi" and "fi" ligatures. However, Turkish does use
          the "ffl," "fl," and "ff" ligatures, and the
          TurkishLigatures feature table lists this one lookup.</p><p>Only the German language system uses the eszet ligature,
          so the GermanLigatures feature table includes a lookup for
          rendering that ligature.</p><p>Because the Latin script can use both sets of ligatures,
          the DefaultLigatures feature table defines two LookupList
          indices: one for the "ffi" and "fi" ligatures, and one for
          the "ffl," "fl," and "ff" ligatures. If the text-processing
          client selects this feature, then the font applies both
          lookups.</p><p>Note that the TurkishLigatures and DefaultLigatures
          feature tables both list a LookupListIndex of one (1) for
          the "ffl," "fl," and "ff" ligatures lookup. This is because
          language-specific lookups override all default
          language-system lookups, and a language-system feature table
          must explicitly list all lookups that apply to the
          language.</p><div class="table"><a name="idm7485"></a><p class="title"><strong>Table 21.21. Example 3</strong></p><div class="table-contents"><table class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>FeatureList</td><td> </td></tr><tr><td> </td><td>TheFeatureList</td><td>FeatureList table definition</td></tr><tr><td>0003</td><td>3</td><td>FeatureCount FeatureRecord[0]</td></tr><tr><td>6C696761</td><td>"liga"</td><td>FeatureTag</td></tr><tr><td>0014</td><td>TurkishLigatures</td><td>offset to Feature table, FflFfFlLiga
                  FeatureRecord[1]</td></tr><tr><td>6C696761</td><td>"liga"</td><td>FeatureTag</td></tr><tr><td>001A</td><td>DefaultLigatures</td><td>offset to Feature table, FfiFiLiga, FflFfFlLiga
                  FeatureRecord[2]</td></tr><tr><td>6C696761</td><td>"liga"</td><td>FeatureTag</td></tr><tr><td>0022</td><td>GermanLigatures</td><td>offset to Feature table, EszetLiga</td></tr><tr><td> </td><td>Feature</td><td> </td></tr><tr><td> </td><td>TurkishLigatures</td><td>Feature table definition</td></tr><tr><td>0000</td><td>NULL</td><td>FeatureParams, reserved, null</td></tr><tr><td>0001</td><td>1</td><td>LookupCount</td></tr><tr><td>0000</td><td>1</td><td>LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td> </td><td>Feature</td><td> </td></tr><tr><td> </td><td>DefaultLigatures</td><td>Feature table definition</td></tr><tr><td>0000</td><td>NULL</td><td>FeatureParams - reserved, null</td></tr><tr><td>0002</td><td>2</td><td>LookupCount</td></tr><tr><td>0000</td><td>0</td><td>LookupListIndex[0], in arbitrary order, ffi, fi
                  ligatures</td></tr><tr><td>0001</td><td>1</td><td>LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td> </td><td>Feature</td><td> </td></tr><tr><td> </td><td>GermanLigatures</td><td>Feature table definition</td></tr><tr><td>0000</td><td>NULL</td><td>FeatureParams - reserved, null</td></tr><tr><td>0001</td><td>3</td><td>LookupCount</td></tr><tr><td>0000</td><td>0</td><td>LookupListIndex[0], in arbitrary order, ffi, fi
                  ligatures</td></tr><tr><td>0001</td><td>1</td><td>LookupListIndex[1], ffl, fl, ff ligature
                  substitution Lookup</td></tr><tr><td>0002</td><td>2</td><td>LookupListIndex[2], eszet ligature substitution
                  Lookup</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7602"></a>Example 4: LookupList Table and Lookup Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.22.1"></a>Specification</h4></div></div></div><p>A continuation of Example 3, Example 4 shows three
          ligature lookups in the LookupList table. The first
          generates the "ffi" and "fi" ligatures; the second produces
          the "ffl," "fl," and "ff" ligatures; and the third generates
          the eszet ligature. Each lookup table defines an offset to a
          subtable that contains data for the ligature
          substitution.</p><div class="table"><a name="idm7607"></a><p class="title"><strong>Table 21.22. Example 4</strong></p><div class="table-contents"><table class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>LookupList</td><td> </td></tr><tr><td> </td><td>TheLookupList</td><td>LookupList table definition</td></tr><tr><td>0003</td><td>3</td><td>LookupCount</td></tr><tr><td>0008</td><td>FfiFiLookup</td><td>Offset to Lookup[0] table, in design
                  order</td></tr><tr><td>0010</td><td>FflFlFfLookup</td><td>offset to Lookup[1] table</td></tr><tr><td>0018</td><td>EszetLookup</td><td>offset to Lookup[2] table</td></tr><tr><td> </td><td>Lookup</td><td> </td></tr><tr><td> </td><td>FfiFiLookup</td><td>Lookup[0] table definition</td></tr><tr><td>0004</td><td>4</td><td>LookupType, ligature subst</td></tr><tr><td>000C</td><td>0x000C</td><td>LookupFlag, IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td>0001</td><td>1</td><td>SubTableCount</td></tr><tr><td>0018</td><td>FfiFiSubtable</td><td>offset to FfiFi ligature substitution
                  subtable</td></tr><tr><td> </td><td>Lookup</td><td> </td></tr><tr><td> </td><td>FflFlFfLookup</td><td>Lookup[1] table definition</td></tr><tr><td>0004</td><td>4</td><td>LookupType ligature subst</td></tr><tr><td>000C</td><td>0x000C</td><td>LookupFlag- IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td>0001</td><td>1</td><td>SubTableCount</td></tr><tr><td>0028</td><td>FflFlFfSubtable</td><td>offset to FflFlFf ligature substitution
                  subtable</td></tr><tr><td> </td><td>Lookup</td><td> </td></tr><tr><td> </td><td>EszetLookup</td><td>Lookup[2] table definition</td></tr><tr><td>0004</td><td>4</td><td>LookupType- ligature subst</td></tr><tr><td>000C</td><td>0x000C</td><td>LookupFlag- IgnoreLigatures,
                  IgnoreMarks</td></tr><tr><td>0001</td><td>1</td><td>SubTableCount</td></tr><tr><td>0038</td><td>EszetSubtable</td><td>offset to Eszet ligature substitution
                  subtable</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7712"></a>Example 5: CoverageFormat1 Table (GlyphID List)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.23.1"></a>Specification</h4></div></div></div><p>Example 5 illustrates a Coverage table that lists the
          GlyphIDs of all lowercase descender glyphs in a font. The
          table uses the list format instead of the range format
          because the GlyphIDs for the descender glyphs are not
          consecutively ordered.</p><div class="table"><a name="idm7717"></a><p class="title"><strong>Table 21.23. Example 5</strong></p><div class="table-contents"><table class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>DescenderCoverage</td><td>Coverage table definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat lists</td></tr><tr><td>0005</td><td>5</td><td>GlyphCount</td></tr><tr><td>0038</td><td>gGlyphID</td><td>GlyphArray[0], in GlyphID order</td></tr><tr><td>003B</td><td>jGlyphID</td><td>GlyphArray[1]</td></tr><tr><td>0041</td><td>pGlyphID</td><td>GlyphArray[2]</td></tr><tr><td>0042</td><td>qGlyphID</td><td>GlyphArray[3]</td></tr><tr><td>004A</td><td>yGlyphID</td><td>GlyphArray[4]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7762"></a>Example 6: CoverageFormat2 Table (GlyphID Ranges)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.24.1"></a>Specification</h4></div></div></div><p>Example 6 shows a Coverage table that defines ten
          numeral glyphs (0 through 9). The table uses the range
          format instead of the list format because the GlyphIDs are
          ordered consecutively in the font. The StartCoverageIndex of
          zero (0) indicates that the first GlyphID, for the zero
          glyph, returns a Coverage Index of 0. The second GlyphID,
          for the numeral one (1) glyph, returns a Coverage Index of
          1, and so on.</p><div class="table"><a name="idm7767"></a><p class="title"><strong>Table 21.24. Example 6</strong></p><div class="table-contents"><table class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>CoverageFormat2</td><td> </td></tr><tr><td> </td><td>NumeralCoverage</td><td>Coverage table definition</td></tr><tr><td>0002</td><td>2</td><td>CoverageFormat, GlyphID ranges</td></tr><tr><td>0001</td><td>1</td><td>RangeCount RangeRecord[0]</td></tr><tr><td>004E</td><td>0glyphID</td><td>Start GlyphID</td></tr><tr><td>0057</td><td>9glyphID</td><td>End GlyphID</td></tr><tr><td>0000</td><td>0</td><td>StartCoverageIndex, first CoverageIndex =
                  0</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7804"></a>Example 7: ClassDefFormat1 Table (Class Array)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.25.1"></a>Specification</h4></div></div></div><p>The ClassDef table in Example 7 assigns class values to
          the lowercase glyphs in a font. The x-height glyphs are in
          Class 0, the ascender glyphs are in Class 1, and the
          descender glyphs are in Class 2. The array begins with the
          index for the lowercase "a" glyph.</p><div class="table"><a name="idm7809"></a><p class="title"><strong>Table 21.25. Example 7</strong></p><div class="table-contents"><table class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ClassDefFormat1</td><td> </td></tr><tr><td> </td><td>LowercaseClassDef</td><td>ClassDef table definition</td></tr><tr><td>0001</td><td>1</td><td>ClassFormat</td></tr><tr><td>0032</td><td>aGlyphID</td><td>StartGlyph</td></tr><tr><td>001A</td><td>26</td><td>GlyphCount</td></tr><tr><td>0000</td><td>0</td><td>aGlyph, Xheight Class 0</td></tr><tr><td>0001</td><td>1</td><td>bGlyph, Ascender Class 1</td></tr><tr><td>0000</td><td>0</td><td>cGlyph, Xheight Class 0</td></tr><tr><td>0001</td><td>1</td><td>dGlyph, Ascender Class 1</td></tr><tr><td>0000</td><td>0</td><td>eGlyph, Xheight Class 0</td></tr><tr><td>0001</td><td>1</td><td>fGlyph, Ascender Class 1</td></tr><tr><td>0002</td><td>2</td><td>gGlyph, Descender Class 2</td></tr><tr><td>0001</td><td>1</td><td>hGlyph, Ascender Class 1</td></tr><tr><td>0000</td><td>0</td><td>iGlyph, Ascender Class 1</td></tr><tr><td>0002</td><td>2</td><td>jGlyph, Descender Class 2</td></tr><tr><td>0001</td><td>1</td><td>kGlyph, Ascender Class 1</td></tr><tr><td>0001</td><td>1</td><td>lGlyph, Ascender Class 1</td></tr><tr><td>0000</td><td>0</td><td>mGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>nGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>oGlyph, Xheight Class 0</td></tr><tr><td>0002</td><td>2</td><td>pGlyph, Descender Class 2</td></tr><tr><td>0002</td><td>2</td><td>qGlyph, Descender Class 2</td></tr><tr><td>0000</td><td>0</td><td>rGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>sGlyph, Xheight Class 0</td></tr><tr><td>0001</td><td>1</td><td>tGlyph, Ascender Class 1</td></tr><tr><td>0000</td><td>0</td><td>uGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>vGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>wGlyph, Xheight Class 0</td></tr><tr><td>0000</td><td>0</td><td>xGlyph, Xheight Class 0</td></tr><tr><td>0002</td><td>2</td><td>yGlyph, Descender Class 2</td></tr><tr><td>0000</td><td>0</td><td>zGlyph, Xheight Class 0</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm7942"></a>Example 8: ClassDefFormat2 Table (Class Ranges)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.26.1"></a>Specification</h4></div></div></div><p>In Example 8, the ClassDef table assigns class values to
          four types of glyphs in the Arabic script: medium-height
          base glyphs, high base glyphs, very high base glyphs, and
          default mark glyphs. The table lists only Class 1, Class 2,
          and Class 3; all glyphs not explicitly assigned a class fall
          into Class 0.</p><p>The table uses the range format because the GlyphIDs in
          each class are ordered consecutively in the font. In the
          ClassRange array, ClassRange definitions are ordered by the
          Start glyph index in each range. The indices of the high
          base glyphs, defined in ClassRange[0], are first in the font
          and have a class value of 2. ClassRange[1] defines all the
          very high base glyphs and assigns a class value of 3.
          ClassRange[2] contains all default mark glyphs; the class
          value is 1. Class 0 consists of all the medium-height base
          glyphs, which are not explicitly assigned a class
          value.</p><div class="table"><a name="idm7948"></a><p class="title"><strong>Table 21.26. Example 8</strong></p><div class="table-contents"><table class="table" summary="Example 8" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>ClassDefFormat2</td><td> </td></tr><tr><td> </td><td>GlyphHeightClassDef</td><td>Class table definition</td></tr><tr><td>0002</td><td>2</td><td>Class Format ranges</td></tr><tr><td>0003</td><td>3</td><td>ClassRangeCount ClassRange[0], ordered by
                  StartGlyphID</td></tr><tr><td>0030</td><td>tahGlyphID</td><td>Start first GlyphID in the range</td></tr><tr><td>0031</td><td>dhahGlyphID</td><td>End Last GlyphID in the range</td></tr><tr><td>0002</td><td>2</td><td>Class, high base glyphs, ClassRange[1]</td></tr><tr><td>0040</td><td>cafGlyphID</td><td>Start, first GlyphID in the range</td></tr><tr><td>0041</td><td> gafGlyphID</td><td>End, Last GlyphID in the range</td></tr><tr><td>0003</td><td>3</td><td>Class, very high base glyphs,
                  ClassRange[2]</td></tr><tr><td>00D2</td><td>fathatanDefaultGlyphID</td><td>Start, first GlyphID in the range</td></tr><tr><td>00D3</td><td>dammatanDefaultGlyphID</td><td>End, Last GlyphID in the range</td></tr><tr><td>0001</td><td>1</td><td>Class default marks</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm8009"></a>Example 9: Device Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.22.27.1"></a>Specification</h4></div></div></div><p>Example 9 defines the minimum extent value for a math
          script, using a Device table to adjust the value according
          to the size of the output font. Here, the Device table
          defines single-pixel adjustments for font sizes from 11 ppem
          to 15 ppem. The DeltaFormat is 1, which signifies a packed
          array of signed 2-bit values, eight values per
          uint16.</p><div class="table"><a name="idm8014"></a><p class="title"><strong>Table 21.27. Example 9</strong></p><div class="table-contents"><table class="table" summary="Example 9" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>DeviceTableFormat1</td><td> </td></tr><tr><td> </td><td>MinCoordDeviceTable</td><td>Device Table definition</td></tr><tr><td>000B</td><td>11</td><td>StartSize, 11 ppem</td></tr><tr><td>000F</td><td>15</td><td>EndSize, 15 ppem</td></tr><tr><td>0001</td><td>1</td><td>DeltaFormat signed 2 bit value, 8 values per
                  uint16</td></tr><tr><td> </td><td>1</td><td>increase 11ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 12ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 13ppem by 1 pixel</td></tr><tr><td> </td><td>1</td><td>increase 14ppem by 1 pixel</td></tr><tr><td>5540</td><td>1</td><td>increase 15ppem by 1 pixel </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>