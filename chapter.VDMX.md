<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VDMX"></a>Chapter 37. Vertical Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm20064"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.38.1.1"></a>Specification</h4></div></div></div><p>The VDMX table relates to CommonType fonts with TrueType
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VDMX"></a>Chapter 37. Vertical Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189291191760"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.38.1.1"></a>Specification</h4></div></div></div><p>The VDMX table relates to CommonType fonts with TrueType
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VDMX"></a>Chapter 37. Vertical Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62723035184"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.38.1.1"></a>Specification</h4></div></div></div><p>The VDMX table relates to CommonType fonts with TrueType
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.VDMX"></a>Chapter 37. Vertical Device Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465829561744"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.38.1.1"></a>Specification</h4></div></div></div><p>The VDMX table relates to CommonType fonts with TrueType
>>>>>>> Rebuild
        outlines. Under Windows, the usWinAscent and usWinDescent
        values from the <a class="link" href="chapter.OS2.html" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table will be used to
        determine the maximum black height for a font at any given
        size. Windows calls this distance the Font Height. Because
        TrueType instructions can lead to Font Heights that differ
        from the actual scaled and rounded values, basing the Font
        Height strictly on the yMax and yMin can result in "lost
        pixels."  Windows will clip any pixels that extend above the
        yMax or below the yMin. In order to avoid grid fitting the
        entire font to determine the correct height, the VDMX table
        has been defined.</p><p>The VDMX table consists of a header followed by
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          groupings of VDMX records:</p><div class="table"><a name="idm20071"></a><p class="title"><strong>Table 37.1. VDMX Header</strong></p><div class="table-contents"><table class="table" summary="VDMX Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Version number (0 or 1).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRecs</td><td>Number of VDMX groups present</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRatios</td><td>Number of aspect ratio
              groupings</td><td class="auto-generated"> </td></tr><tr><td>Ratio</td><td>ratRange [numRatios]</td><td>Ratio ranges (see below for more
              info)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset [numRatios]</td><td>Offset from start of this table to the VDMX
              group for this ratio range.</td><td class="auto-generated"> </td></tr><tr><td>Vdmx</td><td>groups</td><td>The actual VDMX groupings (documented below)
                </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm20104"></a><p class="title"><strong>Table 37.2. Ratio Record</strong></p><div class="table-contents"><table class="table" summary="Ratio Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>BYTE</td><td>bCharSet</td><td>Character set (see below)</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>xRatio</td><td>Value to use for x-Ratio</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yStartRatio</td><td>Starting y-Ratio value</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yEndRatio</td><td>Ending y-ratio value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Ratios are set up as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><tbody><tr><td>For a 1:1 aspect ratio</td><td>Ratios.xRatio = 1; Ratios.yStartRatio = 1;
=======
          groupings of VDMX records:</p><div class="table"><a name="idm189291187792"></a><p class="title"><strong>Table 37.1. VDMX Header</strong></p><div class="table-contents"><table class="table" summary="VDMX Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Version number (0 or 1).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRecs</td><td>Number of VDMX groups present</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRatios</td><td>Number of aspect ratio
              groupings</td><td class="auto-generated"> </td></tr><tr><td>Ratio</td><td>ratRange [numRatios]</td><td>Ratio ranges (see below for more
              info)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset [numRatios]</td><td>Offset from start of this table to the VDMX
              group for this ratio range.</td><td class="auto-generated"> </td></tr><tr><td>Vdmx</td><td>groups</td><td>The actual VDMX groupings (documented below)
                </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm189291176464"></a><p class="title"><strong>Table 37.2. Ratio Record</strong></p><div class="table-contents"><table class="table" summary="Ratio Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>BYTE</td><td>bCharSet</td><td>Character set (see below)</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>xRatio</td><td>Value to use for x-Ratio</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yStartRatio</td><td>Starting y-Ratio value</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yEndRatio</td><td>Ending y-ratio value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Ratios are set up as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><tbody><tr><td>For a 1:1 aspect ratio</td><td>Ratios.xRatio = 1; Ratios.yStartRatio = 1;
>>>>>>> Rebuild
=======
          groupings of VDMX records:</p><div class="table"><a name="idm62723031216"></a><p class="title"><strong>Table 37.1. VDMX Header</strong></p><div class="table-contents"><table class="table" summary="VDMX Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Version number (0 or 1).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRecs</td><td>Number of VDMX groups present</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRatios</td><td>Number of aspect ratio
              groupings</td><td class="auto-generated"> </td></tr><tr><td>Ratio</td><td>ratRange [numRatios]</td><td>Ratio ranges (see below for more
              info)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset [numRatios]</td><td>Offset from start of this table to the VDMX
              group for this ratio range.</td><td class="auto-generated"> </td></tr><tr><td>Vdmx</td><td>groups</td><td>The actual VDMX groupings (documented below)
                </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm62723019888"></a><p class="title"><strong>Table 37.2. Ratio Record</strong></p><div class="table-contents"><table class="table" summary="Ratio Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>BYTE</td><td>bCharSet</td><td>Character set (see below)</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>xRatio</td><td>Value to use for x-Ratio</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yStartRatio</td><td>Starting y-Ratio value</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yEndRatio</td><td>Ending y-ratio value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Ratios are set up as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><tbody><tr><td>For a 1:1 aspect ratio</td><td>Ratios.xRatio = 1; Ratios.yStartRatio = 1;
