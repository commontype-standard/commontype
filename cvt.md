<h3 id="cvt"><dfn>cvt  table</dfn> - Control Value Table</h3>

<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td>Used by [=glyf table=] </td> </tr>
</table>

This table contains an array of values used by the TrueType instruction processor. Instructions in the [=glyf table=] can load values from this table using the `RCVT[]` instruction.

<pre class="idl">
interface cvtTable {
  attribute FWORD[] values;
};
</pre>

The number of values is determined by the {{TableRecord/length}} of the table specified in the {{TableRecord}} in the `sfnt` header. This length must be an multiple of 2.

<h4 id="cvt-in-cons">Implementation notes for font consumers</h4>

As the TrueType control value table is also writable using `WCVF[]` and `WCVP[]` instructions, it is recommended to read this table and use it to initialize an in-memory Control Value Table.
