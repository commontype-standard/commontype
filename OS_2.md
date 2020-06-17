# OS/2 - OS/2 and Windows Metrics

## Introduction

### Specification

The OS/2 table consists of a set of metrics that are required in
OpenType fonts. The fourth version of the OS/2 table (version 3)
follows:

| Type   | Name                | Description |
| ------ | ------------------- | ----------- |
| USHORT | version             | 0x0003      |
| SHORT  | xAvgCharWidth       |             |
| USHORT | usWeightClass       |             |
| USHORT | usWidthClass        |             |
| USHORT | fsType              |             |
| SHORT  | ySubscriptXSize     |             |
| SHORT  | ySubscriptYSize     |             |
| SHORT  | ySubscriptXOffset   |             |
| SHORT  | ySubscriptYOffset   |             |
| SHORT  | ySuperscriptXSize   |             |
| SHORT  | ySuperscriptYSize   |             |
| SHORT  | ySuperscriptXOffset |             |
| SHORT  | ySuperscriptYOffset |             |
| SHORT  | yStrikeoutSize      |             |
| SHORT  | yStrikeoutPosition  |             |
| SHORT  | sFamilyClass        |             |
| BYTE   | panose\[10\]        |             |
| ULONG  | ulUnicodeRange1     | Bits 0-31   |
| ULONG  | ulUnicodeRange2     | Bits 32-63  |
| ULONG  | ulUnicodeRange3     | Bits 64-95  |
| ULONG  | ulUnicodeRange4     | Bits 96-127 |
| CHAR   | achVendID\[4\]      |             |
| USHORT | fsSelection         |             |
| USHORT | usFirstCharIndex    |             |
| USHORT | usLastCharIndex     |             |
| SHORT  | sTypoAscender       |             |
| SHORT  | sTypoDescender      |             |
| SHORT  | sTypoLineGap        |             |
| USHORT | usWinAscent         |             |
| USHORT | usWinDescent        |             |
| ULONG  | ulCodePageRange1    | Bits 0-31   |
| ULONG  | ulCodePageRange2    | Bits 32-63  |
| SHORT  | sxHeight            |             |
| SHORT  | sCapHeight          |             |
| USHORT | usDefaultChar       |             |
| USHORT | usBreakChar         |             |
| USHORT | usMaxContext        |             |

**version**

Format: 2-byte unsigned short

Units: n/a

Title: OS/2 table version number.

Description: The version number for this OS/2 table.

Comments: The version number allows for identification of the precise
contents and layout for the OS/2 table. The version number for this
layout is three (3). Versions zero (0, TrueType rev 1.5), one (1,
TrueType rev 1.66) and two (2, OpenType rev 1.2) have been used
previously.

**xAvgCharWidth**

Format: 2-byte signed short

Units: Pels / em units

Title: Average weighted escapement.

Description: The Average Character Width parameter specifies the
arithmetic average of the escapement (width) of all non-zero width
glyphs in the font.

Comments: The value of xAvgCharWidth is calculated by obtaining the
arithmetic average of the width of all non-zero width glyphs in the
font. Furthermore, it is strongly recommended that implementers do not
rely on this value for computing layout for lines of text. Especially,
for cases where complex scripts are used.

**usWeightClass**

Format: 2-byte unsigned short

Title: Weight class.

Description: Indicates the visual weight (degree of blackness or
thickness of strokes) of the characters in the font.

Comments:

| Value | Description               | C Definition (from windows.h) |
| ----- | ------------------------- | ----------------------------- |
| 100   | Thin                      | FW\_THIN                      |
| 200   | Extra-light (Ultra-light) | FW\_EXTRALIGHT                |
| 300   | Light                     | FW\_LIGHT                     |
| 400   | Normal (Regular)          | FW\_NORMAL                    |
| 500   | Medium                    | FW\_MEDIUM                    |
| 600   | Semi-bold (Demi-bold)     | FW\_SEMIBOLD                  |
| 700   | Bold                      | FW\_BOLD                      |
| 800   | Extra-bold (Ultra-bold)   | FW\_EXTRABOLD                 |
| 900   | Black (Heavy)             | FW\_BLACK                     |

**usWidthClass**

Format: 2-byte unsigned short

Title: Width class.

Description: Indicates a relative change from the normal aspect ratio
(width to height ratio) as specified by a font designer for the glyphs
in a font.

Comments: Although every character in a font may have a different
numeric aspect ratio, each character in a font of normal width has a
relative aspect ratio of one. When a new type style is created of a
different width class (either by a font designer or by some automated
means) the relative aspect ratio of the characters in the new font is
some percentage greater or less than those same characters in the normal
font -- it is this difference that this parameter specifies.

| Value | Description     | C Definition             | % of normal |
| ----- | --------------- | ------------------------ | ----------- |
| 1     | Ultra-condensed | FWIDTH\_ULTRA\_CONDENSED | 50          |
| 2     | Extra-condensed | FWIDTH\_EXTRA\_CONDENSED | 62.5        |
| 3     | Condensed       | FWIDTH\_CONDENSED        | 75          |
| 4     | Semi-condensed  | FWIDTH\_SEMI\_CONDENSED  | 87.5        |
| 5     | Medium (normal) | FWIDTH\_NORMAL           | 100         |
| 6     | Semi-expanded   | FWIDTH\_SEMI\_EXPANDED   | 112.5       |
| 7     | Expanded        | FWIDTH\_EXPANDED         | 125         |
| 8     | Extra-expanded  | FWIDTH\_EXTRA\_EXPANDED  | 150         |
| 9     | Ultra-expanded  | FWIDTH\_ULTRA\_EXPANDED  | 200         |

**fsType**

Format: 2-byte unsigned short

Title: Type flags.

Description: Indicates font embedding licensing rights for the font.
Embeddable fonts may be stored in a document. When a document with
embedded fonts is opened on a system that does not have the font
installed (the remote system), the embedded font may be loaded for
temporary (and in some cases, permanent) use on that system by an
embedding-aware application. Embedding licensing rights are granted by
the vendor of the font.

The OpenType Font Embedding DLL Specification and DLL release notes
describe the APIs used to implement support for OpenType font embedding
and loading. *Applications that implement support for font embedding,
either through use of the Font Embedding DLL or through other means,
must not embed fonts which are not licensed to permit embedding.
Further, applications loading embedded fonts for temporary use (see
Preview & Print and Editable embedding below) must delete the fonts when
the document containing the embedded font is closed.*

This version of the OS/2 table makes bits 0 - 3 a set of exclusive bits.
In other words, at most one bit in this range may be set at a time. The
purpose is to remove misunderstandings caused by previous behavior of
using the least restrictive of the bits that are set.

| Bit   | BitMask | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       | 0x0000  | Installable Embedding: No fsType bit is set. Thus fsType is zero. Fonts with this setting indicate that they may be embedded and permanently installed on the remote system by an application. The user of the remote system acquires the identical rights, obligations and licenses for that font as the original purchaser of the font, and is subject to the same end-user license agreement, copyright, design patent, and/or trademark as was the original purchaser. |
| 0     | 0x0001  | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 1     | 0x0002  | Restricted License embedding: Fonts that have *only* this bit set must not be *modified, embedded or exchanged in any manner* without first obtaining permission of the legal owner. Caution: For Restricted License embedding to take effect, it must be the only level of embedding selected.                                                                                                                                                                            |
| 2     | 0x0004  | Preview & Print embedding: When this bit is set, the font may be embedded, and temporarily loaded on the remote system. Documents containing Preview & Print fonts must be opened "read-only;" no edits can be applied to the document.                                                                                                                                                                                                                                    |
| 3     | 0x0008  | Editable embedding: When this bit is set, the font may be embedded but must only be installed *temporarily* on other systems. In contrast to Preview & Print fonts, documents containing Editable fonts *may* be opened for reading, editing is permitted, and changes may be saved.                                                                                                                                                                                       |
| 4-7   |         | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 8     | 0x0100  | No subsetting: When this bit is set, the font may not be subsetted prior to embedding. Other embedding restrictions specified in bits 0-3 and 9 also apply.                                                                                                                                                                                                                                                                                                                |
| 9     | 0x0200  | Bitmap embedding only: When this bit is set, only bitmaps contained in the font may be embedded. No outline data may be embedded. If there are no bitmaps available in the font, then the font is considered unembeddable and the embedding services will fail. Other embedding restrictions specified in bits 0-3 and 8 also apply.                                                                                                                                       |
| 10-15 |         | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**ySubscriptXSize**

Format: 2-byte signed short

Units: Font design units

Title: Subscript horizontal font size.

Description: The recommended horizontal size in font design units for
subscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the em square size of the font being used for a subscript.
The horizontal font size specifies a font designer's recommended
horizontal font size for subscript characters associated with this font.
If a font does not include all of the required subscript characters for
an application, and the application can substitute characters by scaling
the character of a font or by substituting characters from another font,
this parameter specifies the recommended em square for those subscript
characters.

For example, if the em square for a font is 2048 and ySubScriptXSize is
set to 205, then the horizontal size for a simulated subscript character
would be 1/10th the size of the normal character.

**ySubscriptYSize**

Format: 2-byte signed short

Units: Font design units

Title: Subscript vertical font size.

Description: The recommended vertical size in font design units for
subscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.
numerics and other, the numeric sizes should be stressed. This size
field maps to the emHeight of the font being used for a subscript. The
horizontal font size specifies a font designer's recommendation for
horizontal font size of subscript characters associated with this font.
If a font does not include all of the required subscript characters for
an application, and the application can substitute characters by scaling
the characters in a font or by substituting characters from another
font, this parameter specifies the recommended horizontal EmInc for
those subscript characters.

For example, if the em square for a font is 2048 and ySubScriptYSize is
set to 205, then the vertical size for a simulated subscript character
would be 1/10th the size of the normal character.

**ySubscriptXOffset**

Format: 2-byte signed short

Units: Font design units

Title: Subscript x offset.

Description: The recommended horizontal offset in font design untis for
subscripts for this font.

Comments: The Subscript X Offset parameter specifies a font designer's
recommended horizontal offset -- from the character origin of the font
to the character origin of the subscript's character -- for subscript
characters associated with this font. If a font does not include all of
the required subscript characters for an application, and the
application can substitute characters, this parameter specifies the
recommended horizontal position from the character escapement point of
the last character before the first subscript character. For upright
characters, this value is usually zero; however, if the characters of a
font have an incline (italic characters) the reference point for
subscript characters is usually adjusted to compensate for the angle of
incline.

**ySubscriptYOffset**

Format: 2-byte signed short

Units: Font design units

Title: Subscript y offset.

Description: The recommended vertical offset in font design units from
the baseline for subscripts for this font.

Comments: The Subscript Y Offset parameter specifies a font designer's
recommended vertical offset from the character baseline to the character
baseline for subscript characters associated with this font. Values are
expressed as a positive offset below the character baseline. If a font
does not include all of the required subscript for an application, this
parameter specifies the recommended vertical distance below the
character baseline for those subscript characters.

**ySuperscriptXSize**

Format: 2-byte signed short

Units: Font design units

Title: Superscript horizontal font size.

Description: The recommended horizontal size in font design units for
superscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the em square size of the font being used for a subscript.
The horizontal font size specifies a font designer's recommended
horizontal font size for superscript characters associated with this
font. If a font does not include all of the required superscript
characters for an application, and the application can substitute
characters by scaling the character of a font or by substituting
characters from another font, this parameter specifies the recommended
em square for those superscript characters.

For example, if the em square for a font is 2048 and ySuperScriptXSize
is set to 205, then the horizontal size for a simulated superscript
character would be 1/10th the size of the normal character.

**ySuperscriptYSize**

Format: 2-byte signed short

Units: Font design units

Title: Superscript vertical font size.

Description: The recommended vertical size in font design units for
superscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the emHeight of the font being used for a subscript. The
vertical font size specifies a font designer's recommended vertical font
size for superscript characters associated with this font. If a font
does not include all of the required superscript characters for an
application, and the application can substitute characters by scaling
the character of a font or by substituting characters from another font,
this parameter specifies the recommended EmHeight for those superscript
characters.

For example, if the em square for a font is 2048 and ySuperScriptYSize
is set to 205, then the vertical size for a simulated superscript
character would be 1/10th the size of the normal character.

**ySuperscriptXOffset**

Format: 2-byte signed short

Units: Font design units

Title: Superscript x offset.

Description: The recommended horizontal offset in font design units for
superscripts for this font.

Comments: The Superscript X Offset parameter specifies a font designer's
recommended horizontal offset -- from the character origin to the
superscript character's origin for the superscript characters associated
with this font. If a font does not include all of the required
superscript characters for an application, this parameter specifies the
recommended horizontal position from the escapement point of the
character before the first superscript character. For upright
characters, this value is usually zero; however, if the characters of a
font have an incline (italic characters) the reference point for
superscript characters is usually adjusted to compensate for the angle
of incline.

**ySuperscriptYOffset**

Format: 2-byte signed short

Units: Font design units

Title: Superscript y offset.

Description: The recommended vertical offset in font design units from
the baseline for superscripts for this font.

Comments: The Superscript Y Offset parameter specifies a font designer's
recommended vertical offset -- from the character baseline to the
superscript character's baseline associated with this font. Values for
this parameter are expressed as a positive offset above the character
baseline. If a font does not include all of the required superscript
characters for an application, this parameter specifies the recommended
vertical distance above the character baseline for those superscript
characters.

