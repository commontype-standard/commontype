<h5 id="format-12-cmap-subtable">Format 12 cmap subtable</h5>

<table>
    <tr><th>Introduced</th> <td> 1.3 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This subtable format allows for 32-bit mappings of multiple contiguous segments.

<pre class="idl">
interface CmapFormat12Subtable {
    attribute USHORT format;
    attribute USHORT formatMinor;
    attribute ULONG length;
    attribute ULONG language;
    attribute ULONG numGroups;
    attribute SequentialMapGroup[] groups;
};

interface SequentialMapGroup {
    attribute ULONG startCharCode;
    attribute ULONG endCharCode;
    attribute ULONG startGlyphID;
};
</pre>

<h6 id="cmap-12-impl-prod">Implementation notes for font producers</h6>

* Groups must be arranged in increasing value of {{startCharCode}}.
* Groups may not overlap.
