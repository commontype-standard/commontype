<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.font_file"></a>Chapter 2. The CommonType Font File</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465839637536"></a></h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>A CommonType font file contains data, structured as a
          series of <em class="glossterm">tables</em>. <em class="glossterm">Font
          consumers</em> use combinations of data from the tables
          contained in the font to process and render glyph sequences.
      </p><p>
          The glyphs in a font may be represented in a number of
          <em class="glossterm">glyph representation format</em>s.
          CommonType supports three <em class="glossterm">outline formats</em>
          (TrueType outlines, PostScript outlines and SVG outlines), as
          well as a variety of <em class="glossterm">bitmap formats</em>.
          Some of the supporting data is used no matter which glyph
          representation format is used; some of the supporting
          data is specific to the glyph representation format.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465839633152"></a>Filenames</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>CommonType font files must have either the extension
          <code class="filename">.otf</code> or the extension
          <code class="filename">.ttf</code>,
          depending on the representation format used.</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Font files where the only
            <em class="glossterm">glyph representation format</em> in use
            is TrueType outlines <em class="glossterm">may</em> have the
            extension <code class="filename">.ttf</code>.
          </p></li><li class="listitem"><p>
              <a class="link" href="chapter.font_file.html#font_file.ttc" title="TrueType Collections">TrueType Collection</a>
              fonts <em class="glossterm">must</em> have a
              <code class="filename">.ttc</code> extension.
            </p></li><li class="listitem"><p>Font files containing any other representations
            <em class="glossterm">must</em> have the extension
            <code class="filename">.otf</code>.
          </p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465839622608"></a>Data Types</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>The following data types are used in the CommonType font
        file. All CommonType fonts use Motorola-style byte ordering (Big
        Endian).</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Data Type</th><th>Description</th></tr></thead><tbody><tr><td><span class="type">BYTE</span>, <span class="type">uint8</span></td><td>8-bit unsigned integer.</td></tr><tr><td><span class="type">CHAR</span>, <span class="type">int8</span></td><td>8-bit signed integer.</td></tr><tr><td><span class="type">USHORT</span>, <span class="type">uint16</span></td><td>16-bit unsigned integer.</td></tr><tr><td><span class="type">SHORT</span>, int16</td><td>16-bit signed integer.</td></tr><tr><td><span class="type">UINT24</span></td><td>24-bit signed integer.</td></tr><tr><td><span class="type">ULONG</span>, <span class="type">uint32</span></td><td>32-bit unsigned integer.</td></tr><tr><td><span class="type">LONG</span>, <span class="type">int32</span></td><td>32-bit signed integer.</td></tr><tr><td><span class="type">Fixed</span></td><td>32-bit signed fixed-point number (16.16)</td></tr><tr><td><span class="type">FWORD</span></td><td>16-bit signed integer (<span class="type">SHORT</span>) that describes a quantity in <em class="glossterm">font unit</em>s.</td></tr><tr><td><span class="type">UFWORD</span></td><td>16-bit unsigned integer (<span class="type">USHORT</span>) that describes
      a quantity in <em class="glossterm">font unit</em>s.</td></tr><tr><td><span class="type">F2DOT14</span></td><td>16-bit signed fixed number with the low 14 bits of
            fraction (2.14).</td></tr><tr><td><span class="type">LONGDATETIME</span></td><td>Date represented in number of seconds since 12:00
            midnight, January 1, 1904. The value is represented as a
            signed 64-bit integer.</td></tr><tr><td><span class="type">Tag</span></td><td>Array of four <span class="type">BYTE</span>s
                (hence with a total length of 32 bits) used to
                identify a script, language system, feature, or
                baseline.
              </td></tr><tr><td><span class="type">GlyphID</span></td><td>A <span class="type">USHORT</span> representing a
                <em class="glossterm">glyph index number</em>.
              </td></tr><tr><td><span class="type">Offset</span></td><td>A <span class="type">USHORT</span> representing an offset to a table.
                The NULL offset is represented as <code class="literal">0x0000</code>.
              </td></tr><tr><td><span class="type">Version</span></td><td>A 32-bit unsigned table version number.
                (See <a class="link" href="chapter.font_file.html#font_file.versions" title="Version Numbers">Version Numbers</a>
                below.) The upper 16 bits represent the major version
                number, and the lower 16 bits represent the minor
                version number.
              </td></tr></tbody></table></div><div class="section"><div class="titlepage"><div><div><h5 class="title"><a name="section.3.3.1.1"></a>Signed Fixed-Point Numbers</h5></div></div></div><p>
          As mentioned above, the <span class="type">F2DOT14</span> type is a fixed-point
          value consisting of a two bit, signed, 2's complement mantissa,
          and a 14-bit unsigned fraction. To compute the actual value,
          take the mantissa and add the fraction.
        </p><p>
          When converting floating-point numbers to <span class="type">F2DOT14</span>,
          multiply the floating point number by 2<sup>14</sup>,
          and then round to an integer format. When rounding, font producers
          <em class="glossterm">must</em> apply the following rounding strategy:
        </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>When the fractional part is 0.5 or higher, round to the
            <span class="emphasis"><em>next higher integer</em></span>.</p></li><li class="listitem"><p>When the fractional part is less than 0.5 or higher,
              truncate the fractional part.</p></li></ul></div><div role="discussion" class="section"><div class="titlepage"><div><div><h6 class="title"><a name="section.3.3.1.1.1"></a>Discussion</h6></div></div></div><p> Examples of <span class="type">F2DOT14</span> values are: </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Decimal Value</th><th>Hex Value</th><th>Mantissa</th><th>Fraction</th></tr></thead><tbody><tr><td>1.999939</td><td>0x7fff</td><td>1</td><td>16383/16384</td></tr><tr><td>1.75</td><td>0x7000</td><td>1</td><td>12288/16384</td></tr><tr><td>0.000061</td><td>0x0001</td><td>0</td><td>1/16384</td></tr><tr><td>0.0</td><td>0x0000</td><td>0</td><td>0/16384</td></tr><tr><td>-0.000061</td><td>0xffff</td><td>-1</td><td>16383/16384</td></tr><tr><td>-2.0</td><td>0x8000</td><td>-2</td><td>0/16384</td></tr></tbody></table></div><p>
    The following Python code will convert a floating point number to a
    <span class="type">F2DOT14</span> value and vice versa:
  </p><pre class="programlisting">
    def floatToF2DOT14(f):
      return int(math.floor( (value * 1 &lt;&lt; 14) + 0.5))

    def f2DOT14ToFloat(fixed):
      return fixed / (1 &lt; &lt; 14)
  </pre></div></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="font_file.versions"></a>Version Numbers</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>Most tables have version numbers, and the version number
    for the entire font is contained in the Table
    Directory. Note that there are two different table version
    number types, each with its own numbering scheme:
      </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>
            <span class="type">USHORT</span> version numbers always start at zero
            (<code class="literal">0</code>).
          </p></li><li class="listitem"><p>
            Fixed version numbers (<span class="type">Version</span>) always start at one
            (<code class="literal">1.0</code> or <code class="literal">0x00010000</code>),
            except where noted (<a class="link" href="chapter.EBDT.html" title="Chapter 28. EBDT - Embedded Bitmap Data Table">EBDT</a>,
            <a class="link" href="chapter.EBLC.html" title="Chapter 29. EBLC - Embedded Bitmap Location Table">EBLC</a> and <a class="link" href="chapter.EBSC.html" title="Chapter 30. EBSC - Embedded Bitmap Scaling Table">EBSC</a>
            tables).
          </p></li></ul></div><p><em class="glossterm">Font consumers</em> reading tables
        <em class="glossterm">must</em> include code to check version numbers
        so that if and when the format and therefore the version number
        changes, older implementations will reject newer versions
        gracefully if the changes are incompatible.</p><p>When a <span class="type">Version</span> number is used as a version, the
        upper 16 bits represent the major version number, and the lower
        16 bits represent the minor version number. For example, the version
        number of a <a class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a> table version 0.5 is
        <code class="literal">0x00005000</code>, and that of <a class="link" href="chapter.vhea.html" title="Chapter 38. vhea - Vertical Header Table">vhea</a>
        table version 1.1 is <code class="literal">0x00011000</code>.
        If a <em class="glossterm">font consumer</em> understands a major version
        number, then it can safely proceed reading the table. The
        minor version number indicates extensions to the format that
        are undetectable by implementations that do not support
        them.</p><p>The only exception to this is the
        <a class="link" href="chapter.font_file.html#font_file.offset">Offset Table</a>'s
        <code class="literal">sfnt</code> version, described below.</p><p>When a <span class="type">USHORT</span> number is used to indicate version,
        it should be treated as though it were a minor version number;
        i.e., all format changes are compatible extensions.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="organization"></a>Organization of an CommonType Font</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>A key characteristic of the CommonType format is the
        TrueType <code class="literal">sfnt</code> "wrapper", which provides
        organization for a collection of tables in a general and
        extensible manner.</p><p class="remark"><em><span class="remark">
        <p> A formal definition of "table" is needed here.</p>
      </span></em></p><p>Within a CommonType font file, all tables
        <em class="glossterm">must</em> be aligned to four byte boundries. Any
        remaining space between tables must be padded with zeros.
      </p><div class="section"><div class="titlepage"><div><div><h5 class="title"><a name="section.3.5.1.1"></a>Offset Table</h5></div></div></div><p>A CommonType font file which is not a TrueType Collection
          begins with an <span class="emphasis"><em>Offset Table</em></span> at byte 0 of
          the file. If the font file is a TrueType collection, the font file
          begins with a <code class="literal">TTC Header</code>, which contains a list
          of the byte indexes of the Offset Table of each font in the
          collection.
        </p><div class="table"><a name="idm465839541344"></a><p class="title"><strong>Table 2.1. Offset Table</strong></p><div class="table-contents"><table class="table" summary="Offset Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Version</td><td><code class="literal">sfnt</code> version</td><td>0x00010000 for version 1.0, or the <span class="type">Tag</span> "<code class="literal">OTTO</code>.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numTables</td><td>Number of tables.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>searchRange</td><td>(Maximum power of 2 &lt;= numTables) x
                16.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entrySelector</td><td>Log2(maximum power of 2 &lt;=
                numTables).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>rangeShift</td><td>NumTables x 16-searchRange.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p> CommonType font files whose only <em class="glossterm">glyph representation
          format</em> is TrueType outlines <em class="glossterm">must</em>
          have a <code class="literal">sfnt</code> version of <code class="literal">1.0</code>
          expressed as a <span class="type">Version</span> type. CommonType fonts
          containing other representation formats <em class="glossterm">must</em>
          have a <code class="literal">sfnt</code> version of "<code class="literal">OTTO</code>"
          expressed as a <span class="type">Tag</span> type.
        </p></div><div class="section"><div class="titlepage"><div><div><h5 class="title"><a name="section.3.5.1.2"></a>Table Directory</h5></div></div></div><p>The <span class="emphasis"><em>Offset Table</em></span> is followed immediately
            by the <span class="emphasis"><em>Table Directory</em></span>, which is made up of
            a list of <span class="emphasis"><em>Table Directory Entry</em></span> elements.
            Entries in the <span class="emphasis"><em>Table Directory</em></span> must be
            sorted in ascending order by tag. Offset values in the
            <span class="emphasis"><em>Table Directory Entry</em></span> are measured from the
            start of the font file.
          </p><div class="table"><a name="idm465837134304"></a><p class="title"><strong>Table 2.2. Table Directory Entry</strong></p><div class="table-contents"><table class="table" summary="Table Directory Entry" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>tag</td><td>4 -byte identifier.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>checkSum</td><td>CheckSum for this table.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>offset</td><td>Offset from beginning of TrueType font
                file.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Length of this table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The <span class="emphasis"><em>Table Directory</em></span> makes it possible for
          a given font to contain only those tables it actually needs.
          As a result there is no standard value for <code class="varname">numTables</code>.
        </p><p>Table names are specified as <em class="glossterm">tag</em>s. A
          <em class="glossterm">tag</em> is a reference to a predefined constant
          within a given context. For example, when used as a table name, the
          tag <code class="literal">hhea</code> means "Horizontal header". Tags are
          defined in this specification for table names, CommonType Layout
          feature names, names of languages, and names of scripts.
          All tag names consist of four characters. Tags with less than
          four letters <em class="glossterm">must</em> be followed by the
          necessary trailing spaces. All tag names must be made up of
          printable characters with ASCII values between 32 and 126.
        </p><p>
          The length of all tables recorded in the table
          directory must be their actual length, disregarding any zero
          byte padding required to align tables on four-byte boundaries.
        </p></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465838657872"></a>Calculating Checksums</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.3.6.1"></a>Specification</h4></div></div></div><p>Table checksums are the unsigned sum of the longs of a
        given table. In C, the following function can be used to
        determine a checksum:</p><pre class="programlisting">
