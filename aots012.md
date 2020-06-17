# IBM Font Class Parameters

## Introduction

### Specification

This section defines the IBM Font Class and the IBM Font Subclass
parameter values to be used in the classification of font designs by the
font designer or supplier. This information is stored in the
sFamilyClass field of a font's OS/2 table.

sFamilyClass

Format: 2-byte signed short

Title: Font-family class and subclass. Also see section 3.4.

Description: This parameter is a classification of font-family design.

Comments: The font class and font subclass are registered values
assigned by IBM to each font family. This parameter is intended for use
in selecting an alternate font when the requested font is not available.
The font class is the most general and the font subclass is the most
specific. The high byte of this field contains the family class, while
the low byte contains the family subclass.

These values classify a font design as to its appearance, but do not
identify the specific font family, typeface variation, designer,
supplier, size, or metric table differences. It should be noted that
some font designs may be classified equally well into more than IBM Font
Class or Subclass. Such designs should be matched to a classification
for which substitution of another font design from the same class or
subclass would generally result in a similar appearance of the presented
document.

## Class ID = 0 No Classification

### Specification

This class ID is used to indicate that the associated font has no design
classification or that the design classification is not of significance
to the creator or user of the font resource.

## Class ID = 1 Oldstyle Serifs

### Specification

This style is generally based upon the Latin printing style of the 15th
to 17th century, with a mild diagonal contrast in stroke emphasis
(lighter in upper left to lower right, heavier in upper right to lower
left) and bracketed serifs. This IBM Class reflects the ISO Serif Class,
Oldstyle and Legibility Subclasses as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design subclassification is not of
significance to the creator or user of the font resource.

**Subclass ID = 1 : IBM Rounded Legibility**

This style is generally characterized by a large x-height, with short
ascenders and descenders. Specifically, it is distinguished by a medium
resolution, hand tuned, bitmap rendition of the more general rounded
legibility subclass. An example of this font style is the IBM Sonoran
Serif family. This IBM Subclass reflects the ISO Serif Class, Legibility
Subclass, and Rounded Specific Group as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 2 : Garalde**

This style is generally characterized by a medium x-height, with tall
ascenders. An example of this font style is the ITC Garamond family.
This IBM Subclass reflects the ISO Serif Class, Oldstyle Subclass, and
Garalde Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 3 : Venetian**

This style is generally characterized by a medium x-height, with a
relatively monotone appearance and sweeping tails based on the designs
of the early Venetian printers. An example of this font style is the
Goudy family. This IBM Subclass reflects the ISO Serif Class, Oldstyle
Subclass, and Venetian Specific Group as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 4 : Modified Venetian**

This style is generally characterized by a large x-height, with a
relatively monotone appearance and sweeping tails based on the designs
of the early Venetian printers. An example of this font style is the
Allied Linotype Palatino family. This IBM Subclass reflects the ISO
Serif Class, Transitional Subclass, and Modified Specific Group as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 5 : Dutch Modern**

This style is generally characterized by a large x-height, with wedge
shaped serifs and a circular appearance to the bowls similar to the
Dutch Traditional Subclass below, but with lighter stokes. An example of
this font style is the Monotype Times New Roman family. This IBM
Subclass reflects the ISO Serif Class, Oldstyle Subclass, and Dutch
Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 6 : Dutch Traditional**

This style is generally characterized by a large x-height, with wedge
shaped serifs and a circular appearance of the bowls. An example of this
font style is the IBM Press Roman family. This IBM Subclass reflects the
ISO Serif Class and Legibility Subclass as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 7 : Contemporary**

This style is generally characterized by a small x-height, with light
stokes and serifs. An example of this font style is the University
family. This IBM Subclass reflects the ISO Serif Class and Contemporary
Subclass as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 8 : Calligraphic**

This style is generally characterized by the fine hand writing style of
calligraphy, while retaining the characteristic Oldstyle appearance.
This IBM Subclass is not reflected in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 9-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 2 Transitional Serifs

### Specification

