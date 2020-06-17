# Advanced Typographic Extensions – OpenType Layout

## Overview

### Specification

The Advanced Typographic tables (OpenType Layout tables) extend the
functionality of fonts with either TrueType or CFF outlines. OpenType
Layout fonts contain additional information that extends the
capabilities of the fonts to support high-quality international
typography:

  - OpenType Layout fonts allow a rich mapping between characters and
    glyphs, which supports ligatures, positional forms, alternates, and
    other substitutions.

  - OpenType Layout fonts include information to support features for
    two-dimensional positioning and glyph attachment.

  - OpenType Layout fonts contain explicit script and language
    information, so a text-processing application can adjust its
    behavior accordingly.

  - OpenType Layout fonts have an open format that allows font
    developers to define their own typographical features.

This overview introduces the power and flexibility of the OpenType
Layout font model. The OpenType Layout tables are described in more
detail in the "Font File Tables" section of the OpenType specification.

OpenType Layout Common Table Formats are documented in the chapter
"OpenType Layout Common Table Formats".

Registered OpenType Layout Tags for scripts, languages, and baselines,
are documented in the chapter "OpenType Layout Registered Features".

## OpenType Layout at a Glance

### Specification

OpenType Layout addresses complex typographical issues that especially
affect people using text-processing applications in multi-lingual and
non-Latin environments.

OpenType Layout fonts may contain alternative forms of characters and
mechanisms for accessing them. For example, in Arabic, the shape of a
character often varies with the character's position in a word. As shown
here, the ha character will take any of four shapes, depending on
whether it stands alone or whether it falls at the beginning, middle, or
end of a word. OpenType Layout helps a text-processing application
determine which variant to substitute when composing text.

![Figure 1a. Isolated, initial, medial, and final forms of the Arabic
character ha.](fig1a.gif)

Similarly, OpenType Layout helps an application use the correct forms of
characters when text is positioned vertically instead of horizontally,
such as with Kanji. For example, Kanji uses alternative forms of
parentheses when positioned vertically.

![Figure 1b. Alternative forms of parentheses used when positioning
Kanji vertically.](fig1b.gif)

The OpenType Layout font format also supports the composition and
decomposition of ligatures. For example, English, French, and other
languages based on Latin can substitute a single ligature, such as "fi",
for its component glyphs - in this case, "f" and "i". Conversely, the
individual "f" and "i" glyphs could replace the ligature, possibly to
give a text-processing application more flexibility when spacing glyphs
to fill a line of justified text.

![Figure 1c. Two Latin glyphs and their associated ligature.](fig1c.gif)

![Figure 1d. Three Arabic glyphs and their associated
ligature](fig1d.gif)

Glyph substitution is just one way OpenType Layout extends font
capabilities. Using precise X and Y coordinates for positioning glyphs,
OpenType Layout fonts also can identify points for attaching one glyph
to another to create cursive text and glyphs that need diacritical or
other special marks.

OpenType Layout fonts also may contain baseline information that
specifies how to position glyphs horizontally or vertically. Because
baselines may vary from one script (set of characters) to another, this
information is especially useful for aligning text that mixes glyphs
from scripts for different languages.

![Figure 1c. A line of text, baselines adjusted, mixing Latin and Arabic
scripts.](fig1e.gif)

## TrueType versus OpenType Layout

### Specification

A TrueType font is a collection of several tables that contain different
types of data: glyph outlines, metrics, bitmaps, mapping information,
and much more. OpenType Layout fonts contain all this basic information,
plus additional tables containing information for advanced typography.

Text-processing applications - referred to as "clients" of OpenType
Layout - can retrieve and parse the information in OpenType Layout
tables. So, for example, a text-processing client can choose the correct
character shapes and space them properly.

As much as possible, the tables of OpenType Layout define only the
information that is specific to the font layout. The tables do not try
to encode information that remains constant within the conventions of a
particular language or the typography of a particular script. Such
information that would be replicated across all fonts in a given
language belongs in the text-processing application for that language,
not in the fonts.

