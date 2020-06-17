<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.cmap"></a>Chapter 5. cmap - Character to Glyph Index Mapping Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800201696"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.1.1"></a>Specification</h3></div></div></div><p role="">This table defines the mapping of character codes to the
          glyph index values used in the font. It may contain more
          than one subtable, in order to support more than one
          character encoding scheme. Character codes that do not
          correspond to any glyph in the font should be mapped to
          glyph index 0. The glyph at this location must be a special
          glyph representing a missing character, commonly known as
          .notdef.</p><p role="">The table header indicates the character encodings for
          which subtables are present. Each subtable is in one of seven
          possible formats and begins with a format code indicating
          the format used.</p><p role="">The platform ID and platform-specific encoding ID in the
          header entry (and, in the case of the Macintosh platform,
          the language field in the subtable itself) are used to
          specify a particular <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding.The header entries must be sorted first by platform
          ID, then by platform-specific encoding ID, and then by the
          version field in the corresponding subtable. Each platform
          ID, platform-specific encoding ID, and subtable language
          combination may appear only once in the
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table.</p><p role="">When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1. When
          building a symbol font for Windows, the platform ID should
          be 3 and the encoding ID should be 0. When building a font
          that will be used on the Macintosh, the platform ID should
          be 1 and the encoding ID should be 0.</p><p role="">All Microsoft Unicode encodings (Platform ID = 3,
          Encoding ID = 1) must provide at least a Format 4
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable. If the font is meant to
          support supplementary Unicode characters, it will additionally
          need a Format 12 subtable with a platform encoding ID 10.
          The contents of the Format 12 subtable need to be a superset
          of the contents of the Format 4 subtable. Microsoft
          <span role="" class="emphasis"><em>strongly</em></span> recommends using a Unicode
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> for all fonts. However, some other
          encodings that appear in current fonts follow:</p><div class="table"><a name="idm80800193056"></a><p class="title"><strong>Table 5.1. Microsoft Encodings</strong></p><div class="table-contents"><table role="" class="table" summary="Microsoft Encodings" border="1"><colgroup><col width="10pc"/><col width="10pc"/><col width="10pc"/></colgroup><thead><tr><th role="">Platform ID</th><th role="">Encoding ID</th><th role="">Description</th></tr></thead><tbody><tr><td role="">3</td><td role="">0</td><td role="">Symbol</td></tr><tr><td role="">3</td><td role="">1</td><td role="">Unicode</td></tr><tr><td role="">3</td><td role="">2</td><td role="">ShiftJIS</td></tr><tr><td role="">3</td><td role="">3</td><td role="">PRC</td></tr><tr><td role="">3</td><td role="">4</td><td role="">Big5</td></tr><tr><td role="">3</td><td role="">5</td><td role="">Wansung</td></tr><tr><td role="">3</td><td role="">6</td><td role="">Johab</td></tr><tr><td role="">3</td><td role="">7</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">9</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">9</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">10</td><td role="">UCS-4</td></tr></tbody></table></div></div><br class="table-break"/><p role="">Unicode Variation Sequences supported by the font may be
        specified in the cmap table under platform ID 0 and encoding
        ID 5, using a format 14 cmap subtable.</p><p role="">The Character To Glyph Index Mapping Table is organized
          as follows:</p><div class="table"><a name="idm80800170016"></a><p class="title"><strong>Table 5.2. cmap Header</strong></p><div class="table-contents"><table role="" class="table" summary="cmap Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Table version number (0).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numTables</td><td role="">Number of encoding tables that follow.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The cmap table header is followed by an array of
	  encoding records that specify the particular encoding and
	  the offset to the subtable for that encoding. The number of
	  encoding records is numTables. An encoding record entry
	  looks like:</p><div class="table"><a name="idm80800164272"></a><p class="title"><strong>Table 5.3. Encoding Record</strong></p><div class="table-contents"><table role="" class="table" summary="Encoding Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">platformID</td><td role="">Platform ID.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">encodingID</td><td role="">Platform-specific encoding ID.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">offset</td><td role="">Byte offset from beginning of table to the
                  subtable for this encoding.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.1.2"></a>Annotation</h3></div></div></div><p role="">The first paragraph covers three cases of missing
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
          should be mapped to glyph index 0."</p><p role="">The case of unknown formats is a bit more complicated.
          The recommendation is to mandate that all characters codes
          should map to glyph 0 for subtables in unknown
          formats.</p><p role="">The descriptions of the fields of this table do not include
          names for them, as most other tables do. The recommendation
          is to include them: version, numTables, platformID,
          encodingID, offset.</p><p role="">In the fifth paragraph, "UCS-4 (surrogate) characters"
          should be replaced by "Unicode supplemental characters" or
          "Unicode supplemental (non-BMP) characters". BMP characters are also
          UCS-4 characters. And anyways, UCS-4 is an encoding, not a
          character collection.</p><p role="">It is legal to have a single subtable which is referenced
          from multiple entries? This is useful when a given character
          encoding is present on multiple platforms. For example, if
          there is a Unicode cmap subtable, it can be referenced from
          one entry with platformID/encodingID (0, 3), and from
          another entry with (3, 1).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="cmap_cust"></a>OTF Windows NT compatibility mapping</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.2.1"></a>Specification</h3></div></div></div><p role="">If a platform ID 4 (custom), encoding ID 0-255 (OTF
          Windows NT compatibility mapping) <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding is present in an OpenType font with CFF outlines,
          then the OTF font driver in Windows NT will: (a) superimpose
          the glyphs encoded at character codes 0-255 in the encoding
          on the corresponding Windows ANSI (code page 1252) Unicode
          values in the Unicode encoding it reports to the system; (b)
          add Windows ANSI (CharSet 0) to the list of CharSets
          supported by the font; and (c) consider the value of the
          encoding ID to be a Windows CharSet value and add it to the
          list of CharSets supported by the font. Note: The
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must use Format 0 or 6 for
          its subtable, and the encoding must be identical to the
          CFF's encoding.</p><p role="">This <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> encoding is not required.
          It provides a compatibility mechanism for non-Unicode
          applications that use the font as if it were Windows ANSI
          encoded. Non-Windows ANSI Type 1 fonts, such as Cyrillic and
          Central European fonts, that Adobe shipped in the past had
          "0" (Windows ANSI) recorded in the CharSet field of the .PFM
          file; ATM for Windows 9x ignores the CharSet altogether.
          Adobe provides this compatibility <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          encoding in every OTF converted from a Type1 font in which
          the Encoding is not StandardEncoding.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="language_note"></a>Note on the language field in cmap
        subtables</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.3.1"></a>Specification</h3></div></div></div><p role="">This field must be set to zero for all
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtables whose platform IDs are
          other than Macintosh (platform ID 1). For
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtables whose platform IDs are
          Macintosh, set this field to the Macintosh language ID of
          the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable plus one, or to zero if
          the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable is not
          language-specific. For example, a Mac OS Turkish
          <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must set this field to 18,
          since the Macintosh language ID for Turkish is 17. A Mac OS
          Roman <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable must set this field
          to 0, since Mac OS Roman is not a language-specific
          encoding.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800137392"></a>Format 0: Byte encoding table</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.4.1"></a>Specification</h3></div></div></div><p role="">This is the Apple standard character to glyph index
          mapping table.</p><div class="table"><a name="idm80800135184"></a><p class="title"><strong>Table 5.4. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Format number is set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in this
              document.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">glyphIdArray[256]</td><td role="">An array that maps character codes to glyph
              index values.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is a simple 1 to 1 mapping of character codes to
          glyph indices. The glyph set is limited to 256. Note that if
          this format is used to index into a larger glyph set, only
          the first 256 glyphs will be accessible.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.4.2"></a>Annotation</h3></div></div></div><p role="">As the declaration stands, the length field seems
          superfluous, since the table appears to always be 262 bytes
          long. This can be explained in one of two ways:

          </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">the length field is included to make the first three
                words of all cmap subtables similar; it must always be
                262.</p></li><li role="" class="listitem"><p role="">the glyphIdArray does not need to be always 256
                elements long, it can be shorter.</p></li></ul></div><p role="">In the spirit of "generate conservatively, accept
          liberally", we recommend that font designers always put 256
          entries in glyphIdArray (and consequently set length to 262), and
          that font consumers be ready to handle fonts where the
          glyphIdArray contains length - 6 entries (but no more than
          256).</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800120960"></a>Format 2: High-byte mapping through table </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.5.1"></a>Specification</h3></div></div></div><p role="">This subtable is useful for the national character code
          standards used for Japanese, Chinese, and Korean characters.
          These code standards use a mixed 8/16-bit encoding, in which
          certain byte values signal the first byte of a 2-byte
          character (but these values are also legal as the second
          byte of a 2-byte character).</p><p role="">In addition, even for the 2-byte characters, the mapping
          of character codes to glyph index values depends heavily on
          the first byte. Consequently, the table begins with an array
          that maps the first byte to a 4-word subHeader. For 2-byte
          character codes, the subHeader is used to map the second
          byte's value through a subArray, as described below. When
          processing mixed 8/16-bit text, subHeader 0 is special: it
          is used for single-byte character codes. When subHeader zero
          is used, a second byte is not needed; the single byte value
          is mapped through the subArray.</p><div class="table"><a name="idm80800117376"></a><p class="title"><strong>Table 5.5. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Format number is set to 2.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">subHeaderKeys [256]</td><td role="">Array that maps high bytes to subHeaders:
              value is subHeader index * 8.</td><td class="auto-generated"> </td></tr><tr><td role="">4 words struct</td><td role="">subHeaders []</td><td role="">Variable-length array of subHeader
              structures.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphIndexArray []</td><td role="">Variable-length array containing subarrays
              used for mapping the low byte of 2-byte
              characters.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A subHeader is structured as follows:</p><div class="table"><a name="idm80800104576"></a><p class="title"><strong>Table 5.6. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">firstCode</td><td role="">First valid low byte for this
              subHeader.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">entryCount</td><td role="">Number of valid low bytes for this
              subHeader.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">idDelta</td><td role="">See text below.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">idRangeOffset</td><td role="">See text below.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The firstCode and entryCount values specify a subrange
          that begins at firstCode and has a length equal to the value
          of entryCount. This subrange stays within the 0-255 range of
          the byte being mapped. Bytes outside of this subrange are
          mapped to glyph index 0 (missing glyph). The offset of the
          byte within this subrange is then used as index into a
          corresponding subarray of glyphIndexArray. This subarray is
          also of length entryCount. The value of the idRangeOffset is
          the number of bytes past the actual location of the
          idRangeOffset word where the glyphIndexArray element
          corresponding to firstCode appears.</p><p role="">Finally, if the value obtained from the subarray is not
          0 (which indicates the missing glyph), you should add
          idDelta to it in order to get the glyphIndex. The value
          idDelta permits the same subarray to be used for several
          different subheaders. The idDelta arithmetic is modulo
          65536.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.5.2"></a>Annotation</h3></div></div></div><p role="">How about an intelligible description of the use of this
        format? Assuming that it intends to describe the same
        structure as the Apple True Type format, simply switching to
        their version would already be a vast improvement.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800092688"></a>Format 4: Segment mapping to delta values</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.6.1"></a>Specification</h3></div></div></div><p role="">This is the Microsoft standard character to glyph index
          mapping table for fonts that support Unicode ranges other
          than the range [U+D800 - U+DFFF] (defined as Surrogates
          Area, in Unicode v 3.0) which is used for UCS-4
          characters. If a font supports this character range (i.e. in
          turn supports the UCS-4 characters) a subtable in this
          format with a platform specific encoding ID 1 is yet needed,
          in addition to a subtable in format 12 with a platform
          specific encoding ID 10. Please see details on format 12
          below, for fonts that support UCS-4 characters on
          Windows.</p><p role="">This format is used when the character codes for the
          characters represented by a font fall into several
          contiguous ranges, possibly with holes in some or all of the
          ranges (that is, some of the codes in a range may not have a
          representation in the font). The format-dependent data is
          divided into three parts, which must occur in the following
          order:</p><div role="" class="orderedlist"><ol class="orderedlist" type="1"><li role="" class="listitem"><p role="">A four-word header gives parameters for an optimized
              search of the segment list;</p></li><li role="" class="listitem"><p role="">Four parallel arrays describe the segments (one
              segment for each contiguous range of codes);</p></li><li role="" class="listitem"><p role="">A variable-length array of glyph IDs (unsigned
              words).</p></li></ol></div><div class="table"><a name="idm80800086064"></a><p class="title"><strong>Table 5.7. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Format number is set to 4.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">segCountX2</td><td role="">2 x segCount.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">searchRange</td><td role="">2 x (2**floor(log2(segCount)))</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">entrySelector</td><td role="">log2(searchRange/2)</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">rangeShift</td><td role="">2 x segCount - searchRange</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">endCount [segCount]</td><td role="">End characterCode for each segment,
              last=0xFFFF.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">reservedPad</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">startCount [segCount]</td><td role="">Start character code for each
              segment.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">idDelta [segCount]</td><td role="">Delta for all character codes in
              segment.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">idRangeOffset [segCount]</td><td role="">Offsets into glyphIdArray or 0</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphIdArray []</td><td role="">Glyph index array (arbitrary length)
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The number of segments is specified by segCount, which
          is not explicitly in the header; however, all of the header
          parameters are derived from it. The searchRange value is
          twice the largest power of 2 that is less than or equal to
          segCount. For example, if segCount=39, we have the
          following:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="10pc"/><col width="10pc"/><col width="10pc"/></colgroup><tbody><tr><td role="">segCountX2</td><td role="">78</td><td role=""> </td></tr><tr><td role="">searchRange</td><td role="">64</td><td role="">(2 * largest power of 2 &lt;=39)</td></tr><tr><td role="">entrySelector</td><td role="">5</td><td role="">log2 (32)</td></tr><tr><td role="">rangeShift</td><td role="">14</td><td role="">2 x 39 - 64</td></tr></tbody></table></div><p role="">Each segment is described by a startCode and endCode,
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
          must be present.</p><p role="">If the idRangeOffset value for the segment is not 0, the
          mapping of character codes relies on glyphIdArray. The
          character code offset from startCode is added to the
          idRangeOffset value. This sum is used as an offset from the
          current location within idRangeOffset itself to index out
          the correct glyphIdArray value. This obscure indexing trick
          works because glyphIdArray immediately follows idRangeOffset
          in the font file. The C expression that yields the glyph
          index is:</p><div role="" class="literallayout"><p><br/>
  *(idRangeOffset[i]/2<br/>
    + (c - startCount[i])<br/>
    + &amp;idRangeOffset[i])<br/>
    </p></div><p role="">The value c is the character code in question, and i is
          the segment index in which c appears. If the value obtained
          from the indexing operation is not 0 (which indicates
          missingGlyph), idDelta[i] is added to it to get the glyph
          index. The idDelta arithmetic is modulo 65536.</p><p role="">If the idRangeOffset is 0, the idDelta value is added
          directly to the character code offset (i.e. idDelta[i] + c)
          to get the corresponding glyph index. Again, the idDelta
          arithmetic is modulo 65536.</p><p role="">As an example, the variant part of the table to map
          characters 10-20, 30-90, and 153-480 onto a contiguous range
          of glyph indices may look like this:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="10pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/><col width="5pc"/></colgroup><tbody><tr><td role="">segCountX2:</td><td role="">8</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">searchRange:</td><td role="">8</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">entrySelector:</td><td role="">4</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">rangeShift:</td><td role="">0</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">endCode:</td><td role="">20</td><td role="">90</td><td role="">480</td><td role="">0Xffff</td></tr><tr><td role="">reservedPad:</td><td role="">0</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">startCode:</td><td role="">10</td><td role="">30</td><td role="">153</td><td role="">0Xffff</td></tr><tr><td role="">idDelta:</td><td role="">-9</td><td role="">-18</td><td role="">-27</td><td role="">1</td></tr><tr><td role="">idRangeOffset:</td><td role="">0</td><td role="">0</td><td role="">0</td><td role="">0</td></tr></tbody></table></div><p role="">This table performs the following mappings:</p><div role="" class="literallayout"><p><br/>
