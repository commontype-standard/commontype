# loca - Index to Location

## Introduction

### Specification

The indexToLoc table stores the offsets to the locations of the glyphs
in the font, relative to the beginning of the glyphData table. In order
to compute the length of the last glyph element, there is an extra entry
after the last valid index.

By definition, index zero points to the "missing character," which is
the character that appears if a character is not found in the font. The
missing character is commonly represented by a blank box (such as ) or a
space. If the font does not contain an outline for the missing
character, then the first and second offsets should have the same value.
This also applies to any other character without an outline, such as the
space character.

Most routines will look at the [maxp](#chapter.maxp) table to determine
the number of glyphs in the font, but the value in the
[loca](#chapter.loca) table should agree.

There are two versions of this table, the short and the long. The
version is specified in the indexToLocFormat entry in the
[head](#chapter.head) table.

**Short version**

| Type   | Name          | Description                                                                                                                                           |
| ------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| USHORT | offsets \[n\] | The actual local offset divided by 2 is stored. The value of n is numGlyphs + 1. The value for numGlyphs is found in the [maxp](#chapter.maxp) table. |

**Long version**

| Type  | Name          | Description                                                                                                                              |
| ----- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| ULONG | offsets \[n\] | The actual local offset is stored. The value of n is numGlyphs + 1. The value for numGlyphs is found in the [maxp](#chapter.maxp) table. |

Note that the local offsets should be long-aligned, i.e., multiples of
4. Offsets which are not long-aligned may seriously degrade performance
of some processors.

### Annotation

We assume that 'indexToLoc' should be replaced by 'loca' and 'glyphData'
should be replaced by 'glyph'.

