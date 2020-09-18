<h3 id="map-chars-process" rel="off-new-10.1"><dfn>Mapping characters to glyphs</dfn></h3>

When a text is being shaped by a font consumer, the font consumer uses the data in the cmap table to map codepoints in the input character repertoire to glyph IDs in the font.

XXX which subtable to use

* When a Unicode character is followed by a variation selector character (i.e. a character in the range `U+FE00..U+FE0F`), the font consumer should check if the cmap table contains a format 14 subtable. If so, this should be processed first, as below.

* Character codes that are not mapped to any glyph in the font by the data in the cmap table (either because there is no subtable for their encoding or because the subtable in a format not supported by the application or because the subtable does not contain a mapping for this character code) should be mapped to glyph ID 0.

<h4 id="processing-a-format-0-subtable">Processing a format 0 subtable</h4>

Font consumers must read the {{length}} field of the subtable, and read either <code>(length - 6)</code> glyph IDs or 256, whichever is fewer.

To map codepoints to glyph IDs in a format 0 subtable, each input
          codepoint is used to index the {{glyphIdArray}} to retrieve a glyph ID.
          Before indexing the array, the font consumer must ensure that the input
          codepoint is less than the number of entries in the {{glyphIdArray}};
          if it is not less, then the character is mapped to glyph index 0.


<h4 id="processing-a-format-2-subtable">Processing a format 2 subtable</h4>

* To map codepoints to glyph IDs in a format 2 subtable, the font consumer should consume the input character stream one byte at a time, and perform the following sequence of operations.
* First, the input byte is used to index the subHeaderKeys array to obtain a <emphasis>subheader key</emphasis>.
* Where the subheader key is 0, this indicates that the input byte is the only byte in this codepoint. The input byte is then directly looked up in the {{glyphIndexArray}} to obtain the glyph ID.
* Where the subheader key is greater than 0, this indicates a two-byte character. First, the subheader key should be divided by 8, and the font consumer should then use this to index into the subheader array to obtain the appropriate subheader.
* Next, the font consumer should consume another input byte, the <emphasis>low byte</emphasis>, and ensure that the value of the low byte is within the range of this subheader - that is, that the low byte is more than or equal to `firstCode` and less than `firstCode+entryCount`. If the low byte is not within the range of the subheader, glyph ID 0 is returned.
* `firstCode` is then subtracted from the low byte to determine the <emphasis>index offset</emphasis>. The font consumer will then advance {{CmapFormat4Subtable/idRangeOffset}} bytes from the position of the {{CmapFormat4Subtable/idRangeOffset}} element in the subheader to find the beginning of the glyph mapping subrange, and then also advance by the index offset to determine the glyph ID.
* Finally, if the glyph ID is non-zero, {{CmapFormat4Subtable/idDelta}} is added to the glyph ID module 65536 to return the final glyph ID.

<h4 id="processing-a-format-4-subtable">Processing a format 4 subtable</h4>

When reading a format 4 subtable, the values {{searchRange}}, {{entrySelector}} and {{rangeShift}} should be ignored.

To map codepoints to glyph IDs in a format 4 subtable, the font
consumer should first search the segment arrays for the first {{endCode}}
that is greater than or equal to the codepoint to be mapped. If the
corresponding {{startCode}} is less than or equal to the character code,
then the segment contains a mapping for this codepoint. Otherwise,
the missing glyph ID 0 is returned.

XXX this para and next still needs rewriting.
If the {{idRangeOffset}} value for the segment is not 0, the
mapping of character codes relies on {{glyphIdArray}}. The
character code offset from {{startCode}} is added to the
{{idRangeOffset}} value. This sum is used as an offset from the
current location within {{idRangeOffset}} itself to index out
the correct {{glyphIdArray}} value. This obscure indexing trick
works because {{glyphIdArray}} immediately follows {{idRangeOffset}}
in the font file. The C expression that yields the glyph
index is:

<pre>
*(idRangeOffset[i]/2
+ (c - startCode[i])
+ &amp;idRangeOffset[i])
</pre>

The value `c` is the character code in question, and `i` is
the segment index in which `c` appears. If the value obtained
from the indexing operation is not 0 (which indicates
missingGlyph), `idDelta[i]` is added to it to get the glyph
index. The {{CmapFormat4Subtable/idDelta}} arithmetic is modulo 65536.

