# Changes log

## Version 1.4

### Specification

Released October 11, 2002

baselinetags.htm

  - Corrected typographic error.

  - Changed hanging baseline references from Hindi to Tibetan.

chapter2.htm

  - Corrected link to GDEF table.

  - Add documentation on new script tag 'DFLT'.

cmap.htm

  - Add Name column to tabular data to make consistent with other parts
    of spec.

  - Correct description of Encoding Record.

cvt.htm

  - Indicate that length must be integral value of FWORD units.

default.htm

  - Update the version number to 1.4.

dsig.htm

  - Provide information for ulVersion to be 0x00000001.

  - Update to show usFlag bits that are assigned.

  - Add section on signatures for TrueType Collections.

ebdt.htm

  - Change wording to indicate 'EBDT' is superset of 'bdat'. These are
    not the same.

featurelist.htm

  - Added new features: abvf, c2pc, ljmo, nlck, pcap, pref, rtla, tjmo,
    unic, and vjmo.

  - Change friendly name of 'calt' from Connection Forms to Contextual
    Alternates.

fpgm.htm

  - Add comment that array size n is the number of bytes in the table.

gdef.htm

  - Example 6, typos in the comments column for increasing 15 and 16ppem
    corrected.

gpos.htm

  - Clarify origin of Cartesian coordinate system at baseline of the
    left side.

  - Specify all values are done in font unit measurements.

  - Update images for better presentation.

  - PairPosFormat1 subtable ValueRecord changed to Offset,
    PairSetOffset\[PairSetCount\].

  - Update wording on MarkToMark attachment.

gsub.htm

  - Add Lookup Type 8, Reverse Chaining contextual single substitution.

hdmx.htm

  - Remove references to EGA.

  - Add statement that bit 2 of head.flag must be set to 1.

  - Add Name columns to tabular data for consistency with spec.

head.htm

  - Updated macStyle bit descriptions for bits 2 to 15.

  - unitsPerEm annotated that it should be a power of 2.

hhea.htm

  - Change FWord to FWORD for correct data type spelling.

ibmfc.htm

  - Fix formatting to indent subclasses for better readability.

name.htm

  - Add Name column to tabular data for consistency with spec.

  - Correct descriptions in Naming Table for count and
    nameRecord\[count\].

  - Clarified description of encoding ID 0/3. Added encoding ID 0/4.
    Changed description of encoding ID 3/10 to UTF-32.

  - Added description and example, for use of name ID 4 in CFF fonts.

  - Clarified working for use of name ID 5 (Version string).

  - Changed wording for name ID 16 (Preferred Family) and name ID 17
    (Preferred Subfamily).

  - Suggest that style strings (name ID 2 or 17) match with
    OS/2.usWeightClass and OS/2.usWidthClass.

os2.htm

  - Updated version number to 0x0003

  - Updated Unicode sub-range bits to be aligned with Unicode 3.2.

  - Remove weighted calculation of xAvgCharWidth.

  - Make fsType bits 0-3 to be mutually exclusive. In other words, only
    one of those bits may be set to "1" at a time. This is to avoid
    problems of ambiguity in what the font designer intends.

  - Change link to PANOSE specification.

  - Updated description of usFirstCharIndex, usLastCharIndex,
    usDefaultChar, usBreakChar; in context of fonts that provide
    surrogate character support.

otff.htm

  - Update filename information for TrueType outline fonts.

  - Add data types for FWORD and UFWORD.

  - Corrected content and description of TTC header v1 and v2.

  - Moved VORG table to PostScript Outlines group.

pclt.htm

  - Change to discourage use of this table.

proposals.htm

  - Remove proposed feature tags that were incorporated into this
    version.

recom.htm

  - Added recommendation for first four glyphs in font.

  - Added recommendation for shape of .notdef glyph.

scripttags.htm

  - Add script tags for Byzantine Music and Default.

ttinst2.doc

  - Corrected description in Logical\_Functions.Greater\_Than.