This style is generally based upon the Latin printing style of the 18th
to 19th century, with a pronounced vertical contrast in stroke emphasis
(vertical strokes being heavier than the horizontal strokes) and
bracketed serifs. This IBM Class reflects the ISO Serif Class,
Transitional Subclass as documented in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Direct Line**

This style is generally characterized by a medium x-height, with fine
serifs, noticeable contrast, and capitol letters of approximately the
same width. An example of this font style is the Monotype Baskerville
family. This IBM Subclass reflects the ISO Serif Class, Transitional
Subclass, and Direct Line Specific Group as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 2 : Script**

This style is generally characterized by a hand written script
appearance while retaining the Transitional Direct Line style. An
example of this font style is the IBM Nasseem (Arabic) family. This IBM
Subclass is not specifically reflected in the 12/87 ISO/IEC 9541-5 draft
standard, though the ISO Serif Class, Transitional Subclass, and Direct
Line Specific Group would be a close approximation.

**Subclass ID = 3-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 3 Modern Serifs

### Specification

This style is generally based upon the Latin printing style of the 20th
century, with an extreme contrast between the thick and thin portion of
the strokes. This IBM Class reflects the ISO Serif Class, Modern
Subclass as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Italian**

This style is generally characterized by a medium x-height, with thin
hairline serifs. An example of this font style is the Monotype Bodoni
family. This IBM Subclass reflects the ISO Serif Class, Modern Subclass,
and Italian Specific Group as documented in the 12/87 ISO/IEC 9541-5
draft standard.

**Subclass ID = 2 : Script**

This style is generally characterized by a hand written script
appearance while retaining the Modern Italian style. An example of this
font style is the IBM Narkissim (Hebrew) family. This IBM Subclass is
not specifically reflected in the 12/87 ISO/IEC 9541-5 draft standard,
though the ISO Serif Class, Modern Subclass, and Italian Specific Group
would be a close approximation.

**Subclass ID = 3-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 4 Clarendon Serifs

### Specification

This style is a variation of the Oldstyle Serifs and the Transitional
Serifs, with a mild vertical stroke contrast and bracketed serifs. This
IBM Class reflects the ISO Serif Class, Square Serif Subclass as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Clarendon**

This style is generally characterized by a large x-height, with serifs
and strokes of equal weight. An example of this font style is the Allied
Linotype Clarendon family. This IBM Subclass reflects the ISO Serif
Class, Square Serif Subclass, and Clarendon Specific Group as documented
in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 2 : Modern**

This style is generally characterized by a large x-height, with serifs
of a lighter weight than the strokes and the strokes of a lighter weight
than the Traditional. An example of this font style is the Monotype
Century Schoolbook family. This IBM Subclass reflects the ISO Serif
Class, Square Serif Subclass, and Clarendon Specific Group as documented
in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 3 : Traditional**

This style is generally characterized by a large x-height, with serifs
of a lighter weight than the strokes. An example of this font style is
the Monotype Century family.This IBM Subclass reflects the ISO Serif
Class, Square Serif Subclass, and Clarendon Specific Group as documented
in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 4 : Newspaper**

This style is generally characterized by a large x-height, with a
simpler style of design and serifs of a lighter weight than the strokes.
An example of this font style is the Allied Linotype Excelsior Family.
This IBM Subclass reflects the ISO Serif Class, Square Serif Subclass,
and Clarendon Specific Group as documented in the 12/87 ISO/IEC 9541-5
draft standard.

**Subclass ID = 5 : Stub Serif**

This style is generally characterized by a large x-height, with short
stub serifs and relatively bold stems. An example of this font style is
the Cheltenham Family. This IBM Subclass reflects the ISO Serif Class,
Square Serif Subclass, and Short Specific Group as documented in the
12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 6 : Monotone**

This style is generally characterized by a large x-height, with monotone
stems. An example of this font style is the ITC Korinna Family. This IBM
Subclass reflects the ISO Serif Class, Square Serif Subclass, and
Monotone Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 7 : Typewriter**

