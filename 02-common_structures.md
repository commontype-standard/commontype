<h3>Common Structures and Data</h3>

<h4><dfn>Platform and Encoding Identifiers</dfn></h4>

Data entries in the [=cmap table=] and [=name table=] are designated as being for the
consumption of particular combinations of *platform* and *platform encoding*. The *platform encoding* selects a character repertoire and
codepoint-to-character mapping available on the given platform. The
platform encoding identifier is not unique across platforms, and hence
implementors must consider platform and platform encoding as a tuple.
The following table defines the platform and platform encoding tuples.

<table>
  <thead>
    <tr>
      <td>Platform ID</td>
      <td>Platform Encoding ID</td>
      <td>Description</td>
    </tr>
  </thead>
  <tbody>
    <tr><th colspan=3>Platform 0 (Unicode)</th></tr>
    <tr role="deprecated">
      <td>0</td>
      <td>0</td>
      <td>Unicode 1.0</td>
    </tr>
    <tr role="deprecated">
      <td>0</td>
      <td>1</td>
      <td>Unicode 1.1</td>
    </tr>
    <tr role="deprecated">
      <td>0</td>
      <td>2</td>
      <td>ISO/IEC 10646</td>
    </tr>
    <tr>
      <td>0</td>
      <td>3</td>
      <td>Unicode 2.0+ BMP (see discussion)</td>
    </tr>
    <tr>
      <td>0</td>
      <td>4</td>
      <td>Unicode 2.0+ (see discussion)</td>
    </tr>
    <tr>
      <td>0</td>
      <td>5</td>
      <td>Unicode Variation Sequences</td>
    </tr>
    <tr>
      <td>0</td>
      <td>6</td>
      <td>Unicode 2.0+ (see discussion)</td>
    </tr>
    <tr><th colspan=3>Platform 1 (Macintosh)</th></tr>
    <tr>
      <td>1</td>
      <td>0</td>
      <td>Roman</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>1</td>
      <td>Japanese</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>2</td>
      <td>Chinese (Traditional)</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>3</td>
      <td>Korean</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>4</td>
      <td>Arabic</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>5</td>
      <td>Hebrew</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>6</td>
      <td>Greek</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>7</td>
      <td>Russian</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>8</td>
      <td>RSymbol</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>9</td>
      <td>Devanagari</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>10</td>
      <td>Gurmukhi</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>11</td>
      <td>Gujarati</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>12</td>
      <td>Oriya</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>13</td>
      <td>Bengali</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>14</td>
      <td>Tamil</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>15</td>
      <td>Telugu</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>16</td>
      <td>Kannada</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>17</td>
      <td>Malayalam</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>18</td>
      <td>Sinhalese</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>19</td>
      <td>Burmese</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>20</td>
      <td>Khmer</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>21</td>
      <td>Thai</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>22</td>
      <td>Laotian</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>23</td>
      <td>Georgian</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>24</td>
      <td>Armenian</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>25</td>
      <td>Chinese (Simplified)</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>26</td>
      <td>Tibetan</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>27</td>
      <td>Mongolian</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>28</td>
      <td>Geez</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>29</td>
      <td>Slavic</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>30</td>
      <td>Vietnamese</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>31</td>
      <td>Sindhi</td>
    </tr>
    <tr role="deprecated">
      <td>1</td>
      <td>32</td>
      <td>Uninterpreted</td>
    </tr>
    <tr><th colspan=3>Platform 2 (ISO)</th></tr>
    <tr role="deprecated">
      <td>2</td>
      <td>0</td>
      <td>7-bit ASCII</td>
    </tr>
    <tr role="deprecated">
      <td>2</td>
      <td>1</td>
      <td>ISO 10646</td>
    </tr>
    <tr role="deprecated">
      <td>2</td>
      <td>2</td>
      <td>ISO 8859-1</td>
    </tr>
    <tr><th colspan=3>Platform 3 (Windows)</th></tr>
    <tr>
      <td>3</td>
      <td>0</td>
      <td>Symbol font *(see discussion)*</td>
    </tr>
    <tr>
      <td>3</td>
      <td>1</td>
      <td>Unicode (BMP characters only)</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>2</td>
      <td>ShiftJIS</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>3</td>
      <td>PRC</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>4</td>
      <td>Big5</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>5</td>
      <td>Wansung</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>6</td>
      <td>Johab</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>7</td>
      <td>Reserved</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>9</td>
      <td>Reserved</td>
    </tr>
    <tr role="deprecated">
      <td>3</td>
      <td>9</td>
      <td>Reserved</td>
    </tr>
    <tr>
      <td>3</td>
      <td>10</td>
      <td>Unicode (access to full range)</td>
    </tr>
    <tr><th colspan=3>Platform 4 (Custom)</th></tr>
    <tr role="deprecated">
      <td>4</td>
      <td>0-255</td>
      <td>OTF Windows NT compatibility mapping</td>
    </tr>
  </tbody>
</table>

PlatformID values 240 through 255 are reserved for user-defined
platforms.

