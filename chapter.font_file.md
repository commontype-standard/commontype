<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.font_file"></a>Chapter 3. The OpenType Font File</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630539648"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.1.1"></a>Specification</h3></div></div></div><p role="">An OpenType font file contains data, in table format,
          that comprises either a TrueType or a PostScript outline
          font. Rasterizers use combinations of data from the tables
          contained in the font to render the TrueType or PostScript
          glyph outlines. Some of this supporting data is used no
          matter which outline format is used; some of the supporting
          data is specific to either TrueType or PostScript.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630536608"></a>Filenames</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.2.1"></a>Specification</h3></div></div></div><p role="">OpenType fonts may have the extension .OTF or .TTF,
          depending on the kind of outlines in the font and the
          creator's desire for compatibility on systems without native
          OpenType support.</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">In all cases, fonts with only CFF data (no TrueType
              outlines) always have an .OTF extension.</p></li><li role="" class="listitem"><p role="">Fonts containing TrueType outlines may have either
              .OTF or .TTF, depending on the desire for backward
              compatibility on older systems or with previous versions
              of the font. TrueType Collection fonts should have a
              .TTC extension whether or not the fonts have OpenType
              layout tables present.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630531312"></a>Data Types</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.3.1"></a>Specification</h3></div></div></div><p role="">The following data types are used in the OpenType font
        file. All OpenType fonts use Motorola-style byte ordering (Big
        Endian):</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="8pc"/><col width="22pc"/></colgroup><thead><tr><th role="">Data Type</th><th role="">Description</th></tr></thead><tbody><tr><td role="">BYTE</td><td role="">8-bit unsigned integer.</td></tr><tr><td role="">CHAR</td><td role="">8-bit signed integer.</td></tr><tr><td role="">USHORT</td><td role="">16-bit unsigned integer.</td></tr><tr><td role="">SHORT</td><td role="">16-bit signed integer.</td></tr><tr><td role="">UINT24</td><td role="">24-bit signed integer.</td></tr><tr><td role="">ULONG</td><td role="">32-bit unsigned integer.</td></tr><tr><td role="">LONG</td><td role="">32-bit signed integer.</td></tr><tr><td role="">Fixed</td><td role="">32-bit signed fixed-point number (16.16)</td></tr><tr><td role="">FUNIT</td><td role="">Smallest measurable distance in the em space.</td></tr><tr><td role="">FWORD</td><td role="">16-bit signed integer (SHORT) that describes a
		  quantity in FUnits.</td></tr><tr><td role="">UFWORD</td><td role="">16-bit unsigned integer (USHORT) that describes
		  a quantity in FUnits.</td></tr><tr><td role="">F2DOT14</td><td role="">16-bit signed fixed number with the low 14 bits of
            fraction (2.14).</td></tr><tr><td role="">LONGDATETIME</td><td role="">Date represented in number of seconds since 12:00
            midnight, January 1, 1904. The value is represented as a
            signed 64-bit integer.</td></tr><tr><td role="">Tag</td><td role="">Array of four uint8s (length = 32 bits) used to
            identify a script, language system, feature, or
            baseline</td></tr><tr><td role="">GlyphID</td><td role="">Glyph index number, same as uint16 (length = 16
                bits)</td></tr><tr><td role="">Offset</td><td role=""> Offset to a table, same as uint16 (length = 16
            bits), NULL offset = 0x0000</td></tr></tbody></table></div><p role="">The F2DOT14 format consists of a signed, 2's
        complement mantissa and an unsigned fraction. To compute the
        actual value, take the mantissa and add the fraction. Examples
        of 2.14 values are:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="7.5pc"/><col width="7.5pc"/><col width="7.5pc"/><col width="7.5pc"/></colgroup><thead><tr><th role="">Decimal Value</th><th role="">Hex Value</th><th role="">Mantissa</th><th role="">Fraction</th></tr></thead><tbody><tr><td role="">1.999939</td><td role="">0x7fff</td><td role="">1</td><td role="">16383/16384</td></tr><tr><td role="">1.75</td><td role="">0x7000</td><td role="">1</td><td role="">12288/16384</td></tr><tr><td role="">0.000061</td><td role="">0x0001</td><td role="">0</td><td role="">1/16384</td></tr><tr><td role="">0.0</td><td role="">0x0000</td><td role="">0</td><td role="">0/16384</td></tr><tr><td role="">-0.000061</td><td role="">0xffff</td><td role="">-1</td><td role="">16383/16384</td></tr><tr><td role="">-2.0</td><td role="">0x8000</td><td role="">-2</td><td role="">0/16384</td></tr></tbody></table></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.3.2"></a>Annotation</h3></div></div></div><p role="">A number of synonyms are used for throughout the
          specification. They should be documented, and may be even
          replace the type above, as their names are more useful:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="15pc"/><col width="15pc"/></colgroup><tbody><tr><td role="">uint8</td><td role="">BYTE</td></tr><tr><td role="">int8</td><td role="">CHAR</td></tr><tr><td role="">uint16</td><td role="">USHORT</td></tr><tr><td role="">int16</td><td role="">SHORT</td></tr><tr><td role="">uint32</td><td role="">ULONG</td></tr><tr><td role="">int32</td><td role="">LONG</td></tr></tbody></table></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630476640"></a>Version Numbers</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.4.1"></a>Specification</h3></div></div></div><p role="">Most tables have version numbers, and the version number
	  for the entire font is contained in the Table
	  Directory. Note that there are two different table version
	  number types, each with its own numbering scheme. USHORT
	  version numbers always start at zero (0). Fixed version
	  numbers always start at one (1.0 or 0x00010000), except
	  where noted (<a role="" class="link" href="chapter.EBDT.md" title="Chapter 27. EBDT - Embedded Bitmap Data Table">EBDT</a>,
	  <a role="" class="link" href="chapter.EBLC.md" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a> and <a role="" class="link" href="chapter.EBSC.md" title="Chapter 29. EBSC - Embedded Bitmap Scaling Table">EBSC</a>
	  tables).</p><p role="">Implementations reading tables must include code to
        check version numbers so that if and when the format and
        therefore the version number changes, older implementations
        will reject newer versions gracefully, if the changes are
        incompatible.</p><p role="">When a Fixed number is used as a version, the upper 16
        bits comprise a major version number, and the lower 16 bits a
        minor. Tables with non-zero minor version numbers always
        specify the literal value of the version number since the
        normal representation of Fixed numbers is not necessarily
        followed. For example, the version number of
        <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a> table version 0.5 is 0x00005000, and
        that of <a role="" class="link" href="chapter.vhea.md" title="Chapter 37. vhea - Vertical Header Table">vhea</a> table version 1.1 is
        0x00011000. If an implementation understands a major version
        number, then it can safely proceed reading the table. The
        minor version number indicates extensions to the format that
        are undetectable by implementations that do not support
        them.</p><p role="">The only exception to this is the Offset Table's sfnt
        version. This serves solely to identify whether the OpenType
        font contains TrueType outlines (a value of 1.0) or CFF data
        (the tag 'OTTO'), as described in the section below,
        <a role="" class="link" href="chapter.font_file.md#organization" title="Organization of an OpenType Font">Organization of an OpenType
        font</a>.</p><p role="">When a USHORT number is used to indicate version, it
        should be treated as though it were a minor version number;
        i.e., all format changes are compatible extensions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="organization"></a>Organization of an OpenType Font</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.5.1"></a>Specification</h3></div></div></div><p role="">A key characteristic of the OpenType format is the
        TrueType sfnt "wrapper", which provides organization for a
        collection of tables in a general and extensible
        manner.</p><p role="">The OpenType font file begins with the Offset Table. If
	  the font file contains only one font, the Offset Table will
	  begin at byte 0 of the file. If the font file is a TrueType
	  collection, the beginning point of the Offset Table for each
	  font is indicated in the TTCHeader.</p><div class="table"><a name="idm114630463600"></a><p class="title"><strong>Table 3.1. Offset Table</strong></p><div class="table-contents"><table role="" class="table" summary="Offset Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">sfnt version</td><td role="">0x00010000 for version 1.0.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numTables</td><td role="">Number of tables.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">searchRange</td><td role="">(Maximum power of 2 &lt;= numTables) x
              16.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">entrySelector</td><td role="">Log2(maximum power of 2 &lt;=
              numTables).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">rangeShift</td><td role="">NumTables x 16-searchRange.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">OpenType fonts that contain TrueType outlines should use
          the value of 1.0 for the sfnt version. OpenType fonts
          containing CFF data should use the tag 'OTTO' as the sfnt
          version number.</p><p role="">Note: The Apple specification for TrueType fonts allows
	  for 'true' and 'typ1' for sfnt version. These version tags
	  should not be used for fonts which contain OpenType
	  tables.</p><p role="">The Offset Table is followed immediately by the Table
          Directory entries. Entries in the Table Directory must be
          sorted in ascending order by tag. Offset values in the Table
          Directory are measured from the start of the font
          file.</p><div class="table"><a name="idm114630452160"></a><p class="title"><strong>Table 3.2. Table Directory</strong></p><div class="table-contents"><table role="" class="table" summary="Table Directory" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">tag</td><td role="">4 -byte identifier.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">checkSum</td><td role="">CheckSum for this table.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">offset</td><td role="">Offset from beginning of TrueType font
              file.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">length</td><td role="">Length of this table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The Table Directory makes it possible for a given font
        to contain only those tables it actually needs. As a result
        there is no standard value for numTables.</p><p role="">Tags are the names given to tables in the OpenType font
        file. All tag names consist of four characters. Names with
        less than four letters are allowed if followed by the
        necessary trailing spaces. All tag names defined within a font
        (e.g., table names, feature tags, language tags) must be built
        from printing characters represented by ASCII values
        32-126</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.5.2"></a>Annotation</h3></div></div></div><p role="">For clarity, is may be worth to add "or 'OTTO'" to the
          description of the field snft version in the first
          table. I realize that the paragraph following the table
          makes that clear, but users of the specification familiar
          with it are likely to look at the tables only.</p><p role="">The type of the tag field in the second table should
          probably be 'Tag'.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630439952"></a>Calculating Checksums</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.6.1"></a>Specification</h3></div></div></div><p role="">Table checksums are the unsigned sum of the longs of a
        given table. In C, the following function can be used to
        determine a checksum:</p><div role="" class="literallayout"><p><br/>
