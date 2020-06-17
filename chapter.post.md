<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.post"></a>Chapter 13. post - PostScript</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114628319456"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.13.1.1"></a>Specification</h3></div></div></div><p role="">This table contains additional information needed to use
        TrueType or OpenType fonts on PostScript printers.  This
        includes data for the FontInfo dictionary entry and the
        PostScript names of all the glyphs. For more information about
        PostScript names, see the Adobe document <a role="" class="ulink" href="http://partners.adobe.com/asn/developer/typeforum/unicodegm.html" target="_top">Unicode
        and Glyph Names</a>.</p><p role="">Versions 1.0, 2.0, and 2.5 refer to TrueType fonts and
          OpenType fonts with TrueType data. OpenType fonts with
          TrueType data may also use Version 3.0. OpenType fonts with
          CFF data use Version 3.0 only.</p><p role="">The table begins as follows:</p><div class="table"><a name="idm114628315280"></a><p class="title"><strong>Table 13.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">Version</td><td role="">
              <table border="0" summary="Simple list" role="" class="simplelist"><tr><td>0x00010000 for version 1.0</td></tr><tr><td>0x00020000 for version 2.0</td></tr><tr><td>0x00025000 for version 2.5
                  (deprecated)</td></tr><tr><td>0x00030000 for version 3.0</td></tr></table>
            </td><td class="auto-generated"> </td></tr><tr><td role="">Fixed</td><td role="">italicAngle</td><td role="">Italic angle in counter-clockwise degrees
              from the vertical. Zero for upright text, negative for
              text that leans to the right (forward).</td><td class="auto-generated"> </td></tr><tr><td role="">FWord</td><td role="">underlinePosition</td><td role="">This is the suggested distance of the top
              of the underline from the baseline (negative
              values indicate below baseline). The
              PostScript definition of this FontInfo dictionary key (the y
              coordinate of the center of the stroke) is not used for
              historical reasons. The value of the PostScript key may be
              calculated by subtracting half the underlineThickness from
              the value of this field.</td><td class="auto-generated"> </td></tr><tr><td role="">FWord</td><td role="">underlineThickness</td><td role="">Suggested values for the underline
              thickness.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">isFixedPitch</td><td role="">Set to 0 if the font is proportionally
              spaced, non-zero if the font is not proportionally
              spaced (i.e. monospaced).</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">minMemType42</td><td role="">Minimum memory usage when an OpenType font is
              downloaded.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">maxMemType42</td><td role="">Maximum memory usage when an OpenType font is
              downloaded.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">minMemType1</td><td role="">Minimum memory usage when an OpenType font is
              downloaded as a Type 1 font.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">maxMemType1</td><td role="">Maximum memory usage when an OpenType font is
              downloaded as a Type 1 font.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The last four entries in the table are present because
          PostScript drivers can do better memory management if the
          virtual memory (VM) requirements of a downloadable OpenType
          font are known before the font is downloaded. This
          information should be supplied if known. If it is not known,
          set the value to zero. The driver will still work but will
          be less efficient.</p><p role="">Maximum memory usage is minimum memory usage plus
          maximum runtime memory use. Maximum runtime memory use
          depends on the maximum band size of any bitmap potentially
          rasterized by the font scaler. Runtime memory usage could be
          calculated by rendering characters at different point sizes
          and comparing memory use.</p><p role="">If the version is 1.0 or 3.0, the table ends here. The
          additional entries for versions 2.0 and 2.5 are shown below.
          Apple has defined a version 4.0 for use with Apple's AAT
          (Apple Advanced Typography), which is described in their
          documentation.</p><h4><a name="idm114628294688"></a>Version 1.0</h4><p role="">This TrueType-based font file contains exactly the 258
          glyphs in the standard Macintosh TrueType font file (see
          <a role="" class="ulink" href="http://www.microsoft.com/typography/otspec/WGL4.htm" target="_top">The
            WGL4.0 Character Set</a> chapter for a list of the
          Macintosh glyphs). As a result, the glyph names are taken
          from the system with no storage required by the font.</p><h4><a name="idm114628292880"></a>Version 2.0</h4><p role="">This is the version required by TrueType-based fonts to
          be used on Windows.</p><div class="table"><a name="idm114628292000"></a><p class="title"><strong>Table 13.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">numberOfGlyphs</td><td role="">Number of glyphs (this should be the same as
              numGlyphs in <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a>
              table).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphNameIndex [numGlyphs]</td><td role="">This is not an offset, but is the ordinal
              number of the glyph in <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> string
              tables.</td><td class="auto-generated"> </td></tr><tr><td role="">CHAR</td><td role="">names [numberNewGlyphs]</td><td role="">Glyph names with length bytes [variable] (a
              Pascal string).</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This TrueType-based font file contains glyphs not in the
          standard Macintosh set or the ordering of the glyphs in the
          TrueType font file is non-standard (again, for the
          Macintosh). The glyph name array maps the glyphs in this
          font to name index. If the name index is between 0 and 257,
          treat the name index as a glyph index in the Macintosh
          standard order. If the name index is between 258 and 32767,
          then subtract 258 and use that to index into the list of
          Pascal strings at the end of the table. Thus a given font
          may map some of its glyphs to the standard glyph names, and
          some to its own names.</p><p role="">Index numbers 32768 through 65535 are reserved for
          future use. If you do not want to associate a PostScript
          name with a particular glyph, use index number 0 which
          points the name .notdef.</p><h4><a name="idm114628282320"></a>Version 2.5</h4><p role="">This version of the <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> table has
          been deprecated as of OpenType Specification v1.3.</p><p role="">This version provides a space saving table for
          TrueType-based fonts which contain a pure subset of, or a
          simple reordering of, the standard Macintosh glyph
          set.</p><div class="table"><a name="idm114628280208"></a><p class="title"><strong>Table 13.3. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">numberOfGlyphs</td><td role="">Number of glyphs</td><td class="auto-generated"> </td></tr><tr><td role="">CHAR</td><td role="">offset [numGlyphs]</td><td role="">Difference between graphic index and standard
              order of glyph</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This version is useful for TrueType-based font files
          that contain only glyphs in the standard Macintosh glyph set
          but which have those glyphs arranged in a non-standard order
          or which are missing some glyphs. The table contains one
          byte for each glyph in the font file. The byte is treated as
          a signed offset that maps the glyph index used in this font
          into the standard glyph index. In other words, assuming that
          the font contains the three glyphs A, B, and C which are the
          37th, 38th, and 39th glyphs in the standard ordering, the
          <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> table would contain the bytes +36,
          +36, +36. This format has been deprecated by Apple, as of
          February 2000.</p><h4><a name="idm114628273360"></a>Version 3.0</h4><p role="">This version is used by OpenType fonts with TrueType or
          CFF data. The version makes it possible to create a special
          font that is not burdened with a large
          <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> table set of glyph names.</p><p role="">This version specifies that no PostScript name
          information is provided for the glyphs in this font file.
          The printing behavior of this version on PostScript printers
          is unspecified, except that it should not result in a fatal
          or unrecoverable error. Some drivers may print nothing,
          other drivers may attempt to print using a default naming
          scheme.</p><p role="">Windows makes use of the italic angle value in the
          <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> table but does not actually
          <span role="" class="emphasis"><em>require</em></span> any glyph names to be stored as
          Pascal strings.</p></div></div></div>