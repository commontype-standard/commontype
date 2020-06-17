# name - Naming Table

## Introduction

### Specification

The naming table allows multilingual strings to be associated with the
OpenType font file. These strings can represent copyright notices, font
names, family names, style names, and so on. To keep this table short,
the font manufacturer may wish to make a limited set of entries in some
small set of languages; later, the font can be "localized" and the
strings translated or added. Other parts of the OpenType font file that
require these strings can then refer to them simply by their index
number. Clients that need a particular string can look it up by its
platform ID, character encoding ID, language ID and name ID. Note that
some platforms may require single byte character strings, while others
may require double byte strings.

For historical reasons, some applications which install fonts perform
version control using Macintosh platform (platform ID 1) strings from
the [name](#chapter.name) table. Because of this, we strongly recommend
that the [name](#chapter.name) table of all fonts include Macintosh
platform strings and that the syntax of the version number (name id 5)
follows the guidelines given in this document.

The Naming Table is organized as follows:

| Type          | Name                 | Description                                              |
| ------------- | -------------------- | -------------------------------------------------------- |
| USHORT        | format               | Format selector (=0).                                    |
| USHORT        | count                | Number of name records.                                  |
| USHORT        | stringOffset         | Offset to start of string storage (from start of table). |
| n NameRecords | nameRecord \[count\] | The name records where count is the number of records.   |
| (Variable)    |                      | Storage for the actual string data.                      |

Each NameRecord looks like this:

| Type   | Name       | Description                                          |
| ------ | ---------- | ---------------------------------------------------- |
| USHORT | platformID | Platform ID.                                         |
| USHORT | encodingID | Platform-specific encoding ID.                       |
| USHORT | languageID | Language ID.                                         |
| USHORT | nameID     | Name ID.                                             |
| USHORT | length     | String length (in bytes).                            |
| USHORT | offset     | String offset from start of storage area (in bytes). |

Following are the descriptions of the four kinds of ID. Note that the
specific values listed here are the only ones that are predefined; new
ones may be added by registry with Apple Developer Technical Support.
Similar to the character encoding table, the NameRecords is sorted by
platform ID, then platform-specific ID, then language ID, and then by
name ID.

| PlatformID | Platform name      | Platform-specific encoding IDs            | Language IDs           |
| ---------- | ------------------ | ----------------------------------------- | ---------------------- |
| 0          | Unicode            | [Various](#name_enc0)                     | None                   |
| 1          | Macintosh          | [Script manager code](#name_enc1)         | [Various](#name_lang1) |
| 2          | ISO \[deprecated\] | [ISO encoding](#name_enc2) \[deprecated\] | None                   |
| 3          | Microsoft          | [Microsoft encoding](#name_enc3)          | [Various](#name_lang3) |
| 4          | Custom             | [Custom](#name_enc4)                      | None                   |

Platform IDs, Platform-specific encoding IDs and Language IDs

Note that platform ID 2 (ISO) has been deprecated as of OpenType
Specification v1.3. It was intended to represent ISO/IEC 10646, as
opposed to Unicode; both standards have identical character code
assignments.

PlatformID values 240 through 255 are reserved for user-defined
platforms. The DTS registry will never assign these values to a
registered platform.

| EncodingID | Description                                                |
| ---------- | ---------------------------------------------------------- |
| 0          | Unicode 1.0 semantics                                      |
| 1          | Unicode 1.1 semantics                                      |
| 2          | ISO 10646:1993 semantics                                   |
| 3          | Unicode 2.0 and onwards semantics, Unicode BMP only        |
| 4          | Unicode 2.0 and onwards semantics, Unicode full repertoire |
| 5          | Unicode Variation Sequences                                |

Unicode platform-specific encoding IDs (platform ID = 0)

A new encoding ID for the Unicode platform will be assigned if a new
version of Unicode moves characters, in order to properly specify
character code semantics. The distinction between Unicode
platform-specific encoding IDs 1 and 2 is for historical reasons only;
Unicode 1.1 is in fact identical in repertoire and encoding to ISO
10646:1993 (before any amendments).

Unicode platform encoding ID 5 can be used for encodings in the 'cmap'
table but not for strings in the 'name' table.

There are currently no language IDs defined for the Unicode platform.
This means that it can be used for encodings in the
[cmap](#chapter.cmap) table but not for strings in the
[name](#chapter.name) table.

| Platform ID | Encoding ID | Description             |
| ----------- | ----------- | ----------------------- |
| 3           | 0           | Symbol                  |
| 3           | 1           | Unicode BMP only        |
| 3           | 2           | ShiftJIS                |
| 3           | 3           | PRC                     |
| 3           | 4           | Big5                    |
| 3           | 5           | Wansung                 |
| 3           | 6           | Johab                   |
| 3           | 7           | Reserved                |
| 3           | 8           | Reserved                |
| 3           | 9           | Reserved                |
| 3           | 10          | Unicode full repertoire |

Microsoft platform-specific encoding IDs (platform ID= 3)

When building a Unicode font for Windows, the platform ID should be 3
and the encoding ID should be 1. When building a symbol font for
Windows, the platform ID should be 3 and the encoding ID should be 0.
When building a font that will be used on the Macintosh, the platform ID
should be 1 and the encoding ID should be 0.

Microsoft Language IDs (platform ID = 3)

The language ID (LCID in the table below) refers to a value which
identifies the language in which a particular string is written. Fifty
of the language ID's assigned by Microsoft are listed below, along with
their corresponding code pages. There are 85 additional language ID's
assigned. corresponding code pages. There are 85 additional language
ID's assigned. For a full list, please see the [Microsoft Global
Development](http://www.microsoft.com/globaldev/reference/loclanghome.asp)
site or [Knowledge Base article
Q224804](http://support.microsoft.com/default.aspx?scid=kb;EN-US;q224804).

| Primary Language | Locale Name                | LCID        | Win CP | OEM CP          |
| ---------------- | -------------------------- | ----------- | ------ | --------------- |
| Albanian         | Albania                    | (041c; SQI) |        |                 |
| Basque           | Basque                     | (042D; EUQ) | 1252   | 850             |
| Byelorussian     | Byelorussia                | (0423, BEL) | 1251   | 866             |
| Bulgarian        | Bulgaria                   | (0402, BGR) | 1251   | 866             |
| Catalan          | Catalan                    | (0403; CAT) | 1252   | 850             |
| Croatian         | Croatian                   | (041a, SHL) | 1250   | 852             |
| Czech            | Czech                      | (0405; CSY) | 1250   | 852             |
| Danish           | Danish                     | (0406; DAN) | 1252   | 865             |
| Dutch (2):       | Dutch (Standard)           | (0413; NLD) | 1252   | 850             |
| Dutch (2):       | Belgian (Flemish)          | (0813; NLB) | 1252   | 850             |
| English (6):     | American                   | (0409; ENU) | 1252   | 437             |
| English (6):     | British                    | (0809; ENG) | 1252   | 850             |
| English (6):     | Australian                 | (0c09; ENA) | 1252   | 850             |
| English (6):     | Canadian                   | (1009; ENC) | 1252   | 850             |
| English (6):     | New Zealand                | (1409; ENZ) | 1252   | 850             |
| English (6):     | Ireland                    | (1809; ENI) | 1252   | 850             |
| Estonian         | Estonia                    | (0425, ETI) | 1257   | 775             |
| Finnish          | Finnish                    | (040b; FIN) | 1252   | 850             |
| French           | French (Standard)          | (040c; FRA) | 1252   | 850             |
| French           | Belgian                    | (080c; FRB) | 1252   | 850             |
| French           | Canadian                   | (0c0c; FRC) | 1252   | 850             |
| French           | Swiss                      | (100c; FRS) | 1252   | 850             |
| French           | Luxembourg                 | (140c; FRL) | 1252   | 850             |
| German           | German (Standard)          | (0407; DEU) | 1252   | 850             |
| German           | Swiss                      | (0807; DES) | 1252   | 850             |
| German           | Austrian                   | (0c07; DEA) | 1252   | 850             |
| German           | Luxembourg                 | (1007; DEL) | 1252   | 850             |
| German           | Liechtenstein              | (1407; DEC) | 1252   | 850             |
| Greek            | Greek                      | (0408; ELL) | 1253   | 737 or 869\[3\] |
| Hungarian        | Hungarian                  | (040e; HUN) | 1250   | 852             |
| Icelandic        | Icelandic                  | (040F; ISL) | 1252   | 850             |
| Italian (2):     | Italian (Standard)         | (0410; ITA) | 1252   | 850             |
| Italian (2):     | Swiss                      | (0810; ITS) | 1252   | 850             |
| Latvian          | Latvia                     | (0426, LVI) | 1257   | 775             |
| Lithuanian       | Lithuania                  | (0427, LTH) | 1257   | 775             |
| Norwegian (2):   | Norwegian (Bokmal)         | (0414; NOR) | 1252   | 850             |
| Norwegian (2):   | Norwegian (Nynorsk)        | (0814; NON) | 1252   | 850             |
| Polish           | Polish                     | (0415; PLK) | 1250   | 852             |
| Portuguese (2):  | Portuguese (Brazilian)     | (0416; PTB) | 1252   | 850             |
| Portuguese (2):  | Portuguese (Standard)      | (0816; PTG) | 1252   | 850             |
| Romanian (2):    | Romania                    | (0418, ROM) | 1250   | 852             |
| Russian          | Russian                    | (0419; RUS) | 1251   | 866             |
| Slovak           | Slovak                     | (041b; SKY) | 1250   | 852             |
| Slovenian        | Slovenia                   | (0424, SLV) | 1250   | 852             |
| Spanish (3):     | Spanish (Traditional Sort) | (040a; ESP) | 1252   | 850             |
| Spanish (3):     | Mexican                    | (080a; ESM) | 1252   | 850             |
| Spanish (3):     | Spanish (Modern Sort)      | (0c0a; ESN) | 1252   | 850             |
| Swedish          | Swedish                    | (041D; SVE) | 1252   | 850             |
| Turkish          | Turkish                    | (041f; TRK) | 1254   | 857             |
| Ukrainian        | Ukraine                    | (0422, UKR) | 1251   | 866             |

| Code | Script                |
| ---- | --------------------- |
| 0    | Roman                 |
| 1    | Japanese              |
| 2    | Chinese (Traditional) |
| 3    | Korean                |
| 4    | Arabic                |
| 5    | Hebrew                |
| 6    | Greek                 |
| 7    | Russian               |
| 8    | RSymbol               |
| 9    | Devanagari            |
| 10   | Gurmukhi              |
| 11   | Gujarati              |
| 12   | Oriya                 |
| 13   | Bengali               |
| 14   | Tamil                 |
| 15   | Telugu                |
| 16   | Kannada               |
| 17   | Malayalam             |
| 18   | Sinhalese             |
| 19   | Burmese               |
| 20   | Khmer                 |
| 21   | Thai                  |
| 22   | Laotian               |
| 23   | Georgian              |
| 24   | Armenian              |
| 25   | Chinese (Simplified)  |
| 26   | Tibetan               |
| 27   | Mongolian             |
| 28   | Geez                  |
| 29   | Slavic                |
| 30   | Vietnamese            |
| 31   | Sindhi                |
| 32   | Uninterpreted         |

Macintosh platform-specific encoding IDs (script manager codes),
(platform ID = 1)

| Code | Language                      |
| ---- | ----------------------------- |
| 0    | English                       |
| 1    | French                        |
| 2    | German                        |
| 3    | Italian                       |
| 4    | Dutch                         |
| 5    | Swedish                       |
| 6    | Spanish                       |
| 7    | Danish                        |
| 8    | Portuguese                    |
| 9    | Norwegian                     |
| 10   | Hebrew                        |
| 11   | Japanese                      |
| 12   | Arabic                        |
| 13   | Finnish                       |
| 14   | Greek                         |
| 15   | Icelandic                     |
| 16   | Maltese                       |
| 17   | Turkish                       |
| 18   | Yugoslavian                   |
| 19   | Chinese (Traditional)         |
| 20   | Urdu                          |
| 21   | Hindi                         |
| 22   | Thai                          |
| 23   | Korean                        |
| 24   | Lithuanian                    |
| 25   | Polish                        |
| 26   | Hungarian                     |
| 27   | Estonian                      |
| 28   | Latvian                       |
| 29   | Sami                          |
| 30   | Faroese                       |
| 31   | Farsi/Persian                 |
| 32   | Russian                       |
| 33   | Chinese (Simplified)          |
| 34   | Flemish                       |
| 35   | Irish Gaelic                  |
| 36   | Albanian                      |
| 37   | Romanian                      |
| 38   | Czech                         |
| 39   | Slovak                        |
| 40   | Slovenian                     |
| 41   | Yiddish                       |
| 42   | Serbian                       |
| 43   | Macedonian                    |
| 44   | Bulgarian                     |
| 45   | Ukrainian                     |
| 46   | Byelorussian                  |
| 47   | Uzbek                         |
| 48   | Kazakh                        |
| 49   | Azerbaijani (Cyrillic script) |
| 50   | Azerbaijani (Arabic script)   |
| 51   | Armenian                      |
| 52   | Georgian                      |
| 53   | Moldavian                     |
| 54   | Kirghiz                       |
| 55   | Tajiki                        |
| 56   | Turkmen                       |
| 57   | Mongolian (Mongolian script)  |
| 58   | Mongolian (Cyrillic script)   |
| 59   | Pashto                        |
| 60   | Kurdish                       |
| 61   | Kashmiri                      |
| 62   | Sindhi                        |
| 63   | Tibetan                       |
| 64   | Nepali                        |
| 65   | Sanskrit                      |
| 66   | Marathi                       |
| 67   | Bengali                       |
| 68   | Assamese                      |
| 69   | Gujarati                      |
| 70   | Punjabi                       |
| 71   | Oriya                         |
| 72   | Malayalam                     |
| 73   | Kannada                       |
| 74   | Tamil                         |
| 75   | Telugu                        |
| 76   | Sinhalese                     |
| 77   | Burmese                       |
| 78   | Khmer                         |
| 79   | Lao                           |
| 80   | Vietnamese                    |
| 81   | Indonesian                    |
| 82   | Tagalong                      |
| 83   | Malay (Roman script)          |
| 84   | Malay (Arabic script)         |
| 85   | Amharic                       |
| 86   | Tigrinya                      |
| 87   | Galla                         |
| 88   | Somali                        |
| 89   | Swahili                       |
| 90   | Kinyarwanda/Ruanda            |
| 91   | Rundi                         |
| 92   | Nyanja/Chewa                  |
| 93   | Malagasy                      |
| 94   | Esperanto                     |
| 128  | Welsh                         |
| 129  | Basque                        |
| 130  | Catalan                       |
| 131  | Latin                         |
| 132  | Quenchua                      |
| 133  | Guarani                       |
| 134  | Aymara                        |
| 135  | Tatar                         |
| 136  | Uighur                        |
| 137  | Dzongkha                      |
| 138  | Javanese (Roman script)       |
| 139  | Sundanese (Roman script)      |
| 140  | Galician                      |
| 141  | Afrikaans                     |
| 142  | Breton                        |
| 143  | Inuktitut \[\!\!fixed\]       |
| 144  | Scottish Gaelic               |
| 145  | Manx Gaelic                   |
| 146  | Irish Gaelic (with dot above) |
| 147  | Tongan                        |
| 148  | Greek (polytonic)             |
| 149  | Greenlandic                   |
| 150  | Azerbaijani (Roman script)    |

Macintosh language IDs (platform ID = 1)

| Code | ISO encoding |
| ---- | ------------ |
| 0    | 7-bit ASCII  |
| 1    | ISO 10646    |
| 2    | ISO 8859-1   |

ISO specific encodings (platform ID=2) \[Deprecated\]

There are no ISO-specific language IDs.

| ID    | Custom encoding                      |
| ----- | ------------------------------------ |
| 0-255 | OTF Windows NT compatibility mapping |

Custom platform-specific encoding IDs (platform ID=4)

In cases where a custom platform [cmap](#chapter.cmap) is present for
OTF Windows NT compatibility, the encoding ID must be set to the Windows
charset value (in the range 0 to 255, inclusive) present in the .PFM
file of the original Type 1 font. See the [cmap](#chapter.cmap) table
for more details on the [OTF Windows NT compatibility cmap](#cmap_cust).

There are currently no language IDs defined for the Custom platform.
This means that it can be used for encodings in the
[cmap](#chapter.cmap) table but not for strings in the
[name](#chapter.name) table.

Name IDs

The following name IDs are pre-defined, and they apply to all platforms
unless indicated otherwise. Name IDs 21 to 255, inclusive, are reserved
for future standard names. Name IDs 256 to 32767, inclusive, are
reserved for font-specific names such as those referenced by a font's
layout feature.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>Copyright notice.</td>
</tr>
<tr class="even">
<td>1</td>
<td>Font Family nam. Up to four fonts can share the Font Family name, forming a font style linking group (regular, italic, bold, bold italic - as defined by OS/2.fsSelection bit settings).</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Font Subfamily name. The Font Subfamily name distiguishes the font in a group with the same Font Family name (name ID 1). This is assumed to address style (italic, oblique) and ! weight (light, bold, black, etc.). A font with no particular differences in weight or style (e.g. medium weight, not italic and fsSelection bit 6 set) should have the string "Regular" stored in this position.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Unique font identifier</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Full font name; this should be a combination of strings 1 and 2. Exception: if the font is "Regular" as indicated in string 2, then use only the family name contained in string 1. An exception to the above definition of Full font name is for Microsoft platform strings for CFF OpenType fonts: in this case, the Full font name string must be identical to the PostScript FontName in the CFF Name INDEX.</td>
</tr>
<tr class="even">
<td>5</td>
<td>Version string. Should begin with the syntax 'Version &lt;number&gt;.&lt;number&gt;' (upper case, lower case, or mixed, with a space between "Version" and the number). The string must contain a version number of the following form: one or more digits (0-9) of value less than 65,535, followed by a period, followed by one or more digits of value less than 65,535. Any character other than a digit will terminate the minor number. A character such as ";" is helpful to separate different pieces of version information. The first such match in the string can be used by installation software to compare font versions. Note that some installers may require the string to start with "Version ", followed by a version number as above.</td>
</tr>
<tr class="odd">
<td>6</td>
<td><p>Postscript name for the font; Name ID 6 specifies a string which is used to invoke a PostScript language font that corresponds to this OpenType font. If no name ID 6 is present, then there is no defined method for invoking this font on a PostScript interpreter.</p>
<p>OpenType fonts which include a name with name ID of 6 shall include these two names with name ID 6, and characteristics as follows:</p>
<p>a. Platform: 1 [Macintosh]; Platform-specific encoding: 0 [Roman]; Language: 0 [English].</p>
<p>b Platform: 3 [Microsoft]; Platform-specific encoding: 1 [Unicode]; Language: 0x409 [English (American)].</p>
<p>Names with name ID 6 other than the above two, if present, must be ignored.</p>
<p>When translated to ASCII, these two name strings must be identical; no longer than 63 characters; and restricted to the printable ASCII subset, codes 33 through 126, except for the 10 characters: '[', ']', '(', ')', '{', '}', '&lt;', '&gt;', '/', '%'.</p>
<p>In CFF OpenType fonts, these two name strings, when translated to ASCII, must also be identical to the font name as stored in the CFF's Name INDEX.</p>
<p>The term "PostScript Name" here means a string identical to the two identical name ID 6 strings described above.</p>
<p>Depending on the particular font format that PostScript language font uses, the invocation method for the PostScript font differs, and the semantics of the resulting PostScript language font differ. The method used to invoke this font depends on the presence of name ID 20.</p>
<p>If a name ID 20 is present in this font, then the default assumption should be that the PostScript Name defined by name ID 6 should be used with the "composefont" invocation. This PostScript Name is then the name of a PostScript language CIDFont resource which corresponds to the glyphs of the OpenType font. This name is valid to pass, with an appropriate PostScript language CMap reference, and an instance name, to the PostScript language "composefont" operator.</p>
<p>If no name ID 20 is present in this font, then the default assumption should be that the PostScript Name defined by name ID 6 should be used with the "findfont" invocation, for locating the font in the context of a PostScript interpreter. This PostScript Name is then the name of a PostScript language Font resource which corresponds to the glyphs of the OpenType font. This name is valid to pass to the PostScript language "findfont" operator. Note that this does <em>not</em> necessarily imply that the resulting font dictionary accepts an /Encoding array, such as when the font referenced is a Type 0 PostScript font.</p>
<p>Note that this specification applies only to data fork OpenType fonts. Macintosh resource-fork TrueType and other Macintosh sfnt-wrapped fonts supply the PostScript font name to be used with the "findfont" invocation, in order to invoke the font in a PostScript interpreter, in the FOND resource style-mapping table.</p>
<p>Developers may choose to ignore the default usage when appropriate. For example, PostScript printers whose version is earlier than 2015 cannot process CID font resources, and a CJK OpenType/CFF-CID font can be downloaded only as a set of Type 1 PostScript fonts. Legacy CJK TrueType fonts, which do not have a name ID 20, may still be most effectively downloaded as a CID font resource. Definition of the full set of situations in which the defaults should not be followed is outside the scope of this document.</p></td>
</tr>
<tr class="even">
<td>7</td>
<td>Trademark; this is used to save any trademark notice/information for this font. Such information should be based on legal advice. This is <em>distinctly</em> separate from the copyright.</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Manufacturer Name.</td>
</tr>
<tr class="even">
<td>9</td>
<td>Designer; name of the designer of the typeface.</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Description; description of the typeface. Can contain revision information, usage recommendations, history, features, etc.</td>
</tr>
<tr class="even">
<td>11</td>
<td>URL Vendor; URL of font vendor (with protocol, e.g., http://, ftp://). If a unique serial number is embedded in the URL, it can be used to register the font.</td>
</tr>
<tr class="odd">
<td>12</td>
<td>URL Designer; URL of typeface designer (with protocol, e.g., http://, ftp://).</td>
</tr>
<tr class="even">
<td>13</td>
<td>License Description; description of how the font may be legally used, or different example scenarios for licensed use. This field should be written in plain language, not legalese.</td>
</tr>
<tr class="odd">
<td>14</td>
<td>License Info URL; URL where additional licensing information can be found.</td>
</tr>
<tr class="even">
<td>15</td>
<td>Reserved; Set to zero.</td>
</tr>
<tr class="odd">
<td>16</td>
<td>For historical reasons, font families have contained a maximum of four styles, but font designers may group more than four fonts to a single family. The Preferred Family allows font designers to include the preferred family grouping which contains more than four fonts. This ID is only present if it is different from ID 1.</td>
</tr>
<tr class="even">
<td>17</td>
<td>Preferred Subfamily allows font designers to include the preferred subfamily grouping that is more descriptive than ID 2. This ID is only present if it is different from ID 2 and must be unique for the the Preferred Family.</td>
</tr>
<tr class="odd">
<td>18</td>
<td>Compatible Full (Macintosh only); On the Macintosh, the menu name is constructed using the FOND resource. This usually matches the Full Name. If you want the name of the font to appear differently than the Full Name, you can insert the Compatible Full Name in ID 18.</td>
</tr>
<tr class="even">
<td>19</td>
<td>Sample text; This can be the font name, or any other text that the designer thinks is the best sample to display the font in.</td>
</tr>
<tr class="odd">
<td>20</td>
<td><p>PostScript CID findfont name; Its presence in a font means that the nameID 6 holds a PostScript font name that is meant to be used with the "composefont" invocation in order to invoke the font in a PostScript interpreter. See the definition of name ID 6.</p>
<p>The value held in the name ID 20 string is interpreted as a PostScript font name that is meant to be used with the "findfont" invocation, in order to invoke the font in a PostScript interpreter.</p>
<p>If the name ID 20 is present in a font, there must be one name ID 20 record for every Macintosh platform cmap subtable in that font. A particular name ID 20 record is associated with the encoding specified by the matching cmap subtable. A name ID 20 record is matched to a cmap subtable when they have the same platform and platform-specific encoding IDs, and corresponding language/version IDs. Name ID 20 records are meant to be used only with Macintosh cmap subtables. The version field for a cmap subtable is one more than the language ID value for the corresponding name ID 20 record, with the exception of the cmap subtable version field 0. This version field, meaning "not language-specific", corresponds to the language ID value 0xFFFF, or decimal 65535, for the corresponding name ID 20 record.</p>
<p>When translated to ASCII, this name string must be restricted to the printable ASCII subset, codes 33 through 126, except for the 10 characters: '[', ']', '(', ')', '{', '}', '&lt;', '&gt;', '/', '%'.</p>
<p>Note that this specification applies only to data fork OpenType fonts. Macintosh resource-fork TrueType and other Macintosh sfnt-wrapped fonts supply the PostScript font name to be used with the "findfont" invocation, in order to invoke the font in a PostScript interpreter, in the FOND resource style-mapping table.</p>
<p>Note that a particular Name ID 20 string always corresponds to a particular Macintosh cmap subtable. However, some host OpenType/TTF fonts also contain a post table, format 4, which provides a mapping from glyph ID to encoding value, and also corresponds to a particular Macintosh cmap subtable. Unfortunately, the <a href="#chapter.post">post</a> table format 4 contains no provision for identifying which Macintosh cmap subtable it matches, nor for providing more than one mapping. Host fonts which contain a <a href="#chapter.post">post</a> table format 4, should also contain only a single Macintosh cmap subtable, and a single Name ID 20 string. In the case where there is more than one Macintosh cmap subtable and more than one Name ID 20 string, there is no definition of which one matches the <a href="#chapter.post">post</a> table format 4.</p></td>
</tr>
</tbody>
</table>

Note that while both Apple and Microsoft support the same set of name
strings, the interpretations may be somewhat different. But since name
strings are stored by platform, encoding and language (placing separate
strings in for both Apple and MS platforms), this should not present a
problem.

The key information for this table for MS fonts relates to the use of
strings 1, 2 and 4. To better help understand, here are some examples of
name usage, weight class and style flags:

| Font                     | Name ID 1    | Name ID 2   | Name ID 4                | Name ID 16 | Name ID 17         |
| ------------------------ | ------------ | ----------- | ------------------------ | ---------- | ------------------ |
| Arial Narrow             | Arial Narrow | Regular     | Arial Narrow             | Arial      | Narrow             |
| Arial Narrow Italic      | Arial Narrow | Italic      | Arial Narrow Italic      | Arial      | Narrow Italic      |
| Arial Narrow Bold        | Arial Narrow | Bold        | Arial Narrow Bold        | Arial      | Narrow Bold        |
| Arial Narrow Bold Italic | Arial Narrow | Bold Italic | Arial Narrow Bold Italic | Arial      | Narrow Bold Italic |
| Arial                    | Arial        | Regular     | Arial                    | Arial      |                    |
| Arial Italic             | Arial        | Italic      | Arial Italic             | Arial      | Italic             |
| Arial Bold               | Arial        | Bold        | Arial Bold               | Arial      | Bold               |
| Arial Bold Italic        | Arial        | Bold Italic | Arial Bold Italic        | Arial      | Bold Italic        |
| Arial Black              | Arial Black  | Regular     | Arial Black              | Arial      | Black              |
| Arial Black Italic       | Arial Black  | Italic      | Arial Black Italic       | Arial      | Black Italic       |

In addition to name strings, OS/2.usWeightClass, OS/2.usWidthClass,
OS/2.fsSelection style bits, and head.macStyle bits are shown. These
settings allow the fonts to fit together into a single family of varying
weight and compression/expansion.

| Font                     | OS/2 usWeightClass | OS/2 usWidthClass | OS/2 fsSelection Italic | OS/2 fsSelection Bold | OS/2 fsSelection Regular | head macStyle Bold | head macStyle Italic | head macStyle Condensed | head macStyle Extended |
| ------------------------ | ------------------ | ----------------- | ----------------------- | --------------------- | ------------------------ | ------------------ | -------------------- | ----------------------- | ---------------------- |
| Arial Narrow             | 400                | 3                 |                         |                       | x                        |                    |                      | x                       |                        |
| Arial Narrow Italic      | 400                | 3                 | x                       |                       |                          |                    | x                    | x                       |                        |
| Arial Narrow Bold        | 700                | 3                 |                         | x                     |                          | x                  |                      | x                       |                        |
| Arial Narrow Bold Italic | 700                | 3                 | x                       | x                     |                          | x                  | x                    | x                       |                        |
| Arial                    | 400                | 5                 |                         |                       | x                        |                    |                      |                         |                        |
| Arial Italic             | 400                | 5                 | x                       |                       |                          |                    | x                    |                         |                        |
| Arial Bold               | 700                | 5                 |                         | x                     |                          | x                  |                      |                         |                        |
| Arial Bold Italic        | 700                | 5                 | x                       | x                     |                          | x                  | x                    |                         |                        |
| Arial Black              | 900                | 5                 |                         | x                     |                          | x                  |                      |                         |                        |
| Arial Black Italic       | 900                | 5                 | x                       | x                     |                          | x                  | x                    |                         |                        |

Note that OS/2 and Windows both require that all name strings be defined
in Unicode. Thus all 'name' table strings for platform ID = 3
(Microsoft) will require two bytes per character. Macintosh fonts
require single byte strings.

Examples of how these strings might be defined:

0\. The copyright string from the font vendor. *© Copyright the Monotype
Corporation plc, 1990*

1\. The name the user sees. *Times New Roman*

2\. The name of the style. *Bold*

3\. A unique identifier that applications can store to identify the font
being used. Monotype: *Times New Roman Bold:1990*

4\. The complete, hopefully unique, human readable name of the font.
This name is used by Windows. *Times New Roman Bold*. (If this were the
Microsoft platform string for a CFF OpenType font, then the value would
be *TimesNewRoman-Bold*, as described in the definition of name ID 4
above.)

5\. Release and version information from the font vendor. *Version 1.00
June 1, 1990, initial release*

6\. The name the font will be known by on a PostScript printer.
*TimesNewRoman-Bold*

7\. Trademark string. *Times New Roman is a registered trademark of the
Monotype Corporation.*

8\. Manufacturer. *Monotype Corporation plc*

9\. Designer. *Stanley Morison*

10\. Description. *Designed in 1932 for the Times of London newspaper.
Excellent readability and a narrow overall width, allowing more words
per line than most fonts.*

11\. URL of Vendor. *http://www.monotype.com*

12\. URL of Designer. *http://www.monotype.com*

13\. License Description. *This font may be installed on all of your
machines and printers, but you may not sell or give these fonts to
anyone else.*

14\. License Info URL. *http://www.monotype.com/license/*

15\. Reserved. Set to zero.

16\. Preferred Family. No name string present, since it is the same as
name ID 1 (Font Family name).

17\. Preferred Subfamily. No name string present, since it is the same
as name ID 2 (Font Subfamily name).

18\. Compatible Full (Macintosh only). No name string present, since it
is the same as name ID 4 (Full name).

19\. Sample text. *The quick brown fox jumps over the lazy dog.*

20\. PostScript CID findfont name. No name string present. Thus, the
PostScript Name defined by name ID 6 should be used with the "findfont"
invocation for locating the font in the context of a PostScript
interpreter.

The following is an example of only name IDs 6 and 20 in the CFF
OpenType Japanese font Kozuka Mincho Std Regular (other name IDs are
also present in this font):

6\. PostScript name: *KozMinStd-Regular*. Since a name ID 20 is present
in the font (see below), then the PostScript name defined by name ID 6
should be used with the "composefont" invocation for locating the font
in the context of a PostScript interpreter.

20\. PostScript CID findfont name: *KozMinStd-Regular-83pv-RKSJ-H*, in a
name record of Platform 1 \[Macintosh\], Platform-specific script 1
\[Japanese\], Language: 0xFFFF \[English\]. This name string is a
PostScript name that should be used with the "findfont" invocation for
locating the font in the context of a PostScript interpreter, and is
associated with the encoding specified by the following cmap subtable,
which must be present in the font: Platform: 1 \[Macintosh\];
Platform-specific encoding: 1 \[Japanese\]; Language: 0 \[not
language-specific\].

### Annotation

In the example, string 19 is not set in italic like the other strings.