ULONG<br/>
CalcTableChecksum(ULONG *Table, ULONG Length)<br/>
{<br/>
ULONG Sum = 0L;<br/>
ULONG *Endptr = Table+((Length+3) &amp; ~3) / sizeof(ULONG);<br/>
<br/>
while (Table &lt; EndPtr)<br/>
        Sum += *Table++;<br/>
return Sum;<br/>
}<br/>
</p></div><div role="" class="blockquote"><blockquote role="" class="blockquote"><p role="">Note: This function implies that the length of a table
          must be a multiple of four bytes. In fact, a font is not
          considered structurally proper without the correct padding.
          All tables must begin on four byte boundries, and any
          remaining space between tables is padded with zeros. The
          length of all tables should be recorded in the table
          directory with their actual length (not their padded
          length).</p></blockquote></div><p role="">To calculate the checkSum for the <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a>
          table which itself includes the checkSumAdjustment entry for
          the entire font, do the following:</p><div role="" class="orderedlist"><ol class="orderedlist" type="1"><li role="" class="listitem"><p role="">Set the checkSumAdjustment to 0.</p></li><li role="" class="listitem"><p role="">Calculate the checksum for all the tables including
              the <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a> table and enter that value
              into the table directory.</p></li><li role="" class="listitem"><p role="">Calculate the checksum for the entire font.</p></li><li role="" class="listitem"><p role="">Subtract that value from the hex value B1B0AFBA.</p></li><li role="" class="listitem"><p role="">Store the result in checkSumAdjustment.</p></li></ol></div><p role="">The checkSum for the head table which includes the
          checkSumAdjustment entry for the entire font is now
          incorrect. That is not a problem. Do not change it. An
          application attempting to verify that the <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a> table has
          not changed should calculate the checkSum for that table by
          not including the checkSumAdjustment value, and compare the
          result with the entry in the table directory.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630427456"></a>TrueType Collections</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.7.1"></a>Specification</h3></div></div></div><p role="">A TrueType Collection (TTC) is a means of delivering
        multiple OpenType fonts in a single file structure. TrueType
        Collections are most useful when the fonts to be delivered
        together share many glyphs in common. By allowing multiple
        fonts to share glyph sets, TTCs can result in a significant
        saving of file space.</p><p role="">For example, a group of Japanese fonts may each have
        their own designs for the kana glyphs, but share identical
        designs for the kanji. With ordinary OpenType font files, the
        only way to include the common kanji glyphs is to copy their
        glyph data into each font. Since the kanji represent much more
        data than the kana, this results in a great deal of wasteful
        duplication of glyph data. TTCs were defined to solve this
        problem.</p><p role="">The CFF rasterizer does not currently support TTC
        files.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630423072"></a>The TTC File Structure</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.8.1"></a>Specification</h3></div></div></div><p role="">A TrueType Collection file consists of a single TTC
	  Header table, one or more Offset Tables with Table
	  Directories, and a number of OpenType tables. The TTC Header
	  must be located at the beginning of the TTC file.</p><p role="">Each OpenType table in a TTC file is referenced through
	  the Offset Table and Table Directories of each font which
	  uses that table. Some of the OpenType tables must appear multiple
	  times, once for each font included in the TTC; while other
	  tables should be shared by multiple fonts in the TTC.</p><p role="">As an example, consider a TTC file which combines two
          Japanese fonts (Font1 and Font2). The fonts have different
          kana designs (Kana1 and Kana2) but use the same design for
          kanji. The TTC file contains a single
          <a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a> table which includes both designs of
          kana together with the kanji; both fonts' Table Directories
          point to this <a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a> table. But each font's
          Table Directory points to a different
          <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table, which identifies the glyph
          set to use. Font1's <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table points to
          the Kana1 region of the <a role="" class="link" href="chapter.loca.md" title="Chapter 17. loca - Index to Location">loca</a> and
          <a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a> tables for kana glyphs, and to the
          kanji region for the kanji. Font2's <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          table points to the Kana2 region of the
          <a role="" class="link" href="chapter.loca.md" title="Chapter 17. loca - Index to Location">loca</a> and <a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a> tables
          for kana glyphs, and to the same kanji region for the
          kanji.</p><p role="">The tables that should have a unique copy per font are
          those that are used by the system in identifying the font
          and its character mapping, including
          <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>, <a role="" class="link" href="chapter.name.md" title="Chapter 10. name - Naming Table">name</a>, and
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a>. The tables that should be shared by
          fonts in the TTC are those that define glyph and instruction
          data or use glyph indices to access data:
          <a role="" class="link" href="chapter.glyf.md" title="Chapter 16. glyf - Glyf Data">glyf</a>, <a role="" class="link" href="chapter.loca.md" title="Chapter 17. loca - Index to Location">loca</a>,
          <a role="" class="link" href="chapter.hmtx.md" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a>, <a role="" class="link" href="chapter.hdmx.md" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a>,
          <a role="" class="link" href="chapter.LTSH.md" title="Chapter 34. LTSH - Linear Threshold">LTSH</a>, <a role="" class="link" href="">cvt </a>,
          <a role="" class="link" href="chapter.fpgm.md" title="Chapter 15. fpgm - Font Program">fpgm</a>, <a role="" class="link" href="chapter.prep.md" title="Chapter 18. prep - Control Value Program">prep</a>,
          <a role="" class="link" href="chapter.EBLC.md" title="Chapter 28. EBLC - Embedded Bitmap Location Table">EBLC</a>, <a role="" class="link" href="chapter.EBDT.md" title="Chapter 27. EBDT - Embedded Bitmap Data Table">EBDT</a>,
          <a role="" class="link" href="chapter.EBSC.md" title="Chapter 29. EBSC - Embedded Bitmap Scaling Table">EBSC</a>, <a role="" class="link" href="chapter.maxp.md" title="Chapter 9. maxp - Maximum Profile">maxp</a>, and so
          on. In practice, any tables which have identical data for
          two or more fonts may be shared.</p><p role="">A tool is available from Microsoft to help build .TTC
          files. The process involves paying close attention the issue
          of glyph renumbering in a font and the side effects that can
          result, in the <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table and elsewhere.
          The fonts to be merged must also have compatible TrueType
          instructions-that is, their preprograms, function
          definitions, and control values must not conflict.</p><p role="">TrueType Collection files use the filename suffix
        .TTC.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630400832"></a>TTC Header</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.9.1"></a>Specification</h3></div></div></div><p role="">There are two versions of the TTC Header: Version 1.0
        has been used for TTC files without digital
        signatures. Version 2.0 can be used for TTC files with or
        without digital signatures ’ if there's no signature, then
        the last three fields of the version 2.0 header are left
        null</p><p role="">If a digital signature is used, the DSIG table for the
        file must be the last table in the TTC file. Signatures in a
        TTC file are expected to be Format 1 signatures</p><p role="">The purpose of the TTC Header table is to locate the
        different Offset Tables within a TTC file. The TTC Header
        is located at the beginning of the TTC file (offset = 0). It
        consists of an identification tag, a version number, a count
        of the number of OpenType fonts (Table Directories) in the
        file, and an array of offsets to each Offset Table.</p><div class="table"><a name="idm114630396720"></a><p class="title"><strong>Table 3.3. TTC Header Version 1.0</strong></p><div class="table-contents"><table role="" class="table" summary="TTC Header Version 1.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">TAG</td><td role="">TTCTag</td><td role="">TrueType Collection ID string:
              'ttcf'</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">Version</td><td role="">Version of the TTC Header (1.0),
              0x00010000</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numFonts</td><td role="">Number of fonts in the TTC</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">OffsetTable [numFonts]</td><td role="">Array of offsets to Offset Table for each
	      font from the beginning of the file</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigTag</td><td role="">Tag indicating that a DSIG table exists. This
              tag should equal 0x44534947 (<a role="" class="link" href="chapter.DSIG.md" title="Chapter 30. DSIG - Digital Signature Table">DSIG</a>)</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigLength</td><td role="">The length (in bytes) of the DSIG
              table</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigOffset</td><td role="">The offset (in bytes) of the DSIG table from
              the beginning of the TTC file</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm114630383456"></a><p class="title"><strong>Table 3.4. TTC Header Version 2.0</strong></p><div class="table-contents"><table role="" class="table" summary="TTC Header Version 2.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">TAG</td><td role="">TTCTag</td><td role="">TrueType Collection ID string:
              'ttcf'</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">Version</td><td role="">Version of the TTC Header (2.0),
              0x00020000</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numFonts</td><td role="">Number of fonts in TTC</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">OffsetTable [numFonts]</td><td role="">Array of offsets to Offset Table for each
	      font from the beginning of the file</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigTag</td><td role="">Tag
            indicating that a DSIG table exists, 0x44534947
            (<a role="" class="link" href="chapter.DSIG.md" title="Chapter 30. DSIG - Digital Signature Table">DSIG</a>) (null if no
            signature)</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigLength</td><td role="">The length (in bytes) of the DSIG table (null
              if no signature)</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulDsigOffset</td><td role="">The offset (in bytes) of the DSIG table from
              the beginning of the TTC file (null if no
              signature)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.9.2"></a>Annotation</h3></div></div></div><p role="">The type of the TTCTag field in both format should
          probably be 'Tag' instead of 'TAG'.</p><p role="">The value of the Version field in both tables seems to
          be wrong; it's missing a 0 at the end.</p><p role="">The description of the difference between version 1.0
          and version 2.0 seems to contradict the content of the
          version 1.0 table. If a version 1.0 table is for files
          without a digital signature, what is the meaning of the
          fields ulDsigTag, ulDsigLength and ulDsigOffset?</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm114630366816"></a>Font Tables</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.3.10.1"></a>Specification</h3></div></div></div><p role="">  The rasterizer has a much easier time traversing
        tables if they are padded so that each table begins on a
        4-byte boundary. It is highly recommended that all tables be
        long-aligned and padded with zeroes.</p></div></div></div>