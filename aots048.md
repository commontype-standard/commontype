# Misc

## Code to sort out

## Test Font Fragments

1.  A neutral character has no inherent directionality; it is not a
    character with zero (0) width. Spaces and punctuation are examples
    of neutral characters. Non-neutral characters are those with
    inherent directionality. For example, Roman letters (left-to-right)
    and Arabic letters(right-to-left) have directionality. In a "normal"
    Roman font where spaces and punctuation are present, the font
    direction hints should be set to two (2).

2.  This includes Font and CVT Programs, as well as the instructions for
    each glyph.

3.  737 is default, but 869 (IBM Greek) will be available at setup time
    through the selection of a bogus Greek locale in Custom Setup.

4.  Setting bit 57 implies that there is at least one codepoint beyond
    the Basic Multilingual Plane that is supported by this font.

5.  Setting bit 57 implies that there is at least one codepoint beyond
    the Basic Multilingual Plane that is supported by this font.

6.  This glyph name is also used for another Unicode value listed in
    this document. If a separate design for this glyph is desired, it
    may be given a uni\<CODE\> glyph name, where \<CODE\> is a 4-digit
    uppercase hexadecimal number that indicates the Unicode value.
    
    For example, if different designs are desired for MICRO SIGN
    (U+00B5) and GREEK SMALL LETTER MU (U+03BC), then glyph "mu" should
    be designed as MICRO SIGN and glyph "uni03BC" should be designed as
    GREEK SMALL LETTER MU.
    
    Refer to the Adobe document 'Unicode and Glyph Names' for more
    details.

7.  This is an optional glyph
