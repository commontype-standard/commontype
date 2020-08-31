<h3 id="cmap"><dfn>cmap table</dfn> - Character to Glyph Index Mapping Table</h3>

<table>
    <tr><th>Introduced</th> <td> </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Required </td> </tr>
    <tr><th>Dependencies</th> <td> </td> </tr>
</table>

The `cmap` table defines the mapping from characters to glyphs. A font file may contain multiple mappings.

<pre class="idl">
interface CmapTableHeader {
  attribute SHORT tableVersion;
  attribute SHORT numSubTables;
  attribute CmapEncodingRecord[] cmapEncodingRecords;
};

interface CmapEncodingRecord {
  attribute SHORT platformID;
  attribute SHORT encodingID;
  attribute LONG offset;
};

</pre>

<dl dfn-type=attribute dfn-for=CmapTableHeader>
  <dt><dfn>tableVersion</dfn></dt>
  <dd>Table version. Must be zero.</dd>

  <dt><dfn>numSubTables</dfn></dt>
  <dd>Number of mapping records.</dd>
</dl>

The [=platform and encoding identifiers=] in the encoding record are used to specify the character repertoire and encoding used by the subtable.

The {{offset}} into each subtable, which contains the actual character to glyph ID mappings, is measured from the start of the cmap table.

<pre class=include>path: cmap/format-0.md</pre>
<pre class=include>path: cmap/format-2.md</pre>
<pre class=include>path: cmap/format-4.md</pre>
<pre class=include>path: cmap/format-6.md</pre>
<pre class=include>path: cmap/format-8.md</pre>
<pre class=include>path: cmap/format-10.md</pre>
<pre class=include>path: cmap/format-12.md</pre>
<pre class=include>path: cmap/format-13.md</pre>
<pre class=include>path: cmap/format-14.md</pre>

<h4 id="cmap.in-prod">Implementation notes for font producers</h4>

* Subtables contain a [=language identifier=] field. For cmap subtables with platform ID 1 (Macintosh) which contain language-specific mappings, this ID field must be set to the [=Macintosh language ID=] of the language *plus one*. Otherwise, the language ID field must be set to zero.

* Encoding records in the cmap table header must be sorted first by platform ID, then by platform-specific encoding ID, and then by language ID in the corresponding subtable. Each platform ID, platform-specific encoding ID, and language ID combination must appear only once in the cmap table.

<div class="note">
CommonType's recommendation is that  font producers creating fonts with characters entirely
within the Basic Multilingual Plane should generate cmap table entries
with Unicode codepoint encoding, using platform ID 0 platform encoding ID
3 and platform ID 3 platform encoding 1. Character to glyph ID
assignments compatible with the MacRoman encoding should be made using
platform ID 1 platform encoding 0.

The choice of subtable format is not entirely a free one, as certain
combinations of platform and platform encoding mandate particular
formats:

-   When the platform ID is 0 and platform encoding is 5 (Unicode
    Variation Sequences), the subtable must be format 10.
-   When platform ID is 3 and platform encoding ID is 1 (Windows
    Unicode), the subtable must be format 4.
-   When the platform ID is 3 and platform encoding is 10 (Windows
    full-range Unicode) to access codepoints beyond the Basic
    Multilingual Plane, the subtable must be format 12.
-   When the platform ID is 4 (Custom), the subtable must be format 0 or
    format 6.

Oterwise, CommonType recommends the use of format 4, 6 and 12 subtables.

It is legal to have a single subtable which is referenced from multiple
entries? This is useful when a given character encoding is present on
multiple platforms. For example, if there is a Unicode cmap subtable, it
can be referenced from one entry with platformID/encodingID (0, 3), and
from another entry with (3, 1).

The language field XXX
</div>

<div class="example"> For example, a Mac OS Turkish cmap subtable must set
this field to 18, since the Macintosh language ID for Turkish is 17. A
Mac OS Roman cmap subtable must set this field to 0, since Mac OS Roman
is not a language-specific encoding.
</div>

<h4 id="cmap.in-cons">Implementation notes for font consumers</h4>

See [=Mapping characters to glyphs=].
