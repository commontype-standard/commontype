<h3 id="avar"><dfn>avar table</dfn> - Axis Variations Table</h3>

<table>
    <tr><th>Introduced</th> <td> 1.8 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required for font consumers, optional for font producers</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The `avar` table describes a function for variable font axes to map between a linear axis value and a set of piecewise linear functions.

<pre class=include>path: idl/avarTable.md</pre>


<dl dfn-type=attribute dfn-for=avarTable>
  <dt><dfn>tableMajorVersion</dfn></dt>
  <dd>Table version. Must be 1.</dd>
  <dt><dfn>tableMinorVersion</dfn></dt>
  <dd>Table version. Must be 0.</dd>
  <dt><dfn>axisCount</dfn></dt>
  <dd>Must be equal to the number of axes defined in the [=fvar table=].</dd>
</dl>

<h4 id="avar.in-prod">Implementation notes for font producers</h4>

* If this table is used, then all axes defined must have a corresponding {{SegmentMaps}} record. The records must appear in the order in which the axes are defined in the [=fvar table=].

* If a default (linear -1 to +1) mapping is required for an axis, then the {{positionMapCount}} of its corresponding {{SegmentMaps}} record must be 0.

* If a non-linear mapping is provided, then {{AxisValueMap}} must contain at least three entries; one which maps {{fromCoordinate}} -1 to {{toCoordinate}} -1, one which maps {{fromCoordinate}} 0 to {{toCoordinate}} 0, and one which maps {{fromCoordinate}} 1 to {{toCoordinate}} 1.

* {{toCoordinate}} entries must increase monotonically.

<h4 id="avar.in-cons">Implementation notes for font consumers</h4>

See [[#processing-variable-fonts]].
