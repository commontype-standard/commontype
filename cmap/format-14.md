<h5 id="format-14-cmap-subtable">Format 14 cmap subtable</h5>

<table>
    <tr><th>Introduced</th> <td> 1.6 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This subtable format is intended for Unicode Variation Sequences, which consist of a base glyph followed by a variation selector. This subtable
determines how variation selectors are to be processed.

<pre class="idl">
interface CmapFormat14Subtable {
    attribute USHORT format;
    attribute ULONG numVarSelectorRecords;
    attribute VariationSelector[] varSelectorRecord;
};

interface VariationSelector {
		attribute uint24 varSelector;
		attribute Offset32 defaultUVSOffset;
		attribute Offset32 nonDefaultUVSOffset;
};
</pre>

<dl dfn-type=attribute dfn-for=VariationSelector>
  <dt><dfn>varSelector</dfn></dt>
  <dd>A 24-bit integer denoting the Unicode codepoint of the variation selector.</dd>
  <dt><dfn>defaultUVSOffset</dfn></dt>
  <dd>Offset (from start of subtable) to the {{DefaultUVS}} table for this variation selector.</dd>
  <dt><dfn>nonDefaultUVSOffset</dfn></dt>
  <dd>Offset (from start of subtable) to the {{NonDefaultUVS}} table for this variation selector.</dd>
</dl>

<div class="note">
	Note that due to the presence of the 24-bit {{varSelector}} field, this subtable does not align on four-byte boundaries.
</div>

A `DefaultUVS` table has the following format:

<pre class="idl">
interface DefaultUVS {
		attribute ULONG numUnicodeValueRanges;
		attribute UnicodeRange[] ranges;
};

interface UnicodeRange {
		attribute uint24 startUnicodeValue;
		attribute byte additionalCount;
};
</pre>

<dl dfn-type=attribute dfn-for=UnicodeRange>
  <dt><dfn>startUnicodeValue</dfn></dt>
  <dd>A 24-bit integer denoting the Unicode codepoint of the first codepoint covered by this segment.</dd>
  <dt><dfn>additionalCount</dfn></dt>
  <dd>Number of codepoints in this segment minus one.</dd>
</dl>

A `NonDefaultUVS` table has the following format:

<pre class="idl">
interface NonDefaultUVS {
		attribute ULONG numUVSMappings;
		attribute UVSMapping[] uvsMappings;
};
interface UVSMapping {
        attribute uint24 unicodeValue;
        attribute USHORT glyphId;
};
</pre>

<h6 id="cmap14-in">Implementation notes for font producers</h6>

* `startUnicodeValue + additionalCount` must not exceed `0xFFFFFF`.
* {{UnicodeRange}} fields must appear in ascending order of {{startUnicodeValue}}.
* The segments must not overlap.
* {{UVSMapping}} fields must appear in ascending order of {{unicodeValue}}.

<div class="example">
The font Kozuka Gothic Pro encodes two variations of the Unicode codepoint `0x4e0e` (与); the default has the central horizontal stroke running through the character (glyph id 3881), and the alternate has it floating to the left (glyph id 20073). The alternate is selected with the Unicode Variation Selector `0x0e0101`. With no UVS, or with the VS `0x0e0100`, the default glyph ID should be returned. There are no other glyphs with variations for codepoints continguous with `0x4e0e`.

First, to deal with the default case, there will be a {{VariationSelector}} record with {{varSelector}} `0x0e0100`. Amongst the {{ranges}} of the {{DefaultUVS}} table for this {{VariationSelector}} record will be a {{UnicodeRange}} as follows:

<table>
    <tr><th>startUnicodeValue</th><td>0x4e0e</td></tr>
    <tr><th>additionalCount</th><td>0</td></tr>
</table>

To deal with the variation, there will be a {{VariationSelector}} record with {{varSelector}} `0x0e0101`. Amongst the {{uvsMappings}} of the {{NonDefaultUVS}} table for this {{VariationSelector}} record will be a {{UVSMapping}} as follows:

<table>
    <tr><th>unicodeValue</th><td>0x4e0e</td></tr>
    <tr><th>glyphId</th><td>20073</td></tr>
</table>
</div>
