<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VDMX"></a>Chapter 36. Vertical Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm80791854144"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.36.1.1"></a>Specification</h3></div></div></div><p role="">The VDMX table relates to OpenType fonts with TrueType
        outlines. Under Windows, the usWinAscent and usWinDescent
        values from the <a role="" class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table will be used to
        determine the maximum black height for a font at any given
        size. Windows calls this distance the Font Height. Because
        TrueType instructions can lead to Font Heights that differ
        from the actual scaled and rounded values, basing the Font
        Height strictly on the yMax and yMin can result in "lost
        pixels."  Windows will clip any pixels that extend above the
        yMax or below the yMin. In order to avoid grid fitting the
        entire font to determine the correct height, the VDMX table
        has been defined.</p><p role="">The VDMX table consists of a header followed by
          groupings of VDMX records:</p><div class="table"><a name="idm80791850176"></a><p class="title"><strong>Table 36.1. VDMX Header</strong></p><div class="table-contents"><table role="" class="table" summary="VDMX Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">Version number (0 or 1).</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numRecs</td><td role="">Number of VDMX groups present</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numRatios</td><td role="">Number of aspect ratio
              groupings</td><td class="auto-generated"> </td></tr><tr><td role="">Ratio</td><td role="">ratRange [numRatios]</td><td role="">Ratio ranges (see below for more
              info)</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">offset [numRatios]</td><td role="">Offset from start of this table to the VDMX
              group for this ratio range.</td><td class="auto-generated"> </td></tr><tr><td role="">Vdmx</td><td role="">groups</td><td role="">The actual VDMX groupings (documented below)
                </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80792896256"></a><p class="title"><strong>Table 36.2. Ratio Record</strong></p><div class="table-contents"><table role="" class="table" summary="Ratio Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">BYTE</td><td role="">bCharSet</td><td role="">Character set (see below)</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">xRatio</td><td role="">Value to use for x-Ratio</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">yStartRatio</td><td role="">Starting y-Ratio value</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">yEndRatio</td><td role="">Ending y-ratio value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Ratios are set up as follows:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><tbody><tr><td role="">For a 1:1 aspect ratio</td><td role="">Ratios.xRatio = 1; Ratios.yStartRatio = 1;
                  Ratios.yEndRatio = 1;</td></tr><tr><td role="">For 1:1 through 2:1 ratio</td><td role="">Ratios.xRatio = 2; Ratios.yStartRatio = 1;
                  Ratios.yEndRatio = 2;</td></tr><tr><td role="">For 1.33:1 ratio</td><td role="">Ratios.xRatio = 4; Ratios.yStartRatio = 3;
                  Ratios.yEndRatio = 3;</td></tr><tr><td role="">For all aspect ratios</td><td role="">Ratio.xRatio = 0; Ratio.yStartRatio = 0;
                  Ratio.yEndRatio = 0;</td></tr></tbody></table></div><p role="">All values set to zero signal the default grouping to
          use; if present, this must be the last Ratio group in the
          table. Ratios of 2:2 are the same as 1:1.</p><p role="">Aspect ratios are matched against the target device by
          normalizing the entire ratio range record based on the
          current X resolution and performing a range check of Y
          resolutions for each record after normalization. Once a
          match is found, the search stops. If the 0,0,0 group is
          encountered during the search, it is used (therefore if this
          group is not at the end of the ratio groupings, no group
          that follows it will be used). If there is not a match and
          there is no 0,0,0 record, then there is no VDMX data for
          that aspect ratio.</p><p role="">Note that range checks are conceptually performed as
        follows:</p><p role="">(deviceXRatio == Ratio.xRatio) &amp;&amp; (deviceYRatio
          &gt;= Ratio.yStartRatio) &amp;&amp; (deviceYRatio &lt;=
          Ratio.yEndRatio)</p><p role="">Each ratio grouping refers to a specific VDMX record
          group; there must be at least 1 VDMX group in the
          table.</p><p role="">The bCharSet value is used to denote cases where the
          VDMX group was computed based on a subset of the glyphs
          present in the font file. The semantics of bCharSet is
	  different based on the version of the VDMX table. It is
	  recommended that VDMX version 1 be used. The currently
	  defined values for character set are:</p><div class="table"><a name="idm80792876336"></a><p class="title"><strong>Table 36.3. Character Set Values ’ Version 0</strong></p><div class="table-contents"><table role="" class="table" summary="Character Set Values ’ Version 0" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">No subset; the VDMX group applies to all glyphs
                  in the font. This is used for symbol or dingbat
                  fonts.</td></tr><tr><td role="">1</td><td role="">Windows ANSI subset; the VDMX group was
                  computed using only the glyphs required to complete
                  the Windows ANSI character set. Windows will ignore
                  any VDMX entries that are not for the ANSI subset
                  (i.e. ANSI_CHARSET)</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80792869232"></a><p class="title"><strong>Table 36.4. Character Set Values ’ Version 1</strong></p><div class="table-contents"><table role="" class="table" summary="Character Set Values ’ Version 1" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">No subset; the VDMX group applies to all glyphs
                  in the font. If adding new character sets to
		  existing font, add this flag and the groups necessary
		  to support it. This should only be used in conjunction
		  with ANSI_CHARSET.</td></tr><tr><td role="">1</td><td role="">No subset; the VDMX group applies to all glyphs
                in the font. Used when creating a new font for
                Windows. No need to support SYMBOL_CHARSET.</td></tr></tbody></table></div></div><br class="table-break"/><p role="">VDMX groups immediately follow the table header. Each
          set of records (there need only be one set) has the
          following layout:</p><div class="table"><a name="idm80792861600"></a><p class="title"><strong>Table 36.5. VDMX Group</strong></p><div class="table-contents"><table role="" class="table" summary="VDMX Group" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">recs</td><td role="">Number of height records in this
              group</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">startsz</td><td role="">Starting yPelHeight</td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">endsz</td><td role="">Ending yPelHeight</td><td class="auto-generated"> </td></tr><tr><td role="">vTable</td><td role="">entry [recs]</td><td role="">The VDMX records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm80792853360"></a><p class="title"><strong>Table 36.6. vTable Record</strong></p><div class="table-contents"><table role="" class="table" summary="vTable Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">yPelHeight</td><td role="">yPelHeight to which values apply</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMax</td><td role="">Maximum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMin</td><td role="">Minimum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">This table must appear in sorted order (sorted by
          yPelHeight), but need not be continous. It should have an
          entry for every pel height where the yMax and yMin do not
          scale linearly, where linearly scaled heights are defined
          as:</p><p role="">Hinted yMax and yMin are identical to scaled/rounded
          yMax and yMin</p><p role="">It is assumed that once yPelHeight reaches 255, all
          heights will be linear, or at least close enough to linear
          that it no longer matters. Please note that while the Ratios
          structure can only support ppem sizes up to 255, the vTable
          structure can support much larger pel heights (up to 65535).
          The choice of SHORT and USHORT for vTable is dictated by the
          requirement that yMax and yMin be signed values (and 127 to
          -128 is too small a range) and the desire to word-align the
          vTable elements.</p></div></div></div>