<div class="note">
* Platform IDs and platform encoding IDs are used in two tables: [=cmap=] and name. cmap contains mappings between glyph IDs and codepoints in some operating system character encoding. name contains strings encoded in particular character encodings. Prior to the widespread adoption of Unicode as a common character encoding, the platform-specific nature of character encodings meant that data needed to be tagged with its platform character encoding so that it could be properly interpreted. Additionally, for fonts to operate correctly on multiple platforms, glyph mappings and text strings needed to be specified in multiple encodings, one for each platform on which the font was expected to operate.

* Platform ID 3 platform encoding ID 0 refers to the character repertoire and encoding used by the [Wingdings font](https://en.wikipedia.org/wiki/Wingdings#Character_set). It should only be used for symbol fonts following this encoding.

* The Unicode platform was introduced to allow for cross-platform encoding. However, the Unicode character assignments did not stabilize until backwards compatibility was guaranteed after the release of Unicode 2.0. For example, in Unicode 1.0, codepoint U+370 was allocated as Greek Non-Spacing Iota Below. In Unicode 1.1, this character was moved to codepoint U+345. Hence data using the Unicode platform must also specify the version of the Unicode Standard for which they are encoded. Despite the current prevalence of Unicode, the platform ID system is still required for the name table, as will be explained in the appropriate chapter.

* Platform ID 2 (ISO) was introduced to accommodate the character repertoire of ISO/IEC 10646, but when this standard was released it used the same character repertoire as Unicode and so this platform became redundant. Its use is discouraged by CommonType: font producers should not use it, and font consumers should use an alternative name/cmap entry instead.

* Platform 4 was introduced as a compatibility measure for Windows NT to allow non-Unicode applications to use fonts as though they were Windows ANSI encoded. Its use is discouraged by CommonType: font producers should not use it.

</div>

<h4><dfn>Language Identifier</dfn></h4>

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

<h5><dfn>Macintosh language ID</dfn></h5>

<table>

  <thead><tr><th>Code</th><th>   Language</th></tr></thead>
  <tbody>
<tr><td>  0</td><td>      English</td></tr>
<tr><td>  1</td><td>      French</td></tr>
<tr><td>  2</td><td>      German</td></tr>
<tr><td>  3</td><td>      Italian</td></tr>
<tr><td>  4</td><td>      Dutch</td></tr>
<tr><td>  5</td><td>      Swedish</td></tr>
<tr><td>  6</td><td>      Spanish</td></tr>
<tr><td>  7</td><td>      Danish</td></tr>
<tr><td>  8</td><td>      Portuguese</td></tr>
<tr><td>  9</td><td>      Norwegian</td></tr>
<tr><td>  10</td><td>     Hebrew</td></tr>
<tr><td>  11</td><td>     Japanese</td></tr>
<tr><td>  12</td><td>     Arabic</td></tr>
<tr><td>  13</td><td>     Finnish</td></tr>
<tr><td>  14</td><td>     Greek</td></tr>
<tr><td>  15</td><td>     Icelandic</td></tr>
<tr><td>  16</td><td>     Maltese</td></tr>
<tr><td>  17</td><td>     Turkish</td></tr>
<tr><td>  18</td><td>     Yugoslavian</td></tr>
<tr><td>  19</td><td>     Chinese (Traditional)</td></tr>
<tr><td>  20</td><td>     Urdu</td></tr>
<tr><td>  21</td><td>     Hindi</td></tr>
<tr><td>  22</td><td>     Thai</td></tr>
<tr><td>  23</td><td>     Korean</td></tr>
<tr><td>  24</td><td>     Lithuanian</td></tr>
<tr><td>  25</td><td>     Polish</td></tr>
<tr><td>  26</td><td>     Hungarian</td></tr>
<tr><td>  27</td><td>     Estonian</td></tr>
<tr><td>  28</td><td>     Latvian</td></tr>
<tr><td>  29</td><td>     Sami</td></tr>
<tr><td>  30</td><td>     Faroese</td></tr>
<tr><td>  31</td><td>     Farsi/Persian</td></tr>
<tr><td>  32</td><td>     Russian</td></tr>
<tr><td>  33</td><td>     Chinese (Simplified)</td></tr>
<tr><td>  34</td><td>     Flemish</td></tr>
<tr><td>  35</td><td>     Irish Gaelic</td></tr>
<tr><td>  36</td><td>     Albanian</td></tr>
<tr><td>  37</td><td>     Romanian</td></tr>
<tr><td>  38</td><td>     Czech</td></tr>
<tr><td>  39</td><td>     Slovak</td></tr>
<tr><td>  40</td><td>     Slovenian</td></tr>
<tr><td>  41</td><td>     Yiddish</td></tr>
<tr><td>  42</td><td>     Serbian</td></tr>
<tr><td>  43</td><td>     Macedonian</td></tr>
<tr><td>  44</td><td>     Bulgarian</td></tr>
<tr><td>  45</td><td>     Ukrainian</td></tr>
<tr><td>  46</td><td>     Byelorussian</td></tr>
<tr><td>  47</td><td>     Uzbek</td></tr>
<tr><td>  48</td><td>     Kazakh</td></tr>
<tr><td>  49</td><td>     Azerbaijani (Cyrillic script)</td></tr>
<tr><td>  50</td><td>     Azerbaijani (Arabic script)</td></tr>
<tr><td>  51</td><td>     Armenian</td></tr>
<tr><td>  52</td><td>     Georgian</td></tr>
<tr><td>  53</td><td>     Moldavian</td></tr>
<tr><td>  54</td><td>     Kirghiz</td></tr>
<tr><td>  55</td><td>     Tajiki</td></tr>
<tr><td>  56</td><td>     Turkmen</td></tr>
<tr><td>  57</td><td>     Mongolian (Mongolian script)</td></tr>
<tr><td>  58</td><td>     Mongolian (Cyrillic script)</td></tr>
<tr><td>  59</td><td>     Pashto</td></tr>
<tr><td>  60</td><td>     Kurdish</td></tr>
<tr><td>  61</td><td>     Kashmiri</td></tr>
<tr><td>  62</td><td>     Sindhi</td></tr>
<tr><td>  63</td><td>     Tibetan</td></tr>
<tr><td>  64</td><td>     Nepali</td></tr>
<tr><td>  65</td><td>     Sanskrit</td></tr>
<tr><td>  66</td><td>     Marathi</td></tr>
<tr><td>  67</td><td>     Bengali</td></tr>
<tr><td>  68</td><td>     Assamese</td></tr>
<tr><td>  69</td><td>     Gujarati</td></tr>
<tr><td>  70</td><td>     Punjabi</td></tr>
<tr><td>  71</td><td>     Oriya</td></tr>
<tr><td>  72</td><td>     Malayalam</td></tr>
<tr><td>  73</td><td>     Kannada</td></tr>
<tr><td>  74</td><td>     Tamil</td></tr>
<tr><td>  75</td><td>     Telugu</td></tr>
<tr><td>  76</td><td>     Sinhalese</td></tr>
<tr><td>  77</td><td>     Burmese</td></tr>
<tr><td>  78</td><td>     Khmer</td></tr>
<tr><td>  79</td><td>     Lao</td></tr>
<tr><td>  80</td><td>     Vietnamese</td></tr>
<tr><td>  81</td><td>     Indonesian</td></tr>
<tr><td>  82</td><td>     Tagalong</td></tr>
<tr><td>  83</td><td>     Malay (Roman script)</td></tr>
<tr><td>  84</td><td>     Malay (Arabic script)</td></tr>
<tr><td>  85</td><td>     Amharic</td></tr>
<tr><td>  86</td><td>     Tigrinya</td></tr>
<tr><td>  87</td><td>     Galla</td></tr>
<tr><td>  88</td><td>     Somali</td></tr>
<tr><td>  89</td><td>     Swahili</td></tr>
<tr><td>  90</td><td>     Kinyarwanda/Ruanda</td></tr>
<tr><td>  91</td><td>     Rundi</td></tr>
<tr><td>  92</td><td>     Nyanja/Chewa</td></tr>
<tr><td>  93</td><td>     Malagasy</td></tr>
<tr><td>  94</td><td>     Esperanto</td></tr>
<tr><td>  128</td><td>    Welsh</td></tr>
<tr><td>  129</td><td>    Basque</td></tr>
<tr><td>  130</td><td>    Catalan</td></tr>
<tr><td>  131</td><td>    Latin</td></tr>
<tr><td>  132</td><td>    Quenchua</td></tr>
<tr><td>  133</td><td>    Guarani</td></tr>
<tr><td>  134</td><td>    Aymara</td></tr>
<tr><td>  135</td><td>    Tatar</td></tr>
<tr><td>  136</td><td>    Uighur</td></tr>
<tr><td>  137</td><td>    Dzongkha</td></tr>
<tr><td>  138</td><td>    Javanese (Roman script)</td></tr>
<tr><td>  139</td><td>    Sundanese (Roman script)</td></tr>
<tr><td>  140</td><td>    Galician</td></tr>
<tr><td>  141</td><td>    Afrikaans</td></tr>
<tr><td>  142</td><td>    Breton</td></tr>
<tr><td>  143</td><td>    Inuktitut \[!!fixed\]</td></tr>
<tr><td>  144</td><td>    Scottish Gaelic</td></tr>
<tr><td>  145</td><td>    Manx Gaelic</td></tr>
<tr><td>  146</td><td>    Irish Gaelic (with dot above)</td></tr>
<tr><td>  147</td><td>    Tongan</td></tr>
<tr><td>  148</td><td>    Greek (polytonic)</td></tr>
<tr><td>  149</td><td>    Greenlandic</td></tr>
<tr><td>  150</td><td>    Azerbaijani (Roman script)</td></tr>
</tbody>
</table>

<h5><dfn>Windows language ID</dfn></h5>

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
