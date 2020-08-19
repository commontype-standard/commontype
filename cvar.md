<h3 id="cvar"><dfn>cvar table</dfn> - CVT Variations Table</h3>

<table>
    <tr><th>Introduced</th> <td> 1.8 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td>Used by [=cvt table=] </td> </tr>
</table>

The `cvar` table determines how TrueType control values in the [=cvt table=] are to be adjusted when a variable font is instantiated.

<pre class="idl">
interface CvarTable {
  attribute USHORT tableMajorVersion;
  attribute USHORT tableMinorVersion;
  attribute USHORT tupleVariationCount;
  attribute Offset16 dataOffset;
  attribute TupleVariationHeader[] tupleVariationHeaders;
};
</pre>

