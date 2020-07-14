<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.common_structures"></a>Chapter 4. Common Structures and Data</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="common_structures.platformencoding"></a>Platform and Encoding Identifiers</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.1.1"></a>Specification</h4></div></div></div><p>
        Data entries in the <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> and <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>
        tables are designated as being for the consumption of particular
        combinations of <em class="glossterm">platform</em> and <em class="glossterm">
        platform encoding</em>. The platform encoding selects a
        character repertoire and codepoint-to-character mapping available
        on the given platform. The platform encoding identifier is not unique
        across platforms, and hence implementors must consider platform and
        platform encoding as a tuple. The following table defines the
        platform and platform encoding tuples permitted by the
        CommonType Specification.
      </p><div class="table"><a name="idm754"></a><p class="title"><strong>Table 4.1. Platforms and Platform Encoding Identifiers</strong></p><div class="table-contents"><table class="table" summary="Platforms and Platform Encoding Identifiers" border="1"><colgroup><col/><col/><col/></colgroup><thead><tr><th>Platform ID</th><th>Encoding ID</th><th>Description</th></tr></thead><tbody><tr role="deprecated"><td>0 (Unicode)</td><td>0</td><td>Unicode 1.0</td></tr><tr role="deprecated"><td>0 (Unicode)</td><td>1</td><td>Unicode 1.1</td></tr><tr role="deprecated"><td>0 (Unicode)</td><td>2</td><td>ISO/IEC 10646</td></tr><tr><td>0 (Unicode)</td><td>3</td><td>Unicode 2.0+ BMP (see discussion)</td></tr><tr><td>0 (Unicode)</td><td>4</td><td>Unicode 2.0+ (see discussion)</td></tr><tr><td>0 (Unicode)</td><td>5</td><td>Unicode Variation Sequences</td></tr><tr><td>0 (Unicode)</td><td>6</td><td>Unicode 2.0+ (see discussion)</td></tr><tr><td>1 (Macintosh)</td><td>0</td><td>Roman</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>1</td><td>Japanese</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>2</td><td>Chinese (Traditional)</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>3</td><td>Korean</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>4</td><td>Arabic</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>5</td><td>Hebrew</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>6</td><td>Greek</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>7</td><td>Russian</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>8</td><td>RSymbol</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>9</td><td>Devanagari</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>10</td><td>Gurmukhi</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>11</td><td>Gujarati</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>12</td><td>Oriya</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>13</td><td>Bengali</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>14</td><td>Tamil</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>15</td><td>Telugu</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>16</td><td>Kannada</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>17</td><td>Malayalam</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>18</td><td>Sinhalese</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>19</td><td>Burmese</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>20</td><td>Khmer</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>21</td><td>Thai</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>22</td><td>Laotian</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>23</td><td>Georgian</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>24</td><td>Armenian</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>25</td><td>Chinese (Simplified)</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>26</td><td>Tibetan</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>27</td><td>Mongolian</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>28</td><td>Geez</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>29</td><td>Slavic</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>30</td><td>Vietnamese</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>31</td><td>Sindhi</td></tr><tr role="deprecated"><td>1 (Macintosh)</td><td>32</td><td>Uninterpreted</td></tr><tr role="deprecated"><td>2 (ISO)</td><td>0</td><td>7-bit ASCII</td></tr><tr role="deprecated"><td>2 (ISO)</td><td>1</td><td>ISO 10646</td></tr><tr role="deprecated"><td>2 (ISO)</td><td>2</td><td>ISO 8859-1</td></tr><tr><td>3 (Windows)</td><td>0</td><td>Symbol font (see discussion)</td></tr><tr><td>3 (Windows)</td><td>1</td><td>Unicode (BMP characters only)</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>2</td><td>ShiftJIS</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>3</td><td>PRC</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>4</td><td>Big5</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>5</td><td>Wansung</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>6</td><td>Johab</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>7</td><td>Reserved</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>9</td><td>Reserved</td></tr><tr role="deprecated"><td>3 (Windows)</td><td>9</td><td>Reserved</td></tr><tr><td>3 (Windows)</td><td>10</td><td>Unicode (access to full range)</td></tr><tr role="deprecated"><td>4 (Custom)</td><td>0-255</td><td>OTF Windows NT compatibility mapping</td></tr></tbody></table></div></div><br class="table-break"/><p>PlatformID values 240 through 255 are reserved for
          user-defined platforms.</p></div><div role="discussion" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.5.1.2"></a>Discussion</h4></div></div></div><p>
        Platform IDs and platform encoding IDs are used in two CommonType
        tables: <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> and <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>.
        <a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> contains mappings between glyph IDs and
        codepoints in some operating system character encoding.
        <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> contains strings encoded in particular
        character encodings. Prior to the widespread adoption of Unicode
        as a common character encoding, the platform-specific nature of
        character encodings meant that data needed to be tagged with its
        platform character encoding so that it could be properly interpreted.
        Additionally, for fonts to operate correctly on multiple platforms,
        glyph mappings and text strings needed to be specified in multiple
        encodings, one for each platform on which the font was expected to
        operate.
      </p><p>
        Platform ID 3 platform encoding ID 0 refers to the character repertoire
        and encoding used by the <a class="link" href="https://en.wikipedia.org/wiki/Wingdings#Character_set" target="_top">Wingdings font</a>. It should only be used
        for symbol fonts following this encoding.
      </p><p>The Unicode platform was introduced to allow for cross-platform
        encoding. However, the Unicode character assignments did not stabilize
        until backwards compatibility was guaranteed after the release of Unicode
        2.0. For example, in Unicode 1.0, codepoint U+370 was allocated as
        Greek Non-Spacing Iota Below. In Unicode 1.1, this character was moved to
        codepoint U+345. Hence data using the Unicode platform must also specify
        the version of the Unicode Standard for which they are encoded.
        Despite the current prevalence of Unicode, the platform ID system is
        still required for the <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table, as will be
        explained in the appropriate chapter.
      </p><p>
        Platform ID 2 (ISO) was introduced to accommodate the character
        repertoire of ISO/IEC 10646, but when this standard was released it
        used the same character repertoire as Unicode and so this platform
        became redundant. Font producers should not use it, and font consumers
        should use an alternative <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>/<a class="link" href="chapter.cmap.html" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> entry instead.
      </p><p>
        Platform 4 was introduced as a compatibility measure for Windows NT to
        allow non-Unicode applications to use fonts as though they were Windows
        ANSI encoded. Font producers should not use it.
      </p></div></div></div>