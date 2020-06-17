<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.name"></a>Chapter 10. name - Naming Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80799721840"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.10.1.1"></a>Specification</h3></div></div></div><p role="">The naming table allows multilingual strings to be
          associated with the OpenType font file. These strings can
          represent copyright notices, font names, family names, style
          names, and so on. To keep this table short, the font
          manufacturer may wish to make a limited set of entries in
          some small set of languages; later, the font can be
          "localized" and the strings translated or added. Other parts
          of the OpenType font file that require these strings can
          then refer to them simply by their index number. Clients
          that need a particular string can look it up by its platform
          ID, character encoding ID, language ID and name ID. Note
          that some platforms may require single byte character
          strings, while others may require double byte
          strings.</p><p role="">For historical reasons, some applications which install
          fonts perform version control using Macintosh platform
          (platform ID 1) strings from the <a role="" class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>
          table. Because of this, we strongly recommend that the
          <a role="" class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table of all fonts include Macintosh
          platform strings and that the syntax of the version number
          (name id 5) follows the guidelines given in this
          document.</p><p role="">The Naming Table is organized as follows:</p><div class="table"><a name="idm80799716320"></a><p class="title"><strong>Table 10.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">format</td><td role="">Format selector (=0).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">count</td><td role="">Number of name records.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">stringOffset</td><td role="">Offset to start of string storage (from start
                  of table).</td><td class="auto-generated"> </td></tr><tr><td role="">n NameRecords</td><td role="">nameRecord [count]</td><td role="">The name records where count is the number of
	      records.</td><td class="auto-generated"> </td></tr><tr><td role="">(Variable)</td><td role=""> </td><td role="">Storage for the actual string data.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each NameRecord looks like this:</p><div class="table"><a name="idm80799706512"></a><p class="title"><strong>Table 10.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">platformID</td><td role="">Platform ID.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">encodingID</td><td role="">Platform-specific encoding ID.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">languageID</td><td role="">Language ID.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">nameID</td><td role="">Name ID.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">length</td><td role="">String length (in bytes).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">offset</td><td role="">String offset from start of storage area (in
                  bytes).</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Following are the descriptions of the four kinds of ID.
          Note that the specific values listed here are the only ones
          that are predefined; new ones may be added by registry with
          Apple Developer Technical Support. Similar to the character
          encoding table, the NameRecords is sorted by platform ID,
          then platform-specific ID, then language ID, and then by
          name ID.</p><div class="table"><a name="idm80799694816"></a><p class="title"><strong>Table 10.3. Platform IDs, Platform-specific encoding IDs and
            Language IDs</strong></p><div class="table-contents"><table role="" class="table" summary="Platform IDs, Platform-specific encoding IDs and&#10;            Language IDs" border="1"><colgroup><col width="3pc"/><col width="8pc"/><col width="11pc"/><col width="8pc"/></colgroup><thead><tr><th role="">PlatformID</th><th role="">Platform name</th><th role="">Platform-specific encoding IDs</th><th role="">Language IDs</th></tr></thead><tbody><tr><td role="">0</td><td role="">Unicode</td><td role=""><a role="" class="link" href="chapter.name.html#name_enc0" title="Table 10.4. Unicode platform-specific encoding IDs (platform ID = 0)">Various</a></td><td role="">None</td></tr><tr><td role="">1</td><td role="">Macintosh</td><td role=""><a role="" class="link" href="chapter.name.html#name_enc1" title="Table 10.6. Macintosh platform-specific encoding IDs (script manager codes), (platform ID = 1)">Script manager
                    code</a></td><td role=""><a role="" class="link" href="chapter.name.html#name_lang1" title="Table 10.7. Macintosh language IDs (platform ID = 1)">Various</a></td></tr><tr><td role="">2</td><td role="">ISO [deprecated]</td><td role=""><a role="" class="link" href="chapter.name.html#name_enc2" title="Table 10.8. ISO specific encodings (platform ID=2) [Deprecated]">ISO
                    encoding</a> [deprecated]</td><td role="">None</td></tr><tr><td role="">3</td><td role="">Microsoft</td><td role=""><a role="" class="link" href="chapter.name.html#name_enc3" title="Table 10.5. Microsoft platform-specific encoding IDs (platform ID= 3)">Microsoft
                    encoding</a></td><td role=""><a role="" class="link" href="chapter.name.html#name_lang3">Various</a></td></tr><tr><td role="">4</td><td role="">Custom</td><td role=""><a role="" class="link" href="chapter.name.html#name_enc4" title="Table 10.9. Custom platform-specific encoding IDs (platform ID=4)">Custom</a></td><td role="">None</td></tr></tbody></table></div></div><br class="table-break"/><p role="">Note that platform ID 2 (ISO) has been deprecated as of
          OpenType Specification v1.3. It was intended to represent
          ISO/IEC 10646, as opposed to Unicode; both standards have
          identical character code assignments.</p><p role="">PlatformID values 240 through 255 are reserved for
          user-defined platforms. The DTS registry will never assign
          these values to a registered platform.</p><div class="table"><a name="name_enc0"></a><p class="title"><strong>Table 10.4. Unicode platform-specific encoding IDs (platform ID =
            0)</strong></p><div class="table-contents"><table role="" class="table" summary="Unicode platform-specific encoding IDs (platform ID =&#10;            0)" border="1"><colgroup><col width="3pc"/><col width="27pc"/></colgroup><thead><tr><th role="">EncodingID</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">Unicode 1.0 semantics</td></tr><tr><td role="">1</td><td role="">Unicode 1.1 semantics</td></tr><tr><td role="">2</td><td role="">ISO 10646:1993 semantics</td></tr><tr><td role="">3</td><td role="">Unicode 2.0 and onwards semantics, Unicode BMP only</td></tr><tr><td role="">4</td><td role="">Unicode 2.0 and onwards semantics, Unicode
		  full repertoire</td></tr><tr><td role="">5</td><td role="">Unicode Variation Sequences</td></tr></tbody></table></div></div><br class="table-break"/><p role="">A new encoding ID for the Unicode platform will be
          assigned if a new version of Unicode moves characters, in
          order to properly specify character code semantics. The
          distinction between Unicode platform-specific encoding IDs 1
          and 2 is for historical reasons only; Unicode 1.1 is in fact
          identical in repertoire and encoding to ISO 10646:1993
          (before any amendments).</p><p role="">Unicode platform encoding ID 5 can be used for encodings
        in the 'cmap' table but not for strings in the 'name' table.</p><p role="">There are currently no language IDs defined for the
          Unicode platform. This means that it can be used for
          encodings in the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table but not for
          strings in the <a role="" class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table.</p><div class="table"><a name="name_enc3"></a><p class="title"><strong>Table 10.5. Microsoft platform-specific encoding IDs (platform
            ID= 3)</strong></p><div class="table-contents"><table role="" class="table" summary="Microsoft platform-specific encoding IDs (platform&#10;            ID= 3)" border="1"><colgroup><col width="5pc"/><col width="5pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Platform ID</th><th role="">Encoding ID</th><th role="">Description</th></tr></thead><tbody><tr><td role="">3</td><td role="">0</td><td role="">Symbol</td></tr><tr><td role="">3</td><td role="">1</td><td role="">Unicode BMP only</td></tr><tr><td role="">3</td><td role="">2</td><td role="">ShiftJIS</td></tr><tr><td role="">3</td><td role="">3</td><td role="">PRC</td></tr><tr><td role="">3</td><td role="">4</td><td role="">Big5</td></tr><tr><td role="">3</td><td role="">5</td><td role="">Wansung</td></tr><tr><td role="">3</td><td role="">6</td><td role="">Johab</td></tr><tr><td role="">3</td><td role="">7</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">8</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">9</td><td role="">Reserved</td></tr><tr><td role="">3</td><td role="">10</td><td role="">Unicode full repertoire</td></tr></tbody></table></div></div><br class="table-break"/><p role="">When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1. When
          building a symbol font for Windows, the platform ID should
          be 3 and the encoding ID should be 0. When building a font
          that will be used on the Macintosh, the platform ID should
          be 1 and the encoding ID should be 0.</p><p role="">Microsoft Language IDs (platform ID = 3)</p><p role="">The language ID (LCID in the table below) refers to a
          value which identifies the language in which a particular
          string is written. Fifty of the language ID's assigned by
          Microsoft are listed below, along with their corresponding
          code pages. There are 85 additional language ID's assigned.
          corresponding code pages. There are 85 additional language
          ID's assigned.  For a full list, please see the <a role="" class="ulink" href="http://www.microsoft.com/globaldev/reference/loclanghome.asp" target="_top">Microsoft
          Global Development</a> site or <a role="" class="ulink" href="http://support.microsoft.com/default.aspx?scid=kb;EN-US;q224804" target="_top">Knowledge
          Base article Q224804</a>.</p><div class="informaltable"><a name="name_lang3"></a><table role="" class="informaltable" border="1"><colgroup><col width="8pc"/><col width="8pc"/><col width="6pc"/><col width="4pc"/><col width="4pc"/></colgroup><thead><tr><th role="">Primary Language</th><th role="">Locale Name</th><th role="">LCID</th><th role="">Win CP</th><th role="">OEM CP</th></tr></thead><tbody><tr><td role="">Albanian</td><td role="">Albania</td><td role="">(041c; SQI)</td><td role=""> </td><td role=""> </td></tr><tr><td role="">Basque</td><td role="">Basque</td><td role="">(042D; EUQ)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Byelorussian</td><td role="">Byelorussia</td><td role="">(0423, BEL)</td><td role="">1251</td><td role="">866</td></tr><tr><td role="">Bulgarian</td><td role="">Bulgaria</td><td role="">(0402, BGR)</td><td role="">1251</td><td role="">866</td></tr><tr><td role="">Catalan</td><td role="">Catalan</td><td role="">(0403; CAT)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Croatian</td><td role="">Croatian</td><td role="">(041a, SHL)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Czech</td><td role="">Czech</td><td role="">(0405; CSY)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Danish</td><td role="">Danish</td><td role="">(0406; DAN)</td><td role="">1252</td><td role="">865</td></tr><tr><td role="">Dutch (2):</td><td role="">Dutch (Standard)</td><td role="">(0413; NLD)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Dutch (2):</td><td role="">Belgian (Flemish)</td><td role="">(0813; NLB)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">English (6):</td><td role="">American</td><td role="">(0409; ENU)</td><td role="">1252</td><td role="">437</td></tr><tr><td role="">English (6):</td><td role="">British</td><td role="">(0809; ENG)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">English (6):</td><td role="">Australian</td><td role="">(0c09; ENA)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">English (6):</td><td role="">Canadian</td><td role="">(1009; ENC)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">English (6):</td><td role="">New Zealand</td><td role="">(1409; ENZ)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">English (6):</td><td role="">Ireland</td><td role="">(1809; ENI)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Estonian</td><td role="">Estonia</td><td role="">(0425, ETI)</td><td role="">1257</td><td role="">775</td></tr><tr><td role="">Finnish</td><td role="">Finnish</td><td role="">(040b; FIN)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">French</td><td role="">French (Standard)</td><td role="">(040c; FRA)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">French</td><td role="">Belgian</td><td role="">(080c; FRB)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">French</td><td role="">Canadian</td><td role="">(0c0c; FRC)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">French</td><td role="">Swiss</td><td role="">(100c; FRS)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">French</td><td role="">Luxembourg</td><td role="">(140c; FRL)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">German</td><td role="">German (Standard)</td><td role="">(0407; DEU)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">German</td><td role="">Swiss</td><td role="">(0807; DES)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">German</td><td role="">Austrian</td><td role="">(0c07; DEA)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">German</td><td role="">Luxembourg</td><td role="">(1007; DEL)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">German</td><td role="">Liechtenstein</td><td role="">(1407; DEC)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Greek</td><td role="">Greek</td><td role="">(0408; ELL)</td><td role="">1253</td><td role="">737 or 869<a href="#ftn.idm80799559072" class="footnote" id="idm80799559072"><sup class="footnote">[a]</sup></a></td></tr><tr><td role="">Hungarian</td><td role="">Hungarian</td><td role="">(040e; HUN)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Icelandic</td><td role="">Icelandic</td><td role="">(040F; ISL)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Italian (2):</td><td role="">Italian (Standard)</td><td role="">(0410; ITA)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Italian (2):</td><td role="">Swiss</td><td role="">(0810; ITS)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Latvian</td><td role="">Latvia</td><td role="">(0426, LVI)</td><td role="">1257</td><td role="">775</td></tr><tr><td role="">Lithuanian</td><td role="">Lithuania</td><td role="">(0427, LTH)</td><td role="">1257</td><td role="">775</td></tr><tr><td role="">Norwegian (2):</td><td role="">Norwegian (Bokmal)</td><td role="">(0414; NOR)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Norwegian (2):</td><td role="">Norwegian (Nynorsk)</td><td role="">(0814; NON)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Polish</td><td role="">Polish</td><td role="">(0415; PLK)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Portuguese (2):</td><td role="">Portuguese (Brazilian)</td><td role="">(0416; PTB)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Portuguese (2):</td><td role="">Portuguese (Standard)</td><td role="">(0816; PTG)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Romanian (2):</td><td role="">Romania</td><td role="">(0418, ROM)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Russian</td><td role="">Russian</td><td role="">(0419; RUS)</td><td role="">1251</td><td role="">866</td></tr><tr><td role="">Slovak</td><td role="">Slovak</td><td role="">(041b; SKY)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Slovenian</td><td role="">Slovenia</td><td role="">(0424, SLV)</td><td role="">1250</td><td role="">852</td></tr><tr><td role="">Spanish (3):</td><td role="">Spanish (Traditional Sort)</td><td role="">(040a; ESP)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Spanish (3):</td><td role="">Mexican</td><td role="">(080a; ESM)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Spanish (3):</td><td role="">Spanish (Modern Sort)</td><td role="">(0c0a; ESN)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Swedish</td><td role="">Swedish</td><td role="">(041D; SVE)</td><td role="">1252</td><td role="">850</td></tr><tr><td role="">Turkish</td><td role="">Turkish</td><td role="">(041f; TRK)</td><td role="">1254</td><td role="">857</td></tr><tr><td role="">Ukrainian</td><td role="">Ukraine</td><td role="">(0422, UKR)</td><td role="">1251</td><td role="">866 </td></tr></tbody><tbody class="footnotes"><tr><td colspan="5"><div id="ftn.idm80799559072" role="" class="footnote"><p role=""><a href="#idm80799559072" class="para"><sup class="para">[a] </sup></a>737 is default, but 869 (IBM Greek) will be
                      available at setup time through the selection of
                      a bogus Greek locale in Custom Setup.</p></div></td></tr></tbody></table></div><div class="table"><a name="name_enc1"></a><p class="title"><strong>Table 10.6. Macintosh platform-specific encoding IDs (script
            manager codes), (platform ID = 1)</strong></p><div class="table-contents"><table role="" class="table" summary="Macintosh platform-specific encoding IDs (script&#10;            manager codes), (platform ID = 1)" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Code</th><th role="">Script</th></tr></thead><tbody><tr><td role="">0</td><td role="">Roman</td></tr><tr><td role="">1</td><td role="">Japanese</td></tr><tr><td role="">2</td><td role="">Chinese (Traditional)</td></tr><tr><td role="">3</td><td role="">Korean</td></tr><tr><td role="">4</td><td role="">Arabic</td></tr><tr><td role="">5</td><td role="">Hebrew</td></tr><tr><td role="">6</td><td role="">Greek</td></tr><tr><td role="">7</td><td role="">Russian</td></tr><tr><td role="">8</td><td role="">RSymbol</td></tr><tr><td role="">9</td><td role="">Devanagari</td></tr><tr><td role="">10</td><td role="">Gurmukhi</td></tr><tr><td role="">11</td><td role="">Gujarati</td></tr><tr><td role="">12</td><td role="">Oriya</td></tr><tr><td role="">13</td><td role="">Bengali</td></tr><tr><td role="">14</td><td role="">Tamil</td></tr><tr><td role="">15</td><td role="">Telugu</td></tr><tr><td role="">16</td><td role="">Kannada</td></tr><tr><td role="">17</td><td role="">Malayalam</td></tr><tr><td role="">18</td><td role="">Sinhalese</td></tr><tr><td role="">19</td><td role="">Burmese</td></tr><tr><td role="">20</td><td role="">Khmer</td></tr><tr><td role="">21</td><td role="">Thai</td></tr><tr><td role="">22</td><td role="">Laotian</td></tr><tr><td role="">23</td><td role="">Georgian</td></tr><tr><td role="">24</td><td role="">Armenian</td></tr><tr><td role="">25</td><td role="">Chinese (Simplified)</td></tr><tr><td role="">26</td><td role="">Tibetan</td></tr><tr><td role="">27</td><td role="">Mongolian</td></tr><tr><td role="">28</td><td role="">Geez</td></tr><tr><td role="">29</td><td role="">Slavic</td></tr><tr><td role="">30</td><td role="">Vietnamese</td></tr><tr><td role="">31</td><td role="">Sindhi</td></tr><tr><td role="">32</td><td role="">Uninterpreted</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="name_lang1"></a><p class="title"><strong>Table 10.7. Macintosh language IDs (platform ID = 1)</strong></p><div class="table-contents"><table role="" class="table" summary="Macintosh language IDs (platform ID = 1)" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Code</th><th role="">Language</th></tr></thead><tbody><tr><td role="">0</td><td role="">English</td></tr><tr><td role="">1</td><td role="">French</td></tr><tr><td role="">2</td><td role="">German</td></tr><tr><td role="">3</td><td role="">Italian</td></tr><tr><td role="">4</td><td role="">Dutch</td></tr><tr><td role="">5</td><td role="">Swedish</td></tr><tr><td role="">6</td><td role="">Spanish</td></tr><tr><td role="">7</td><td role="">Danish</td></tr><tr><td role="">8</td><td role="">Portuguese</td></tr><tr><td role="">9</td><td role="">Norwegian</td></tr><tr><td role="">10</td><td role="">Hebrew</td></tr><tr><td role="">11</td><td role="">Japanese</td></tr><tr><td role="">12</td><td role="">Arabic</td></tr><tr><td role="">13</td><td role="">Finnish</td></tr><tr><td role="">14</td><td role="">Greek</td></tr><tr><td role="">15</td><td role="">Icelandic</td></tr><tr><td role="">16</td><td role="">Maltese</td></tr><tr><td role="">17</td><td role="">Turkish</td></tr><tr><td role="">18</td><td role="">Yugoslavian</td></tr><tr><td role="">19</td><td role="">Chinese (Traditional)</td></tr><tr><td role="">20</td><td role="">Urdu</td></tr><tr><td role="">21</td><td role="">Hindi</td></tr><tr><td role="">22</td><td role="">Thai</td></tr><tr><td role="">23</td><td role="">Korean</td></tr><tr><td role="">24</td><td role="">Lithuanian</td></tr><tr><td role="">25</td><td role="">Polish</td></tr><tr><td role="">26</td><td role="">Hungarian</td></tr><tr><td role="">27</td><td role="">Estonian</td></tr><tr><td role="">28</td><td role="">Latvian</td></tr><tr><td role="">29</td><td role="">Sami</td></tr><tr><td role="">30</td><td role="">Faroese</td></tr><tr><td role="">31</td><td role="">Farsi/Persian</td></tr><tr><td role="">32</td><td role="">Russian</td></tr><tr><td role="">33</td><td role="">Chinese (Simplified)</td></tr><tr><td role="">34</td><td role="">Flemish</td></tr><tr><td role="">35</td><td role="">Irish Gaelic</td></tr><tr><td role="">36</td><td role="">Albanian</td></tr><tr><td role="">37</td><td role="">Romanian</td></tr><tr><td role="">38</td><td role="">Czech</td></tr><tr><td role="">39</td><td role="">Slovak</td></tr><tr><td role="">40</td><td role="">Slovenian</td></tr><tr><td role="">41</td><td role="">Yiddish</td></tr><tr><td role="">42</td><td role="">Serbian</td></tr><tr><td role="">43</td><td role="">Macedonian</td></tr><tr><td role="">44</td><td role="">Bulgarian</td></tr><tr><td role="">45</td><td role="">Ukrainian</td></tr><tr><td role="">46</td><td role="">Byelorussian </td></tr><tr><td role="">47</td><td role="">Uzbek </td></tr><tr><td role="">48</td><td role="">Kazakh </td></tr><tr><td role="">49</td><td role="">Azerbaijani (Cyrillic script) </td></tr><tr><td role="">50</td><td role="">Azerbaijani (Arabic script) </td></tr><tr><td role="">51</td><td role="">Armenian </td></tr><tr><td role="">52</td><td role="">Georgian </td></tr><tr><td role="">53</td><td role="">Moldavian</td></tr><tr><td role="">54</td><td role="">Kirghiz</td></tr><tr><td role="">55</td><td role="">Tajiki</td></tr><tr><td role="">56</td><td role="">Turkmen</td></tr><tr><td role="">57</td><td role="">Mongolian (Mongolian script)</td></tr><tr><td role="">58</td><td role="">Mongolian (Cyrillic script)</td></tr><tr><td role="">59</td><td role="">Pashto</td></tr><tr><td role="">60</td><td role="">Kurdish</td></tr><tr><td role="">61</td><td role="">Kashmiri</td></tr><tr><td role="">62</td><td role="">Sindhi</td></tr><tr><td role="">63</td><td role="">Tibetan</td></tr><tr><td role="">64</td><td role="">Nepali</td></tr><tr><td role="">65</td><td role="">Sanskrit</td></tr><tr><td role="">66</td><td role="">Marathi</td></tr><tr><td role="">67</td><td role="">Bengali</td></tr><tr><td role="">68</td><td role="">Assamese</td></tr><tr><td role="">69</td><td role="">Gujarati</td></tr><tr><td role="">70</td><td role="">Punjabi</td></tr><tr><td role="">71</td><td role="">Oriya</td></tr><tr><td role="">72</td><td role="">Malayalam</td></tr><tr><td role="">73</td><td role="">Kannada</td></tr><tr><td role="">74</td><td role="">Tamil</td></tr><tr><td role="">75</td><td role="">Telugu </td></tr><tr><td role="">76</td><td role="">Sinhalese </td></tr><tr><td role="">77</td><td role="">Burmese </td></tr><tr><td role="">78</td><td role="">Khmer </td></tr><tr><td role="">79</td><td role="">Lao </td></tr><tr><td role="">80</td><td role="">Vietnamese </td></tr><tr><td role="">81</td><td role="">Indonesian </td></tr><tr><td role="">82</td><td role="">Tagalong </td></tr><tr><td role="">83</td><td role="">Malay (Roman script) </td></tr><tr><td role="">84</td><td role="">Malay (Arabic script) </td></tr><tr><td role="">85</td><td role="">Amharic </td></tr><tr><td role="">86</td><td role="">Tigrinya </td></tr><tr><td role="">87</td><td role="">Galla </td></tr><tr><td role="">88</td><td role="">Somali </td></tr><tr><td role="">89</td><td role="">Swahili </td></tr><tr><td role="">90</td><td role="">Kinyarwanda/Ruanda </td></tr><tr><td role="">91</td><td role="">Rundi </td></tr><tr><td role="">92</td><td role="">Nyanja/Chewa </td></tr><tr><td role="">93</td><td role="">Malagasy </td></tr><tr><td role="">94</td><td role="">Esperanto </td></tr><tr><td role="">128</td><td role="">Welsh </td></tr><tr><td role="">129</td><td role="">Basque </td></tr><tr><td role="">130</td><td role="">Catalan </td></tr><tr><td role="">131</td><td role="">Latin </td></tr><tr><td role="">132</td><td role="">Quenchua </td></tr><tr><td role="">133</td><td role="">Guarani </td></tr><tr><td role="">134</td><td role="">Aymara </td></tr><tr><td role="">135</td><td role="">Tatar </td></tr><tr><td role="">136</td><td role="">Uighur </td></tr><tr><td role="">137</td><td role="">Dzongkha </td></tr><tr><td role="">138</td><td role="">Javanese (Roman script) </td></tr><tr><td role="">139</td><td role="">Sundanese (Roman script) </td></tr><tr><td role="">140</td><td role="">Galician </td></tr><tr><td role="">141</td><td role="">Afrikaans </td></tr><tr><td role="">142</td><td role="">Breton </td></tr><tr><td role="">143</td><td role="">Inuktitut [!!fixed] </td></tr><tr><td role="">144</td><td role="">Scottish Gaelic </td></tr><tr><td role="">145</td><td role="">Manx Gaelic </td></tr><tr><td role="">146</td><td role="">Irish Gaelic (with dot above) </td></tr><tr><td role="">147</td><td role="">Tongan </td></tr><tr><td role="">148</td><td role="">Greek (polytonic) </td></tr><tr><td role="">149</td><td role="">Greenlandic </td></tr><tr><td role="">150</td><td role="">Azerbaijani (Roman script) </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="name_enc2"></a><p class="title"><strong>Table 10.8. ISO specific encodings (platform ID=2)
            [Deprecated]</strong></p><div class="table-contents"><table role="" class="table" summary="ISO specific encodings (platform ID=2)&#10;            [Deprecated]" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Code</th><th role="">ISO encoding</th></tr></thead><tbody><tr><td role="">0</td><td role="">7-bit ASCII</td></tr><tr><td role="">1</td><td role="">ISO 10646</td></tr><tr><td role="">2</td><td role="">ISO 8859-1</td></tr></tbody></table></div></div><br class="table-break"/><p role="">There are no ISO-specific language IDs.</p><div class="table"><a name="name_enc4"></a><p class="title"><strong>Table 10.9. Custom platform-specific encoding IDs (platform
            ID=4)</strong></p><div class="table-contents"><table role="" class="table" summary="Custom platform-specific encoding IDs (platform&#10;            ID=4)" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">ID</th><th role="">Custom encoding</th></tr></thead><tbody><tr><td role="">0-255</td><td role="">OTF Windows NT compatibility mapping</td></tr></tbody></table></div></div><br class="table-break"/><p role="">In cases where a custom platform <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          is present for OTF Windows NT compatibility, the encoding ID
          must be set to the Windows charset value (in the range 0 to
          255, inclusive) present in the .PFM file of the original
          Type 1 font. See the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table for more
          details on the <a role="" class="link" href="chapter.cmap.html#cmap_cust" title="OTF Windows NT compatibility mapping">OTF Windows NT
            compatibility cmap</a>.</p><p role="">There are currently no language IDs defined for the
          Custom platform. This means that it can be used for
          encodings in the <a role="" class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> table but not for
          strings in the <a role="" class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table.</p><p role="">Name IDs</p><p role="">The following name IDs are pre-defined, and they apply to
          all platforms unless indicated otherwise. Name IDs 21 to
          255, inclusive, are reserved for future standard names. Name
          IDs 256 to 32767, inclusive, are reserved for font-specific
          names such as those referenced by a font's layout feature.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3pc"/><col width="27pc"/></colgroup><thead><tr><th role="">Code</th><th role="">Meaning</th></tr></thead><tbody><tr><td role="">0</td><td role="">Copyright notice.</td></tr><tr><td role="">1</td><td role="">Font Family nam. Up to four
		  fonts can share the Font Family name, forming a font
		  style linking group (regular, italic, bold, bold
		  italic - as defined by OS/2.fsSelection bit
		  settings).</td></tr><tr><td role="">2</td><td role="">Font Subfamily name. The Font
		  Subfamily name distiguishes the font in a group with
		  the same Font Family name (name ID 1). This is
		  assumed to address style (italic, oblique) and !
		  weight (light, bold, black, etc.). A font with no
		  particular differences in weight or style (e.g.
		  medium weight, not italic and fsSelection bit 6 set)
		  should have the string "Regular" stored in this
		  position.</td></tr><tr><td role="">3</td><td role="">Unique font identifier</td></tr><tr><td role="">4</td><td role="">Full font name; this should be
		  a combination of strings 1 and 2. Exception: if the
		  font is "Regular" as indicated in string 2, then use
		  only the family name contained in string 1. An
		  exception to the above definition of Full font name
		  is for Microsoft platform strings for CFF OpenType
		  fonts: in this case, the Full font name string must
		  be identical to the PostScript FontName in the CFF
		  Name INDEX. </td></tr><tr><td role="">5</td><td role="">Version string. Should begin
		  with the syntax 'Version &lt;number&gt;.&lt;number&gt;'
		  (upper case, lower case, or mixed, with a space
		  between "Version" and the number).  The string must
		  contain a version number of the following form: one
		  or more digits (0-9) of value less than 65,535,
		  followed by a period, followed by one or more digits
		  of value less than 65,535. Any character other than
		  a digit will terminate the minor number. A character
		  such as ";" is helpful to separate different pieces
		  of version information. The first such match in
		  the string can be used by installation software to
		  compare font versions. Note that some installers may
		  require the string to start with "Version ",
		  followed by a version number as above.</td></tr><tr><td role="">6</td><td role="">
		  <p role="">Postscript name for the font; Name ID 6
                    specifies a string which is used to invoke a
                    PostScript language font that corresponds to this
                    OpenType font. If no name ID 6 is present, then
                    there is no defined method for invoking this font
                    on a PostScript interpreter.</p> <p role="">OpenType
                    fonts which include a name with name ID of 6 shall
                    include these two names with name ID 6, and
                    characteristics as follows:</p> <p role="">a.
                    Platform: 1 [Macintosh]; Platform-specific
                    encoding: 0 [Roman]; Language: 0 [English].</p>
                  <p role="">b Platform: 3 [Microsoft]; Platform-specific
                    encoding: 1 [Unicode]; Language: 0x409 [English
                    (American)]. </p> <p role="">Names with name ID 6
                    other than the above two, if present, must be
                    ignored.</p> <p role="">When translated to ASCII,
                    these two name strings must be identical; no
                    longer than 63 characters; and restricted to the
                    printable ASCII subset, codes 33 through 126,
                    except for the 10 characters: '[', ']', '(', ')',
                    '{', '}', '&lt;', '&gt;', '/', '%'.</p> <p role="">In
                    CFF OpenType fonts, these two name strings, when
                    translated to ASCII, must also be identical to the
                    font name as stored in the CFF's Name
                    INDEX.</p> <p role="">The term "PostScript Name"
                    here means a string identical to the two identical
                    name ID 6 strings described above.</p>
                  <p role="">Depending on the particular font format that
                    PostScript language font uses, the invocation
                    method for the PostScript font differs, and the
                    semantics of the resulting PostScript language
                    font differ. The method used to invoke this font
                    depends on the presence of name ID 20.</p>
                  <p role="">If a name ID 20 is present in this font, then
                    the default assumption should be that the
                    PostScript Name defined by name ID 6 should be
                    used with the "composefont" invocation. This
                    PostScript Name is then the name of a PostScript
                    language CIDFont resource which corresponds to the
                    glyphs of the OpenType font. This name is valid to
                    pass, with an appropriate PostScript language CMap
                    reference, and an instance name, to the PostScript
                    language "composefont" operator.</p> <p role="">If
                    no name ID 20 is present in this font, then the
                    default assumption should be that the PostScript
                    Name defined by name ID 6 should be used with the
                    "findfont" invocation, for locating the font in
                    the context of a PostScript interpreter. This
                    PostScript Name is then the name of a PostScript
                    language Font resource which corresponds to the
                    glyphs of the OpenType font. This name is valid to
                    pass to the PostScript language "findfont"
                    operator. Note that this does
                    <span role="" class="emphasis"><em>not</em></span> necessarily imply that
                    the resulting font dictionary accepts an /Encoding
                    array, such as when the font referenced is a Type
                    0 PostScript font.</p> <p role="">Note that this
                    specification applies only to data fork OpenType
                    fonts. Macintosh resource-fork TrueType and other
                    Macintosh sfnt-wrapped fonts supply the PostScript
                    font name to be used with the "findfont"
                    invocation, in order to invoke the font in a
                    PostScript interpreter, in the FOND resource
                    style-mapping table.</p> <p role="">Developers may
                    choose to ignore the default usage when
                    appropriate. For example, PostScript printers
                    whose version is earlier than 2015 cannot process
                    CID font resources, and a CJK OpenType/CFF-CID
                    font can be downloaded only as a set of Type 1
                    PostScript fonts. Legacy CJK TrueType fonts, which
                    do not have a name ID 20, may still be most
                    effectively downloaded as a CID font resource.
                    Definition of the full set of situations in which
                    the defaults should not be followed is outside the
                    scope of this document.</p>
                </td></tr><tr><td role="">7</td><td role="">Trademark; this is used to
                save any trademark notice/information for this
                font. Such information should be based on legal
                advice. This is <span role="" class="emphasis"><em>distinctly</em></span>
                separate from the copyright. </td></tr><tr><td role="">8</td><td role="">Manufacturer Name.</td></tr><tr><td role="">9</td><td role="">Designer; name of the designer of the
                  typeface.</td></tr><tr><td role="">10</td><td role="">Description; description of the typeface. Can
                  contain revision information, usage recommendations,
                  history, features, etc.</td></tr><tr><td role="">11</td><td role="">URL Vendor; URL of font vendor (with protocol,
                  e.g., http://, ftp://). If a unique serial number is
                  embedded in the URL, it can be used to register the
                  font.</td></tr><tr><td role="">12</td><td role="">URL Designer; URL of typeface designer (with
                  protocol, e.g., http://, ftp://).</td></tr><tr><td role="">13</td><td role="">License Description; description of how the
                  font may be legally used, or different example
                  scenarios for licensed use. This field should be
                  written in plain language, not legalese.</td></tr><tr><td role="">14</td><td role="">License Info URL; URL where additional
                  licensing information can be found.</td></tr><tr><td role="">15</td><td role="">Reserved; Set to zero.</td></tr><tr><td role="">16</td><td role="">For historical reasons, font
		  families have contained a maximum of four styles,
		  but font designers may group more than four fonts to
		  a single family.  The Preferred Family allows font
		  designers to include the preferred family grouping
		  which contains more than four fonts. This ID is only
		  present if it is different from ID 1. </td></tr><tr><td role="">17</td><td role="">Preferred Subfamily allows
		  font designers to include the preferred subfamily
		  grouping that is more descriptive than ID 2. This ID
		  is only present if it is different from ID 2 and
		  must be unique for the the Preferred Family.</td></tr><tr><td role="">18</td><td role="">Compatible Full (Macintosh only); On the
                  Macintosh, the menu name is constructed using the
                  FOND resource. This usually matches the Full Name.
                  If you want the name of the font to appear
                  differently than the Full Name, you can insert the
                  Compatible Full Name in ID 18. </td></tr><tr><td role="">19</td><td role="">Sample text; This can be the font name, or any
                  other text that the designer thinks is the best
                  sample to display the font in.</td></tr><tr><td role="">20</td><td role=""><p role="">PostScript CID findfont name; Its
                    presence in a font means that the nameID 6 holds a
                    PostScript font name that is meant to be used with
                    the "composefont" invocation in order to invoke
                    the font in a PostScript interpreter. See the
                    definition of name ID 6.</p> <p role="">The value
                    held in the name ID 20 string is interpreted as a
                    PostScript font name that is meant to be used with
                    the "findfont" invocation, in order to invoke the
                    font in a PostScript interpreter.</p> <p role="">If
                    the name ID 20 is present in a font, there must be
                    one name ID 20 record for every Macintosh platform
                    cmap subtable in that font. A particular name ID
                    20 record is associated with the encoding
                    specified by the matching cmap subtable. A name ID
                    20 record is matched to a cmap subtable when they
                    have the same platform and platform-specific
                    encoding IDs, and corresponding language/version
                    IDs. Name ID 20 records are meant to be used only
                    with Macintosh cmap subtables. The version field
                    for a cmap subtable is one more than the language
                    ID value for the corresponding name ID 20 record,
                    with the exception of the cmap subtable version
                    field 0. This version field, meaning "not
                    language-specific", corresponds to the language ID
                    value 0xFFFF, or decimal 65535, for the
                    corresponding name ID 20 record.</p> <p role="">When
                    translated to ASCII, this name string must be
                    restricted to the printable ASCII subset, codes 33
                    through 126, except for the 10 characters: '[',
                    ']', '(', ')', '{', '}', '&lt;', '&gt;', '/',
                    '%'.</p> <p role="">Note that this specification
                    applies only to data fork OpenType fonts.
                    Macintosh resource-fork TrueType and other
                    Macintosh sfnt-wrapped fonts supply the PostScript
                    font name to be used with the "findfont"
                    invocation, in order to invoke the font in a
                    PostScript interpreter, in the FOND resource
                    style-mapping table.</p> <p role="">Note that a
                    particular Name ID 20 string always corresponds to
                    a particular Macintosh cmap subtable. However,
                    some host OpenType/TTF fonts also contain a post
                    table, format 4, which provides a mapping from
                    glyph ID to encoding value, and also corresponds
                    to a particular Macintosh cmap subtable.
                    Unfortunately, the <a role="" class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table
                    format 4 contains no provision for identifying
                    which Macintosh cmap subtable it matches, nor for
                    providing more than one mapping. Host fonts which
                    contain a <a role="" class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table format 4,
                    should also contain only a single Macintosh cmap
                    subtable, and a single Name ID 20 string. In the
                    case where there is more than one Macintosh cmap
                    subtable and more than one Name ID 20 string,
                    there is no definition of which one matches the
                    <a role="" class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table format
                    4.</p></td></tr></tbody></table></div><p role="">Note that while both Apple and Microsoft support the
          same set of name strings, the interpretations may be
          somewhat different. But since name strings are stored by
          platform, encoding and language (placing separate strings in
          for both Apple and MS platforms), this should not present a
          problem.</p><p role="">The key information for this table for MS fonts relates
          to the use of strings 1, 2 and 4. To better help understand,
          here are some examples of name usage, weight class and style
          flags:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th role="">Font</th><th role="">Name ID 1</th><th role="">Name ID 2</th><th role="">Name ID 4</th><th role="">Name ID 16</th><th role="">Name ID 17</th></tr></thead><tbody><tr><td role="">Arial Narrow</td><td role="">Arial Narrow</td><td role="">Regular</td><td role="">Arial Narrow</td><td role="">Arial</td><td role="">Narrow</td></tr><tr><td role="">Arial Narrow Italic</td><td role="">Arial Narrow</td><td role="">Italic</td><td role="">Arial Narrow Italic</td><td role="">Arial</td><td role="">Narrow Italic</td></tr><tr><td role="">Arial Narrow Bold</td><td role="">Arial Narrow</td><td role="">Bold</td><td role="">Arial Narrow Bold</td><td role="">Arial</td><td role="">Narrow Bold</td></tr><tr><td role="">Arial Narrow Bold Italic</td><td role="">Arial Narrow</td><td role="">Bold Italic</td><td role="">Arial Narrow Bold Italic</td><td role="">Arial</td><td role="">Narrow Bold Italic</td></tr><tr><td role="">Arial</td><td role="">Arial</td><td role="">Regular</td><td role="">Arial</td><td role="">Arial</td></tr><tr><td role="">Arial Italic</td><td role="">Arial</td><td role="">Italic</td><td role="">Arial Italic</td><td role="">Arial</td><td role="">Italic</td></tr><tr><td role="">Arial Bold</td><td role="">Arial</td><td role="">Bold</td><td role="">Arial Bold</td><td role="">Arial</td><td role="">Bold</td></tr><tr><td role="">Arial Bold Italic</td><td role="">Arial</td><td role="">Bold Italic</td><td role="">Arial Bold Italic</td><td role="">Arial</td><td role="">Bold Italic</td></tr><tr><td role="">Arial Black</td><td role="">Arial Black</td><td role="">Regular</td><td role="">Arial Black</td><td role="">Arial</td><td role="">Black</td></tr><tr><td role="">Arial Black Italic</td><td role="">Arial Black</td><td role="">Italic</td><td role="">Arial Black Italic</td><td role="">Arial</td><td role="">Black Italic</td></tr></tbody></table></div><p role="">In addition to name strings, OS/2.usWeightClass,
	  OS/2.usWidthClass, OS/2.fsSelection style bits, and
	  head.macStyle bits are shown. These settings allow the fonts
	  to fit together into a single family of varying weight and
	  compression/expansion.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/><col/><col/><col/><col/></colgroup><thead><tr><th role="">Font</th><th role="">OS/2 usWeightClass</th><th role="">OS/2 usWidthClass</th><th role="">OS/2 fsSelection Italic</th><th role="">OS/2 fsSelection Bold</th><th role="">OS/2 fsSelection Regular</th><th role="">head macStyle Bold</th><th role="">head macStyle Italic</th><th role="">head macStyle Condensed</th><th role="">head macStyle Extended</th></tr></thead><tbody><tr><td role="">Arial Narrow</td><td role="">400</td><td role="">3</td><td role=""> </td><td role=""> </td><td role="">x</td><td role=""> </td><td role=""> </td><td role="">x</td><td role=""> </td></tr><tr><td role="">Arial Narrow Italic</td><td role="">400</td><td role="">3</td><td role="">x</td><td role=""> </td><td role=""> </td><td role=""> </td><td role="">x</td><td role="">x</td><td role=""> </td></tr><tr><td role="">Arial Narrow Bold</td><td role="">700</td><td role="">3</td><td role=""> </td><td role="">x</td><td role=""> </td><td role="">x</td><td role=""> </td><td role="">x</td><td role=""> </td></tr><tr><td role="">Arial Narrow Bold Italic</td><td role="">700</td><td role="">3</td><td role="">x</td><td role="">x</td><td role=""> </td><td role="">x</td><td role="">x</td><td role="">x</td><td role=""> </td></tr><tr><td role="">Arial</td><td role="">400</td><td role="">5</td><td role=""> </td><td role=""> </td><td role="">x</td><td role=""> </td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">Arial Italic</td><td role="">400</td><td role="">5</td><td role="">x</td><td role=""> </td><td role=""> </td><td role=""> </td><td role="">x</td><td role=""> </td><td role=""> </td></tr><tr><td role="">Arial Bold</td><td role="">700</td><td role="">5</td><td role=""> </td><td role="">x</td><td role=""> </td><td role="">x</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">Arial Bold Italic</td><td role="">700</td><td role="">5</td><td role="">x</td><td role="">x</td><td role=""> </td><td role="">x</td><td role="">x</td><td role=""> </td><td role=""> </td></tr><tr><td role="">Arial Black</td><td role="">900</td><td role="">5</td><td role=""> </td><td role="">x</td><td role=""> </td><td role="">x</td><td role=""> </td><td role=""> </td><td role=""> </td></tr><tr><td role="">Arial Black Italic</td><td role="">900</td><td role="">5</td><td role="">x</td><td role="">x</td><td role=""> </td><td role="">x</td><td role="">x</td><td role=""> </td><td role=""> </td></tr></tbody></table></div><p role="">Note that OS/2 and Windows both require that all name
          strings be defined in Unicode. Thus all 'name' table strings
          for platform ID = 3 (Microsoft) will require two bytes per
          character. Macintosh fonts require single byte
          strings.</p><p role="">Examples of how these strings might be defined:</p><p role="">0. The copyright string from the font vendor. <span role="" class="emphasis"><em>©
          Copyright the Monotype Corporation plc, 1990</em></span></p><p role="">1. The name the user sees. <span role="" class="emphasis"><em>Times New
            Roman</em></span></p><p role="">2. The name of the style. <span role="" class="emphasis"><em>Bold</em></span></p><p role="">3. A unique identifier that applications can store to
          identify the font being used. Monotype: <span role="" class="emphasis"><em>Times New Roman
          Bold:1990</em></span></p><p role="">4. The complete, hopefully unique, human readable name
          of the font. This name is used by Windows. <span role="" class="emphasis"><em>Times
          New Roman Bold</em></span>. (If this were the Microsoft
          platform string for a CFF OpenType font, then the value
          would be <span role="" class="emphasis"><em>TimesNewRoman-Bold</em></span>, as
          described in the definition of name ID 4 above.)</p><p role="">5. Release and version information from the font vendor.
          <span role="" class="emphasis"><em>Version 1.00 June 1, 1990, initial release</em></span></p><p role="">6. The name the font will be known by on a PostScript
          printer. <span role="" class="emphasis"><em>TimesNewRoman-Bold</em></span></p><p role="">7. Trademark string. <span role="" class="emphasis"><em>Times New Roman is a registered
          trademark of the Monotype Corporation.</em></span></p><p role="">8. Manufacturer. <span role="" class="emphasis"><em>Monotype Corporation
        plc</em></span></p><p role="">9. Designer. <span role="" class="emphasis"><em>Stanley Morison</em></span></p><p role="">10. Description. <span role="" class="emphasis"><em>Designed in 1932 for the Times of
          London newspaper. Excellent readability and a narrow overall
          width, allowing more words per line than most fonts.</em></span></p><p role="">11. URL of Vendor.
          <span role="" class="emphasis"><em>http://www.monotype.com</em></span></p><p role="">12. URL of Designer.
          <span role="" class="emphasis"><em>http://www.monotype.com</em></span></p><p role="">13. License Description. <span role="" class="emphasis"><em>This font may be installed on
          all of your machines and printers, but you may not sell or
          give these fonts to anyone else.</em></span></p><p role="">14. License Info URL.
          <span role="" class="emphasis"><em>http://www.monotype.com/license/</em></span></p><p role="">15. Reserved. Set to zero.</p><p role="">16. Preferred Family. No name string
          present, since it is the same as name ID 1 (Font Family
          name).</p><p role="">17. Preferred Subfamily. No name string
          present, since it is the same as name ID 2 (Font Subfamily
          name).</p><p role="">18. Compatible Full (Macintosh only). No name string
          present, since it is the same as name ID 4 (Full
          name).</p><p role="">19. Sample text. <span role="" class="emphasis"><em>The quick brown fox jumps over the lazy
          dog.</em></span></p><p role="">20. PostScript CID findfont name. No name string
          present. Thus, the PostScript Name defined by name ID 6
          should be used with the "findfont" invocation for locating
          the font in the context of a PostScript interpreter.</p><p role="">The following is an example of only name IDs 6 and 20 in
          the CFF OpenType Japanese font Kozuka Mincho Std Regular
          (other name IDs are also present in this font):</p><p role="">6. PostScript name:
          <span role="" class="emphasis"><em>KozMinStd-Regular</em></span>. Since a name ID 20
          is present in the font (see below), then the PostScript name
          defined by name ID 6 should be used with the "composefont"
          invocation for locating the font in the context of a
          PostScript interpreter.</p><p role="">20. PostScript CID findfont name:
          <span role="" class="emphasis"><em>KozMinStd-Regular-83pv-RKSJ-H</em></span>, in a
          name record of Platform 1 [Macintosh], Platform-specific
          script 1 [Japanese], Language: 0xFFFF [English]. This name
          string is a PostScript name that should be used with the
          "findfont" invocation for locating the font in the context
          of a PostScript interpreter, and is associated with the
          encoding specified by the following cmap subtable, which
          must be present in the font: Platform: 1 [Macintosh];
          Platform-specific encoding: 1 [Japanese]; Language: 0 [not
          language-specific].</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.10.1.2"></a>Annotation</h3></div></div></div><p role="">In the example, string 19 is not set in italic like the
        other strings.</p></div></div></div>