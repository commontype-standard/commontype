<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.advanced"></a>Chapter 20. Advanced Typographic Extensions – CommonType Layout</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6164"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.1.1"></a>Specification</h4></div></div></div><p>The Advanced Typographic tables (CommonType Layout tables)
	  extend the functionality of fonts with either TrueType or CFF
	outlines. CommonType Layout fonts contain additional information
	that extends the capabilities of the fonts to support
	high-quality international typography:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>CommonType Layout fonts allow a rich mapping between
		characters and glyphs, which supports ligatures,
		positional forms, alternates, and other
		substitutions.</p></li><li class="listitem"><p>CommonType Layout fonts include information to
		support features for two-dimensional positioning and
		glyph attachment.</p></li><li class="listitem"><p>CommonType Layout fonts contain explicit script and
		language information, so a text-processing application
		can adjust its behavior accordingly.</p></li><li class="listitem"><p>CommonType Layout fonts have an open format that
		allows font developers to define their own
		typographical features.</p></li></ul></div><p>
      </p><p>This overview introduces the power and flexibility of
	  the CommonType Layout font model. The CommonType Layout tables
	  are described in more detail in the "Font File Tables"
	  section of the CommonType specification.</p><p>CommonType Layout Common Table Formats are documented in
	  the chapter "CommonType Layout Common Table Formats".</p><p>Registered CommonType Layout Tags for scripts, languages,
	  and baselines, are documented in the chapter "CommonType
	  Layout Registered Features". </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6181"></a>CommonType Layout at a Glance</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.2.1"></a>Specification</h4></div></div></div><p>CommonType Layout addresses complex typographical issues
	  that especially affect people using text-processing
	  applications in multi-lingual and non-Latin
	  environments.</p><p>CommonType Layout fonts may contain alternative forms of
	  characters and mechanisms for accessing them. For example,
	  in Arabic, the shape of a character often varies with the
	  character's position in a word. As shown here, the ha
	  character will take any of four shapes, depending on whether
	  it stands alone or whether it falls at the beginning,
	  middle, or end of a word. CommonType Layout helps a
	  text-processing application determine which variant to
	  substitute when composing text. </p><div class="figure"><a name="idm6187"></a><p class="title"><strong>Figure 20.1. Figure 1a. Isolated, initial, medial, and final forms
	    of the Arabic character ha.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1a.gif" alt="Figure 1a. Isolated, initial, medial, and final forms of the Arabic character ha."/></div></div></div><br class="figure-break"/><p> Similarly, CommonType Layout helps an application use the
	  correct forms of characters when text is positioned
	  vertically instead of horizontally, such as with Kanji. For
	  example, Kanji uses alternative forms of parentheses when
	  positioned vertically.</p><div class="figure"><a name="idm6193"></a><p class="title"><strong>Figure 20.2. Figure 1b. Alternative forms of parentheses used when
	    positioning Kanji vertically.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1b.gif" alt="Figure 1b. Alternative forms of parentheses used when positioning Kanji vertically."/></div></div></div><br class="figure-break"/><p> The CommonType Layout font format also supports the
	  composition and decomposition of ligatures. For example,
	  English, French, and other languages based on Latin can
	  substitute a single ligature, such as "fi", for its
	  component glyphs - in this case, "f" and "i". Conversely,
	  the individual "f" and "i" glyphs could replace the
	  ligature, possibly to give a text-processing application
	  more flexibility when spacing glyphs to fill a line of
	  justified text.</p><div class="figure"><a name="idm6199"></a><p class="title"><strong>Figure 20.3. Figure 1c. Two Latin glyphs and their associated
	    ligature.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1c.gif" alt="Figure 1c. Two Latin glyphs and their associated ligature."/></div></div></div><br class="figure-break"/><div class="figure"><a name="idm6204"></a><p class="title"><strong>Figure 20.4. Figure 1d. Three Arabic glyphs and their associated
	    ligature</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1d.gif" alt="Figure 1d. Three Arabic glyphs and their associated ligature"/></div></div></div><br class="figure-break"/><p>Glyph substitution is just one way CommonType Layout
	  extends font capabilities. Using precise X and Y coordinates
	  for positioning glyphs, CommonType Layout fonts also can
	  identify points for attaching one glyph to another to create
	  cursive text and glyphs that need diacritical or other
	  special marks.</p><p>CommonType Layout fonts also may contain baseline
	  information that specifies how to position glyphs
	  horizontally or vertically. Because baselines may vary from
	  one script (set of characters) to another, this information
	  is especially useful for aligning text that mixes glyphs
	  from scripts for different languages.</p><div class="figure"><a name="idm6211"></a><p class="title"><strong>Figure 20.5. Figure 1c. A line of text, baselines adjusted, mixing
	    Latin and Arabic scripts.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1e.gif" alt="Figure 1c. A line of text, baselines adjusted, mixing Latin and Arabic scripts."/></div></div></div><br class="figure-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6216"></a>TrueType versus CommonType Layout</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.3.1"></a>Specification</h4></div></div></div><p>A TrueType font is a collection of several tables that
	  contain different types of data: glyph outlines, metrics,
	  bitmaps, mapping information, and much more. CommonType Layout
	  fonts contain all this basic information, plus additional
	  tables containing information for advanced
	  typography.</p><p>Text-processing applications - referred to as "clients"
	  of CommonType Layout - can retrieve and parse the information
	  in CommonType Layout tables. So, for example, a
	  text-processing client can choose the correct character
	  shapes and space them properly.</p><p>As much as possible, the tables of CommonType Layout
	  define only the information that is specific to the font
	  layout. The tables do not try to encode information that
	  remains constant within the conventions of a particular
	  language or the typography of a particular script. Such
	  information that would be replicated across all fonts in a
	  given language belongs in the text-processing application
	  for that language, not in the fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6223"></a>CommonType Layout Terminology</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.4.1"></a>Specification</h4></div></div></div><p>The CommonType Layout model is organized around glyphs,
	  scripts, language systems, and features</p><h5><a name="idm6228"></a>Characters versus glyphs</h5><p>Users don't view or print characters: a user views or
	  prints glyphs. A glyph is a representation of a
	  character. The character "capital letter A" is represented
	  by the glyph "A" in Times New Roman Bold and "A" in Arial
	  Bold. A font is a collection of glyphs. To retrieve glyphs,
	  the client uses information in the "cmap" table of the font,
	  which maps the client's character codes to glyph indices in
	  the table.</p><p>Glyphs can also represent combinations of characters and
	  alternative forms of characters: glyphs and characters do
	  not strictly correspond one-to-one. For example, a user
	  might type two characters, which might be better represented
	  with a single ligature glyph. Conversely, the same character
	  might take different forms at the beginning, middle, or end
	  of a word, so a font would need several different glyphs to
	  represent a single character. CommonType Layout fonts contain
	  a table that provides a client with information about
	  possible glyph substitutions.</p><div class="figure"><a name="idm6231"></a><p class="title"><strong>Figure 20.6. Figure 1f. Multiple glyphs for the ampersand character.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1f.gif" alt="Figure 1f. Multiple glyphs for the ampersand character."/></div></div></div><br class="figure-break"/><h5><a name="idm6236"></a>Scripts</h5><p>A script is composed of a group of related characters,
	  which may be used by one or more languages. Latin, Arabic,
	  and Thai are examples of scripts. A font may use a single
	  script, or it may use many scripts. Within an CommonType
	  Layout font, scripts are identified by unique 4-byte
	  tags.</p><div class="figure"><a name="idm6238"></a><p class="title"><strong>Figure 20.7. Figure 1g. Glyphs in the Latin, Kanji, and Arabic
	    scripts.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig2a.gif" alt="Figure 1g. Glyphs in the Latin, Kanji, and Arabic scripts."/></div></div></div><br class="figure-break"/><h5><a name="idm6243"></a>Language systems</h5><p>Scripts, in turn, may be divided into language
	  systems. For example, the Latin script is used to write
	  English, French, or German, but each language has its own
	  special requirements for text processing. A font developer
	  can choose to provide information that is tailored to the
	  script, to the language system, or to both.</p><p>Language systems, unlike scripts, are not necessarily
	  evident when a text-processing client examines the
	  characters being used. To avoid ambiguity, the user or the
	  operating system needs to identify the language
	  system. Otherwise, the client will use the default
	  language-system information provided with each
	  script.</p><div class="figure"><a name="idm6246"></a><p class="title"><strong>Figure 20.8. Figure 1h. Differences in the English, French, and
	    German language system.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1h.gif" alt="Figure 1h. Differences in the English, French, and German language system."/></div></div></div><br class="figure-break"/><h5><a name="idm6251"></a>Features</h5><p>Features define the basic functionality of the font. A
	  font that contains tables to handle diacritical marks will
	  have a "mark" feature. A font that supports substitution of
	  vertical glyphs will have a "vert" feature.</p><p>The CommonType Layout feature model provides great
	  flexibility to font developers because features do not have
	  to be predefined by Microsoft Corporation. Instead, font
	  developers can work with application developers to determine
	  useful features for fonts, add such features to CommonType
	  Layout fonts, and enable client applications to support such
	  features.</p><div class="figure"><a name="idm6254"></a><p class="title"><strong>Figure 20.9. Figure 1i. The relationship of scripts, language
	    systems, features, and lookups for substitution and
	    positioning tables.</strong></p><div class="figure-contents"><div class="mediaobject"><img src="src/images/../../fig1i.gif" alt="Figure 1i. The relationship of scripts, language systems, features, and lookups for substitution and positioning tables."/></div></div></div><br class="figure-break"/><h5><a name="idm6259"></a>CommonType Layout tables</h5><p>CommonType Layout comprises five new tables: GSUB, GPOS,
	  BASE, JSTF, and GDEF. These tables and their formats are
	  discussed in detail in the chapters that follow this
	  overview.</p><p>GSUB: Contains information about glyph substitutions to
	  handle single glyph substitution, one-to-many substitution
	  (ligature decomposition), aesthetic alternatives, multiple
	  glyph substitution (ligatures), and contextual glyph
	  substitution.</p><p>GPOS: Contains information about X and Y positioning of
	  glyphs to handle single glyph adjustment, adjustment of
	  paired glyphs, cursive attachment, mark attachment, and
	  contextual glyph positioning.</p><p>BASE: Contains information about baseline offsets on a
	  script-by-script basis.</p><p>JSTF: Contains justification information, including
	  whitespace and Kashida adjustments.</p><p>GDEF: Contains information about all individual glyphs
	  in the font: type (simple glyph, ligature, or combining
	  mark), attachment points (if any), and ligature caret (if a
	  ligature glyph).</p><p>Common Table Formats: Several common table formats are
	  used by the CommonType Layout tables.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6267"></a>Text processing with CommonType Layout fonts</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.5.1"></a>Specification</h4></div></div></div><p>A text-processing client follows a standard process to
	  convert the string of characters entered by a user into
	  positioned glyphs. To produce text with CommonType Layout
	  fonts:</p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>Using the cmap table in the font, the client
	      converts the character codes into a string of glyph
	      indices.</p></li><li class="listitem"><p>Using information in the GSUB table, the client
	      modifies the resulting string, substituting positional
	      or vertical glyphs, ligatures, or other alternatives as
	      appropriate.</p></li><li class="listitem"><p>Using positioning information in the GPOS table and
	      baseline offset information in the BASE table, the
	      client then positions the glyphs.</p></li><li class="listitem"><p>Using design coordinates the client determines
	      device-independent line breaks. Design coordinates are
	      high-resolution and device-independent.</p></li><li class="listitem"><p>Using information in the JSTF table, the client
	      justifies the lines, if the user has specified such
	      alignment.</p></li><li class="listitem"><p>The operating system rasterizes the line of glyphs
	      and renders the glyphs in device coordinates that
	      correspond to the resolution of the output
	      device.</p></li></ol></div><p>Throughout this process the text-processing client keeps
	  track of the association between the character codes for the
	  original text and the glyph indices of the final, rendered
	  text. In addition, the client may save language and script
	  information within the text stream to clearly associate
	  character codes with typographical behavior.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.5.2"></a>Annotation</h4></div></div></div><p>An alternative point of view is to say that the font, and
	  in particular the GSUB and GPOS tables contain fragments of
	  programs which operate on a glyph run. The layout engine
	  decides how the typographic treatments specified in its
	  input should be realized, and in particular whether some of
	  the programs fragments should be invoked to manipulate the
	  glyph run. These program fragments are written in a very
	  specialized language.</p><p>The implementation of the glyph run structure is not
	  part of this specification. However, there is some
	  connection since the GSUB and GPOS programs do operate on
	  that structure. We capture here this connection in the form
	  of an interface:</p><pre class="programlisting"><a name="d1e21762"></a><code class="classname">GlyphRun interface</code> ==
      