ULONG
CalcTableChecksum(ULONG *Table, ULONG Length)
{
ULONG Sum = 0L;
ULONG *Endptr = Table+((Length+3) &amp; ~3) / sizeof(ULONG);

while (Table &lt; EndPtr)
        Sum += *Table++;
return Sum;
}
</pre><p>
        The <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table is a special case, as it
        contains a <code class="varname">checkSumAdjustment</code> field which is
        calculated and written <span class="emphasis"><em>after</em></span> the table's
        checksum is calculated, necessarily invalidating that checksum.
        To calculate the checksum for the <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a>
          table, do the following:
        </p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>Set the <code class="varname">checkSumAdjustment</code> to 0.</p></li><li class="listitem"><p>Calculate the checksum for all the tables including
              the <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table and enter that value
              into the table directory.</p></li><li class="listitem"><p>Calculate the checksum for the entire font.</p></li><li class="listitem"><p>Subtract that value from the hex value
            <code class="literal">B1B0AFBA</code>.</p></li><li class="listitem"><p>Store the result in <code class="varname">checkSumAdjustment</code>.
          </p></li></ol></div><p>Rewriting the <code class="varname">checkSumAdjustment</code> with
          invalidate <code class="varname">checkSum</code> for the
          <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a>. That is not a problem. Do not change it. A
          <em class="glossterm">font consumer</em> attempting to verify that
          the <a class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table has not changed should
          calculate the checkSum for that table by assuming the
          <code class="varname">checkSumAdjustment</code> value is zero before
          comparing the result with the entry in the
          <span class="emphasis"><em>Table Directory</em></span>.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="font_file.ttc"></a>TrueType Collections</h3></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>A <em class="glossterm">TrueType Collection</em> (TTC) is a means
        of delivering multiple CommonType fonts within a single file.
        TrueType Collections are most useful when the fonts to be delivered
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
        files.</p><div role="fragment" class="section"><div class="titlepage"><div><div><h5 class="title"><a name="idm465838637696"></a>The TTC File Structure</h5></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>A TrueType Collection file consists of a single
            <span class="emphasis"><em>TTC Header</em></span> table, one or more
            <span class="emphasis"><em>Offset Tables</em></span> with
            <span class="emphasis"><em>Table Directories</em></span>, and a number of
            CommonType tables. The <span class="emphasis"><em>TTC Header</em></span>
            must be located at the beginning of the TTC file.
          </p><p>
            A CommonType table within a TTC file is found by first locating
            the <span class="emphasis"><em>Offset Table</em></span> and <span class="emphasis"><em>Table Directories</em></span> for the font being consumed.Some of the CommonType tables must appear multiple
            times, once for each font included in the TTC; while other
            tables should be shared by multiple fonts in the TTC.</p><p>
            As an example, consider a TTC file which combines two
              Japanese fonts (Font1 and Font2). The fonts have different
              kana designs (Kana1 and Kana2) but use the same design for
              kanji. The TTC file contains a single
              <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> table which includes both designs of
              kana together with the kanji; both fonts' <span class="emphasis"><em>Table
              Directories</em></span> point to this <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a>
              table. But each font's <span class="emphasis"><em>Table Directory</em></span>
              points to a different <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table, which
              identifies the glyph set to use.
              Font1's <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table points to
              the Kana1 region of the <a class="link" href="chapter.loca.html" title="Chapter 17. loca - Index to Location">loca</a> and
              <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> tables for kana glyphs, and to the
              kanji region for the kanji. Font2's <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
              table points to the Kana2 region of the
              <a class="link" href="chapter.loca.html" title="Chapter 17. loca - Index to Location">loca</a> and <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a> tables
              for kana glyphs, and to the same kanji region for the
              kanji.</p><p>The tables that <dt/> have a
              unique copy per font are
              those that are used by the system in identifying the font
              and its character mapping, including
              <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>, <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>, and
              <a class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a>. The tables that <dt/>
              be shared by fonts in the TTC are those that define glyph
              and instruction data or use glyph indices to access data:
              <a class="link" href="chapter.glyf.html" title="Chapter 16. glyf - Glyf Data">glyf</a>, <a class="link" href="chapter.loca.html" title="Chapter 17. loca - Index to Location">loca</a>,
              <a class="link" href="chapter.hmtx.html" title="Chapter 8. hmtx - Horizontal Metrics">hmtx</a>, <a class="link" href="chapter.hdmx.html" title="Chapter 33. hdmx - Horizontal Device Metrics">hdmx</a>,
              <a class="link" href="chapter.LTSH.html" title="Chapter 35. LTSH - Linear Threshold">LTSH</a>, <a class="link" href="">cvt </a>,
              <a class="link" href="chapter.fpgm.html" title="Chapter 15. fpgm - Font Program">fpgm</a>, <a class="link" href="chapter.prep.html" title="Chapter 18. prep - Control Value Program">prep</a>,
              <a class="link" href="chapter.EBLC.html" title="Chapter 29. EBLC - Embedded Bitmap Location Table">EBLC</a>, <a class="link" href="chapter.EBDT.html" title="Chapter 28. EBDT - Embedded Bitmap Data Table">EBDT</a>,
              <a class="link" href="chapter.EBSC.html" title="Chapter 30. EBSC - Embedded Bitmap Scaling Table">EBSC</a>, <a class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a>, and so
              on. In practice, any tables which have identical data for
              two or more fonts <dt/> be shared.</p><p>When merging multiple font files into a TTC,
              close attention must be paid to the issue
              of glyph renumbering in a font and the side effects that can
              result, in the <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table and elsewhere.
              <em><span class="remark">What side effects? What needs to be remembered?</span></em>
              The fonts to be merged must also have compatible TrueType
              instructions-that is, their preprograms, function
              definitions, and control values must not conflict.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h5 class="title"><a name="font_file.ttcheader"></a>TTC Header</h5></div></div></div><div role="specification" class="section"><div class="titlepage"/><p>There are two versions of the <span class="emphasis"><em>TTC Header</em></span>:
            Version 1.0 was used for TTC files without digital
            signatures. Font producers should now produce version 2.0
            <span class="emphasis"><em>TTC Header</em></span>s, whether or not the files include
            digital signatures. When there is no digital signature,
            the last three fields of the version 2.0 header are zero
            filled.</p><p>If a digital signature is used, the <a class="link" href="chapter.DSIG.html" title="Chapter 31. DSIG - Digital Signature Table">DSIG</a>
            table for the file must be the last table in the TTC file.
            Signatures in a TTC file are expected to be Format 1 signatures.
          </p><p>The purpose of the <span class="emphasis"><em>TTC Header</em></span> table is
            to locate the different <span class="emphasis"><em>Offset Tables</em></span>
            within a TTC file. The <span class="emphasis"><em>TTC Header</em></span> is located
            at the beginning of the TTC file (offset = 0). It consists of
            an identification tag, a version number, a count of the number
            of CommonType fonts (<span class="emphasis"><em>Table Directories</em></span>) in the
            file, and an array of offsets to each <span class="emphasis"><em>Offset
            Table</em></span>.
          </p><div class="table"><a name="idm465838604688"></a><p class="title"><strong>Table 2.3. TTC Header Version 1.0</strong></p><div class="table-contents"><table class="table" summary="TTC Header Version 1.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>TTCTag</td><td>TrueType Collection ID string:
                  <code class="literal">ttcf</code></td><td class="auto-generated"> </td></tr><tr><td>Version</td><td>Version</td><td>Version of the TTC Header (1.0),
                  <code class="literal">0x00010000</code></td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numFonts</td><td>Number of fonts in the TTC</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>OffsetTable [numFonts]</td><td>Array of offsets to Offset Table for each
            font from the beginning of the file</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm465838596080"></a><p class="title"><strong>Table 2.4. TTC Header Version 2.0</strong></p><div class="table-contents"><table class="table" summary="TTC Header Version 2.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Tag</td><td>TTCTag</td><td>TrueType Collection ID string:
                  <code class="literal">ttcf</code></td><td class="auto-generated"> </td></tr><tr><td>Version</td><td>Version</td><td>Version of the TTC Header (2.0),
                  0x00020000</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numFonts</td><td>Number of fonts in the TTC</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>OffsetTable [numFonts]</td><td>Array of offsets to Offset Table for each
            font from the beginning of the file</td><td class="auto-generated"> </td></tr><tr><td>Tag</td><td>ulDsigTag</td><td>Tag indicating that a DSIG table exists,
                <code class="literal">0x44534947</code> (<a class="link" href="chapter.DSIG.html" title="Chapter 31. DSIG - Digital Signature Table">DSIG</a>),
                or <code class="literal">0x00000000</code> if there is no
                <a class="link" href="chapter.DSIG.html" title="Chapter 31. DSIG - Digital Signature Table">DSIG</a> table.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigLength</td><td>The length (in bytes) of the DSIG table (null
                  if no signature)</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulDsigOffset</td><td>The offset (in bytes) of the DSIG table from
                  the beginning of the TTC file (null if no
                  signature)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div></div></div>