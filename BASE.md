<h3 id="BASE"><dfn>BASE table</dfn> - Baseline Table</h3>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The BASE table provides information to allow font consumers to align glyphs from different scripts along appropriate baselines. It may also be used for adjusting the baseline-to-baseline spacing of a text by defining script-, language-, and feature specific glyph extent values.

<pre class="idl">
interface BaseTableHeaderVersion10 {
  attribute USHORT tableMajorVersion;
  attribute USHORT tableMinorVersion;
  attribute Offset16 horizAxisOffset;
  attribute Offset16 vertAxisOffset;
};

interface BaseTableHeaderVersion11 : BaseTableHeaderVersion10 {
  attribute Offset16 itemVarStoreOffset;
};
</pre>

<dl dfn-type=attribute dfn-for=BaseTableHeaderVersion10>
  <dt><dfn>tableMajorVersion</dfn></dt>
  <dd>Table version. Must be 1.</dd>
  <dt><dfn>tableMinorVersion</dfn></dt>
  <dd>Table version. Must be 0 if item variation stores are not present, and 1 if item variation stores are present.</dd>
  <dt><dfn>horizAxisOffset</dfn></dt>
  <dd>Offset to the horizontal axis table, or zero if no horizontal axis table is present.
  <dt><dfn>vertAxisOffset</dfn></dt>
  <dd>Offset to the vertical axis table, or zero if no vertical axis table is present.
</dl>
<dl dfn-type=attribute dfn-for=BaseTableHeaderVersion11>
  <dt><dfn>itemVarStoreOffset</dfn></dt>
  <dd>Offset to the item variation store table or zero if no item variation store table is present.</dd>
</dl>

<div class="note">
  Note that within the `BASE` table and all of its subtables, all offset values are computed from the start of their respective subtable.
</div>