**yStrikeoutSize**

Format: 2-byte signed short

Units: Font design units

Title: Strikeout size.

Description: Width of the strikeout stroke in font design units.

Comments: This field should normally be the width of the em dash for the
current font. If the size is one, the strikeout line will be the line
represented by the strikeout position field. If the value is two, the
strikeout line will be the line represented by the strikeout position
and the line immediately above the strikeout position. For a Roman font
with a 2048 em square, 102 is suggested.

**yStrikeoutPosition**

Format: 2-byte signed short

Units: Font design units

Title: Strikeout position.

Description: The position of the top of the strikeout stroke relative to
the baseline in font design units.

Comments: Positive values represent distances above the baseline, while
negative values represent distances below the baseline. A value of zero
falls directly on the baseline, while a value of one falls one pel above
the baseline. The value of strikeout position should not interfere with
the recognition of standard characters, and therefore should not line up
with crossbars in the font. For a Roman font with a 2048 em square, 460
is suggested.

**sFamilyClass**

Format: 2-byte signed short

Title: Font-family class and subclass.

Description: This parameter is a classification of font-family design.

Comments: The font class and font subclass are registered values
assigned by IBM to each font family. This parameter is intended for use
in selecting an alternate font when the requested font is not available.
The font class is the most general and the font subclass is the most
specific. The high byte of this field contains the family class, while
the low byte contains the family subclass. More information about this
field.

**Panose**

Format: 10 byte array

Title: PANOSE classification number

International: Additional specifications are required for PANOSE to
classify non-Latin character sets.

Description: This 10 byte series of numbers is used to describe the
visual characteristics of a given typeface. These characteristics are
then used to associate the font with other fonts of similar appearance
having different names. The variables for each digit are listed below.
The Panose values are fully described in the Panose "greybook"
reference, currently owned by Agfa-Monotype.

Comments: The PANOSE definition contains ten digits each of which
currently describes up to sixteen variations. Windows uses bFamilyType,
bSerifStyle and bProportion in the font mapper to determine family type.
It also uses bProportion to determine if the font is monospaced. If the
font is a symbol font, the first byte of the PANOSE number (bFamilyType)
must be set to "pictorial." Good PANOSE values in fonts are very
valuable to users of the Windows fonts folder. The specification for
assigning PANOSE values is located at
<http://www.panose.com/hardware/pan2.asp>.

| Type | Name             |
| ---- | ---------------- |
| BYTE | bFamilyType      |
| BYTE | bSerifStyle      |
| BYTE | bWeight          |
| BYTE | bProportion;     |
| BYTE | bContrast        |
| BYTE | bStrokeVariation |
| BYTE | bArmStyle        |
| BYTE | bLetterform      |
| BYTE | bMidline         |
| BYTE | bXHeight         |

**ulUnicodeRange1 (Bits 0-31)**

**ulUnicodeRange2 (Bits 32-63)**

**ulUnicodeRange3 (Bits 64-95)**

**ulUnicodeRange4 (Bits 96-127)**

Format: 32-bit unsigned long(4 copies) totaling 128 bits.

Title: Unicode Character Range

