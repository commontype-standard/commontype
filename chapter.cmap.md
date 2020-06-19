<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.cmap"></a>Chapter 4. cmap - Character to Glyph Index Mapping Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890901776"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.1.1"></a>Specification</h4></div></div></div><p>This table defines the mapping of character codes to the
          glyph index values used in the font. It may contain more
          than one subtable, in order to support more than one
          character encoding scheme. Character codes that do not
          correspond to any glyph in the font should be mapped to
          glyph index 0. The glyph at this location must be a special
          glyph representing a missing character, commonly known as
          .notdef.</p><p>The table header indicates the character encodings for
          which subtables are present. Each subtable is in one of seven
          possible formats and begins with a format code indicating
          the format used.</p><p>The platform ID and platform-specific encoding ID in the
          header entry (and, in the case of the Macintosh platform,
          the language field in the subtable itself) are used to
          specify a particular <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding.The header entries must be sorted first by platform
          ID, then by platform-specific encoding ID, and then by the
          version field in the corresponding subtable. Each platform
          ID, platform-specific encoding ID, and subtable language
          combination may appear only once in the
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table.</p><p>When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1. When
          building a symbol font for Windows, the platform ID should
          be 3 and the encoding ID should be 0. When building a font
          that will be used on the Macintosh, the platform ID should
          be 1 and the encoding ID should be 0.</p><p>All Microsoft Unicode encodings (Platform ID = 3,
          Encoding ID = 1) must provide at least a Format 4
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable. If the font is meant to
          support supplementary Unicode characters, it will additionally
          need a Format 12 subtable with a platform encoding ID 10.
          The contents of the Format 12 subtable need to be a superset
          of the contents of the Format 4 subtable. Microsoft
          <span class="emphasis"><em>strongly</em></span> recommends using a Unicode
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> for all fonts. However, some other
          encodings that appear in current fonts follow:</p><div class="table"><a name="idm516890892640"></a><p class="title"><strong>Table 4.1. Microsoft Encodings</strong></p><div class="table-contents"><table class="table" summary="Microsoft Encodings" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Platform ID</th><th>Encoding ID</th><th>Description</th></tr></thead><tbody><tr><td>3</td><td>0</td><td>Symbol</td></tr><tr><td>3</td><td>1</td><td>Unicode</td></tr><tr><td>3</td><td>2</td><td>ShiftJIS</td></tr><tr><td>3</td><td>3</td><td>PRC</td></tr><tr><td>3</td><td>4</td><td>Big5</td></tr><tr><td>3</td><td>5</td><td>Wansung</td></tr><tr><td>3</td><td>6</td><td>Johab</td></tr><tr><td>3</td><td>7</td><td>Reserved</td></tr><tr><td>3</td><td>9</td><td>Reserved</td></tr><tr><td>3</td><td>9</td><td>Reserved</td></tr><tr><td>3</td><td>10</td><td>UCS-4</td></tr></tbody></table></div></div><br class="table-break"/><p>Unicode Variation Sequences supported by the font may be
        specified in the cmap table under platform ID 0 and encoding
        ID 5, using a format 14 cmap subtable.</p><p>The Character To Glyph Index Mapping Table is organized
          as follows:</p><div class="table"><a name="idm516890871008"></a><p class="title"><strong>Table 4.2. cmap Header</strong></p><div class="table-contents"><table class="table" summary="cmap Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Table version number (0).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numTables</td><td>Number of encoding tables that follow.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The cmap table header is followed by an array of
	  encoding records that specify the particular encoding and
	  the offset to the subtable for that encoding. The number of
	  encoding records is numTables. An encoding record entry
	  looks like:</p><div class="table"><a name="idm516890865232"></a><p class="title"><strong>Table 4.3. Encoding Record</strong></p><div class="table-contents"><table class="table" summary="Encoding Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>platformID</td><td>Platform ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>encodingID</td><td>Platform-specific encoding ID.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>offset</td><td>Byte offset from beginning of table to the
                  subtable for this encoding.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.1.2"></a>Annotation</h4></div></div></div><p>The first paragraph covers three cases of missing
          glyphs: (1) there is a cmap subtable for the encoding but
          the character code is not covered by the subtable; (2) there
          is no subtable for the encoding; (3) there is a cmap for the
          encoding, but the format of that subtable is not 0, 2, 4 or
          6, 8, 10, or 12 (the currently defined formats). It is quite
          clear that the described behaviour applies to the first
          case, but it is not clear that this is the mandated
          behaviour in the second or third case. We assume it is.
          Recommendation: make that clear, by rephrasing: "Character
          codes that do not correspond to any glyph in the font
          (either because there is no subtable for their encoding or
          or because the subtable in a format not supported by the
          application or because the subtable does not map them)
          should be mapped to glyph index 0."</p><p>The case of unknown formats is a bit more complicated.
          The recommendation is to mandate that all characters codes
          should map to glyph 0 for subtables in unknown
          formats.</p><p>The descriptions of the fields of this table do not include
          names for them, as most other tables do. The recommendation
          is to include them: version, numTables, platformID,
          encodingID, offset.</p><p>In the fifth paragraph, "UCS-4 (surrogate) characters"
          should be replaced by "Unicode supplemental characters" or
          "Unicode supplemental (non-BMP) characters". BMP characters are also
          UCS-4 characters. And anyways, UCS-4 is an encoding, not a
          character collection.</p><p>It is legal to have a single subtable which is referenced
          from multiple entries? This is useful when a given character
          encoding is present on multiple platforms. For example, if
          there is a Unicode cmap subtable, it can be referenced from
          one entry with platformID/encodingID (0, 3), and from
          another entry with (3, 1).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="cmap_cust"></a>OTF Windows NT compatibility mapping</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.2.1"></a>Specification</h4></div></div></div><p>If a platform ID 4 (custom), encoding ID 0-255 (OTF
          Windows NT compatibility mapping) <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding is present in an CommonType font with CFF outlines,
          then the OTF font driver in Windows NT will: (a) superimpose
          the glyphs encoded at character codes 0-255 in the encoding
          on the corresponding Windows ANSI (code page 1252) Unicode
          values in the Unicode encoding it reports to the system; (b)
          add Windows ANSI (CharSet 0) to the list of CharSets
          supported by the font; and (c) consider the value of the
          encoding ID to be a Windows CharSet value and add it to the
          list of CharSets supported by the font. Note: The
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must use Format 0 or 6 for
          its subtable, and the encoding must be identical to the
          CFF's encoding.</p><p>This <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> encoding is not required.
          It provides a compatibility mechanism for non-Unicode
          applications that use the font as if it were Windows ANSI
          encoded. Non-Windows ANSI Type 1 fonts, such as Cyrillic and
          Central European fonts, that Adobe shipped in the past had
          "0" (Windows ANSI) recorded in the CharSet field of the .PFM
          file; ATM for Windows 9x ignores the CharSet altogether.
          Adobe provides this compatibility <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding in every OTF converted from a Type1 font in which
          the Encoding is not StandardEncoding.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="language_note"></a>Note on the language field in cmap
        subtables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.3.1"></a>Specification</h4></div></div></div><p>This field must be set to zero for all
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtables whose platform IDs are
          other than Macintosh (platform ID 1). For
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtables whose platform IDs are
          Macintosh, set this field to the Macintosh language ID of
          the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable plus one, or to zero if
          the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable is not
          language-specific. For example, a Mac OS Turkish
          <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must set this field to 18,
          since the Macintosh language ID for Turkish is 17. A Mac OS
          Roman <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must set this field
          to 0, since Mac OS Roman is not a language-specific
          encoding.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890838288"></a>Format 0: Byte encoding table</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.4.1"></a>Specification</h4></div></div></div><p>This is the Apple standard character to glyph index
          mapping table.</p><div class="table"><a name="idm516890836080"></a><p class="title"><strong>Table 4.4. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format number is set to 0.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in this
              document.</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>glyphIdArray[256]</td><td>An array that maps character codes to glyph
              index values.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is a simple 1 to 1 mapping of character codes to
          glyph indices. The glyph set is limited to 256. Note that if
          this format is used to index into a larger glyph set, only
          the first 256 glyphs will be accessible.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.4.2"></a>Annotation</h4></div></div></div><p>As the declaration stands, the length field seems
          superfluous, since the table appears to always be 262 bytes
          long. This can be explained in one of two ways:

          </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>the length field is included to make the first three
                words of all cmap subtables similar; it must always be
                262.</p></li><li class="listitem"><p>the glyphIdArray does not need to be always 256
                elements long, it can be shorter.</p></li></ul></div><p>
      </p><p>In the spirit of "generate conservatively, accept
          liberally", we recommend that font designers always put 256
          entries in glyphIdArray (and consequently set length to 262), and
          that font consumers be ready to handle fonts where the
          glyphIdArray contains length - 6 entries (but no more than
          256).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890821728"></a>Format 2: High-byte mapping through table </h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.5.1"></a>Specification</h4></div></div></div><p>This subtable is useful for the national character code
          standards used for Japanese, Chinese, and Korean characters.
          These code standards use a mixed 8/16-bit encoding, in which
          certain byte values signal the first byte of a 2-byte
          character (but these values are also legal as the second
          byte of a 2-byte character).</p><p>In addition, even for the 2-byte characters, the mapping
          of character codes to glyph index values depends heavily on
          the first byte. Consequently, the table begins with an array
          that maps the first byte to a 4-word subHeader. For 2-byte
          character codes, the subHeader is used to map the second
          byte's value through a subArray, as described below. When
          processing mixed 8/16-bit text, subHeader 0 is special: it
          is used for single-byte character codes. When subHeader zero
          is used, a second byte is not needed; the single byte value
          is mapped through the subArray.</p><div class="table"><a name="idm516890818144"></a><p class="title"><strong>Table 4.5. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format number is set to 2.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>subHeaderKeys [256]</td><td>Array that maps high bytes to subHeaders:
              value is subHeader index * 8.</td><td class="auto-generated"> </td></tr><tr><td>4 words struct</td><td>subHeaders []</td><td>Variable-length array of subHeader
              structures.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>glyphIndexArray []</td><td>Variable-length array containing subarrays
              used for mapping the low byte of 2-byte
              characters.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A subHeader is structured as follows:</p><div class="table"><a name="idm516890805584"></a><p class="title"><strong>Table 4.6. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>firstCode</td><td>First valid low byte for this
              subHeader.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entryCount</td><td>Number of valid low bytes for this
              subHeader.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>idDelta</td><td>See text below.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>idRangeOffset</td><td>See text below.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The firstCode and entryCount values specify a subrange
          that begins at firstCode and has a length equal to the value
          of entryCount. This subrange stays within the 0-255 range of
          the byte being mapped. Bytes outside of this subrange are
          mapped to glyph index 0 (missing glyph). The offset of the
          byte within this subrange is then used as index into a
          corresponding subarray of glyphIndexArray. This subarray is
          also of length entryCount. The value of the idRangeOffset is
          the number of bytes past the actual location of the
          idRangeOffset word where the glyphIndexArray element
          corresponding to firstCode appears.</p><p>Finally, if the value obtained from the subarray is not
          0 (which indicates the missing glyph), you should add
          idDelta to it in order to get the glyphIndex. The value
          idDelta permits the same subarray to be used for several
          different subheaders. The idDelta arithmetic is modulo
          65536.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.5.2"></a>Annotation</h4></div></div></div><p>How about an intelligible description of the use of this
        format? Assuming that it intends to describe the same
        structure as the Apple True Type format, simply switching to
        their version would already be a vast improvement.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890793616"></a>Format 4: Segment mapping to delta values</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.6.1"></a>Specification</h4></div></div></div><p>This is the Microsoft standard character to glyph index
          mapping table for fonts that support Unicode ranges other
          than the range [U+D800 - U+DFFF] (defined as Surrogates
          Area, in Unicode v 3.0) which is used for UCS-4
          characters. If a font supports this character range (i.e. in
          turn supports the UCS-4 characters) a subtable in this
          format with a platform specific encoding ID 1 is yet needed,
          in addition to a subtable in format 12 with a platform
          specific encoding ID 10. Please see details on format 12
          below, for fonts that support UCS-4 characters on
          Windows.</p><p>This format is used when the character codes for the
          characters represented by a font fall into several
          contiguous ranges, possibly with holes in some or all of the
          ranges (that is, some of the codes in a range may not have a
          representation in the font). The format-dependent data is
          divided into three parts, which must occur in the following
          order:</p><div class="orderedlist"><ol class="orderedlist" type="1"><li class="listitem"><p>A four-word header gives parameters for an optimized
              search of the segment list;</p></li><li class="listitem"><p>Four parallel arrays describe the segments (one
              segment for each contiguous range of codes);</p></li><li class="listitem"><p>A variable-length array of glyph IDs (unsigned
              words).</p></li></ol></div><div class="table"><a name="idm516890786992"></a><p class="title"><strong>Table 4.7. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format number is set to 4.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>segCountX2</td><td>2 x segCount.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>searchRange</td><td>2 x (2**floor(log2(segCount)))</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entrySelector</td><td>log2(searchRange/2)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>rangeShift</td><td>2 x segCount - searchRange</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>endCount [segCount]</td><td>End characterCode for each segment,
              last=0xFFFF.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>reservedPad</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>startCount [segCount]</td><td>Start character code for each
              segment.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>idDelta [segCount]</td><td>Delta for all character codes in
              segment.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>idRangeOffset [segCount]</td><td>Offsets into glyphIdArray or 0</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>glyphIdArray []</td><td>Glyph index array (arbitrary length)
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The number of segments is specified by segCount, which
          is not explicitly in the header; however, all of the header
          parameters are derived from it. The searchRange value is
          twice the largest power of 2 that is less than or equal to
          segCount. For example, if segCount=39, we have the
          following:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/></colgroup><tbody><tr><td>segCountX2</td><td>78</td><td> </td></tr><tr><td>searchRange</td><td>64</td><td>(2 * largest power of 2 &lt;=39)</td></tr><tr><td>entrySelector</td><td>5</td><td>log2 (32)</td></tr><tr><td>rangeShift</td><td>14</td><td>2 x 39 - 64</td></tr></tbody></table></div><p>Each segment is described by a startCode and endCode,
          along with an idDelta and an idRangeOffset, which are used
          for mapping the character codes in the segment. The segments
          are sorted in order of increasing endCode values, and the
          segment values are specified in four parallel arrays. You
          search for the first endCode that is greater than or equal
          to the character code you want to map. If the corresponding
          startCode is less than or equal to the character code, then
          you use the corresponding idDelta and idRangeOffset to map
          the character code to a glyph index (otherwise, the
          missingGlyph is returned). For the search to terminate, the
          final endCode value must be 0xFFFF. This segment need not
          contain any valid mappings. (It can just map the single
          character code 0xFFFF to missingGlyph). However, the segment
          must be present.</p><p>If the idRangeOffset value for the segment is not 0, the
          mapping of character codes relies on glyphIdArray. The
          character code offset from startCode is added to the
          idRangeOffset value. This sum is used as an offset from the
          current location within idRangeOffset itself to index out
          the correct glyphIdArray value. This obscure indexing trick
          works because glyphIdArray immediately follows idRangeOffset
          in the font file. The C expression that yields the glyph
          index is:</p><div class="literallayout"><p><br/>
  *(idRangeOffset[i]/2<br/>
    + (c - startCount[i])<br/>
    + &amp;idRangeOffset[i])<br/>
    </p></div><p>The value c is the character code in question, and i is
          the segment index in which c appears. If the value obtained
          from the indexing operation is not 0 (which indicates
          missingGlyph), idDelta[i] is added to it to get the glyph
          index. The idDelta arithmetic is modulo 65536.</p><p>If the idRangeOffset is 0, the idDelta value is added
          directly to the character code offset (i.e. idDelta[i] + c)
          to get the corresponding glyph index. Again, the idDelta
          arithmetic is modulo 65536.</p><p>As an example, the variant part of the table to map
          characters 10-20, 30-90, and 153-480 onto a contiguous range
          of glyph indices may look like this:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/></colgroup><tbody><tr><td>segCountX2:</td><td>8</td><td> </td><td> </td><td> </td></tr><tr><td>searchRange:</td><td>8</td><td> </td><td> </td><td> </td></tr><tr><td>entrySelector:</td><td>4</td><td> </td><td> </td><td> </td></tr><tr><td>rangeShift:</td><td>0</td><td> </td><td> </td><td> </td></tr><tr><td>endCode:</td><td>20</td><td>90</td><td>480</td><td>0Xffff</td></tr><tr><td>reservedPad:</td><td>0</td><td> </td><td> </td><td> </td></tr><tr><td>startCode:</td><td>10</td><td>30</td><td>153</td><td>0Xffff</td></tr><tr><td>idDelta:</td><td>-9</td><td>-18</td><td>-27</td><td>1</td></tr><tr><td>idRangeOffset:</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></tbody></table></div><p>This table performs the following mappings:</p><div class="literallayout"><p><br/>
