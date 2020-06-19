<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.name"></a>Chapter 9. name - Naming Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm516889360128"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.10.1.1"></a>Specification</h4></div></div></div><p>The naming table allows multilingual strings to be
          associated with the CommonType font file. These strings can
          represent copyright notices, font names, family names, style
          names, and so on. To keep this table short, the font
          manufacturer may wish to make a limited set of entries in
          some small set of languages; later, the font can be
          "localized" and the strings translated or added. Other parts
          of the CommonType font file that require these strings can
          then refer to them simply by their index number. Clients
          that need a particular string can look it up by its platform
          ID, character encoding ID, language ID and name ID. Note
          that some platforms may require single byte character
          strings, while others may require double byte
          strings.</p><p>For historical reasons, some applications which install
          fonts perform version control using Macintosh platform
          (platform ID 1) strings from the <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a>
          table. Because of this, we strongly recommend that the
          <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a> table of all fonts include Macintosh
          platform strings and that the syntax of the version number
          (name id 5) follows the guidelines given in this
          document.</p><p>The Naming Table is organized as follows:</p><div class="table"><a name="idm516889354608"></a><p class="title"><strong>Table 9.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format selector (=0).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>count</td><td>Number of name records.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>stringOffset</td><td>Offset to start of string storage (from start
                  of table).</td><td class="auto-generated"> </td></tr><tr><td>n NameRecords</td><td>nameRecord [count]</td><td>The name records where count is the number of
	      records.</td><td class="auto-generated"> </td></tr><tr><td>(Variable)</td><td> </td><td>Storage for the actual string data.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each NameRecord looks like this:</p><div class="table"><a name="idm516889344800"></a><p class="title"><strong>Table 9.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>platformID</td><td>Platform ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>encodingID</td><td>Platform-specific encoding ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>languageID</td><td>Language ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>nameID</td><td>Name ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>String length (in bytes).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset</td><td>String offset from start of storage area (in
                  bytes).</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Following are the descriptions of the four kinds of ID.
          Note that the specific values listed here are the only ones
          that are predefined; new ones may be added by registry with
          Apple Developer Technical Support. Similar to the character
          encoding table, the NameRecords is sorted by platform ID,
          then platform-specific ID, then language ID, and then by
          name ID.</p><div class="table"><a name="idm516889333104"></a><p class="title"><strong>Table 9.3. Platform IDs, Platform-specific encoding IDs and
            Language IDs</strong></p><div class="table-contents"><table class="table" summary="Platform IDs, Platform-specific encoding IDs and&#10;            Language IDs" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>PlatformID</th><th>Platform name</th><th>Platform-specific encoding IDs</th><th>Language IDs</th></tr></thead><tbody><tr><td>0</td><td>Unicode</td><td>
                <a class="link" href="chapter.name.html#name_enc0" title="Table 9.4. Unicode platform-specific encoding IDs (platform ID = 0)">Various</a>
              </td><td>None</td></tr><tr><td>1</td><td>Macintosh</td><td>
                <a class="link" href="chapter.name.html#name_enc1" title="Table 9.6. Macintosh platform-specific encoding IDs (script manager codes), (platform ID = 1)">Script manager
                    code</a>
              </td><td>
                <a class="link" href="chapter.name.html#name_lang1" title="Table 9.7. Macintosh language IDs (platform ID = 1)">Various</a>
              </td></tr><tr><td>2</td><td>ISO [deprecated]</td><td>
                <a class="link" href="chapter.name.html#name_enc2" title="Table 9.8. ISO specific encodings (platform ID=2) [Deprecated]">ISO
                    encoding</a> [deprecated]</td><td>None</td></tr><tr><td>3</td><td>Microsoft</td><td>
                <a class="link" href="chapter.name.html#name_enc3" title="Table 9.5. Microsoft platform-specific encoding IDs (platform ID= 3)">Microsoft
                    encoding</a>
              </td><td>
                <a class="link" href="chapter.name.html#name_lang3">Various</a>
              </td></tr><tr><td>4</td><td>Custom</td><td>
                <a class="link" href="chapter.name.html#name_enc4" title="Table 9.9. Custom platform-specific encoding IDs (platform ID=4)">Custom</a>
              </td><td>None</td></tr></tbody></table></div></div><br class="table-break"/><p>Note that platform ID 2 (ISO) has been deprecated as of
          CommonType Specification v1.3. It was intended to represent
          ISO/IEC 10646, as opposed to Unicode; both standards have
          identical character code assignments.</p><p>PlatformID values 240 through 255 are reserved for
          user-defined platforms. The DTS registry will never assign
          these values to a registered platform.</p><div class="table"><a name="name_enc0"></a><p class="title"><strong>Table 9.4. Unicode platform-specific encoding IDs (platform ID =
            0)</strong></p><div class="table-contents"><table class="table" summary="Unicode platform-specific encoding IDs (platform ID =&#10;            0)" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>EncodingID</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>Unicode 1.0 semantics</td></tr><tr><td>1</td><td>Unicode 1.1 semantics</td></tr><tr><td>2</td><td>ISO 10646:1993 semantics</td></tr><tr><td>3</td><td>Unicode 2.0 and onwards semantics, Unicode BMP only</td></tr><tr><td>4</td><td>Unicode 2.0 and onwards semantics, Unicode
		  full repertoire</td></tr><tr><td>5</td><td>Unicode Variation Sequences</td></tr></tbody></table></div></div><br class="table-break"/><p>A new encoding ID for the Unicode platform will be
          assigned if a new version of Unicode moves characters, in
          order to properly specify character code semantics. The
          distinction between Unicode platform-specific encoding IDs 1
          and 2 is for historical reasons only; Unicode 1.1 is in fact
          identical in repertoire and encoding to ISO 10646:1993
          (before any amendments).</p><p>Unicode platform encoding ID 5 can be used for encodings
        in the 'cmap' table but not for strings in the 'name' table.</p><p>There are currently no language IDs defined for the
          Unicode platform. This means that it can be used for
          encodings in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table but not for
          strings in the <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a> table.</p><div class="table"><a name="name_enc3"></a><p class="title"><strong>Table 9.5. Microsoft platform-specific encoding IDs (platform
            ID= 3)</strong></p><div class="table-contents"><table class="table" summary="Microsoft platform-specific encoding IDs (platform&#10;            ID= 3)" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Platform ID</th><th>Encoding ID</th><th>Description</th></tr></thead><tbody><tr><td>3</td><td>0</td><td>Symbol</td></tr><tr><td>3</td><td>1</td><td>Unicode BMP only</td></tr><tr><td>3</td><td>2</td><td>ShiftJIS</td></tr><tr><td>3</td><td>3</td><td>PRC</td></tr><tr><td>3</td><td>4</td><td>Big5</td></tr><tr><td>3</td><td>5</td><td>Wansung</td></tr><tr><td>3</td><td>6</td><td>Johab</td></tr><tr><td>3</td><td>7</td><td>Reserved</td></tr><tr><td>3</td><td>8</td><td>Reserved</td></tr><tr><td>3</td><td>9</td><td>Reserved</td></tr><tr><td>3</td><td>10</td><td>Unicode full repertoire</td></tr></tbody></table></div></div><br class="table-break"/><p>When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1. When
          building a symbol font for Windows, the platform ID should
          be 3 and the encoding ID should be 0. When building a font
          that will be used on the Macintosh, the platform ID should
          be 1 and the encoding ID should be 0.</p><p>Microsoft Language IDs (platform ID = 3)</p><p>The language ID (LCID in the table below) refers to a
          value which identifies the language in which a particular
          string is written. Fifty of the language ID's assigned by
          Microsoft are listed below, along with their corresponding
          code pages. There are 85 additional language ID's assigned.
          corresponding code pages. There are 85 additional language
          ID's assigned.  For a full list, please see the <a class="ulink" href="http://www.microsoft.com/globaldev/reference/loclanghome.asp" target="_top">Microsoft
          Global Development</a> site or <a class="ulink" href="http://support.microsoft.com/default.aspx?scid=kb;EN-US;q224804" target="_top">Knowledge
          Base article Q224804</a>.</p><div class="informaltable"><a name="name_lang3"></a><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th>Primary Language</th><th>Locale Name</th><th>LCID</th><th>Win CP</th><th>OEM CP</th></tr></thead><tbody><tr><td>Albanian</td><td>Albania</td><td>(041c; SQI)</td><td> </td><td> </td></tr><tr><td>Basque</td><td>Basque</td><td>(042D; EUQ)</td><td>1252</td><td>850</td></tr><tr><td>Byelorussian</td><td>Byelorussia</td><td>(0423, BEL)</td><td>1251</td><td>866</td></tr><tr><td>Bulgarian</td><td>Bulgaria</td><td>(0402, BGR)</td><td>1251</td><td>866</td></tr><tr><td>Catalan</td><td>Catalan</td><td>(0403; CAT)</td><td>1252</td><td>850</td></tr><tr><td>Croatian</td><td>Croatian</td><td>(041a, SHL)</td><td>1250</td><td>852</td></tr><tr><td>Czech</td><td>Czech</td><td>(0405; CSY)</td><td>1250</td><td>852</td></tr><tr><td>Danish</td><td>Danish</td><td>(0406; DAN)</td><td>1252</td><td>865</td></tr><tr><td>Dutch (2):</td><td>Dutch (Standard)</td><td>(0413; NLD)</td><td>1252</td><td>850</td></tr><tr><td>Dutch (2):</td><td>Belgian (Flemish)</td><td>(0813; NLB)</td><td>1252</td><td>850</td></tr><tr><td>English (6):</td><td>American</td><td>(0409; ENU)</td><td>1252</td><td>437</td></tr><tr><td>English (6):</td><td>British</td><td>(0809; ENG)</td><td>1252</td><td>850</td></tr><tr><td>English (6):</td><td>Australian</td><td>(0c09; ENA)</td><td>1252</td><td>850</td></tr><tr><td>English (6):</td><td>Canadian</td><td>(1009; ENC)</td><td>1252</td><td>850</td></tr><tr><td>English (6):</td><td>New Zealand</td><td>(1409; ENZ)</td><td>1252</td><td>850</td></tr><tr><td>English (6):</td><td>Ireland</td><td>(1809; ENI)</td><td>1252</td><td>850</td></tr><tr><td>Estonian</td><td>Estonia</td><td>(0425, ETI)</td><td>1257</td><td>775</td></tr><tr><td>Finnish</td><td>Finnish</td><td>(040b; FIN)</td><td>1252</td><td>850</td></tr><tr><td>French</td><td>French (Standard)</td><td>(040c; FRA)</td><td>1252</td><td>850</td></tr><tr><td>French</td><td>Belgian</td><td>(080c; FRB)</td><td>1252</td><td>850</td></tr><tr><td>French</td><td>Canadian</td><td>(0c0c; FRC)</td><td>1252</td><td>850</td></tr><tr><td>French</td><td>Swiss</td><td>(100c; FRS)</td><td>1252</td><td>850</td></tr><tr><td>French</td><td>Luxembourg</td><td>(140c; FRL)</td><td>1252</td><td>850</td></tr><tr><td>German</td><td>German (Standard)</td><td>(0407; DEU)</td><td>1252</td><td>850</td></tr><tr><td>German</td><td>Swiss</td><td>(0807; DES)</td><td>1252</td><td>850</td></tr><tr><td>German</td><td>Austrian</td><td>(0c07; DEA)</td><td>1252</td><td>850</td></tr><tr><td>German</td><td>Luxembourg</td><td>(1007; DEL)</td><td>1252</td><td>850</td></tr><tr><td>German</td><td>Liechtenstein</td><td>(1407; DEC)</td><td>1252</td><td>850</td></tr><tr><td>Greek</td><td>Greek</td><td>(0408; ELL)</td><td>1253</td><td>737 or 869<a href="#ftn.idm516889202416" class="footnote" id="idm516889202416"><sup class="footnote">[a]</sup></a>
              </td></tr><tr><td>Hungarian</td><td>Hungarian</td><td>(040e; HUN)</td><td>1250</td><td>852</td></tr><tr><td>Icelandic</td><td>Icelandic</td><td>(040F; ISL)</td><td>1252</td><td>850</td></tr><tr><td>Italian (2):</td><td>Italian (Standard)</td><td>(0410; ITA)</td><td>1252</td><td>850</td></tr><tr><td>Italian (2):</td><td>Swiss</td><td>(0810; ITS)</td><td>1252</td><td>850</td></tr><tr><td>Latvian</td><td>Latvia</td><td>(0426, LVI)</td><td>1257</td><td>775</td></tr><tr><td>Lithuanian</td><td>Lithuania</td><td>(0427, LTH)</td><td>1257</td><td>775</td></tr><tr><td>Norwegian (2):</td><td>Norwegian (Bokmal)</td><td>(0414; NOR)</td><td>1252</td><td>850</td></tr><tr><td>Norwegian (2):</td><td>Norwegian (Nynorsk)</td><td>(0814; NON)</td><td>1252</td><td>850</td></tr><tr><td>Polish</td><td>Polish</td><td>(0415; PLK)</td><td>1250</td><td>852</td></tr><tr><td>Portuguese (2):</td><td>Portuguese (Brazilian)</td><td>(0416; PTB)</td><td>1252</td><td>850</td></tr><tr><td>Portuguese (2):</td><td>Portuguese (Standard)</td><td>(0816; PTG)</td><td>1252</td><td>850</td></tr><tr><td>Romanian (2):</td><td>Romania</td><td>(0418, ROM)</td><td>1250</td><td>852</td></tr><tr><td>Russian</td><td>Russian</td><td>(0419; RUS)</td><td>1251</td><td>866</td></tr><tr><td>Slovak</td><td>Slovak</td><td>(041b; SKY)</td><td>1250</td><td>852</td></tr><tr><td>Slovenian</td><td>Slovenia</td><td>(0424, SLV)</td><td>1250</td><td>852</td></tr><tr><td>Spanish (3):</td><td>Spanish (Traditional Sort)</td><td>(040a; ESP)</td><td>1252</td><td>850</td></tr><tr><td>Spanish (3):</td><td>Mexican</td><td>(080a; ESM)</td><td>1252</td><td>850</td></tr><tr><td>Spanish (3):</td><td>Spanish (Modern Sort)</td><td>(0c0a; ESN)</td><td>1252</td><td>850</td></tr><tr><td>Swedish</td><td>Swedish</td><td>(041D; SVE)</td><td>1252</td><td>850</td></tr><tr><td>Turkish</td><td>Turkish</td><td>(041f; TRK)</td><td>1254</td><td>857</td></tr><tr><td>Ukrainian</td><td>Ukraine</td><td>(0422, UKR)</td><td>1251</td><td>866 </td></tr></tbody><tbody class="footnotes"><tr><td colspan="5"><div id="ftn.idm516889202416" class="footnote"><p><a href="#idm516889202416" class="para"><sup class="para">[a] </sup></a>737 is default, but 869 (IBM Greek) will be
                      available at setup time through the selection of
                      a bogus Greek locale in Custom Setup.</p></div></td></tr></tbody></table></div><div class="table"><a name="name_enc1"></a><p class="title"><strong>Table 9.6. Macintosh platform-specific encoding IDs (script
            manager codes), (platform ID = 1)</strong></p><div class="table-contents"><table class="table" summary="Macintosh platform-specific encoding IDs (script&#10;            manager codes), (platform ID = 1)" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Code</th><th>Script</th></tr></thead><tbody><tr><td>0</td><td>Roman</td></tr><tr><td>1</td><td>Japanese</td></tr><tr><td>2</td><td>Chinese (Traditional)</td></tr><tr><td>3</td><td>Korean</td></tr><tr><td>4</td><td>Arabic</td></tr><tr><td>5</td><td>Hebrew</td></tr><tr><td>6</td><td>Greek</td></tr><tr><td>7</td><td>Russian</td></tr><tr><td>8</td><td>RSymbol</td></tr><tr><td>9</td><td>Devanagari</td></tr><tr><td>10</td><td>Gurmukhi</td></tr><tr><td>11</td><td>Gujarati</td></tr><tr><td>12</td><td>Oriya</td></tr><tr><td>13</td><td>Bengali</td></tr><tr><td>14</td><td>Tamil</td></tr><tr><td>15</td><td>Telugu</td></tr><tr><td>16</td><td>Kannada</td></tr><tr><td>17</td><td>Malayalam</td></tr><tr><td>18</td><td>Sinhalese</td></tr><tr><td>19</td><td>Burmese</td></tr><tr><td>20</td><td>Khmer</td></tr><tr><td>21</td><td>Thai</td></tr><tr><td>22</td><td>Laotian</td></tr><tr><td>23</td><td>Georgian</td></tr><tr><td>24</td><td>Armenian</td></tr><tr><td>25</td><td>Chinese (Simplified)</td></tr><tr><td>26</td><td>Tibetan</td></tr><tr><td>27</td><td>Mongolian</td></tr><tr><td>28</td><td>Geez</td></tr><tr><td>29</td><td>Slavic</td></tr><tr><td>30</td><td>Vietnamese</td></tr><tr><td>31</td><td>Sindhi</td></tr><tr><td>32</td><td>Uninterpreted</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="name_lang1"></a><p class="title"><strong>Table 9.7. Macintosh language IDs (platform ID = 1)</strong></p><div class="table-contents"><table class="table" summary="Macintosh language IDs (platform ID = 1)" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Code</th><th>Language</th></tr></thead><tbody><tr><td>0</td><td>English</td></tr><tr><td>1</td><td>French</td></tr><tr><td>2</td><td>German</td></tr><tr><td>3</td><td>Italian</td></tr><tr><td>4</td><td>Dutch</td></tr><tr><td>5</td><td>Swedish</td></tr><tr><td>6</td><td>Spanish</td></tr><tr><td>7</td><td>Danish</td></tr><tr><td>8</td><td>Portuguese</td></tr><tr><td>9</td><td>Norwegian</td></tr><tr><td>10</td><td>Hebrew</td></tr><tr><td>11</td><td>Japanese</td></tr><tr><td>12</td><td>Arabic</td></tr><tr><td>13</td><td>Finnish</td></tr><tr><td>14</td><td>Greek</td></tr><tr><td>15</td><td>Icelandic</td></tr><tr><td>16</td><td>Maltese</td></tr><tr><td>17</td><td>Turkish</td></tr><tr><td>18</td><td>Yugoslavian</td></tr><tr><td>19</td><td>Chinese (Traditional)</td></tr><tr><td>20</td><td>Urdu</td></tr><tr><td>21</td><td>Hindi</td></tr><tr><td>22</td><td>Thai</td></tr><tr><td>23</td><td>Korean</td></tr><tr><td>24</td><td>Lithuanian</td></tr><tr><td>25</td><td>Polish</td></tr><tr><td>26</td><td>Hungarian</td></tr><tr><td>27</td><td>Estonian</td></tr><tr><td>28</td><td>Latvian</td></tr><tr><td>29</td><td>Sami</td></tr><tr><td>30</td><td>Faroese</td></tr><tr><td>31</td><td>Farsi/Persian</td></tr><tr><td>32</td><td>Russian</td></tr><tr><td>33</td><td>Chinese (Simplified)</td></tr><tr><td>34</td><td>Flemish</td></tr><tr><td>35</td><td>Irish Gaelic</td></tr><tr><td>36</td><td>Albanian</td></tr><tr><td>37</td><td>Romanian</td></tr><tr><td>38</td><td>Czech</td></tr><tr><td>39</td><td>Slovak</td></tr><tr><td>40</td><td>Slovenian</td></tr><tr><td>41</td><td>Yiddish</td></tr><tr><td>42</td><td>Serbian</td></tr><tr><td>43</td><td>Macedonian</td></tr><tr><td>44</td><td>Bulgarian</td></tr><tr><td>45</td><td>Ukrainian</td></tr><tr><td>46</td><td>Byelorussian </td></tr><tr><td>47</td><td>Uzbek </td></tr><tr><td>48</td><td>Kazakh </td></tr><tr><td>49</td><td>Azerbaijani (Cyrillic script) </td></tr><tr><td>50</td><td>Azerbaijani (Arabic script) </td></tr><tr><td>51</td><td>Armenian </td></tr><tr><td>52</td><td>Georgian </td></tr><tr><td>53</td><td>Moldavian</td></tr><tr><td>54</td><td>Kirghiz</td></tr><tr><td>55</td><td>Tajiki</td></tr><tr><td>56</td><td>Turkmen</td></tr><tr><td>57</td><td>Mongolian (Mongolian script)</td></tr><tr><td>58</td><td>Mongolian (Cyrillic script)</td></tr><tr><td>59</td><td>Pashto</td></tr><tr><td>60</td><td>Kurdish</td></tr><tr><td>61</td><td>Kashmiri</td></tr><tr><td>62</td><td>Sindhi</td></tr><tr><td>63</td><td>Tibetan</td></tr><tr><td>64</td><td>Nepali</td></tr><tr><td>65</td><td>Sanskrit</td></tr><tr><td>66</td><td>Marathi</td></tr><tr><td>67</td><td>Bengali</td></tr><tr><td>68</td><td>Assamese</td></tr><tr><td>69</td><td>Gujarati</td></tr><tr><td>70</td><td>Punjabi</td></tr><tr><td>71</td><td>Oriya</td></tr><tr><td>72</td><td>Malayalam</td></tr><tr><td>73</td><td>Kannada</td></tr><tr><td>74</td><td>Tamil</td></tr><tr><td>75</td><td>Telugu </td></tr><tr><td>76</td><td>Sinhalese </td></tr><tr><td>77</td><td>Burmese </td></tr><tr><td>78</td><td>Khmer </td></tr><tr><td>79</td><td>Lao </td></tr><tr><td>80</td><td>Vietnamese </td></tr><tr><td>81</td><td>Indonesian </td></tr><tr><td>82</td><td>Tagalong </td></tr><tr><td>83</td><td>Malay (Roman script) </td></tr><tr><td>84</td><td>Malay (Arabic script) </td></tr><tr><td>85</td><td>Amharic </td></tr><tr><td>86</td><td>Tigrinya </td></tr><tr><td>87</td><td>Galla </td></tr><tr><td>88</td><td>Somali </td></tr><tr><td>89</td><td>Swahili </td></tr><tr><td>90</td><td>Kinyarwanda/Ruanda </td></tr><tr><td>91</td><td>Rundi </td></tr><tr><td>92</td><td>Nyanja/Chewa </td></tr><tr><td>93</td><td>Malagasy </td></tr><tr><td>94</td><td>Esperanto </td></tr><tr><td>128</td><td>Welsh </td></tr><tr><td>129</td><td>Basque </td></tr><tr><td>130</td><td>Catalan </td></tr><tr><td>131</td><td>Latin </td></tr><tr><td>132</td><td>Quenchua </td></tr><tr><td>133</td><td>Guarani </td></tr><tr><td>134</td><td>Aymara </td></tr><tr><td>135</td><td>Tatar </td></tr><tr><td>136</td><td>Uighur </td></tr><tr><td>137</td><td>Dzongkha </td></tr><tr><td>138</td><td>Javanese (Roman script) </td></tr><tr><td>139</td><td>Sundanese (Roman script) </td></tr><tr><td>140</td><td>Galician </td></tr><tr><td>141</td><td>Afrikaans </td></tr><tr><td>142</td><td>Breton </td></tr><tr><td>143</td><td>Inuktitut [!!fixed] </td></tr><tr><td>144</td><td>Scottish Gaelic </td></tr><tr><td>145</td><td>Manx Gaelic </td></tr><tr><td>146</td><td>Irish Gaelic (with dot above) </td></tr><tr><td>147</td><td>Tongan </td></tr><tr><td>148</td><td>Greek (polytonic) </td></tr><tr><td>149</td><td>Greenlandic </td></tr><tr><td>150</td><td>Azerbaijani (Roman script) </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="name_enc2"></a><p class="title"><strong>Table 9.8. ISO specific encodings (platform ID=2)
            [Deprecated]</strong></p><div class="table-contents"><table class="table" summary="ISO specific encodings (platform ID=2)&#10;            [Deprecated]" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Code</th><th>ISO encoding</th></tr></thead><tbody><tr><td>0</td><td>7-bit ASCII</td></tr><tr><td>1</td><td>ISO 10646</td></tr><tr><td>2</td><td>ISO 8859-1</td></tr></tbody></table></div></div><br class="table-break"/><p>There are no ISO-specific language IDs.</p><div class="table"><a name="name_enc4"></a><p class="title"><strong>Table 9.9. Custom platform-specific encoding IDs (platform
            ID=4)</strong></p><div class="table-contents"><table class="table" summary="Custom platform-specific encoding IDs (platform&#10;            ID=4)" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>ID</th><th>Custom encoding</th></tr></thead><tbody><tr><td>0-255</td><td>OTF Windows NT compatibility mapping</td></tr></tbody></table></div></div><br class="table-break"/><p>In cases where a custom platform <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          is present for OTF Windows NT compatibility, the encoding ID
          must be set to the Windows charset value (in the range 0 to
          255, inclusive) present in the .PFM file of the original
          Type 1 font. See the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table for more
          details on the <a class="link" href="chapter.cmap.html#cmap_cust" title="OTF Windows NT compatibility mapping">OTF Windows NT
            compatibility cmap</a>.</p><p>There are currently no language IDs defined for the
          Custom platform. This means that it can be used for
          encodings in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> table but not for
          strings in the <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a> table.</p><p>Name IDs</p><p>The following name IDs are pre-defined, and they apply to
          all platforms unless indicated otherwise. Name IDs 21 to
          255, inclusive, are reserved for future standard names. Name
          IDs 256 to 32767, inclusive, are reserved for font-specific
          names such as those referenced by a font's layout feature.</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Code</th><th>Meaning</th></tr></thead><tbody><tr><td>0</td><td>Copyright notice.</td></tr><tr><td>1</td><td>Font Family nam. Up to four
		  fonts can share the Font Family name, forming a font
		  style linking group (regular, italic, bold, bold
		  italic - as defined by OS/2.fsSelection bit
		  settings).</td></tr><tr><td>2</td><td>Font Subfamily name. The Font
		  Subfamily name distiguishes the font in a group with
		  the same Font Family name (name ID 1). This is
		  assumed to address style (italic, oblique) and !
		  weight (light, bold, black, etc.). A font with no
		  particular differences in weight or style (e.g.
		  medium weight, not italic and fsSelection bit 6 set)
		  should have the string "Regular" stored in this
		  position.</td></tr><tr><td>3</td><td>Unique font identifier</td></tr><tr><td>4</td><td>Full font name; this should be
		  a combination of strings 1 and 2. Exception: if the
		  font is "Regular" as indicated in string 2, then use
		  only the family name contained in string 1. An
		  exception to the above definition of Full font name
		  is for Microsoft platform strings for CFF CommonType
		  fonts: in this case, the Full font name string must
		  be identical to the PostScript FontName in the CFF
		  Name INDEX. </td></tr><tr><td>5</td><td>Version string. Should begin
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
		  followed by a version number as above.</td></tr><tr><td>6</td><td>
                <p>Postscript name for the font; Name ID 6
                    specifies a string which is used to invoke a
                    PostScript language font that corresponds to this
                    CommonType font. If no name ID 6 is present, then
                    there is no defined method for invoking this font
                    on a PostScript interpreter.</p>
                <p>CommonType
                    fonts which include a name with name ID of 6 shall
                    include these two names with name ID 6, and
                    characteristics as follows:</p>
                <p>a.
                    Platform: 1 [Macintosh]; Platform-specific
                    encoding: 0 [Roman]; Language: 0 [English].</p>
                <p>b Platform: 3 [Microsoft]; Platform-specific
                    encoding: 1 [Unicode]; Language: 0x409 [English
                    (American)]. </p>
                <p>Names with name ID 6
                    other than the above two, if present, must be
                    ignored.</p>
                <p>When translated to ASCII,
                    these two name strings must be identical; no
                    longer than 63 characters; and restricted to the
                    printable ASCII subset, codes 33 through 126,
                    except for the 10 characters: '[', ']', '(', ')',
                    '{', '}', '&lt;', '&gt;', '/', '%'.</p>
                <p>In
                    CFF CommonType fonts, these two name strings, when
                    translated to ASCII, must also be identical to the
                    font name as stored in the CFF's Name
                    INDEX.</p>
                <p>The term "PostScript Name"
                    here means a string identical to the two identical
                    name ID 6 strings described above.</p>
                <p>Depending on the particular font format that
                    PostScript language font uses, the invocation
                    method for the PostScript font differs, and the
                    semantics of the resulting PostScript language
                    font differ. The method used to invoke this font
                    depends on the presence of name ID 20.</p>
                <p>If a name ID 20 is present in this font, then
                    the default assumption should be that the
                    PostScript Name defined by name ID 6 should be
                    used with the "composefont" invocation. This
                    PostScript Name is then the name of a PostScript
                    language CIDFont resource which corresponds to the
                    glyphs of the CommonType font. This name is valid to
                    pass, with an appropriate PostScript language CMap
                    reference, and an instance name, to the PostScript
                    language "composefont" operator.</p>
                <p>If
                    no name ID 20 is present in this font, then the
                    default assumption should be that the PostScript
                    Name defined by name ID 6 should be used with the
                    "findfont" invocation, for locating the font in
                    the context of a PostScript interpreter. This
                    PostScript Name is then the name of a PostScript
                    language Font resource which corresponds to the
                    glyphs of the CommonType font. This name is valid to
                    pass to the PostScript language "findfont"
                    operator. Note that this does
                    <span class="emphasis"><em>not</em></span> necessarily imply that
                    the resulting font dictionary accepts an /Encoding
                    array, such as when the font referenced is a Type
                    0 PostScript font.</p>
                <p>Note that this
                    specification applies only to data fork CommonType
                    fonts. Macintosh resource-fork TrueType and other
                    Macintosh sfnt-wrapped fonts supply the PostScript
                    font name to be used with the "findfont"
                    invocation, in order to invoke the font in a
                    PostScript interpreter, in the FOND resource
                    style-mapping table.</p>
                <p>Developers may
                    choose to ignore the default usage when
                    appropriate. For example, PostScript printers
                    whose version is earlier than 2015 cannot process
                    CID font resources, and a CJK CommonType/CFF-CID
                    font can be downloaded only as a set of Type 1
                    PostScript fonts. Legacy CJK TrueType fonts, which
                    do not have a name ID 20, may still be most
                    effectively downloaded as a CID font resource.
                    Definition of the full set of situations in which
                    the defaults should not be followed is outside the
                    scope of this document.</p>
              </td></tr><tr><td>7</td><td>Trademark; this is used to
                save any trademark notice/information for this
                font. Such information should be based on legal
                advice. This is <span class="emphasis"><em>distinctly</em></span>
                separate from the copyright. </td></tr><tr><td>8</td><td>Manufacturer Name.</td></tr><tr><td>9</td><td>Designer; name of the designer of the
                  typeface.</td></tr><tr><td>10</td><td>Description; description of the typeface. Can
                  contain revision information, usage recommendations,
                  history, features, etc.</td></tr><tr><td>11</td><td>URL Vendor; URL of font vendor (with protocol,
                  e.g., http://, ftp://). If a unique serial number is
                  embedded in the URL, it can be used to register the
                  font.</td></tr><tr><td>12</td><td>URL Designer; URL of typeface designer (with
                  protocol, e.g., http://, ftp://).</td></tr><tr><td>13</td><td>License Description; description of how the
                  font may be legally used, or different example
                  scenarios for licensed use. This field should be
                  written in plain language, not legalese.</td></tr><tr><td>14</td><td>License Info URL; URL where additional
                  licensing information can be found.</td></tr><tr><td>15</td><td>Reserved; Set to zero.</td></tr><tr><td>16</td><td>For historical reasons, font
		  families have contained a maximum of four styles,
		  but font designers may group more than four fonts to
		  a single family.  The Preferred Family allows font
		  designers to include the preferred family grouping
		  which contains more than four fonts. This ID is only
		  present if it is different from ID 1. </td></tr><tr><td>17</td><td>Preferred Subfamily allows
		  font designers to include the preferred subfamily
		  grouping that is more descriptive than ID 2. This ID
		  is only present if it is different from ID 2 and
		  must be unique for the the Preferred Family.</td></tr><tr><td>18</td><td>Compatible Full (Macintosh only); On the
                  Macintosh, the menu name is constructed using the
                  FOND resource. This usually matches the Full Name.
                  If you want the name of the font to appear
                  differently than the Full Name, you can insert the
                  Compatible Full Name in ID 18. </td></tr><tr><td>19</td><td>Sample text; This can be the font name, or any
                  other text that the designer thinks is the best
                  sample to display the font in.</td></tr><tr><td>20</td><td>
                <p>PostScript CID findfont name; Its
                    presence in a font means that the nameID 6 holds a
                    PostScript font name that is meant to be used with
                    the "composefont" invocation in order to invoke
                    the font in a PostScript interpreter. See the
                    definition of name ID 6.</p>
                <p>The value
                    held in the name ID 20 string is interpreted as a
                    PostScript font name that is meant to be used with
                    the "findfont" invocation, in order to invoke the
                    font in a PostScript interpreter.</p>
                <p>If
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
                    corresponding name ID 20 record.</p>
                <p>When
                    translated to ASCII, this name string must be
                    restricted to the printable ASCII subset, codes 33
                    through 126, except for the 10 characters: '[',
                    ']', '(', ')', '{', '}', '&lt;', '&gt;', '/',
                    '%'.</p>
                <p>Note that this specification
                    applies only to data fork CommonType fonts.
                    Macintosh resource-fork TrueType and other
                    Macintosh sfnt-wrapped fonts supply the PostScript
                    font name to be used with the "findfont"
                    invocation, in order to invoke the font in a
                    PostScript interpreter, in the FOND resource
                    style-mapping table.</p>
                <p>Note that a
                    particular Name ID 20 string always corresponds to
                    a particular Macintosh cmap subtable. However,
                    some host CommonType/TTF fonts also contain a post
                    table, format 4, which provides a mapping from
                    glyph ID to encoding value, and also corresponds
                    to a particular Macintosh cmap subtable.
                    Unfortunately, the <a class="link" href="chapter.post.html" title="Chapter 12. post - PostScript">post</a> table
                    format 4 contains no provision for identifying
                    which Macintosh cmap subtable it matches, nor for
                    providing more than one mapping. Host fonts which
                    contain a <a class="link" href="chapter.post.html" title="Chapter 12. post - PostScript">post</a> table format 4,
                    should also contain only a single Macintosh cmap
                    subtable, and a single Name ID 20 string. In the
                    case where there is more than one Macintosh cmap
                    subtable and more than one Name ID 20 string,
                    there is no definition of which one matches the
                    <a class="link" href="chapter.post.html" title="Chapter 12. post - PostScript">post</a> table format
                    4.</p>
              </td></tr></tbody></table></div><p>Note that while both Apple and Microsoft support the
          same set of name strings, the interpretations may be
          somewhat different. But since name strings are stored by
          platform, encoding and language (placing separate strings in
          for both Apple and MS platforms), this should not present a
          problem.</p><p>The key information for this table for MS fonts relates
          to the use of strings 1, 2 and 4. To better help understand,
          here are some examples of name usage, weight class and style
          flags:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/></colgroup><thead><tr><th>Font</th><th>Name ID 1</th><th>Name ID 2</th><th>Name ID 4</th><th>Name ID 16</th><th>Name ID 17</th></tr></thead><tbody><tr><td>Arial Narrow</td><td>Arial Narrow</td><td>Regular</td><td>Arial Narrow</td><td>Arial</td><td>Narrow</td></tr><tr><td>Arial Narrow Italic</td><td>Arial Narrow</td><td>Italic</td><td>Arial Narrow Italic</td><td>Arial</td><td>Narrow Italic</td></tr><tr><td>Arial Narrow Bold</td><td>Arial Narrow</td><td>Bold</td><td>Arial Narrow Bold</td><td>Arial</td><td>Narrow Bold</td></tr><tr><td>Arial Narrow Bold Italic</td><td>Arial Narrow</td><td>Bold Italic</td><td>Arial Narrow Bold Italic</td><td>Arial</td><td>Narrow Bold Italic</td></tr><tr><td>Arial</td><td>Arial</td><td>Regular</td><td>Arial</td><td>Arial</td></tr><tr><td>Arial Italic</td><td>Arial</td><td>Italic</td><td>Arial Italic</td><td>Arial</td><td>Italic</td></tr><tr><td>Arial Bold</td><td>Arial</td><td>Bold</td><td>Arial Bold</td><td>Arial</td><td>Bold</td></tr><tr><td>Arial Bold Italic</td><td>Arial</td><td>Bold Italic</td><td>Arial Bold Italic</td><td>Arial</td><td>Bold Italic</td></tr><tr><td>Arial Black</td><td>Arial Black</td><td>Regular</td><td>Arial Black</td><td>Arial</td><td>Black</td></tr><tr><td>Arial Black Italic</td><td>Arial Black</td><td>Italic</td><td>Arial Black Italic</td><td>Arial</td><td>Black Italic</td></tr></tbody></table></div><p>In addition to name strings, OS/2.usWeightClass,
	  OS/2.usWidthClass, OS/2.fsSelection style bits, and
	  head.macStyle bits are shown. These settings allow the fonts
	  to fit together into a single family of varying weight and
	  compression/expansion.</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/><col/><col/><col/><col/><col/><col/><col/></colgroup><thead><tr><th>Font</th><th>OS/2 usWeightClass</th><th>OS/2 usWidthClass</th><th>OS/2 fsSelection Italic</th><th>OS/2 fsSelection Bold</th><th>OS/2 fsSelection Regular</th><th>head macStyle Bold</th><th>head macStyle Italic</th><th>head macStyle Condensed</th><th>head macStyle Extended</th></tr></thead><tbody><tr><td>Arial Narrow</td><td>400</td><td>3</td><td> </td><td> </td><td>x</td><td> </td><td> </td><td>x</td><td> </td></tr><tr><td>Arial Narrow Italic</td><td>400</td><td>3</td><td>x</td><td> </td><td> </td><td> </td><td>x</td><td>x</td><td> </td></tr><tr><td>Arial Narrow Bold</td><td>700</td><td>3</td><td> </td><td>x</td><td> </td><td>x</td><td> </td><td>x</td><td> </td></tr><tr><td>Arial Narrow Bold Italic</td><td>700</td><td>3</td><td>x</td><td>x</td><td> </td><td>x</td><td>x</td><td>x</td><td> </td></tr><tr><td>Arial</td><td>400</td><td>5</td><td> </td><td> </td><td>x</td><td> </td><td> </td><td> </td><td> </td></tr><tr><td>Arial Italic</td><td>400</td><td>5</td><td>x</td><td> </td><td> </td><td> </td><td>x</td><td> </td><td> </td></tr><tr><td>Arial Bold</td><td>700</td><td>5</td><td> </td><td>x</td><td> </td><td>x</td><td> </td><td> </td><td> </td></tr><tr><td>Arial Bold Italic</td><td>700</td><td>5</td><td>x</td><td>x</td><td> </td><td>x</td><td>x</td><td> </td><td> </td></tr><tr><td>Arial Black</td><td>900</td><td>5</td><td> </td><td>x</td><td> </td><td>x</td><td> </td><td> </td><td> </td></tr><tr><td>Arial Black Italic</td><td>900</td><td>5</td><td>x</td><td>x</td><td> </td><td>x</td><td>x</td><td> </td><td> </td></tr></tbody></table></div><p>Note that OS/2 and Windows both require that all name
          strings be defined in Unicode. Thus all 'name' table strings
          for platform ID = 3 (Microsoft) will require two bytes per
          character. Macintosh fonts require single byte
          strings.</p><p>Examples of how these strings might be defined:</p><p>0. The copyright string from the font vendor. <span class="emphasis"><em>©
          Copyright the Monotype Corporation plc, 1990</em></span>
      </p><p>1. The name the user sees. <span class="emphasis"><em>Times New
            Roman</em></span>
      </p><p>2. The name of the style. <span class="emphasis"><em>Bold</em></span>
      </p><p>3. A unique identifier that applications can store to
          identify the font being used. Monotype: <span class="emphasis"><em>Times New Roman
          Bold:1990</em></span>
      </p><p>4. The complete, hopefully unique, human readable name
          of the font. This name is used by Windows. <span class="emphasis"><em>Times
          New Roman Bold</em></span>. (If this were the Microsoft
          platform string for a CFF CommonType font, then the value
          would be <span class="emphasis"><em>TimesNewRoman-Bold</em></span>, as
          described in the definition of name ID 4 above.)</p><p>5. Release and version information from the font vendor.
          <span class="emphasis"><em>Version 1.00 June 1, 1990, initial release</em></span>
      </p><p>6. The name the font will be known by on a PostScript
          printer. <span class="emphasis"><em>TimesNewRoman-Bold</em></span>
      </p><p>7. Trademark string. <span class="emphasis"><em>Times New Roman is a registered
          trademark of the Monotype Corporation.</em></span>
      </p><p>8. Manufacturer. <span class="emphasis"><em>Monotype Corporation
        plc</em></span>
      </p><p>9. Designer. <span class="emphasis"><em>Stanley Morison</em></span>
      </p><p>10. Description. <span class="emphasis"><em>Designed in 1932 for the Times of
          London newspaper. Excellent readability and a narrow overall
          width, allowing more words per line than most fonts.</em></span>
      </p><p>11. URL of Vendor.
          <span class="emphasis"><em>http://www.monotype.com</em></span>
      </p><p>12. URL of Designer.
          <span class="emphasis"><em>http://www.monotype.com</em></span>
      </p><p>13. License Description. <span class="emphasis"><em>This font may be installed on
          all of your machines and printers, but you may not sell or
          give these fonts to anyone else.</em></span>
      </p><p>14. License Info URL.
          <span class="emphasis"><em>http://www.monotype.com/license/</em></span>
      </p><p>15. Reserved. Set to zero.</p><p>16. Preferred Family. No name string
          present, since it is the same as name ID 1 (Font Family
          name).</p><p>17. Preferred Subfamily. No name string
          present, since it is the same as name ID 2 (Font Subfamily
          name).</p><p>18. Compatible Full (Macintosh only). No name string
          present, since it is the same as name ID 4 (Full
          name).</p><p>19. Sample text. <span class="emphasis"><em>The quick brown fox jumps over the lazy
          dog.</em></span>
      </p><p>20. PostScript CID findfont name. No name string
          present. Thus, the PostScript Name defined by name ID 6
          should be used with the "findfont" invocation for locating
          the font in the context of a PostScript interpreter.</p><p>The following is an example of only name IDs 6 and 20 in
          the CFF CommonType Japanese font Kozuka Mincho Std Regular
          (other name IDs are also present in this font):</p><p>6. PostScript name:
          <span class="emphasis"><em>KozMinStd-Regular</em></span>. Since a name ID 20
          is present in the font (see below), then the PostScript name
          defined by name ID 6 should be used with the "composefont"
          invocation for locating the font in the context of a
          PostScript interpreter.</p><p>20. PostScript CID findfont name:
          <span class="emphasis"><em>KozMinStd-Regular-83pv-RKSJ-H</em></span>, in a
          name record of Platform 1 [Macintosh], Platform-specific
          script 1 [Japanese], Language: 0xFFFF [English]. This name
          string is a PostScript name that should be used with the
          "findfont" invocation for locating the font in the context
          of a PostScript interpreter, and is associated with the
          encoding specified by the following cmap subtable, which
          must be present in the font: Platform: 1 [Macintosh];
          Platform-specific encoding: 1 [Japanese]; Language: 0 [not
          language-specific].</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.10.1.2"></a>Annotation</h4></div></div></div><p>In the example, string 19 is not set in italic like the
        other strings.</p></div></div></div>