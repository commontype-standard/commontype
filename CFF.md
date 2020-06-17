# CFF - PostScript font program (Compact Font Format) table

## Introduction

### Specification

This table contains a compact representation of a PostScript Type 1, or
CIDFont and is structured according to Adobe Technical Note \#5176: [The
Compact Font Format
Specification](http://partners.adobe.com/asn/developer/pdfs/tn/5176.CFF.pdf)
and Adobe Technical Note \#5177: [The Type 2 Charstring
Format](http://partners.adobe.com/asn/developer/pdfs/tn/5177.Type2.pdf).

Existing TrueType fonts use a glyph index to specify and access glyphs
within a font, e.g. to index the loca table and thereby access glyph
data in the glyf table. This concept is retained in OpenType PostScript
fonts except that glyph data is accessed through the CharStrings INDEX
of the [CFF](#chapter.CFF) table.

### Annotation

The CFF specification was developed independantly of the OpenType
specification and is also meant to be used in other contexts. Because of
that, some CFF FontSets are not legal CFF tables. These restrictions
should be part of the OpenType specification and are mentioned here:

It is unclear whether the deletion mechanism of CFF FontSets (by setting
the first byte of a font name to 0) is allowed. Given the intended use,
it is not clear that such a mechanism is useful in OpenType fonts, and
we assume that it is not allowed.

It is unclear which font in a CFF FontSet should be used in the context
of an OpenType font. One possibility is to impose that the CFF FontSet
contain only one font, with the side effect of ruling out synthetic
fonts. Another possibility is to use the first font in the FontSet. Yet
another possibility is to use the font whose name matches some entry in
the [name](#chapter.name) table. We assume that the first possibility is
actually the desired one.

It is not clear whether the name stored in the Name INDEX must be equal
to some entry in the OpenType [name](#chapter.name) table.

While the Top DICT must define (explicitly or implicitly) an Encoding,
this Encoding is never used. Thus the best is to not include an Encoding
entry in the Top DICT and to get the default Standard Encoding,
regardless of the font content.

Since Multiple Master technology is not part of OpenType, the Top DICT
must not contain the operators BaseFontName and BaseFontBlend.