ttoreg.htm

  - Reworded and reorganized for better readability.

vdmx.htm

  - Change ratio record and vTable record to tabular format.

  - Recommend use of version 1 vdmx.

wgl4e.htm

  - Optional glyphs identified and marked. Added a footnote.

## Version 1.3

### Specification

Released April, 2001.

Multiple Master support in OpenType, discontinued. The following tables
pertaining to it have been removed from this version of the OpenType
specification: 'fvar', 'MMSD', 'MMFX'.

base.htm

  - BaseTagList Table: Added a sentence with a link to the baseline tags
    in the tags registry.

  - BaseCoord Format 4: removed

cff.htm

  - Removed references to MM fonts in the CFF and Type 2 Charstring
    Format specifications. See the change log in each specification for
    additional changes made.

chapter2.htm

  - Table Organisation: In paragraph 3, changed the number of types of
    GSUB and GPOS lookups. Phrase added to Paragraph 4 to exclude the
    Extension lookup.

  - LookupFlag bit enumeration: Name of the first bit reverted back to
    RightToLeft. Provided newer description of its use.

  - Coverage Table: added to exclude the Extension lookup.

cmap.htm

  - Merged paragraph 3 and 4 in the introduction section.

  - Added notes that fonts for Windows that support UCS-4 characters
    (surrogates), need to use an encoding ID 10 and format 12.

  - The version field has been renamed as 'language', to align it with
    Apple's TT spec. Added a note to clarify the use of this field.

  - Added information that platform ID 3, encoding ID 7,8 and 9 are
    reserved.

  - Added platform ID 3, encoding ID 10.

  - Swapped the description of encoding ID 3 and 4. They were
    incorrectly mapped to Big5 and PRC respectively, in earlier versions
    of the specification.

  - Added a note on OTF Windows compatibility mapping.

  - Formats 2, 4, 6. Made the description of the 'length' field in these
    formats consistent with the rest of the formats.

  - Format 2: Removed the duplicate entry for subHeaders\[ \].

  - Format 4: Corrected 'endCode' and 'startCode' values in the example
    for this format.

  - Supporting 4-byte character codes (Formats 8, 10, 12): Added these
    new formats.

ebdt.htm

  - minor typo in the name of ebdtComponent corrected.

feattags.htm

  - Added features 'ccmp', 'fin2', 'fin3', med2' and 'rlig'.

  - Clarified the Feature Interaction sections for 'kern', 'vkrn'.

  - UB lookup type to be used, in the Recommended implementation section
    of 'ordn'.

fvar.htm: This table removed.

gdef.htm

  - Introduction: Added information on the MarkAttachClassDef field.

  - Overview: Updated image to contain MarkAttachClassDef.

  - GDEF Header: Added missing information on the MarkAttachClassDef
    field.

  - GDEF Header Table: Added the note that offsets might be null for the
    GlyphClassDef, AttachList, LigCaretList, MarkAttachClassDef

  - GlyphClassDef Enumeration List: An explanatory note added for
    definition of ligatures and component glyphs.

  - Mark Attachment Class Definition Table: An explanatory section and
    example 7 added.

  - CaretValue: Format 4: This format used by MM fonts removed.

gpos.htm

  - Corrected the link "Common Table Formats" to read "OpenType Common
    Table Formats"; throughout table.

  - Table Organization: Updated the image. Added links for all lookup
    types. Added Extension positioning as LookupType 9, types 10+ are
    now Reserved.

  - PairPosFormat1 subtable: PairSet field corrected to specify it as an
    array of Offsets.

  - Lookup Type 6: Sentence added to clarify input context for
    MarkToBase, MarkToLigature and MarkToMark positioning tables.

  - LookupType 9: Extension Positioning: This new lookup type added.

  - ValueRecord table: Removed XIdPlacement, YIdPlacement, XIdAdvance,
    YIdAdvance and the sentence following the table.

  - ValueFormat bit enumeration: Removed XIdPlacement, YIdPlacement,
    XIdAdvance, YIdAdvance and the sentence following the table.

  - Anchor Table: Format 4: This format used by MM fonts removed

