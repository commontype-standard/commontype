<h4 id="hmtx"><dfn>hmtx table</dfn> - Horizontal Metrics Table</h4>
<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> </td>  </tr>
</table>

This table contains glyph-level horizontal metric information.

<pre class=include>path: idl/hmtxTable.md</pre>

<dl dfn-type=attribute dfn-for=hmtxTable>
  <dt><dfn>hMetrics</dfn></dt>
  <dd>The number of metrics is determined by {{hheaTable/numberofHMetrics}}.</dd>
  <dt><dfn>leftSideBearings</dfn></dt>
  <dd>The number of entries in this array is determined by {{maxpTableCFF/numGlyphs}} - {{hheaTable/numberofHMetrics}}.</dd>

</dl>
