<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.BASE"></a>Chapter 22. BASE - Baseline Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627375504"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.1.1"></a>Specification</h3></div></div></div><p role="">The Baseline table (<a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>) provides
          information used to align glyphs of different scripts and
          sizes in a line of text, whether the glyphs are in the same
          font or in different fonts. To improve text layout, the
          Baseline table also provides minimum (min) and maximum (max)
          glyph extent values for each script, language system, or
          feature in a font.</p><p role="">Lines of text composed with glyphs of different scripts
          and point sizes need adjustment to correct interline spacing
          and alignment. For example, glyphs designed to be the same
          point size often differ in height and depth from one font to
          another (see figure 5a). This variation can produce
          interline spacing that looks too large or too small, and
          diacritical marks, math symbols, subscripts, and
          superscripts may be clipped.</p><div class="figure"><a name="idm114627371648"></a><p class="title"><strong>Figure 22.1. Figure 5a. Incorrect alignment of glyphs from Latin
            and Kanji (Latin dominant)</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig5a.gif" alt="Figure 5a. Incorrect alignment of glyphs from Latin and Kanji (Latin dominant)"/></div></div></div><br class="figure-break"/><p role="">In addition, different baselines can cause text lines to
          waver visually as glyphs from different scripts are placed
          next to one another. For example, ideographic scripts
          position all glyphs on a low baseline. With Latin scripts,
          however, the baseline is higher, and some glyphs descend
          below it. Finally, several Indic scripts use a high "hanging
          baseline" to align the tops of the glyphs.</p><p role="">To solve these composition problems, the
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table recommends baseline positions
          and min/max extents for each script (see figure 5b). Script
          min/max extents can be modified for particular language
          systems or features.</p><div class="figure"><a name="idm114627367488"></a><p class="title"><strong>Figure 22.2. Figure 5b. Proper alignment of glyphs from Latin and
            Kanji (Latin dominant)</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig5b.gif" alt="Figure 5b. Proper alignment of glyphs from Latin and Kanji (Latin dominant)"/></div></div></div><br class="figure-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627364912"></a>Baseline Values</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.2.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table uses a model that
          assumes one script at one size is the "dominant run" during
          text processing-that is, all other baselines are defined in
          relation to this the dominant run.</p><p role="">For example, Latin glyphs and the ideographic Kanji
          glyphs have different baselines. If a Latin script of a
          particular size is specified as the dominant run, then all
          Latin glyphs of all sizes will be aligned on the roman
          baseline, and all Kanji glyphs will be aligned on the lower
          ideographic baseline defined for use with Latin text. As a
          result, all glyphs will look aligned within each line of
          text.</p><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table supplies recommended
          baseline positions; a client can specify others. For
          instance, the client may want to assign baseline positions
          different from those in the font.</p><div class="figure"><a name="idm114627359936"></a><p class="title"><strong>Figure 22.3. Figure 5c. Comparing Latin and Kanji baselines, with
            characters aligned according to the dominant run</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig5c.gif" alt="Figure 5c. Comparing Latin and Kanji baselines, with characters aligned according to the dominant run"/></div></div></div><br class="figure-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627357328"></a>Min/Max Extent Values</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.3.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table gives clients the
          option of using script, language system, or feature-specific
          extent values to improve composition (see figure 5c). For
          example, suppose a font contains glyphs in Latin and Arabic
          scripts, and the min/max extents defined for the Arabic
          script are larger than the Latin extents. The font also
          supports Urdu, a language system that includes specific
          variants of the Arabic glyphs, and some Urdu variants
          require larger min/max extents than the default Arabic
          extents. To accommodate the Urdu glyphs, the
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table can define language-specific
          min/max extent values that will override the default Arabic
          extents-but only when rendering Urdu glyphs.</p><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table also can define
          feature-specific min/max values that apply only when a
          particular feature is enabled.  Suppose that the font
          described earlier also supports the Farsi language system,
          which has one feature that requires a minor alteration of
          the Arabic script extents to display properly. The
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table can specify these extent
          values and apply them only when that feature is enabled in
          the Farsi language.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627350640"></a>Table Organization</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.4.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table begins with offsets to
          Axis tables that describe layout data for the horizontal and
          vertical layout directions of text. A font can provide
          layout data for both text directions or for only one text
          direction:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The Horizontal Axis table (HorizAxis) defines
              information used to lay out text horizontally. All
              baseline and min/max values refer to the Y
              direction.</p></li><li role="" class="listitem"><p role="">The Vertical Axis table (VertAxis) defines
              information used to lay out text vertically. All
              baseline and min/max values refer to the X
              direction.</p></li></ul></div><p role="">Note: The same baseline tags can be used for both
          horizontal and vertical axes. For example, the 'romn' tag
          description used for the vertical axis would indicate the
          baseline of rotated Latin text.</p><p role="">Figure 5d shows how the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table is
        organized.</p><div class="figure"><a name="idm114627343760"></a><p class="title"><strong>Figure 22.4. Figure 5d. High-level organization of <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>
            table</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/fig5d.gif" alt="Figure 5d. High-level organization of BASE table"/></div></div></div><br class="figure-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627340672"></a>Text Direction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.5.1"></a>Specification</h3></div></div></div><p role="">The HorizAxis and VertAxis tables organize layout
          information by script in BaseScriptList tables. A
          BaseScriptList enumerates all scripts in the font that are
          written in a particular direction (horizontal or
          vertical).</p><p role="">For example, consider a Japanese font that contains
          Kanji, Kana, and Latin scripts. Because all three scripts
          are rendered horizontally, all three are defined in the
          BaseScriptList of the HorizAxis table. Kanji and Kana also
          are rendered vertically, so those two scripts are defined in
          the BaseScriptList of the VertAxis table, too.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627337088"></a>Baseline Data</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.6.1"></a>Specification</h3></div></div></div><p role="">Each Axis table also references a BaseTagList, which
          identifies all the baselines for all scripts written in the
          same direction (horizontal or vertical). The BaseTagList may
          also include baseline tags for scripts supported in other
          fonts.</p><p role="">Each script in a BaseScriptList is represented by a
          BaseScriptRecord. This record references a BaseScript table,
          which contains layout data for the script. In turn, the
          BaseScript table references a BaseValues table, which
          contains baseline information and several MinMax tables that
          define min/max extent values.</p><p role="">The BaseValues table specifies the coordinate values for
          all baselines in the BaseTagList. In addition, it identifies
          one of these baselines as the default baseline for the
          script. As glyphs in a script are scaled, they grow or
          shrink from the script's default baseline position. Each
          baseline can have unique coordinates. This contrasts with
          TrueType 1.0, which implies a single, fixed baseline for all
          scripts in a font. With the OpenType Layout tables, each
          script can be aligned independently, although more than one
          script may use the same baseline values.</p><p role="">Baseline coordinates for scripts in the same font must
          be specified in relation to each other for correct alignment
          of the glyphs. Consider the font, discussed earlier,
          containing both Latin and Kanji glyphs. If the BaseTagList
          of the HorizAxis table specifies two baselines, the roman
          and the ideographic, then the layout data for both the Latin
          and Kanji scripts will specify coordinate positions for both
          baselines:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The BaseValues table for the Latin script will give
              coordinates for both baselines and specify the roman
              baseline as the default.</p></li><li role="" class="listitem"><p role="">The BaseValues table for the Kanji script will give
              coordinates for both baselines and specify the
              ideographic baseline as the default.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114627329328"></a>Min/Max Extents</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.7.1"></a>Specification</h3></div></div></div><p role="">The BaseScript table can define minimum and maximum
          extent values for each script, language system, or feature.
          (These values are distinct from the min/max extent values
          recorded for the font as a whole in the head, hhea, vhea,
          and OS/2 tables.) These extent values appear in three
          tables:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The DefaultMinMax table defines the default min/max
              extents for the script.</p></li><li role="" class="listitem"><p role="">A MinMax table, referenced through a
              BaseLangSysRecord, specifies min/max extents to
              accommodate the glyphs in a specific language
              system.</p></li><li role="" class="listitem"><p role="">A FeatMinMaxRecord, referenced from the MinMax
              table, provides min/max extent values to support
              feature-specific glyph actions.</p><p role="">Note: Language-system or feature-specific extent
              values may be essential to define some fonts. However,
              the default min/max extent values specified for each
              script should usually be enough to support high-quality
              text layout.</p></li></ul></div><p role="">The actual baseline and min/max extent values used by
          the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table reside in BaseCoord
          tables. Three formats are defined for BaseCoord table
          data. All formats define single X or Y coordinate values in
          design units, but two formats support fine adjustments to
          these values based on a contour point or a Device
          table.</p><p role="">The rest of this chapter describes all the tables
          defined within the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table. Sample
          tables and lists that illustrate typical data for a font are
          supplied at the end of the chapter.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639658432"></a>BASE Header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.8.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table begins with a header
          that consists of a version number for the table (Version),
          initially set to 1.0 (0x00010000), and offsets to horizontal
          and vertical Axis tables (HorizAxis and VertAxis).</p><p role="">Each Axis table stores all baseline information and
          min/max extents for one layout direction. The HorizAxis
          table contains Y values for horizontal text layout; the
          VertAxis table contains X values for vertical text
          layout.</p><p role="">A font may supply information for both
          layout directions. If a font has values for only one text
          direction, the Axis table offset value for the other
          direction will be set to NULL.</p><p role="">Example 1 at the end of this chapter shows a sample
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> Header.</p><div class="table"><a name="idm114639653248"></a><p class="title"><strong>Table 22.1. BASE Header</strong></p><div class="table-contents"><table role="" class="table" summary="BASE Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">fixed32</td><td role="">Version</td><td role="">Version of the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a>
              table-initially 0x00010000</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">HorizAxis</td><td role="">Offset to horizontal Axis table-from
              beginning of <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">VertAxis</td><td role="">Offset to vertical Axis table-from beginning
              of <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639644272"></a>Axis Tables: HorizAxis and VertAxis</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.9.1"></a>Specification</h3></div></div></div><p role="">An Axis table is used to render scripts either
          horizontally or vertically. It consists of offsets, measured
          from the beginning of the Axis table, to a BaseTagList and a
          BaseScriptList:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The BaseScriptList enumerates all scripts rendered
              in the text layout direction.</p></li><li role="" class="listitem"><p role="">The BaseTagList enumerates all baselines used to
              render the scripts in the text layout direction. If no
              baseline data is available for a text direction, the
              offset to the corresponding BaseTagList may be set to
              NULL.</p></li></ul></div><p role="">Example 1 at the end of this chapter shows an example of
          an Axis table.</p><div class="table"><a name="idm114639639184"></a><p class="title"><strong>Table 22.2. Axis Table</strong></p><div class="table-contents"><table role="" class="table" summary="Axis Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">BaseTagList</td><td role="">Offset to BaseTagList table-from beginning of
              Axis table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BaseScriptList</td><td role="">Offset to BaseScriptList table-from beginning
              of Axis table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639633488"></a>BaseTagList Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.10.1"></a>Specification</h3></div></div></div><p role="">The BaseTagList table identifies the baselines for all
          scripts in the font that are rendered in the same text
          direction. Each baseline is identified with a 4-byte
          baseline tag. The <a role="" class="link" href="chapter.tags_registry.md#ttoreg_basetags" title="Script tags">Baseline Tags</a>
          section of the OpenType Tag Registry lists currently
          registered baseline tags. The BaseTagList can define any
          number of baselines, and it may include baseline tags for
          scripts supported in other fonts.</p><p role="">Each script in the BaseScriptList table must designate
          one of these BaseTagList baselines as its default, which the
          OpenType Layout Services use to align all glyphs in the
          script. Even though the BaseScriptList and the BaseTagList
          are defined independently of one another, the BaseTagList
          typically includes a tag for each different default baseline
          needed to render the scripts in the layout direction. If
          some scripts use the same default baseline, the BaseTagList
          needs to list the common baseline tag only once. </p><p role="">The BaseTagList table consists of an array of baseline
          identification tags (BaselineTag), listed alphabetically,
          and a count of the total number of baseline Tags in the
          array (BaseTagCount).</p><p role="">Example 1 at the end of this chapter shows a sample
          BaseTagList table.</p><div class="table"><a name="idm114639628240"></a><p class="title"><strong>Table 22.3. BaseTagList table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseTagList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseTagCount</td><td role="">Number of baseline identification tags in
              this text direction-may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td role="">Tag</td><td role="">BaselineTag [BaseTagCount]</td><td role="">Array of 4-byte baseline identification
              tags-must be in alphabetical order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639622528"></a>BaseScriptList Table and BaseScript Record</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.11.1"></a>Specification</h3></div></div></div><p role="">The BaseScriptList table identifies all scripts in the
          font that are rendered in the same layout direction. If a
          script is not listed here, then the text-processing client
          will render the script using the layout information
          specified for the entire font.</p><p role="">For each script listed in the BaseScriptList table, a
          BaseScriptRecord must be defined that identifies the script
          and references its layout data. BaseScriptRecords are stored
          in the BaseScriptRecord array, ordered alphabetically by the
          BaseScriptTag in each record. The BaseScriptCount specifies
          the total number of BaseScriptRecords in the array.</p><p role="">Example 1 at the end of this chapter shows a sample
          BaseScriptList table.</p><div class="table"><a name="idm114639618880"></a><p class="title"><strong>Table 22.4. BaseScriptList table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseScriptList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseScriptCount</td><td role="">Number of BaseScriptRecords
              defined</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">BaseScriptRecord [BaseScriptCount]</td><td role="">Array of BaseScriptRecords-in alphabetical
              order by BaseScriptTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A BaseScriptRecord contains a script identification tag
          (BaseScriptTag), which must be identical to the ScriptTag
          used to define the script in the ScriptList of a
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table.
          Each record also must include an offset to a BaseScript
          table that defines the baseline and min/max extent data for
          the script.</p><p role="">Example 1 at the end of this chapter shows a sample
          BaseScriptRecord.</p><div class="table"><a name="idm114631472864"></a><p class="title"><strong>Table 22.5. BaseScriptRecord</strong></p><div class="table-contents"><table role="" class="table" summary="BaseScriptRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">BaseScriptTag</td><td role="">4-byte script identification
            tag</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BaseScript</td><td role="">Offset to BaseScript table-from beginning of
            BaseScriptList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631467136"></a>BaseScript Table and BaseLangSys Record</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.12.1"></a>Specification</h3></div></div></div><p role="">A BaseScript table organizes and specifies the baseline
          data and min/max extent data for one script. Within a
          BaseScript table, the BaseValues table contains baseline
          information, and one or more MinMax tables contain min/max
          extent data.</p><p role="">The BaseValues table identifies the default baseline for
          the script and lists coordinate positions for each baseline
          named in the corresponding BaseTagList. Each script can
          assign a different position to each baseline, so each script
          can be aligned independently in relation to any other
          script. (For more details, see the BaseValues table
          description later in this chapter.)</p><p role="">The DefaultMinMax table defines the default min/max
          extent values for the script. (For details, see the MinMax
          table description below.) If a language system or feature
          defined in the font has no effect on the script's default
          min/max extents, the OpenType Layout Services will use the
          default script values.</p><p role="">Sometimes language-specific overrides for min/max
          extents are needed to properly render the glyphs in a
          specific language system. For example, a glyph substitution
          required in a language system may result in a glyph whose
          extents exceed the script's default min/max extents. Each
          language system that specifies min/max extent values must
          define a BaseLangSysRecord. The record should identify the
          language system (BaseLangSysTag) and contain an offset to a
          MinMax table of language-specific extent coordinates.</p><p role="">Feature-specific overrides for min/max extents also may
          be needed to accommodate the effects of glyph actions used
          to implement a specific feature. For example, superscript or
          subscript features may require changes to the default script
          or language system extents. Feature-specific extent values
          not limited to a specific language system may be specified
          in the DefaultMinMax table. However, extent values used for
          a specific language system require a BaseLangSysRecord and a
          MinMax table. In addition to specifying coordinate data, the
          MinMax table must contain offsets to FeatMinMaxRecords that
          define the feature-specific min/max data.</p><p role="">A BaseScript table has four components:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">An offset to a BaseValues table (BaseValues). If no
              baseline data is defined for the script or the
              corresponding BaseTagList is set to NULL, the offset to
              the BaseValues table may be set to NULL.</p></li><li role="" class="listitem"><p role="">An offset to the DefaultMinMax table. If no default
              min/max extent data is defined for the script, this
              offset may be set to NULL.</p></li><li role="" class="listitem"><p role="">An array of BaseLangSysRecords (BaseLangSysRecord).
              The individual records stored in the BaseLangSysRecord
              array are listed alphabetically by
              BaseLangSysTag.</p></li><li role="" class="listitem"><p role="">A count of the BaseLangSysRecords included
              (BaseLangSysCount). If no language system or
              language-specific feature min/max values are defined,
              the BaseLangSysCount may be set to zero (0).</p></li></ul></div><p role="">Example 2 at the end of this chapter shows a sample
          BaseScript table.</p><div class="table"><a name="idm114631455776"></a><p class="title"><strong>Table 22.6. BaseScript Table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseScript Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">BaseValues</td><td role="">Offset to BaseValues table-from beginning of
              BaseScript table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">DefaultMinMax</td><td role="">Offset to MinMax table- from beginning of
              BaseScript table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BaseLangSysCount</td><td role="">Number of BaseLangSysRecords defined-may be
              zero (0)</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">BaseLangSysRecord [BaseLangSysCount]</td><td role="">Array of BaseLangSysRecords-in alphabetical
              order by BaseLangSysTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A BaseLangSysRecord defines min/max extents for a
          language system or a language-specific feature. Each record
          contains an identification tag for the language system
          (BaseLangSysTag) and an offset to a MinMax table (MinMax)
          that defines extent coordinate values for the language
          system and references feature-specific extent data.</p><p role="">Example 2 at the end of this chapter shows a
          BaseLangSysRecord.</p><div class="table"><a name="idm114631446256"></a><p class="title"><strong>Table 22.7. BaseLangSysRecord</strong></p><div class="table-contents"><table role="" class="table" summary="BaseLangSysRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">BaseLangSysTag</td><td role="">4-byte language system identification
              tag</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MinMax</td><td role="">Offset to MinMax table-from beginning of
              BaseScript table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631440512"></a>BaseValues Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.13.1"></a>Specification</h3></div></div></div><p role="">A BaseValues table lists the coordinate positions of all
          baselines named in the BaselineTag array of the
          corresponding BaseTagList and identifies a default baseline
          for a script.</p><p role="">Note: When the offset to the corresponding BaseTagList
          is NULL, a BaseValues table is not needed. However, if the
          offset is not NULL, then each script must specify coordinate
          positions for all baselines named in the BaseTagList.</p><p role="">The default baseline, one per script, is the baseline
          used to lay out and align the glyphs in the script. The
          DefaultIndex in the BaseValues table identifies the default
          baseline with a value that equals the array index position
          of the corresponding tag in the BaselineTag array.</p><p role="">For example, the Han and Latin scripts use different
          baselines to align text. If a font supports both of these
          scripts, the BaselineTag array in the BaseTagList of the
          HorizAxis table will contain two tags, listed
          alphabetically: "ideo" in BaselineTag[0] for the Han
          ideographic baseline, and "romn" in BaselineTag[1] for the
          Latin baseline. The BaseValues table for the Latin script
          will specify the roman baseline as the default, so the
          DefaultIndex in the BaseValues table for Latin will be "1"
          to indicate the roman baseline tag. In the BaseValues table
          for the Han script, the DefaultIndex will be "0" to indicate
          the ideographic baseline tag.</p><p role="">Two or more scripts may share a default baseline. For
          instance, if the font described above also supports the
          Cyrillic script, the BaselineTag array does not need a
          baseline tag for Cyrillic because Cyrillic and Latin share
          the same baseline. The DefaultIndex defined in the
          BaseValues table for the Cyrillic script will specify "1" to
          indicate the roman baseline tag, listed in the second
          position in the BaselineTag array.</p><p role="">In addition to identifying the DefaultIndex, the
          BaseValues table contains an offset to an array of BaseCoord
          tables (BaseCoord) that list the coordinate positions for
          all baselines, including the default baseline, named in the
          associated BaselineTag array. One BaseCoord table is defined
          for each baseline. The BaseCoordCount defines the total
          number of BaseCoord tables, which must equal the number of
          baseline tags listed in BaseTagCount in the
          BaseTagList.</p><p role="">Each baseline coordinate is defined as a single X or Y
          value in design units measured from the zero position on the
          relevant X or Y axis. For example, a BaseCoord table defined
          in the HorizAxis table will contain a Y value because
          horizontal baselines are positioned vertically. BaseCoord
          values may be negative. Each script may assign a different
          coordinate to each baseline.</p><p role="">Offsets to each BaseCoord table are stored in a
          BaseCoord array within the BaseValues table. The order of
          the stored offsets corresponds to the order of the tags
          listed in the BaselineTag array of the BaseTagList. In other
          words, the first position in the BaseCoord array will define
          the offset to the BaseCoord table for the first baseline
          named in the BaselineTag array, the second position will
          define the offset to the BaseCoord table for the second
          baseline named in the BaselineTag array, and so on.</p><p role="">Example 3 at the end of the chapter has two parts, one
          that shows a BaseValues table and one that shows a chart
          with different baseline positions defined for several
          scripts.</p><div class="table"><a name="idm114631430944"></a><p class="title"><strong>Table 22.8. BaseValues table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseValues table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">DefaultIndex</td><td role="">Index number of default baseline for this
              script-equals index position of baseline tag in
              BaselineArray of the BaseTagList</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BaseCoordCount</td><td role="">Number of BaseCoord tables defined-should
              equal BaseTagCount in the BaseTagList</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">BaseCoord [BaseCoordCount]</td><td role="">Array of offsets to BaseCoord-from beginning
              of BaseValues table-order matches BaselineTag array in
              the BaseTagList</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631423536"></a>The MinMax Table and FeatMinMaxRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.14.1"></a>Specification</h3></div></div></div><p role="">The MinMax table specifies extents for scripts and
          language systems. It also contains an array of
          FeatMinMaxRecords used to define feature-specific
          extents.</p><p role="">Both the MinMax table and the FeatMinMaxRecord define
          offsets to two BaseCoord tables: one that defines the
          mimimum extent value (MinCoord), and one that defines the
          maximum extent value (MaxCoord). Each extent value is a
          single X or Y value, depending upon the text direction, and
          is specified in design units. Coordinate values may be
          negative.</p><p role="">Different tables define the min/max extent values for
          scripts, language systems, and features:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Min/max extent values for a script are defined in
              the DefaultMinMax table, referenced in a BaseScript
              table.</p></li><li role="" class="listitem"><p role="">Within the DefaultMinMax table, FeatMinMaxRecords
              can specify extent values for features that apply to the
              entire script.</p></li><li role="" class="listitem"><p role="">Min/max extent values for a language system are
              defined in the MinMax table, referenced in a
              BaseLangSysRecord.</p></li><li role="" class="listitem"><p role="">FeatMinMaxRecords can be defined within the MinMax
              table to specify extent values for features applied
              within a language system.</p></li></ul></div><p role="">In a FeatMinMaxRecord, the MinCoord and MaxCoord tables
          specify the minimum and maximum coordinate values for the
          feature, and a FeatureTableTag defines a 4-byte feature
          identification tag. The FeatureTableTag must match the tag
          used to identify the feature in the FeatureList of the
          <a role="" class="link" href="chapter.GSUB.md" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>
          table.</p><p role="">Each feature that exceeds the default min/max values
          requires a FeatMinMaxRecord. All FeatMinMaxRecords are
          listed alphabetically by FeatureTableTag in an array
          (FeatMinMaxRecord) within the MinMax table. FeatMinMaxCount
          defines the total number of FeatMinMaxRecords.</p><p role="">Text-processing clients should use the following
          procedure to access the script, language system, and
          feature-specific extent data:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Determine script extents in relation to the text
              content.</p></li><li role="" class="listitem"><p role="">Select language-specific extent values with respect
              to the language system in use.</p></li><li role="" class="listitem"><p role="">Have the application or user choose feature-specific
              extent values.</p></li><li role="" class="listitem"><p role="">If no extent values are defined for a language
              system or for language-specific features, use the
              default min/max extent values for the script.</p></li></ul></div><p role="">Example 4 at the end of this chapter has two parts. One
          shows MinMax tables and a FeatMinMaxRecord for different
          script, language system, and feature extents. The second
          part shows how to define these tables when a language system
          needs feature-specific extent values for an obscure feature,
          but otherwise the language system and script extent values
          match.</p><div class="table"><a name="idm114631407488"></a><p class="title"><strong>Table 22.9. MinMax table</strong></p><div class="table-contents"><table role="" class="table" summary="MinMax table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Offset</td><td role="">MinCoord</td><td role="">Offset to BaseCoord table-defines minimum
              extent value-from the beginning of MinMax table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MaxCoord</td><td role="">Offset to BaseCoord table-defines maximum
              extent value-from the beginning of MinMax table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">FeatMinMaxCount</td><td role="">Number of FeatMinMaxRecords-may be zero
              (0)</td><td class="auto-generated"> </td></tr><tr><td role="">struct</td><td role="">FeatMinMaxRecord [FeatMinMaxCount]</td><td role="">Array of FeatMinMaxRecords-in alphabetical
              order, by FeatureTableTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm114631399120"></a><p class="title"><strong>Table 22.10. FeatMinMaxRecord</strong></p><div class="table-contents"><table role="" class="table" summary="FeatMinMaxRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Tag</td><td role="">FeatureTableTag</td><td role="">4-byte feature identification tag-must match
              FeatureTag in FeatureList</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MinCoord</td><td role="">Offset to BaseCoord table-defines minimum
              extent value-from beginning of MinMax table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">MaxCoord</td><td role="">Offset to BaseCoord table-defines maximum
              extent value-from beginning of MinMax table-may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631391760"></a>BaseCoord Tables</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.15.1"></a>Specification</h3></div></div></div><p role="">Within the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table, a BaseCoord table defines
          baseline and min/max extent values. Each BaseCoord table
          defines one X or Y value:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">If defined within the HorizAxis table, then the
              BaseCoord table contains a Y value.</p></li><li role="" class="listitem"><p role="">If defined within the VertAxis table, then the
              BaseCoord table contains an X value.</p></li></ul></div><p role="">All values are defined in design units, which typically
          are scaled and rounded to the nearest integer when scaling
          the glyphs. Values may be negative.</p><p role="">Three formats available for BaseCoord table data define
          single X or Y coordinate values in design units. Two of the
          formats also support fine adjustments to the X or Y values
          based on a contour point or a Device table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631384992"></a>BaseCoord Format 1</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.16.1"></a>Specification</h3></div></div></div><p role="">The first BaseCoord format (BaseCoordFormat1) consists
          of a format identifier, followed by a single design unit
          coordinate that specifies the BaseCoord value. This format
          has the benefits of small size and simplicity, but the
          BaseCoord value cannot be hinted for fine adjustments at
          different sizes or device resolutions.</p><p role="">Example 5 at the end of the chapter shows a sample of a
          BaseCoordFormat1 table.</p><div class="table"><a name="idm114631382000"></a><p class="title"><strong>Table 22.11. BaseCoordFormat1 table: Design units only</strong></p><div class="table-contents"><table role="" class="table" summary="BaseCoordFormat1 table: Design units only" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseCoordFormat</td><td role="">Format identifier-format = 1</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">Coordinate</td><td role="">X or Y value, in design units</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631376352"></a>BaseCoord Format 2</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.17.1"></a>Specification</h3></div></div></div><p role="">The second BaseCoord format (BaseCoordFormat2) specifies
          the BaseCoord value in design units, but also supplies a
          glyph index and a contour point for reference. During font
          hinting, the contour point on the glyph outline may move.
          The point's final position after hinting provides the final
          value for rendering a given font size.</p><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: Glyph positioning operations defined in the
            <a role="" class="link" href="chapter.GPOS.md" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table do not affect the point's
            final position.</p></blockquote></div><p role="">Example 6 shows a sample of a BaseCoordFormat2
          table.</p><div class="table"><a name="idm114631371888"></a><p class="title"><strong>Table 22.12. BaseCoordFormat2 table: Design units plus contour point</strong></p><div class="table-contents"><table role="" class="table" summary="BaseCoordFormat2 table: Design units plus contour point" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseCoordFormat</td><td role="">Format identifier-format = 2</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">Coordinate</td><td role="">X or Y value, in design units</td><td class="auto-generated"> </td></tr><tr><td role="">GlyphID</td><td role="">ReferenceGlyph</td><td role="">GlyphID of control glyph</td><td class="auto-generated"> </td></tr><tr><td role="">uint16</td><td role="">BaseCoordPoint</td><td role="">Index of contour point on the
              ReferenceGlyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631363344"></a>BaseCoord Format 3</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.18.1"></a>Specification</h3></div></div></div><p role="">The third BaseCoord format (BaseCoordFormat3) also
          specifies the BaseCoord value in design units, but it uses a
          Device table rather than a contour point to adjust the
          value. This format offers the advantage of fine-tuning the
          BaseCoord value for any font size and device resolution.
          (For more information about Device tables, see the chapter,
          Common Table Formats.)</p><p role="">Example 7 at the end of this chapter shows a sample of a
          BaseCoordFormat3 table.</p><div class="table"><a name="idm114631360304"></a><p class="title"><strong>Table 22.13. BaseCoordFormat3 table: Design units plus Device table</strong></p><div class="table-contents"><table role="" class="table" summary="BaseCoordFormat3 table: Design units plus Device table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">uint16</td><td role="">BaseCoordFormat</td><td role="">Format identifier-format = 3</td><td class="auto-generated"> </td></tr><tr><td role="">int16</td><td role="">Coordinate</td><td role="">X or Y value, in design units</td><td class="auto-generated"> </td></tr><tr><td role="">Offset</td><td role="">DeviceTable</td><td role="">Offset to Device table for X or Y
              value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631353168"></a>BASE Table Examples</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.19.1"></a>Specification</h3></div></div></div><p role="">The rest of this chapter describes and illustrates
          examples of all the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> tables. All the
          examples reflect unique parameters described below, but the
          samples provide a useful reference for building tables
          specific to other situations.</p><p role="">Most of the examples have three columns showing hex
          data, source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631349120"></a>Example 1: BASE Header Table, Axis Table, BaseTagList
        Table, BaseScriptList Table, and BaseScriptRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.20.1"></a>Specification</h3></div></div></div><p role="">Example 1 describes a sample font that contains four
          scripts: Cyrillic, Devanagari, Han, and Latin. All four
          scripts are rendered horizontally; only one script, Han, is
          rendered vertically. As a result, the
          <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> header gives offsets to two Axis
          tables: HorizAxis and VertAxis. Example 1 only shows data
          defined in the HorizAxis table.</p><p role="">In the HorizAxis table, the BaseScriptList enumerates
          all four scripts. The BaseTagList table names three
          horizontal baselines for rendering these scripts: hanging,
          ideographic, and roman. The hanging baseline is the default
          for Devanagari, the ideographic baseline is the default for
          Han, and the roman baseline is the default for both Latin
          and Cyrillic.</p><p role="">The VertAxis table (not shown) would be defined
          similarly: its BaseScriptList would enumerate one script,
          Han, and its BaseTagList would specify the vertically
          centered baseline for rendering the Han script.</p><div class="table"><a name="idm114631344432"></a><p class="title"><strong>Table 22.14. Example 1</strong></p><div class="table-contents"><table role="" class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role=""><span role="" class="emphasis"><em>BASEHeader</em></span></td><td role=""> </td></tr><tr><td role=""> </td><td role="">TheBASEHeader</td><td role=""><a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table header definition</td></tr><tr><td role="">00010000</td><td role="">0x00010000</td><td role="">Version</td></tr><tr><td role="">0008</td><td role="">HorizontalAxisTable</td><td role="">Offset to HorizAxis table</td></tr><tr><td role="">010C</td><td role="">VerticalAxisTable</td><td role="">Offset to VertAxis tabl</td></tr><tr><td role=""> </td><td role="">Axis</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizontalAxisTable</td><td role="">Axis table definition</td></tr><tr><td role="">0004</td><td role="">HorizBaseTagList</td><td role="">Offset to BaseTagList table</td></tr><tr><td role="">0012</td><td role="">HorizBaseScriptList</td><td role="">Offset to BaseScriptList tabl</td></tr><tr><td role=""> </td><td role="">BaseTagList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizBaseTagList</td><td role="">BaseTagList table definition</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">BaseTagCount</td></tr><tr><td role="">68616E67</td><td role="">"hang"</td><td role="">BaselineTag[0], in alphabetical order</td></tr><tr><td role="">6964656F</td><td role="">"ideo"</td><td role="">BaselineTag[1]</td></tr><tr><td role="">726F6D6E</td><td role="">"romn"</td><td role="">BaselineTag[2]</td></tr><tr><td role=""> </td><td role="">BaseScriptList</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizBaseScriptList</td><td role="">BaseScriptList table definition</td></tr><tr><td role="">0004</td><td role="">4</td><td role="">BaseScriptCount BaseScriptRecord[0], in
                  alphabetical order</td></tr><tr><td role="">6379726C</td><td role="">"cyrl"</td><td role="">BaseScriptTag for Cyrillic script</td></tr><tr><td role="">001A</td><td role="">HorizCyrillicBaseScriptTable</td><td role="">Offset to BaseScript table for Cyrillic script
                  BaseScriptRecord[1]</td></tr><tr><td role="">6465766E</td><td role="">"devn"</td><td role="">BaseScriptTag for Devanagari script</td></tr><tr><td role="">0060</td><td role="">HorizDevanagariBaseScriptTable</td><td role="">Offset to BaseScript table for Devanagari
                  script BaseScriptRecord[2]</td></tr><tr><td role="">68616E69</td><td role="">"hani"</td><td role="">BaseScriptTag for Han script</td></tr><tr><td role="">008A</td><td role="">HorizHanBaseScriptTable</td><td role="">Offset to BaseScript table for Han script
                  BaseScriptRecord[3]</td></tr><tr><td role="">6C61746E</td><td role="">"latn"</td><td role="">BaseScriptTag for Latin script</td></tr><tr><td role="">00B4</td><td role="">HorizLatinBaseScriptTable</td><td role="">Offset to BaseScript table for Latin
                  script</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631305408"></a>Example 2: BaseScript Table and BaseLangSysRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.21.1"></a>Specification</h3></div></div></div><p role="">Example 2 shows the BaseScript table and
          BaseLangSysRecord for the Cyrillic script, one of the four
          scripts included in the sample font described in Example 1.
          The BaseScript table specifies offsets to tables that
          contain the baseline and min/max extent data for Cyrillic.
          (The BaseScript tables for the other three scripts in the
          font would be defined similarly.) Again, the table specifies
          only the horizontal text-layout information.</p><p role="">The HorizCyrillicBaseValues table contains the baseline
          information for the script, and the
          HorizCyrillicDefaultMinMax table contains the default script
          extents. In addition, a BaseLangSysRecord defines min/max
          extent data for the Russian language system.</p><div class="table"><a name="idm114631302016"></a><p class="title"><strong>Table 22.15. Example 2</strong></p><div class="table-contents"><table role="" class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseScript</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicBaseScriptTable</td><td role="">BaseScript table definition for Cyrillic
                  script</td></tr><tr><td role="">000C</td><td role="">HorizCyrillicBaseValuesTable</td><td role="">Offset to BaseValues table</td></tr><tr><td role="">0022</td><td role="">HorizCyrillicDefaultMinMaxTable</td><td role="">Offset to DefaultMinMax table default script
                  extents</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseLangSysCount, feature-specific extents
                  BaseLangSysRecord[0] in alphabetical order</td></tr><tr><td role="">52555320</td><td role="">"RUS "</td><td role="">BaseLangSysTag, Russian language system</td></tr><tr><td role="">0030</td><td role="">HorizRussianMinMaxTable</td><td role="">Offset to MinMax table feature-specific
                  extents</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631289360"></a>Example 3: BaseValues Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.22.1"></a>Specification</h3></div></div></div><p role="">Example 3 extends the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table
          definition for the Cyrillic script described in Examples 1
          and 2. It contains two parts:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Example 3A illustrates a fully defined BaseValues
              table for Cyrillic. The table includes the corresponding
              BaseCoord table definitions.</p></li><li role="" class="listitem"><p role="">Example 3B shows two different sets of baseline
              values that can be defined for each of the four scripts
              in the sample font.</p></li></ul></div><p role="">The examples show only horizontal text-layout data, and
          the font uses 2,048 design units/em.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114631283200"></a>Example 3A: BaseValues Table for Cyrillic</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.23.1"></a>Specification</h3></div></div></div><p role="">The BaseValues table of Example 3A identifies the
          default baseline for Cyrillic and specifies coordinate
          positions for each baseline listed in the BaseTagList shown
          in Example 1:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The hanging baseline is the default for the
              Devanagari script, and it has the highest baseline
              position.</p></li><li role="" class="listitem"><p role="">The ideographic baseline is the default for the Han
              script, and it has the lowest baseline position.</p></li><li role="" class="listitem"><p role="">The roman baseline is the default for both the Latin
              and Cyrillic scripts, and its position lies between the
              hanging and ideographic baselines.</p></li></ul></div><div class="table"><a name="idm114631277664"></a><p class="title"><strong>Table 22.16. Example 3A</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3A" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseValues</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicBaseValuesTable</td><td role="">BaseValues table definition for Cyrillic
                  script</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">DefaultIndex, roman baseline BaselineTag
                  index</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">BaseCoordCount, equals BaseTagCount</td></tr><tr><td role="">000A</td><td role="">HorizHangingBaseCoordForCyrl</td><td role="">Offset to BaseCoord[0] table hanging baseline
                  coordinate, order matches order of BaselineTag array
                  in BaseTagList</td></tr><tr><td role="">000E</td><td role="">HorizideographicBaseCoordForCyrl</td><td role="">Offset to BaseCoord[1] table ideographic
                  baseline coordinate</td></tr><tr><td role="">0012</td><td role="">HorizromanBaseCoordForCyrl</td><td role="">Offset to BaseCoord[2] table roman baseline
                  coordinat</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizHangingBaseCoordForCyrl</td><td role="">BaseCoord table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">05DC</td><td role="">1500</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizideographicBaseCoordForCyrl</td><td role="">BaseCoord table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">FEE0</td><td role="">-288</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizromanBaseCoordinateForCyrl</td><td role="">BaseCoord table definition</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat, design units only</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">Coordinate, Y value, in design units</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639589424"></a>Example 3B: Baseline Values for Four Scripts</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.24.1"></a>Specification</h3></div></div></div><p role="">Example 3B shows two tables that contain baseline values
          for each of the four scripts in the sample font described in
          Example 1:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The first table shows what might happen if the
              baseline values in all four scripts are designed
              consistently. Their respective BaseValues tables list
              identical baseline values with the roman baseline
              positioned at a Y value of zero (0), the ideographic
              baseline at 1500, and the hanging baseline at
              -288.</p></li><li role="" class="listitem"><p role="">The second table shows what might happen if the
              baseline values in the scripts are designed differently
              with the default baseline for each script at the zero
              (0) coordinate.</p></li></ul></div><p role="">Either method of assigning baseline values can be used
          in the <a role="" class="link" href="chapter.BASE.md" title="Chapter 22. BASE - Baseline Table">BASE</a> table.</p><div class="table"><a name="idm114639583472"></a><p class="title"><strong>Table 22.17. Example 3B: Identical baseline values</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3B: Identical baseline values" border="1"><colgroup><col width="10pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/></colgroup><thead><tr><th role="">Baseline type</th><th role="">Han</th><th role="">Latin</th><th role="">Cyrillic</th><th role="">Devanagari</th></tr></thead><tbody><tr><td role="">hanging</td><td role="">1500</td><td role="">1500</td><td role="">1500</td><td role="">1500</td></tr><tr><td role="">roman</td><td role="">0</td><td role="">0</td><td role="">0</td><td role="">0</td></tr><tr><td role="">ideographic</td><td role="">-288</td><td role="">-288</td><td role="">-288</td><td role="">-288</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm114639569664"></a><p class="title"><strong>Table 22.18. Example 3B: Assigned baseline values with default
            baselines at 0</strong></p><div class="table-contents"><table role="" class="table" summary="Example 3B: Assigned baseline values with default&#10;            baselines at 0" border="1"><colgroup><col width="10pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/></colgroup><thead><tr><th role="">Baseline type</th><th role="">Han</th><th role="">Latin</th><th role="">Cyrillic</th><th role="">Devanagari</th></tr></thead><tbody><tr><td role="">hanging</td><td role="">1788</td><td role="">1500</td><td role="">1500</td><td role="">0</td></tr><tr><td role="">roman</td><td role="">288</td><td role="">0</td><td role="">0</td><td role="">-1500</td></tr><tr><td role="">ideographic</td><td role="">0</td><td role="">-288</td><td role="">-288</td><td role="">-1788</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639555280"></a>Example 4: MinMax Table and FeatMinMaxRecord</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.25.1"></a>Specification</h3></div></div></div><p role="">Example 4 shows MinMax table and FeatMinMaxRecord
          definitions for the same Cyrillic script described in the
          previous example. It contains two parts:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Example 4A defines tables with different script,
              language system, and feature extents.</p></li><li role="" class="listitem"><p role="">Example 4B shows these same table definitions
              written when the language system extents match the
              script extents, but an obscure feature of the language
              system requires feature-specific extents if that feature
              is implemented.</p></li></ul></div><p role="">The examples show only horizontal text-layout data, and
          the font uses 2,048 design units/em.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639549568"></a>Example 4A: Min/Max Extents For Cyrillic Script, Russian
        Language, and Russian Feature</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.26.1"></a>Specification</h3></div></div></div><p role="">Example 4A shows two MinMax tables and a
          FeatMinMaxRecord for the Cyrillic script, along with sample
          BaseCoord tables. Only the MinCoord extent data is
          included.</p><p role="">The DefaultMinMax table defines the default minimum and
          maximum extents for the Cyrillic script. Another MinMax
          table defines language-specific min/max extents for the
          Russian language system to accommodate the height and width
          of certain glyphs used in Russian. Also, a FeatMinMaxRecord
          defines min/max extents for a single feature in the Russian
          language system that substitutes a tall integral math symbol
          when required.</p><div class="table"><a name="idm114639546272"></a><p class="title"><strong>Table 22.19. Example 4A</strong></p><div class="table-contents"><table role="" class="table" summary="Example 4A" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">MinMax</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicDefaultMinMaxTable</td><td role="">DefaultMinMax table definition, Cyrillic
                  script</td></tr><tr><td role="">0006</td><td role="">HorizCyrillicMinCoordTable</td><td role="">MinCoord offset to BaseCoord table</td></tr><tr><td role="">000A</td><td role="">HorizCyrillicMaxCoordTable</td><td role="">MaxCoord offset to BaseCoord table</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">FeatMinMaxCount no default feature extents
                  FeatMinMaxRecord[], no FeatMinMaxRecord</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicMinCoordTable</td><td role="">BaseCoord table definition, default Cyrillic
              Min extent coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat, design units only</td></tr><tr><td role="">FF38</td><td role="">-200</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicMaxCoordTable</td><td role="">BaseCoord table
                  definition default Cyrillic Max extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat, design units only</td></tr><tr><td role="">0674</td><td role="">1652</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">MinMax</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianMinMaxTable</td><td role="">MinMax table definition
                  Russian language extents</td></tr><tr><td role="">000E</td><td role="">HorizRussianLangSysMinCoordTable</td><td role="">MinCoord Offset to BaseCoord table</td></tr><tr><td role="">0012</td><td role="">HorizRussianLangSysMaxCoordTable</td><td role="">MaxCoord Offset to BaseCoord table</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">FeatMinMaxCount FeatMinMaxRecord[0] in
                  alphabetical order</td></tr><tr><td role="">696E7467</td><td role="">"intg"</td><td role="">FeatureTableTag integral math symbol Feature
                  must be same as Tag in FeatureList</td></tr><tr><td role="">0016</td><td role="">HorizRussianFeatureMinCoordTable</td><td role="">MinCoord Offset to BaseCoord table</td></tr><tr><td role="">001A</td><td role="">HorizRussianFeatureMaxCoordTable</td><td role="">MaxCoord Offset to BaseCoord tabl</td></tr><tr><td role=""> </td><td role="">HorizRussianLangSys</td><td role=""> </td></tr><tr><td role=""> </td><td role="">MinCoordTable</td><td role="">BaseCoord table definition
                  Russian language min extent coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">FF08</td><td role="">-248</td><td role="">Coordinate Y value, in design units, increased
                  Min extent beyond default Cyrillic min exten</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianLangSysMaxCoordTable</td><td role="">BaseCoord
                  table definition Russian language feature Max extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">06A4</td><td role="">1700</td><td role="">Coordinate Y value, in design units increased
                  max extent beyond default Cyrillic max exten</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianFeatureMinCoordTable</td><td role="">BaseCoord
                  table definition Russian language Min extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat Design Units Only</td></tr><tr><td role="">FED8</td><td role="">-296</td><td role="">Coordinate Y value, in design units, increased
                  Min extent beyond default Cyrillic script and
                  Russian language min extent</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianFeatureMaxCoordTable</td><td role="">BaseCoord
                  table definition Russian language feature Max extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">06D8</td><td role="">1752</td><td role="">Coordinate Y value, in design units increased
                  Max extent beyond default Cyrillic script and
                  Russian language max extents</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639491808"></a>Example 4B: Min/Max Extents For Cyrillic Script and
        Russian Feature</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.27.1"></a>Specification</h3></div></div></div><p role="">A particular language system does not need to define
          min/max extent coordinates if its extents match the default
          extents defined for the script. However, an obscure or
          infrequently used feature within the language system may
          require feature-specific extent values for proper
          rendering.</p><p role="">Example 4B shows the MinMax and FeatMinMaxRecord table
          definitions for this situation. The example also includes a
          BaseScript table, but not a BaseValues tables since it is
          not relevant in this example. The example shows horizontal
          text layout extents for the Cyrillic script and
          feature-specific extents for one feature in the Russian
          language system. Much of the data is repeated from Example
          4A and modified here for comparison.</p><p role="">The BaseScript table includes a DefaultMinMax table for
          the Cyrillic script and a BaseLangSysRecord that defines a
          BaseLangSysTag and an offset to a MinMax table for the
          Russian language. The MinMax table includes a
          FeatMinMaxRecord and specifies a FeatMinMaxCount, but both
          the MinCoord and MaxCoord offsets in the MinMax table are
          set to NULL since no language-specific extent values are
          defined for Russian. The FeatMinMaxRecord defines the
          min/max coordinates for the Russian feature and specifies
          the correct FeatureTableTag.</p><div class="table"><a name="idm114639487392"></a><p class="title"><strong>Table 22.20. Example 4B</strong></p><div class="table-contents"><table role="" class="table" summary="Example 4B" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseScript</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicBaseScriptTable</td><td role="">BaseScript table
                  definition Cyrillic script</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to BaseValues table</td></tr><tr><td role="">000C</td><td role="">HorizCyrillicDefault MinMaxTable</td><td role="">offset to DefaultMinMax table for default
                  script extents</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseLangSysCount</td></tr><tr><td role=""> </td><td role=""> </td><td role="">BaseLangSysRecord[0] for Russian
                  feature-specific-extents</td></tr><tr><td role="">52555320</td><td role="">"RUS</td><td role="">" BaseLangSysTag = Russian</td></tr><tr><td role="">001A</td><td role="">HorizRussianMinMaxTable</td><td role="">offset to MinMax table for feature-specific
                  extent</td></tr><tr><td role=""> </td><td role="">MinMax</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicDefaultMinMaxTable</td><td role="">DefaultMinMax
                  table definition Cyrillic script</td></tr><tr><td role="">0006</td><td role="">HorizCyrillicMinCoordTable</td><td role="">MinCoord offset to BaseCoord table</td></tr><tr><td role="">000A</td><td role="">HorizCyrillicMaxCoordTable</td><td role="">MaxCoord offset to BaseCoord table</td></tr><tr><td role="">0000</td><td role="">0</td><td role="">FeatMinMaxCount, no default feature extents
                  FeatMinMaxRecord[], no FeatMinMaxRecords</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicMinCoordTable</td><td role="">BaseCoord table
                  definition default Cyrillic Min extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">FF38</td><td role="">-200</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizCyrillicMaxCoordTable</td><td role="">BaseCoord table
                  definition default Cyrillic Min extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">0674</td><td role="">1652</td><td role="">Coordinate Y value, in design unit</td></tr><tr><td role=""> </td><td role="">MinMax</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianMinMaxTable</td><td role="">MinMax table definition
                  for Russian feature no extent differences for
                  Russian language itself</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to Min BaseCoord table not defined,
                  matches default</td></tr><tr><td role="">0000</td><td role="">NULL</td><td role="">offset to Max BaseCoord table not defined,
                  matches default</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">FeatMinMaxCount, FeatMinMaxRecord[0] in
                  alphabetical order</td></tr><tr><td role="">696E7467</td><td role="">"intg"</td><td role="">FeatureTableTag integral math sign Feature must
                  be same as Tag in FeatureList</td></tr><tr><td role="">000E</td><td role="">HorizRussianFeatureMinCoordTable</td><td role="">MinCoord offset to BaseCoord table</td></tr><tr><td role="">0012</td><td role="">HorizRussianFeatureMaxCoordTable</td><td role="">MaxCoord offset to BaseCoord tabl</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianFeatureMinCoordTable</td><td role="">BaseCoord
                  table definition Russian Feature Min extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat, design units only</td></tr><tr><td role="">FED8</td><td role="">-296</td><td role="">Coordinate Y value, in design units increased
                  Min extent beyond default Cyrillic Min
                  extent</td></tr><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizRussianFeatureMaxCoordTable</td><td role="">BaseCoord
                  table definition, Russian feature Max extent
                  coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat design units only</td></tr><tr><td role="">06D8</td><td role="">1752</td><td role="">Coordinate Y value, in design units, increased
                  Max extent beyond default Cyrillic Max
                  extent</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639433040"></a>Example 5: BaseCoordFormat1 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.28.1"></a>Specification</h3></div></div></div><p role="">Example 5 illustrates BaseCoordFormat1, which specifies
          single coordinate values in design units only. The font uses
          2,048 design units/em. The example defines the default
          minimum extent coordinate for a math script.</p><div class="table"><a name="idm114639430608"></a><p class="title"><strong>Table 22.21. Example 5</strong></p><div class="table-contents"><table role="" class="table" summary="Example 5" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseCoordFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizMathMinCoordTable</td><td role="">Definition of BaseCoord
                  table for Math Min coordinate</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">BaseCoordFormat, design units only</td></tr><tr><td role="">FEE8</td><td role="">-280</td><td role="">Coordinate Y value, in design units</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639422400"></a>Example 6: BaseCoordFormat2 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.29.1"></a>Specification</h3></div></div></div><p role="">Example 6 illustrates the BaseCoord Format 2. Like
          Example 5, it specifies the minimum extent coordinate for a
          math script. With this format, the coordinate value depends
          on the final position of a specific contour point on one
          glyph, the integral math symbol, after hinting. Again, the
          value is in design units (2,048 units/em).</p><div class="table"><a name="idm114639419840"></a><p class="title"><strong>Table 22.22. Example 6</strong></p><div class="table-contents"><table role="" class="table" summary="Example 6" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseCoordFormat2</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizMathMinCoordTable</td><td role="">BaseCoord table
                  definition for Math Min coordinate</td></tr><tr><td role="">0002</td><td role="">2</td><td role="">BaseCoordFormat design units plus contour
                  point</td></tr><tr><td role="">FEE8</td><td role="">-280</td><td role="">Coordinate Y value, in design units</td></tr><tr><td role="">0128</td><td role="">IntegralSignGlyphID</td><td role="">ReferenceGlyph math integral sign</td></tr><tr><td role="">0043</td><td role="">67</td><td role="">BaseCoordPoint glyph contour point
                  index</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114639408672"></a>Example 7: BaseCoordFormat3 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.22.30.1"></a>Specification</h3></div></div></div><p role="">Example 7 illustrates the BaseCoord Format 3. Like
          Examples 5 and 6, it specifies the minimum extent coordinate
          for a math script in design units (2,048 units/em). This
          format, however, uses a Device table to modify the
          coordinate value for the point size and resolution of the
          output font. Here, the Device table defines pixel
          adjustments for font sizes from 11 ppem to 15 ppem. The
          adjustments add one pixel at each size.</p><div class="table"><a name="idm114639406000"></a><p class="title"><strong>Table 22.23. Example 7</strong></p><div class="table-contents"><table role="" class="table" summary="Example 7" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">HexData</th><th role="">Source</th><th role="">Comment</th></tr></thead><tbody><tr><td role=""> </td><td role="">BaseCoordFormat3</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizMathMinCoordTable</td><td role="">BaseCoord table
                  definition for Math Min coordinate</td></tr><tr><td role="">0003</td><td role="">3</td><td role="">BaseCoordFormat design units plus device
                  table</td></tr><tr><td role=""> </td><td role="">-280</td><td role="">Coordinate Y value, in design
                  units</td></tr><tr><td role="">000C</td><td role="">HorizMathMinCoordDeviceTable</td><td role="">Offset to Device tabl</td></tr><tr><td role=""> </td><td role="">DeviceTableFormat1</td><td role=""> </td></tr><tr><td role=""> </td><td role="">HorizMathMinCoordDeviceTable</td><td role="">Device table
                  definition for MinCoord</td></tr><tr><td role="">000B</td><td role="">11</td><td role="">StartSize -11 ppem</td></tr><tr><td role="">000F</td><td role="">15</td><td role="">EndSize -15 ppem</td></tr><tr><td role="">0001</td><td role="">1</td><td role="">DeltaFormat signed 2 bit value, 8 values per
                  uint16</td></tr><tr><td role=""> </td><td role="">1</td><td role="">Increase 11ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">Increase 12ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">Increase 13ppem by 1 pixel</td></tr><tr><td role=""> </td><td role="">1</td><td role="">Increase 14ppem by 1 pixel</td></tr><tr><td role="">5540</td><td role="">1</td><td role="">Increase 15ppem by 1 pixel</td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>