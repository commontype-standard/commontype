<h4>Format 4 cmap subtable</h4>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This format is used to map Unicode characters in the Basic Multilingual Plane. It is used when the codepoints to be mapped can be divided into several contiguous ranges or "segments". The segments may include codepoints which are not mapped to glyphs.

<pre class="idl">
interface CmapFormat4Subtable {
    attribute USHORT format;
    attribute USHORT length;
    attribute USHORT language;
    attribute USHORT segCountX2;
    attribute USHORT searchRange;
    attribute USHORT entrySelector;
    attribute USHORT rangeShift;
    attribute USHORT[] endCode;
    attribute USHORT reservedPad;
    attribute USHORT[] startCode;
    attribute SHORT[] idDelta;
    attribute USHORT idRangeOffset;
    attribute USHORT[] glyphIdArray;
};
</pre>

<dl dfn-type=attribute dfn-for=CmapFormat4Subtable>
  <dt><dfn>segCountX2</dfn></dt>
  <dd>The number of segments multiplied by two.</dd>
  <dt><dfn>searchRange</dfn></dt>
  <dd>Intended for optimization, this value is defined as `2 x (2**floor(log2(segCount)))`, but see note below.
  <dt><dfn>entrySelector</dfn></dt>
  <dd>Intended for optimization, this value is defined as `log2(searchRange/2)`, but see note below.
  <dt><dfn>rangeShift</dfn></dt>
  <dd>Intended for optimization, this value is defined as `2 x segCount - searchRange`, but see note below.
  <dt><dfn>endCode</dfn></dt>
  <dd>An array of `segCount` codepoints representing the final codepoint in each segment.
  <dt><dfn>startCode</dfn></dt>
  <dd>An array of `segCount` codepoints representing the initial codepoint in each segment.
  <dt><dfn>idDelta</dfn></dt>
  <dd>An array of `segCount` 16-bit values representing the delta to be added to each codepoint in the segment.
  <dt><dfn>idRangeOffset</dfn></dt>
  <dd>An array of `segCount` unsigned 16-bit values representing the offset into the {{glyphIdArray}} for this segment.

<div class="note">
Note that unlike most offset values in the file format, the {{idRangeOffset}} counts the number of bytes from *the byte position of the* {{idRangeOffset}} *record itself* to the target element, rather than from the start of the subtable header.
</div>

  </dd>
</dl>

<div class="note">
    It is a security vulnerability for font consumers to trust the values of {{searchRange}}, {{entrySelector}} and {{rangeShift}}, instead of computing them afresh from the {{segCountX2}} value. Their use is therefore *discouraged* by CommonType.
</div>

<h5>Implementation notes for font producers</h5>

The final segment must have an endCode value of `0xFFFF`.
This segment need not contain any valid mappings, but must be present.

<div class="example">
Here is an example of filling in the header information for a table with
39 segments according to the formal definition:

<table>
  <tr><th>segCountX2</th><td>78</td></tr>
  <tr><th>searchRange</th><td>64</td><td>(2 * largest power of 2 <=39)</td></tr>
  <tr><th>entrySelector</th><td>5</td><td>log2 (32)</td></tr>
  <tr><th>rangeShift</th><td>14</td><td>2 x 39 - 64</td></tr>
</table>

That said, the {{searchRange}}, {{entrySelector}} and {{rangeShift}} fields are
ignored by all current implementations, and should be treated as unused.
</div>

<div class="note">
Uniscribe will fail if the final segment does not have an {{endCode}} of
0xFFFF, but other implementations will succeed.
</div>

