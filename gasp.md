<h4 id="gasp" rel="off-5.3.7"><dfn>gasp table</dfn> - Grid Fitting and Scan-Conversion Procedure Table</h4>
<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> </td>  </tr>
</table>

This table describes hints to the rasterizer for rendering glyphs at particular pixel-per-em sizes.

<pre class=include>path: idl/gaspTable.md</pre>

<dl dfn-type=attribute dfn-for=GaspRange>
  <dt><dfn>rangeGaspBehavior</dfn></dt>
  <dd>A bit mask of flags:
    <ul>
        <li> **0x1**: use grid-fitting.
        <li> **0x2**: use grayscale rendering.
        <li> **0x4**: use grid-fitting with ClearType symmetric smoothing
        <li> **0x8**: use ClearType smoothing
    </ul>
</li>
</dl>

<h5 id="gasp.in-prod">Implementation notes for font producers</h5>

* {{GaspRange}} records should be ordered in increasing value of {{GaspRange/rangeMaxPPEM}}.
* The final {{GaspRange}} record must have a {{GaspRange/rangeMaxPPEM}} of 0xFFFF, specifying behaviour for all sizes above the previous record.

