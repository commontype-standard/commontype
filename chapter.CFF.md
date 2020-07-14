<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.CFF"></a>Chapter 19. CFF - PostScript font program (Compact Font Format) table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm332053815424"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.20.1.1"></a>Specification</h4></div></div></div><p>This table contains a compact representation of a
          PostScript Type 1, or CIDFont and is structured according to
          Adobe Technical Note #5176: <a class="ulink" href="http://partners.adobe.com/asn/developer/pdfs/tn/5176.CFF.pdf" target="_top">The
            Compact Font Format Specification</a> and Adobe
          Technical Note #5177: <a class="ulink" href="http://partners.adobe.com/asn/developer/pdfs/tn/5177.Type2.pdf" target="_top">The
            Type 2 Charstring Format</a>.</p><p>Existing TrueType fonts use a glyph index to specify and
          access glyphs within a font, e.g. to index the loca table
          and thereby access glyph data in the glyf table. This
          concept is retained in CommonType PostScript fonts except
          that glyph data is accessed through the CharStrings INDEX of
          the <a class="link" href="chapter.CFF.html" title="Chapter 19. CFF - PostScript font program (Compact Font Format) table">CFF</a> table.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.20.1.2"></a>Annotation</h4></div></div></div><p>The CFF specification was developed independantly of the
          CommonType specification and is also meant to be used in other
          contexts. Because of that, some CFF FontSets are not legal
          CFF tables. These restrictions should be part of the
          CommonType specification and are mentioned here:</p><p>It is unclear whether the deletion mechanism of CFF
          FontSets (by setting the first byte of a font name to 0) is
          allowed.  Given the intended use, it is not clear that such
          a mechanism is useful in CommonType fonts, and we assume that
          it is not allowed.</p><p>It is unclear which font in a CFF FontSet should be used
          in the context of an CommonType font. One possibility is to
          impose that the CFF FontSet contain only one font, with the
          side effect of ruling out synthetic fonts. Another
          possibility is to use the first font in the FontSet. Yet
          another possibility is to use the font whose name matches
          some entry in the <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table. We assume
          that the first possibility is actually the desired one.</p><p>It is not clear whether the name stored in the Name INDEX
          must be equal to some entry in the CommonType
          <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table.</p><p>While the Top DICT must define (explicitly or
          implicitly) an Encoding, this Encoding is never used. Thus
          the best is to not include an Encoding entry in the Top DICT
          and to get the default Standard Encoding, regardless of the
          font content.</p><p>Since Multiple Master technology is not part of
          CommonType, the Top DICT must not contain the operators
          BaseFontName and BaseFontBlend.</p></div></div></div>