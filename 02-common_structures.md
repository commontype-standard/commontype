<h3 id="common-structures">Common Structures and Data</h3>

<h4 id="variation-common-structures" role="unfinished">Common Structures for Variable Fonts</h4>

<pre class="idl">
interface Tuple {
  attribute F2DOT14[] coordinates;
};

interface TupleVariationHeader {
  attribute USHORT variationDataSize;
  attribute USHORT tupleIndex;
  attribute Tuple peakTuple;
  attribute Tuple intermediateStartTuple;
  attribute Tuple intermediateEndTuple;
};
</pre>

XXX

<pre class=include>path: idl/ItemVariationStore.md</pre>


<h4 id="platform-and-encoding-ids"><dfn>Platform and Encoding Identifiers</dfn></h4>

Data entries in the [=cmap table=] and [=name table=] are designated as being for the
consumption of particular combinations of <dfn>platform</dfn> and <dfn>platform encoding</dfn>. The *platform encoding* selects a character repertoire and
codepoint-to-character mapping available on the given platform. The
platform encoding identifier is not unique across platforms, and hence
implementors must consider platform and platform encoding as a tuple.
[[#A-PlatEncoding]] defines the platform and platform encoding tuples.

<div class="note">
* Platform IDs and platform encoding IDs are used in two tables: the [=cmap table=] and the [=name table=]. `cmap` contains mappings between glyph IDs and codepoints in some operating system character encoding. `name` contains strings encoded in particular character encodings. Prior to the widespread adoption of Unicode as a common character encoding, the platform-specific nature of character encodings meant that data needed to be tagged with its platform character encoding so that it could be properly interpreted. Additionally, for fonts to operate correctly on multiple platforms, glyph mappings and text strings needed to be specified in multiple encodings, one for each platform on which the font was expected to operate.

* Platform ID 3 platform encoding ID 0 refers to the character repertoire and encoding used by the [Wingdings font](https://en.wikipedia.org/wiki/Wingdings#Character_set). It should only be used for symbol fonts following this encoding.

* The Unicode platform was introduced to allow for cross-platform encoding. However, the Unicode character assignments did not stabilize until backwards compatibility was guaranteed after the release of Unicode 2.0. For example, in Unicode 1.0, codepoint U+370 was allocated as Greek Non-Spacing Iota Below. In Unicode 1.1, this character was moved to codepoint U+345. Hence data using the Unicode platform must also specify the version of the Unicode Standard for which they are encoded. Despite the current prevalence of Unicode, the platform ID system is still required for the name table, as will be explained in the appropriate chapter.

* Platform ID 2 (ISO) was introduced to accommodate the character repertoire of ISO/IEC 10646, but when this standard was released it used the same character repertoire as Unicode and so this platform became redundant. Its use is discouraged by CommonType: font producers should not use it, and font consumers should use an alternative name/cmap entry instead.

* Platform 4 was introduced as a compatibility measure for Windows NT to allow non-Unicode applications to use fonts as though they were Windows ANSI encoded. Its use is discouraged by CommonType: font producers should not use it.

</div>

<h4 id="language-id"><dfn>Language Identifier</dfn></h4>

The cmap and name tables also specify that data refers to particular
languages: language-specific character-to-glyph mappings in the case of
Macintosh platform entries in the cmap table, and strings written in
particular languages in the name table.

The data is therefore marked with its language, but the identifiers
specifying a language are depending on the platform ID in use.

There are no language identifiers defined for the Unicode platform
(platform ID = 0), the ISO platform (platform ID = 2), or the custom
platform (platform ID = 4). This means that while these platforms may be
used for cmap table entries, they cannot be used for name table entries.

<h5 id="mac-language-id"><dfn>Macintosh language ID</dfn></h5>

The list of language identifiers defined for the Macintosh platform can be found in [[#B-MacLanguage]].

<h5 id="windows-language-id">Windows language ID</h5>

<pre class=biblio>
  {
    "ms-lcid": {
    "title": "Windows Language Code Identifier (LCID) Reference",
    "href": "https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-lcid/",
    "publisher": "Microsoft"
  }
  }
</pre>
On the Windows platform, Microsoft LCIDs should be used to refer to languages. See [[!ms-lcid]] for the list of LCID values and their interpretation.