This style is generally characterized by a large x-height, with moderate
stroke thickness characteristic of a typewriter. An example of this font
style is the Prestige Elite Family. This IBM Subclass reflects the ISO
Serif Class, Square Serif Subclass, and Typewriter Specific Group as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 8-14: (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 5 Slab Serifs

### Specification

This style is characterized by serifs with a square transition between
the strokes and the serifs (no brackets). This IBM Class reflects the
ISO Serif Class, Square Serif Subclass (except the Clarendon Specific
Group) as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Monotone**

This style is generally characterized by a large x-height, with serifs
and strokes of equal weight. An example of this font style is the ITC
Lubalin Family. This IBM Subclass reflects the ISO Serif Class, Square
Serif Subclass, and Monotone Specific Group as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 2 : Humanist**

This style is generally characterized by a medium x-height, with serifs
of lighter weight that the strokes. An example of this font style is the
Candida Family. This IBM Subclass reflects the ISO Serif Class, Square
Serif Subclass, and Monotone Specific Group as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 3 : Geometric**

This style is generally characterized by a large x-height, with serifs
and strokes of equal weight and a geometric (circles and lines) design.
An example of this font style is the Monotype Rockwell Family. This IBM
Subclass reflects the ISO Serif Class, Square Serif Subclass, and
Monotone Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 4 : Swiss**

This style is generally characterized by a large x-height, with serifs
and strokes of equal weight and an emphasis on the white space of the
characters. An example of this font style is the Allied Linotype Serifa
Family. This IBM Subclass reflects the ISO Serif Class, Square Serif
Subclass, and Monotone Specific Group as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 5 : Typewriter**

This style is generally characterized by a large x-height, with serifs
and strokes of equal but moderate thickness, and a geometric design. An
example of this font style is the IBM Courier Family. This IBM Subclass
reflects the ISO Serif Class, Square Serif Subclass, and Monotone
Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 6-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 6 (reserved for future use)

### Specification

This class ID is reserved for future assignment, and shall not be used
without formal assignment by IBM.

## Class ID = 7 Freeform Serifs

### Specification

This style includes serifs, but which expresses a design freedom that
does not generally fit within the other serif design classifications.
This IBM Class reflects the remaining ISO Serif Class subclasses as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Modern**

This style is generally characterized by a medium x-height, with light
contrast in the strokes and a round full design. An example of this font
style is the ITC Souvenir Family. This IBM Subclass is not reflected in
the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 2-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 8 Sans Serif

### Specification

This style includes most basic letter forms (excluding Scripts and
Ornamentals) that do not have serifs on the strokes. This IBM Class
reflects the ISO Sans Serif Class as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : IBM Neo-grotesque Gothic**

This style is generally characterized by a large x-height, with uniform
stroke width and a simple one story design distinguished by a medium
resolution, hand tuned, bitmap rendition of the more general
Neo-grotesque Gothic Subclass. An example of this font style is the IBM
Sonoran Sans Serif family. This IBM Subclass reflects the ISO Sans Serif
Class, Gothic Subclass, and Neo-grotesque Specific Group as documented
in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 2 : Humanist**

This style is generally characterized by a medium x-height, with light
contrast in the strokes and a classic Roman letterform. An example of
this font style is the Allied Linotype Optima family. This IBM Subclass
reflects the ISO Sans Serif Class, Humanist Subclass as documented in
the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 3 : Low-x Round Geometric**

This style is generally characterized by a low x-height, with monotone
stroke weight and a round geometric design. An example of this font
style is the Fundicion Tipograficia Neufville Futura family. This IBM
Subclass reflects the ISO Sans Serif Class, Geometric Subclass, Round
Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 4 : High-x Round Geometric**

This style is generally characterized by a high x-height, with uniform
stroke weight and a round geometric design. An example of this font
style is the ITC Avant Garde Gothic family. This IBM Subclass reflects
the ISO Sans Serif Class, Geometric Subclass, Round Specific Group as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 5 : Neo-grotesque Gothic**

This style is generally characterized by a high x-height, with uniform
stroke width and a simple one story design. An example of this font
style is the Allied Linotype Helvetica family. This IBM Subclass
reflects the ISO Sans Serif Class, Gothic Subclass, Neo-grotesque
Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 6 : Modified Neo-grotesque Gothic**

This style is similar to the Neo-grotesque Gothic style, with design
variations to the G and Q. An example of this font style is the Allied
Linotype Univers family. This IBM Subclass reflects the ISO Sans Serif
Class, Gothic Subclass, Neo-grotesque Specific Group as documented in
the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 7-8 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 9 : Typewriter Gothic**

This style is similar to the Neo-grotesque Gothic style, with moderate
stroke thickness characteristic of a typewriter. An example of this font
style is the IBM Letter Gothic family. This IBM Subclass reflects the
ISO Sans Serif Class, Gothic Subclass, Typewriter Specific Group as
documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 10 : Matrix**

This style is generally a simple design characteristic of a dot matrix
printer. An example of this font style is the IBM Matrix Gothic family.
This IBM Subclass is not reflected in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 11-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 9 Ornamentals

### Specification

This style includes highly decorated or stylized character shapes that
are typically used in headlines. This IBM Class reflects the ISO
Ornamental Class and the ISO Blackletter Class as documented in the
12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Engraver**

This style is characterized by fine lines or lines engraved on the
stems. An example of this font style is the Copperplate family. This IBM
Subclass reflects the ISO Ornamental Class and Inline Subclass, or the
Serif Class and Engraving Subclass as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 2 : Black Letter**

This style is generally based upon the printing style of the German
monasteries and printers of the 12th to 15th centuries. An example of
this font style is the Old English family. This IBM Subclass reflects
the ISO Blackletters Class as documented in the 12/87 ISO/IEC 9541-5
draft standard.

**Subclass ID = 3 : Decorative**

This style is characterized by ornamental designs (typically from
nature, such as leaves, flowers, animals, etc.) incorporated into the
stems and strokes of the characters. An example of this font style is
the Saphire family. This IBM Subclass reflects the ISO Ornamental Class
and Decorative Subclass as documented in the 12/87 ISO/IEC 9541-5 draft
standard.

**Subclass ID = 4 : Three Dimensional**

This style is characterized by a three dimensional (raised) appearance
of the characters created by shading or geometric effects. An example of
this font style is the Thorne Shaded family. This IBM Subclass reflects
the ISO Ornamental Class and Three Dimensional Subclass as documented in
the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 5-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 10 Scripts

### Specification

This style includes those typefaces that are designed to simulate
handwriting. This IBM Class reflects the ISO Script Class and Uncial
Class as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1 : Uncial**

This style is characterized by unjoined (nonconnecting) characters that
are generally based on the hand writing style of Europe in the 6th to
9th centuries. An example of this font style is the Libra family. This
IBM Subclass reflects the ISO Uncial Class as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 2 : Brush Joined**

This style is characterized by joined (connecting) characters that have
the appearance of being painted with a brush, with moderate contrast
between thick and thin strokes. An example of this font style is the
Mistral family. This IBM Subclass reflects the ISO Script Class, Joined
Subclass, and Informal Specific Group as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 3 : Formal Joined**

This style is characterized by joined (connecting) characters that have
a printed (or drawn with a stiff brush) appearance with extreme contrast
between the thick and thin strokes. An example of this font style is the
Coronet family. This IBM Subclass reflects the ISO Script Class, Joined
Subclass, and Formal Specific Group as documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 4 : Monotone Joined**

This style is characterized by joined (connecting) characters that have
a uniform appearance with little or no contrast in the strokes. An
example of this font style is the Kaufmann family. This IBM Subclass
reflects the ISO Script Class, Joined Subclass, and Monotone Specific
Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 5 : Calligraphic**

This style is characterized by beautifully hand drawn, unjoined
(non-connecting) characters that have an appearance of being drawn with
a broad edge pen. An example of this font style is the Thompson
Quillscript family. This IBM Subclass reflects the ISO Script Class,
Unjoined Subclass, and Calligraphic Specific Group as documented in the
12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 6 : Brush Unjoined**

This style is characterized by unjoined (non-connecting) characters that
have the appearance of being painted with a brush, with moderate
contrast between thick and thin strokes. An example of this font style
is the Saltino family. This IBM Subclass reflects the ISO Script Class,
Unjoined Subclass, and Brush Specific Group as documented in the 12/87
ISO/IEC 9541-5 draft standard.

**Subclass ID = 7 : Formal Unjoined**

This style is characterized by unjoined (non-connecting) characters that
have a printed (or drawn with a stiff brush) appearance with extreme
contrast between the thick and thin strokes. An example of this font
style is the Virtuosa family. This IBM Subclass reflects the ISO Script
Class, Unjoined Subclass, and Formal Specific Group as documented in the
12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 8 : Monotone Unjoined**

This style is characterized by unjoined (non-connecting) characters that
have a uniform appearance with little or no contrast in the strokes. An
example of this font style is the Gilles Gothic family. This IBM
Subclass reflects the ISO Script Class, Unjoined Subclass, and Monotone
Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 9-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 : Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 11 (reserved for future use)

### Specification

This class ID is reserved for future assignment, and shall not be used
without formal assignment by IBM.

## Class ID = 12 Symbolic

### Specification

This style is generally design independent, making it suitable for Pi
and special characters (icons, dingbats, technical symbols, etc.) that
may be used equally well with any font. This IBM Class reflects various
ISO Specific Groups, as noted below and documented in the 12/87 ISO/IEC
9541-5 draft standard.

**Subclass ID = 0 : No Classification**

This subclass ID is used to indicate that the associated font has no
design sub-classification or that the design sub-classification is not
of significance to the creator or user of the font resource.

**Subclass ID = 1-2 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 3 : Mixed Serif**

This style is characterized by either both or a combination of serif and
sans serif designs on those characters of the font for which design is
important (e.g., superscript and subscript characters, numbers,
copyright or trademark symbols, etc.). An example of this font style is
found in the IBM Symbol family. This IBM Subclass is not reflected in
the 12/87 ISO/IEC 9541-5 draft standard.

**Subclass ID = 4-5 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 6 : Oldstyle Serif**

This style is characterized by a Oldstyle Serif IBM Class design on
those characters of the font for which design is important (e.g.,
superscript and subscript characters, numbers, copyright or trademark
symbols, etc.). An example of this font style is found in the IBM
Sonoran Pi Serif family. This IBM Subclass is not directly reflected in
the 12/87 ISO/IEC 9541-5 draft standard, though it is indirectly by the
ISO Serif Class and Legibility Subclass (implies that all characters of
the font exhibit the design appearance, while only a subset of the
characters actually exhibit the design).

**Subclass ID = 7 : Neo-grotesque Sans Serif**

This style is characterized by a Neo-grotesque Sans Serif IBM Font Class
and Subclass design on those characters of the font for which design is
important (e.g., superscript and subscript characters, numbers,
copyright or trademark symbols, etc.). An example of this font style is
found in the IBM Sonoran Pi Sans Serif family. This IBM Subclass is not
directly reflected in the 12/87 ISO/IEC 9541-5 draft standard, though it
is indirectly by the ISO Sans Serif Class and Gothic Subclass (implies
that all characters of the font exhibit the design appearance, while
only a subset of the characters actually exhibit the design).

**Subclass ID = 8-14 : (reserved for future use)**

These subclass IDs are reserved for future assignment, and shall not be
used without formal assignment by IBM.

**Subclass ID = 15 :Miscellaneous**

This subclass ID is used for miscellaneous designs of the associated
design class that are not covered by another Subclass.

## Class ID = 13 Reserved

### Specification

This class ID is reserved for future assignment, and shall not be used
without formal assignment by IBM.

## Class ID = 14 Reserved

### Specification

This class ID is reserved for future assignment, and shall not be used
without formal assignment by IBM.

