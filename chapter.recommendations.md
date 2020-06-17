<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.recommendations"></a>Chapter 40. Recommendations for OpenType Fonts</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792670336"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.1.1"></a>Specification</h3></div></div></div><p role="">This chapter outlines recommendations for creating
          OpenType fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792667616"></a>Byte Ordering</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.2.1"></a>Specification</h3></div></div></div><p role="">All OpenType fonts use Motorola-style byte ordering (Big
          Endian).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792664784"></a>'sfnt' Version</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.3.1"></a>Specification</h3></div></div></div><p role="">OpenType fonts that contain TrueType outlines should use
          the value of 1.0 for the sfnt version. OpenType fonts
          containing CFF data should use the tag 'OTTO' as the sfnt
          version number.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792661808"></a>Mixing Outline Formats</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.4.1"></a>Specification</h3></div></div></div><p role="">Both Microsoft and Adobe recommend against mixing
          outline formats within a single font. Choose the format that
          meets your feature requirements.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792658864"></a>Filenames</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.5.1"></a>Specification</h3></div></div></div><p role="">OpenType fonts may have the extension .OTF, .TTF, or .TTC,
          depending on the type of outlines in the font and the
	  presence of OpenType layout tables.</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">Fonts with CFF data always have an .OTF
              extension.</p></li><li role="" class="listitem"><p role="">Fonts containing TrueType outlines that have
            OpenType layout tables should use the .OTF extension when
            backward compatibility is not an issue. Fonts without
            OpenType layout tables, or fonts that have backward
            compatibility issues should use the .TTF
            extension. TrueType Collection fonts should have a .TTC
            extension whether or not the fonts have OpenType layout
            tables present.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792653472"></a>Table Alignment and Length</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.6.1"></a>Specification</h3></div></div></div><p role="">All tables should be aligned to begin at offsets which
          are multiples of four bytes. While this is not required by
          the TrueType rasterizer, it does prevent ambiguous checksum
          calculations and greatly speeds table access on some
          processors.</p><p role="">All tables should be recorded in the table directory
          with their actual length. To ensure that checksums are
          calculated correctly, it is suggested that tables begin on
          LONG word boundries. Any extra space after a table (and
          before the next LONG word boundry) should be padded with
          zeros.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792649680"></a>First Four Glyphs in Fonts</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.7.1"></a>Specification</h3></div></div></div><p role="">TrueType outline fonts should have the following four
	  glyphs at the glyph ID indicated. These were listed in
	  Apple's original TrueType specification. These glyphs are
	  recommended to allow for the same version of the font to
	  work on both Windows and Macintosh. Fonts used on the Mac
	  should be put in a suitcase for the best user
	  experience.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th role="">Glyph ID</th><th role="">Glyph name</th><th role="">Unicode value</th></tr></thead><tbody><tr><td role="">0</td><td role="">.notdef</td><td role="">undefined</td></tr><tr><td role="">1</td><td role="">.null</td><td role="">U+0000</td></tr><tr><td role="">2</td><td role="">CR</td><td role="">U+000D</td></tr><tr><td role="">3</td><td role="">space</td><td role="">U+0020</td></tr></tbody></table></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792636944"></a>Shape of .notdef glyph</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.8.1"></a>Specification</h3></div></div></div><p role="">The .notdef glyph is very important for providing the
	  user feedback that a glyph is not found in the font. This
	  glyph should not be left without an outline as the user will
	  only see what looks like a space if a glyph is missing and
	  not be aware of the active font's limitation.</p><p role="">It is recommended that the shape of the .notdef glyph be
	  either an empty rectangle, a rectangle with a question mark
	  inside of it, or a rectangle with an "X". Creative shapes,
	  like swirls or other symbols, may not be recognized by users
	  as indicating that a glyph is missing from the font and is
	  not being displayed at that location.</p><div class="figure"><a name="idm80792633696"></a><p class="title"><strong>Figure 40.1. Suggested shapes of .notdef glyph</strong></p><div class="figure-contents"><div role="" class="mediaobject"><img src="src/images/notdef.gif" alt="Suggested shapes of .notdef glyph"/></div></div></div><br class="figure-break"/></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792631040"></a>BASE Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.9.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table allows for different
          scripts in the font to specify different values for the same
          baseline tag.  This situation could arise when a developer
          makes a Unicode font, for example, by combining glyphs from
          fonts that use different baseline systems.</p><p role="">However, glyphs from different scripts in this font may
          not appear correctly aligned relative to each other when
          used with applications that either don't support the
          <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table or that support it but
          assume that a particular baseline will not vary across
          scripts. Furthermore, it is not always possible to determine
          the script of every glyph in the font, some
          "weakly-scripted" characters such as punctuation may be used
          in several scripts, and some glyphs such as ornaments may
          not have a script at all.</p><p role="">Thus, it is strongly recommended that developers
          construct their fonts so that all scripts in the
          <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table record the same value for a
          particular baseline if they want their fonts to work as
          expected in the above situations.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792624384"></a>cmap Table </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.10.1"></a>Specification</h3></div></div></div><p role="">When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1 (this
          subtable must use cmap format 4). When building a symbol
          font for Windows, the platform ID should be 3 and the
          encoding ID should be 0.</p><p role="">When building a font to support surrogate characters
          i.e. the UCS-4 (4 byte) form of ISO 10646 (ISO 10646 UCS-4
          contains 2^31 code positions and the Unicode transformation
          formats UTF-8 and UTF-16 access a subset of these code
          positions using surrogate characters), use platform ID 3,
          encoding ID 10 and format 12. Depending on support installed
          and the content of text being displayed, Windows 2000 may
          use either the format 4 or format 12 cmap. Therefore the
          first 64k codepoint to glyph mappings must be identical for
          any font containing both cmap format 4 and format 12. Please
          note, that the content of format 12 subtable, needs to be a
          super set of the content in the format 4 subtable. The
          format 4 subtable needs to be included, for backward
          compatibility needs.</p><p role="">The number of glyphs that may be included in one font is
          limited to 64k.</p><p role="">Remember that, despite references to 'first' and
          'second' subtables, the subtables must be stored in sorted
          order by platform and encoding ID.</p><p role="">Macintosh <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> Table</p><p role="">When building a font containing Roman characters that
          will be used on the Macintosh, an additional subtable is
          required, specifying platform ID of 1 and encoding ID of 0
          (this subtable may use cmap formats 0, 2, 4, or 6).</p><p role="">In order for the Macintosh <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table to be useful,
          the glyphs required for the Macintosh must have glyph
          indices less than 256 (since the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable format 0
          uses BYTE indices and therefore cannot index any glyph above
          255).</p><p role="">The Apple <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable should be constructed
          according to Apple guidelines.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792615152"></a>cvt Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.11.1"></a>Specification</h3></div></div></div><p role="">Should be defined only if required by font
          instructions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792612320"></a>fpgm Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.12.1"></a>Specification</h3></div></div></div><p role="">Should be defined only if required by TrueType font
          instructions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792609488"></a>glyf Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.13.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> table contains TrueType
          outline data, and can be optimized by Agfa MicroType
          Compression. Microsoft recommends that developers perform
          this optimization, using a tool provided by Microsoft, prior
          to finalizing and adding a digital signature to the font.
          This is necessary for the creator's signature to remain
          valid in embedded OpenType fonts.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792605664"></a>hdmx Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.14.1"></a>Specification</h3></div></div></div><p role="">This table improves the performance of OpenType fonts
          with TrueType outlines. This table is not necessary at all
          unless instructions are used to control the "phantom
          points," and should be omitted if bit 2 of the flags field
          in the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table is zero. (See the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table
          documentation in Chapter 2.) Microsoft recommends that this
          table be included for fonts with one or more non-linearly
          scaled glyphs (i.e., bit 2 and 4 of the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table flags
          field are set).</p><p role="">Device records should be defined for all sizes from 8
          through 14 point, and even point sizes from 16 through 24
          point. However, the table requires pixel-per-em sizes, which
          depend on the horizontal resolution of the output device.
          The records in <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> should cover both 96 dpi devices (CGA,
          EGA, VGA) and 300 dpi devices (laser and ink jet
          printers).</p><p role="">Thus, <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> should contain entries for the following
          pixel sizes (PPEM): 11, 12, 13, 15, 16, 17, 19, 21, 24, 27, 29, 32,
          33, 37, 42, 46, 50, 54, 58, 67, 75, 83, 92, 100. These
          values have been rounded to the nearest pixel. For instance,
          12 points at 300 dpi would measure 37.5 pixels, but this is
          rounded down to 37 for this list. </p><p role="">This will add approximately 9,600 bytes to the font
          file. However, there will be a significant improvement in
          speed when a client requests advance widths covered by these
          device records.</p><p role="">If the font includes an <a role="" class="link" href="chapter.LTSH.html" title="Chapter 34. LTSH - Linear Threshold">LTSH</a> table, the hdmx values
          are not needed above the linearity threshold.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792595808"></a>head Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.15.1"></a>Specification</h3></div></div></div><p role="">Although historical usage of the fontRevision value is
          varied, the recommended use of the field is to set it as a
          Fixed 16.16 value, and to report it rounded and zero-padded
          to three fractional decimal places. Examples: Decimal 1.5 is
          set as 0x00018000 and is reported as "1.500"; decimal 1.001
          is set as 0x00010041 and is reported as "1.001". All data
          required. If the font has been compressed with Agfa
          MicroType Compression, this must be indicated in the flags
          field of the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792591840"></a>hhead Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.16.1"></a>Specification</h3></div></div></div><p role="">All data required. It is suggested that monospaced fonts
          set numberOfHMetrics to three (see hmtx).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792588976"></a>hmtx Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.17.1"></a>Specification</h3></div></div></div><p role="">All data required. It is suggested that monospaced fonts
          have three entries in the numberOfHMetrics field. OpenType
          fonts that include CFF data must set numberOfHMetrics equal
          to the number of glyphs in the font and therefore cannot use
          the "repeat last width" optimization normally available
          within the <a role="" class="link" href="chapter.hmtx.html" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a> table.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792585200"></a>kern Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.18.1"></a>Specification</h3></div></div></div><p role="">Should contain a single kerning pair subtable (format
          0). Windows will not support format 2 (two-dimensional array
          of kern values by class); nor multiple tables (only the
          first format 0 table found will be used) nor coverage bits 0
          through 4 (i.e. assumes horizontal data, kerning values, no
          cross stream, and override). OpenType fonts containing CFF
          data do not support the <a role="" class="link" href="chapter.kern.html" title="Chapter 33. kern - Kerning">kern</a> table and should therefore
          specify kerning data using the <a role="" class="link" href="chapter.GPOS.html" title="Chapter 24. GPOS - The Glyph Positioning Table">GPOS</a> table
          (LookupType=2).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792580592"></a>loca Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.19.1"></a>Specification</h3></div></div></div><p role="">All data required for fonts with TrueType outlines. We
          recommend that local offsets should be word-aligned, in both
          the short and long formats of this table.</p><p role="">The actual ordering of the glyphs in the font can be
          optimized based on expected utilization, with the most
          frequently used glyphs appearing at the beginning of the
          font file. Additionally, glyphs that are often used together
          should be grouped together in the file. The will help to
          minimize the amount of swapping required when the font is
          loaded into memory.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792576832"></a>LTSH Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.20.1"></a>Specification</h3></div></div></div><p role="">This table improves the performance of OpenType fonts
          with TrueType outlines. The table should be used if bit 2 or
          4 of flags in <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> is set.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792573264"></a>maxp Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.21.1"></a>Specification</h3></div></div></div><p role="">All data required for a font with TrueType outlines.
          Fonts with CFF data must only fill the numGlyphs
          field.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792570368"></a>'name' Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.22.1"></a>Specification</h3></div></div></div><p role="">Platform and encoding ID's in the name table should be
          consistent with those in the cmap table. If they are not,
          the font will not load in Windows. When building a Unicode
          font for Windows, the platform ID should be 3 and the
          encoding ID should be 1. When building a symbol font for
          Windows, the platform ID should be 3 and the encoding ID
          should be 0.</p><p role="">When building a font containing Roman characters that
          will be used on the Macintosh, an additional name record is
          required, specifying platform ID of 1 and encoding ID of
          0.</p><p role="">Each set of name records should appear for US English
          (language ID = 0x0409 for Microsoft records, language ID = 0
          for Macintosh records); additional language strings for the
          Microsoft set of records (platform ID 3) may be added at the
          discretion of the font vendor.</p><p role="">Remember that, despite references to "first" and
          "second," the name record must be stored in sorted order (by
          platform ID, encoding ID, language ID, name ID). The 'name'
          table platform/encoding IDs must match the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table
          platform/encoding IDs, which is how Windows knows which name
          set to use.</p><p role="">Name strings</p><p role="">We recommend using name ID's 8-12, to identify
          manufacturer, designer, description, URL of the vendor, and
          URL of the designer. URL's must contain the protocol of the
          site: for example, http:// or mailto: or ftp://. The
          OpenType font properties extension can enumerate this
          information to the users.</p><p role="">The Subfamily string in the 'name' table should be used
          for variants of weight (ultra light to extra black) and
          style (oblique/italic or not). So, for example, the full
          font name of "Helvetica Narrow Italic" should be defined as
          Family name "Helvetica Narrow" and Subfamily "Italic". This
          is so that Windows can group the standard four weights of a
          font in a reasonable fashion for non-typographically aware
          applications which only support combinations of "bold" and
          "italic."</p><p role="">The Full font name string usually contains a
          concatenation of strings 1 and 2. However, if the font is
          'Regular' as indicated in string 2, then use only the family
          name contained in string 1. This is the font name that
          Windows will expose to users.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792561744"></a>OS/2 Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.23.1"></a>Specification</h3></div></div></div><p role="">All data required. We recommend applying PANOSE values
          to fonts to improve the user's experience when using the
          Windows fonts folder or other font management utilities. If
          the font is a symbol font, the first byte of the PANOSE
          value must be set to 'decorative.' The PANOSE evaluation
          document is on-line at
          www.fonts.com/hp/panose/greybook/frame.htm.</p><p role="">sTypoAscender, sTypoDescender and sTypoLineGap</p><p role="">sTypoAscender is used to determine the optimum offset
          from the top of a text frame to the first baseline.
          sTypoDescender is used to determine the optimum offset from
          the last baseline to the bottom of the text frame. The value
          of (sTypoAscender - sTypoDescender) is recommended to equal
          one em.</p><p role="">While the OpenType specification allows
          for CJK (Chinese, Japanese, and Korean) fonts'
          sTypoDescender and sTypoAscender fields to specify metrics
          different from the HorizAxis.ideo and HorizAxis.idtp
          baselines in the <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table, CJK font
          developers should be aware that existing applications may
          not read the <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table at all but
          simply use the sTypoDescender and sTypoAscender fields to
          describe the bottom and top edges of the ideographic
          em-box. If developers want their fonts to work correctly
          with such applications, they should ensure that any
          ideographic em-box values in the <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a>
          table describe the same bottom and top edges as the
          sTypoDescender and sTypoAscender fields. See the sections
          "OpenType CJK Font Guidelines" and "Ideographic Em-Box" for
          more details.</p><p role="">For Western fonts, the Ascender
          and Descender fields in Type 1 fonts' AFM files are a good
          source of sTypoAscender and sTypoDescender,
          respectively. The Minion Pro font family (designed on a
          1000-unit em), for example, sets sTypoAscender = 727 and
          sTypoDescender = -273.</p><p role="">sTypoAscender,
          sTypoDescender and sTypoLineGap specify the recommended line
          spacing for single-spaced horizontal text. The
          baseline-to-baseline value is expressed by:</p><p role="">OS/2.sTypoAscender - OS/2.sTypoDescender +
          OS/2.sTypoLineGap</p><p role="">sTypoLineGap will usually be
          set by the font developer such that the value of the above
          expression is approximately 120% of the em. The application
          can use this value as the default horizontal line
          spacing. The Minion Pro font family (designed on a 1000-unit
          em), for example, sets sTypoLineGap = 200.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792551632"></a>post Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.24.1"></a>Specification</h3></div></div></div><p role="">All information required, although the VM Usage fields
          may be set to zero. OpenType fonts containing CFF outlines
          use only format 3.0 of the <a role="" class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table. Glyph names must be
          assigned as described in the Adobe document "Unicode and
          Glyph Names," which specifies glyph naming conventions for
          all Unicode characters as well as those that don't have
          standard Unicode values such as certain ligatures or glyphic
          variants. Note that names for all glyphs must be supplied as
          it cannot be assumed that all Microsoft platforms will
          support the default names supplied on the Macintosh.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792547552"></a>prep Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.25.1"></a>Specification</h3></div></div></div><p role="">Should be defined only if required by the TrueType font
          instructions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792544720"></a>VDMX Table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.26.1"></a>Specification</h3></div></div></div><p role="">This table improves the performance of OpenType fonts
          with TrueType outlines. It Should be present if hints cause
          the font to scale non-linearly. If not present, the font is
          assumed to scale linearly. Clipping may occur if values in
          this table are absent and font exceeds linear height.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792541632"></a>Optimized Table Ordering</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.27.1"></a>Specification</h3></div></div></div><p role="">OpenType fonts with TrueType outlines are more efficient
          in the Windows operating system when the tables are ordered
          as follows (from first to last):</p><p role="">head, hhea, maxp, OS/2, hmtx, LTSH, VDMX, hdmx, cmap,
          fpgm, prep, cvt, loca, <a role="" class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a>, kern, name,
          post, gasp, PCLT, DSIG</p><p role="">The initial loading of an OpenType font containing CFF
          data will be more efficiently handled if the following sfnt
          table ordering is used within the body of the sfnt (listed
          from first to last):</p><p role="">head, hhea, maxp, OS/2, name, cmap, post, CFF, (other
          tables, as convenient)</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792536416"></a>Non-Standard (Symbol) Fonts</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.28.1"></a>Specification</h3></div></div></div><p role="">Non-standard fonts such as Symbol or Wingdings(tm) have
          special requirements for Microsoft platforms. These
          requirements affect the 'cmap,' 'name,' and <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> tables;
          the requirements and recommendations for all other tables
          remain the same.</p><p role="">For the Macintosh, non-standard fonts can continue to
          use platform ID 1 (Macintosh) and encoding ID 0 (Roman
          character set). The <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable should use format 0 and
          follow the standard PostScript character encodings.</p><p role="">For non-standard fonts on Microsoft platforms, however,
          the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> and 'name' tables must use platform ID 3
          (Microsoft) and encoding ID 0 (Unicode, non-standard
          character set). Remember that 'name' table encodings should
          agree with the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table. Additionally, the first byte of
          the PANOSE value in the <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table must be set to
          'decorative.'</p><p role="">The Microsoft <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable (platform 3, encoding 0)
          must use format 4. The character codes should start at
          0xF000, which is in the Private Use Area of Unicode.
          Microsoft suggests deriving the format 4 (Microsoft)
          encodings by simply adding 0xF000 to the format 0
          (Macintosh) encodings.</p><p role="">Under Windows, only the first 224 characters of
          non-standard fonts will be accessible: a space and up to 223
          printing characters. It does not matter where in user space
          these start, but 0xF020 is suggested. The usFirstCharIndex
          and usLastCharIndex values in the <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table would be set
          based on the actual minimum and maximum character indices
          used.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792525920"></a>Device Resolutions</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.29.1"></a>Specification</h3></div></div></div><p role="">Windows makes use of a logical device resolution. The
          physical resolution of a device is also available, but fonts
          will be rendered based on the logical resolution. The table
          below lists some important logical resolutions in dots per
          inch (Horizontal x Vertical). The most important ratios (in
          order) are 1:1, 1.67:1 and 1.33:1.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Device</th><th role="">Resolution</th><th role="">Aspect Ratio</th></tr></thead><tbody><tr><td role="">CGA</td><td role="">96 x 48</td><td role="">2:1</td></tr><tr><td role="">EGA</td><td role="">96 x 72</td><td role="">1.33:1</td></tr><tr><td role="">VGA</td><td role="">96 x 96</td><td role="">1:1</td></tr><tr><td role="">8514</td><td role="">120 x 120</td><td role="">1:1</td></tr><tr><td role="">Dot Matrix</td><td role="">120 x 72</td><td role="">1.67:1</td></tr><tr><td role="">Laser Printer</td><td role="">300 x 300</td><td role="">1:1</td></tr><tr><td role="">Laser Printer</td><td role="">600 x 600</td><td role="">1:1</td></tr></tbody></table></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792506960"></a>Baseline to Baseline Distances</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.30.1"></a>Specification</h3></div></div></div><p role="">The <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table fields sTypoAscender, sTypoDescender,
          and sTypoLineGap free applications from Macintosh- or
          Windows-specific metrics which are constrained by backward
          compatibility requirements. The following discussion only
          pertains to the platform-specific metrics.</p><p role="">The suggested Baseline to Baseline Distance (BTBD) is
          computed differently for Windows and the Macintosh, and it
          is based on different OpenType metrics. However, if the
          recommendations below are followed, the BTBD will be the
          same for both Windows and the Mac.</p><p role="">Windows</p><p role="">The Windows metrics in the table below are returned as
          part of the logical font data structure by the GDI
          CreateLogFont( ) API.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Windows Metric</th><th role="">OpenType Metric</th></tr></thead><tbody><tr><td role="">ascent</td><td role="">usWinAscent</td></tr><tr><td role="">descent</td><td role="">usWinDescent</td></tr><tr><td role="">internal leading</td><td role="">usWinAscent + usWinDescent - unitsPerEm</td></tr><tr><td role="">external leading</td><td role="">MAX(0, LineGap - ((usWinAscent + usWinDescent)
                  - (Ascender - Descender)))</td></tr></tbody></table></div><p role="">The suggested BTBD = ascent + descent + external
          leading</p><p role="">It should be clear that the "external leading" can never
          be less than zero. Pixels above the ascent or below the
          descent will be clipped from the character; this is true for
          all output devices.</p><p role="">The usWinAscent and usWinDescent are values from the
          <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table. The unitsPerEm value is from
          the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table. The LineGap, Ascender and
          Descender values are from the <a role="" class="link" href="chapter.hhea.html" title="Chapter 7. hhea - Horizontal Header">hhea</a>
          table.</p><p role="">Macintosh</p><p role="">Ascender and Descender are metrics defined by Apple and
          are not to be confused with the Windows ascent or descent,
          nor should they be confused with the true typographic
          ascender and descender that are found in AFM files. The
          Macintosh metrics below are returned by the Apple Advanced
          Typography (AAT) GetFontInfo () API.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Macintosh Metric</th><th role="">OpenType Metric</th></tr></thead><tbody><tr><td role="">ascender</td><td role="">Ascender</td></tr><tr><td role="">descender</td><td role="">Descender</td></tr><tr><td role="">leading</td><td role="">LineGap</td></tr></tbody></table></div><p role="">The suggested BTBD = ascent + descent + leading</p><p role="">If pixels extend above the ascent or below the descent,
          the character will be squashed in the vertical direction so
          that all pixels fit within these limitations; this is true
          for screen display only.</p><p role="">Making Them Match</p><p role="">If you perform some simple algebra, you will see that
          the suggested BTBD across both Macintosh and Windows will be
          identical if and only if:</p><p role="">LineGap &gt;= (yMax - yMin) - (Ascender - Descender)</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792478016"></a>Style Bits</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.31.1"></a>Specification</h3></div></div></div><p role="">For backwards compatibility with previous versions of
          Windows, the macStyle bits in the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table will be used
          to determine whetr or not a font is regular, bold or
          italic (in the absence of an <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table). This is
          completely independent of the usWeightClass and PANOSE
          information in the <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table, the ItalicAngle in the
          <a role="" class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table, and all other related metrics. If the <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a>
          table is present, then the fsSelection bits are used to
          determine this information.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792471504"></a>Drop-out Control</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.32.1"></a>Specification</h3></div></div></div><p role="">Drop-out control is needed if there is a difference in
          bitmaps with dropout control on and off. Two cases where
          drop-out control is needed are when the font is rotated or
          when the size of the font is at or below 8 ppem. Do not use
          SCANCTRL unless needed. SCANCTRL or the drop-out control
          rasterizer should be avoided for Roman fonts above 8 points
          per em (ppem) when the font is not under rotation. SCANCTRL
          should not be used for "stretched" fonts (e.g. fonts
          displayed at non-square aspect ratios, like that found on an
          EGA).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792468112"></a>Embedded Bitmaps</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.33.1"></a>Specification</h3></div></div></div><p role="">Three tables are used to embed bitmaps in OpenType
          fonts. They are the <a role="" class="link" href="chapter.EBLC.html" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> table for
          embedded bitmap locators, the <a role="" class="link" href="chapter.EBDT.html" title="Chapter 27. EBDT - Embedded Bitmap Data Table">EBDT</a> table
          for embedded bitmap data, and the <a role="" class="link" href="chapter.EBSC.html" title="Chapter 29. EBSC - Embedded Bitmap Scaling Table">EBSC</a>
          table for embedded bitmap scaling information.  OpenType
          embedded bitmaps are also called 'sbits'.</p><p role="">The behavior of sbits within an OpenType font is essentially
          transparent to the client. A client need not be aware
          whether the bitmap returned by the rasterizer comes from an
          sbit or from a scan-converted outline.</p><p role="">The metrics in 'sbit' tables overrule the outline
          metrics at all sizes where sbits are defined. Fonts with
          <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> tables should correct those tables
          with 'sbit' values.</p><p role="">'Sbit only' fonts, that is fonts with embedded bitmaps
          but without outline data, are permitted. Care must be taken
          to ensure that all required OpenType tables except
          <a role="" class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> and <a role="" class="link" href="chapter.loca.html" title="Chapter 17. loca - Index to Location">loca</a> are
          present in such a font. Obviously, such fonts will only be
          able to return glyphs and sizes for which sbits are
          defined.</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">These metrics are returned as part of the logical
              font data structure by the GDI CreateLogFont()
              API.</p></li><li role="" class="listitem"><p role="">These metrics are returned by the Apple Advanced
              Typography (AAT) GetFontInfo() API.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80792456976"></a>OpenType CJK Font Guidelines</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.40.34.1"></a>Specification</h3></div></div></div><p role="">This section provides a checklist of links to various
          CJK-related sections of the OpenType specification. Some
          items are requirements; others, recommendations:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">The ideographic em-box of an OpenType font will be
              determined as described in the section "Ideographic
              Em-Box" in the Baseline Tags section of the OpenType
              Layout Tag Registry. Also see the description for
              OS/2.sTypoAscender and OS/2.sTypoDescender, and the
              <a role="" class="link" href="chapter.BASE.html" title="Chapter 22. BASE - Baseline Table">BASE</a> table recommendation section
              above.</p></li><li role="" class="listitem"><p role="">CJK font vendors can choose to provide the
              ideographic character face (ICF) metrics, which
              applications can use for accurate text alignment. This
              is described in the section "Ideographic Character Face"
              in the Baseline Tags section of the OpenType Layout Tag
              Registry.</p></li><li role="" class="listitem"><p role="">All OpenType fonts that are used for vertical
              writing must include a Vertical Header
              (<a role="" class="link" href="chapter.vhea.html" title="Chapter 37. vhea - Vertical Header Table">vhea</a>) table and a Vertical Metrics
              (<a role="" class="link" href="chapter.vmtx.html" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a>) table. CFF OpenType fonts that
              are used for vertical writing may also include,
              optionally, a Vertical Origin (<a role="" class="link" href="chapter.VORG.html" title="Chapter 39. VORG - Vertical Origin Table">VORG</a>)
              table for precise vertical origin information.</p></li><li role="" class="listitem"><p role="">If an OpenType font with CFF outlines is to be used
              for vertical writing, Adobe Type Manager/NT 4.1 and the
              Windows 2000 OTF driver require that a Vertical Rotation
              ('vrt2') feature be present in the Glyph Substitution
              (<a role="" class="link" href="chapter.GSUB.html" title="Chapter 25. GSUB - The Glyph Substitution Table">GSUB</a>) table. See the Feature Tags
              section of the OpenType Layout Tag Registry for a
              description of and further requirements for this
              feature.</p></li><li role="" class="listitem"><p role="">See the Feature Tags section of the OpenType Layout
              Tag Registry for descriptions of currently registered
              OpenType layout features, such as Alternate Half Widths
              ('halt') and Traditional Forms ('trad'), that can be
              specified in the font.</p></li></ul></div></div></div></div>