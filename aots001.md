# About this specification

## Overview

### Specification

This specification details the format of OpenType fonts, the TrueType
and CFF outline formats, and the TrueType hinting language. This
specification has been developed jointly by Adobe and Microsoft. Because
OpenType is an extension of TrueType, there is also information in this
document that was originally authored by Apple.

Many references to both TrueType and PostScript exist throughout this
document, as OpenType fonts combine the two technologies.

If you have comments or suggestions about this document, please send
mail to the Microsoft Typography Group.

### Annotation

The “Annotation” sections provides clarification of the published
specification, sometimes by suggesting a different wording, sometimes by
providing background information.

The “Specification” sections contain the exact text of version 1.3 of
the OpenType specification.

### XML Representation

The “XML representation” sections propose an XML representation of
OpenType fonts. The mains goals are:

  - allow the precise representation of fonts in an XML form, to
    facilitate exchange, manipulation by programs, or archival of fonts.

  - be a convenient form to author fonts or fragments of fonts; in
    particular, facilitate the creation of fonts to test OpenType
    engines.

The XML representation is currently formalized in a Relax NG schema,
expressed here in the compact syntax.

### Validation

The “Validation” sections are the source code for a font validator. The
intent is that the validator would detect violation of the
specification, as well as violation of additional rules and dubious
constructs.

