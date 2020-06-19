<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.CommonType_tables"></a>Chapter 3. CommonType Tables</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm567"></a>CommonType Tables</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.4.1.1"></a>Specification</h4></div></div></div><p>Whether TrueType or PostScript outlines are used in an
        CommonType font, the following tables are required for the font
        to function correctly:</p><div class="table"><a name="idm572"></a><p class="title"><strong>Table 3.1. Required Tables</strong></p><div class="table-contents"><table class="table" summary="Required Tables" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
              </td><td>Character to glyph mapping</td></tr><tr><td>
                <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a>
              </td><td>Font header</td></tr><tr><td>
                <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a>
              </td><td>Horizontal header</td></tr><tr><td>
                <a class="link" href="chapter.hmtx.html" title="Chapter 7. hmtx - Horizontal Metrics">hmtx</a>
              </td><td>Horizontal metrics</td></tr><tr><td>
                <a class="link" href="chapter.maxp.html" title="Chapter 8. maxp - Maximum Profile">maxp</a>
              </td><td>Maximum profile</td></tr><tr><td>
                <a class="link" href="chapter.name.html" title="Chapter 9. name - Naming Table">name</a>
              </td><td>Naming table</td></tr><tr><td>
                <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a>
              </td><td>OS/2 and Windows specific metrics</td></tr><tr><td>
                <a class="link" href="chapter.post.html" title="Chapter 12. post - PostScript">post</a>
              </td><td>PostScript information</td></tr></tbody></table></div></div><br class="table-break"/><p>For CommonType fonts based on TrueType outlines, the
        following tables are used:</p><div class="table"><a name="idm613"></a><p class="title"><strong>Table 3.2. Tables Related to TrueType Outlines</strong></p><div class="table-contents"><table class="table" summary="Tables Related to TrueType Outlines" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.cvt.html" title="Chapter 13. cvt - Control Value Table">cvt</a>
              </td><td>Control Value Table</td></tr><tr><td>
                <a class="link" href="chapter.fpgm.html" title="Chapter 14. fpgm - Font Program">fpgm</a>
              </td><td>Font program</td></tr><tr><td>
                <a class="link" href="chapter.glyf.html" title="Chapter 15. glyf - Glyf Data">glyf</a>
              </td><td>Glyph data</td></tr><tr><td>
                <a class="link" href="chapter.loca.html" title="Chapter 16. loca - Index to Location">loca</a>
              </td><td>Index to location</td></tr><tr><td>
                <a class="link" href="chapter.prep.html" title="Chapter 17. prep - Control Value Program">prep</a>
              </td><td>CVT Program</td></tr></tbody></table></div></div><br class="table-break"/><p>The PostScript font extensions define a new set of
        tables containing data specific to PostScript fonts that are
        used instead of the tables listed above.</p><div class="table"><a name="idm642"></a><p class="title"><strong>Table 3.3. Tables Related to PostScript Outlines</strong></p><div class="table-contents"><table class="table" summary="Tables Related to PostScript Outlines" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.CFF.html" title="Chapter 18. CFF - PostScript font program (Compact Font Format) table">CFF</a>
              </td><td>PostScript font program (compact font format)</td></tr><tr><td>
                <a class="link" href="chapter.VORG.html" title="Chapter 38. VORG - Vertical Origin Table">VORG</a>
              </td><td>Vertical Origin</td></tr></tbody></table></div></div><br class="table-break"/><p>Multiple Master support in CommonType, has been
          discontinued as of version 1.3 of the specification. The
          'fvar', 'MMSD', 'MMFX' tables have hence been
          removed.</p><p>There are also several optional tables that support
        vertical layout as well as other advanced typographic
        functions:</p><div class="table"><a name="idm660"></a><p class="title"><strong>Table 3.4. Advanced Typographic Tables</strong></p><div class="table-contents"><table class="table" summary="Advanced Typographic Tables" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.BASE.html" title="Chapter 21. BASE - Baseline Table">BASE</a>
              </td><td>Baseline data</td></tr><tr><td>
                <a class="link" href="chapter.GDEF.html" title="Chapter 22. GDEF - The Glyph Definition Table">GDEF</a>
              </td><td> Glyph definition data</td></tr><tr><td>
                <a class="link" href="chapter.GPOS.html" title="Chapter 23. GPOS - The Glyph Positioning Table">GPOS</a>
              </td><td> Glyph positioning data</td></tr><tr><td>
                <a class="link" href="chapter.GSUB.html" title="Chapter 24. GSUB - The Glyph Substitution Table">GSUB</a>
              </td><td> Glyph substitution data</td></tr><tr><td>
                <a class="link" href="chapter.JSTF.html" title="Chapter 25. JSTF - The Justification Table">JSTF</a>
              </td><td> Justification data</td></tr></tbody></table></div></div><br class="table-break"/><p>For information on common table formats, please see
          <a class="link" href="">CommonType Layout Common Table
            Formats</a>.</p><p>CommonType fonts may also contain bitmaps of glyphs, in
          addition to outlines. Hand-tuned bitmaps are especially
          useful in CommonType fonts for representing complex glyphs at
          very small sizes. If a bitmap for a particular size is
          provided in a font, it will be used by the system instead of
          the outline when rendering the glyph. (Note: ATM does not
          currently support hinted bitmaps in CommonType fonts.)</p><div class="table"><a name="idm691"></a><p class="title"><strong>Table 3.5. Tables Related to Bitmap Glyphs</strong></p><div class="table-contents"><table class="table" summary="Tables Related to Bitmap Glyphs" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.EBDT.html" title="Chapter 26. EBDT - Embedded Bitmap Data Table">EBDT</a>
              </td><td>Embedded bitmap data</td></tr><tr><td>
                <a class="link" href="chapter.EBLC.html" title="Chapter 27. EBLC - Embedded Bitmap Location Table">EBLC</a>
              </td><td>Embedded bitmap location data</td></tr><tr><td>
                <a class="link" href="chapter.EBSC.html" title="Chapter 28. EBSC - Embedded Bitmap Scaling Table">EBSC</a>
              </td><td>Embedded bitmap scaling data</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm711"></a><p class="title"><strong>Table 3.6. Other CommonType Tables</strong></p><div class="table-contents"><table class="table" summary="Other CommonType Tables" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Tag</th><th>Name</th></tr></thead><tbody><tr><td>
                <a class="link" href="chapter.DSIG.html" title="Chapter 29. DSIG - Digital Signature Table">DSIG</a>
              </td><td>Digital signature</td></tr><tr><td>
                <a class="link" href="chapter.gasp.html" title="Chapter 30. gasp - Grid-fitting And Scan-conversion Procedure">gasp</a>
              </td><td>Grid-fitting/Scan-conversion</td></tr><tr><td>
                <a class="link" href="chapter.hdmx.html" title="Chapter 31. hdmx - Horizontal Device Metrics">hdmx</a>
              </td><td>Horizontal device metrics</td></tr><tr><td>
                <a class="link" href="chapter.kern.html" title="Chapter 32. kern - Kerning">kern</a>
              </td><td>Kerning</td></tr><tr><td>
                <a class="link" href="chapter.LTSH.html" title="Chapter 33. LTSH - Linear Threshold">LTSH</a>
              </td><td>Linear threshold data</td></tr><tr><td>
                <a class="link" href="chapter.PCLT.html" title="Chapter 34. PCLT - PCL 5 Table">PCLT</a>
              </td><td>PCL 5 data</td></tr><tr><td>
                <a class="link" href="chapter.VDMX.html" title="Chapter 35. Vertical Device Metrics">VDMX</a>
              </td><td>Vertical device metrics</td></tr><tr><td>
                <a class="link" href="chapter.vhea.html" title="Chapter 36. vhea - Vertical Header Table">vhea</a>
              </td><td>Vertical Metrics header</td></tr><tr><td>
                <a class="link" href="chapter.vmtx.html" title="Chapter 37. vmtx - Vertical Metrics Table">vmtx</a>
              </td><td>Vertical Metrics</td></tr></tbody></table></div></div><br class="table-break"/></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.4.1.2"></a>Annotation</h4></div></div></div><p>The sentence that introduces the tables related to
        PostScript outlines should probably be better phrased: "For
        CommonType fonts based on PostScript outlines, the following
        tables are used:" It parallels the sentence for TT outlines.</p><p>The sentence that points to the "CommonType Layout Common
        Table Formats" should probably be moved to the paragraph that
        introduces the Advanced Typographic Tables. Currently, it is
        between the paragraph that introduces bitmap related tables
        and the list of those tables.</p></div></div></div>