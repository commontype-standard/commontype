# Vertical Device Metrics

## Overview

### Specification

The VDMX table relates to OpenType fonts with TrueType outlines. Under
Windows, the usWinAscent and usWinDescent values from the
[OS/2](#chapter.OS2) table will be used to determine the maximum black
height for a font at any given size. Windows calls this distance the
Font Height. Because TrueType instructions can lead to Font Heights that
differ from the actual scaled and rounded values, basing the Font Height
strictly on the yMax and yMin can result in "lost pixels." Windows will
clip any pixels that extend above the yMax or below the yMin. In order
to avoid grid fitting the entire font to determine the correct height,
the VDMX table has been defined.

The VDMX table consists of a header followed by groupings of VDMX
records:

| Type   | Name                   | Description                                                             |
| ------ | ---------------------- | ----------------------------------------------------------------------- |
| USHORT | version                | Version number (0 or 1).                                                |
| USHORT | numRecs                | Number of VDMX groups present                                           |
| USHORT | numRatios              | Number of aspect ratio groupings                                        |
| Ratio  | ratRange \[numRatios\] | Ratio ranges (see below for more info)                                  |
| USHORT | offset \[numRatios\]   | Offset from start of this table to the VDMX group for this ratio range. |
| Vdmx   | groups                 | The actual VDMX groupings (documented below)                            |

VDMX Header

| Type | Name        | Description               |
| ---- | ----------- | ------------------------- |
| BYTE | bCharSet    | Character set (see below) |
| BYTE | xRatio      | Value to use for x-Ratio  |
| BYTE | yStartRatio | Starting y-Ratio value    |
| BYTE | yEndRatio   | Ending y-ratio value      |

Ratio Record

Ratios are set up as follows:

|                           |                                                                  |
| ------------------------- | ---------------------------------------------------------------- |
| For a 1:1 aspect ratio    | Ratios.xRatio = 1; Ratios.yStartRatio = 1; Ratios.yEndRatio = 1; |
| For 1:1 through 2:1 ratio | Ratios.xRatio = 2; Ratios.yStartRatio = 1; Ratios.yEndRatio = 2; |
| For 1.33:1 ratio          | Ratios.xRatio = 4; Ratios.yStartRatio = 3; Ratios.yEndRatio = 3; |
| For all aspect ratios     | Ratio.xRatio = 0; Ratio.yStartRatio = 0; Ratio.yEndRatio = 0;    |

All values set to zero signal the default grouping to use; if present,
this must be the last Ratio group in the table. Ratios of 2:2 are the
same as 1:1.

Aspect ratios are matched against the target device by normalizing the
entire ratio range record based on the current X resolution and
performing a range check of Y resolutions for each record after
normalization. Once a match is found, the search stops. If the 0,0,0
group is encountered during the search, it is used (therefore if this
group is not at the end of the ratio groupings, no group that follows it
will be used). If there is not a match and there is no 0,0,0 record,
then there is no VDMX data for that aspect ratio.

Note that range checks are conceptually performed as follows:

(deviceXRatio == Ratio.xRatio) && (deviceYRatio \>= Ratio.yStartRatio)
&& (deviceYRatio \<= Ratio.yEndRatio)

Each ratio grouping refers to a specific VDMX record group; there must
be at least 1 VDMX group in the table.

The bCharSet value is used to denote cases where the VDMX group was
computed based on a subset of the glyphs present in the font file. The
semantics of bCharSet is different based on the version of the VDMX
table. It is recommended that VDMX version 1 be used. The currently
defined values for character set are:

| Value | Description                                                                                                                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | No subset; the VDMX group applies to all glyphs in the font. This is used for symbol or dingbat fonts.                                                                                                                 |
| 1     | Windows ANSI subset; the VDMX group was computed using only the glyphs required to complete the Windows ANSI character set. Windows will ignore any VDMX entries that are not for the ANSI subset (i.e. ANSI\_CHARSET) |

Character Set Values ’ Version 0

| Value | Description                                                                                                                                                                                                                   |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0     | No subset; the VDMX group applies to all glyphs in the font. If adding new character sets to existing font, add this flag and the groups necessary to support it. This should only be used in conjunction with ANSI\_CHARSET. |
| 1     | No subset; the VDMX group applies to all glyphs in the font. Used when creating a new font for Windows. No need to support SYMBOL\_CHARSET.                                                                                   |

Character Set Values ’ Version 1

VDMX groups immediately follow the table header. Each set of records
(there need only be one set) has the following layout:

| Type   | Name           | Description                            |
| ------ | -------------- | -------------------------------------- |
| USHORT | recs           | Number of height records in this group |
| BYTE   | startsz        | Starting yPelHeight                    |
| BYTE   | endsz          | Ending yPelHeight                      |
| vTable | entry \[recs\] | The VDMX records                       |

VDMX Group

| Type   | Name       | Description                                 |
| ------ | ---------- | ------------------------------------------- |
| USHORT | yPelHeight | yPelHeight to which values apply            |
| SHORT  | yMax       | Maximum value (in pels) for this yPelHeight |
| SHORT  | yMin       | Minimum value (in pels) for this yPelHeight |

vTable Record

This table must appear in sorted order (sorted by yPelHeight), but need
not be continous. It should have an entry for every pel height where the
yMax and yMin do not scale linearly, where linearly scaled heights are
defined as:

Hinted yMax and yMin are identical to scaled/rounded yMax and yMin

It is assumed that once yPelHeight reaches 255, all heights will be
linear, or at least close enough to linear that it no longer matters.
Please note that while the Ratios structure can only support ppem sizes
up to 255, the vTable structure can support much larger pel heights (up
to 65535). The choice of SHORT and USHORT for vTable is dictated by the
requirement that yMax and yMin be signed values (and 127 to -128 is too
small a range) and the desire to word-align the vTable elements.