## OpenType Layout Terminology

### Specification

The OpenType Layout model is organized around glyphs, scripts, language
systems, and features

**Characters versus glyphs**

Users don't view or print characters: a user views or prints glyphs. A
glyph is a representation of a character. The character "capital letter
A" is represented by the glyph "A" in Times New Roman Bold and "A" in
Arial Bold. A font is a collection of glyphs. To retrieve glyphs, the
client uses information in the "cmap" table of the font, which maps the
client's character codes to glyph indices in the table.

Glyphs can also represent combinations of characters and alternative
forms of characters: glyphs and characters do not strictly correspond
one-to-one. For example, a user might type two characters, which might
be better represented with a single ligature glyph. Conversely, the same
character might take different forms at the beginning, middle, or end of
a word, so a font would need several different glyphs to represent a
single character. OpenType Layout fonts contain a table that provides a
client with information about possible glyph substitutions.

![Figure 1f. Multiple glyphs for the ampersand character.](fig1f.gif)

**Scripts**

A script is composed of a group of related characters, which may be used
by one or more languages. Latin, Arabic, and Thai are examples of
scripts. A font may use a single script, or it may use many scripts.
Within an OpenType Layout font, scripts are identified by unique 4-byte
tags.

![Figure 1g. Glyphs in the Latin, Kanji, and Arabic scripts.](fig2a.gif)

**Language systems**

Scripts, in turn, may be divided into language systems. For example, the
Latin script is used to write English, French, or German, but each
language has its own special requirements for text processing. A font
developer can choose to provide information that is tailored to the
script, to the language system, or to both.

Language systems, unlike scripts, are not necessarily evident when a
text-processing client examines the characters being used. To avoid
ambiguity, the user or the operating system needs to identify the
language system. Otherwise, the client will use the default
language-system information provided with each script.

![Figure 1h. Differences in the English, French, and German language
system.](fig1h.gif)

**Features**

Features define the basic functionality of the font. A font that
contains tables to handle diacritical marks will have a "mark" feature.
A font that supports substitution of vertical glyphs will have a "vert"
feature.

The OpenType Layout feature model provides great flexibility to font
developers because features do not have to be predefined by Microsoft
Corporation. Instead, font developers can work with application
developers to determine useful features for fonts, add such features to
OpenType Layout fonts, and enable client applications to support such
features.

![Figure 1i. The relationship of scripts, language systems, features,
and lookups for substitution and positioning tables.](fig1i.gif)

**OpenType Layout tables**

OpenType Layout comprises five new tables: GSUB, GPOS, BASE, JSTF, and
GDEF. These tables and their formats are discussed in detail in the
chapters that follow this overview.

GSUB: Contains information about glyph substitutions to handle single
glyph substitution, one-to-many substitution (ligature decomposition),
aesthetic alternatives, multiple glyph substitution (ligatures), and
contextual glyph substitution.

GPOS: Contains information about X and Y positioning of glyphs to handle
single glyph adjustment, adjustment of paired glyphs, cursive
attachment, mark attachment, and contextual glyph positioning.

BASE: Contains information about baseline offsets on a script-by-script
basis.

JSTF: Contains justification information, including whitespace and
Kashida adjustments.

GDEF: Contains information about all individual glyphs in the font: type
(simple glyph, ligature, or combining mark), attachment points (if any),
and ligature caret (if a ligature glyph).

Common Table Formats: Several common table formats are used by the
OpenType Layout tables.

## Text processing with OpenType Layout fonts

### Specification

A text-processing client follows a standard process to convert the
string of characters entered by a user into positioned glyphs. To
produce text with OpenType Layout fonts:

1.  Using the cmap table in the font, the client converts the character
    codes into a string of glyph indices.

2.  Using information in the GSUB table, the client modifies the
    resulting string, substituting positional or vertical glyphs,
    ligatures, or other alternatives as appropriate.

3.  Using positioning information in the GPOS table and baseline offset
    information in the BASE table, the client then positions the glyphs.

