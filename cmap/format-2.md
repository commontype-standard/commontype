<h4>Format 2 cmap subtable</h4>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This subtable is designed to faciliate mapping characters to glyphs within the encoding mechanisms which use a mixed 8/16-bit encoding, such as the legacy national character code standards used for Japanese, Chinese, and Korean characters.

In a mixed encoding, codepoints may be represented either by a one byte integer or a two byte integer, with certain values of the initial byte acting as a continuation signal.

<pre class="idl">
interface CmapFormat2Subtable {
  attribute USHORT format;
  attribute USHORT length;
  attribute USHORT language;
  attribute USHORT[] subHeaderKeys;
  attribute CmapFormat2Subheader[] subheaders;
  attribute USHORT[] glyphIndexArray;
};
</pre>

<dl dfn-type=attribute dfn-for=CmapFormat2Subtable>
  <dt><dfn>format</dfn></dt>
  <dd>Set to 2.</dd>
  <dt><dfn>subHeaderKeys</dfn></dt>
  <dd>An 256-element array mapping high bytes to {{CmapFormat2Subheader}} structures.</dd>
</dl>

<pre class="idl">
interface CmapFormat2Subheader {
	attribute USHORT firstCode;
	attribute USHORT entryCount;
	attribute SHORT idDelta;
	attribute USHORT idRangeOffset;
};
</pre>

<dl dfn-type=attribute dfn-for=CmapFormat2Subheader>
  <dt><dfn>firstCode</dfn></dt>
  <dd>First low-byte value handled by this subheader.</dd>

  <dt><dfn>entryCount</dfn></dt>
  <dd>Number of low-byte values handled by this subheader.</dd>

  <dt><dfn>idRangeOffset</dfn></dt>
  <dd>The element of the {{glyphElement}} array corresponding to the {{firstCode}}. Note that unlike most offset values in this standard, the {{idRangeOffset}} counts the number of bytes from <emphasis>the byte position of the {{idRangeOffset}} record itself</emphasis> to the target element, rather than from the start of the subtable header.</dd>

</dl>

The first element of the {{subheaders}} array must contain the following values:

<table>
    <tr><th>firstCode</th><td>0</td></tr>
    <tr><th>entryCode</th><td>256</td></tr>
    <tr><th>idDelta</th><td>0</td></tr>
    <tr><th>idRangeOffset</th><td>offset to start of {{glyphIndexArray}}</td></tr>
