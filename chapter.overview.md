<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.overview"></a>Chapter 1. Overview</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm360573219584"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.2.1.1"></a>Specification</h4></div></div></div><p>The CommonType font format is an extension of the TrueType
	font format, adding support for PostScript font data. The
	CommonType font format was developed jointly by Microsoft and
	Adobe. CommonType fonts and the operating system services which
	support CommonType fonts provide users with a simple way to
	install and use fonts, whether the fonts contain TrueType
	outlines or CFF (PostScript) outlines.</p><p>The CommonType font format addresses the following goals:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>broader multi-platform support</p></li><li class="listitem"><p>better support for international character sets</p></li><li class="listitem"><p>better protection for font data</p></li><li class="listitem"><p>smaller file sizes to make font distribution more
	      efficient</p></li><li class="listitem"><p>broader support for advanced typographic control</p></li></ul></div><p>CommonType fonts are also referred to as TrueType Open
	v.2.0 fonts, because they use the TrueType 'sfnt' font file
	format. PostScript data included in CommonType fonts may be
	directly rasterized or converted to the TrueType outline
	format for rendering, depending on which rasterizers have been
	installed in the host operating system. But the user model is
	the same: CommonType fonts just work. Users will not need to be
	aware of the type of outline data in CommonType fonts. And font
	creators can use whichever outline format they feel provides
	the best set of features for their work, without worrying
	about limiting a font's usability.</p><p>CommonType fonts can include the CommonType Layout tables,
	which allow font creators to design better international and
	high-end typographic fonts. The CommonType Layout tables contain
	information on glyph substitution, glyph positioning,
	justification, and baseline positioning, enabling
	text-processing applications to improve text layout.</p><p>As with TrueType fonts, CommonType fonts allow the
	handling of large glyph sets using Unicode encoding. Such
	encoding allows broad international support, as well as
	support for typographic glyph variants.</p><p>Additionally, CommonType fonts may contain digital
	signatures, which allows operating systems and browsing
	applications to identify the source and integrity of font
	files, including embedded font files obtained in web
	documents, before using them. Also, font developers can encode
	embedding restrictions in CommonType fonts, and these
	restrictions cannot be altered in a font signed by the
	developer.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm360573211200"></a>Related documentation</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.2.2.1"></a>Specification</h4></div></div></div><p>The following documents may be consulter for further
	information:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Adobe Technical Note #5176: "The Compact Font Format
	      Specification."</p></li><li class="listitem"><p>Adobe Technical Note #5177: "Type 2 Charstring Format."</p></li><li class="listitem"><p>TrueType 1.0 Font Files, Technical
	      Specification. Microsoft.</p></li><li class="listitem"><p>CommonType Layout Font Specification. Microsoft.</p></li><li class="listitem"><p>Adobe Type 1 Font Format. Addison Wesley, 1991; ISBN
	      0-201-57044-0.</p></li><li class="listitem"><p>Adobe Technical Note #5015: "The Type 1 Font Format
	      Supplement." This document contains all updates to the
	      Type 1 format.</p></li><li class="listitem"><p>Adobe Technical Note #5087: "Multiple Master Font
	      Programs for the Macintosh."</p></li><li class="listitem"><p>Adobe Technical Note #5088 "Font Naming Issues."
	      This document discusses general font name issues. </p></li><li class="listitem"><p>Adobe's Unicode and Glyph Names guide.</p></li></ul></div></div></div></div>