Both horizontal and vertical axis tables have the same structure. As this structure is somewhat complex, the formal properties of the structure will be described here, and interpretation and further discussion will be provided in the [[#base-discussion]] section below.

<pre class="idl">
interface BaseAxisTable {
  attribute Offset16 baseTagListOffset;
  attribute Offset16 baseScriptListOffset;
};
interface BaseTagList {
  attribute USHORT baseTagCount;
  attribute Tag[] baseLineTags;
};
interface BaseScriptList {
  attribute USHORT baseScriptCount;
  attribute BaseScriptRecord[] baseScriptRecords;
};
interface BaseScriptRecord {
  attribute Tag baseScriptTag;
  attribute Offset16 baseScriptOffset;
};
interface BaseScript {
  attribute Offset16 baseValuesOffset;
  attribute Offset16 defaultMinMaxOffset;
  attribute USHORT baseLangSysCount;
  attribute BaseLangSysRecord[] baseLangSysRecords;
};
interface BaseValues {
  attribute USHORT defaultBaselineIndex;
  attribute USHORT baseCoordCount;
  attribute Offset16[] baseCoords;
};
interface MinMax {
  attribute Offset16 minCoord;
  attribute Offset16 maxCoord;
  attribute USHORT featMinMaxCount;
  attribute FeatMinMaxRecord featMinMaxRecords;
};
interface FeatMinMaxRecord {
  attribute Tag featureTableTag;
  attribute Offset16 minCoord;
  attribute Offset16 maxCoord;
};
interface BaseLangSysRecord {
  attribute Tag baseLangSysTag;
  attribute Offset16 minMaxOffset;
};
</pre>

* The {{BaseTagList/tag}} value in the {{BaseTagList}} table must be a valid [=baseline tag=].
* The {{BaseScriptList/tag}} value in the {{BaseScriptList}} table must be a valid [=script tag=].
* The {{BaseLangSysRecord/tag}} value in the {{BaseLangSysRecord}} table must be a valid [=language tag=]. {{baseLangSysRecords}} must be specified in alphabetic order of language tag.
* The {{BaseValues/baseCoordCount}} value must be equal to the {{BaseTagList/baseTagCount}} value.
* The {{MinMax/minCoord}} and {{MinMax/maxCoord}} offsets point to a {{BaseCoord}} table in one of the following formats:

<pre class="idl">
  typedef (BaseCoordFormat1 or BaseCoordFormat2 or BaseCoordFormat3) BaseCoord;

  interface BaseCoordFormat1 {
    attribute USHORT baseCoordFormat;
    attribute SHORT coordinate;
  };

  interface BaseCoordFormat2 {
    attribute USHORT baseCoordFormat;
    attribute SHORT coordinate;
    attribute USHORT referenceGlyph;
    attribute USHORT baseCoordPoint;
  };

  interface BaseCoordFormat3 {
    attribute USHORT baseCoordFormat;
    attribute SHORT coordinate;
    attribute Offset16 deviceTable;
  };
</pre>

* The {{baseCoordFormat}} must be 1, 2, or 3 respectively.
* In a format 2 coordinate table, {{referenceGlyph}} and {{baseCoordPoint}} are respectively the glyph ID and coordinate index of a point on the glyph, such that if the process of hinting adjusts the position of this point, {{coordinate}} is also adjusted by the same amount.
* In a non-variable font file, the format 3 {{deviceTable}} offset refers to a {{DeviceTable}}; in a variable font file, it refers to an {{ItemVariationStore}}.

<h4 id="base-discussion">Discussion</h4>
<div class="nonnormative">

The purpose of this table is to enable the correct display of mixed-script text by providing for definition of multiple baselines. For example, a document which contains both English and Japanese text may wish to align the Japanese text along a lower baseline to the Latin baseline (typically, matching the position of Latin descenders). A font file could therefore use the `BASE` table to define the positions of the *ideographic baseline* and *Roman baseline*.

The baselines in the `BASE` table can be further specified by script, and separate values may be provided for horizontal and vertical layout.

As well as specifying baselines, the `BASE` table can be used to adjust the line spacing of a text by providing alternate glyph extent values depending on the combination of script, language and enabled layout features in use.

For each axis (horizontal and vertical) specified in the table:

* The {{BaseTagList}} contains the list of the baselines to be defined for the given axis. The baselines are identified by a [=baseline tag=].
* The {{BaseScriptList}} contains a list of records linking a script with baseline information in the form of a {{BaseScript}} table. The scripts are identified by a [=script tag=]. To set default baseline values for scripts not enumerated explicitly, the `DFLT` script may be used.
* The script-specific {{BaseScript}} table contains:
    * {{baseValuesOffset}}, a pointer to a {{BaseValues}} table which contains the list of baseline coordinate information, corresponding to the baselines defined in the {{BaseTagList}}, as well as a selector {{defaultBaselineIndex}} specifying the default baseline for this script.
    * {{defaultMinMaxOffset}}, a pointer to a default glyph extents table (a {{MinMax}} table) for this script.
    * and a list of {{BaseLangSysRecord}} tables which specify language-specific glyph extents by mapping between [=language tag=] and a {{MinMax}} table.
* Each glyph extents table (the {{MinMax}} table) may also provide alternative extent values to be used when certain layout features are enabled.

</div>

<h4 id="base-in-prod">Implementation notes for font producers</h4>

<div class="example">
Let us assume that we have a font file which only contains Latin script glyphs. However, we want this font to display correctly when Japanese characters (of a different font file) are used in mixed-script text. The Roman baseline of the font is at y-coordinate 0, and we wish to specify that the ideographic baseline is at -163 design units. The font producer will perform the following operations:

* Create a {{BaseTagList}} table with {{baseTagCount}}=2 and two tag entries, `romn` and `ideo`.
* No script-specific baselines are to defined, so only one {{BaseScriptRecord}} record will be needed. Create a {{BaseScriptList}} table with {{baseScriptCount}}=1, and a {{BaseScriptRecord}} table with {{baseScriptTag}}=`DFLT`.
* Create a {{BaseScript}} table. As we are not adjusting glyph extents (neither for the script itself or for language-specific variations), its {{defaultMinMaxOffset}} and the {{baseLangSysCount}} will both be zero. Set the {{baseScriptOffse}} in the {{BaseScriptRecord}} to point to this table.
* Create a {{BaseValues}} table with baseline values for each of the baselines we are defining. Set {{baseCoordCount}}=2 and, as the default baseline for this font will be the Roman baseline, set {{defaultBaselineIndex}}=0. The {{baseCoords}} array will point to two {{BaseCoord}} tables, one for each of the two baselines in turn:
    * One {{BaseCoordFormat1}} table with {{BaseCoordFormat1/baseCoordFormat}}=1 and {{BaseCoordFormat1/coordinate}}=0 to represent the Roman baseline.
    * A second {{BaseCoordFormat1}} table with {{BaseCoordFormat1/baseCoordFormat}}=1 and {{BaseCoordFormat1/coordinate}}=-163 to represent the ideographic baseline.
* Create an {{BaseAxisTable}} containing offsets to the {{BaseTagList}} and {{BaseScriptList}} tables.
* Create a {{BaseTableHeaderVersion10}} with {{tableMajorVersion}}=1 and {{tableMinorVersion}}=0, and with {{horizAxisOffset}} pointing to the {{BaseAxisTable}}.

</div>