4.  Using design coordinates the client determines device-independent
    line breaks. Design coordinates are high-resolution and
    device-independent.

5.  Using information in the JSTF table, the client justifies the lines,
    if the user has specified such alignment.

6.  The operating system rasterizes the line of glyphs and renders the
    glyphs in device coordinates that correspond to the resolution of
    the output device.

Throughout this process the text-processing client keeps track of the
association between the character codes for the original text and the
glyph indices of the final, rendered text. In addition, the client may
save language and script information within the text stream to clearly
associate character codes with typographical behavior.

### Annotation

An alternative point of view is to say that the font, and in particular
the GSUB and GPOS tables contain fragments of programs which operate on
a glyph run. The layout engine decides how the typographic treatments
specified in its input should be realized, and in particular whether
some of the programs fragments should be invoked to manipulate the glyph
run. These program fragments are written in a very specialized language.

The implementation of the glyph run structure is not part of this
specification. However, there is some connection since the GSUB and GPOS
programs do operate on that structure. We capture here this connection
in the form of an interface:

    GlyphRun interface ==
          
    package com.adobe.aots.opentype;
    
    public interface GlyphRun {
      glyphrun.methods: 1, 2, 3, 4, 5, 6
    }

First, we have two simple methods to access the number of glyphs in the
run and the ID of glyph at a specific position:

    GlyphRun interface ==
          
      public int glyphCount ();
      public int glyphAt (int pos);

Another pair of accessors, this time to get the position of a glyph:

    GlyphRun interface ==
          
      public int getXPos (int g);
      public int getYPos (int g);

The specification does not address the situation where a feature is
applied to only part of a glyph run. However, it is necessary to support
that situation: consider the case of a fragment on which 'onum' is
applied, while 'kern' is applied to whole glyph run. Clearly, it is not
possible to decompose that glyph run in three independant glyph runs to
be processed separately, since it would imply no kerning between the
last glyph subject to 'onum' and the glyph followin it. Thus, a
GPOS/GSUB engine needs to figure out if a given lookup is to be applied
at a given position:

    GlyphRun interface ==
          
      public boolean isLookupApplied (int lookupIndex, int start, int stop);

The MarkToLigature GPOS lookup type has the implicit notion of ligature
component, and of the component to which a mark following a ligature
attaches to:

    GlyphRun interface ==
          
      public void setLigComponents (int[] components);
      public int getLigComponent (int g);

The GSUB lookups result in the replaced of one or more glyphs by one or
more glyphs:

    GlyphRun interface ==
          
      public void replace (int position, int replacementGlyph);
      public void replace (int position, int[] replacementGlyphs);
      public void replace (int[] positions, int replacementGlyph);

The GPOS lookups result in the adjustment of a glyph position:

    GlyphRun interface ==
          
      public void adjustPlacementAndAdvance (int g, ValueRecord vr);
      public void move (int g, int x, int y);

## OpenType Layout fonts in Windows 95

### Specification

The core system fonts in the Middle East and Far East versions of
Windows 95 are OpenType Layout fonts. These fonts demonstrate aspects of
OpenType Layout's versatility.

**Middle East Windows 95**

Middle East Windows 95 uses several Arabic OpenType Layout fonts: fixed
regular weight, proportional regular weight, fixed bold, and
proportional bold. These fonts take advantage of many glyph substitution
features available in OpenType Layout, namely simple substitution
(one-to-one contextual), ligature substitution (many-to-one), and mark
set substitutions. In Middle East Windows 95, the operating system
itself handles glyph substitution, using data in the GSUB table of each
font.

**Far East Windows 95**

Far East Windows 95 also uses several OpenType Layout fonts: fixed
serif, proportional serif, fixed sans serif, and proportional sans
serif. The Japanese fonts take advantage of a subset of OpenType Layout
features, including vertical glyph substitution and baseline
positioning. As with Middle East Windows 95, the operating system in Far
East Windows 95 will handle glyph substitution, using data in the GSUB
table in each font. However, the text-processing client will need to
handle baseline positioning, using data in the BASE table in each font.

