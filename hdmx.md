<h4 id="hdmx" rel="off-5.7.2+8.12"><dfn>hdmx table</dfn> - Horizontal Device Metrics Table</h4>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> [=glyf table=] </td> </tr>
</table>

This table pre-computes scaled glyph widths for fonts where the widths can scale non-linearly due to TrueType instructions. Such fonts should set bit 4 of {{headTable/flags}}; where this bit is not set, this table should not be produced.

<pre class=include>path: idl/hdmxTable.md</pre>

* The {{hdmxTable/records}} array must be sorted in increasing order of {{DeviceRecord/pixelSize}}.
* Font producers must pad the {{DeviceRecord}} with 0 bytes to a multiple of 32 bytes. The length in {{hdmxTable/sizeDeviceRecord}} should include this padding.
