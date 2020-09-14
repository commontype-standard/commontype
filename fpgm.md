<h4 id="fpgm"><dfn>fpgm table</dfn> - Font Program Table</h4>

<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td>Used by [=glyf table=] </td> </tr>
</table>

This table contains an array of instructions used by the TrueType instruction processor. It is executed once at the start of font processing, and defines function and instruction definitions.

<pre class=include>path: idl/fpgmTable.md</pre>

The number of values is determined by the {{TableRecord/length}} of the table specified in the {{TableRecord}} in the `sfnt` header.