gsub.htm

  - Corrected the link "Common Table Formats" to read "OpenType Common
    Table Formats"; throughout table.

  - Substituting Glyphs with OpenType: Types of lookups corrected to
    six. Added an explanation to the ligature substitution section, to
    clarify the location occupied by a ligature glyph when it replaces a
    sequence of glyphs. Missing paragraph on Chaining contextual
    substitution added.

  - Table Organization: Updated image.

  - LookupType Enumeration table for glyph substitution: Added links for
    all lookup types. Added Extension Substitution as the 7th lookup
    type. This hence classifies types 8+ as Reserved.

  - LookupType 2:: Prohibited the deletion of an input glyph, and added
    that GlyphCount should always be greater than 0.

  - Chaining Context Substitution Format 1: Simple Chaining Context
    Glyph Substitution: Added that the match for the string 'backtrack
    sequence + input sequence + lookahead sequence' takes place in the
    simplest of cases; and that lookup flag values affect
    backtrack/lookahead sequences. Since the input sequence includes the
    covered glyph, removed "covered glyph" from the above string.

  - LookupType 7: Extension Substitution: This new lookup type added.

head.htm

  - table: Clarified description for bit 1, 5-10. Added specification
    for bit 13.

hhea.htm

  - table: Added a footnote for the fields Ascender, Descender and
    LineGap.

hmtx.htm

  - Added a note that the advanceWidth for each glyph in CFF OpenType
    fonts must match its x width in the CFF table.

loca.htm

  - Corrected minor typo.

maxp.htm

  - Added a note to indicate the difference in representing the
    fractional part of a version number when it is non-zero.

mmfx.htm: This table removed.

mmsd.htm: This table removed.

name.htm

  - Minor rewording of text done in the introduction section related to
    fonts for the Macintosh.

  - Platform ID, specific encoding ID and languageId information
    combined into one table.

  - Unicode platform-specific encoding IDs (platform ID = 0): This new
    table added.

  - Microsoft platform-specific encoding IDs: This table replaced with a
    more comprehensive table from the cmap.htm.

  - Mac platform-specific encoding IDs: Clarified IDs 2 and 25.
    Corrected typo in ID 32.

  - Mac language IDs: Newer IDs added 23-150.

  - ISO specific encodings (platform ID=2): Marked as deprecated. Minor
    typo in the sentence below the table corrected.

  - Custom platform-specific encoding IDs (platform ID = 4): Newer
    platform ID added.

  - Name IDs: Added newer description for nameID 5. Added nameID 19 and
    20.

  - Examples: Added example for nameID 19.

  - LCID-CP list: Updated this list.

os2.htm

  - xAvgCharWidth.description: Comments for this field updated.

  - fsType.table: Added Bit Mask and description details for the case
    when no bit is set; added Bit Mask value 0x0001.

  - fsType.comments: Information on setting Bit Masks consolidated into
    the description column of the table. Removed the redundant section
    below the table.

  - yStrikeoutPosition.description: Added that this is the distance of
    the top of the strikeout stroke.

  - panose.description: Removed dead url for the PANOSE evaluation
    document, added that the "greybook" reference could be used instead.

  - ulUnicodeRange.table: Updated the Unicode standard version number to
    3.0 in the description for these fields. Added bits 70- 127. Added a
    footnote for setting bit 57 (Surrogates).

  - usFirstCharIndex.description: Minor correction-- added the word
    platform specific.

  - sTypoAscender and sTypodescender: Minor corrections done; "design
    space" now referred to as "ideo em box" in the descriptions; added a
    links to recom.htm for these fields.

  - usWinAscent: Explanatory note added to explain the circumstances in
    which clipping will take place.

  - usWinDescent: Explanatory note added to explain the circumstances in
    which clipping will take place.

  - sxHeight: Added a note that this metric can be used in font
    substitution.

  - usDefaultChar: that for a given font, missing glyphs will be
    displayed using the content of glyph 0 in the selected font.

