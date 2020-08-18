<h4 id="format-10-cmap">Format 10 cmap subtable</h4>

<table>
    <tr><th>Introduced</th> <td> 1.3 </td> </tr>
    <tr><th>Deprecated</th> <td> 1.9 of CommonType </td> </tr>
    <tr><th>Will be removed</th> <td>  1.10 of CommonType</td></tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Discouraged by CommonType. Not supported by Uniscribe. Font producers should use format 12 instead.</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This format was intended for fonts mapping a contiguous block of codepoints outside the Unicode BMP.

<pre class="idl">
interface CmapFormat10Subtable {
    attribute USHORT format;
    attribute USHORT formatVersionMinor;
    attribute ULONG length;
    attribute ULONG language;
    attribute ULONG startCharCode;
    attribute ULONG numChars;
    attribute USHORT[] glyphs;
};</pre>

<dl dfn-type=attribute dfn-for=CmapFormat10Subtable>
  <dt><dfn>startCharCode</dfn></dt>
  <dd>First character code in the subrange.</dd>
  <dt><dfn>numChars</dfn></dt>
  <dd>Number of character codes in the subrange.</dd>
  <dt><dfn>glyphs</dfn></dt>
  <dd>Array of `numChars` glyph indices.</dd>
</dl>