10 -&gt; 10 - 9 = 1<br/>
20 -&gt; 20 - 9 = 11<br/>
30 -&gt; 30 - 18 = 12<br/>
90 -&gt; 90 - 18 = 72<br/>
...and so on.<br/>
</p></div><p role="">Note that the delta values could be reworked so as to
          reorder the segments.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.6.2"></a>Annotation</h3></div></div></div><p role="">The first sentence should probably be changed to
        "... for fonts that support Unicode BMP characters".</p><p role="">In the table that describes the fields, it seems that
          the fields startCount and endCount should instead be
          startCode and endCode. These are better names, and are the
          names used in the text.</p><p role="">In the example, the idDelta of the third range should
          probably be -80, so that the character code 153 is mapped to
          the glyphID 153-80 = 73.</p><p role="">The meaning of the last sentence escapes me. May be it
        should be removed?</p><p role="">It seems a necessary property of this format that the
          segments be disjoint, yet it is not mentionned
          explicitly.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800021408"></a>Format 6: Trimmed table mapping </h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.7.1"></a>Specification</h3></div></div></div><div class="table"><a name="idm80800019616"></a><p class="title"><strong>Table 5.8. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Format number is set to 6.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">This is the length in bytes of the
              subtable.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">firstCode</td><td role="">First character code of
              subrange.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">entryCount</td><td role="">Number of character codes in
              subrange.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphIdArray [entryCount]</td><td role="">Array of glyph index values for character
              codes in the range. </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The firstCode and entryCount values specify a subrange
          (beginning at firstCode, length = entryCount) within the
          range of possible character codes. Codes outside of this
          subrange are mapped to glyph index 0. The offset of the code
          (from the first code) within this subrange is used as index
          to the glyphIdArray, which provides the glyph index
          value.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.7.2"></a>Annotation</h3></div></div></div><p role="">It is unclear whether the entryCount can be 0. We assume
          it can and recommend to add a sentence to that
          effect.</p><p role="">This format is very similar to format 0, in that there
          is an explicit list of glyph indices for a contiguous range
          of character code. However, there are two intersting
          properties: the range can be bigger than 256; and more
          importantly, the glyph indices are USHORT instead of
          BYTE. So this format can be used for byte encodings to reach
          glyphs other than the first 256 glyphs.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80800003728"></a>Supporting 4-byte character codes</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.8.1"></a>Specification</h3></div></div></div><p role="">While the four existing <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable formats which
          currently exist have served us well, the introduction of the
          Surrogates Area in Unicode 2.0 has stressed them past the
          point of utility. This section specifies three formats,
          format 8, 10 and 12; which directly support 4-byte character
          codes. A major change introduced with these three formats is
          a more pure 32-bit orientation. The <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table version
          number will continue to be 0x0000, for those fonts that make
          use of these formats.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.8.2"></a>Annotation</h3></div></div></div><p role="">A better formulation in the first sentence could be
        "... the introduction of supplemental characters in Unicode
        2.0..."</p><p role="">The semicolon after "12" should be changed to a
        comma.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799997072"></a>Format 8: mixed 16-bit and 32-bit coverage</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.9.1"></a>Specification</h3></div></div></div><p role="">Format 8 is a bit like format 2, in that it provides for
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
          with no further information required.</p><p role="">Here's the format 8 subtable format:</p><div class="table"><a name="idm80799993520"></a><p class="title"><strong>Table 5.9. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Subtable format; set to 8.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">reserved</td><td role="">Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">length</td><td role="">Byte length of this subtable (including the
              header)</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">is32 [8192]</td><td role="">Tightly packed array of bits (8K bytes total)
              indicating whether the particular 16-bit (index) value
              is the start of a 32-bit character code
                </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role=""> nGroups</td><td role=""> Number of groupings which follow
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Here follow the individual groups. Each group has the
          following format:</p><div class="table"><a name="idm80799980976"></a><p class="title"><strong>Table 5.10. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role=""> startCharCode</td><td role=""> First character code in this group; note
              that if this group is for one or more 16-bit character
              codes (which is determined from the is32 array), this
              32-bit value will have the high 16-bits set to zero
            </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role=""> endCharCode</td><td role=""> Last character code in this group; same
              condition as listed above for the startCharCode
                </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role=""> startGlyphID</td><td role=""> Glyph index corresponding to the starting
              character code </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">A few notes here. The endCharCode is used, rather than a
          count, because comparisons for group matching are usually
          done on an existing character code, and having the
          endCharCode be there explicitly saves the necessity of an
          addition per group. Groups must be sorted by increasing
          startCharCode. A group's endCharCode must be less than the
          startCharCode of the following group, if any.</p><p role="">To determine if a particular word (cp) is the first half
          of 32-bit code points, one can use an expression such as (
          is32[ cp / 8 ] &amp; ( 1 &lt;&lt; ( 7 - ( cp % 8 ) ) ) ). If this is
          non-zero, then the word is the first half of a 32-bit code
          point.</p><p role="">0 is not a special value for the high word of a 32-bit
          code point. A font may not have both a glyph for the code
          point 0x0000 and glyphs for code points with a high word of
          0x0000.</p><p role="">The presence of the packed array of bits indicating
          whether a particular 16-bit value is the start of a 32-bit
          character code is useful even when the font contains no
          glyphs for a particular 16-bit start value. This is because
          the system software often needs to know how many bytes ahead
          the next character begins, even if the current character
          maps to the missing glyph. By including this information
          explicitly in this table, no "secret" knowledge needs to be
          encoded into the OS.</p><p role="">Although this format might work advantageously on some
          platforms for non-Unicode encodings, Microsoft does not
          support it for Unicode encoded UCS-4 characters.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.9.2"></a>Annotation</h3></div></div></div><p role="">First paragraph, second sentence, should be: "If a font
          maps Unicode supplemental characters, it's likely to map
          Unicode BMP characters as well."</p><p role="">For coherence with the other formats, the description of
          the format field should be "Format number is set to 8" and
          the description of the length field should be "This is the
          length in bytes of the subtable."</p><p role="">This format is dubious and would probably best be
          deprecated. If For Unicode encodings, it is useful only for
          UTF-16 (the only version that has 16 bit code units), so
          spending 8K bytes to is