otff.htm

  - Version Numbers: Added explanation that representation of a non-zero
    fractional part in version numbers, differs from the representation
    of the matissa.

  - Tables Related to PostScript Outlines: Removed links and description
    details for the fvar, MMSD and MMFX tables.

  - Advanced Typographic Tables: Added a link to OpenType Layout Common
    Table Formats.

  - Other OpenType Tables: the VORG table name to the list.

otover.htm: Related documentation: Removed sections in the description
related to MM fonts.

post.htm

  - table.version.description: Added versions 2.5 and 3.0

  - table.underlinePosition.description: PostScript information added.

  - version2.0: Updated name and description details in the table
    contents

  - version2.5: Updated table contents, added that this version has been
    deprecated.

recom.htm

  - [BASE](#chapter.BASE) Table: This section added.

  - [cmap](#chapter.cmap) table: Added details on requirements that need
    to be satisfied by surrogate fonts on Windows.

  - [head](#chapter.head) Table: Added details regarding usage of the
    fontRevision value.

  - [hhead](#chapter.hhead) Table: Removed sentence which incorrectly
    stated that OpenType fonts that include CFF data must set
    numberOfHMetrics equal to the number of glyphs in the font.

  - [post](#chapter.post) Table: Updated content related to glyph names
    in the post table.

  - 'os/2' Table: Added section on sTypoAscender, sTypoDescender,
    sTypoLineGap.

  - General Recommendations: Updated the table ordering list for
    OpenType fonts containing CFF data by adding the
    [maxp](#chapter.maxp) table; and, removing the 'fvar' and 'MMSD'
    tables.

  - Baseline to Baseline Distances: Added a paragraph on the recommended
    use of sTypoAscender, sTypoDescender, and sTypoLineGap.

  - OpenType CJK Font Guidelines: This new section added.

ttochap1.htm

  - Introduction: Removed 'MMSD' reference. Expanded the brief
    description of the content of Registered OpenType Layout Tags to
    reflect all OpenType tags: scripts, languages, baselines, features.

  - How Multiple Master OpenType Fonts Use OpenType Layout Tables: This
    section removed.

ttoreg.htm

  - Added links in the introduction section, to help jump to the script,
    language, baseline and feature tag sections.

  - Script tags: Corrected script tag length description. Added newer
    script tags.

  - Language system tags: Added newer language tags.

  - Baseline tags: Added newer baseline tags: "icfb", "icft" and "idtp".
    Expanded the description of existing tags into two
    categories:"Baseline for HorizAxis" and "Baseline for VertAxis".

  - Ideographic Em-Box: This new section added.

  - Ideographic Character Face: This new section added.

vhea.htm

  - Introduction: Added a link each for the vmtx table and the CJK
    guidelines section.

  - table.version.description: Version number increased to 1.1. Added a
    note to indicate the difference in representing the fractional part
    of a version number when it is non-zero.

  - table.ascent: Replaced by vertTypoAscender.

  - table.descent: Replaced by vertTypoDescender.

  - table.lineGap: Replaced by vertTypoLineGap.

  - Vertical Header Table Example: Changed version value to 1.1.
    Corrected the name for vertTypoLineGap

vmtx.htm

  - Introduction: Added a link for accessing the CJK guidelines section.

  - Vertical Origin and Advance Height: This new section added.

  - Vertical Metrics Table Format: Added a note on the calculating the
    top side bearing.

vorg.htm

  - This new table added. This is needed by CFF OpenType fonts to locate
    the origin of vertical glyphs.

wgl4d.htm

  - Added a missing asterisk for PostScriptName.macron

  - Added the U+02dc (tilde)-- was missing from the list.

## Version 1.25

### Specification

Released July, 2000

feattags.htm (Feature Tags)

  - Features added: abvm (Above-base Mark Positioning); abvs (Above-base
    Substitutions); akhn (Akhand); blwf (Below-base Forms); blws
    (Below-base Substitutions); clig (Contextual Ligatures); cswh
    (Contextual Swash); curs (Cursive Positioning); dist (Distances);
    falt (Final Glyph on Line Alternates); half (Half Forms); haln
    (Halant Forms); hkna (Horizontal Kana Alternates); isol (Isolated
    Forms); jalt (Justification Alternates); locl (Localized Forms)
    (replaces jajp, kokr, vivn, zhch, and zhtw); mkmk (Mark to Mark
    Positioning); nukt (Nukta Forms); pres (Pre-base substitutions);
    pstf (Post-base Forms); psts (Post-base Substitutions); rphf (Reph
    Forms); ruby (Ruby Notation Forms); size (Optical Size); vatu (Vattu
    Variants); vhal (Alternate Vertical Half Metrics); vkna (Vertical
    Kana Alternates); vkrn (Vertical Kerning) vpal (Proportional
    Alternate Vertical Metrics).

  - Features removed: crcy (Currency), dpng (Diphthongs), jajp (Japanese
    Forms), kokr (Korean Forms), vivn (Vietnamese Forms), zhcn
    (Simplified Chinese Forms), zhtw (Traditional Chinese Forms).

  - Features modified: aalt: Added ordering suggestion, reworked user
    interface suggestions, clarified implementation recommendation,
    feature interaction and function. altv: changed tag to valt. c2sc,
    dlig: Clarified function, example and feature interaction. calt,
    case, dnom, expt, halt, hist, hwid, jp78, jp83, jp90, kern, lfbd,
    liga, lnum, numr, onum, pwid, qwid, rtbd, smpl, sups, titl, twid,
    valt: Clarified feature interaction. fina, init, medi, rand, salt,
    swsh: Clarified user interface suggestion and feature interaction.
    frac: Added numr and dnom extensions, clarified feature interaction.
    fwid, palt: Clarified feature interaction and function. hngl:
    Clarified feature interaction and implementation recommendation.
    ital: Clarified function and feature interaction. mark: Added
    example, application interface, user interface suggestion, script
    sensitivity, feature interaction. Modified recommended
    implementation. mset: Added example. nalt: Clarified user interface
    suggestion, implementation recommendation and feature interaction.
    opbd: Added lfbd and rtbd extensions; clarified user interface
    suggestion and feature interaction. ordn: Clarified script
    sensitivity, corrected lookup type, clarified implementation
    recommendation and feature interaction. ornm: Clarified user
    interface suggestion, implementation recommendation, feature
    interaction and function description. smcp: Added note about
    dotlessi; clarified function and feature interaction. trad:
    corrected terminology (hanzi, not hanja), clarified user interface
    suggestion and implementation recommendation. vert: Clarified
    feature interaction and added ordering recommendation; extended
    application interface notes. vrt2: Changed 'friendly' name,
    clarified feature interaction and added ordering recommendation;
    added ATM/OTF driver information and descriptions of how to
    construct the rotated glyphs in the Function section. zero:
    Clarified user interface suggestion.

  - Features relocated: mark and mset have been moved from the Metric
    Behaviors category, to the Other Substitutions category for
    consistency in classification.

chapter2.htm

  - modified description of FeatureParams field for a non-null offset
    (the size feature uses it).

## Version 1.2

### Specification

Released November, 1998

Data type notation and spelling corrected throughout

base.htm - added BaseCoord Table Format 4

chapter2.htm - corrected example 3; refined description of next glyph;
reserved RightToLeft lookup flag; corrected descriptions of LookupFlag
bits

cmap.htm - removed legacy encodings

dsig.htm - updated field names and format of signature record; added
step to creation of content digest

feattags.htm - registered new features crcy, dnom, jajp, kokr, lfbd,
numr, rtbd, vivn, vrt2, zhcn, zhtw; removed features trak, vrot; edited
and clarified descriptions of features afrc, altv, c2sc, calt, case,
cpsp, dlig, dpng, expt, fina, frac, fwid, halt, hlig, lngl, hwid, init,
ital, jp78, jp90, kern, lnum, medi, mgrk, onum, opbd, ordn, ornm, palt,
pnum, pwid, qwid, smcp, smpl, sups, tnam, tnum, trad, twid, vert

gdef.htm - added MarkAttachClassDef to header, and MarkAttachmentType
bit setting to LookupFlag bits; added CaretValue Table Format 4

glyf.htm - added table detailing component record structure

gsub.htm - added format 6, for chaining contextual substitution; general
editing

gpos.htm - added format 8, for chaining contextual positioning;
clarified pair positioning operations; corrected Example 10; clarified
coordinate system description; refined description of when a lookup is
finished; added AnchorTable Format 4; general editing

head.htm - added note about fontRevision field; clarified description of
compression flag

hhea.htm - corrected description of numberOfHMetrics

mmfx.htm - corrections throughout; added MMFXIdZero

name.htm - general editing

os2.htm - renamed usMaxLookup to usMaxContext; edited descriptions of
defaultChar and breakChar; updated registered vendors

otff.htm - general editing; added ulDsigTag and related fields to TTC
header; added datatypes LONGDATETIME; clarified checksum calculations;
added tag name restrictions; clarified use of version numbers

post.htm - renamed FormatType to Version

vhea.htm - replaced mention of centerline with vertical baseline;
corrected description of numOfLongVerMetrics

CFF.pdf and Type2.pdf updated (December 1998)

Several PostScript glyph names corrected in the WGL tables (18 December
1998)

name.htm - Descriptions of name ID 13 and 14 corrected (29 January 1999)

mmsd.htm - Attribute flags corrected (29 January 1999)

head.htm - Data type of xMin corrected (29 January 1999)

## Version 1.1

### Specification

Released April, 1999

CFF and Type2 specs updated

chapter2.htm - corrected typo in figure 2d (fig2d.gif)

dsig.htm - added info about location of DSIG table; added list of sfnt
structural requirements

feattags.htm - created more comprehensive list and description of layout
feature tags

gpos.htm - corrected illustration 4f (fig4f.gif)

head.htm - added bit 12 (converted) to flags field

hhea.htm - removed CFF restriction listed in numberOfHMetrics field;
added caretOffset field.

maxp.htm - added version 0.5 table (numGlyphs field); general editing

name.htm - added name id's 16, 17, and 18; corrected name id example

os2.htm - added new version (2), adding new fields sxHeight, sCapHeight,
usDefaultChar, usBreakChar, usMaxLookup; clarified sTypoAscender and
sTypoDescender fields; changed some Unicode range values to reflect
Unicode 2; updated registered vendors

otff.htm - general editing; added description of two types of TTC
headers, and DSIG table location

recom.htm - general editing

## Version 1.01

### Specification

Released October, 1997

mmfx.htm, fvar.htm, mmsd.htm, otover.htm, recom.htm - edits throughout

loca.htm - changed long-aligned to word-aligned for local offsets

wgl4.htm - added reference to Euro symbol

dsig.htm - added note about system use of dsig table to distinguish OT
from TT fonts

ttoreg.htm - added VIT, TRK, and ROM lang sys tags

otff.htm - rearranged table list

base.htm - change to basecoordformat3 data type

gpos.htm - pairposformat1 subtable valuerecord becomes offset

kern.htm - gpos clarification

name.htm - added name id's 13 and 14

ltsh.htm - clarified option for fixed-pitch fonts

dmx.htm - version 1 added to vdmx table

os2.htm - added codepage range 8 for Vietnamese; added new vendor id's,
including UNKN

## Version 1.0

### Specification

Released April, 1997

