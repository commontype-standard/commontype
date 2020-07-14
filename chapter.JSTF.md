<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.JSTF"></a>Chapter 27. JSTF - The Justification Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17078"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.1.1"></a>Specification</h4></div></div></div><p>The Justification table (<a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>)
        provides font developers with additional control over glyph
        substitution and positioning in justified text.
        Text-processing clients now have more options to expand or
        shrink word and glyph spacing so text fills the specified line
        length.</p><p>When justifying text, the text-processing client
        distributes the characters in each line to completely fill the
        specified line length. Whether removing space to fit more
        characters in the line or adding more space to spread the
        characters, justification can produce large gaps between
        words, cramped or extended glyph spacing, uneven line break
        patterns, and other jarring visual effects. For
        example:</p><div class="figure"><a name="idm17085"></a><p class="title"><strong>Figure 27.1. Figure 6a. Poorly justified text</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig6a.gif" alt="Figure 6a. Poorly justified text"/></div></div></div><br class="figure-break"/><p>To offset these effects, text-processing clients have
        used justification algorithms that redistribute the space with
        a series of glyph spacing adjustments that progress from least
        to most obvious. Typically, the client will begin by expanding
        or compressing the space between words. If these changes
        aren't enough or look distracting, the client might hyphenate
        the word at the end of the line or adjust the space between
        glyphs in one or more lines.</p><p>To disguise spacing inconsistencies so they won't
        disrupt the flow of text for a reader, the font developer can
        use the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table to enable or disable
        individual glyph substitution and positioning actions that
        apply to specific scripts, language systems, and glyphs in the
        font.</p><p>For instance, a ligature glyph can replace multiple
        glyphs, shortening the line of text with an unobtrusive,
        localized adjustment (see Figure 6b). Font-specific
        positioning changes can be applied to particular glyphs in a
        text line that combines two or more fonts. Other options
        include repositioning the individual glyphs in the line,
        expanding the space between specific pairs of glyphs, and
        decreasing the spacing within particular glyph
        sequences.</p><div class="figure"><a name="idm17094"></a><p class="title"><strong>Figure 27.2. Figure 6b. <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> shortens the top
          line of this example by using the "ffi" ligature</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig6b.gif" alt="Figure 6b. JSTF shortens the top line of this example by using the &quot;ffi&quot; ligature"/></div></div></div><br class="figure-break"/><p>The font designer or developer defines
        <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> data as prioritized suggestions. Each
        suggestion lists the particular actions that the client can
        use to adjust the line of text. Justification actions may
        apply to both vertical and horizonal text.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17102"></a>Table Organization</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.2.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table organizes data by
        script and language system, as do the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>
        and <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables.  The
        <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table begins with a header that lists
        scripts in an array of JstfScriptRecords (see Figure 6c). Each
        record contains a ScriptTag and an offset to a JstfScript
        table that contains script and language-specific data:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>A default justification language system table
              (DefJstfLangSys) defines script-specific data that
              applies to the entire script in the absence of any
              language-specific information.</p></li><li class="listitem"><p>A justification language system table (JstfLangSys)
              stores the justification data for each language
              system.</p></li></ul></div><div class="figure"><a name="idm17116"></a><p class="title"><strong>Figure 27.3. Figure 6c. High-level organization of <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>
            table</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig6c.gif" alt="Figure 6c. High-level organization of JSTF table"/></div></div></div><br class="figure-break"/><p>A JstfLangSys table contains a list of justification
        suggestions. Each suggestion consists of a list of
        <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> LookupList
        indices to lookups that may be enabled or disabled to add or
        remove space in the line of text. In addition, each suggestion
        can include a set of dedicated justification lookups with
        maximum adjustment values to extend or shrink the amount of
        space.</p><p>The font developer prioritizes suggestions based on how
        they affect the appearance and function of the text line, and
        the client applies the suggestions in that order.
        Low-numbered (high-priority) suggestions correspond to "least
        bad" options.</p><p>Each script also may supply a list of extender glyphs,
        such as kashidas in Arabic. A client may use the extender
        glyphs in addition to the justification suggestions.</p><p>A client begins justifying a line of text only after
	implementing all selected <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
	<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> features for the string. Starting with
	the lowest-numbered suggestion, the client enables or disables
	the lookups specified in the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table,
	reassembles the lookups in the LookupList order, and applies
	them to each glyph in the string one after another. If the
	line still is not the correct length, the client processes the
	next suggestion in ascending order of priority. This continues
	until the line length meets the justification
	requirements.</p><p>Note: If any <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> suggestion at any
	priority level modifies a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
	<a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookup that was previously applied to
	the glyph string, then the text processing client must apply
	the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> suggestion to an unmodified
	version of the glyph string.</p><p>The rest of this chapter describes the tables and
        records used by the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table for scripts
        and language systems:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Script information includes the JstfScript table
              (plus its associated JstfLangSysRecords) and the
              ExtenderGlyph table.</p></li><li class="listitem"><p>Language system information includes the JstfLangSys
              table, JstfPriority table (and its associated
              JstfDataRecord), the JstfModList table, and the JstfMax
              table.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17143"></a>JSTF Header</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.3.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table begins with a header
          that contains a version number for the table (Version), a
          count of the number of scripts used in the font
          (JstfScriptCount), and an array of records
          (JstfScriptRecord). Each record contains a script tag
          (JstfScriptTag) and an offset to a JstfScript table
          (JstfScript).</p><p>Note: The JstfScriptTags must correspond with the
          ScriptTags listed in the <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> tables.</p><p>Example 1 at the end of this chapter shows a
          <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> Header table and
          JstfScriptRecord.</p><div class="table"><a name="idm17154"></a><p class="title"><strong>Table 27.1. JSTF header</strong></p><div class="table-contents"><table class="table" summary="JSTF header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>fixed32</td><td>Version</td><td>Version of the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a>
              table-initially set to 0x00010000</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>JstfScriptCount</td><td>Number of JstfScriptRecords in this
              table</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>JstfScriptRecord [JstfScriptCount]</td><td>Array of JstfScriptRecords-in alphabetical
              order, by JstfScriptTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm17176"></a><p class="title"><strong>Table 27.2. JstfScriptRecord</strong></p><div class="table-contents"><table class="table" summary="JstfScriptRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>JstfScriptTag</td><td>4-byte JstfScript
              identification</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>JstfScript</td><td>Offset to JstfScript table-from beginning of
              <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> Header</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.3.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62234"></a><code class="classname">JST</code> ==
      
  JSTF =
    element JSTF {
      attribute major { "1" },
      attribute minor { "0" },

      element script {
        attribute tag { text }
        jstfScriptTableOffset
      }*

      (  standaloneJstfScriptTable
       | standaloneExtenderGlyphTable
       | standaloneJstfLangSysTable
       | standaloneJstfPriorityTable
       | standaloneJstfModList
       | standaloneJstfMaxTable

       | standaloneLookupTable
       | standaloneSinglePosTable
       | standalonePairPosTable
       | standaloneCursiveAttachmentTable
       | standaloneMarkToBaseAttachmentTable
       | standaloneMarkToLigatureAttachmentTable
       | standaloneMarkToMarkAttachmentTable
       | standaloneExtensionTable

       | standaloneCoverageTable
       | standaloneClassDefTable
       | standaloneDeviceTable)*
      )*
    }
