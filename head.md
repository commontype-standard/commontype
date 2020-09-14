<h3 id="cmap"><dfn>head table</dfn> - Font Header Table</h3>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The `head` table contains general header information.

<pre class="idl">
interface HeadTable {
  attribute VERSION tableVersion;
  attribute VERSION fontRevision;
  attribute ULONG checkSumAdjustment;
  attribute ULONG magicNumber;
  attribute USHORT flags;
  attribute USHORT unitsPerEm;
  attribute LONGDATETIME created;
  attribute LONGDATETIME modified;
  attribute SHORT xMin;
  attribute SHORT yMin;
  attribute SHORT xMax;
  attribute SHORT yMax;
  attribute USHORT macStyle;
  attribute USHORT lowestRecPPEM;
  attribute SHORT fontDirectionHint;
  attribute SHORT indexToLocFormat;
  attribute SHORT unused;
};
</pre>

<dl dfn-type=attribute dfn-for=HeadTable>
    <dt><dfn>tableVersion</dfn></dt>
    <dd>Table version. Must be set to 1.0.</dd>
    <dt><dfn>magicNumber</dfn></dt>
    <dd>Must be set to 0x5f0f3cf5.</dd>
    <dt><dfn>flags</dfn></dt>
    <dd>
</dl>

<h4 id="head.in-prod">Implementation notes for font producers</h4>

* The {fontRevision} value *should* be equivalent to the value in string 5 of the [=name table=].
* The {checkSumAdjustment}

