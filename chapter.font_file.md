<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.font_file"></a>Chapter 2. The CommonType Font File</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715619984"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.1.1"></a>Specification</h4></div></div></div><p>An CommonType font file contains data, in table format,
          that comprises either a TrueType or a PostScript outline
          font. Rasterizers use combinations of data from the tables
          contained in the font to render the TrueType or PostScript
          glyph outlines. Some of this supporting data is used no
          matter which outline format is used; some of the supporting
          data is specific to either TrueType or PostScript.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715616944"></a>Filenames</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.2.1"></a>Specification</h4></div></div></div><p>CommonType fonts may have the extension .OTF or .TTF,
          depending on the kind of outlines in the font and the
          creator's desire for compatibility on systems without native
          CommonType support.</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>In all cases, fonts with only CFF data (no TrueType
              outlines) always have an .OTF extension.</p></li><li class="listitem"><p>Fonts containing TrueType outlines may have either
              .OTF or .TTF, depending on the desire for backward
              compatibility on older systems or with previous versions
              of the font. TrueType Collection fonts should have a
              .TTC extension whether or not the fonts have CommonType
              layout tables present.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715611648"></a>Data Types</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.3.1"></a>Specification</h4></div></div></div><p>The following data types are used in the CommonType font
        file. All CommonType fonts use Motorola-style byte ordering (Big
        Endian):</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Data Type</th><th>Description</th></tr></thead><tbody><tr><td>BYTE</td><td>8-bit unsigned integer.</td></tr><tr><td>CHAR</td><td>8-bit signed integer.</td></tr><tr><td>USHORT</td><td>16-bit unsigned integer.</td></tr><tr><td>SHORT</td><td>16-bit signed integer.</td></tr><tr><td>UINT24</td><td>24-bit signed integer.</td></tr><tr><td>ULONG</td><td>32-bit unsigned integer.</td></tr><tr><td>LONG</td><td>32-bit signed integer.</td></tr><tr><td>Fixed</td><td>32-bit signed fixed-point number (16.16)</td></tr><tr><td>FUNIT</td><td>Smallest measurable distance in the em space.</td></tr><tr><td>FWORD</td><td>16-bit signed integer (SHORT) that describes a
		  quantity in FUnits.</td></tr><tr><td>UFWORD</td><td>16-bit unsigned integer (USHORT) that describes
		  a quantity in FUnits.</td></tr><tr><td>F2DOT14</td><td>16-bit signed fixed number with the low 14 bits of
            fraction (2.14).</td></tr><tr><td>LONGDATETIME</td><td>Date represented in number of seconds since 12:00
            midnight, January 1, 1904. The value is represented as a
            signed 64-bit integer.</td></tr><tr><td>Tag</td><td>Array of four uint8s (length = 32 bits) used to
            identify a script, language system, feature, or
            baseline</td></tr><tr><td>GlyphID</td><td>Glyph index number, same as uint16 (length = 16
                bits)</td></tr><tr><td>Offset</td><td> Offset to a table, same as uint16 (length = 16
            bits), NULL offset = 0x0000</td></tr></tbody></table></div><p>The F2DOT14 format consists of a signed, 2's
        complement mantissa and an unsigned fraction. To compute the
        actual value, take the mantissa and add the fraction. Examples
        of 2.14 values are:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Decimal Value</th><th>Hex Value</th><th>Mantissa</th><th>Fraction</th></tr></thead><tbody><tr><td>1.999939</td><td>0x7fff</td><td>1</td><td>16383/16384</td></tr><tr><td>1.75</td><td>0x7000</td><td>1</td><td>12288/16384</td></tr><tr><td>0.000061</td><td>0x0001</td><td>0</td><td>1/16384</td></tr><tr><td>0.0</td><td>0x0000</td><td>0</td><td>0/16384</td></tr><tr><td>-0.000061</td><td>0xffff</td><td>-1</td><td>16383/16384</td></tr><tr><td>-2.0</td><td>0x8000</td><td>-2</td><td>0/16384</td></tr></tbody></table></div></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.3.2"></a>Annotation</h4></div></div></div><p>A number of synonyms are used for throughout the
          specification. They should be documented, and may be even
          replace the type above, as their names are more useful:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><tbody><tr><td>uint8</td><td>BYTE</td></tr><tr><td>int8</td><td>CHAR</td></tr><tr><td>uint16</td><td>USHORT</td></tr><tr><td>int16</td><td>SHORT</td></tr><tr><td>uint32</td><td>ULONG</td></tr><tr><td>int32</td><td>LONG</td></tr></tbody></table></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715560800"></a>Version Numbers</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.4.1"></a>Specification</h4></div></div></div><p>Most tables have version numbers, and the version number
	  for the entire font is contained in the Table
	  Directory. Note that there are two different table version
	  number types, each with its own numbering scheme. USHORT
	  version numbers always start at zero (0). Fixed version
	  numbers always start at one (1.0 or 0x00010000), except
	  where noted (<a class="link" href="chapter.EBDT.html" title="Chapter 26. EBDT - Embedded Bitmap Data Table">EBDT</a>,
	  <a class="link" href="chapter.EBLC.html" title="Chapter 27. EBLC - Embedded Bitmap Location Table">EBLC</a> and <a class="link" href="chapter.EBSC.html" title="Chapter 28. EBSC - Embedded Bitmap Scaling Table">EBSC</a>
	  tables).</p><p>Implementations reading tables must include code to
        check version numbers so that if and when the format and
        therefore the version number changes, older implementations
        will reject newer versions gracefully, if the changes are
        incompatible.</p><p>When a Fixed number is used as a version, the upper 16
        bits comprise a major version number, and the lower 16 bits a
        minor. Tables with non-zero minor version numbers always
        specify the literal value of the version number since the
        normal representation of Fixed numbers is not necessarily
        followed. For example, the version number of
        <a class="link" href="chapter.maxp.html" title="Chapter 8. maxp - Maximum Profile">maxp</a> table version 0.5 is 0x00005000, and
        that of <a class="link" href="chapter.vhea.html" title="Chapter 36. vhea - Vertical Header Table">vhea</a> table version 1.1 is
        0x00011000. If an implementation understands a major version
        number, then it can safely proceed reading the table. The
        minor version number indicates extensions to the format that
        are undetectable by implementations that do not support
        them.</p><p>The only exception to this is the Offset Table's sfnt
        version. This serves solely to identify whether the CommonType
        font contains TrueType outlines (a value of 1.0) or CFF data
        (the tag 'OTTO'), as described in the section below,
        <a class="link" href="chapter.font_file.html#organization" title="Organization of an CommonType Font">Organization of an CommonType
        font</a>.</p><p>When a USHORT number is used to indicate version, it
        should be treated as though it were a minor version number;
        i.e., all format changes are compatible extensions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="organization"></a>Organization of an CommonType Font</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.5.1"></a>Specification</h4></div></div></div><p>A key characteristic of the CommonType format is the
        TrueType sfnt "wrapper", which provides organization for a
        collection of tables in a general and extensible
        manner.</p><p>The CommonType font file begins with the Offset Table. If
	  the font file contains only one font, the Offset Table will
	  begin at byte 0 of the file. If the font file is a TrueType
	  collection, the beginning point of the Offset Table for each
	  font is indicated in the TTCHeader.</p><div class="table"><a name="idm300715547744"></a><p class="title"><strong>Table 2.1. Offset Table</strong></p><div class="table-contents"><table class="table" summary="Offset Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Fixed</td><td>sfnt version</td><td>0x00010000 for version 1.0.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numTables</td><td>Number of tables.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>searchRange</td><td>(Maximum power of 2 &lt;= numTables) x
              16.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entrySelector</td><td>Log2(maximum power of 2 &lt;=
              numTables).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>rangeShift</td><td>NumTables x 16-searchRange.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>CommonType fonts that contain TrueType outlines should use
          the value of 1.0 for the sfnt version. CommonType fonts
          containing CFF data should use the tag 'OTTO' as the sfnt
          version number.</p><p>Note: The Apple specification for TrueType fonts allows
	  for 'true' and 'typ1' for sfnt version. These version tags
	  should not be used for fonts which contain CommonType
	  tables.</p><p>The Offset Table is followed immediately by the Table
          Directory entries. Entries in the Table Directory must be
          sorted in ascending order by tag. Offset values in the Table
          Directory are measured from the start of the font
          file.</p><div class="table"><a name="idm300715536304"></a><p class="title"><strong>Table 2.2. Table Directory</strong></p><div class="table-contents"><table class="table" summary="Table Directory" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>tag</td><td>4 -byte identifier.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>checkSum</td><td>CheckSum for this table.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>offset</td><td>Offset from beginning of TrueType font
              file.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Length of this table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The Table Directory makes it possible for a given font
        to contain only those tables it actually needs. As a result
        there is no standard value for numTables.</p><p>Tags are the names given to tables in the CommonType font
        file. All tag names consist of four characters. Names with
        less than four letters are allowed if followed by the
        necessary trailing spaces. All tag names defined within a font
        (e.g., table names, feature tags, language tags) must be built
        from printing characters represented by ASCII values
        32-126</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.5.2"></a>Annotation</h4></div></div></div><p>For clarity, is may be worth to add "or 'OTTO'" to the
          description of the field snft version in the first
          table. I realize that the paragraph following the table
          makes that clear, but users of the specification familiar
          with it are likely to look at the tables only.</p><p>The type of the tag field in the second table should
          probably be 'Tag'.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715524096"></a>Calculating Checksums</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.6.1"></a>Specification</h4></div></div></div><p>Table checksums are the unsigned sum of the longs of a
        given table. In C, the following function can be used to
        determine a checksum:</p><div class="literallayout"><p><br/>
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
</p></div><div class="blockquote"><blockquote class="blockquote"><p>Note: This function implies that the length of a table
          must be a multiple of four bytes. In fact, a font is not
          considered structurally proper without the correct padding.
          All tables must begin on four byte boundries, and any
          remaining space between tables is padded with zeros. The
          length of all tables should be recorded in the table
          directory with their actual length (not their padded
          length).</p></blockquote></div><p>To calculate the checkSum for the <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a>
          table which itself includes the checkSumAdjustment entry for
          the entire font, do the following:</p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>Set the checkSumAdjustment to 0.</p></li><li class="listitem"><p>Calculate the checksum for all the tables including
              the <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a> table and enter that value
              into the table directory.</p></li><li class="listitem"><p>Calculate the checksum for the entire font.</p></li><li class="listitem"><p>Subtract that value from the hex value B1B0AFBA.</p></li><li class="listitem"><p>Store the result in checkSumAdjustment.</p></li></ol></div><p>The checkSum for the head table which includes the
          checkSumAdjustment entry for the entire font is now
          incorrect. That is not a problem. Do not change it. An
          application attempting to verify that the <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a> table has
          not changed should calculate the checkSum for that table by
          not including the checkSumAdjustment value, and compare the
          result with the entry in the table directory.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715511136"></a>TrueType Collections</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.7.1"></a>Specification</h4></div></div></div><p>A TrueType Collection (TTC) is a means of delivering
        multiple CommonType fonts in a single file structure. TrueType
        Collections are most useful when the fonts to be delivered
        together share many glyphs in common. By allowing multiple
        fonts to share glyph sets, TTCs can result in a significant
        saving of file space.</p><p>For example, a group of Japanese fonts may each have
        their own designs for the kana glyphs, but share identical
        designs for the kanji. With ordinary CommonType font files, the
        only way to include the common kanji glyphs is to copy their
        glyph data into each font. Since the kanji represent much more
        data than the kana, this results in a great deal of wasteful
        duplication of glyph data. TTCs were defined to solve this
        problem.</p><p>The CFF rasterizer does not currently support TTC
        files.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715506752"></a>The TTC File Structure</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.8.1"></a>Specification</h4></div></div></div><p>A TrueType Collection file consists of a single TTC
	  Header table, one or more Offset Tables with Table
	  Directories, and a number of CommonType tables. The TTC Header
	  must be located at the beginning of the TTC file.</p><p>Each CommonType table in a TTC file is referenced through
	  the Offset Table and Table Directories of each font which
	  uses that table. Some of the CommonType tables must appear multiple
	  times, once for each font included in the TTC; while other
	  tables should be shared by multiple fonts in the TTC.</p><p>As an example, consider a TTC file which combines two
          Japanese fonts (Font1 and Font2). The fonts have different
          kana designs (Kana1 and Kana2) but use the same design for
          kanji. The TTC file contains a single
          <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a> table which includes both designs of
          kana together with the kanji; both fonts' Table Directories
          point to this <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a> table. But each font's
          Table Directory points to a different
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table, which identifies the glyph
          set to use. Font1's <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table points to
          the Kana1 region of the <a class="link" href="chapter.loca.html" title="Chapter 16. loca - Index to Location">loca</a> and
          <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a> tables for kana glyphs, and to the
          kanji region for the kanji. Font2's <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          table points to the Kana2 region of the
          <a class="link" href="chapter.loca.html" title="Chapter 16. loca - Index to Location">loca</a> and <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a> tables
          for kana glyphs, and to the same kanji region for the
          kanji.</p><p>The tables that should have a unique copy per font are
          those that are used by the system in identifying the font
          and its character mapping, including
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>, <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a>, and
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a>. The tables that should be shared by
          fonts in the TTC are those that define glyph and instruction
          data or use glyph indices to access data:
          <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a>, <a class="link" href="chapter.loca.html" title="Chapter 16. loca - Index to Location">loca</a>,
          <a class="link" href="chapter.hmtx.html" title="Chapter 7. hmtx - Horizontal Metrics">hmtx</a>, <a class="link" href="chapter.hdmx.html" title="Chapter 31. hdmx - Horizontal Device Metrics">hdmx</a>,
          <a class="link" href="chapter.LTSH.html" title="Chapter 33. LTSH - Linear Threshold">LTSH</a>, <a class="link" href="">cvt </a>,
          <a class="link" href="chapter.fpgm.html" title="Chapter 14. fpgm - Font Program">fpgm</a>, <a class="link" href="chapter.prep.html" title="Chapter 17. prep - Control Value Program">prep</a>,
          <a class="link" href="chapter.EBLC.html" title="Chapter 27. EBLC - Embedded Bitmap Location Table">EBLC</a>, <a class="link" href="chapter.EBDT.html" title="Chapter 26. EBDT - Embedded Bitmap Data Table">EBDT</a>,
          <a class="link" href="chapter.EBSC.html" title="Chapter 28. EBSC - Embedded Bitmap Scaling Table">EBSC</a>, <a class="link" href="chapter.maxp.html" title="Chapter 8. maxp - Maximum Profile">maxp</a>, and so
          on. In practice, any tables which have identical data for
          two or more fonts may be shared.</p><p>A tool is available from Microsoft to help build .TTC
          files. The process involves paying close attention the issue
          of glyph renumbering in a font and the side effects that can
          result, in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table and elsewhere.
          The fonts to be merged must also have compatible TrueType
          instructions-that is, their preprograms, function
          definitions, and control values must not conflict.</p><p>TrueType Collection files use the filename suffix
        .TTC.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715484496"></a>TTC Header</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.9.1"></a>Specification</h4></div></div></div><p>There are two versions of the TTC Header: Version 1.0
        has been used for TTC files without digital
        signatures. Version 2.0 can be used for TTC files with or
        without digital signatures ’ if there's no signature, then
        the last three fields of the version 2.0 header are left
        null</p><p>If a digital signature is used, the DSIG table for the
        file must be the last table in the TTC file. Signatures in a
        TTC file are expected to be Format 1 signatures</p><p>The purpose of the TTC Header table is to locate the
        different Offset Tables within a TTC file. The TTC Header
        is located at the beginning of the TTC file (offset = 0). It
        consists of an identification tag, a version number, a count
        of the number of CommonType fonts (Table Directories) in the
        file, and an array of offsets to each Offset Table.</p><div class="table"><a name="idm300715480368"></a><p class="title"><strong>Table 2.3. TTC Header Version 1.0</strong></p><div class="table-contents"><table class="table" summary="TTC Header Version 1.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>TAG</td><td>TTCTag</td><td>TrueType Collection ID string:
              'ttcf'</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>Version</td><td>Version of the TTC Header (1.0),
              0x00010000</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numFonts</td><td>Number of fonts in the TTC</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>OffsetTable [numFonts]</td><td>Array of offsets to Offset Table for each
	      font from the beginning of the file</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigTag</td><td>Tag indicating that a DSIG table exists. This
              tag should equal 0x44534947 (<a class="link" href="chapter.DSIG.html" title="Chapter 29. DSIG - Digital Signature Table">DSIG</a>)</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigLength</td><td>The length (in bytes) of the DSIG
              table</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigOffset</td><td>The offset (in bytes) of the DSIG table from
              the beginning of the TTC file</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm300715467104"></a><p class="title"><strong>Table 2.4. TTC Header Version 2.0</strong></p><div class="table-contents"><table class="table" summary="TTC Header Version 2.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>TAG</td><td>TTCTag</td><td>TrueType Collection ID string:
              'ttcf'</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>Version</td><td>Version of the TTC Header (2.0),
              0x00020000</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numFonts</td><td>Number of fonts in TTC</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>OffsetTable [numFonts]</td><td>Array of offsets to Offset Table for each
	      font from the beginning of the file</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigTag</td><td>Tag
            indicating that a DSIG table exists, 0x44534947
            (<a class="link" href="chapter.DSIG.html" title="Chapter 29. DSIG - Digital Signature Table">DSIG</a>) (null if no
            signature)</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigLength</td><td>The length (in bytes) of the DSIG table (null
              if no signature)</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigOffset</td><td>The offset (in bytes) of the DSIG table from
              the beginning of the TTC file (null if no
              signature)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.9.2"></a>Annotation</h4></div></div></div><p>The type of the TTCTag field in both format should
          probably be 'Tag' instead of 'TAG'.</p><p>The value of the Version field in both tables seems to
          be wrong; it's missing a 0 at the end.</p><p>The description of the difference between version 1.0
          and version 2.0 seems to contradict the content of the
          version 1.0 table. If a version 1.0 table is for files
          without a digital signature, what is the meaning of the
          fields ulDsigTag, ulDsigLength and ulDsigOffset?</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm300715450464"></a>Font Tables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.10.1"></a>Specification</h4></div></div></div><p>  The rasterizer has a much easier time traversing
        tables if they are padded so that each table begins on a
        4-byte boundary. It is highly recommended that all tables be
        long-aligned and padded with zeroes.</p></div></div></div>