</pre></div><div role="zzzcompiler" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.3.3"></a>Compiler</h4></div></div></div><pre class="programlisting">
  public void fromXML (Element jstf)
      throws InvalidFontException, UnsupportedFontException {

    Map&lt;Element, Block&gt; blockCache = new HashMap&lt;Element, Block&gt; ();
    NodeList scripts = jstf.getChildNodes ();
    int scriptCount = scripts.getLength ();

    Block me = new Block (4 + 6*scriptCount, scriptCount);
    me.setFixed (0, 1, 0);

    for (int i = 0; i &lt; l.getLength (); i++) {
      (Element) script = (Element) scripts.item (i);

      me.setTag (4 + 6*i + offset, script.getAttribute ("tag"));
      me.setOffset (4 + 6*i + 4,
                    jstfScriptTableFromXML (script. jstf, blockCache)); }

    data = me.serialize ();
  }
</pre></div><div role="zzzdecompiler" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.3.4"></a>Decompiler</h4></div></div></div><pre class="programlisting">
  public void toXML (DecompilerConfig conf)
      throws org.xml.sax.SAXException, InvalidFontException {

    int [] counts = new int [data.length];
    for (int i = 0; i &lt; counts.length; i++) {
      counts [i] = 0; }

    int scriptCount = getuint16 (4);
    for (int i = 0; i &lt; scriptCount; i++) {
      jstfScriptTableToXMLCount (getOffset (4 + 6*i + 4), counts); }

    if (conf.pointers == DecompilerConfig.PointersAreShown.never) {
      for (int i = 0; i &lt; counts.length; i++) {
        counts [i] = 1; }}
    if (conf.pointers == DecompilerConfig.PointersAreShown.always) {
      for (int i = 0; i &lt; counts.length; i++) {
        counts [i] = 2; }}

    AttributesImpl at;

    int [] version = getTableVersion ();
    at = new AttributesImpl ();
    at.addAttribute ("", "major", "major", "CDATA", "" + version [0]);
    at.addAttribute ("", "minor", "minor", "CDATA", "" + version [1]);

    conf.ch.startElement ("JSTF", at); {

      for (int i = 0; i &lt; scriptCount; i++) {
        at = new AttributesImpl ();
        at.addAttribute ("", "tag", "tag", "CDATA",
                         Tag.tag2string (getTag (4 + 6*i)));
        jstfScriptTableOffsetToXML (conf, getOffset (4 + 6*i + 4), counts,
                                    script, at); }

      for (int i = 0; i &lt; scriptCount; i++) {
        jstfScriptTableToXML (conf, getOffset (4 + 6*i + 4), counts); }

      conf.ch.endElement ("JSTF"); }
  }
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17208"></a>Justification Script Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.4.1"></a>Specification</h4></div></div></div><p>A Justification Script (JstfScript) table describes the
        justification information for a single script. It consists of
        an offset to a table that defines extender glyphs
        (ExtenderGlyph), an offset to a default justification table
        for the script (DefJstfLangSys), and a count of the language
        systems that define justification data
        (JstfLangSysCount).</p><p>If a script uses the same justification information for
        all language systems, the font developer defines only the
        DefJstfLangSys table and sets the JstfLangSysCount to zero
        (0). However, if any language system has unique justification
        suggestions, JstfLangSysCount will be a positive value, and
        the JstfScript table must include an array of records
        (JstfLangSysRecord), one for each language system. Each
        JstfLangSysRecord contains a language system tag
        (JstfLangSysTag) and an offset to a justification language
        system table (JstfLangSys). In the JstfLangSysRecord array,
        records are ordered alphabetically by JstfLangSysTag.</p><p>Note: No JstfLangSysRecord is defined for the default
        script data; the data is stored in the DefJstfLangSys table
        instead.</p><p>Example 2 at the end of the chapter shows a JstfScript
        table for the Arabic script and a JstfLangSysRecord for the
        Farsi language system.</p><div class="table"><a name="idm17216"></a><p class="title"><strong>Table 27.3. JstfScript table</strong></p><div class="table-contents"><table class="table" summary="JstfScript table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>ExtenderGlyph</td><td>Offset to ExtenderGlyph table-from beginning
              of JstfScript table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>DefJstfLangSys</td><td>Offset to Default JstfLangSys table-from
              beginning of JstfScript table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>JstfLangSysCount</td><td>Number of JstfLangSysRecords in this table-
              may be zero (0)</td><td class="auto-generated"> </td></tr><tr><td>struct</td><td>JstfLangSysRecord [JstfLangSysCount]</td><td>Array of JstfLangSysRecords-in alphabetical
              order, by JstfLangSysTag</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm17241"></a><p class="title"><strong>Table 27.4. JstfLangSysRecord</strong></p><div class="table-contents"><table class="table" summary="JstfLangSysRecord" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>JstfLangSysTag</td><td>4-byte JstfLangSys identifier</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>JstfLangSys</td><td>Offset to JstfLangSys table-from beginning of
              JstfScript table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.4.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62402"></a><code class="classname">JST</code> ==
      
  jstfScriptTable =
    element extenderGlyph { extenderGlyphTableOffset }?,
    element defaultLangSys { jstfLangSysTableOffset }?,
    element langSys {
      attribute tag { text },
      jstfLangSysTableOffset
    }*

  standaloneJstfScriptTable =
    element jstfScriptTable { attribute id { text }, jstfScriptTable }

  jstfScriptTableOffset = attribute name { text } | jstfScriptTable
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17264"></a>Extender Glyph Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.5.1"></a>Specification</h4></div></div></div><p>The Extender Glyph table (ExtenderGlyph) lists indices
        of glyphs, such as Arabic kashidas, that a client may insert
        to extend the length of the line for justification. The table
        consists of a count of the extender glyphs for the script
        (GlyphCount) and an array of extender glyph indices
        (ExtenderGlyph), arranged in increasing numerical
        order.</p><p>Example 2 at the end of this chapter shows an
	ExtenderGlyph table for Arabic kashida glyphs.</p><div class="table"><a name="idm17270"></a><p class="title"><strong>Table 27.5. ExtenderGlyph table</strong></p><div class="table-contents"><table class="table" summary="ExtenderGlyph table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>GlyphCount</td><td>Number of Extender Glyphs in this
              script</td><td class="auto-generated"> </td></tr><tr><td>GlyphID</td><td>ExtenderGlyph [GlyphCount]</td><td>GlyphIDs-in increasing numerical
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.5.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62474"></a><code class="classname">JST</code> ==
      
  extenderGlyphTable =
    attribute glyphs { text }

  standaloneExtenderGlyphTable =
    element extenderGlyphTable { attribute id { text }, extenderGlyphTable }

  extenderGlyphTableOffset = attribute name { text } | extenderGlyphTable
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17293"></a>Justification Language System Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.6.1"></a>Specification</h4></div></div></div><p>The Justification Language System (JstfLangSys) table
        contains an array of justification suggestions, ordered by
        priority. A text-processing client doing justification should
        begin with the suggestion that has a zero (0) priority, and
        then-as necessary-apply suggestions of increasing priority
        until the text is justified.</p><p>The font developer defines the number and the meaning of
        the priority levels. Each priority level stands alone; its
        suggestions are not added to the previous levels. The
        JstfLangSys table consists of a count of the number of
        priority levels (JstfPriorityCnt) and an array of offsets to
        Justification Priority tables (JstfPriority), stored in
        priority order. Example 2 at the end of the chapter shows how
        to define a JstfLangSys table.</p><div class="table"><a name="idm17299"></a><p class="title"><strong>Table 27.6. JstfLangSys table</strong></p><div class="table-contents"><table class="table" summary="JstfLangSys table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>JstfPriorityCnt</td><td>Number of JstfPriority tables</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>JstfPriority [JstfPriorityCnt]</td><td>Array of offsets to JstfPriority tables-from
              beginning of JstfLangSys table-in priority
              order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.6.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62547"></a><code class="classname">JST</code> ==
      
  jstfLangSysTable =
    element priority {
      jstfPriorityTableOffset
    }*

  standaloneJstfLangSysTable =
    element jstfLangSysTable { attribute id { text }, jstfLanSysTable }

  jstfLangSysTableOffset = attribute name { text } | jstfLangSysTable
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17322"></a>Justification Priority Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.7.1"></a>Specification</h4></div></div></div><p>A Justification Priority (JstfPriority) table defines
          justification suggestions for a single priority level. Each
          priority level specifies whether to enable or disable
          <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> and <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookups
          or apply text justification lookups to shrink and extend
          lines of text.</p><p>JstfPriority has offsets to four tables with line
          shrinkage data: two are JstfGSUBModList tables for enabling
          and disabling glyph substitution lookups, and two are
          JstfGPOSModList tables for enabling and disabling glyph
          positioning lookups. Offsets to JstfGSUBModList and
          JstfGPOSModList tables also are defined for line
          extension.</p><p>Example 3 at the end of this chapter demonstrates two
          JstfPriority tables for two justification
          suggestions.</p><div class="table"><a name="idm17331"></a><p class="title"><strong>Table 27.7. JstfPriority table</strong></p><div class="table-contents"><table class="table" summary="JstfPriority table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Offset</td><td>ShrinkageEnableGSUB</td><td>Offset to Shrinkage Enable JstfGSUBModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ShrinkageDisableGSUB</td><td>Offset to Shrinkage Disable JstfGSUBModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ShrinkageEnableGPOS</td><td>Offset to Shrinkage Enable JstfGPOSModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ShrinkageDisableGPOS</td><td>Offset to Shrinkage Disable JstfGPOSModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ShrinkageJstfMax</td><td>Offset to Shrinkage JstfMax table-from
              beginning of JstfPriority table -may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExtensionEnableGSUB</td><td>Offset to Extension Enable JstfGSUBModList
              table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExtensionDisableGSUB</td><td>Offset to Extension Disable JstfGSUBModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExtensionEnableGPOS</td><td>Offset to Extension Enable JstfGSUBModList
              table-may be NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExtensionDisableGPOS</td><td>Offset to Extension Disable JstfGSUBModList
              table-from beginning of JstfPriority table-may be
              NULL</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>ExtensionJstfMax</td><td>Offset to Extension JstfMax table-from
              beginning of JstfPriority table -may be
              NULL</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.7.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62749"></a><code class="classname">JST</code> ==
      
  jstfPriorityTable =
    element shrinkage {
      element enableGSUB   { jstfModListOffset }?,
      element disableGSUB  { jstfModListOffset }?,
      element enableGPOS   { jstfModListOffset }?,
      element disableGPOS  { jstfModListOffset }?,
      element jstfMax      { jstfMaxTableOffset }? },

    element extension {
      element enableGSUB   { jstfModListOffset }?,
      element disableGSUB  { jstfModListOffset }?,
      element enableGPOS   { jstfModListOffset }?,
      element disableGPOS  { jstfModListOffset }?,
      element jstfMax      { jstfMaxTableOffset }? }

  standaloneJstfPriorityTable =
    element jstfPriority { attribute id { text }, jstfPriorityTable }

  jstfPriorityTableOffset = attribute name { text } | jstfPriorityTable
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17386"></a>Justification Modification List Tables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.8.1"></a>Specification</h4></div></div></div><p>The Justification Modification List tables
          (JstfGSUBModList and JstfGPOSModList) contain lists of
          indices into the lookup lists of either the GSUB or GPOS
          tables. The client can enable or disable the lookups to
          justify text. For example, to increase line length, the
          client might disable a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> ligature
          substitution.</p><p>Each JstfModList table consists of a count of Lookups
          (LookupCount) and an array of lookup indices
          (LookupIndex).</p><p>To justify a line of text, a text-processing client
          enables or disables the specified lookups in a JstfModList
          table, reassembles the lookups in the LookupList order, and
          applies them to each glyph in the string one after
          another.</p><p>Note: If any <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> suggestion at any
          priority level modifies a <a class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a> or
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookup previously applied to the
          glyph string, then the text-processing client must apply the
          <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> suggestion to an unmodified version
          of the glyph string.</p><p>Example 3 at the end of this chapter shows
          JstfGSUBModList and JstfGPOSModList tables with data for
          shrinking and extending text line lengths.</p><div class="table"><a name="idm17400"></a><p class="title"><strong>Table 27.8. JstfGSUBModList table</strong></p><div class="table-contents"><table class="table" summary="JstfGSUBModList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LookupCount</td><td>Number of lookups for this
              modification</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GSUBLookupIndex [LookupCount]</td><td>Array of LookupIndex identifiers in GSUB-in
              increasing numerical order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm17417"></a><p class="title"><strong>Table 27.9. JstfGPOSModList table</strong></p><div class="table-contents"><table class="table" summary="JstfGPOSModList table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LookupCount</td><td>Number of lookups for this
              modification</td><td class="auto-generated"> </td></tr><tr><td>uint16</td><td>GPOSLookupIndex [LookupCount]</td><td>Array of LookupIndex identifiers in GPOS-in
              increasing numerical order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.8.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62882"></a><code class="classname">JST</code> ==
      
  jstfModList =
    attribute lookups { text }

  standaloneJstfModList =
    element jstfModList { attribute id { text }, jstfModList }

  jstfModListOffset = attribute name { text } | jstfModList
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17440"></a>Justification Maximum Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.9.1"></a>Specification</h4></div></div></div><p>A Justification Maximum table (JstfMax) consists of an
          array of offsets to justification lookups (Lookup) and a
          count of the defined lookups (Lookup). JstfMax lookups
          typically are located after the JstfMax table in the font
          definition.</p><p>JstfMax tables have the same format as lookup tables and
          subtables in the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table, but the
          JstfMax lookups reside in the <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table
          and contain justification data only. The lookup data might
          specify a single adjustment value for positioning all glyphs
          in the script, or it might specify more elaborate
          adjustments, such as different values for different glyphs
          or special values for specific pairs of glyphs.</p><p>Note: All <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> lookup types except
          contextual positioning lookups may be defined in a JstfMax
          table.</p><p>JstfMax lookup values are defined in
          <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> ValueRecords and may be specified
          for any advance or placement position, whether horizontal or
          vertical. These values define the maximum shrinkage or
          extension allowed per glyph. To justify text, a
          text-processing client may choose to adjust a glyph's
          positioning by any amount from zero (0) to the specified
          maximum.</p><p>Example 4 at the end of this chapter shows a JstfMax
          table. It defines a justification lookup to change the size
          of the word space glyph to extend line lengths.</p><div class="table"><a name="idm17453"></a><p class="title"><strong>Table 27.10. JstfMax table</strong></p><div class="table-contents"><table class="table" summary="JstfMax table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>uint16</td><td>LookupCount</td><td>Number of lookup Indices for this
              modification</td><td class="auto-generated"> </td></tr><tr><td>Offset</td><td>Lookup [LookupCount]</td><td>Array of offsets to
              <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a>-type lookup tables-from
              beginning of JstfMax table-in design order</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.9.2"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e62980"></a><code class="classname">JST</code> ==
      
  jstfMaxTable =
    element lookup {
      GPOSJSTFlookupTableOffset
    }*

  standaloneJstfMaxTable =
    element jstfMaxTable { attribute id { text }, jstfMaxTable }

  jstfMaxTableOffset = attribute name { text } | jstfMaxTable

  standaloneGPOSJSTFlookupTable =
    element lookupTable { attribute id { text }, GPOSJSTlookupTable

  GPOSJSTFlookupTableOffset = attribute name { text } | GPOSJSTFlookupTable
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17477"></a>JSTF Table Examples</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.10.1"></a>Specification</h4></div></div></div><p>The rest of this chapter describes examples of all the
          <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> table formats. All the examples reflect unique
          parameters described below, but the samples provide a useful
          reference for building tables specific to other
          situations.</p><p>The examples have three columns showing hex data,
          source, and comments.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17484"></a>Example 1: JSTF Header Table and JstfScriptRecord</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.11.1"></a>Specification</h4></div></div></div><p>Example 1 demonstrates how a script is defined in the
          <a class="link" href="chapter.JSTF.html" title="Chapter 27. JSTF - The Justification Table">JSTF</a> Header with a JstfScriptRecord that
          identifies the script and references its JstfScript
          table.</p><div class="table"><a name="idm17490"></a><p class="title"><strong>Table 27.11. Example 1</strong></p><div class="table-contents"><table class="table" summary="Example 1" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>JSTFHeader</td><td> </td></tr><tr><td> </td><td>TheJSTFHeader</td><td>JSTFHeader table
                  definition</td></tr><tr><td>00010000</td><td>0x00010000</td><td>version</td></tr><tr><td>0001</td><td>1</td><td>JstfScriptCount JstfScriptRecord[0]</td></tr><tr><td>74686169</td><td>"thai"</td><td>JstfScriptTag</td></tr><tr><td>000C</td><td>ThaiScript</td><td>offset to JstfScript table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17523"></a>Example 2: JstfScript Table, ExtenderGlyph Table,
        JstfLangSysRecord, and JstfLangSys Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.12.1"></a>Specification</h4></div></div></div><p>Example 2 shows a JstfScript table for the Arabic script
          and the tables it references. The DefJstfLangSys table
          defines justification data to apply to the script in the
          absence of language-specific information. In the example,
          the table lists two justification suggestions in priority
          order.</p><p>JstfScript also supplies language-specific justification
          data for the Farsi language. The JstfLangSysRecord
          identifies the language and references its JstfLangSys
          table. The FarsiJstfLangSys lists one suggestion for
          justifying Farsi text.</p><p>The ExtenderGlyph table in JstfScript lists the indices
          of all the extender glyphs used in the script.</p><div class="table"><a name="idm17530"></a><p class="title"><strong>Table 27.12. Example 2</strong></p><div class="table-contents"><table class="table" summary="Example 2" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>JstfScript</td><td> </td></tr><tr><td> </td><td>ArabicScript</td><td>JstfScript table
                  definition</td></tr><tr><td>000C</td><td>ArabicExtenders</td><td>ExtenderGlyph</td></tr><tr><td>0012</td><td>ArabicDefJstfLangSys</td><td>offset to DefJstfLangSys table</td></tr><tr><td>0001</td><td>1</td><td>JstfLangSysCount JstfLangSysRecord[0]</td></tr><tr><td>50455220</td><td>"FAR</td><td>" JstfLangSysTag</td></tr><tr><td>0018</td><td>FarsiJstfLangSys</td><td>JstfLangSy</td></tr><tr><td> </td><td>ExtenderGlyph</td><td> </td></tr><tr><td> </td><td>ArabicExtenders</td><td>ExtenderGlyph table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>GlyphCount</td></tr><tr><td>01D3</td><td>TatweelGlyphID</td><td>ExtenderGlyph[0]</td></tr><tr><td>01D4</td><td>LongTatweelGlyphID</td><td>ExtenderGlyph[1</td></tr><tr><td> </td><td>JstfLangSys</td><td> </td></tr><tr><td> </td><td>ArabicDefJstfLangSys</td><td>JstfLangSys table
                  definition</td></tr><tr><td>0002</td><td>2</td><td>JstfPriorityCnt</td></tr><tr><td>000A</td><td>ArabicScriptJstfPriority1</td><td>offset to JstfPriority[0] table</td></tr><tr><td>001E</td><td>ArabicScriptJstfPriority2</td><td>offset to JstfPriority[1] tabl</td></tr><tr><td> </td><td>JstfLangSys</td><td> </td></tr><tr><td> </td><td>FarsiJstfLangSys</td><td>JstfLangSys table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>JstfPriorityCnt</td></tr><tr><td>002C</td><td>FarsiLangJstfPriority1</td><td>offset to JstfPriority[0] table</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17623"></a>Example 3: JstfPriority Table, JstfGSUBModList Table, and
        JstfGPOSModList Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.13.1"></a>Specification</h4></div></div></div><p>Example 3 shows the JstfPriority and JstfModList table
          definitions for two justification suggestions defined in
          priority order. The first suggestion uses ligature
          substitution to shrink the lengths of text lines, and it
          extends line lengths by replacing ligatures with their
          individual glyph components. Other lookup actions are not
          recommended at this priority level and are set to NULL. The
          associated JstfModList tables enable and disable three
          substitution lookups.</p><p>The second suggestion enables glyph kerning to reduce
          line lenths and disables glyph kerning to extend line
          lengths. Each action uses three lookups. This suggestion
          also includes a JstfMax table to extend line lengths, called
          WordSpaceExpandMax, which is described in Example 4.</p><div class="table"><a name="idm17629"></a><p class="title"><strong>Table 27.13. Example 3</strong></p><div class="table-contents"><table class="table" summary="Example 3" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>JstfPriority</td><td> </td></tr><tr><td> </td><td>USEnglishFirstJstfPriority</td><td>JstfPriority table
                  definition</td></tr><tr><td>0028</td><td>EnableGSUBLookupsToShrink</td><td>offset to ShrinkageEnableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageDisableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageEnableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageDisableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to Shrinkage JstfMax table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionEnableGSUB, JstfGSUBModList
                  table</td></tr><tr><td>0038</td><td>DisableGSUBLookupsToExtend</td><td>offset to ExtensionDisableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionEnableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionDisableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to Extension JstfMax tabl</td></tr><tr><td> </td><td>JstfPriority</td><td> </td></tr><tr><td> </td><td>USEnglishSecondJstfPriority</td><td>JstfPriority table
                  definition</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageEnableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageDisableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ShrinkageEnableGPOS JstfGPOSModList
                  table</td></tr><tr><td>001C</td><td>DisableGPOSLookupsToShrink</td><td>offset to ShrinkageDisableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to Shrinkage JstfMax table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionEnableGSUB JstfGSUBModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionDisableGSUB JstfGSUBModList
                  table</td></tr><tr><td>002C</td><td>EnableGPOSLookupsToExtend</td><td>offset to ExtensionEnableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to ExtensionDisableGPOS JstfGPOSModList
                  table</td></tr><tr><td>0000</td><td>NULL</td><td>offset to Extension JstfMax tabl</td></tr><tr><td> </td><td>JstfGSUBModList</td><td> </td></tr><tr><td> </td><td>EnableGSUBLookupsToShrink</td><td>JstfGSUBModList table
                  definition, enable three ligature substitution
                  lookups</td></tr><tr><td>0003</td><td>3</td><td>LookupCount</td></tr><tr><td>002E</td><td>46</td><td>LookupIndex[0]</td></tr><tr><td>0035</td><td>53</td><td>LookupIndex[1]</td></tr><tr><td>0063</td><td>99</td><td>LookupIndex[2</td></tr><tr><td> </td><td>JstfGPOSModList</td><td> </td></tr><tr><td> </td><td>DisableGPOSLookupsToShrink</td><td>JstfGPOSModList
                  table definition, disable three tight kerning
                  lookups</td></tr><tr><td>0003</td><td>3</td><td>LookupCount</td></tr><tr><td>006C</td><td>108</td><td>LookupIndex[0]</td></tr><tr><td>006E</td><td>110</td><td>LookupIndex[1]</td></tr><tr><td>0070</td><td>112</td><td>LookupIndex[2</td></tr><tr><td> </td><td>JstfGSUBModList</td><td> </td></tr><tr><td> </td><td>DisableGSUBLookupsToExtend</td><td>JstfGSUBModList
                  table definition, disable three ligature
                  substitution lookups</td></tr><tr><td>0003</td><td>3</td><td>LookupCount</td></tr><tr><td>002E</td><td>46</td><td>LookupIndex[0]</td></tr><tr><td>0035</td><td>53</td><td>LookupIndex[1]</td></tr><tr><td>0063</td><td>99</td><td>LookupIndex[2</td></tr><tr><td> </td><td>JstfGPOSModList</td><td> </td></tr><tr><td> </td><td>EnableGPOSLookupsToExtend</td><td>JstfGPOSModList table
                  definition enable three tight kerning
                  lookups</td></tr><tr><td>0003</td><td>3</td><td>LookupCount</td></tr><tr><td>006C</td><td>108</td><td>LookupIndex[0]</td></tr><tr><td>006E</td><td>110</td><td>LookupIndex[1]</td></tr><tr><td>0070</td><td>112</td><td>LookupIndex[2]</td></tr></tbody></table></div></div><br class="table-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm17830"></a>Example 4: JstfMax Table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.28.14.1"></a>Specification</h4></div></div></div><p>The JstfMax table in Example 4 defines a lookup to
          expand the advance width of the word space glyph and extend
          line lengths. The lookup definition is identical to the
          SinglePos lookup type in the <a class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table
          although it is enabled only when justifying text. The
          ValueRecord in the WordSpaceExpand lookup subtable specifies
          an XAdvance adjustment of 360 units, which is the maximum
          value the font developer recommends for acceptable text
          rendering. The text-processing client may implement the
          lookup using any value between zero and the maximum.</p><div class="table"><a name="idm17836"></a><p class="title"><strong>Table 27.14. Example 4</strong></p><div class="table-contents"><table class="table" summary="Example 4" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>HexData</th><th>Source</th><th>Comment</th></tr></thead><tbody><tr><td> </td><td>JstfMax</td><td> </td></tr><tr><td> </td><td>WordSpaceExpandMax</td><td>JstfMax table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>LookupCount</td></tr><tr><td>0004</td><td>WordSpaceExpandLookup</td><td>offset to Jstf Lookup[0] tabl</td></tr><tr><td> </td><td>Lookup</td><td> </td></tr><tr><td> </td><td>WordSpaceExpandLookup</td><td>Jstf Lookup table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>LookupType, SinglePos Lookup</td></tr><tr><td>0000</td><td>0x0000</td><td>LookupFlag</td></tr><tr><td>0001</td><td>1</td><td>SubTableCount</td></tr><tr><td>0008</td><td>WordSpaceExpandSubtable</td><td>offset to Subtable[0], SinglePos
                  subtabl</td></tr><tr><td> </td><td>SinglePosFormat1</td><td> </td></tr><tr><td> </td><td>WordSpaceExpandSubtable</td><td>SinglePos subtable
                  definition</td></tr><tr><td>0001</td><td>1</td><td>PosFormat</td></tr><tr><td>0008</td><td>WordSpaceCoverage</td><td>offset to Coverage table</td></tr><tr><td>0004</td><td>0x0004</td><td>ValueFormat, XAdvance only</td></tr><tr><td>0168</td><td>360</td><td>Value XAdvance value in Jstf, this is a max
                  value, expand word space from zero to this
                  amoun</td></tr><tr><td> </td><td>CoverageFormat1</td><td> </td></tr><tr><td> </td><td>WordSpaceCoverage</td><td>Coverage table
                  definition</td></tr><tr><td>0001</td><td>1</td><td>CoverageFormat</td></tr><tr><td>0001</td><td>1</td><td>GlyphCount</td></tr><tr><td>0022</td><td>WordSpaceGlyphID</td><td>GlyphArray[0]</td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>