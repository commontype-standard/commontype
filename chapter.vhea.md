<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vhea"></a>Chapter 37. vhea - Vertical Header Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320128168176"></a>Overview</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.37.1.1"></a>Specification</h3></div></div></div><p role="">The vertical header table (tag name:
        <a role="" class="link" href="chapter.vhea.md" title="Chapter 37. vhea - Vertical Header Table">vhea</a>) contains information needed for
        vertical fonts. The glyphs of vertical fonts are written
        either top to bottom or bottom to top. This table contains
        information that is general to the font as a
        whole. Information that pertains to specific glyphs is given
        in the vertical metrics table (tag name:
        <a role="" class="link" href="chapter.vmtx.md" title="Chapter 38. vmtx - Vertical Metrics Table">vmtx</a>) described separately. The formats of
        these tables are similar to those for horizontal metrics (hhea
        and hmtx).</p><p role="">Data in the vertical header table must be consistent
          with data that appears in the vertical metrics table. The
          advance height and top sidebearing values in the vertical
          metrics table must correspond with the maximum advance
          height and minimum bottom sidebearing values in the vertical
          header table.</p><p role="">See the section "OpenType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
          Korean) fonts.</p><p role="">The difference between version 1.0 and version 1.1 is
	  the name and definition of: </p><div role="" class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li role="" class="listitem"><p role="">ascender becomes vertTypoAscender</p></li><li role="" class="listitem"><p role="">descender becomes vertTypoDescender</p></li><li role="" class="listitem"><p role="">lineGap becomes vertTypoLineGap</p></li></ul></div><p role="">The vertical header table format follows: Vertical
          Header Table</p><div class="table"><a name="idm320128159344"></a><p class="title"><strong>Table 37.1. Version 1.0</strong></p><div class="table-contents"><table role="" class="table" summary="Version 1.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">version</td><td role="">Version number of the vertical header table;
              0x0001000 for version 1.0</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ascent</td><td role="">Distance in FUnits from the centerline to the
	      previous line’ descent.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">descent</td><td role="">Distance in FUnits from the centerline to
	      the next line’s ascent.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">lineGap</td><td role="">Reserved; set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">advanceHeightMax</td><td role="">The maximum advance height measurement
	      — in FUnits — found in the font. This value
	      must be consistent with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">minTop</td><td role="">The minimum top sidebearing measurement found
              in the font, in FUnits. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">minBottom</td><td role="">The minimum bottom sidebearing measurement
              found in the font, in FUnits. This value must be
              consistent with the entries in the vertical metrics
              table. </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMaxExtent</td><td role="">Defined as yMaxExtent=minTopSideBearing +
              (yMax - yMin)</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretSlopeRise</td><td role="">The value of the caretSlopeRise field divided
              by the value of the caretSlopeRun Field determines the
              slope of the caret. A value of 0 for the rise and a
              value of 1 for the run specifies a horizontal caret. A
              value of 1 for the rise and a value of 0 for the run
              specifies a vertical caret. Intermediate values are
              desirable for fonts whose glyphs are oblique or italic.
              For a vertical font, a horizontal caret is
              best.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretSlopeRun</td><td role="">See the caretSlopeRise field. Value=1 for
              nonslanted vertical fonts.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretOffset</td><td role="">The amount by which the highlight on a
              slanted glyph needs to be shifted away from the glyph in
              order to produce the best appearance. Set value equal to
              0 for nonslanted fonts.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">metricDataFormat</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numOfLongVerMetrics</td><td role="">Number of advance heights in the vertical
              metrics table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm320128130176"></a><p class="title"><strong>Table 37.2. Version 1.1</strong></p><div class="table-contents"><table role="" class="table" summary="Version 1.1" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">Fixed</td><td role="">version</td><td role="">Version number of the vertical header table;
              0x00011000 for version 1.1. Note the representation of a
              non-zero fractional part, in Fixed
              numbers.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">vertTypoAscender</td><td role="">The vertical typographic ascender for this
              font. It is the distance in FUnits from the ideographic
              em-box center baseline for the vertical axis to the
              right of the ideographic em-box and is usually set to
              (head.unitsPerEm)/2. For example, a font with an em of
              1000 fUnits will set this field to 500. See the baseline
              section of the OpenType Tag Registry for a description
              of the ideographic em-box. </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">vertTypoDescender</td><td role="">The vertical typographic descender for this
              font. It is the distance in FUnits from the ideographic
              em-box center baseline for the horizontal axis to the
              left of the ideographic em-box and is usually set to
              (head.unitsPerEm)/2. For example, a font with an em of
              1000 fUnits will set this field to 500.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">vertTypoLineGap</td><td role="">The vertical typographic gap for this font.
              An application can determine the recommended line
              spacing for single spaced vertical text for an OpenType
              font by the following expression: ideo embox width +
              vhea.vertTypoLineGap </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">advanceHeightMax</td><td role="">The maximum advance height measurement -in
              FUnits found in the font. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">minTopSideBearing</td><td role="">The minimum top sidebearing measurement found
              in the font, in FUnits. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">minBottomSideBearing</td><td role="">The minimum bottom sidebearing measurement
              found in the font, in FUnits. This value must be
              consistent with the entries in the vertical metrics
              table. </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yMaxExtent</td><td role="">Defined as yMaxExtent=minTopSideBearing +
              (yMax - yMin)</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretSlopeRise</td><td role="">The value of the caretSlopeRise field divided
              by the value of the caretSlopeRun Field determines the
              slope of the caret. A value of 0 for the rise and a
              value of 1 for the run specifies a horizontal caret. A
              value of 1 for the rise and a value of 0 for the run
              specifies a vertical caret. Intermediate values are
              desirable for fonts whose glyphs are oblique or italic.
              For a vertical font, a horizontal caret is
              best.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretSlopeRun</td><td role="">See the caretSlopeRise field. Value=1 for
              nonslanted vertical fonts.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">caretOffset</td><td role="">The amount by which the highlight on a
              slanted glyph needs to be shifted away from the glyph in
              order to produce the best appearance. Set value equal to
              0 for nonslanted fonts.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">metricDataFormat</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">numOfLongVerMetrics</td><td role="">Number of advance heights in the vertical
              metrics table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p role="">Vertical Header Table Example</p><div class="table"><a name="idm320128099776"></a><p class="title"><strong>Table 37.3. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">0x00011000</td><td role="">version</td><td role="">Version number of the vertical header table,
              in fixed-point format, is 1.1 </td><td class="auto-generated"> </td></tr><tr><td role="">1024</td><td role="">vertTypoAscender</td><td role="">Half the em-square height.</td><td class="auto-generated"> </td></tr><tr><td role="">-1024</td><td role="">vertTypoDescender</td><td role="">Minus half the em-square
              height.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">vertTypoLineGap</td><td role="">Typographic line gap is 0
              FUnits.</td><td class="auto-generated"> </td></tr><tr><td role="">2079</td><td role="">advanceHeightMax</td><td role="">The maximum advance height measurement found
              in the font is 2079 FUnits.</td><td class="auto-generated"> </td></tr><tr><td role="">-342</td><td role="">minTopSideBearing</td><td role="">The minimum top sidebearing measurement found
              in the font is -342 FUnits.</td><td class="auto-generated"> </td></tr><tr><td role="">-333</td><td role="">minBottomSideBearing</td><td role="">The minimum bottom sidebearing measurement
              found in the font is -333 FUnits.</td><td class="auto-generated"> </td></tr><tr><td role="">2036</td><td role="">yMaxExtent</td><td role="">minTopSideBearing +
              (yMax-yMin)=2036.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">caretSlopeRise</td><td role="">The caret slope rise of 0 and a caret slope
              run of 1 indicate a horizontal caret for a vertical
              font.</td><td class="auto-generated"> </td></tr><tr><td role="">1</td><td role="">caretSlopeRun</td><td role="">The caret slope rise of 0 and a caret slope
              run of 1 indicate a horizontal caret for a vertical
              font.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">caretOffset</td><td role="">Value set to 0 for nonslanted
              fonts.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">reserved</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">0</td><td role="">metricDataFormat</td><td role="">Set to 0.</td><td class="auto-generated"> </td></tr><tr><td role="">258</td><td role="">numOfLongVerMetrics</td><td role="">Number of advance heights in the vertical
              metrics table is 258.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>