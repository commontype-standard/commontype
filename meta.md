<h4 id="meta"><dfn>meta table</dfn> - Metadata Table</h4>
<table>
    <tr><th>Introduced</th> <td> 1.0 </td> </tr>
    <tr><th>Deprecated</th> <td> </td> </tr>
    <tr><th>Will be removed</th> <td> </td> </tr>
    <tr><th>Originator</th> <td> </td> </tr>
    <tr><th>Requirement status</th> <td> Optional</td> </tr>
    <tr><th>Dependencies</th> <td> </td>  </tr>
</table>

This table allows for arbitrary textual or binary metadata to be associated with a font file.

<pre class=include>path: idl/metaTable.md</pre>

<dl dfn-type=attribute dfn-for=DataMap>
  <dt><dfn>dataOffset</dfn></dt>
  <dd>Offset in bytes to the metadata entry, measured from the *start of the meta table*.
  </dd>
</dl>

The following metadata tags have been registered:

* `appl`: Apple private use
* `bild`: Apple private use
* `dlng`: Design languages. A comma-separated list of language/script combinations for which the font was designed.
* `slng`: Supported languages. A comma-separated list of language/script combinations which the font can support.

The language/script combinations in `dlng`/`slng` metadata blocks are adapted from [[!BCP47]]. While the definitions and data are identical to BCP47, within the `dlng`/`slng` data blocks, the script subtag is mandatory and the language tag is optional.

<div class="example">
    A font may be designed for Japanese, and include sufficient kanji to adequately display Chinese, even though some radical forms will differ in appearance from those expected by Chinese users. Its `dlng` will therefore be `Jpan` but its `slng` would be `Jpan,Hans,Hant`
</div>