10 -&gt; 10 - 9 = 1<br/>
20 -&gt; 20 - 9 = 11<br/>
30 -&gt; 30 - 18 = 12<br/>
90 -&gt; 90 - 18 = 72<br/>
...and so on.<br/>
</p></div><p>Note that the delta values could be reworked so as to
          reorder the segments.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.6.2"></a>Annotation</h4></div></div></div><p>The first sentence should probably be changed to
        "... for fonts that support Unicode BMP characters".</p><p>In the table that describes the fields, it seems that
          the fields startCount and endCount should instead be
          startCode and endCode. These are better names, and are the
          names used in the text.</p><p>In the example, the idDelta of the third range should
          probably be -80, so that the character code 153 is mapped to
          the glyphID 153-80 = 73.</p><p>The meaning of the last sentence escapes me. May be it
        should be removed?</p><p>It seems a necessary property of this format that the
          segments be disjoint, yet it is not mentionned
          explicitly.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890725984"></a>Format 6: Trimmed table mapping </h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.7.1"></a>Specification</h4></div></div></div><div class="table"><a name="idm516890724144"></a><p class="title"><strong>Table 4.8. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format number is set to 6.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>firstCode</td><td>First character code of
              subrange.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>entryCount</td><td>Number of character codes in
              subrange.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>glyphIdArray [entryCount]</td><td>Array of glyph index values for character
              codes in the range. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The firstCode and entryCount values specify a subrange
          (beginning at firstCode, length = entryCount) within the
          range of possible character codes. Codes outside of this
          subrange are mapped to glyph index 0. The offset of the code
          (from the first code) within this subrange is used as index
          to the glyphIdArray, which provides the glyph index
          value.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.7.2"></a>Annotation</h4></div></div></div><p>It is unclear whether the entryCount can be 0. We assume
          it can and recommend to add a sentence to that
          effect.</p><p>This format is very similar to format 0, in that there
          is an explicit list of glyph indices for a contiguous range
          of character code. However, there are two intersting
          properties: the range can be bigger than 256; and more
          importantly, the glyph indices are USHORT instead of
          BYTE. So this format can be used for byte encodings to reach
          glyphs other than the first 256 glyphs.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890707792"></a>Supporting 4-byte character codes</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.8.1"></a>Specification</h4></div></div></div><p>While the four existing <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable formats which
          currently exist have served us well, the introduction of the
          Surrogates Area in Unicode 2.0 has stressed them past the
          point of utility. This section specifies three formats,
          format 8, 10 and 12; which directly support 4-byte character
          codes. A major change introduced with these three formats is
          a more pure 32-bit orientation. The <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table version
          number will continue to be 0x0000, for those fonts that make
          use of these formats.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.8.2"></a>Annotation</h4></div></div></div><p>A better formulation in the first sentence could be
        "... the introduction of supplemental characters in Unicode
        2.0..."</p><p>The semicolon after "12" should be changed to a
        comma.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890700912"></a>Format 8: mixed 16-bit and 32-bit coverage</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.9.1"></a>Specification</h4></div></div></div><p>Format 8 is a bit like format 2, in that it provides for
          mixed-length character codes. If a font contains characters
          from the Unicode Surrogates Area (U+D800-U+DFFF), which are
          UCS-4 characters; it's likely that it will also include
          other, regular 16-bit Unicodes as well. We therefore need a
          format to map a mixture of 16-bit and 32-bit character
          codes, just as format 2 allows a mixture of 8-bit and 16-bit
          codes. A simplifying assumption is made: namely, that there
          are no 32-bit character codes which share the same first 16
          bits as any 16-bit character code. This means that the
          determination as to whether a particular 16-bit value is a
          standalone character code or the start of a 32-bit character
          code can be made by looking at the 16-bit value directly,
          with no further information required.</p><p>Here's the format 8 subtable format:</p><div class="table"><a name="idm516890697312"></a><p class="title"><strong>Table 4.9. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Subtable format; set to 8.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>reserved</td><td>Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Byte length of this subtable (including the
              header)</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>is32 [8192]</td><td>Tightly packed array of bits (8K bytes total)
              indicating whether the particular 16-bit (index) value
              is the start of a 32-bit character code
                </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td> nGroups</td><td> Number of groupings which follow
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Here follow the individual groups. Each group has the
          following format:</p><div class="table"><a name="idm516890684368"></a><p class="title"><strong>Table 4.10. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td> startCharCode</td><td> First character code in this group; note
              that if this group is for one or more 16-bit character
              codes (which is determined from the is32 array), this
              32-bit value will have the high 16-bits set to zero
            </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td> endCharCode</td><td> Last character code in this group; same
              condition as listed above for the startCharCode
                </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td> startGlyphID</td><td> Glyph index corresponding to the starting
              character code </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>A few notes here. The endCharCode is used, rather than a
          count, because comparisons for group matching are usually
          done on an existing character code, and having the
          endCharCode be there explicitly saves the necessity of an
          addition per group. Groups must be sorted by increasing
          startCharCode. A group's endCharCode must be less than the
          startCharCode of the following group, if any.</p><p>To determine if a particular word (cp) is the first half
          of 32-bit code points, one can use an expression such as (
          is32[ cp / 8 ] &amp; ( 1 &lt;&lt; ( 7 - ( cp % 8 ) ) ) ). If this is
          non-zero, then the word is the first half of a 32-bit code
          point.</p><p>0 is not a special value for the high word of a 32-bit
          code point. A font may not have both a glyph for the code
          point 0x0000 and glyphs for code points with a high word of
          0x0000.</p><p>The presence of the packed array of bits indicating
          whether a particular 16-bit value is the start of a 32-bit
          character code is useful even when the font contains no
          glyphs for a particular 16-bit start value. This is because
          the system software often needs to know how many bytes ahead
          the next character begins, even if the current character
          maps to the missing glyph. By including this information
          explicitly in this table, no "secret" knowledge needs to be
          encoded into the OS.</p><p>Although this format might work advantageously on some
          platforms for non-Unicode encodings, Microsoft does not
          support it for Unicode encoded UCS-4 characters.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.9.2"></a>Annotation</h4></div></div></div><p>First paragraph, second sentence, should be: "If a font
          maps Unicode supplemental characters, it's likely to map
          Unicode BMP characters as well."</p><p>For coherence with the other formats, the description of
          the format field should be "Format number is set to 8" and
          the description of the length field should be "This is the
          length in bytes of the subtable."</p><p>This format is dubious and would probably best be
          deprecated. If For Unicode encodings, it is useful only for
          UTF-16 (the only version that has 16 bit code units), so
          spending 8K bytes to is