If the {{CmapFormat4Subtable/idRangeOffset}} is 0, the idDelta value is added
directly to the codepoint modulo 65536 (i.e. `(idDelta[i] + c)%65536`)
and the value is returned as the glyph ID.

<div class="example">
As an example of the mapping process, a subtable which maps codepoints
10-20, 30-90, and 153-480 onto a contiguous range of glyph indices may
look like this:

<pre>
  segCountX2:      8
  searchRange:     8
  entrySelector:   4
  rangeShift:      0
  endCode:         20   90    480   0Xffff
  reservedPad:     0
  startCode:       10   30    153   0Xffff
  idDelta:         -9   -18   -80   1
  idRangeOffset:   0    0     0     0
</pre>

This table performs the following mappings:

      10 -> 10 - 9 = 1
      20 -> 20 - 9 = 11
      30 -> 30 - 18 = 12
      90 -> 90 - 18 = 72
      153 -> 153 - 80 = 73
      ...and so on.
</div>

<h4 id="processing-a-format-6-subtable">Processing a format 6 subtable</h4>

To map codepoints to glyph IDs in a format 6 subtable, each input
codepoint is subtracted from {{firstCode}}, and this value is used to index the {{glyphIdArray}} to retrieve a glyph ID.

Before indexing the array, the font consumer must ensure that the input codepoint is less than the {{entryCount}}; if it is not less, then the character is mapped to glyph index 0.

<h4 id="processing-a-format-10-subtable">Processing a format 10 subtable</h4>

To map codepoints to glyph IDs in a format 10 subtable, each input
codepoint is subtracted from {{startCharCode}}, and this value is used to index the {{glyphs}} to retrieve a glyph ID.

Before indexing the array, the font consumer must ensure that the input codepoint is less than the {{numChars}}; if it is not less, then the character is mapped to glyph index 0.

<h4 id="processing-a-format-12-subtable">Processing a format 12 subtable</h4>

To map codepoints to glyph IDs in a format 12 subtable, the font
consumer should first search the groups for the first {{endCharCode}}
that is greater than or equal to the codepoint to be mapped. If the
corresponding {{startCharCode}} is less than or equal to the character code,
then the segment contains a mapping for this codepoint. Otherwise,
the missing glyph ID 0 is returned.

Next the value of {{startCharCode}} is subtracted from the codepoint, and
the result is added to {{startGlyphID}} to retrieve a glyph ID.

<h4 id="processing-a-format-13-subtable">Processing a format 13 subtable</h4>

To map codepoints to glyph IDs in a format 12 subtable, the font
consumer should first search the groups for the first {{endCharCode}}
that is greater than or equal to the codepoint to be mapped. If the
corresponding {{startCharCode}} is less than or equal to the character code,
then the segment contains a mapping for this codepoint. Otherwise,
the missing glyph ID 0 is returned. Once a matching group is found, the value of {{glyphID}} is returned.

<h4 id="processing-a-format-14-subtable">Processing a format 14 subtable</h4>

To map codepoints to glyph IDs in a format 14 subtable, both the base codepoint and the codepoint of the Unicode Variation Selector need to be considered together.

First, the font consumer should search for a {{VariationSelector}} record with a {{varSelector}} equal to the codepoint of the Unicode Variation Selector. If no record is found, format 14 table processing ends and the codepoint is mapped using the next available subtable.

If a record is found, the font consumer should search for a {{UVSMapping}} entry where the {{unicodeValue}} matches the codepoint to be mapped. If one is present, the {{glyphId}} from the mapping should be returned. If not, the codepoint should be mapped using the next available subtable.

The {{DefaultUVS}} tables can be ignored.

<h4 id="cmap-processing-general">General notes</h4>

If a platform ID 4 (custom), encoding ID 0-255 (OTF Windows NT
compatibility mapping) cmap encoding is present in an CommonType font
with CFF outlines, then the OTF font driver in Windows NT will: (a)
superimpose the glyphs encoded at character codes 0-255 in the encoding
on the corresponding Windows ANSI (code page 1252) Unicode values in the
Unicode encoding it reports to the system; (b) add Windows ANSI (CharSet
0) to the list of CharSets supported by the font; and (c) consider the
value of the encoding ID to be a Windows CharSet value and add it to the
list of CharSets supported by the font.

This cmap encoding provides a compatibility mechanism for non-Unicode
applications that use the font as if it were Windows ANSI encoded.
