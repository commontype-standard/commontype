<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.EBSC"></a>Chapter 30. EBSC - Embedded Bitmap Scaling Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm18360"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.31.1.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.EBSC.html" title="Chapter 30. EBSC - Embedded Bitmap Scaling Table">EBSC</a> table provides a mechanism for describing
          embedded bitmaps which are created by scaling other embedded
          bitmaps. While this is the sort of thing that outline font
          technologies were invented to avoid, there are cases (small
          sizes of Kanji, for example) where scaling a bitmap produces
          a more legible font than scan-converting an outline. For
          this reason the <a class="link" href="chapter.EBSC.html" title="Chapter 30. EBSC - Embedded Bitmap Scaling Table">EBSC</a> table allows a font to define a
          bitmap strike as a scaled version of another strike.</p><p>The <a class="link" href="chapter.EBSC.html" title="Chapter 30. EBSC - Embedded Bitmap Scaling Table">EBSC</a> table begins with a header containing the
          table version and number of strikes.</p><div class="table"><a name="idm18369"></a><p class="title"><strong>Table 30.1. ebscHeader</strong></p><div class="table-contents"><table class="table" summary="ebscHeader" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>FIXED</td><td>version</td><td>initially defined as 0x00020000</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>numSizes</td><td> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The ebscHeader is followed immediately by the
          bitmapScaleTable array. The numSizes in the ebscHeader
          indicates the number of bitmapScaleTables in the array. Each
          strike is defined by one bitmapScaleTable.</p><div class="table"><a name="idm18387"></a><p class="title"><strong>Table 30.2. bitmapScaleTable</strong></p><div class="table-contents"><table class="table" summary="bitmapScaleTable" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>sbitLineMetrics</td><td>hori</td><td>line metrics</td><td class="auto-generated"> </td></tr><tr><td>sbitLineMetrics</td><td>vert</td><td>line metrics</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>ppemX</td><td>target horizontal pixels per Em</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>ppemY</td><td>target vertical pixels per Em</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>substitutePpemX</td><td>use bitmaps of this size</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>substitutePpemY</td><td>use bitmaps of this size</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The line metrics have the same meaning as those in the
          bitmapSizeTable, and refer to font wide metrics after
          scaling. The ppemX and ppemY values describe the size of the
          font after scaling. The substitutePpemX and substitutePpemY
          values describe the size of a strike that exists as an sbit
          in the <a class="link" href="chapter.EBLC.html" title="Chapter 29. EBLC - Embedded Bitmap Location Table">EBLC</a> and 'EBDT', and that will be scaled up or down
          to generate the new strike.</p><p>Notice that scaling in the x direction is independent of
          scaling in the y direction, and their scaling values may
          differ. A square aspect-ratio strike could be scaled to a
          non-square aspect ratio. Glyph metrics are scaled by the
          same factor as the pixels per Em (in the appropriate
          direction), and are rounded to the nearest integer
          pixel.</p></div></div></div>