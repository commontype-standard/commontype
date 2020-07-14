<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.name"></a>Chapter 10. name - Naming Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm2784"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.11.1.1"></a>Specification</h4></div></div></div><p>The naming table allows multilingual strings to be
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
          (platform ID 1) strings from the <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a>
          table. Because of this, we strongly recommend that the
          <a class="link" href="chapter.name.html" title="Chapter 10. name - Naming Table">name</a> table of all fonts include Macintosh
          platform strings and that the syntax of the version number
          (name id 5) follows the guidelines given in this
          document.</p><p>The Naming Table is organized as follows:</p><div class="table"><a name="idm2793"></a><p class="title"><strong>Table 10.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>format</td><td>Format selector (=0).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>count</td><td>Number of name records.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>stringOffset</td><td>Offset to start of string storage (from start
                  of table).</td><td class="auto-generated"> </td></tr><tr><td>n NameRecords</td><td>nameRecord [count]</td><td>The name records where count is the number of
	      records.</td><td class="auto-generated"> </td></tr><tr><td>(Variable)</td><td> </td><td>Storage for the actual string data.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Each NameRecord looks like this:</p><div class="table"><a name="idm2822"></a><p class="title"><strong>Table 10.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>platformID</td><td>Platform ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>encodingID</td><td>Platform-specific encoding ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>languageID</td><td>Language ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>nameID</td><td>Name ID.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>length</td><td>String length (in bytes).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset</td><td>String offset from start of storage area (in
                  bytes).</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Following are the descriptions of the four kinds of ID.
          Note that the specific values listed here are the only ones
          that are predefined; new ones may be added by registry with
          Apple Developer Technical Support. Similar to the character
          encoding table, the NameRecords is sorted by platform ID,
          then platform-specific ID, then language ID, and then by
          name ID.
          XXX - refer to common structures
        </p><p>When building a Unicode font for Windows, the platform
          ID should be 3 and the encoding ID should be 1. When
          building a symbol font for Windows, the platform ID should
          be 3 and the encoding ID should be 0. When building a font
          that will be used on the Macintosh, the platform ID should
          be 1 and the encoding ID should be 0.</p><p>Name IDs</p><p>The following name IDs are pre-defined, and they apply to
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
                    Unfortunately, the <a class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table
                    format 4 contains no provision for identifying
                    which Macintosh cmap subtable it matches, nor for
                    providing more than one mapping. Host fonts which
                    contain a <a class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table format 4,
                    should also contain only a single Macintosh cmap
                    subtable, and a single Name ID 20 string. In the
                    case where there is more than one Macintosh cmap
                    subtable and more than one Name ID 20 string,
                    there is no definition of which one matches the
                    <a class="link" href="chapter.post.html" title="Chapter 13. post - PostScript">post</a> table format
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
          language-specific].</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.11.1.2"></a>Annotation</h4></div></div></div><p>In the example, string 19 is not set in italic like the
        other strings.</p></div></div></div>