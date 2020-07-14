<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.vhea"></a>Chapter 38. vhea - Vertical Header Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm239470418288"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.39.1.1"></a>Specification</h4></div></div></div><p>The vertical header table (tag name:
        <a class="link" href="chapter.vhea.html" title="Chapter 38. vhea - Vertical Header Table">vhea</a>) contains information needed for
        vertical fonts. The glyphs of vertical fonts are written
        either top to bottom or bottom to top. This table contains
        information that is general to the font as a
        whole. Information that pertains to specific glyphs is given
        in the vertical metrics table (tag name:
        <a class="link" href="chapter.vmtx.html" title="Chapter 39. vmtx - Vertical Metrics Table">vmtx</a>) described separately. The formats of
        these tables are similar to those for horizontal metrics (hhea
        and hmtx).</p><p>Data in the vertical header table must be consistent
          with data that appears in the vertical metrics table. The
          advance height and top sidebearing values in the vertical
          metrics table must correspond with the maximum advance
          height and minimum bottom sidebearing values in the vertical
          header table.</p><p>See the section "CommonType CJK Font Guidelines" for more
          information about constructing CJK (Chinese, Japanese, and
          Korean) fonts.</p><p>The difference between version 1.0 and version 1.1 is
	  the name and definition of: </p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>ascender becomes vertTypoAscender</p></li><li class="listitem"><p>descender becomes vertTypoDescender</p></li><li class="listitem"><p>lineGap becomes vertTypoLineGap</p></li></ul></div><p>
      </p><p>The vertical header table format follows: Vertical
          Header Table</p><div class="table"><a name="idm239470409328"></a><p class="title"><strong>Table 38.1. Version 1.0</strong></p><div class="table-contents"><table class="table" summary="Version 1.0" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Fixed</td><td>version</td><td>Version number of the vertical header table;
              0x0001000 for version 1.0</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ascent</td><td>Distance in <em class="glossterm">font unit</em>s from the centerline to the
	      previous line’ descent.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>descent</td><td>Distance in <em class="glossterm">font unit</em>s from the centerline to
	      the next line’s ascent.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>lineGap</td><td>Reserved; set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>advanceHeightMax</td><td>The maximum advance height measurement
	      — in <em class="glossterm">font unit</em>s — found in the font. This value
	      must be consistent with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>minTop</td><td>The minimum top sidebearing measurement found
              in the font, in <em class="glossterm">font unit</em>s. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>minBottom</td><td>The minimum bottom sidebearing measurement
              found in the font, in <em class="glossterm">font unit</em>s. This value must be
              consistent with the entries in the vertical metrics
              table. </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMaxExtent</td><td>Defined as yMaxExtent=minTopSideBearing +
              (yMax - yMin)</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretSlopeRise</td><td>The value of the caretSlopeRise field divided
              by the value of the caretSlopeRun Field determines the
              slope of the caret. A value of 0 for the rise and a
              value of 1 for the run specifies a horizontal caret. A
              value of 1 for the rise and a value of 0 for the run
              specifies a vertical caret. Intermediate values are
              desirable for fonts whose glyphs are oblique or italic.
              For a vertical font, a horizontal caret is
              best.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretSlopeRun</td><td>See the caretSlopeRise field. Value=1 for
              nonslanted vertical fonts.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretOffset</td><td>The amount by which the highlight on a
              slanted glyph needs to be shifted away from the glyph in
              order to produce the best appearance. Set value equal to
              0 for nonslanted fonts.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>metricDataFormat</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numOfLongVerMetrics</td><td>Number of advance heights in the vertical
              metrics table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><div class="table"><a name="idm239470378208"></a><p class="title"><strong>Table 38.2. Version 1.1</strong></p><div class="table-contents"><table class="table" summary="Version 1.1" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>Fixed</td><td>version</td><td>Version number of the vertical header table;
              0x00011000 for version 1.1. Note the representation of a
              non-zero fractional part, in Fixed
              numbers.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>vertTypoAscender</td><td>The vertical typographic ascender for this
              font. It is the distance in <em class="glossterm">font unit</em>s from the ideographic
              em-box center baseline for the vertical axis to the
              right of the ideographic em-box and is usually set to
              (head.unitsPerEm)/2. For example, a font with an em of
              1000 fUnits will set this field to 500. See the baseline
              section of the CommonType Tag Registry for a description
              of the ideographic em-box. </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>vertTypoDescender</td><td>The vertical typographic descender for this
              font. It is the distance in <em class="glossterm">font unit</em>s from the ideographic
              em-box center baseline for the horizontal axis to the
              left of the ideographic em-box and is usually set to
              (head.unitsPerEm)/2. For example, a font with an em of
              1000 fUnits will set this field to 500.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>vertTypoLineGap</td><td>The vertical typographic gap for this font.
              An application can determine the recommended line
              spacing for single spaced vertical text for an CommonType
              font by the following expression: ideo embox width +
              vhea.vertTypoLineGap </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>advanceHeightMax</td><td>The maximum advance height measurement -in
              <em class="glossterm">font unit</em>s found in the font. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>minTopSideBearing</td><td>The minimum top sidebearing measurement found
              in the font, in <em class="glossterm">font unit</em>s. This value must be consistent
              with the entries in the vertical metrics
              table.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>minBottomSideBearing</td><td>The minimum bottom sidebearing measurement
              found in the font, in <em class="glossterm">font unit</em>s. This value must be
              consistent with the entries in the vertical metrics
              table. </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yMaxExtent</td><td>Defined as yMaxExtent=minTopSideBearing +
              (yMax - yMin)</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretSlopeRise</td><td>The value of the caretSlopeRise field divided
              by the value of the caretSlopeRun Field determines the
              slope of the caret. A value of 0 for the rise and a
              value of 1 for the run specifies a horizontal caret. A
              value of 1 for the rise and a value of 0 for the run
              specifies a vertical caret. Intermediate values are
              desirable for fonts whose glyphs are oblique or italic.
              For a vertical font, a horizontal caret is
              best.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretSlopeRun</td><td>See the caretSlopeRise field. Value=1 for
              nonslanted vertical fonts.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>caretOffset</td><td>The amount by which the highlight on a
              slanted glyph needs to be shifted away from the glyph in
              order to produce the best appearance. Set value equal to
              0 for nonslanted fonts.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>metricDataFormat</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>numOfLongVerMetrics</td><td>Number of advance heights in the vertical
              metrics table.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>Vertical Header Table Example</p><div class="table"><a name="idm239461940960"></a><p class="title"><strong>Table 38.3. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>0x00011000</td><td>version</td><td>Version number of the vertical header table,
              in fixed-point format, is 1.1 </td><td class="auto-generated"> </td></tr><tr><td>1024</td><td>vertTypoAscender</td><td>Half the em-square height.</td><td class="auto-generated"> </td></tr><tr><td>-1024</td><td>vertTypoDescender</td><td>Minus half the em-square
              height.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>vertTypoLineGap</td><td>Typographic line gap is 0
              <em class="glossterm">font unit</em>s.</td><td class="auto-generated"> </td></tr><tr><td>2079</td><td>advanceHeightMax</td><td>The maximum advance height measurement found
              in the font is 2079 <em class="glossterm">font unit</em>s.</td><td class="auto-generated"> </td></tr><tr><td>-342</td><td>minTopSideBearing</td><td>The minimum top sidebearing measurement found
              in the font is -342 <em class="glossterm">font unit</em>s.</td><td class="auto-generated"> </td></tr><tr><td>-333</td><td>minBottomSideBearing</td><td>The minimum bottom sidebearing measurement
              found in the font is -333 <em class="glossterm">font unit</em>s.</td><td class="auto-generated"> </td></tr><tr><td>2036</td><td>yMaxExtent</td><td>minTopSideBearing +
              (yMax-yMin)=2036.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>caretSlopeRise</td><td>The caret slope rise of 0 and a caret slope
              run of 1 indicate a horizontal caret for a vertical
              font.</td><td class="auto-generated"> </td></tr><tr><td>1</td><td>caretSlopeRun</td><td>The caret slope rise of 0 and a caret slope
              run of 1 indicate a horizontal caret for a vertical
              font.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>caretOffset</td><td>Value set to 0 for nonslanted
              fonts.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>reserved</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>0</td><td>metricDataFormat</td><td>Set to 0.</td><td class="auto-generated"> </td></tr><tr><td>258</td><td>numOfLongVerMetrics</td><td>Number of advance heights in the vertical
              metrics table is 258.</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/></div></div></div>