package com.adobe.aots.CommonType;

public interface GlyphRun {
  <code class="classname">glyphrun.methods: <a class="link" href="chapter.advanced.html#d1e21774">1</a>, <a class="link" href="chapter.advanced.html#d1e21783">2</a>, <a class="link" href="chapter.advanced.html#d1e21792">3</a>, <a class="link" href="chapter.advanced.html#d1e21802">4</a>, <a class="link" href="chapter.advanced.html#d1e21811">5</a>, <a class="link" href="chapter.advanced.html#d1e21820">6</a></code>
}
</pre><p>First, we have two simple methods to access the number
	  of glyphs in the run and the ID of glyph at a specific
	  position:</p><pre class="programlisting"><a name="d1e21774"></a><code class="classname">GlyphRun interface</code> ==
      
  public int glyphCount ();
  public int glyphAt (int pos);
</pre><p>Another pair of accessors, this time to get the position
	  of a glyph:</p><pre class="programlisting"><a name="d1e21783"></a><code class="classname">GlyphRun interface</code> ==
      
  public int getXPos (int g);
  public int getYPos (int g);
</pre><p>The specification does not address the situation where
	  a feature is applied to only part of a glyph run. However,
	  it is necessary to support that situation: consider the case
	  of a fragment on which 'onum' is applied, while 'kern' is
	  applied to whole glyph run. Clearly, it is not possible to
	  decompose that glyph run in three independant glyph runs to
	  be processed separately, since it would imply no kerning
	  between the last glyph subject to 'onum' and the glyph
	  followin it. Thus, a GPOS/GSUB engine needs
	  to figure out if a given lookup is to be applied at a given
	  position:</p><pre class="programlisting"><a name="d1e21792"></a><code class="classname">GlyphRun interface</code> ==
      
  public boolean isLookupApplied (int lookupIndex, int start, int stop);
