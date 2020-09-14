<h4 id="DSIG"><dfn>DSIG table</dfn> - Digital Signature Table</h4>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The DSIG table was intended to store digital signatures to ensure the integrity of font files and to prevent the unauthorized modification of font files, particularly to prevent the removal of embedding restrictions. However, the verification process for these signatures is sufficiently burdensome that there are no known implementations of it. Font producers should, however, include an empty DSIG table (one with no zero signature records) in order to satisfy the expectations of some font consumers.

<pre class=include>path: idl/DSIGTable.md</pre>

