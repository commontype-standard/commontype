# fpgm - Font Program

## Introduction

### Specification

This table is similar to the CVT Program, except that it is only run
once, when the font is first used. It is used only for FDEFs and IDEFs.
Thus the CVT Program need not contain function definitions. However, the
CVT Program may redefine existing FDEFs or IDEFs.

This table is optional.

| Type       | Name | Description                                                                    |
| ---------- | ---- | ------------------------------------------------------------------------------ |
| BYTE \[n\] |      | Instructions. n is the number of BYTE items that fit in the size of the table. |