</pre><p>The MarkToLigature GPOS lookup type has the implicit
	  notion of ligature component, and of the component to which
	  a mark following a ligature attaches to:</p><pre class="programlisting"><a name="d1e21802"></a><code class="classname">GlyphRun interface</code> ==
      
  public void setLigComponents (int[] components);
  public int getLigComponent (int g);
</pre><p>The GSUB lookups result in the replaced of one or more
	  glyphs by one or more glyphs:</p><pre class="programlisting"><a name="d1e21811"></a><code class="classname">GlyphRun interface</code> ==
      
  public void replace (int position, int replacementGlyph);
  public void replace (int position, int[] replacementGlyphs);
  public void replace (int[] positions, int replacementGlyph);
</pre><p>The GPOS lookups result in the adjustment of a glyph
	  position:</p><pre class="programlisting"><a name="d1e21820"></a><code class="classname">GlyphRun interface</code> ==
      
  public void adjustPlacementAndAdvance (int g, ValueRecord vr);
  public void move (int g, int x, int y);
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm6331"></a>CommonType Layout fonts in Windows 95</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.21.6.1"></a>Specification</h4></div></div></div><p>The core system fonts in the Middle East and Far East
	  versions of Windows 95 are CommonType Layout fonts. These
	  fonts demonstrate aspects of CommonType Layout's
	  versatility.</p><h5><a name="idm6336"></a>Middle East Windows 95</h5><p>Middle East Windows 95 uses several Arabic CommonType
	  Layout fonts: fixed regular weight, proportional regular
	  weight, fixed bold, and proportional bold. These fonts take
	  advantage of many glyph substitution features available in
	  CommonType Layout, namely simple substitution (one-to-one
	  contextual), ligature substitution (many-to-one), and mark
	  set substitutions. In Middle East Windows 95, the operating
	  system itself handles glyph substitution, using data in the
	  GSUB table of each font.</p><h5><a name="idm6338"></a>Far East Windows 95</h5><p>Far East Windows 95 also uses several CommonType Layout
	  fonts: fixed serif, proportional serif, fixed sans serif,
	  and proportional sans serif. The Japanese fonts take
	  advantage of a subset of CommonType Layout features, including
	  vertical glyph substitution and baseline positioning. As
	  with Middle East Windows 95, the operating system in Far
	  East Windows 95 will handle glyph substitution, using data
	  in the GSUB table in each font. However, the text-processing
	  client will need to handle baseline positioning, using data
	  in the BASE table in each font. </p></div></div></div>