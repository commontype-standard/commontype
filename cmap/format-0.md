<h5 id="format-0-cmap-subtable">Format 0 cmap subtable</h5>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required by font consumers; Discouraged by CommonType for font producers (use format 6 instead) </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This is a simple character to glyph index mapping table. It is limited to 256 character codepoints and can only access glyph IDs between 0 and 255.

<pre class="idl">
interface CmapFormat0Subtable {
  attribute USHORT format;
  attribute USHORT length;
  attribute USHORT language;
  attribute byte[] glyphIdArray;
};
</pre>

[=Font producers=] must include 256 elements in the {{glyphIdArray}} and set the {{CmapFormat0Subtable/length}} to 262.
