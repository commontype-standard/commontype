<h4 id="COLR-CPAL" rel="off-5.7.11+5.7.12"><dfn>COLR table</dfn> and <dfn>CPAL table</dfn> - Color Outlines</h4>

<table>
    <tr><th>Introduced</th> <td> 1.7 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> If one is present, the other must also be present</td>  </tr>
</table>

These tables provide a mechanism for specifying color glyphs by layering outlines from different glyph IDs on top of one another and applying colorisation from a color palette. A *base glyph*, specified by glyph ID, is mapped to a contiguous subarray of *layer records*, each containing the index of a layer glyph and color palette value.

<h5 id="COLR">COLR table</h5>

<pre class="idl">
interface COLRTable {
    attribute USHORT version;
    attribute USHORT numBaseGlyphRecords;
    attribute Offset32 baseGlyphRecordsOffset;
    attribute Offset32 layerRecordsOffset;
    attribute USHORT numLayerRecords;
};

interface BaseGlyphRecord {
    attribute USHORT gid;
    attribute USHORT firstLayerIndex;
    attribute USHORT numLayers;
};

interface LayerRecord {
    attribute USHORT gid;
    attribute USHORT paletteIndex;
};
</pre>
<dl dfn-type=attribute dfn-for=COLRTable>
  <dt><dfn>version</dfn></dt>
  <dd>Table version. Must be 0.</dd>
  <dt><dfn>baseGlyphRecordsOffset</dfn></dt>
  <dd>Offset from the beginning of the `COLR` table to a contiguous array of {{numBaseGlyphRecords}} {{BaseGlyphRecord}} tables.</dd>
  <dt><dfn>layerRecordsOffset</dfn></dt>
  <dd>Offset from the beginning of the `COLR` table to a contiguous array of {{numLayerRecords}} {{LayerRecord}} tables.</dd>
</dl>
<dl dfn-type=attribute dfn-for=BaseGlyphRecord>
  <dt><dfn>firstLayerIndex</dfn></dt>
  <dd>Index into the {{LayerRecord}} array of the first layer of the colorized glyph.</dd>
</dl>

<h5 id="CPAL">CPAL table</h5>

<pre class="idl">
typedef (CPALTableVersion0 or CPALTableVersion1) CPALTable;

interface CPALTableVersion0 {
    attribute USHORT version;
    attribute USHORT numPaletteEntries;
    attribute USHORT numPalettes;
    attribute USHORT numColorRecords;
    attribute Offset32 offsetFirstColorRecord;
    attribute USHORT[] colorRecordIndices;
};
interface CPALTableVersion1: CPALTableVersion0 {
    attribute Offset32 offsetPaletteTypeArray;
    attribute Offset32 offsetPaletteLabelArray;
    attribute Offset32 offsetPaletteEntryLabelArray;
};

interface ColorRecord {
    attribute uint8 blue;
    attribute uint8 green;
    attribute uint8 red;
    attribute uint8 alpha;
};
</pre>

<div class="note">

* Color records may be shared between palettes. Distinct colors are stored as an array of {{numColorRecords}} {{ColorRecord}}s. ({{offsetFirstColorRecord}} points to the index of the first color record.) Because of this, the total number of color records may be less than the product of {{numPaletteEntries}} and {{numPalettes}}.

* A `CPAL` table must contain at least one palette, containing at least one entry.

* All palettes must contain the same number of entries.

* The colors in each palette are indexed from 0, and are found by multiplying the selected palette ID by {{numPaletteEntries}}, adding the selected color ID, and using the result as an index into the {{colorRecordIndices}} array. The resulting index is used to index the {{ColorRecord}} array.

</div>

The following additional structures are used in format 1 `CPAL` tables:

<pre class="idl">
interface PaletteTypeArray {
    attribute ULONG[] paletteTypes;
};
interface PaletteLabelsArray {
    attribute USHORT[] paletteLabels;
};
interface PaletteEntryLabelsArray {
    attribute USHORT[] paletteEntryLabels;
};
</pre>
<dl dfn-type=attribute dfn-for=PaletteTypeArray>
  <dt><dfn>paletteTypes</dfn></dt>
  <dd>An array of size {{numPalettes}}, specifying the following flags for each palette:
    <ul>
        <li> **0x1**: this palette is suitable for displaying on a light background.
        <li> **0x2**: this palette is suitable for displaying on a dark background.
    </ul>
    <div class="note">Note that both flags may be set if the palette is suitable for both light and dark backgrounds.</div>
  </dd>
</dl>
<dl dfn-type=attribute dfn-for=PaletteLabelsArray>
  <dt><dfn>paletteLabels</dfn></dt>
  <dd>An array of size {{numPalettes}}, specifying [=name table=] entries providing a user-facing name for each palette.</dd>
</dl>
<dl dfn-type=attribute dfn-for=PaletteEntryLabelsArray>
  <dt><dfn>paletteEntryLabels</dfn></dt>
  <dd>An array of size {{numPaletteEntries}}, specifying [=name table=] entries providing a user-facing name for each palette entry.</dd>
</dl>

<div class="note">
    Note that each of the {{offsetPaletteTypeArray}}, {{offsetPaletteLabelArray}} and {{offsetPaletteEntryLabelArray}} entries in the {{CPALTableVersion1}} table may be set to zero if no information is to be provided.
</div>

<h5 id="COLR.in-prod">Implementation notes for font producers</h5>

* All glyphs referenced by a {{BaseGlyphRecord}} must have the same horizontal advance value.

<h5 id="COLR.in-cons">Implementation notes for font consumers</h5>

See [=Processing Color Fonts=].
