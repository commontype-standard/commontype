# Overview

## Introduction

### Specification

The OpenType font format is an extension of the TrueType font format,
adding support for PostScript font data. The OpenType font format was
developed jointly by Microsoft and Adobe. OpenType fonts and the
operating system services which support OpenType fonts provide users
with a simple way to install and use fonts, whether the fonts contain
TrueType outlines or CFF (PostScript) outlines.

The OpenType font format addresses the following goals:

  - broader multi-platform support

  - better support for international character sets

  - better protection for font data

  - smaller file sizes to make font distribution more efficient

  - broader support for advanced typographic control

OpenType fonts are also referred to as TrueType Open v.2.0 fonts,
because they use the TrueType 'sfnt' font file format. PostScript data
included in OpenType fonts may be directly rasterized or converted to
the TrueType outline format for rendering, depending on which
rasterizers have been installed in the host operating system. But the
user model is the same: OpenType fonts just work. Users will not need to
be aware of the type of outline data in OpenType fonts. And font
creators can use whichever outline format they feel provides the best
set of features for their work, without worrying about limiting a font's
usability.

OpenType fonts can include the OpenType Layout tables, which allow font
creators to design better international and high-end typographic fonts.
The OpenType Layout tables contain information on glyph substitution,
glyph positioning, justification, and baseline positioning, enabling
text-processing applications to improve text layout.

As with TrueType fonts, OpenType fonts allow the handling of large glyph
sets using Unicode encoding. Such encoding allows broad international
support, as well as support for typographic glyph variants.

Additionally, OpenType fonts may contain digital signatures, which
allows operating systems and browsing applications to identify the
source and integrity of font files, including embedded font files
obtained in web documents, before using them. Also, font developers can
encode embedding restrictions in OpenType fonts, and these restrictions
cannot be altered in a font signed by the developer.

## Related documentation

### Specification

The following documents may be consulter for further information:

  - Adobe Technical Note \#5176: "The Compact Font Format
    Specification."

  - Adobe Technical Note \#5177: "Type 2 Charstring Format."

  - TrueType 1.0 Font Files, Technical Specification. Microsoft.

  - OpenType Layout Font Specification. Microsoft.

  - Adobe Type 1 Font Format. Addison Wesley, 1991; ISBN 0-201-57044-0.

  - Adobe Technical Note \#5015: "The Type 1 Font Format Supplement."
    This document contains all updates to the Type 1 format.

  - Adobe Technical Note \#5087: "Multiple Master Font Programs for the
    Macintosh."

  - Adobe Technical Note \#5088 "Font Naming Issues." This document
    discusses general font name issues.

  - Adobe's Unicode and Glyph Names guide.

