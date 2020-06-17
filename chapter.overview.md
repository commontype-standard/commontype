<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.overview"></a>Chapter 2. Overview</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135436928"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.2.1.1"></a>Specification</h3></div></div></div><p role="">The OpenType font format is an extension of the TrueType
	font format, adding support for PostScript font data. The
	OpenType font format was developed jointly by Microsoft and
	Adobe. OpenType fonts and the operating system services which
	support OpenType fonts provide users with a simple way to
	install and use fonts, whether the fonts contain TrueType
	outlines or CFF (PostScript) outlines.</p><p role="">The OpenType font format addresses the following goals:

	  </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">broader multi-platform support</p></li><li role="" class="listitem"><p role="">better support for international character sets</p></li><li role="" class="listitem"><p role="">better protection for font data</p></li><li role="" class="listitem"><p role="">smaller file sizes to make font distribution more
	      efficient</p></li><li role="" class="listitem"><p role="">broader support for advanced typographic control</p></li></ul></div><p role="">OpenType fonts are also referred to as TrueType Open
	v.2.0 fonts, because they use the TrueType 'sfnt' font file
	format. PostScript data included in OpenType fonts may be
	directly rasterized or converted to the TrueType outline
	format for rendering, depending on which rasterizers have been
	installed in the host operating system. But the user model is
	the same: OpenType fonts just work. Users will not need to be
	aware of the type of outline data in OpenType fonts. And font
	creators can use whichever outline format they feel provides
	the best set of features for their work, without worrying
	about limiting a font's usability.</p><p role="">OpenType fonts can include the OpenType Layout tables,
	which allow font creators to design better international and
	high-end typographic fonts. The OpenType Layout tables contain
	information on glyph substitution, glyph positioning,
	justification, and baseline positioning, enabling
	text-processing applications to improve text layout.</p><p role="">As with TrueType fonts, OpenType fonts allow the
	handling of large glyph sets using Unicode encoding. Such
	encoding allows broad international support, as well as
	support for typographic glyph variants.</p><p role="">Additionally, OpenType fonts may contain digital
	signatures, which allows operating systems and browsing
	applications to identify the source and integrity of font
	files, including embedded font files obtained in web
	documents, before using them. Also, font developers can encode
	embedding restrictions in OpenType fonts, and these
	restrictions cannot be altered in a font signed by the
	developer.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320135426048"></a>Related documentation</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.2.2.1"></a>Specification</h3></div></div></div><p role="">The following documents may be consulter for further
	information:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Adobe Technical Note #5176: "The Compact Font Format
	      Specification."</p></li><li role="" class="listitem"><p role="">Adobe Technical Note #5177: "Type 2 Charstring Format."</p></li><li role="" class="listitem"><p role="">TrueType 1.0 Font Files, Technical
	      Specification. Microsoft.</p></li><li role="" class="listitem"><p role="">OpenType Layout Font Specification. Microsoft.</p></li><li role="" class="listitem"><p role="">Adobe Type 1 Font Format. Addison Wesley, 1991; ISBN
	      0-201-57044-0.</p></li><li role="" class="listitem"><p role="">Adobe Technical Note #5015: "The Type 1 Font Format
	      Supplement." This document contains all updates to the
	      Type 1 format.</p></li><li role="" class="listitem"><p role="">Adobe Technical Note #5087: "Multiple Master Font
	      Programs for the Macintosh."</p></li><li role="" class="listitem"><p role="">Adobe Technical Note #5088 "Font Naming Issues."
	      This document discusses general font name issues. </p></li><li role="" class="listitem"><p role="">Adobe's Unicode and Glyph Names guide.</p></li></ul></div></div></div></div>