If the intent is really for a Unicode encodings,
          then it is known </p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799967008"></a>Format 10: Trimmed array</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.10.1"></a>Specification</h3></div></div></div><p role="">Format 10 is a bit like format 6, in that it defines a
        trimmed array for a tight range of 32-bit character
        codes:</p><div class="table"><a name="idm80799964736"></a><p class="title"><strong>Table 5.11. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Subtable format; set to 10.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">reserved</td><td role="">Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">length</td><td role="">Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role=""> startCharCode</td><td role=""> First character code covered </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role=""> numChars</td><td role=""> Number of character codes covered
            </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role=""> glyphs []</td><td role=""> Array of glyph indices for the character
              codes covered </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This format is not supported by Microsoft.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.10.2"></a>Annotation</h3></div></div></div><p role="">For coherence with the other formats, the description of
        the format field should be "Format number is set to 10" and the
        description of the length field should be "This is the length
        in bytes of the subtable."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799948400"></a>Format 12: Segmented coverage</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.11.1"></a>Specification</h3></div></div></div><p role="">This is the Microsoft standard character to glyph index
          mapping table for fonts supporting the UCS-4 characters in
          the Unicode Surrogates Area (U+D800 - U+DFFF). It is a bit
          like format 4, in that it defines segments for sparse
          representation in 4-byte character space. Here's the
          subtable format:</p><div class="table"><a name="idm80799945840"></a><p class="title"><strong>Table 5.12. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Subtable format; set to 12.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">reserved</td><td role="">Reserved; set to 0</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">length</td><td role="">Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">language</td><td role="">Please see <a role="" class="link" href="chapter.cmap.html#language_note" title="Note on the language field in cmap subtables">Note
                on the language field in cmap subtables</a> in
              this document.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">nGroups</td><td role="">Number of groupings which follow
            </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Fonts providing Unicode encoded UCS-4 character support
          for Windows 2000 and later, need to have a subtable with
          platform ID 3, platform specific encoding ID 1 in format 4;
          and in addition, need to have a subtable for platform ID 3,
          platform specific encoding ID 10 in format 12. Please note,
          that the content of format 12 subtable, needs to be a super
          set of the content in the format 4 subtable. The format 4
          subtable needs to be in the cmap table to enable backward
          compatibility needs.</p><p role="">Here follow the individual groups, each of which has the
          following format:</p><div class="table"><a name="idm80799934048"></a><p class="title"><strong>Table 5.13. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">startCharCode</td><td role="">First character code in this group
            </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">endCharCode</td><td role="">Last character code in this group
            </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">startGlyphID</td><td role="">Glyph index corresponding to the starting
              character code </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Groups must be sorted by increasing startCharCode. A
          group's endCharCode must be less than the startCharCode of
          the following group, if any. The endCharCode is used, rather
          than a count, because comparisons for group matching are
          usually done on an existing character code, and having the
          endCharCode be there explicitly saves the necessity of an
          addition per group.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.11.2"></a>Annotation</h3></div></div></div><p role="">First paragraph, first sentence should be reworded: "...
          for fonts supporting Unicode supplemental characters."
          Similarly, second paragraph, first sentence should be
          reworded: "Fonts providing support for Unicode supplemental
          characters..."</p><p role="">For coherence with the other formats, the description of
          the format field should be "Format number is set to 12" and
          the description of the length field should be "This is the
          length in bytes of the subtable."</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799923680"></a>Format 14: Unicode Variation Sequences</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.5.12.1"></a>Specification</h3></div></div></div><p role="">Subtable format 14 specifies the Unicode Variation
        Sequences (UVSes) supported by the font. A Variation Sequence,
        according to the Unicode Standard, comprises a base character
        followed by a variation selector; e.g. &lt;U+82A6,
        U+E0101&gt;.</p><p role="">The subtable partitions the UVSes supported by the font
        into two categories: “default” and
        “non-default” UVSes. Given a UVS, if the glyph
        obtained by looking up the base character of that sequence in
        the Unicode cmap subtable (i.e. the UCS-4 or the BMP cmap
        subtable) is the glyph to use for that sequence, then the
        sequence is a “default” UVS; otherwise it is a
        “non-defaultJ=f UVS, and the glyph to use for that
        sequence is specified in the format 14 subtable itself.</p><p role="">The example below shows how a font vendor can use format
        14 for a JIS-2004-aware font.</p><div class="table"><a name="idm80799919312"></a><p class="title"><strong>Table 5.14. Format 14 header</strong></p><div class="table-contents"><table role="" class="table" summary="Format 14 header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Subtable format; set to 14.</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">length</td><td role="">Byte length of this subtable (including the
              header) </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">numVarSelectorRecords</td><td role="">Number of Variation Selector Records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is immediately followed by 'numVarSelectorRecords'
        Variation Selector Records.</p><div class="table"><a name="idm80799912000"></a><p class="title"><strong>Table 5.15. Variation Selector Record</strong></p><div class="table-contents"><table role="" class="table" summary="Variation Selector Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">UINT24</td><td role="">varSelector</td><td role="">Variation selector</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">defaultUVSOffset</td><td role="">Offset to Default UVS Table. May be 0. </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">nonDefaultUVSOffset</td><td role="">Offset to Non-Default UVS Table. May be 0.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The Variation Selector Records are sorted in increasing
        order of 'varSelector'. No two records may have the same
        'varSelector'. All offsets in a record are relative to the
        beginning of the format 14 cmap subtable.</p><p role="">A Variation Selector Record and the data its offsets
        point to specify those UVSes supported by the font for which
        the variation selector is the 'varSelector' value of the
        record. The base characters of the UVSes are stored in the
        tables pointed to by the offsets. The UVSes are partitioned by
        whether they are default or non-default UVSes.</p><p role="">Glyph IDs to be used for non-default UVSes are specified
        in the Non-Default UVS table.</p><p role="">Default UVS Table</p><p role="">A Default UVS Table is simply a range-compressed list of
        Unicode scalar values, representing the base characters of the
        default UVSes which use the 'varSelector' of the associated
        Variation Selector Record.</p><div class="table"><a name="idm80799902272"></a><p class="title"><strong>Table 5.16. Default UVS Table header</strong></p><div class="table-contents"><table role="" class="table" summary="Default UVS Table header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">numUnicodeValueRanges</td><td role="">Number of ranges that follow</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is immediately followed by 'numUnicodeValueRanges'
        Unicode Value Ranges, each of which represents a contiguous
        range of Unicode values.</p><div class="table"><a name="idm80799897904"></a><p class="title"><strong>Table 5.17. Unicode Value Range</strong></p><div class="table-contents"><table role="" class="table" summary="Unicode Value Range" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">UINT24</td><td role="">startUnicodeValue</td><td role="">First value in this range</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">additionalCount</td><td role="">Number of <span role="" class="emphasis"><em>additional</em></span>
            values in this range</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">For example, the range U+4E4D...U+4E4F (3 values) will
        set 'startUnicodeValue' to 0x004E4D and 'additionalCount' to
        2. A singleton range will set 'additionalCount' to 0.</p><p role="">('startUnicodeValue' + 'additionalCount') must not
        exceed 0xFFFFFF.</p><p role="">The Unicode Value Ranges are sorted in increasing order
        of 'startUnicodeValue'. The ranges must not overlap; i.e.,
        ('startUnicodeValue' + 'additionalCount') must be less than
        the 'startUnicodeValue' of the following range (if
        any).</p><p role="">Non-Default UVS Table</p><p role="">A Non-Default UVS Table is a list of pairs of Unicode
        scalar values and glyph IDs. The Unicode values represent the
        base characters of all non-default UVSes which use the
        'varSelector' of the associated Variation Selector Record, and
        the glyph IDs specify the glyph IDs to use for the
        UVSes.</p><div class="table"><a name="idm80799889344"></a><p class="title"><strong>Table 5.18. Non-Default UVS Table header</strong></p><div class="table-contents"><table role="" class="table" summary="Non-Default UVS Table header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">ULONG</td><td role="">numUVSMappings</td><td role="">Number of UVS Mappings that follow</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This is immediately followed by 'numUVSMappings' UVS
        Mappings.</p><div class="table"><a name="idm80799885056"></a><p class="title"><strong>Table 5.19. UVS Mapping</strong></p><div class="table-contents"><table role="" class="table" summary="UVS Mapping" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">UINT24</td><td role="">unicodeValue</td><td role="">Base Unicode value of the UVS</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">glyphID</td><td role="">Glyph ID of the UVS</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">The UVS Mappings are sorted in increasing order of
        'unicodeValue'. No two mappings in this table may have the
        same 'unicodeValue' values.</p><p role="">Example</p><p role="">Here is an example of how a format 14 cmap subtable may
        be used in a font that is aware of JIS-2004 variant
        glyphs. The CIDs (character IDs) in this example refer to
        those in the Adobe Character Collection 'Adobe-Japan1', and
        may be assumed to be identical to the glyph IDs in the font in
        our example.</p><p role="">JIS-2004 changed the default glyph variants for some of
        its code points. For example:</p><p role="">JIS-90: U+82A6 -&gt; CID 1142</p><p role="">JIS-2004: U+82A6 -&gt; CID 7961</p><p role="">Both of these glyph variants are supported through the
        use of UVSes, as the following examples from Unicode's UVS
        registry show:</p><p role="">U+82A6 U+E0100 -&gt; CID 1142</p><p role="">U+82A6 U+E0101 -&gt; CID 7961</p><p role="">If the font wants to support the JIS-2004 variants by
        default, it will:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">encode glyph ID 7961 at U+82A6 in the Unicode cmap
            subtable,</p></li><li role="" class="listitem"><p role="">specify &lt;U+82A6, U+E0101&gt; in the UVS cmap
            subtable's Default UVS Table ('varSelector' will be
            0x0E0101 and 'defaultUVSOffset' will point to data
            containing a 0x0082A6 Unicode value)</p></li><li role="" class="listitem"><p role="">specify &lt;U+82A6, U+E0100&gt; -&gt; glyph ID 1142 in the
            UVS cmap subtable's Non-Default UVS Table ('varSelector'
            will be 0x0E0100 and 'nonDefaultBaseUVOffset' will point
            to data containing a 'unicodeValue' 0x82A6 and 'glyphID'
            1142). </p></li></ul></div><p role="">If, however, the font wants to support the JIS-90
        variants by default, it will:</p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">encode glyph ID 1142 at U+82A6 in the Unicode cmap
            subtable,</p><p role="">specify &lt;U+82A6, U+E0100&gt; in the
            UVS cmap subtable's Default UVS Table</p></li><li role="" class="listitem"><p role="">specify &lt;U+82A6, U+E0101&gt; -&gt; glyph ID 7961 in the
            UVS cmap subtables Non-Default UVS Table </p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799866976"></a>Various test fonts</h2></div></div></div></div></div>