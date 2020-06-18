<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.overview"></a>Chapter 1. Overview</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363769366896"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>The CommonType font format is an extension of the TrueType
	font format, adding support for PostScript font data. The
	CommonType font format is derived from the OpenType font format
  developed jointly by Microsoft and Adobe. CommonType fonts and the
  operating system services which
	support CommonType fonts provide users with a simple way to
	install and use fonts, whether the fonts contain TrueType
	outlines or CFF (PostScript) outlines.</p><p>The CommonType font format addresses the following goals:

	  </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>broader multi-platform support</p></li><li class="listitem"><p>better support for international character sets</p></li><li class="listitem"><p>better protection for font data</p></li><li class="listitem"><p>smaller file sizes to make font distribution more
	      efficient</p></li><li class="listitem"><p>broader support for advanced typographic control</p></li></ul></div><p>
      </p><p>CommonType fonts are also referred to as TrueType Open
	v.2.0 fonts, because they use the TrueType <code class="literal">sfnt</code> font file
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
	developer.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363769415952"></a>Related documentation</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>The following documents may be consulted for further
	information:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p><a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5176.CFF.pdf" target="_top">Adobe Technical Note #5176</a>: "The Compact Font Format
	      Specification."</p></li><li class="listitem"><p><a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5177.Type2.pdf" target="_top">Adobe Technical Note #5177</a>: "Type 2 Charstring Format."</p></li><li class="listitem"><p><a class="link" href="https://docs.microsoft.com/en-us/typography/opentype/spec/" target="_top">The OpenType Specification</a>. Microsoft.</p></li><li class="listitem"><p>Adobe Type 1 Font Format. Addison Wesley, 1991; ISBN
	      0-201-57044-0.</p></li><li class="listitem"><p><a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5015.Type1_Supp.pdf" target="_top">Adobe Technical Note #5015</a>: "The Type 1 Font Format
	      Supplement." This document contains all updates to the
	      Type 1 format.</p></li><li class="listitem"><p><a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/postscript/pdfs/5087.MM_Fond.pdf" target="_top">Adobe Technical Note #5087</a>: "Multiple Master Font
	      Programs for the Macintosh."</p></li><li class="listitem"><p><a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5088.FontNames.pdf" target="_top">Adobe Technical Note #5088</a>: "Font Naming Issues."
	      This document discusses general font name issues. </p></li><li class="listitem"><p>The <a class="link" href="https://github.com/adobe-type-tools/agl-specification" target="_top">Adobe Glyph List Specification</a>.</p></li></ul></div></div></div></div>