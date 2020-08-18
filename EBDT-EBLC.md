<h3 id="EBDT-EBLC"><dfn>EBDT table</dfn> and <dfn>EBLC</dfn> tables - Bitmap Glyphs</h3>

<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> If one is present, the other must also be present</td>  </tr>
</table>

These tables provide the ability to define glyphs as monochrome bitmaps. A font file may contain multiple sets of bitmap images, representing glyphs at a particular size. The `EBDT` table contains the bitmap data (and, optionally, metrics information) while the `EBLC` contains glyph metrics and indices into the `EBDT` table to locate the bitmaps.

<pre class="idl">
interface EBDTTable {
    attribute USHORT tableMajorVersion;
    attribute USHORT tableMinorVersion;
    attribute byte[] data;
};
</pre>
<dl dfn-type=attribute dfn-for=EBDTTable>
  <dt><dfn>tableMajorVersion</dfn></dt>
  <dd>Table version. Must be 2.</dd>
  <dt><dfn>tableMinorVersion</dfn></dt>
  <dd>Table version. Must be 0.</dd>
  <dt><dfn>data</dfn></dt>
  <dd>Bitmap and metric data, indexed by the `EBLC` table.</dd>
</dl>

<pre class="idl">
interface EBLCTable {
    attribute USHORT tableMajorVersion;
    attribute USHORT tableMinorVersion;
    attribute ULONG  numSizes;
    attribute BitmapSize[] strikes;
};
interface BitmapSize {
    attribute Offset32 indexSubTableArrayOffset;
    attribute ULONG indexTablesSize;
    attribute ULONG numberOfIndexSubTables;
    attribute ULONG unused;
    attribute SbitLineMetrics hori;
    attribute SbitLineMetrics vert;
    attribute USHORT startGlyphIndex;
    attribute USHORT endGlyphIndex;
    attribute uint8 ppemX;
    attribute uint8 ppemY;
    attribute uint8 bitDepth;
    attribute int8 flags;
};
interface SbitLineMetrics {
    attribute int8 ascender;
    attribute int8 descender;
    attribute uint8 widthMax;
    attribute int8 caretSlopeNumerator;
    attribute int8 caretSlopeDenominator;
    attribute int8 caretOffset;
    attribute int8 minOriginSB;
    attribute int8 minAdvanceSB;
    attribute int8 maxBeforeBL;
    attribute int8 minAfterBL;
    attribute int8 pad1;
    attribute int8 pad2;
};
</pre>
<dl dfn-type=attribute dfn-for=EBLCTable>
  <dt><dfn>tableMajorVersion</dfn></dt>
  <dd>Table version. Must be 2.</dd>
  <dt><dfn>tableMinorVersion</dfn></dt>
  <dd>Table version. Must be 0.</dd>
  <dt><dfn>strikes</dfn></dt>
  <dd>Specifies bitmaps used at a particular size.</dd>
</dl>
<dl dfn-type=attribute dfn-for=BitmapSize>
    <dt><dfn>indexSubTableArrayOffset</dfn></dt>
    <dd>Offset to the {{IndexSubtableArray}} describing the range of glyph IDs covered by this strike, measured from the beginning of the `EBLC` table.</dd>
    








