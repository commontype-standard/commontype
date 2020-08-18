<h4>Format 8 cmap subtable</h4>

<table>
    <tr><th>Introduced</th> <td> 1.3 </td> </tr>
    <tr><th>Deprecated</th> <td> 1.9 of CommonType </td> </tr>
    <tr><th>Will be removed</th> <td> 1.10 of CommonType </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Discouraged by CommonType and OpenType</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

This format was a mistake. Its intent was to encode both 16-bit Unicode codepoints and surrogate pairs, allowing shaping engines to process Unicode codepoints in UTF-16. However, all rendering engines do (and should) process Unicode as UTF-32, making this format redundant.
