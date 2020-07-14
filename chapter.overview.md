<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.overview"></a>Chapter 1. Overview</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465838692144"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>The CommonType font format is a file format for representing
        font data, including <em class="glossterm">glyph representations</em>,
        layout instructions, and other metadata. The CommonType font format
        derived from the OpenType font format, developed jointly by Microsoft
        and Adobe.</p><p>CommonType fonts <em class="glossterm">may</em> include
        <em class="glossterm">CommonType Layout Tables</em>, which allow font
        creators to contextually substitute and reposition glyphs during
        text layout, enabling support for advanced typographic refinement
        and language support.
        CommonType fonts allow the handling of large glyph sets using Unicode
        encoding. Such encoding allows for broad international support.
      </p><p>
        Additionally, CommonType fonts may contain digital signatures, which
        allows operating systems and browsing applications to identify the
        source and integrity of font files, including embedded font files
        obtained in web documents, before using them. Also, font developers
        can encode embedding restrictions in CommonType fonts, and these
        restrictions cannot be altered in a font signed by the developer.
       </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465838686960"></a>Definitions</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>
        The key words <em class="glossterm">must</em>,
        <em class="glossterm">must not</em>, <em class="glossterm">required</em>,
        <em class="glossterm">shall</em>, <em class="glossterm">shall not</em>,
        <em class="glossterm">should</em>, <em class="glossterm">should not</em>,
        <em class="glossterm">recommended</em>, <em class="glossterm">may</em>,
        and <em class="glossterm">optional</em> in this specification are to
        be interpreted as described in
        <a class="link" href="https://www.ietf.org/rfc/rfc2119.txt" target="_top">RFC 2119</a>.
        Note that for reasons of style, these words are not capitalized in this document.
      </p><p>
        Further key words are defined in the Glossary.
      </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465838679664"></a>Related documentation</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>The following documents may be consulted for further
  information:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>
            <a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5176.CFF.pdf" target="_top">Adobe Technical Note #5176</a>: "The Compact Font Format
        Specification."</p></li><li class="listitem"><p>
            <a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5177.Type2.pdf" target="_top">Adobe Technical Note #5177</a>: "Type 2 Charstring Format."</p></li><li class="listitem"><p>
            <a class="link" href="https://docs.microsoft.com/en-us/typography/opentype/spec/" target="_top">The OpenType Specification</a>. Microsoft.</p></li><li class="listitem"><p>Adobe Type 1 Font Format. Addison Wesley, 1991; ISBN
        0-201-57044-0.</p></li><li class="listitem"><p>
            <a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/postscript/pdfs/5087.MM_Fond.pdf" target="_top">Adobe Technical Note #5087</a>: "Multiple Master Font
        Programs for the Macintosh."</p></li><li class="listitem"><p>
            <a class="link" href="https://www.adobe.com/content/dam/acom/en/devnet/font/pdfs/5088.FontNames.pdf" target="_top">Adobe Technical Note #5088</a>: "Font Naming Issues."
        Discusses general font name issues. </p></li><li class="listitem"><p>The <a class="link" href="https://github.com/adobe-type-tools/agl-specification" target="_top">Adobe Glyph List Specification</a>.</p></li></ul></div></div></div></div>