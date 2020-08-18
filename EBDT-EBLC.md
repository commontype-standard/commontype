<h3 id="EBDT-EBLC" role="unfinished"><dfn>EBDT table</dfn> and <dfn>EBLC</dfn> tables - Bitmap Glyphs</h3>

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
    <dd>Offset to the index subtable array, measured from the beginning of the `EBLC` table.</dd>
    <dt><dfn>numberOfIndexSubTables</dfn></dt>
    <dd>Number of {{IndexSubtableArrayElement}} (and {{IndexSubtable}}) tables in this strike.
    </dd>
    <dt><dfn>startGlyphIndex</dfn></dt>
    <dd>The lowest glyph ID covered by this strike.</dd>
    <dt><dfn>endGlyphIndex</dfn></dt>
    <dd>The highest glyph ID covered by this strike.</dd>
    <dt><dfn>ppemX</dfn></dt>
    <dd>The target horizontal size of this strike.</dd>
    <dt><dfn>ppemY</dfn></dt>
    <dd>The target vertical size of this strike.</dd>
    <dt><dfn>bitDepth</dfn></dt>
    <dd>The number of bits per pixel to specify greyscale values in the bitmaps.</dd>
    <dt><dfn>flags</dfn></dt>
    <dd>If small metrics (see below) are provided for this strike, then this value determines the orientation of the metrics: `0x01` for horizontal metrics, `0x02` for vertical metrics.
</dl>

The {{BitmapSize}} definitions are followed by an "index subtable array" of size {{numberOfIndexSubTables}} for each strike. This is made up of a number of {{IndexSubTableArrayElement}} tables, each covering a range of glyph IDs and providing a pointer to an {{IndexSubtable}} with more information about the glyphs in this range.

<div class="note">
Note that {{IndexSubTableArrayElement}} was previously known as `IndexSubTableArray`; however, this subtable structure only describes a single element. The font file is expected to contain {{numberOfIndexSubTables}} instances of {{IndexSubTableArrayElement}} laid out contiguously for each strike.
</div>

<pre class="idl">
interface IndexSubTableArrayElement {
  attribute USHORT firstGlyphIndex;
  attribute USHORT lastGlyphIndex;
  attribute Offset32 additionalOffsetToIndexSubtable;
};
</pre>
<dl dfn-type=attribute dfn-for=IndexSubTableArrayElement>
    <dt><dfn>firstGlyphIndex</dfn></dt>
    <dd>The first glyph ID covered by this segment.</dd>
    <dt><dfn>lastGlyphIndex</dfn></dt>
    <dd>The final glyph ID (inclusively) covered by this segment.</dd>
    <dt><dfn>additionalOffsetToIndexSubtable</dfn></dt>
    <dd>The offset to the {{IndexSubtable}} for this segment, measured from the *beginning of the first* {{IndexSubTableArrayElement}} *for this strike*.</dd>
</dl>

<div class="note">
  To find the start of an {{IndexSubtable}} for a given {{IndexSubTableArrayElement}}, count {{indexSubTableArrayOffset}} + {{additionalOffsetToIndexSubtable}} bytes from the beginning of the `EBLC` table.
</div>

<pre class="idl">
typedef (IndexSubtable1 or IndexSubtable2 or IndexSubtable3 or IndexSubtable4 or IndexSubtable5) IndexSubtable;

interface IndexSubtableCommon {
  attribute USHORT indexFormat;
  attribute USHORT imageFormat;
  attribute Offset32 imageDataOffset;
};

interface IndexSubtable1 :IndexSubtableCommon {
  attribute Offset32[] offsetArray;
};

interface IndexSubtable2 :IndexSubtableCommon {
  attribute ULONG imageSize;
  attribute BigGlyphMetrics bigMetrics;
};

interface IndexSubtable3 :IndexSubtableCommon {
  attribute Offset32[] offsetArray;
};

interface GlyphIdOffsetPair {
  attribute USHORT glyphID;
  attribute Offset16 offset;
};

interface IndexSubtable4 :IndexSubtableCommon {
  attribute ULONG numGlyphs;
  attribute GlyphIdOffsetPair[] glyphArray;
};
</pre>

