<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.hdmx"></a>Chapter 32. hdmx - Horizontal Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80794352208"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.32.1.1"></a>Specification</h3></div></div></div><p role="">The hdmx table relates to OpenType fonts with TrueType
          outlines. The Horizontal Device Metrics table stores integer
          advance widths scaled to particular pixel sizes. This allows
          the font manager to build integer width tables without
          calling the scaler for each glyph. Typically this table
          contains only selected screen sizes. This table is sorted by
          pixel size. The checksum for this table applies to both
          subtables listed.</p><p role="">Note that for non-square pixel grids, the character
          width (in pixels) will be used to determine which device
          record to use. For example, a 12 point character on a device
          with a resolution of 72x96 would be 12 pixels high, and 16 pixels
          wide. The hdmx device record for 16 pixel characters
          would be used.</p><p role="">When the hdmx table is used, bit 2 of the flag field in
	  the <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table must be set to 1 to
	  indicate that instructions may depend on point size.</p><p role="">If bit 4 of the flag field in the
          <a role="" class="link" href="chapter.head.html" title="Chapter 6. head - Font Header">head</a> table is not set, then it is assumed
          that the font scales linearly; in this case an
          <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> table is not necessary and should
          not be built. If bit 4 of the flag field is set, then one or
          more glyphs in the font are assumed to scale nonlinearly. In
          this case, performance can be improved by including the
          <a role="" class="link" href="chapter.hdmx.html" title="Chapter 32. hdmx - Horizontal Device Metrics">hdmx</a> table with one or more important
          DeviceRecord's for important sizes. Please see the chapter
          "Recommendations for Windows Fonts" for more detail.</p><p role="">The table begins as follows:</p><div class="table"><a name="idm80794344384"></a><p class="title"><strong>Table 32.1. hdmx header</strong></p><div class="table-contents"><table role="" class="table" summary="hdmx header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Table version number (0)</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">numRecords</td><td role="">Number of device records.</td><td class="auto-generated"> </td></tr><tr><td role="">LONG</td><td role="">sizeDeviceRecord</td><td role="">Size of a device record, long
              aligned.</td><td class="auto-generated"> </td></tr><tr><td role="">DeviceRecord</td><td role="">records[numRecords]</td><td role="">Array of device records.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each DeviceRecord for format 0 looks like this.</p><div class="table"><a name="idm80794335680"></a><p class="title"><strong>Table 32.2. Device Record</strong></p><div class="table-contents"><table role="" class="table" summary="Device Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">BYTE</td><td role="">pixelSize</td><td role="">Pixel size for following widths (as
                  ppem).</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">maxWidth</td><td role="">Maximum width.</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">widths [numGlyphs]</td><td role="">Array of widths (numGlyphs is from the
	      <a role="" class="link" href="chapter.maxp.html" title="Chapter 9. maxp - Maximum Profile">maxp</a>)</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Each DeviceRecord is padded with 0's to make it long
          word aligned.</p><p role="">Each Width value is the width of the particular glyph,
          in pixels, at the pixels per em (ppem) size listed at the
          start of the DeviceRecord.</p><p role="">The ppem sizes are measured along the y axis.</p></div></div></div>