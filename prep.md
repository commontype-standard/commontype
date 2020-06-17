# prep - Control Value Program

## Introduction

### Specification

The Control Value Program consists of a set of TrueType instructions
that will be executed whenever the font or point size or transformation
matrix change and before each glyph is interpreted. Any instruction is
legal in the CVT Program but since no glyph is associated with it,
instructions intended to move points within a particular glyph outline
cannot be used in the CVT Program. The name [prep](#chapter.prep) is
anachronistic.

| Type       | Name | Description                                                                                                                                         |
| ---------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| BYTE \[n\] |      | Set of instructions executed whenever point size or font or transformation change. n is the number of BYTE items that fit in the size of the table. |

