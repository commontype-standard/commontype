# hmtx - Horizontal Metrics

## Introduction

### Specification

The type longHorMetric is defined as an array where each element has two
parts: the advance width, which is of type USHORT, and the left side
bearing, which is of type SHORT. Or, more formally:

    typedef struct  _longHorMetric {
         USHORT advanceWidth;
         SHORT  lsb;
    }  longHorMetric;

| Type                               | Name            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| longHorMetric \[numberOfHMetrics\] | hMetrics        | Paired advance width and left side bearing values for each glyph. The value numOfHMetrics comes from the [hhea](#chapter.hhea) table. If the font is monospaced, only one entry need be in the array, but that entry is required. The last entry applies to all subsequent glyphs.                                                                                                                                                                        |
| FWord \[ \]                        | leftSideBearing | Here the advanceWidth is assumed to be the same as the advanceWidth for the last entry above. The number of entries in this array is derived from numGlyphs (from [maxp](#chapter.maxp) table) minus numberOfHMetrics. This generally is used with a run of monospaced glyphs (e.g., Kanji fonts or Courier fonts). Only one run is allowed and it must be at the end. This allows a monospaced font to vary the left side bearing values for each glyph. |

In CFF OpenType fonts, every glyph's advanceWidth as recorded in the
[hmtx](#chapter.hmtx) table must be identical to its x width in the
[CFF](#chapter.CFF) table.

For any glyph, xmax and xmin are given in [glyf](#chapter.glyf) table,
lsb and aw are given in [hmtx](#chapter.hmtx) table. rsb is calculated
as follows:

    rsb = aw - (lsb + xmax - xmin)

If pp1 and pp2 are phantom points used to control lsb and rsb, their
initial position in x is calculated as follows:

    pp1 = xmin - lsb
    pp2 = pp1 + aw

### XML Representation

In the XML representation, the various entries can occur in any order,
and the long and short metrics can even be interleaved. However, the
entries must have distinct gid attribute values, and collectively cover
exactly the range \[0, n-1\]. In a fully valid font, n must of course be
equal to the maxp.numGlyphs.

    ?? ==
          
    hmtx =
      element hmtx {
        element hMetric {
          attribute gid { text },
          attribute lsb { text },
          attribute adv { text }
        }*,
        element lsb {
          attribute gid { text },
          attribute lsb { text }
        }*
      }