>>>>>>> Rebuild
=======
          groupings of VDMX records:</p><div class="table"><a name="idm465829557776"></a><p class="title"><strong>Table 37.1. VDMX Header</strong></p><div class="table-contents"><table class="table" summary="VDMX Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>Version number (0 or 1).</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRecs</td><td>Number of VDMX groups present</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numRatios</td><td>Number of aspect ratio
              groupings</td><td class="auto-generated"> </td></tr><tr><td>Ratio</td><td>ratRange [numRatios]</td><td>Ratio ranges (see below for more
              info)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>offset [numRatios]</td><td>Offset from start of this table to the VDMX
              group for this ratio range.</td><td class="auto-generated"> </td></tr><tr><td>Vdmx</td><td>groups</td><td>The actual VDMX groupings (documented below)
                </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm465829546448"></a><p class="title"><strong>Table 37.2. Ratio Record</strong></p><div class="table-contents"><table class="table" summary="Ratio Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>BYTE</td><td>bCharSet</td><td>Character set (see below)</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>xRatio</td><td>Value to use for x-Ratio</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yStartRatio</td><td>Starting y-Ratio value</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>yEndRatio</td><td>Ending y-ratio value</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Ratios are set up as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col/><col/></colgroup><tbody><tr><td>For a 1:1 aspect ratio</td><td>Ratios.xRatio = 1; Ratios.yStartRatio = 1;
>>>>>>> Rebuild
                  Ratios.yEndRatio = 1;</td></tr><tr><td>For 1:1 through 2:1 ratio</td><td>Ratios.xRatio = 2; Ratios.yStartRatio = 1;
                  Ratios.yEndRatio = 2;</td></tr><tr><td>For 1.33:1 ratio</td><td>Ratios.xRatio = 4; Ratios.yStartRatio = 3;
                  Ratios.yEndRatio = 3;</td></tr><tr><td>For all aspect ratios</td><td>Ratio.xRatio = 0; Ratio.yStartRatio = 0;
                  Ratio.yEndRatio = 0;</td></tr></tbody></table></div><p>All values set to zero signal the default grouping to
          use; if present, this must be the last Ratio group in the
          table. Ratios of 2:2 are the same as 1:1.</p><p>Aspect ratios are matched against the target device by
          normalizing the entire ratio range record based on the
          current X resolution and performing a range check of Y
          resolutions for each record after normalization. Once a
          match is found, the search stops. If the 0,0,0 group is
          encountered during the search, it is used (therefore if this
          group is not at the end of the ratio groupings, no group
          that follows it will be used). If there is not a match and
          there is no 0,0,0 record, then there is no VDMX data for
          that aspect ratio.</p><p>Note that range checks are conceptually performed as
        follows:</p><p>(deviceXRatio == Ratio.xRatio) &amp;&amp; (deviceYRatio
          &gt;= Ratio.yStartRatio) &amp;&amp; (deviceYRatio &lt;=
          Ratio.yEndRatio)</p><p>Each ratio grouping refers to a specific VDMX record
          group; there must be at least 1 VDMX group in the
          table.</p><p>The bCharSet value is used to denote cases where the
          VDMX group was computed based on a subset of the glyphs
          present in the font file. The semantics of bCharSet is
	  different based on the version of the VDMX table. It is
	  recommended that VDMX version 1 be used. The currently
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	  defined values for character set are:</p><div class="table"><a name="idm20151"></a><p class="title"><strong>Table 37.3. Character Set Values ’ Version 0</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 0" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
=======
	  defined values for character set are:</p><div class="table"><a name="idm189291157504"></a><p class="title"><strong>Table 37.3. Character Set Values ’ Version 0</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 0" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
=======
	  defined values for character set are:</p><div class="table"><a name="idm62723000928"></a><p class="title"><strong>Table 37.3. Character Set Values ’ Version 0</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 0" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
=======
	  defined values for character set are:</p><div class="table"><a name="idm465834575472"></a><p class="title"><strong>Table 37.3. Character Set Values ’ Version 0</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 0" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
                  in the font. This is used for symbol or dingbat
                  fonts.</td></tr><tr><td>1</td><td>Windows ANSI subset; the VDMX group was
                  computed using only the glyphs required to complete
                  the Windows ANSI character set. Windows will ignore
                  any VDMX entries that are not for the ANSI subset
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
                  (i.e. ANSI_CHARSET)</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm20165"></a><p class="title"><strong>Table 37.4. Character Set Values ’ Version 1</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 1" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
