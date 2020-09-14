<h5 id="format-6-cmap-subtable">Format 6 cmap subtable</h5>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

Format 6 is used when mapping a single contiguous range of codepoints in a character repertoire. Where there are multiple ranges to be mapped, format 4 subtables are used instead.

<pre class="idl">
interface CmapFormat6Subtable {
    attribute USHORT format;
    attribute USHORT length;
    attribute USHORT language;
    attribute USHORT firstCode;
    attribute USHORT entryCount;
    attribute USHORT[] glyphIdArray;
};
</pre>

<dl dfn-type=attribute dfn-for=CmapFormat6Subtable>
  <dt><dfn>firstCode</dfn></dt>
  <dd>First character code in the subrange.</dd>
  <dt><dfn>entryCount</dfn></dt>
  <dd>Number of character codes in the subrange.</dd>
  <dt><dfn>glyphIdArray</dfn></dt>
  <dd>Array of `entryCount` glyph indices.</dd>
</dl>
