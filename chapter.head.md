<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.head"></a>Chapter 6. head - Font Header</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114629937968"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.6.1.1"></a>Specification</h3></div></div></div><p role="">This table gives global information about the font. The
          bounding box values should be computed using
          <span role="" class="emphasis"><em>only</em></span> glyphs that have contours. Glyphs
          with no contours should be ignored for the purposes of these
          calculations.</p><div class="table"><a name="idm114629935200"></a><p class="title"><strong>Table 6.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">Table version number</td><td role="">0x00010000 for version 1.0.</td><td class="auto-generated"> </td></tr><tr><td role="">Fixed</td><td role="">fontRevision</td><td role="">Set by font manufacturer.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">checkSumAdjustment</td><td role="">To compute: set it to 0, sum the entire font
              as ULONG, then store 0xB1B0AFBA - sum.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">magicNumber</td><td role="">Set to 0x5F0F3CF5.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">flags</td><td role=""><table border="0" summary="Simple list" role="" class="simplelist"><tr><td>Bit 0: baseline for font at y=0;</td></tr><tr><td>Bit 1: left sidebearing at x=0;</td></tr><tr><td>Bit 2: instructions may depend on point
                  size;</td></tr><tr><td>Bit 3: force ppem to integer values for all internal
                  scaler math; may use fractional ppem sizes if this bit is
                  clear;</td></tr><tr><td>Bit 4: instructions may alter advance width (the
                  advance widths might not scale linearly);</td></tr><tr><td>Bits 5-10: These should be set according to
                  <a role="" class="ulink" href="http://developer.apple.com/fonts/TTRefMan/RM06/Chap6head.html" target="_top">Apple's specification</a>. However, they are not
                  implemented in OpenType.</td></tr><tr><td>Bit 11: font data is 'lossless,' as a result of
                  having been compressed and decompressed with the Agfa
                  MicroType Express engine.</td></tr><tr><td>Bit 12: font converted (produce compatible
                  metrics).</td></tr><tr><td>Bit 13: Font optimized for ClearType.</td></tr><tr><td>Bit 14: Reserved, set to 0.</td></tr><tr><td>Bit 15: Reserved, set to 0.</td></tr></table>
            </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">unitsPerEm</td><td role="">Valid range is from 16 to
              16384. This value should be a power of 2 for fonts that
            have TrueType outlines.</td><td class="auto-generated"> </td></tr><tr><td role="">LONGDATETIME</td><td role="">created</td><td role="">Number of seconds since 12:00 midnight,
              January 1, 1904. 64-bit integer.</td><td class="auto-generated"> </td></tr><tr><td role="">LONGDATETIME</td><td role="">modified</td><td role="">Number of seconds since 12:00 midnight,
              January 1, 1904. 64-bit integer.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xMin</td><td role="">For all glyph bounding boxes.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMin</td><td role="">For all glyph bounding boxes.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xMax</td><td role="">For all glyph bounding boxes.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMax</td><td role="">For all glyph bounding boxes.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">macStyle</td><td role="">
	      <table border="0" summary="Simple list" role="" class="simplelist"><tr><td>Bit 0: Bold (if set to 1);</td></tr><tr><td>Bit 1: Italic (if set to 1)</td></tr><tr><td>Bit 2: Underline (if set to 1)</td></tr><tr><td>Bit 3: Outline (if set to 1)</td></tr><tr><td>Bit 4: Shadow (if set to 1)</td></tr><tr><td>Bit 5: Condensed (if set to 1)</td></tr><tr><td>Bit 6: Extended (if set to 1)</td></tr><tr><td>Bits 7-15: Reserved (set to 0)</td></tr></table>
            </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">lowestRecPPEM</td><td role="">Smallest readable size in
              pixels.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">fontDirectionHint</td><td role="">
                  <table border="0" summary="Simple list" role="" class="simplelist"><tr><td>0: Fully mixed directional
                      glyphs;</td></tr><tr><td>1: Only strongly left to right;</td></tr><tr><td>2: Like 1 but also contains
                      neutrals;</td></tr><tr><td>-1: Only strongly right to left;</td></tr><tr><td>-2: Like -1 but also contains
                      neutrals<a href="#ftn.idm114629898864" class="footnote" id="idm114629898864"><sup class="footnote">[a]</sup></a>.</td></tr></table>
            </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">indexToLocFormat</td><td role="">0 for short offsets, 1 for
              long.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">glyphDataFormat</td><td role="">0 for current format.</td><td class="auto-generated"> </td></tr></tbody><tbody class="footnotes"><tr><td colspan="4"><div id="ftn.idm114629898864" role="" class="footnote"><p role=""><a href="#idm114629898864" class="para"><sup class="para">[a] </sup></a>A neutral character has no inherent
                          directionality; it is not a character with
                          zero (0) width. Spaces and punctuation are
                          examples of neutral characters. Non-neutral
                          characters are those with inherent
                          directionality. For example, Roman letters
                          (left-to-right) and Arabic
                          letters(right-to-left) have directionality.
                          In a "normal" Roman font where spaces and
                          punctuation are present, the font direction
                          hints should be set to two (2).</p></div></td></tr></tbody></table></div></div><br class="table-break"/><p role=""/><p role="">Note that macStyle bits must agree with the
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table fsSelection bits. The
          fsSelection bits are used over the macStyle bits in
          Microsoft Windows. The PANOSE values and
          <a role="" class="link" href="chapter.post.md" title="Chapter 13. post - PostScript">post</a> table values are ignored for
          determining bold or italic fonts.</p><p role="">For historical reasons, the fontRevision value contained
          in this table is not used by Windows to determine the
          version of a font. Instead, Windows evaluates the version
          string (id 5) in the <a role="" class="link" href="chapter.name.md" title="Chapter 10. name - Naming Table">name</a> table.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.6.1.2"></a>Annotation</h3></div></div></div><p role="">It seems that Table version number is set to 'OTTO' for
          CFF based fonts.</p></div></div></div>