If the intent is really for a Unicode encodings,
          then it is known </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890670160"></a>Format 10: Trimmed array</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.10.1"></a>Specification</h4></div></div></div><p>Format 10 is a bit like format 6, in that it defines a
        trimmed array for a tight range of 32-bit character
        codes:</p><div class="table"><a name="idm516890667808"></a><p class="title"><strong>Table 4.11. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Subtable format; set to 10.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>reserved</td><td>Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td> startCharCode</td><td> First character code covered </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td> numChars</td><td> Number of character codes covered
            </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td> glyphs []</td><td> Array of glyph indices for the character
              codes covered </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This format is not supported by Microsoft.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.10.2"></a>Annotation</h4></div></div></div><p>For coherence with the other formats, the description of
        the format field should be "Format number is set to 10" and the
        description of the length field should be "This is the length
        in bytes of the subtable."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890651120"></a>Format 12: Segmented coverage</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.11.1"></a>Specification</h4></div></div></div><p>This is the Microsoft standard character to glyph index
          mapping table for fonts supporting the UCS-4 characters in
          the Unicode Surrogates Area (U+D800 - U+DFFF). It is a bit
          like format 4, in that it defines segments for sparse
          representation in 4-byte character space. Here's the
          subtable format:</p><div class="table"><a name="idm516890648560"></a><p class="title"><strong>Table 4.12. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Subtable format; set to 12.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>reserved</td><td>Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>language</td><td>Please see <a class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>nGroups</td><td>Number of groupings which follow
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Fonts providing Unicode encoded UCS-4 character support
          for Windows 2000 and later, need to have a subtable with
          platform ID 3, platform specific encoding ID 1 in format 4;
          and in addition, need to have a subtable for platform ID 3,
          platform specific encoding ID 10 in format 12. Please note,
          that the content of format 12 subtable, needs to be a super
          set of the content in the format 4 subtable. The format 4
          subtable needs to be in the cmap table to enable backward
          compatibility needs.</p><p>Here follow the individual groups, each of which has the
          following format:</p><div class="table"><a name="idm516890636864"></a><p class="title"><strong>Table 4.13. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>startCharCode</td><td>First character code in this group
            </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>endCharCode</td><td>Last character code in this group
            </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>startGlyphID</td><td>Glyph index corresponding to the starting
              character code </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Groups must be sorted by increasing startCharCode. A
          group's endCharCode must be less than the startCharCode of
          the following group, if any. The endCharCode is used, rather
          than a count, because comparisons for group matching are
          usually done on an existing character code, and having the
          endCharCode be there explicitly saves the necessity of an
          addition per group.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.11.2"></a>Annotation</h4></div></div></div><p>First paragraph, first sentence should be reworded: "...
          for fonts supporting Unicode supplemental characters."
          Similarly, second paragraph, first sentence should be
          reworded: "Fonts providing support for Unicode supplemental
          characters..."</p><p>For coherence with the other formats, the description of
          the format field should be "Format number is set to 12" and
          the description of the length field should be "This is the
          length in bytes of the subtable."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516890626400"></a>Format 14: Unicode Variation Sequences</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.12.1"></a>Specification</h4></div></div></div><p>Subtable format 14 specifies the Unicode Variation
        Sequences (UVSes) supported by the font. A Variation Sequence,
        according to the Unicode Standard, comprises a base character
        followed by a variation selector; e.g. &lt;U+82A6,
        U+E0101&gt;.</p><p>The subtable partitions the UVSes supported by the font
        into two categories: “default” and
        “non-default” UVSes. Given a UVS, if the glyph
        obtained by looking up the base character of that sequence in
        the Unicode cmap subtable (i.e. the UCS-4 or the BMP cmap
        subtable) is the glyph to use for that sequence, then the
        sequence is a “default” UVS; otherwise it is a
        “non-defaultJ=f UVS, and the glyph to use for that
        sequence is specified in the format 14 subtable itself.</p><p>The example below shows how a font vendor can use format
        14 for a JIS-2004-aware font.</p><div class="table"><a name="idm516890622032"></a><p class="title"><strong>Table 4.14. Format 14 header</strong></p><div class="table-contents"><table class="table" summary="Format 14 header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Subtable format; set to 14.</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>length</td><td>Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numVarSelectorRecords</td><td>Number of Variation Selector Records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is immediately followed by 'numVarSelectorRecords'
        Variation Selector Records.</p><div class="table"><a name="idm516890614720"></a><p class="title"><strong>Table 4.15. Variation Selector Record</strong></p><div class="table-contents"><table class="table" summary="Variation Selector Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>UINT24</td><td>varSelector</td><td>Variation selector</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>defaultUVSOffset</td><td>Offset to Default UVS Table. May be 0. </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>nonDefaultUVSOffset</td><td>Offset to Non-Default UVS Table. May be 0.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The Variation Selector Records are sorted in increasing
        order of 'varSelector'. No two records may have the same
        'varSelector'. All offsets in a record are relative to the
        beginning of the format 14 cmap subtable.</p><p>A Variation Selector Record and the data its offsets
        point to specify those UVSes supported by the font for which
        the variation selector is the 'varSelector' value of the
        record. The base characters of the UVSes are stored in the
        tables pointed to by the offsets. The UVSes are partitioned by
        whether they are default or non-default UVSes.</p><p>Glyph IDs to be used for non-default UVSes are specified
        in the Non-Default UVS table.</p><p>Default UVS Table</p><p>A Default UVS Table is simply a range-compressed list of
        Unicode scalar values, representing the base characters of the
        default UVSes which use the 'varSelector' of the associated
        Variation Selector Record.</p><div class="table"><a name="idm516890604992"></a><p class="title"><strong>Table 4.16. Default UVS Table header</strong></p><div class="table-contents"><table class="table" summary="Default UVS Table header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>numUnicodeValueRanges</td><td>Number of ranges that follow</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is immediately followed by 'numUnicodeValueRanges'
        Unicode Value Ranges, each of which represents a contiguous
        range of Unicode values.</p><div class="table"><a name="idm516890600624"></a><p class="title"><strong>Table 4.17. Unicode Value Range</strong></p><div class="table-contents"><table class="table" summary="Unicode Value Range" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>UINT24</td><td>startUnicodeValue</td><td>First value in this range</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>additionalCount</td><td>Number of <span class="emphasis"><em>additional</em></span>
            values in this range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>For example, the range U+4E4D...U+4E4F (3 values) will
        set 'startUnicodeValue' to 0x004E4D and 'additionalCount' to
        2. A singleton range will set 'additionalCount' to 0.</p><p>('startUnicodeValue' + 'additionalCount') must not
        exceed 0xFFFFFF.</p><p>The Unicode Value Ranges are sorted in increasing order
        of 'startUnicodeValue'. The ranges must not overlap; i.e.,
        ('startUnicodeValue' + 'additionalCount') must be less than
        the 'startUnicodeValue' of the following range (if
        any).</p><p>Non-Default UVS Table</p><p>A Non-Default UVS Table is a list of pairs of Unicode
        scalar values and glyph IDs. The Unicode values represent the
        base characters of all non-default UVSes which use the
        'varSelector' of the associated Variation Selector Record, and
        the glyph IDs specify the glyph IDs to use for the
        UVSes.</p><div class="table"><a name="idm516890592064"></a><p class="title"><strong>Table 4.18. Non-Default UVS Table header</strong></p><div class="table-contents"><table class="table" summary="Non-Default UVS Table header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>numUVSMappings</td><td>Number of UVS Mappings that follow</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This is immediately followed by 'numUVSMappings' UVS
        Mappings.</p><div class="table"><a name="idm516890587776"></a><p class="title"><strong>Table 4.19. UVS Mapping</strong></p><div class="table-contents"><table class="table" summary="UVS Mapping" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>UINT24</td><td>unicodeValue</td><td>Base Unicode value of the UVS</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>glyphID</td><td>Glyph ID of the UVS</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The UVS Mappings are sorted in increasing order of
        'unicodeValue'. No two mappings in this table may have the
        same 'unicodeValue' values.</p><p>Example</p><p>Here is an example of how a format 14 cmap subtable may
        be used in a font that is aware of JIS-2004 variant
        glyphs. The CIDs (character IDs) in this example refer to
        those in the Adobe Character Collection 'Adobe-Japan1', and
        may be assumed to be identical to the glyph IDs in the font in
        our example.</p><p>JIS-2004 changed the default glyph variants for some of
        its code points. For example:</p><p>JIS-90: U+82A6 -&gt; CID 1142</p><p>JIS-2004: U+82A6 -&gt; CID 7961</p><p>Both of these glyph variants are supported through the
        use of UVSes, as the following examples from Unicode's UVS
        registry show:</p><p>U+82A6 U+E0100 -&gt; CID 1142</p><p>U+82A6 U+E0101 -&gt; CID 7961</p><p>If the font wants to support the JIS-2004 variants by
        default, it will:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>encode glyph ID 7961 at U+82A6 in the Unicode cmap
            subtable,</p></li><li class="listitem"><p>specify &lt;U+82A6, U+E0101&gt; in the UVS cmap
            subtable's Default UVS Table ('varSelector' will be
            0x0E0101 and 'defaultUVSOffset' will point to data
            containing a 0x0082A6 Unicode value)</p></li><li class="listitem"><p>specify &lt;U+82A6, U+E0100&gt; -&gt; glyph ID 1142 in the
            UVS cmap subtable's Non-Default UVS Table ('varSelector'
            will be 0x0E0100 and 'nonDefaultBaseUVOffset' will point
            to data containing a 'unicodeValue' 0x82A6 and 'glyphID'
            1142). </p></li></ul></div><p>If, however, the font wants to support the JIS-90
        variants by default, it will:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>encode glyph ID 1142 at U+82A6 in the Unicode cmap
            subtable,</p><p>specify &lt;U+82A6, U+E0100&gt; in the
            UVS cmap subtable's Default UVS Table</p></li><li class="listitem"><p>specify &lt;U+82A6, U+E0101&gt; -&gt; glyph ID 7961 in the
            UVS cmap subtables Non-Default UVS Table </p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516889504864"></a>Various test fonts</h3></div></div></div></div></div>