Description: This field is used to specify the Unicode blocks or ranges
encompassed by the font file in the [cmap](#chapter.cmap) subtable for
platform 3, encoding ID 1 (Microsoft platform). If the bit is set (1)
then the Unicode range is considered functional. If the bit is clear (0)
then the range is not considered functional. Each of the bits is treated
as an independent flag and the bits can be set in any combination. The
determination of "functional" is left up to the font designer, although
character set selection should attempt to be functional by ranges if at
all possible.

All reserved fields must be zero. Each long is in Big-Endian form. See
the Basic Multilingual Plane of ISO/IEC 10646-1 or the Unicode Standard
v.3.0 for the list of Unicode ranges and characters.

| Bit    | Description                             |
| ------ | --------------------------------------- |
| 0      | Basic Latin                             |
| 1      | Latin-1 Supplement                      |
| 2      | Latin Extended-A                        |
| 3      | Latin Extended-B                        |
| 4      | IPA Extensions                          |
| 5      | Spacing Modifier Letters                |
| 6      | Combining Diacritical Marks             |
| 7      | Greek and Coptic                        |
| 8      | Reserved for Unicode SubRanges          |
| 9      | Cyrillic                                |
|        | Cyrillic Supplementary                  |
| 10     | Armenian                                |
| 11     | Hebrew                                  |
| 12     | Reserved for Unicode SubRanges          |
| 13     | Arabic                                  |
| 14     | Reserved for Unicode SubRanges          |
| 15     | Devanagari                              |
| 16     | Bengali                                 |
| 17     | Gurmukhi                                |
| 18     | Gujarati                                |
| 19     | Oriya                                   |
| 20     | Tamil                                   |
| 21     | Telugu                                  |
| 22     | Kannada                                 |
| 23     | Malayalam                               |
| 24     | Thai                                    |
| 25     | Lao                                     |
| 26     | Georgian                                |
| 27     | Reserved for Unicode SubRanges          |
| 28     | Hangul Jamo                             |
| 29     | Latin Extended Additional               |
| 30     | Greek Extended                          |
| 31     | General Punctuation                     |
| 32     | Superscripts And Subscripts             |
| 33     | Currency Symbols                        |
| 34     | Combining Diacritical Marks For Symbols |
| 35     | Letterlike Symbols                      |
| 36     | Number Forms                            |
| 37     | Arrows                                  |
|        | Supplemental Arrows-A                   |
|        | Supplemental Arrows-B                   |
| 38     | Mathematical Operators                  |
|        | Supplemental Mathematical Operators     |
|        | Miscellaneous Mathematical Symbols-A    |
|        | Miscellaneous Mathematical Symbols-B    |
| 39     | Miscellaneous Technical                 |
| 40     | Control Pictures                        |
| 41     | Optical Character Recognition           |
| 42     | Enclosed Alphanumerics                  |
| 43     | Box Drawing                             |
| 44     | Block Elements                          |
| 45     | Geometric Shapes                        |
| 46     | Miscellaneous Symbols                   |
| 47     | Dingbats                                |
| 48     | CJK Symbols And Punctuation             |
| 49     | Hiragana                                |
| 50     | Katakana                                |
|        | Katakana Phonetic Extensions            |
| 51     | Bopomofo                                |
|        | Bopomofo Extended                       |
|        | Extended Bopomofo                       |
| 52     | Hangul Compatibility Jamo               |
| 53     | Reserved for Unicode SubRanges          |
| 54     | Enclosed CJK Letters And Months         |
| 55     | CJK Compatibility                       |
| 56     | Hangul Syllables                        |
| 57     | Non-Plane 0\[4\]                        |
| 58     | Reserved for Unicode SubRanges          |
| 59     | CJK Unified Ideographs                  |
|        | CJK Radicals Supplement                 |
|        | Kangxi Radicals                         |
|        | Ideographic Description Characters      |
|        | CJK Unified Ideograph Extension A       |
|        | CJK Unified Ideograph Extension B       |
|        | Kanbun                                  |
| 60     | Private Use Area                        |
| 61     | CJK Compatibility Ideographs            |
|        | CJK Compatibility Ideographs Supplement |
| 62     | Alphabetic Presentation Forms           |
| 63     | Arabic Presentation Forms-A             |
| 64     | Combining Half Marks                    |
| 65     | CJK Compatibility Forms                 |
| 66     | Small Form Variants                     |
| 67     | Arabic Presentation Forms-B             |
| 68     | Halfwidth And Fullwidth Forms           |
| 69     | Specials                                |
| 70     | Tibetan                                 |
| 71     | Syriac                                  |
| 72     | Thaana                                  |
| 73     | Sinhala                                 |
| 74     | Myanmar                                 |
| 75     | Ethiopic                                |
| 76     | Cherokee                                |
| 77     | Unified Canadian Aboriginal Syllabics   |
| 78     | Ogham                                   |
| 79     | Runic                                   |
| 80     | Khmer                                   |
| 81     | Mongolian                               |
| 82     | Braille Patterns                        |
| 83     | Yi Syllables                            |
|        | Yi Radicals                             |
| 84     | Tagalog                                 |
|        | Hanunoo                                 |
|        | Buhid                                   |
|        | Tagbanwa                                |
| 85     | Old Italic                              |
| 86     | Gothic                                  |
| 87     | Deseret                                 |
| 88     | Byzantine Musical Symbols               |
|        | Musical Symbols                         |
| 89     | Mathematical Alphanumeric Symbols       |
| 90     | Private Use (plane 15)                  |
|        | Private Use (plane 16)                  |
| 91     | Variation Selectors                     |
| 92     | Tags                                    |
| 93-127 | Reserved for Unicode SubRanges          |

**achVendID**

Format: 4-byte character array

Title: Font Vendor Identification

Description: The four character identifier for the vendor of the given
type face.

Comments: This is not the royalty owner of the original artwork. This is
the company responsible for the marketing and distribution of the
typeface that is being classified. It is reasonable to assume that there
will be 6 vendors of ITC Zapf Dingbats for use on desktop platforms in
the near future (if not already). It is also likely that the vendors
will have other inherent benefits in their fonts (more kern pairs,
unregularized data, hand hinted, etc.). This identifier will allow for
the correct vendor's type to be used over another, possibly inferior,
font file. The Vendor ID value is not required.

Microsoft has assigned values for some font suppliers as listed below.
Uppercase vendor ID's are reserved by Microsoft. Other suppliers can
choose their own mixed case or lowercase ID's, or leave the field blank.

For a list of registered Vendor id's see our [Registered
'vendors'](http://www.microsoft.com/typography/links/vendorlist.asp)
links page.

**fsSelection**

Format: 2-byte bit field.

Title: Font selection flags.

Description: Contains information concerning the nature of the font
patterns, as follows:

| Bit \# | macStyle bit | C Definition | Description                                                  |
| ------ | ------------ | ------------ | ------------------------------------------------------------ |
| 0      | bit 1        | ITALIC       | Font contains Italic characters, otherwise they are upright. |
| 1      |              | UNDERSCORE   | Characters are underscored.                                  |
| 2      |              | NEGATIVE     | Characters have their foreground and background reversed.    |
| 3      |              | OUTLINED     | Outline (hollow) characters, otherwise they are solid.       |
| 4      |              | STRIKEOUT    | Characters are overstruck                                    |
| 5      | bit 0        | BOLD         | Characters are emboldened.                                   |
| 6      |              | REGULAR      | Characters are in the standard weight/style for the font.    |

Comments: All undefined bits must be zero.

This field contains information on the original design of the font. Bits
0 & 5 can be used to determine if the font was designed with these
features or whether some type of machine simulation was performed on the
font to achieve this appearance. Bits 1-4 are rarely used bits that
indicate the font is primarily a decorative or special purpose font.

If bit 6 is set, then bits 0 and 5 must be clear, else the behavior is
undefined. As noted above, the settings of bits 0 and 1 must be
reflected in the macStyle bits in the [head](#chapter.head) table. While
bit 6 on implies that bits 0 and 1 of macStyle are clear (along with
bits 0 and 5 of fsSelection), the reverse is not true. Bits 0 and 1 of
macStyle (and 0 and 5 of fsSelection) may be clear and that does not
give any indication of whether or not bit 6 of fsSelection is clear
(e.g., Arial Light would have all bits cleared; it is not the regular
version of Arial).

**usFirstCharIndex**

Format: 2-byte USHORT

Description: The minimum Unicode index (character code) in this font,
according to the cmap subtable for platform ID 3 and platform- specific
encoding ID 0 or 1. For most fonts supporting Win-ANSI or other
character sets, this value would be 0x0020. This field cannot represent
supplementary character values (codepoints greater than 0xFFFF). Fonts
that support supplementary characters should set the value in this field
to 0xFFFF if the minimum index value is a supplementary character.

**usLastCharIndex**

Format: 2-byte USHORT

Description: The maximum Unicode index (character code) in this font,
according to the cmap subtable for platform ID 3 and encoding ID 0 or 1.
This value depends on which character sets the font supports. This field
cannot represent supplementary character values (codepoints greater than
0xFFFF). Fonts that support supplementary characters should set the
value in this field to 0xFFFF.

**sTypoAscender**

Format: SHORT

Description: The typographic ascender for this font. Remember that this
is not the same as the Ascender value in the [hhea](#chapter.hhea)
table, which Apple defines in a far different manner. One good source
for sTypoAscender in Latin based fonts is the Ascender value from an AFM
file. For CJK fonts see below.

The suggested usage for sTypoAscender is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. The goal is to free applications from Macintosh or
Windows-specific metrics which are constrained by backward compatibility
requirements. These new metrics, when combined with the character design
widths, will allow applications to lay out documents in a
typographically correct and portable fashion. These metrics will be
exposed through Windows APIs. Macintosh applications will need to access
the 'sfnt' resource and parse it to extract this data from the
[OS/2](#chapter.OS2) table.

For CJK (Chinese, Japanese, and Korean) fonts that are intended to be
used for vertical writing (in addition to horizontal writing), the
required value for sTypoAscender is that which describes the top of the
of the ideographic em-box. For example, if the ideographic em-box of the
font extends from coordinates 0,-120 to 1000,880 (that is, a 1000x1000
box set 120 design units below the Latin baseline), then the value of
sTypoAscender must be set to 880. Failing to adhere to these
requirements will result in incorrect vertical layout.

Also see the Recommendations Section for more on this field.

**sTypoDescender**

Format: SHORT

Description: The typographic descender for this font. Remember that this
is not the same as the Descender value in the [hhea](#chapter.hhea)
table, which Apple defines in a far different manner. One good source
for sTypoDescender in Latin based fonts is the Descender value from an
AFM file. For CJK fonts see below.

The suggested usage for sTypoDescender is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. The goal is to free applications from Macintosh or
Windows-specific metrics which are constrained by backward compatability
requirements. These new metrics, when combined with the character design
widths, will allow applications to lay out documents in a
typographically correct and portable fashion. These metrics will be
exposed through Windows APIs. Macintosh applications will need to access
the 'sfnt' resource and parse it to extract this data from the
[OS/2](#chapter.OS2) table (unless Apple exposes the
[OS/2](#chapter.OS2) table through a new API).

For CJK (Chinese, Japanese, and Korean) fonts that are intended to be
used for vertical writing (in addition to horizontal writing), the
required value for sTypoDescender is that which describes the bottom of
the of the ideographic em-box. For example, if the ideographic em-box of
the font extends from coordinates 0,-120 to 1000,880 (that is, a
1000x1000 box set 120 design units below the Latin baseline), then the
value of sTypoDescender must be set to -120. Failing to adhere to these
requirements will result in incorrect vertical layout.

Also see the Recommendations Section for more on this field.

**sTypoLineGap**

Format: 2-byte SHORT

Description: The typographic line gap for this font. Remember that this
is not the same as the LineGap value in the [hhea](#chapter.hhea) table,
which Apple defines in a far different manner.

The suggested usage for usTypoLineGap is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. Typical values average 7-10% of units per em. The goal is to
free applications from Macintosh or Windows-specific metrics which are
constrained by backward compatability requirements (see chapter,
"Recommendations for OpenType Fonts"). These new metrics, when combined
with the character design widths, will allow applications to lay out
documents in a typographically correct and portable fashion. These
metrics will be exposed through Windows APIs. Macintosh applications
will need to access the 'sfnt' resource and parse it to extract this
data from the [OS/2](#chapter.OS2) table (unless Apple exposes the
[OS/2](#chapter.OS2) table through a new API)

**usWinAscent**

Format: 2-byte USHORT

Description: The ascender metric for Windows. This, too, is distinct
from Apple's Ascender value and from the usTypoAscender values.
usWinAscent is computed as the yMax for all characters in the Windows
ANSI character set. usWinAscent is used to compute the Windows font
height and default line spacing. For platform 3 encoding 0 fonts, it is
the same as yMax. Windows will clip the bitmap of any portion of a glyph
that appears above this value. Some applications use this value to
determine default line spacing. This is strongly discouraged. The
typographic ascender, descender and line gap fields in conjunction with
unitsPerEm should be used for this purpose. Developers should set this
field keeping the above factors in mind.

If any clipping is unacceptable, then the value should be set to yMax.

However, if a developer desires to provide appropriate default line
spacing using this field, for those applications that continue to use
this field for doing so (against OpenType recommendations), then the
value should be set appropriately. In such a case, it may result in some
glyph bitmaps being clipped.

**usWinDescent**

Format: 2-byte USHORT

Description: The descender metric for Windows. This, too, is distinct
from Apple's Descender value and from the usTypoDescender values.
usWinDescent is computed as the -yMin for all characters in the Windows
ANSI character set. usWinDescent is used to compute the Windows font
height and default line spacing. For platform 3 encoding 0 fonts, it is
the same as -yMin. Windows will clip the bitmap of any portion of a
glyph that appears below this value. Some applications use this value to
determine default line spacing. This is strongly discouraged. The
typographic ascender, descender and line gap fields in conjunction with
unitsPerEm should be used for this purpose. Developers should set this
field keeping the above factors in mind.

If any clipping is unacceptable, then the value should be set to yMin.

However, if a developer desires to provide appropriate default line
spacing using this field, for those applications that continue to use
this field for doing so (against OpenType recommendations), then the
value should be set appropriately. In such a case, it may result in some
glyph bitmaps being clipped.

**ulCodePageRange1 Bits 0-31**

**ulCodePageRange2 Bits 32-63**

Format: 32-bit unsigned long(2 copies) totaling 64 bits.

Title: Code Page Character Range

Description: This field is used to specify the code pages encompassed by
the font file in the [cmap](#chapter.cmap) subtable for platform 3,
encoding ID 1 (Microsoft platform). If the font file is encoding ID 0,
then the Symbol Character Set bit should be set. If the bit is set (1)
then the code page is considered functional. If the bit is clear (0)
then the code page is not considered functional. Each of the bits is
treated as an independent flag and the bits can be set in any
combination. The determination of "functional" is left up to the font
designer, although character set selection should attempt to be
functional by code pages if at all possible.

Symbol character sets have a special meaning. If the symbol bit (31) is
set, and the font file contains a [cmap](#chapter.cmap) subtable for
platform of 3 and encoding ID of 1, then all of the characters in the
Unicode range 0xF000 - 0xF0FF (inclusive) will be used to enumerate the
symbol character set. If the bit is not set, any characters present in
that range will not be enumerated as a symbol character set.

All reserved fields must be zero. Each long is in Big-Endian form.

| Bit   | Code | Page Description                                 |
| ----- | ---- | ------------------------------------------------ |
| 0     | 1252 | Latin 1                                          |
| 1     | 1250 | Latin 2: Eastern Europe                          |
| 2     | 1251 | Cyrillic                                         |
| 3     | 1253 | Greek                                            |
| 4     | 1254 | Turkish                                          |
| 5     | 1255 | Hebrew                                           |
| 6     | 1256 | Arabic                                           |
| 7     | 1257 | Windows Baltic                                   |
| 8     | 1258 | Vietnamese                                       |
| 9-15  |      | Reserved for Alternate ANSI                      |
| 16    | 874  | Thai                                             |
| 17    | 932  | JIS/Japan                                        |
| 18    | 936  | Chinese: Simplified chars--PRC and Singapore     |
| 19    | 949  | Korean Wansung                                   |
| 20    | 950  | Chinese: Traditional chars--Taiwan and Hong Kong |
| 21    | 1361 | Korean Johab                                     |
| 22-28 |      | Reserved for Alternate ANSI & OEM                |
| 29    |      | Macintosh Character Set (US Roman)               |
| 30    |      | OEM Character Set                                |
| 31    |      | Symbol Character Set                             |
| 32-47 |      | Reserved for OEM                                 |
| 48    | 869  | IBM Greek                                        |
| 49    | 866  | MS-DOS Russian                                   |
| 50    | 865  | MS-DOS Nordic                                    |
| 51    | 864  | Arabic                                           |
| 52    | 863  | MS-DOS Canadian French                           |
| 53    | 862  | Hebrew                                           |
| 54    | 861  | MS-DOS Icelandic                                 |
| 55    | 860  | MS-DOS Portuguese                                |
| 56    | 857  | IBM Turkish                                      |
| 57    | 855  | IBM Cyrillic; primarily Russian                  |
| 58    | 852  | Latin 2                                          |
| 59    | 775  | MS-DOS Baltic                                    |
| 60    | 737  | Greek; former 437 G                              |
| 61    | 708  | Arabic; ASMO 708                                 |
| 62    | 850  | WE/Latin 1                                       |
| 63    | 437  | US                                               |

**sxHeight**

Format: SHORT

Description: This metric specifies the distance between the baseline and
the approximate height of non-ascending lowercase letters measured in
FUnits. This value would normally be specified by a type designer but in
situations where that is not possible, for example when a legacy font is
being converted, the value may be set equal to the top of the unscaled
and unhinted glyph bounding box of the glyph encoded at U+0078 (LATIN
SMALL LETTER X). If no glyph is encoded in this position the field
should be set to 0.

This metric, if specified, can be used in font substitution: the xHeight
value of one font can be scaled to approximate the apparent size of
another.

**sCapHeight**

Format: SHORT

Description: This metric specifies the distance between the baseline and
the approximate height of uppercase letters measured in FUnits. This
value would normally be specified by a type designer but in situations
where that is not possible, for example when a legacy font is being
converted, the value may be set equal to the top of the unscaled and
unhinted glyph bounding box of the glyph encoded at U+0048 (LATIN
CAPITAL LETTER H). If no glyph is encoded in this position the field
should be set to 0.

This metric, if specified, can be used in systems that specify type size
by capital height measured in millimeters. It can also be used as an
alignment metric; the top of a drop capital, for instance, can be
aligned to the sCapHeight metric of the first line of text.

**usDefaultChar**

Format: USHORT

Description: Whenever a request is made for a character that is not in
the font, Windows provides this default character. If the value of this
field is zero, glyph ID 0 is to be used for the default character
otherwise this is the Unicode encoding of the glyph that Windows uses as
the default character. This field cannot represent supplementary
character values (codepoints greater than 0xFFFF).

**usBreakChar**

Format: USHORT

Description: This is the Unicode encoding of the glyph that Windows uses
as the break character. The break character is used to separate words
and justify text. Most fonts specify 'space' as the break character.
This field cannot represent supplementary character values (codepoints
greater than 0xFFFF).

**usMaxContext**

Format: USHORT

Description: The maximum length of a target glyph context for any
feature in this font. For example, a font which has only a pair kerning
feature should set this field to 2. If the font also has a ligature
feature in which the glyph sequence 'f f i' is substituted by the
ligature 'ffi', then this field should be set to 3. This field could be
useful to sophisticated line-breaking engines in determining how far
they should look ahead to test whether something could change that
effects the line breaking. For chaining contextual lookups, the length
of the string (covered glyph) + (input sequence) + (lookahead sequence)
should be considered.

### Specification

The OS/2 table consists of a set of metrics that are required in
OpenType fonts. The fourth version of the OS/2 table (version 3)
follows:

| Type   | Name                | Description |
| ------ | ------------------- | ----------- |
| USHORT | version             | 0x0003      |
| SHORT  | xAvgCharWidth       |             |
| USHORT | usWeightClass       |             |
| USHORT | usWidthClass        |             |
| USHORT | fsType              |             |
| SHORT  | ySubscriptXSize     |             |
| SHORT  | ySubscriptYSize     |             |
| SHORT  | ySubscriptXOffset   |             |
| SHORT  | ySubscriptYOffset   |             |
| SHORT  | ySuperscriptXSize   |             |
| SHORT  | ySuperscriptYSize   |             |
| SHORT  | ySuperscriptXOffset |             |
| SHORT  | ySuperscriptYOffset |             |
| SHORT  | yStrikeoutSize      |             |
| SHORT  | yStrikeoutPosition  |             |
| SHORT  | sFamilyClass        |             |
| BYTE   | panose\[10\]        |             |
| ULONG  | ulUnicodeRange1     | Bits 0-31   |
| ULONG  | ulUnicodeRange2     | Bits 32-63  |
| ULONG  | ulUnicodeRange3     | Bits 64-95  |
| ULONG  | ulUnicodeRange4     | Bits 96-127 |
| CHAR   | achVendID\[4\]      |             |
| USHORT | fsSelection         |             |
| USHORT | usFirstCharIndex    |             |
| USHORT | usLastCharIndex     |             |
| SHORT  | sTypoAscender       |             |
| SHORT  | sTypoDescender      |             |
| SHORT  | sTypoLineGap        |             |
| USHORT | usWinAscent         |             |
| USHORT | usWinDescent        |             |
| ULONG  | ulCodePageRange1    | Bits 0-31   |
| ULONG  | ulCodePageRange2    | Bits 32-63  |
| SHORT  | sxHeight            |             |
| SHORT  | sCapHeight          |             |
| USHORT | usDefaultChar       |             |
| USHORT | usBreakChar         |             |
| USHORT | usMaxContext        |             |

**version**

Format: 2-byte unsigned short

Units: n/a

Title: OS/2 table version number.

Description: The version number for this OS/2 table.

Comments: The version number allows for identification of the precise
contents and layout for the OS/2 table. The version number for this
layout is two (2). Versions one (1) and zero (0) have been used
previously, in rev.1.66 and 1.5, respectively, of the TrueType
specification.

**xAvgCharWidth**

Format: 2-byte signed short

Units: Pels / em units

Title: Average weighted escapement.

Description: The Average Character Width parameter specifies the
arithmetic average of the escapement (width) of all of the 26 lowercase
letters a through z of the Latin alphabet and the space character. If
any of the 26 lowercase letters are not present, this parameter should
equal the weighted average of all glyphs in the font. For non-UGL
(platform 3, encoding 0) fonts, use the unweighted average.

Comments: This parameter is a descriptive attribute of the font that
specifies the spacing of characters for comparing one font to another
for selection or substitution. For proportionally spaced fonts, this
value is useful in estimating the length for lines of text. The
weighting factors provided with this example are only valid for Latin
lowercase letters. If other character sets, or capital letters are used,
the corresponding frequency of use values should be used. One needs to
be careful when comparing fonts that use different frequency of use
values for font mapping. The average character width for the following
set of upper and lowercase letters only, is calculated according to this
formula: Sum the individual character widths multiplied by the following
weighting factors and then divide by 1000. For example:

| Letter | Weight Factor |
| ------ | ------------- |
| a      | 64            |
| b      | 14            |
| c      | 27            |
| d      | 35            |
| e      | 100           |
| f      | 20            |
| g      | 14            |
| h      | 42            |
| i      | 63            |
| j      | 3             |
| k      | 6             |
| l      | 35            |
| m      | 20            |
| n      | 56            |
| o      | 56            |
| p      | 17            |
| q      | 4             |
| r      | 49            |
| s      | 56            |
| t      | 71            |
| u      | 31            |
| v      | 10            |
| w      | 18            |
| x      | 3             |
| y      | 18            |
| z      | 2             |
| space  | 166           |

**usWeightClass**

Format: 2-byte unsigned short

Title: Weight class.

Description: Indicates the visual weight (degree of blackness or
thickness of strokes) of the characters in the font.

Comments:

| Value | Description               | C Definition (from windows.h) |
| ----- | ------------------------- | ----------------------------- |
| 100   | Thin                      | FW\_THIN                      |
| 200   | Extra-light (Ultra-light) | FW\_EXTRALIGHT                |
| 300   | Light                     | FW\_LIGHT                     |
| 400   | Normal (Regular)          | FW\_NORMAL                    |
| 500   | Medium                    | FW\_MEDIUM                    |
| 600   | Semi-bold (Demi-bold)     | FW\_SEMIBOLD                  |
| 700   | Bold                      | FW\_BOLD                      |
| 800   | Extra-bold (Ultra-bold)   | FW\_EXTRABOLD                 |
| 900   | Black (Heavy)             | FW\_BLACK                     |

**usWidthClass**

Format: 2-byte unsigned short

Title: Width class.

Description: Indicates a relative change from the normal aspect ratio
(width to height ratio) as specified by a font designer for the glyphs
in a font.

Comments: Although every character in a font may have a different
numeric aspect ratio, each character in a font of normal width has a
relative aspect ratio of one. When a new type style is created of a
different width class (either by a font designer or by some automated
means) the relative aspect ratio of the characters in the new font is
some percentage greater or less than those same characters in the normal
font -- it is this difference that this parameter specifies.

| Value | Description     | C Definition             | % of normal |
| ----- | --------------- | ------------------------ | ----------- |
| 1     | Ultra-condensed | FWIDTH\_ULTRA\_CONDENSED | 50          |
| 2     | Extra-condensed | FWIDTH\_EXTRA\_CONDENSED | 62.5        |
| 3     | Condensed       | FWIDTH\_CONDENSED        | 75          |
| 4     | Semi-condensed  | FWIDTH\_SEMI\_CONDENSED  | 87.5        |
| 5     | Medium (normal) | FWIDTH\_NORMAL           | 100         |
| 6     | Semi-expanded   | FWIDTH\_SEMI\_EXPANDED   | 112.5       |
| 7     | Expanded        | FWIDTH\_EXPANDED         | 125         |
| 8     | Extra-expanded  | FWIDTH\_EXTRA\_EXPANDED  | 150         |
| 9     | Ultra-expanded  | FWIDTH\_ULTRA\_EXPANDED  | 200         |

**fsType**

Format: 2-byte unsigned short

Title: Type flags.

Description: Indicates font embedding licensing rights for the font.
Embeddable fonts may be stored in a document. When a document with
embedded fonts is opened on a system that does not have the font
installed (the remote system), the embedded font may be loaded for
temporary (and in some cases, permanent) use on that system by an
embedding-aware application. Embedding licensing rights are granted by
the vendor of the font.

The OpenType Font Embedding DLL Specification and DLL release notes
describe the APIs used to implement support for OpenType font embedding
and loading. *Applications that implement support for font embedding,
either through use of the Font Embedding DLL or through other means,
must not embed fonts which are not licensed to permit embedding.
Further, applications loading embedded fonts for temporary use (see
Preview & Print and Editable embedding below) must delete the fonts when
the document containing the embedded font is closed.*

| Bit   | BitMask | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ----- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       | 0x0000  | Installable Embedding: No fsType bit is set. Thus fsType is zero. Fonts with this setting indicate that they may be embedded and permanently installed on the remote system by an application. The user of the remote system acquires the identical rights, obligations and licenses for that font as the original purchaser of the font, and is subject to the same end-user license agreement, copyright, design patent, and/or trademark as was the original purchaser. |
| 0     | 0x0001  | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 1     | 0x0002  | Restricted License embedding: Fonts that have *only* this bit set must not be *modified, embedded or exchanged in any manner* without first obtaining permission of the legal owner. Caution: For Restricted License embedding to take effect, it must be the only level of embedding selected.                                                                                                                                                                            |
| 2     | 0x0004  | Preview & Print embedding: When this bit is set, the font may be embedded, and temporarily loaded on the remote system. Documents containing Preview & Print fonts must be opened "read-only;" no edits can be applied to the document.                                                                                                                                                                                                                                    |
| 3     | 0x0008  | Editable embedding: When this bit is set, the font may be embedded but must only be installed *temporarily* on other systems. In contrast to Preview & Print fonts, documents containing Editable fonts *may* be opened for reading, editing is permitted, and changes may be saved.                                                                                                                                                                                       |
| 4-7   |         | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 8     | 0x0100  | No subsetting: When this bit is set, the font may not be subsetted prior to embedding. Other embedding restrictions specified in the lower byte also apply.                                                                                                                                                                                                                                                                                                                |
| 9     | 0x0200  | Bitmap embedding only: When this bit is set, only bitmaps contained in the font may be embedded. No outline data may be embedded. If there are no bitmaps available in the font, then the font is considered unembeddable and the embedding services will fail. Other embedding restrictions specified in the lower byte also apply.                                                                                                                                       |
| 10-15 |         | Reserved, must be zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

Comments: If multiple embedding bits are set, the least restrictive
license granted takes precedence. For example, if bits 1 and 3 are set,
bit 3 takes precedence over bit 1 and the font may be embedded with
Editable rights. For compatibility purposes, most vendors granting
Editable embedding rights are also setting the Preview & Print bit
(0x000C). This will permit an application that only supports Preview &
Print embedding to detect that font embedding is allowed.

**ySubscriptXSize**

Format: 2-byte signed short

Units: Font design units

Title: Subscript horizontal font size.

Description: The recommended horizontal size in font design units for
subscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the em square size of the font being used for a subscript.
The horizontal font size specifies a font designer's recommended
horizontal font size for subscript characters associated with this font.
If a font does not include all of the required subscript characters for
an application, and the application can substitute characters by scaling
the character of a font or by substituting characters from another font,
this parameter specifies the recommended em square for those subscript
characters.

For example, if the em square for a font is 2048 and ySubScriptXSize is
set to 205, then the horizontal size for a simulated subscript character
would be 1/10th the size of the normal character.

**ySubscriptYSize**

Format: 2-byte signed short

Units: Font design units

Title: Subscript vertical font size.

Description: The recommended vertical size in font design units for
subscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.
numerics and other, the numeric sizes should be stressed. This size
field maps to the emHeight of the font being used for a subscript. The
horizontal font size specifies a font designer's recommendation for
horizontal font size of subscript characters associated with this font.
If a font does not include all of the required subscript characters for
an application, and the application can substitute characters by scaling
the characters in a font or by substituting characters from another
font, this parameter specifies the recommended horizontal EmInc for
those subscript characters.

For example, if the em square for a font is 2048 and ySubScriptYSize is
set to 205, then the vertical size for a simulated subscript character
would be 1/10th the size of the normal character.

**ySubscriptXOffset**

Format: 2-byte signed short

Units: Font design units

Title: Subscript x offset.

Description: The recommended horizontal offset in font design untis for
subscripts for this font.

Comments: The Subscript X Offset parameter specifies a font designer's
recommended horizontal offset -- from the character origin of the font
to the character origin of the subscript's character -- for subscript
characters associated with this font. If a font does not include all of
the required subscript characters for an application, and the
application can substitute characters, this parameter specifies the
recommended horizontal position from the character escapement point of
the last character before the first subscript character. For upright
characters, this value is usually zero; however, if the characters of a
font have an incline (italic characters) the reference point for
subscript characters is usually adjusted to compensate for the angle of
incline.

**ySubscriptYOffset**

Format: 2-byte signed short

Units: Font design units

Title: Subscript y offset.

Description: The recommended vertical offset in font design units from
the baseline for subscripts for this font.

Comments: The Subscript Y Offset parameter specifies a font designer's
recommended vertical offset from the character baseline to the character
baseline for subscript characters associated with this font. Values are
expressed as a positive offset below the character baseline. If a font
does not include all of the required subscript for an application, this
parameter specifies the recommended vertical distance below the
character baseline for those subscript characters.

**ySuperscriptXSize**

Format: 2-byte signed short

Units: Font design units

Title: Superscript horizontal font size.

Description: The recommended horizontal size in font design units for
superscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the em square size of the font being used for a subscript.
The horizontal font size specifies a font designer's recommended
horizontal font size for superscript characters associated with this
font. If a font does not include all of the required superscript
characters for an application, and the application can substitute
characters by scaling the character of a font or by substituting
characters from another font, this parameter specifies the recommended
em square for those superscript characters.

For example, if the em square for a font is 2048 and ySuperScriptXSize
is set to 205, then the horizontal size for a simulated superscript
character would be 1/10th the size of the normal character.

**ySuperscriptYSize**

Format: 2-byte signed short

Units: Font design units

Title: Superscript vertical font size.

Description: The recommended vertical size in font design units for
superscripts for this font.

Comments: If a font has two recommended sizes for subscripts, e.g.,
numerics and other, the numeric sizes should be stressed. This size
field maps to the emHeight of the font being used for a subscript. The
vertical font size specifies a font designer's recommended vertical font
size for superscript characters associated with this font. If a font
does not include all of the required superscript characters for an
application, and the application can substitute characters by scaling
the character of a font or by substituting characters from another font,
this parameter specifies the recommended EmHeight for those superscript
characters.

For example, if the em square for a font is 2048 and ySuperScriptYSize
is set to 205, then the vertical size for a simulated superscript
character would be 1/10th the size of the normal character.

**ySuperscriptXOffset**

Format: 2-byte signed short

Units: Font design units

Title: Superscript x offset.

Description: The recommended horizontal offset in font design units for
superscripts for this font.

Comments: The Superscript X Offset parameter specifies a font designer's
recommended horizontal offset -- from the character origin to the
superscript character's origin for the superscript characters associated
with this font. If a font does not include all of the required
superscript characters for an application, this parameter specifies the
recommended horizontal position from the escapement point of the
character before the first superscript character. For upright
characters, this value is usually zero; however, if the characters of a
font have an incline (italic characters) the reference point for
superscript characters is usually adjusted to compensate for the angle
of incline.

**ySuperscriptYOffset**

Format: 2-byte signed short

Units: Font design units

Title: Superscript y offset.

Description: The recommended vertical offset in font design units from
the baseline for superscripts for this font.

Comments: The Superscript Y Offset parameter specifies a font designer's
recommended vertical offset -- from the character baseline to the
superscript character's baseline associated with this font. Values for
this parameter are expressed as a positive offset above the character
baseline. If a font does not include all of the required superscript
characters for an application, this parameter specifies the recommended
vertical distance above the character baseline for those superscript
characters.

**yStrikeoutSize**

Format: 2-byte signed short

Units: Font design units

Title: Strikeout size.

Description: Width of the strikeout stroke in font design units.

Comments: This field should normally be the width of the em dash for the
current font. If the size is one, the strikeout line will be the line
represented by the strikeout position field. If the value is two, the
strikeout line will be the line represented by the strikeout position
and the line immediately above the strikeout position. For a Roman font
with a 2048 em square, 102 is suggested.

**yStrikeoutPosition**

Format: 2-byte signed short

Units: Font design units

Title: Strikeout position.

Description: The position of the top of the strikeout stroke relative to
the baseline in font design units.

Comments: Positive values represent distances above the baseline, while
negative values represent distances below the baseline. A value of zero
falls directly on the baseline, while a value of one falls one pel above
the baseline. The value of strikeout position should not interfere with
the recognition of standard characters, and therefore should not line up
with crossbars in the font. For a Roman font with a 2048 em square, 460
is suggested.

**sFamilyClass**

Format: 2-byte signed short

Title: Font-family class and subclass.

Description: This parameter is a classification of font-family design.

Comments: The font class and font subclass are registered values
assigned by IBM to each font family. This parameter is intended for use
in selecting an alternate font when the requested font is not available.
The font class is the most general and the font subclass is the most
specific. The high byte of this field contains the family class, while
the low byte contains the family subclass. More information about this
field.

**Panose**

Format: 10 byte array

Title: PANOSE classification number

International: Additional specifications are required for PANOSE to
classify non-Latin character sets.

Description: This 10 byte series of numbers is used to describe the
visual characteristics of a given typeface. These characteristics are
then used to associate the font with other fonts of similar appearance
having different names. The variables for each digit are listed below.
The Panose values are fully described in the Panose "greybook"
reference, currently owned by Agfa-Monotype.

Comments: The PANOSE definition contains ten digits each of which
currently describes up to sixteen variations. Windows uses bFamilyType,
bSerifStyle and bProportion in the font mapper to determine family type.
It also uses bProportion to determine if the font is monospaced. If the
font is a symbol font, the first byte of the PANOSE number (bFamilyType)
must be set to "pictorial." Good PANOSE values in fonts are very
valuable to users of the Windows fonts folder. The specification for
assigning PANOSE values is located at
http://www.fonts.com/hp/panose/greybook/

| Type | Name             |
| ---- | ---------------- |
| BYTE | bFamilyType      |
| BYTE | bSerifStyle      |
| BYTE | bWeight          |
| BYTE | bProportion      |
| BYTE | bContrast        |
| BYTE | bStrokeVariation |
| BYTE | bArmStyle        |
| BYTE | bLetterform      |
| BYTE | bMidline         |
| BYTE | bXHeight         |

**ulUnicodeRange1 (Bits 0-31)**

**ulUnicodeRange2 (Bits 32-63)**

**ulUnicodeRange3 (Bits 64-95)**

**ulUnicodeRange4 (Bits 96-127)**

Format: 32-bit unsigned long(4 copies) totaling 128 bits.

Title: Unicode Character Range

Description: This field is used to specify the Unicode blocks or ranges
encompassed by the font file in the [cmap](#chapter.cmap) subtable for
platform 3, encoding ID 1 (Microsoft platform). If the bit is set (1)
then the Unicode range is considered functional. If the bit is clear (0)
then the range is not considered functional. Each of the bits is treated
as an independent flag and the bits can be set in any combination. The
determination of "functional" is left up to the font designer, although
character set selection should attempt to be functional by ranges if at
all possible.

All reserved fields must be zero. Each long is in Big-Endian form. See
the Basic Multilingual Plane of ISO/IEC 10646-1 or the Unicode Standard
v.3.0 for the list of Unicode ranges and characters.

| Bit    | Description                             |
| ------ | --------------------------------------- |
| 0      | Basic Latin                             |
| 1      | Latin-1 Supplement                      |
| 2      | Latin Extended-A                        |
| 3      | Latin Extended-B                        |
| 4      | IPA Extensions                          |
| 5      | Spacing Modifier Letters                |
| 6      | Combining Diacritical Marks             |
| 7      | Greek                                   |
| 8      | Reserved for Unicode SubRanges          |
| 9      | Cyrillic                                |
| 10     | Armenian                                |
| 11     | Hebrew                                  |
| 12     | Reserved for Unicode SubRanges          |
| 13     | Arabic                                  |
| 14     | Reserved for Unicode SubRanges          |
| 15     | Devanagari                              |
| 16     | Bengali                                 |
| 17     | Gurmukhi                                |
| 18     | Gujarati                                |
| 19     | Oriya                                   |
| 20     | Tamil                                   |
| 21     | Telugu                                  |
| 22     | Kannada                                 |
| 23     | Malayalam                               |
| 24     | Thai                                    |
| 25     | Lao                                     |
| 26     | Georgian                                |
| 27     | Reserved for Unicode SubRanges          |
| 28     | Hangul Jamo                             |
| 29     | Latin Extended Additional               |
| 30     | Greek Extended                          |
| 31     | General Punctuation                     |
| 32     | Superscripts And Subscripts             |
| 33     | Currency Symbols                        |
| 34     | Combining Diacritical Marks For Symbols |
| 35     | Letterlike Symbols                      |
| 36     | Number Forms                            |
| 37     | Arrows                                  |
| 38     | Mathematical Operators                  |
| 39     | Miscellaneous Technical                 |
| 40     | Control Pictures                        |
| 41     | Optical Character Recognition           |
| 42     | Enclosed Alphanumerics                  |
| 43     | Box Drawing                             |
| 44     | Block Elements                          |
| 45     | Geometric Shapes                        |
| 46     | Miscellaneous Symbols                   |
| 47     | Dingbats                                |
| 48     | CJK Symbols And Punctuation             |
| 49     | Hiragana                                |
| 50     | Katakana                                |
| 51     | Bopomofo                                |
|        | Extended Bopomofo                       |
| 52     | Hangul Compatibility Jamo               |
| 53     | CJK Miscellaneous                       |
| 54     | Enclosed CJK Letters And Months         |
| 55     | CJK Compatibility                       |
| 56     | Hangul                                  |
| 57     | Surrogates\[5\]                         |
| 58     | Reserved for Unicode SubRanges          |
| 59     | CJK Unified Ideographs                  |
|        | CJK Radicals Supplement                 |
|        | Kangxi Radicals                         |
|        | Ideographic Description                 |
|        | CJK Unified Ideograph Extension A       |
| 60     | Private Use Area                        |
| 61     | CJK Compatibility Ideographs            |
| 62     | Alphabetic Presentation Forms           |
| 63     | Arabic Presentation Forms-A             |
| 64     | Combining Half Marks                    |
| 65     | CJK Compatibility Forms                 |
| 66     | Small Form Variants                     |
| 67     | Arabic Presentation Forms-B             |
| 68     | Halfwidth And Fullwidth Forms           |
| 69     | Specials                                |
| 70     | Tibetan                                 |
| 71     | Syriac                                  |
| 72     | Thaana                                  |
| 73     | Sinhala                                 |
| 74     | Myanmar                                 |
| 75     | Ethiopic                                |
| 76     | Cherokee                                |
| 77     | Unified Canadian Syllabics              |
| 78     | Ogham                                   |
| 79     | Runic                                   |
| 80     | Khmer                                   |
| 81     | Mongolian                               |
| 82     | Braille                                 |
| 83     | Yi                                      |
|        | Yi Radicals                             |
| 84-127 | Reserved for Unicode SubRanges          |

**achVendID**

Format: 4-byte character array

Title: Font Vendor Identification

Description: The four character identifier for the vendor of the given
type face.

Comments: This is not the royalty owner of the original artwork. This is
the company responsible for the marketing and distribution of the
typeface that is being classified. It is reasonable to assume that there
will be 6 vendors of ITC Zapf Dingbats for use on desktop platforms in
the near future (if not already). It is also likely that the vendors
will have other inherent benefits in their fonts (more kern pairs,
unregularized data, hand hinted, etc.). This identifier will allow for
the correct vendor's type to be used over another, possibly inferior,
font file. The Vendor ID value is not required.

Microsoft has assigned values for some font suppliers as listed below.
Uppercase vendor ID's are reserved by Microsoft. Other suppliers can
choose their own mixed case or lowercase ID's, or leave the field blank.

For a list of registered Vendor id's see our [Registered
'vendors'](http://www.microsoft.com/typography/links/vendorlist.asp)
links page.

**fsSelection**

Format: 2-byte bit field.

Title: Font selection flags.

Description: Contains information concerning the nature of the font
patterns, as follows:

| Bit \# | macStyle bit | C Definition | Description                                                  |
| ------ | ------------ | ------------ | ------------------------------------------------------------ |
| 0      | bit 1        | ITALIC       | Font contains Italic characters, otherwise they are upright. |
| 1      |              | UNDERSCORE   | Characters are underscored.                                  |
| 2      |              | NEGATIVE     | Characters have their foreground and background reversed.    |
| 3      |              | OUTLINED     | Outline (hollow) characters, otherwise they are solid.       |
| 4      |              | STRIKEOUT    | Characters are overstruck                                    |
| 5      | bit 0        | BOLD         | Characters are emboldened.                                   |
| 6      |              | REGULAR      | Characters are in the standard weight/style for the font.    |

Comments: All undefined bits must be zero.

This field contains information on the original design of the font. Bits
0 & 5 can be used to determine if the font was designed with these
features or whether some type of machine simulation was performed on the
font to achieve this appearance. Bits 1-4 are rarely used bits that
indicate the font is primarily a decorative or special purpose font.

If bit 6 is set, then bits 0 and 5 must be clear, else the behavior is
undefined. As noted above, the settings of bits 0 and 1 must be
reflected in the macStyle bits in the [head](#chapter.head) table. While
bit 6 on implies that bits 0 and 1 of macStyle are clear (along with
bits 0 and 5 of fsSelection), the reverse is not true. Bits 0 and 1 of
macStyle (and 0 and 5 of fsSelection) may be clear and that does not
give any indication of whether or not bit 6 of fsSelection is clear
(e.g., Arial Light would have all bits cleared; it is not the regular
version of Arial).

**usFirstCharIndex**

Format: 2-byte USHORT

Description: The minimum Unicode index (character code) in this font,
according to the cmap subtable for platform ID 3 and platform- specific
encoding ID 0 or 1. For most fonts supporting Win-ANSI or other
character sets, this value would be 0x0020.

**usLastCharIndex**

Format: 2-byte USHORT

Description: The maximum Unicode index (character code) in this font,
according to the cmap subtable for platform ID 3 and encoding ID 0 or 1.
This value depends on which character sets the font supports.

**sTypoAscender**

Format: SHORT

Description: The typographic ascender for this font. Remember that this
is not the same as the Ascender value in the [hhea](#chapter.hhea)
table, which Apple defines in a far different manner. One good source
for sTypoAscender in Latin based fonts is the Ascender value from an AFM
file. For CJK fonts see below.

The suggested usage for sTypoAscender is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. The goal is to free applications from Macintosh or
Windows-specific metrics which are constrained by backward compatibility
requirements. These new metrics, when combined with the character design
widths, will allow applications to lay out documents in a
typographically correct and portable fashion. These metrics will be
exposed through Windows APIs. Macintosh applications will need to access
the 'sfnt' resource and parse it to extract this data from the
[OS/2](#chapter.OS2) table.

For CJK (Chinese, Japanese, and Korean) fonts that are intended to be
used for vertical writing (in addition to horizontal writing), the
required value for sTypoAscender is that which describes the top of the
of the ideographic em-box. For example, if the ideographic em-box of the
font extends from coordinates 0,-120 to 1000,880 (that is, a 1000x1000
box set 120 design units below the Latin baseline), then the value of
sTypoAscender must be set to 880. Failing to adhere to these
requirements will result in incorrect vertical layout.

Also see the Recommendations Section for more on this field.

**sTypoDescender**

Format: SHORT

Description: The typographic descender for this font. Remember that this
is not the same as the Descender value in the [hhea](#chapter.hhea)
table, which Apple defines in a far different manner. One good source
for sTypoDescender in Latin based fonts is the Descender value from an
AFM file. For CJK fonts see below.

The suggested usage for sTypoDescender is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. The goal is to free applications from Macintosh or
Windows-specific metrics which are constrained by backward compatability
requirements. These new metrics, when combined with the character design
widths, will allow applications to lay out documents in a
typographically correct and portable fashion. These metrics will be
exposed through Windows APIs. Macintosh applications will need to access
the 'sfnt' resource and parse it to extract this data from the
[OS/2](#chapter.OS2) table (unless Apple exposes the
[OS/2](#chapter.OS2) table through a new API).

For CJK (Chinese, Japanese, and Korean) fonts that are intended to be
used for vertical writing (in addition to horizontal writing), the
required value for sTypoDescender is that which describes the bottom of
the of the ideographic em-box. For example, if the ideographic em-box of
the font extends from coordinates 0,-120 to 1000,880 (that is, a
1000x1000 box set 120 design units below the Latin baseline), then the
value of sTypoDescender must be set to -120. Failing to adhere to these
requirements will result in incorrect vertical layout.

Also see the Recommendations Section for more on this field.

**sTypoLineGap**

Format: 2-byte SHORT

Description: The typographic line gap for this font. Remember that this
is not the same as the LineGap value in the [hhea](#chapter.hhea) table,
which Apple defines in a far different manner.

The suggested usage for usTypoLineGap is that it be used in conjunction
with unitsPerEm to compute a typographically correct default line
spacing. Typical values average 7-10% of units per em. The goal is to
free applications from Macintosh or Windows-specific metrics which are
constrained by backward compatability requirements (see chapter,
"Recommendations for Windows Fonts). These new metrics, when combined
with the character design widths, will allow applications to lay out
documents in a typographically correct and portable fashion. These
metrics will be exposed through Windows APIs. Macintosh applications
will need to access the 'sfnt' resource and parse it to extract this
data from the [OS/2](#chapter.OS2) table (unless Apple exposes the
[OS/2](#chapter.OS2) table through a new API)

**usWinAscent**

Format: 2-byte USHORT

Description: The ascender metric for Windows. This, too, is distinct
from Apple's Ascender value and from the usTypoAscender values.
usWinAscent is computed as the yMax for all characters in the Windows
ANSI character set. usWinAscent is used to compute the Windows font
height and default line spacing. For platform 3 encoding 0 fonts, it is
the same as yMax. Windows will clip the bitmap of any portion of a glyph
that appears above this value. Some applications use this value to
determine default line spacing. This is strongly discouraged. The
typographic ascender, descender and line gap fields in conjunction with
unitsPerEm should be used for this purpose. Developers should set this
field keeping the above factors in mind.

If any clipping is unacceptable, then the value should be set to yMax.

However, if a developer desires to provide appropriate default line
spacing using this field, for those applications that continue to use
this field for doing so (against OpenType recommendations), then the
value should be set appropriately. In such a case, it may result in some
glyph bitmaps being clipped.

**usWinDescent**

Format: 2-byte USHORT

Description: The descender metric for Windows. This, too, is distinct
from Apple's Descender value and from the usTypoDescender values.
usWinDescent is computed as the -yMin for all characters in the Windows
ANSI character set. usWinDescent is used to compute the Windows font
height and default line spacing. For platform 3 encoding 0 fonts, it is
the same as -yMin. Windows will clip the bitmap of any portion of a
glyph that appears below this value. Some applications use this value to
determine default line spacing. This is strongly discouraged. The
typographic ascender, descender and line gap fields in conjunction with
unitsPerEm should be used for this purpose. Developers should set this
field keeping the above factors in mind.

If any clipping is unacceptable, then the value should be set to yMin.

However, if a developer desires to provide appropriate default line
spacing using this field, for those applications that continue to use
this field for doing so (against OpenType recommendations), then the
value should be set appropriately. In such a case, it may result in some
glyph bitmaps being clipped.

**ulCodePageRange1 Bits 0-31**

**ulCodePageRange2 Bits 32-63**

Format: 32-bit unsigned long(2 copies) totaling 64 bits.

Title: Code Page Character Range

Description: This field is used to specify the code pages encompassed by
the font file in the [cmap](#chapter.cmap) subtable for platform 3,
encoding ID 1 (Microsoft platform). If the font file is encoding ID 0,
then the Symbol Character Set bit should be set. If the bit is set (1)
then the code page is considered functional. If the bit is clear (0)
then the code page is not considered functional. Each of the bits is
treated as an independent flag and the bits can be set in any
combination. The determination of "functional" is left up to the font
designer, although character set selection should attempt to be
functional by code pages if at all possible.

Symbol character sets have a special meaning. If the symbol bit (31) is
set, and the font file contains a [cmap](#chapter.cmap) subtable for
platform of 3 and encoding ID of 1, then all of the characters in the
Unicode range 0xF000 - 0xF0FF (inclusive) will be used to enumerate the
symbol character set. If the bit is not set, any characters present in
that range will not be enumerated as a symbol character set.

All reserved fields must be zero. Each long is in Big-Endian form.

| Bit   | Code | Page Description                                 |
| ----- | ---- | ------------------------------------------------ |
| 0     | 1252 | Latin 1                                          |
| 1     | 1250 | Latin 2: Eastern Europe                          |
| 2     | 1251 | Cyrillic                                         |
| 3     | 1253 | Greek                                            |
| 4     | 1254 | Turkish                                          |
| 5     | 1255 | Hebrew                                           |
| 6     | 1256 | Arabic                                           |
| 7     | 1257 | Windows Baltic                                   |
| 8     | 1258 | Vietnamese                                       |
| 9-15  |      | Reserved for Alternate ANSI                      |
| 16    | 874  | Thai                                             |
| 17    | 932  | JIS/Japan                                        |
| 18    | 936  | Chinese: Simplified chars--PRC and Singapore     |
| 19    | 949  | Korean Wansung                                   |
| 20    | 950  | Chinese: Traditional chars--Taiwan and Hong Kong |
| 21    | 1361 | Korean Johab                                     |
| 22-28 |      | Reserved for Alternate ANSI & OEM                |
| 29    |      | Macintosh Character Set (US Roman)               |
| 30    |      | OEM Character Set                                |
| 31    |      | Symbol Character Set                             |
| 32-47 |      | Reserved for OEM                                 |
| 48    | 869  | IBM Greek                                        |
| 49    | 866  | MS-DOS Russian                                   |
| 50    | 865  | MS-DOS Nordic                                    |
| 51    | 864  | Arabic                                           |
| 52    | 863  | MS-DOS Canadian French                           |
| 53    | 862  | Hebrew                                           |
| 54    | 861  | MS-DOS Icelandic                                 |
| 55    | 860  | MS-DOS Portuguese                                |
| 56    | 857  | IBM Turkish                                      |
| 57    | 855  | IBM Cyrillic; primarily Russian                  |
| 58    | 852  | Latin 2                                          |
| 59    | 775  | MS-DOS Baltic                                    |
| 60    | 737  | Greek; former 437 G                              |
| 61    | 708  | Arabic; ASMO 708                                 |
| 62    | 850  | WE/Latin 1                                       |
| 63    | 437  | US                                               |

**sxHeight**

Format: SHORT

Description: This metric specifies the distance between the baseline and
the approximate height of non-ascending lowercase letters measured in
FUnits. This value would normally be specified by a type designer but in
situations where that is not possible, for example when a legacy font is
being converted, the value may be set equal to the top of the unscaled
and unhinted glyph bounding box of the glyph encoded at U+0078 (LATIN
SMALL LETTER X). If no glyph is encoded in this position the field
should be set to 0.

This metric, if specified, can be used in font substitution: the xHeight
value of one font can be scaled to approximate the apparent size of
another.

**sCapHeight**

Format: SHORT

Description: This metric specifies the distance between the baseline and
the approximate height of uppercase letters measured in FUnits. This
value would normally be specified by a type designer but in situations
where that is not possible, for example when a legacy font is being
converted, the value may be set equal to the top of the unscaled and
unhinted glyph bounding box of the glyph encoded at U+0048 (LATIN
CAPITAL LETTER H). If no glyph is encoded in this position the field
should be set to 0.

This metric, if specified, can be used in systems that specify type size
by capital height measured in millimeters. It can also be used as an
alignment metric; the top of a drop capital, for instance, can be
aligned to the sCapHeight metric of the first line of text.

**usDefaultChar**

Format: USHORT

Description: Whenever a request is made for a character that is not in
the font, Windows provides this default character. If the value of this
field is zero, glyph ID 0 is to be used for the default character
otherwise this is the Unicode encoding of the glyph that Windows uses as
the default character.

**usBreakChar**

Format: USHORT

Description: This is the Unicode encoding of the glyph that Windows uses
as the break character. The break character is used to separate words
and justify text. Most fonts specify 'space' as the break character.

**usMaxContext**

Format: USHORT

Description: The maximum length of a target glyph context for any
feature in this font. For example, a font which has only a pair kerning
feature should set this field to 2. If the font also has a ligature
feature in which the glyph sequence 'f f i' is substituted by the
ligature 'ffi', then this field should be set to 3. This field could be
useful to sophisticated line-breaking engines in determining how far
they should look ahead to test whether something could change that
effects the line breaking. For chaining contextual lookups, the length
of the string (covered glyph) + (input sequence) + (lookahead sequence)
should be considered.

### Annotation

Note that the usFirstCharIndex and usLastCharIndex are no longer very
useful, since these fields are not big enough to represent Unicode
supplemental characters.

### XML Representation

    Relax Schema for OS/2 table ==
          
    OS2 |=
      element OS2 {
        attribute version { "0" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v0,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_vendID,
        os2_fsSelection,
        os2_charIndex,
        os2_typo,
        os2_win
      }
    OS2 |=
      element OS2 {
        attribute version { "1" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v0,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_unicodeRange_v1,
        os2_vendID,
        os2_fsSelection,
        os2_charIndex,
        os2_typo,
        os2_win,
        os2_codePageRange_v1
      }
    OS2 |=
      element OS2 {
        attribute version { "2" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v2,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_unicodeRange_v2,
        os2_vendID,
        os2_fsSelection,
        os2_charIndex,
        os2_typo,
        os2_win,
        os2_codePageRange_v2,
        os2_height,
        os2_capHeight,
        os2_defaultChar,
        os2_breakChar,
        os2_maxContext
      }
    OS2 |=
      element OS2 {
        attribute version { "3" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v2,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_unicodeRange_v3,
        os2_vendID,
        os2_fsSelection,
        os2_charIndex,
        os2_typo,
        os2_win,
        os2_codePageRange_v2,
        os2_height,
        os2_capHeight,
        os2_defaultChar,
        os2_breakChar,
        os2_maxContext
      }
    OS2 |=
      element OS2 {
        attribute version { "4" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v2,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_unicodeRange_v4,
        os2_vendID,
        os2_fsSelection_v4,
        os2_charIndex,
        os2_typo,
        os2_win,
        os2_codePageRange_v2,
        os2_height,
        os2_capHeight,
        os2_defaultChar,
        os2_breakChar,
        os2_maxContext
      }
    OS2 |=
      element OS2 {
        attribute version { "5" },
        os2_avgCharWidth,
        os2_weightClass,
        os2_widthClass,
        os2_fsType_v2,
        os2_subscript,
        os2_superscript,
        os2_strikeout,
        os2_familyClass,
        os2_panose,
        os2_unicodeRange_v5,
        os2_vendID,
        os2_fsSelection_v4,
        os2_charIndex,
        os2_typo,
        os2_win,
        os2_codePageRange_v2,
        os2_height,
        os2_capHeight,
        os2_defaultChar,
        os2_breakChar,
        os2_maxContext,
        os2_lowerOpticalPointSize,
        os2_upperOpticalPointSize
      }
    os2_avgCharWidth =
      element avgCharWidth {
        attribute v { text }
      }
    os2_weightClass =
      element weightClass {
        attribute v { text }
      }
    os2_widthClass =
      element widthClass {
        attribute v { text }
      }
    os2_fsType_v0 =
      element fsType {
        attribute Restricted { yesOrNo },
        attribute Preview_and_print { yesOrNo },
        attribute Editable_embedding { yesOrNo }
      }
    os2_fsType_v2 =
      element fsType {
        attribute Restricted { yesOrNo },
        attribute Preview_and_print { yesOrNo },
        attribute Editable_embedding { yesOrNo },
        attribute No_subsetting { yesOrNo },
        attribute Bitmap_embedding_only { yesOrNo }
      }
    os2_subscript =
      element subscript {
        attribute xsize { text },
        attribute ysize { text },
        attribute xoffset { text },
        attribute yoffset { text }
      }
    os2_superscript =
      element superscript {
        attribute xsize { text },
        attribute ysize { text },
        attribute xoffset { text },
        attribute yoffset { text }
      }
    os2_strikeout =
      element strikeout {
        attribute size { text },
        attribute position { text }
      }
    os2_familyClass =
      element familyClass {
        attribute v { text }
      }
    os2_panose =
      element panose {
        attribute familyType { text },
        attribute serifStyle { text },
        attribute weight { text },
        attribute proportion { text },
        attribute contrast { text },
        attribute strokeVariation { text },
        attribute armStyle { text },
        attribute letterform { text },
        attribute midline { text },
        attribute xHeight { text }
      }
    os2_unicodeRange_v1 =
      element unicodeRange {
        attribute Basic_Latin { yesOrNo },
        attribute Latin_1_Supplement { yesOrNo },
        attribute Latin_Extended_A { yesOrNo },
        attribute Latin_Extended_B { yesOrNo },
        attribute IPA_Extensions { yesOrNo },
        attribute Spacing_Modifier_Letters { yesOrNo },
        attribute Combining_Diacritical_Marks { yesOrNo },
        attribute Greek { yesOrNo },
        attribute Greek_Symbols_And_Coptic { yesOrNo },
        attribute Cyrillic { yesOrNo },
        attribute Armenian { yesOrNo },
        attribute Hebrew { yesOrNo },
        attribute Hebrew_Extended { yesOrNo },
        attribute Arabic { yesOrNo },
        attribute Arabic_Extended { yesOrNo },
        attribute Devanagari { yesOrNo },
        attribute Bengali { yesOrNo },
        attribute Gurmukhi { yesOrNo },
        attribute Gujarati { yesOrNo },
        attribute Oriya { yesOrNo },
        attribute Tamil { yesOrNo },
        attribute Telugu { yesOrNo },
        attribute Kannada { yesOrNo },
        attribute Malayalam { yesOrNo },
        attribute Thai { yesOrNo },
        attribute Lao { yesOrNo },
        attribute Georgian { yesOrNo },
        attribute Georgian_Extended { yesOrNo },
        attribute Hangul_Jamo { yesOrNo },
        attribute Latin_Extended_Additional { yesOrNo },
        attribute Greek_Extended { yesOrNo },
        attribute General_Punctuation { yesOrNo },
        attribute Superscripts_And_Subscripts { yesOrNo },
        attribute Currency_Symbols { yesOrNo },
        attribute Combining_Diacritical_Marks_For_Symbols { yesOrNo },
        attribute Letterlike_Symbols { yesOrNo },
        attribute Number_Forms { yesOrNo },
        attribute Arrows { yesOrNo },
        attribute Mathematical_Operators { yesOrNo },
        attribute Miscellaneous_Technical { yesOrNo },
        attribute Control_Pictures { yesOrNo },
        attribute Optical_Character_Recognition { yesOrNo },
        attribute Enclosed_Alphanumerics { yesOrNo },
        attribute Box_Drawing { yesOrNo },
        attribute Block_Elements { yesOrNo },
        attribute Geometric_Shapes { yesOrNo },
        attribute Miscellaneous_Symbols { yesOrNo },
        attribute Dingbats { yesOrNo },
        attribute CJK_Symbols_And_Punctuation { yesOrNo },
        attribute Hiragana { yesOrNo },
        attribute Katakana { yesOrNo },
        attribute Bopomofo { yesOrNo },
        attribute Hangul_Compatibility_Jamo { yesOrNo },
        attribute CJK_Miscellaneous { yesOrNo },
        attribute Enclosed_CJK_Letters_And_Months { yesOrNo },
        attribute CJK_Compatibility { yesOrNo },
        attribute Hangul { yesOrNo },
        attribute CJK_Unified_Ideographs { yesOrNo },
        attribute Private_Use_Area { yesOrNo },
        attribute CJK_Compatibility_Ideographs { yesOrNo },
        attribute Alphabetic_Presentation_Forms { yesOrNo },
        attribute Arabic_Presentation_Forms_A { yesOrNo },
        attribute Combining_Half_Marks { yesOrNo },
        attribute CJK_Compatibility_Forms { yesOrNo },
        attribute Small_Form_Variants { yesOrNo },
        attribute Arabic_Presentation_Forms_B { yesOrNo },
        attribute Halfwidth_And_Fullwidth_Forms { yesOrNo },
        attribute Specials { yesOrNo }
      }
    os2_unicodeRange_v2 =
      element unicodeRange {
        attribute Basic_Latin { yesOrNo },
        attribute Latin_1_Supplement { yesOrNo },
        attribute Latin_Extended_A { yesOrNo },
        attribute Latin_Extended_B { yesOrNo },
        attribute IPA_Extensions { yesOrNo },
        attribute Spacing_Modifier_Letters { yesOrNo },
        attribute Combining_Diacritical_Marks { yesOrNo },
        attribute Greek { yesOrNo },
        attribute Cyrillic { yesOrNo },
        attribute Armenian { yesOrNo },
        attribute Hebrew { yesOrNo },
        attribute Arabic { yesOrNo },
        attribute Devanagari { yesOrNo },
        attribute Bengali { yesOrNo },
        attribute Gurmukhi { yesOrNo },
        attribute Gujarati { yesOrNo },
        attribute Oriya { yesOrNo },
        attribute Tamil { yesOrNo },
        attribute Telugu { yesOrNo },
        attribute Kannada { yesOrNo },
        attribute Malayalam { yesOrNo },
        attribute Thai { yesOrNo },
        attribute Lao { yesOrNo },
        attribute Georgian { yesOrNo },
        attribute Hangul_Jamo { yesOrNo },
        attribute Latin_Extended_Additional { yesOrNo },
        attribute Greek_Extended { yesOrNo },
        attribute General_Punctuation { yesOrNo },
        attribute Superscripts_And_Subscripts { yesOrNo },
        attribute Currency_Symbols { yesOrNo },
        attribute Combining_Diacritical_Marks_For_Symbols { yesOrNo },
        attribute Letterlike_Symbols { yesOrNo },
        attribute Number_Forms { yesOrNo },
        attribute Arrows { yesOrNo },
        attribute Mathematical_Operators { yesOrNo },
        attribute Miscellaneous_Technical { yesOrNo },
        attribute Control_Pictures { yesOrNo },
        attribute Optical_Character_Recognition { yesOrNo },
        attribute Enclosed_Alphanumerics { yesOrNo },
        attribute Box_Drawing { yesOrNo },
        attribute Block_Elements { yesOrNo },
        attribute Geometric_Shapes { yesOrNo },
        attribute Miscellaneous_Symbols { yesOrNo },
        attribute Dingbats { yesOrNo },
        attribute CJK_Symbols_And_Punctuation { yesOrNo },
        attribute Hiragana { yesOrNo },
        attribute Katakana { yesOrNo },
        attribute Bopomofo { yesOrNo },
        attribute Hangul_Compatibility_Jamo { yesOrNo },
        attribute CJK_Miscellaneous { yesOrNo },
        attribute Enclosed_CJK_Letters_And_Months { yesOrNo },
        attribute CJK_Compatibility { yesOrNo },
        attribute Hangul { yesOrNo },
        attribute Surrogates { yesOrNo },
        attribute CJK_Unified_Ideographs { yesOrNo },
        attribute Private_Use_Area { yesOrNo },
        attribute CJK_Compatibility_Ideographs { yesOrNo },
        attribute Alphabetic_Presentation_Forms { yesOrNo },
        attribute Arabic_Presentation_Forms_A { yesOrNo },
        attribute Combining_Half_Marks { yesOrNo },
        attribute CJK_Compatibility_Forms { yesOrNo },
        attribute Small_Form_Variants { yesOrNo },
        attribute Arabic_Presentation_Forms_B { yesOrNo },
        attribute Halfwidth_And_Fullwidth_Forms { yesOrNo },
        attribute Specials { yesOrNo },
        attribute Tibetan { yesOrNo },
        attribute Syriac { yesOrNo },
        attribute Thaana { yesOrNo },
        attribute Sinhala { yesOrNo },
        attribute Myanmar { yesOrNo },
        attribute Ethiopic { yesOrNo },
        attribute Cherokee { yesOrNo },
        attribute Unified_Canadian_Syllabics { yesOrNo },
        attribute Ogham { yesOrNo },
        attribute Runic { yesOrNo },
        attribute Khmer { yesOrNo },
        attribute Mongolian { yesOrNo },
        attribute Braille { yesOrNo },
        attribute Yi { yesOrNo }
      }
    os2_unicodeRange_v3 =
      element unicodeRange {
        attribute Basic_Latin { yesOrNo },
        attribute Latin_1_Supplement { yesOrNo },
        attribute Latin_Extended_A { yesOrNo },
        attribute Latin_Extended_B { yesOrNo },
        attribute IPA_Extensions { yesOrNo },
        attribute Spacing_Modifier_Letters { yesOrNo },
        attribute Combining_Diacritical_Marks { yesOrNo },
        attribute Greek { yesOrNo },
        attribute Cyrillic { yesOrNo },
        attribute Armenian { yesOrNo },
        attribute Hebrew { yesOrNo },
        attribute Arabic { yesOrNo },
        attribute Devanagari { yesOrNo },
        attribute Bengali { yesOrNo },
        attribute Gurmukhi { yesOrNo },
        attribute Gujarati { yesOrNo },
        attribute Oriya { yesOrNo },
        attribute Tamil { yesOrNo },
        attribute Telugu { yesOrNo },
        attribute Kannada { yesOrNo },
        attribute Malayalam { yesOrNo },
        attribute Thai { yesOrNo },
        attribute Lao { yesOrNo },
        attribute Georgian { yesOrNo },
        attribute Hangul_Jamo { yesOrNo },
        attribute Latin_Extended_Additional { yesOrNo },
        attribute Greek_Extended { yesOrNo },
        attribute General_Punctuation { yesOrNo },
        attribute Superscripts_And_Subscripts { yesOrNo },
        attribute Currency_Symbols { yesOrNo },
        attribute Combining_Diacritical_Marks_For_Symbols { yesOrNo },
        attribute Letterlike_Symbols { yesOrNo },
        attribute Number_Forms { yesOrNo },
        attribute Arrows { yesOrNo },
        attribute Mathematical_Operators { yesOrNo },
        attribute Miscellaneous_Technical { yesOrNo },
        attribute Control_Pictures { yesOrNo },
        attribute Optical_Character_Recognition { yesOrNo },
        attribute Enclosed_Alphanumerics { yesOrNo },
        attribute Box_Drawing { yesOrNo },
        attribute Block_Elements { yesOrNo },
        attribute Geometric_Shapes { yesOrNo },
        attribute Miscellaneous_Symbols { yesOrNo },
        attribute Dingbats { yesOrNo },
        attribute CJK_Symbols_And_Punctuation { yesOrNo },
        attribute Hiragana { yesOrNo },
        attribute Katakana { yesOrNo },
        attribute Bopomofo { yesOrNo },
        attribute Hangul_Compatibility_Jamo { yesOrNo },
        attribute Enclosed_CJK_Letters_And_Months { yesOrNo },
        attribute CJK_Compatibility { yesOrNo },
        attribute Hangul { yesOrNo },
        attribute Surrogates { yesOrNo },
        attribute CJK_Unified_Ideographs { yesOrNo },
        attribute Private_Use_Area { yesOrNo },
        attribute CJK_Compatibility_Ideographs { yesOrNo },
        attribute Alphabetic_Presentation_Forms { yesOrNo },
        attribute Arabic_Presentation_Forms_A { yesOrNo },
        attribute Combining_Half_Marks { yesOrNo },
        attribute CJK_Compatibility_Forms { yesOrNo },
        attribute Small_Form_Variants { yesOrNo },
        attribute Arabic_Presentation_Forms_B { yesOrNo },
        attribute Halfwidth_And_Fullwidth_Forms { yesOrNo },
        attribute Specials { yesOrNo },
        attribute Tibetan { yesOrNo },
        attribute Syriac { yesOrNo },
        attribute Thaana { yesOrNo },
        attribute Sinhala { yesOrNo },
        attribute Myanmar { yesOrNo },
        attribute Ethiopic { yesOrNo },
        attribute Cherokee { yesOrNo },
        attribute Unified_Canadian_Syllabics { yesOrNo },
        attribute Ogham { yesOrNo },
        attribute Runic { yesOrNo },
        attribute Khmer { yesOrNo },
        attribute Mongolian { yesOrNo },
        attribute Braille { yesOrNo },
        attribute Yi { yesOrNo },
        attribute Tagalog_Hanunoo_Buhid_Tagbanwa { yesOrNo },
        attribute Old_Italic { yesOrNo },
        attribute Gothic { yesOrNo },
        attribute Deseret { yesOrNo },
        attribute Musical_Symbols { yesOrNo },
        attribute Mathematical_Alphanumeric_Symbols { yesOrNo },
        attribute Private_Use_Supplementary { yesOrNo },
        attribute Variation_Selectors { yesOrNo },
        attribute Tags { yesOrNo }
      }
    os2_unicodeRange_v4 =
      element unicodeRange {
        attribute Basic_Latin { yesOrNo },
        attribute Latin_1_Supplement { yesOrNo },
        attribute Latin_Extended_A { yesOrNo },
        attribute Latin_Extended_B { yesOrNo },
        attribute IPA_Extensions { yesOrNo },
        attribute Spacing_Modifier_Letters { yesOrNo },
        attribute Combining_Diacritical_Marks { yesOrNo },
        attribute Greek { yesOrNo },
        attribute Coptic { yesOrNo },
        attribute Cyrillic { yesOrNo },
        attribute Armenian { yesOrNo },
        attribute Hebrew { yesOrNo },
        attribute Vai { yesOrNo },
        attribute Arabic { yesOrNo },
        attribute NKo { yesOrNo },
        attribute Devanagari { yesOrNo },
        attribute Bengali { yesOrNo },
        attribute Gurmukhi { yesOrNo },
        attribute Gujarati { yesOrNo },
        attribute Oriya { yesOrNo },
        attribute Tamil { yesOrNo },
        attribute Telugu { yesOrNo },
        attribute Kannada { yesOrNo },
        attribute Malayalam { yesOrNo },
        attribute Thai { yesOrNo },
        attribute Lao { yesOrNo },
        attribute Georgian { yesOrNo },
        attribute Balinese { yesOrNo },
        attribute Hangul_Jamo { yesOrNo },
        attribute Latin_Extended_Additional { yesOrNo },
        attribute Greek_Extended { yesOrNo },
        attribute General_Punctuation { yesOrNo },
        attribute Superscripts_And_Subscripts { yesOrNo },
        attribute Currency_Symbols { yesOrNo },
        attribute Combining_Diacritical_Marks_For_Symbols { yesOrNo },
        attribute Letterlike_Symbols { yesOrNo },
        attribute Number_Forms { yesOrNo },
        attribute Arrows { yesOrNo },
        attribute Mathematical_Operators { yesOrNo },
        attribute Miscellaneous_Technical { yesOrNo },
        attribute Control_Pictures { yesOrNo },
        attribute Optical_Character_Recognition { yesOrNo },
        attribute Enclosed_Alphanumerics { yesOrNo },
        attribute Box_Drawing { yesOrNo },
        attribute Block_Elements { yesOrNo },
        attribute Geometric_Shapes { yesOrNo },
        attribute Miscellaneous_Symbols { yesOrNo },
        attribute Dingbats { yesOrNo },
        attribute CJK_Symbols_And_Punctuation { yesOrNo },
        attribute Hiragana { yesOrNo },
        attribute Katakana { yesOrNo },
        attribute Bopomofo { yesOrNo },
        attribute Hangul_Compatibility_Jamo { yesOrNo },
        attribute Phags_pa { yesOrNo },
        attribute Enclosed_CJK_Letters_And_Months { yesOrNo },
        attribute CJK_Compatibility { yesOrNo },
        attribute Hangul { yesOrNo },
        attribute Surrogates { yesOrNo },
        attribute Phoenician { yesOrNo },
        attribute CJK_Unified_Ideographs { yesOrNo },
        attribute Private_Use_Area { yesOrNo },
        attribute CJK_Compatibility_Ideographs { yesOrNo },
        attribute Alphabetic_Presentation_Forms { yesOrNo },
        attribute Arabic_Presentation_Forms_A { yesOrNo },
        attribute Combining_Half_Marks { yesOrNo },
        attribute CJK_Compatibility_Forms { yesOrNo },
        attribute Small_Form_Variants { yesOrNo },
        attribute Arabic_Presentation_Forms_B { yesOrNo },
        attribute Halfwidth_And_Fullwidth_Forms { yesOrNo },
        attribute Specials { yesOrNo },
        attribute Tibetan { yesOrNo },
        attribute Syriac { yesOrNo },
        attribute Thaana { yesOrNo },
        attribute Sinhala { yesOrNo },
        attribute Myanmar { yesOrNo },
        attribute Ethiopic { yesOrNo },
        attribute Cherokee { yesOrNo },
        attribute Unified_Canadian_Syllabics { yesOrNo },
        attribute Ogham { yesOrNo },
        attribute Runic { yesOrNo },
        attribute Khmer { yesOrNo },
        attribute Mongolian { yesOrNo },
        attribute Braille { yesOrNo },
        attribute Yi { yesOrNo },
        attribute Tagalog_Hanunoo_Buhid_Tagbanwa { yesOrNo },
        attribute Old_Italic { yesOrNo },
        attribute Gothic { yesOrNo },
        attribute Deseret { yesOrNo },
        attribute Musical_Symbols { yesOrNo },
        attribute Mathematical_Alphanumeric_Symbols { yesOrNo },
        attribute Private_Use_Supplementary { yesOrNo },
        attribute Variation_Selectors { yesOrNo },
        attribute Tags { yesOrNo },
        attribute Limbu { yesOrNo },
        attribute Tai_Le { yesOrNo },
        attribute New_Tai_Lue { yesOrNo },
        attribute Buginese { yesOrNo },
        attribute Glagolitic { yesOrNo },
        attribute Tifinagh { yesOrNo },
        attribute Yijing_Hexagram_Symbols { yesOrNo },
        attribute Syloti_Nagri { yesOrNo },
        attribute Linear_B { yesOrNo },
        attribute Ancient_Greek_Numbers { yesOrNo },
        attribute Ugaritic { yesOrNo },
        attribute Old_Persian { yesOrNo },
        attribute Shavian { yesOrNo },
        attribute Osmanya { yesOrNo },
        attribute Cypriot_Syllabary { yesOrNo },
        attribute Kharoshthi { yesOrNo },
        attribute Tai_Xuan_Jing_Symbols { yesOrNo },
        attribute Cuneiform { yesOrNo },
        attribute Counting_Rod_Numerals { yesOrNo },
        attribute Sundanese { yesOrNo },
        attribute Lepcha { yesOrNo },
        attribute Ol_Chiki { yesOrNo },
        attribute Saurashtra { yesOrNo },
        attribute Kayah_Li { yesOrNo },
        attribute Rejang { yesOrNo },
        attribute Cham { yesOrNo },
        attribute Ancient_Symbols { yesOrNo },
        attribute Phaistos_Disc { yesOrNo },
        attribute Carian_Lycian_Lydian { yesOrNo },
        attribute Domino_And_Mahjong_Tiles { yesOrNo }
      }
    os2_unicodeRange_v5 =
      element unicodeRange {
        attribute Basic_Latin { yesOrNo },
        attribute Latin_1_Supplement { yesOrNo },
        attribute Latin_Extended_A { yesOrNo },
        attribute Latin_Extended_B { yesOrNo },
        attribute IPA_Extensions { yesOrNo },
        attribute Spacing_Modifier_Letters { yesOrNo },
        attribute Combining_Diacritical_Marks { yesOrNo },
        attribute Greek { yesOrNo },
        attribute Coptic { yesOrNo },
        attribute Cyrillic { yesOrNo },
        attribute Armenian { yesOrNo },
        attribute Hebrew { yesOrNo },
        attribute Vai { yesOrNo },
        attribute Arabic { yesOrNo },
        attribute NKo { yesOrNo },
        attribute Devanagari { yesOrNo },
        attribute Bengali { yesOrNo },
        attribute Gurmukhi { yesOrNo },
        attribute Gujarati { yesOrNo },
        attribute Oriya { yesOrNo },
        attribute Tamil { yesOrNo },
        attribute Telugu { yesOrNo },
        attribute Kannada { yesOrNo },
        attribute Malayalam { yesOrNo },
        attribute Thai { yesOrNo },
        attribute Lao { yesOrNo },
        attribute Georgian { yesOrNo },
        attribute Balinese { yesOrNo },
        attribute Hangul_Jamo { yesOrNo },
        attribute Latin_Extended_Additional { yesOrNo },
        attribute Greek_Extended { yesOrNo },
        attribute General_Punctuation { yesOrNo },
        attribute Superscripts_And_Subscripts { yesOrNo },
        attribute Currency_Symbols { yesOrNo },
        attribute Combining_Diacritical_Marks_For_Symbols { yesOrNo },
        attribute Letterlike_Symbols { yesOrNo },
        attribute Number_Forms { yesOrNo },
        attribute Arrows { yesOrNo },
        attribute Mathematical_Operators { yesOrNo },
        attribute Miscellaneous_Technical { yesOrNo },
        attribute Control_Pictures { yesOrNo },
        attribute Optical_Character_Recognition { yesOrNo },
        attribute Enclosed_Alphanumerics { yesOrNo },
        attribute Box_Drawing { yesOrNo },
        attribute Block_Elements { yesOrNo },
        attribute Geometric_Shapes { yesOrNo },
        attribute Miscellaneous_Symbols { yesOrNo },
        attribute Dingbats { yesOrNo },
        attribute CJK_Symbols_And_Punctuation { yesOrNo },
        attribute Hiragana { yesOrNo },
        attribute Katakana { yesOrNo },
        attribute Bopomofo { yesOrNo },
        attribute Hangul_Compatibility_Jamo { yesOrNo },
        attribute Phags_pa { yesOrNo },
        attribute Enclosed_CJK_Letters_And_Months { yesOrNo },
        attribute CJK_Compatibility { yesOrNo },
        attribute Hangul { yesOrNo },
        attribute Surrogates { yesOrNo },
        attribute Phoenician { yesOrNo },
        attribute CJK_Unified_Ideographs { yesOrNo },
        attribute Private_Use_Area { yesOrNo },
        attribute CJK_Compatibility_Ideographs { yesOrNo },
        attribute Alphabetic_Presentation_Forms { yesOrNo },
        attribute Arabic_Presentation_Forms_A { yesOrNo },
        attribute Combining_Half_Marks { yesOrNo },
        attribute CJK_Compatibility_Forms { yesOrNo },
        attribute Small_Form_Variants { yesOrNo },
        attribute Arabic_Presentation_Forms_B { yesOrNo },
        attribute Halfwidth_And_Fullwidth_Forms { yesOrNo },
        attribute Specials { yesOrNo },
        attribute Tibetan { yesOrNo },
        attribute Syriac { yesOrNo },
        attribute Thaana { yesOrNo },
        attribute Sinhala { yesOrNo },
        attribute Myanmar { yesOrNo },
        attribute Ethiopic { yesOrNo },
        attribute Cherokee { yesOrNo },
        attribute Unified_Canadian_Syllabics { yesOrNo },
        attribute Ogham { yesOrNo },
        attribute Runic { yesOrNo },
        attribute Khmer { yesOrNo },
        attribute Mongolian { yesOrNo },
        attribute Braille { yesOrNo },
        attribute Yi { yesOrNo },
        attribute Tagalog_Hanunoo_Buhid_Tagbanwa { yesOrNo },
        attribute Old_Italic { yesOrNo },
        attribute Gothic { yesOrNo },
        attribute Deseret { yesOrNo },
        attribute Musical_Symbols { yesOrNo },
        attribute Mathematical_Alphanumeric_Symbols { yesOrNo },
        attribute Private_Use_Supplementary { yesOrNo },
        attribute Variation_Selectors { yesOrNo },
        attribute Tags { yesOrNo },
        attribute Limbu { yesOrNo },
        attribute Tai_Le { yesOrNo },
        attribute New_Tai_Lue { yesOrNo },
        attribute Buginese { yesOrNo },
        attribute Glagolitic { yesOrNo },
        attribute Tifinagh { yesOrNo },
        attribute Yijing_Hexagram_Symbols { yesOrNo },
        attribute Syloti_Nagri { yesOrNo },
        attribute Linear_B { yesOrNo },
        attribute Ancient_Greek_Numbers { yesOrNo },
        attribute Ugaritic { yesOrNo },
        attribute Old_Persian { yesOrNo },
        attribute Shavian { yesOrNo },
        attribute Osmanya { yesOrNo },
        attribute Cypriot_Syllabary { yesOrNo },
        attribute Kharoshthi { yesOrNo },
        attribute Tai_Xuan_Jing_Symbols { yesOrNo },
        attribute Cuneiform { yesOrNo },
        attribute Counting_Rod_Numerals { yesOrNo },
        attribute Sundanese { yesOrNo },
        attribute Lepcha { yesOrNo },
        attribute Ol_Chiki { yesOrNo },
        attribute Saurashtra { yesOrNo },
        attribute Kayah_aLi { yesOrNo },
        attribute Rejang { yesOrNo },
        attribute Cham { yesOrNo },
        attribute Ancient_Symbols { yesOrNo },
        attribute Phaistos_Disc { yesOrNo },
        attribute Carian_Lycian_Lydian { yesOrNo },
        attribute Domino_And_Mahjong_Tiles { yesOrNo }
      }
    os2_vendID =
      element vendID {
        attribute v { text }
      }
    os2_fsSelection =
      element fsSelection {
        attribute ITALIC { text },
        attribute UNDERSCORE { text },
        attribute NEGATIVE { text },
        attribute OUTLINED { text },
        attribute STRIKEOUT { text },
        attribute BOLD { text },
        attribute REGULAR { text }
      }
    os2_fsSelection_v4 =
      element fsSelection {
        attribute ITALIC { text },
        attribute UNDERSCORE { text },
        attribute NEGATIVE { text },
        attribute OUTLINED { text },
        attribute STRIKEOUT { text },
        attribute BOLD { text },
        attribute REGULAR { text },
        attribute USE_TYPO_METRICS { text },
        attribute WWS { text },
        attribute OBLIQUE { text }
      }
    os2_charIndex =
      element charIndex {
        attribute first { text },
        attribute last { text }
      }
    os2_typo =
      element typo {
        attribute ascender { text },
        attribute descender { text },
        attribute linegap { text }
      }
    os2_win =
      element win {
        attribute ascent { text },
        attribute descent { text }
      }
    os2_codePageRange_v1 =
      element codePageRange {
        attribute CP_1252 { yesOrNo },
        attribute CP_1250 { yesOrNo },
        attribute CP_1251 { yesOrNo },
        attribute CP_1253 { yesOrNo },
        attribute CP_1254 { yesOrNo },
        attribute CP_1255 { yesOrNo },
        attribute CP_1256 { yesOrNo },
        attribute CP_1257 { yesOrNo },
        attribute CP_874 { yesOrNo },
        attribute CP_932 { yesOrNo },
        attribute CP_936 { yesOrNo },
        attribute CP_949 { yesOrNo },
        attribute CP_950 { yesOrNo },
        attribute CP_1361 { yesOrNo },
        attribute OEM { yesOrNo },
        attribute Symbol { yesOrNo },
        attribute CP_869 { yesOrNo },
        attribute CP_866 { yesOrNo },
        attribute CP_865 { yesOrNo },
        attribute CP_864 { yesOrNo },
        attribute CP_863 { yesOrNo },
        attribute CP_862 { yesOrNo },
        attribute CP_861 { yesOrNo },
        attribute CP_860 { yesOrNo },
        attribute CP_857 { yesOrNo },
        attribute CP_855 { yesOrNo },
        attribute CP_852 { yesOrNo },
        attribute CP_775 { yesOrNo },
        attribute CP_737 { yesOrNo },
        attribute CP_708 { yesOrNo },
        attribute CP_850 { yesOrNo },
        attribute CP_437 { yesOrNo }
      }
    os2_codePageRange_v2 =
      element codePageRange {
        attribute CP_1252 { yesOrNo },
        attribute CP_1250 { yesOrNo },
        attribute CP_1251 { yesOrNo },
        attribute CP_1253 { yesOrNo },
        attribute CP_1254 { yesOrNo },
        attribute CP_1255 { yesOrNo },
        attribute CP_1256 { yesOrNo },
        attribute CP_1257 { yesOrNo },
        attribute CP_1258 { yesOrNo },
        attribute CP_874 { yesOrNo },
        attribute CP_932 { yesOrNo },
        attribute CP_936 { yesOrNo },
        attribute CP_949 { yesOrNo },
        attribute CP_950 { yesOrNo },
        attribute CP_1361 { yesOrNo },
        attribute Macintosh { yesOrNo },
        attribute OEM { yesOrNo },
        attribute Symbol { yesOrNo },
        attribute CP_869 { yesOrNo },
        attribute CP_866 { yesOrNo },
        attribute CP_865 { yesOrNo },
        attribute CP_864 { yesOrNo },
        attribute CP_863 { yesOrNo },
        attribute CP_862 { yesOrNo },
        attribute CP_861 { yesOrNo },
        attribute CP_860 { yesOrNo },
        attribute CP_857 { yesOrNo },
        attribute CP_855 { yesOrNo },
        attribute CP_852 { yesOrNo },
        attribute CP_775 { yesOrNo },
        attribute CP_737 { yesOrNo },
        attribute CP_708 { yesOrNo },
        attribute CP_850 { yesOrNo },
        attribute CP_437 { yesOrNo }
      }
    os2_height =
      element height {
        attribute v { text }
      }
    os2_capHeight =
      element capHeight {
        attribute v { text }
      }
    os2_defaultChar =
      element defaultChar {
        attribute v { text }
      }
    os2_breakChar =
      element breakChar {
        attribute v { text }
      }
    os2_maxContext =
      element maxContext {
        attribute v { text }
      }
    os2_lowerOpticalPointSize =
      element lowerOpticalPointSize {
        attribute v { text }
      }
    os2_upperOpticalPointSize =
      element upperOpticalPointSize {
        attribute v { text }
      }

