<h4 id="head" rel="off-5.2.3+8.13"><dfn>head table</dfn> - Font Header Table</h4>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The `head` table contains general header information.

<pre class=include>path: idl/headTable.md</pre>


<dl dfn-type=attribute dfn-for=headTable>
    <dt><dfn>flags</dfn></dt>
    <dd></dd>
</dl>

<h5 id="head.in-prod">Implementation notes for font producers</h5>

* The {{fontRevision}} value *should* be equivalent to the value in string 5 of the [=name table=].
* The {{checkSumAdjustment}}

