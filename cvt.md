# cvt - Control Value Table

## Introduction

### Specification

This table contains a list of values that can be referenced by
instructions. They can be used, among other things, to control
characteristics for different glyphs. The length of the table must be an
integral number of FWORD units.

| Type        | Name | Description                                                                                                       |
| ----------- | ---- | ----------------------------------------------------------------------------------------------------------------- |
| FWORD \[n\] |      | List of n values referenceable by instructions. n is the number of FWORD items that fit in the size of the table. |