=======
                  (i.e. ANSI_CHARSET)</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm189291151360"></a><p class="title"><strong>Table 37.4. Character Set Values ’ Version 1</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 1" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
=======
                  (i.e. ANSI_CHARSET)</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm62722994784"></a><p class="title"><strong>Table 37.4. Character Set Values ’ Version 1</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 1" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
=======
                  (i.e. ANSI_CHARSET)</td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm465834569328"></a><p class="title"><strong>Table 37.4. Character Set Values ’ Version 1</strong></p><div class="table-contents"><table class="table" summary="Character Set Values ’ Version 1" border="1"><colgroup><col/><col/></colgroup><thead><tr><th>Value</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>No subset; the VDMX group applies to all glyphs
>>>>>>> Rebuild
                  in the font. If adding new character sets to
		  existing font, add this flag and the groups necessary
		  to support it. This should only be used in conjunction
		  with ANSI_CHARSET.</td></tr><tr><td>1</td><td>No subset; the VDMX group applies to all glyphs
                in the font. Used when creating a new font for
                Windows. No need to support SYMBOL_CHARSET.</td></tr></tbody></table></div></div><br class="table-break"/><p>VDMX groups immediately follow the table header. Each
          set of records (there need only be one set) has the
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
          following layout:</p><div class="table"><a name="idm20180"></a><p class="title"><strong>Table 37.5. VDMX Group</strong></p><div class="table-contents"><table class="table" summary="VDMX Group" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>recs</td><td>Number of height records in this
              group</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>startsz</td><td>Starting yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>endsz</td><td>Ending yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>vTable</td><td>entry [recs]</td><td>The VDMX records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm20205"></a><p class="title"><strong>Table 37.6. vTable Record</strong></p><div class="table-contents"><table class="table" summary="vTable Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>yPelHeight</td><td>yPelHeight to which values apply</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMax</td><td>Maximum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMin</td><td>Minimum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This table must appear in sorted order (sorted by
=======
          following layout:</p><div class="table"><a name="idm189291144688"></a><p class="title"><strong>Table 37.5. VDMX Group</strong></p><div class="table-contents"><table class="table" summary="VDMX Group" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>recs</td><td>Number of height records in this
              group</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>startsz</td><td>Starting yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>endsz</td><td>Ending yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>vTable</td><td>entry [recs]</td><td>The VDMX records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm189291136448"></a><p class="title"><strong>Table 37.6. vTable Record</strong></p><div class="table-contents"><table class="table" summary="vTable Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>yPelHeight</td><td>yPelHeight to which values apply</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMax</td><td>Maximum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMin</td><td>Minimum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This table must appear in sorted order (sorted by
>>>>>>> Rebuild
=======
          following layout:</p><div class="table"><a name="idm62722988112"></a><p class="title"><strong>Table 37.5. VDMX Group</strong></p><div class="table-contents"><table class="table" summary="VDMX Group" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>recs</td><td>Number of height records in this
              group</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>startsz</td><td>Starting yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>endsz</td><td>Ending yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>vTable</td><td>entry [recs]</td><td>The VDMX records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm62722979872"></a><p class="title"><strong>Table 37.6. vTable Record</strong></p><div class="table-contents"><table class="table" summary="vTable Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>yPelHeight</td><td>yPelHeight to which values apply</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMax</td><td>Maximum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMin</td><td>Minimum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This table must appear in sorted order (sorted by
>>>>>>> Rebuild
=======
          following layout:</p><div class="table"><a name="idm465834562656"></a><p class="title"><strong>Table 37.5. VDMX Group</strong></p><div class="table-contents"><table class="table" summary="VDMX Group" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>recs</td><td>Number of height records in this
              group</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>startsz</td><td>Starting yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>endsz</td><td>Ending yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>vTable</td><td>entry [recs]</td><td>The VDMX records</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm465834554416"></a><p class="title"><strong>Table 37.6. vTable Record</strong></p><div class="table-contents"><table class="table" summary="vTable Record" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>yPelHeight</td><td>yPelHeight to which values apply</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMax</td><td>Maximum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMin</td><td>Minimum value (in pels) for this yPelHeight</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This table must appear in sorted order (sorted by
>>>>>>> Rebuild
          yPelHeight), but need not be continous. It should have an
          entry for every pel height where the yMax and yMin do not
          scale linearly, where linearly scaled heights are defined
          as:</p><p>Hinted yMax and yMin are identical to scaled/rounded
          yMax and yMin</p><p>It is assumed that once yPelHeight reaches 255, all
          heights will be linear, or at least close enough to linear
          that it no longer matters. Please note that while the Ratios
          structure can only support ppem sizes up to 255, the vTable
          structure can support much larger pel heights (up to 65535).
          The choice of SHORT and USHORT for vTable is dictated by the
          requirement that yMax and yMin be signed values (and 127 to
          -128 is too small a range) and the desire to word-align the
          vTable elements.</p></div></div></div>