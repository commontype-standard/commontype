<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.OS2"></a>Chapter 10. OS/2 - OS/2 and Windows Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm363762435408"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.11.1.1"></a>Specification</h4></div></div></div><p>The OS/2 table consists of a set of metrics that are
          required in CommonType fonts. The fourth version of the OS/2
          table (version 3) follows:</p><div class="table"><a name="idm363762433136"></a><p class="title"><strong>Table 10.1. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>0x0003</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>xAvgCharWidth</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWeightClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWidthClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>fsType</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptXSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptYSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptXOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptYOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptXSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptYSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptXOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptYOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yStrikeoutSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yStrikeoutPosition</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sFamilyClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>panose[10]</td><td> </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange1</td><td>Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange2</td><td>Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange3</td><td>Bits 64-95</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange4</td><td>Bits 96-127</td><td class="auto-generated"> </td></tr><tr><td>CHAR</td><td>achVendID[4]</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>fsSelection</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usFirstCharIndex</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usLastCharIndex</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoAscender</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoDescender</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoLineGap</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWinAscent</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWinDescent</td><td> </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulCodePageRange1</td><td>Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulCodePageRange2</td><td>Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sxHeight</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sCapHeight</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usDefaultChar</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usBreakChar</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usMaxContext</td><td> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><h5><a name="idm363762381376"></a>version</h5><p>Format: 2-byte unsigned short</p><p>Units: n/a</p><p>Title: OS/2 table version number.</p><p>Description: The version number for this OS/2
          table.</p><p>Comments: The version number allows for identification
          of the precise contents and layout for the OS/2 table. The
          version number for this layout is three (3). Versions zero
          (0, TrueType rev 1.5), one (1, TrueType rev 1.66) and two
          (2, CommonType rev 1.2) have been used previously.</p><h5><a name="idm363762378560"></a>xAvgCharWidth</h5><p>Format: 2-byte signed short</p><p>Units: Pels / em units</p><p>Title: Average weighted escapement.</p><p>Description: The Average Character Width parameter
          specifies the arithmetic average of the escapement (width)
          of all non-zero width glyphs in the font.</p><p>Comments: The value of xAvgCharWidth is calculated by
	  obtaining the arithmetic average of the width of all
	  non-zero width glyphs in the font. Furthermore, it is
	  strongly recommended that implementers do not rely on this
	  value for computing layout for lines of text. Especially,
	  for cases where complex scripts are used.</p><h5><a name="idm363762375616"></a>usWeightClass</h5><p>Format: 2-byte unsigned short</p><p>Title: Weight class. </p><p>Description: Indicates the visual weight (degree of
          blackness or thickness of strokes) of the characters in the
          font. </p><p>Comments:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="18pc"/></colgroup><thead><tr><th>Value</th><th>Description</th><th>C Definition (from windows.h)</th></tr></thead><tbody><tr><td>100</td><td>Thin</td><td>FW_THIN</td></tr><tr><td>200</td><td>Extra-light (Ultra-light)</td><td>FW_EXTRALIGHT</td></tr><tr><td>300</td><td>Light</td><td>FW_LIGHT</td></tr><tr><td>400</td><td>Normal (Regular)</td><td>FW_NORMAL</td></tr><tr><td>500</td><td>Medium</td><td>FW_MEDIUM</td></tr><tr><td>600</td><td>Semi-bold (Demi-bold)</td><td>FW_SEMIBOLD</td></tr><tr><td>700</td><td>Bold</td><td>FW_BOLD</td></tr><tr><td>800</td><td>Extra-bold (Ultra-bold)</td><td>FW_EXTRABOLD</td></tr><tr><td>900</td><td>Black (Heavy)</td><td>FW_BLACK</td></tr></tbody></table></div><h5><a name="idm363762354464"></a>usWidthClass </h5><p>Format: 2-byte unsigned short</p><p>Title: Width class. </p><p>Description: Indicates a relative change from the normal
          aspect ratio (width to height ratio) as specified by a font
          designer for the glyphs in a font. </p><p>Comments:  Although every character in a font may have a
          different numeric aspect ratio, each character in a font of
          normal width has a relative aspect ratio of one. When a new
          type style is created of a different width class (either by
          a font designer or by some automated means) the relative
          aspect ratio of the characters in the new font is some
          percentage greater or less than those same characters in the
          normal font -- it is this difference that this parameter
          specifies. </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="14pc"/><col width="4pc"/></colgroup><thead><tr><th>Value</th><th>Description</th><th>C Definition</th><th>% of normal</th></tr></thead><tbody><tr><td>1</td><td>Ultra-condensed</td><td>FWIDTH_ULTRA_CONDENSED</td><td>50</td></tr><tr><td>2</td><td>Extra-condensed</td><td>FWIDTH_EXTRA_CONDENSED</td><td>62.5</td></tr><tr><td>3</td><td>Condensed</td><td>FWIDTH_CONDENSED</td><td>75</td></tr><tr><td>4</td><td>Semi-condensed</td><td>FWIDTH_SEMI_CONDENSED</td><td>87.5</td></tr><tr><td>5</td><td>Medium (normal)</td><td>FWIDTH_NORMAL</td><td>100</td></tr><tr><td>6</td><td>Semi-expanded</td><td>FWIDTH_SEMI_EXPANDED</td><td>112.5</td></tr><tr><td>7</td><td>Expanded</td><td>FWIDTH_EXPANDED</td><td>125</td></tr><tr><td>8</td><td>Extra-expanded</td><td>FWIDTH_EXTRA_EXPANDED</td><td>150</td></tr><tr><td>9</td><td>Ultra-expanded</td><td>FWIDTH_ULTRA_EXPANDED</td><td>200</td></tr></tbody></table></div><h5><a name="idm363762328320"></a>fsType</h5><p>Format: 2-byte unsigned short</p><p>Title: Type flags. </p><p>Description: Indicates font embedding licensing rights
          for the font. Embeddable fonts may be stored in a document.
          When a document with embedded fonts is opened on a system
          that does not have the font installed (the remote system),
          the embedded font may be loaded for temporary (and in some
          cases, permanent) use on that system by an embedding-aware
          application. Embedding licensing rights are granted by the
          vendor of the font.</p><p>The CommonType Font Embedding DLL Specification and DLL
          release notes describe the APIs used to implement support
          for CommonType font embedding and loading.
          <span class="emphasis"><em>Applications that implement support for font
            embedding, either through use of the Font Embedding DLL or
            through other means, must not embed fonts which are not
            licensed to permit embedding. Further, applications
            loading embedded fonts for temporary use (see Preview
            &amp; Print and Editable embedding below) must delete the
            fonts when the document containing the embedded font is
            closed.</em></span></p><p>This version of the OS/2 table makes bits 0 - 3 a set of
	  exclusive bits. In other words, at most one bit in this
	  range may be set at a time. The purpose is to remove
	  misunderstandings caused by previous behavior of using the
	  least restrictive of the bits that are set.</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="1cm"/><col width="2cm"/><col width="10cm"/></colgroup><thead><tr><th>Bit</th><th>BitMask</th><th>Description</th></tr></thead><tbody><tr><td> </td><td>0x0000</td><td>Installable Embedding: No fsType bit is set.
                  Thus fsType is zero. Fonts with this setting
                  indicate that they may be embedded and permanently
                  installed on the remote system by an application.
                  The user of the remote system acquires the identical
                  rights, obligations and licenses for that font as
                  the original purchaser of the font, and is subject
                  to the same end-user license agreement, copyright,
                  design patent, and/or trademark as was the original
                  purchaser.</td></tr><tr><td>0</td><td>0x0001</td><td>Reserved, must be zero.</td></tr><tr><td>1</td><td>0x0002</td><td>Restricted License embedding: Fonts that have
                  <span class="emphasis"><em>only</em></span> this bit set must not be
                  <span class="emphasis"><em>modified, embedded or exchanged in any
                    manner</em></span> without first obtaining
                  permission of the legal owner. Caution: For
                  Restricted License embedding to take effect, it must
                  be the only level of embedding selected.</td></tr><tr><td>2</td><td>0x0004</td><td>Preview &amp; Print embedding: When this bit is
                  set, the font may be embedded, and temporarily
                  loaded on the remote system. Documents containing
                  Preview &amp; Print fonts must be opened "read-only;" no
                  edits can be applied to the document.</td></tr><tr><td>3</td><td>0x0008</td><td>Editable embedding: When this bit is set, the
                  font may be embedded but must only be installed
                  <span class="emphasis"><em>temporarily</em></span> on other systems.
                  In contrast to Preview &amp; Print fonts, documents
                  containing Editable fonts <span class="emphasis"><em>may</em></span>
                  be opened for reading, editing is permitted, and
                  changes may be saved.</td></tr><tr><td>4-7</td><td> </td><td>Reserved, must be zero.</td></tr><tr><td>8</td><td>0x0100</td><td>No subsetting: When this bit is set, the font
                  may not be subsetted prior to embedding. Other
                  embedding restrictions specified in bits 0-3 and 9
                  also apply.</td></tr><tr><td>9</td><td>0x0200</td><td>Bitmap embedding only: When this bit is set,
                  only bitmaps contained in the font may be embedded.
                  No outline data may be embedded. If there are no
                  bitmaps available in the font, then the font is
                  considered unembeddable and the embedding services
                  will fail. Other embedding restrictions specified in
                  bits 0-3 and 8 also apply.</td></tr><tr><td>10-15</td><td> </td><td>Reserved, must be zero.</td></tr></tbody></table></div><h5><a name="idm363771625472"></a>ySubscriptXSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript horizontal font size. </p><p>Description: The recommended horizontal size in font
          design units for subscripts for this font.  </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the em square
          size of the font being used for a subscript. The horizontal
          font size specifies a font designer's recommended horizontal
          font size for subscript characters associated with this
          font. If a font does not include all of the required
          subscript characters for an application, and the application
          can substitute characters by scaling the character of a font
          or by substituting characters from another font, this
          parameter specifies the recommended em square for those
          subscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySubScriptXSize is set to 205, then the horizontal size for
          a simulated subscript character would be 1/10th the size of
          the normal character.</p><h5><a name="idm363771621664"></a>ySubscriptYSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript vertical font size. </p><p>Description: The recommended vertical size in font
          design units for subscripts for this font.  </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g. numerics and other, the numeric sizes
          should be stressed. This size field maps to the emHeight of
          the font being used for a subscript. The horizontal font
          size specifies a font designer's recommendation for
          horizontal font size of subscript characters associated with
          this font. If a font does not include all of the required
          subscript characters for an application, and the application
          can substitute characters by scaling the characters in a
          font or by substituting characters from another font, this
          parameter specifies the recommended horizontal EmInc for
          those subscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySubScriptYSize is set to 205, then the vertical size for a
          simulated subscript character would be 1/10th the size of
          the normal character.</p><h5><a name="idm363771617872"></a>ySubscriptXOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript x offset.</p><p>Description: The recommended horizontal offset in font
          design untis for subscripts for this font. </p><p>Comments: The Subscript X Offset parameter specifies a
          font designer's recommended horizontal offset -- from the
          character origin of the font to the character origin of the
          subscript's character -- for subscript characters associated
          with this font. If a font does not include all of the
          required subscript characters for an application, and the
          application can substitute characters, this parameter
          specifies the recommended horizontal position from the
          character escapement point of the last character before the
          first subscript character. For upright characters, this
          value is usually zero; however, if the characters of a font
          have an incline (italic characters) the reference point for
          subscript characters is usually adjusted to compensate for
          the angle of incline.</p><h5><a name="idm363764671520"></a>ySubscriptYOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript y offset. </p><p>Description: The recommended vertical offset in font
          design units from the baseline for subscripts for this font.
        </p><p>Comments: The Subscript Y Offset parameter specifies a
          font designer's recommended vertical offset from the
          character baseline to the character baseline for subscript
          characters associated with this font. Values are expressed
          as a positive offset below the character baseline. If a font
          does not include all of the required subscript for an
          application, this parameter specifies the recommended
          vertical distance below the character baseline for those
          subscript characters.</p><h5><a name="idm363764668512"></a>ySuperscriptXSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript horizontal font size.</p><p>Description: The recommended horizontal size in font
          design units for superscripts for this font. </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the em square
          size of the font being used for a subscript. The horizontal
          font size specifies a font designer's recommended horizontal
          font size for superscript characters associated with this
          font. If a font does not include all of the required
          superscript characters for an application, and the
          application can substitute characters by scaling the
          character of a font or by substituting characters from
          another font, this parameter specifies the recommended em
          square for those superscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySuperScriptXSize is set to 205, then the horizontal size
          for a simulated superscript character would be 1/10th the
          size of the normal character.</p><h5><a name="idm363764664560"></a>ySuperscriptYSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript vertical font size.</p><p>Description: The recommended vertical size in font
          design units for superscripts for this font. </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the emHeight of
          the font being used for a subscript. The vertical font size
          specifies a font designer's recommended vertical font size
          for superscript characters associated with this font. If a
          font does not include all of the required superscript
          characters for an application, and the application can
          substitute characters by scaling the character of a font or
          by substituting characters from another font, this parameter
          specifies the recommended EmHeight for those superscript
          characters.</p><p>For example, if the em square for a font is 2048 and
          ySuperScriptYSize is set to 205, then the vertical size for
          a simulated superscript character would be 1/10th the size
          of the normal character.</p><h5><a name="idm363762306688"></a>ySuperscriptXOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript x offset.</p><p>Description: The recommended horizontal offset in font
          design units for superscripts for this font. </p><p>Comments: The Superscript X Offset parameter specifies a
          font designer's recommended horizontal offset -- from the
          character origin to the superscript character's origin for
          the superscript characters associated with this font. If a
          font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended horizontal position from the escapement point of
          the character before the first superscript character. For
          upright characters, this value is usually zero; however, if
          the characters of a font have an incline (italic characters)
          the reference point for superscript characters is usually
          adjusted to compensate for the angle of incline.</p><h5><a name="idm363762303392"></a>ySuperscriptYOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript y offset.</p><p>Description: The recommended vertical offset in font
          design units from the baseline for superscripts for this
          font. </p><p>Comments: The Superscript Y Offset parameter specifies a
          font designer's recommended vertical offset -- from the
          character baseline to the superscript character's baseline
          associated with this font. Values for this parameter are
          expressed as a positive offset above the character baseline.
          If a font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended vertical distance above the character baseline
          for those superscript characters.</p><h5><a name="idm363762300224"></a>yStrikeoutSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Strikeout size.</p><p>Description: Width of the strikeout stroke in font
          design units. </p><p>Comments: This field should normally be the width of the
          em dash for the current font. If the size is one, the
          strikeout line will be the line represented by the strikeout
          position field. If the value is two, the strikeout line will
          be the line represented by the strikeout position and the
          line immediately above the strikeout position. For a Roman
          font with a 2048 em square, 102 is suggested.</p><h5><a name="idm363762297280"></a>yStrikeoutPosition</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Strikeout position.</p><p>Description: The position of the top of the strikeout
          stroke relative to the baseline in font design units.
        </p><p>Comments: Positive values represent distances above the
          baseline, while negative values represent distances below
          the baseline. A value of zero falls directly on the
          baseline, while a value of one falls one pel above the
          baseline. The value of strikeout position should not
          interfere with the recognition of standard characters, and
          therefore should not line up with crossbars in the font. For
          a Roman font with a 2048 em square, 460 is suggested.</p><h5><a name="idm363762294720"></a>sFamilyClass</h5><p>Format: 2-byte signed short</p><p>Title: Font-family class and subclass.</p><p>Description: This parameter is a classification of
          font-family design. </p><p>Comments: The font class and font subclass are
          registered values assigned by IBM to each font family. This
          parameter is intended for use in selecting an alternate font
          when the requested font is not available. The font class is
          the most general and the font subclass is the most specific.
          The high byte of this field contains the family class, while
          the low byte contains the family subclass. More information
          about this field.  </p><h5><a name="idm363762292064"></a>Panose</h5><p>Format: 10 byte array</p><p>Title: PANOSE classification number</p><p>International: Additional specifications are required
          for PANOSE to classify non-Latin character sets.</p><p>Description: This 10 byte series of numbers is used to
          describe the visual characteristics of a given typeface.
          These characteristics are then used to associate the font
          with other fonts of similar appearance having different
          names. The variables for each digit are listed below. The
          Panose values are fully described in the Panose "greybook"
          reference, currently owned by Agfa-Monotype. </p><p>Comments: The PANOSE definition contains ten digits each
          of which currently describes up to sixteen variations.
          Windows uses bFamilyType, bSerifStyle and bProportion in the
          font mapper to determine family type. It also uses
          bProportion to determine if the font is monospaced. If the
          font is a symbol font, the first byte of the PANOSE number
          (bFamilyType) must be set to "pictorial." Good PANOSE values
          in fonts are very valuable to users of the Windows fonts
          folder. The specification for assigning PANOSE values is
          located at <a class="ulink" href="http://www.panose.com/hardware/pan2.asp" target="_top">http://www.panose.com/hardware/pan2.asp</a>.</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th>Type</th><th>Name</th></tr></thead><tbody><tr><td>BYTE</td><td>bFamilyType</td></tr><tr><td>BYTE</td><td>bSerifStyle</td></tr><tr><td>BYTE</td><td>bWeight</td></tr><tr><td>BYTE</td><td>bProportion;</td></tr><tr><td>BYTE</td><td>bContrast</td></tr><tr><td>BYTE</td><td>bStrokeVariation</td></tr><tr><td>BYTE</td><td>bArmStyle</td></tr><tr><td>BYTE</td><td>bLetterform</td></tr><tr><td>BYTE</td><td>bMidline</td></tr><tr><td>BYTE</td><td>bXHeight</td></tr></tbody></table></div><h5><a name="idm363762272016"></a>ulUnicodeRange1 (Bits 0-31)</h5><h5><a name="idm363762271600"></a>ulUnicodeRange2 (Bits 32-63)</h5><h5><a name="idm363762271184"></a>ulUnicodeRange3 (Bits 64-95)</h5><h5><a name="idm363762270768"></a>ulUnicodeRange4 (Bits 96-127)</h5><p>Format: 32-bit unsigned long(4 copies) totaling 128
          bits.</p><p>Title: Unicode Character Range</p><p>Description: This field is used to specify the Unicode
          blocks or ranges encompassed by the font file in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform 3, encoding ID 1 (Microsoft platform).
          If the bit is set (1) then the Unicode range is considered
          functional. If the bit is clear (0) then the range is not
          considered functional. Each of the bits is treated as an
          independent flag and the bits can be set in any combination.
          The determination of "functional" is left up to the font
          designer, although character set selection should attempt to
          be functional by ranges if at all possible.</p><p>All reserved fields must be zero. Each long is in Big-Endian
          form. See the Basic Multilingual Plane of ISO/IEC 10646-1 or
          the Unicode Standard v.3.0 for the list of Unicode ranges
          and characters.  </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th>Bit</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>Basic Latin</td></tr><tr><td>1</td><td>Latin-1 Supplement</td></tr><tr><td>2</td><td>Latin Extended-A</td></tr><tr><td>3</td><td>Latin Extended-B</td></tr><tr><td>4</td><td>IPA Extensions</td></tr><tr><td>5</td><td>Spacing Modifier Letters</td></tr><tr><td>6</td><td>Combining Diacritical Marks</td></tr><tr><td>7</td><td>Greek and Coptic</td></tr><tr><td>8</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>9</td><td>Cyrillic</td></tr><tr><td> </td><td>Cyrillic Supplementary</td></tr><tr><td>10</td><td>Armenian</td></tr><tr><td>11</td><td>Hebrew</td></tr><tr><td>12</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>13</td><td>Arabic</td></tr><tr><td>14</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>15</td><td>Devanagari</td></tr><tr><td>16</td><td>Bengali</td></tr><tr><td>17</td><td>Gurmukhi</td></tr><tr><td>18</td><td>Gujarati</td></tr><tr><td>19</td><td>Oriya</td></tr><tr><td>20</td><td>Tamil</td></tr><tr><td>21</td><td>Telugu</td></tr><tr><td>22</td><td>Kannada</td></tr><tr><td>23</td><td>Malayalam</td></tr><tr><td>24</td><td>Thai</td></tr><tr><td>25</td><td>Lao</td></tr><tr><td>26</td><td>Georgian</td></tr><tr><td>27</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>28</td><td>Hangul Jamo</td></tr><tr><td>29</td><td>Latin Extended Additional</td></tr><tr><td>30</td><td>Greek Extended</td></tr><tr><td>31</td><td>General Punctuation</td></tr><tr><td>32</td><td>Superscripts And Subscripts</td></tr><tr><td>33</td><td>Currency Symbols</td></tr><tr><td>34</td><td>Combining Diacritical Marks For Symbols</td></tr><tr><td>35</td><td>Letterlike Symbols</td></tr><tr><td>36</td><td>Number Forms</td></tr><tr><td>37</td><td>Arrows</td></tr><tr><td> </td><td>Supplemental Arrows-A</td></tr><tr><td> </td><td>Supplemental Arrows-B</td></tr><tr><td>38</td><td>Mathematical Operators</td></tr><tr><td> </td><td>Supplemental Mathematical Operators</td></tr><tr><td> </td><td>Miscellaneous Mathematical Symbols-A</td></tr><tr><td> </td><td>Miscellaneous Mathematical Symbols-B</td></tr><tr><td>39</td><td>Miscellaneous Technical</td></tr><tr><td>40</td><td>Control Pictures</td></tr><tr><td>41</td><td>Optical Character Recognition</td></tr><tr><td>42</td><td>Enclosed Alphanumerics</td></tr><tr><td>43</td><td>Box Drawing</td></tr><tr><td>44</td><td>Block Elements</td></tr><tr><td>45</td><td>Geometric Shapes</td></tr><tr><td>46</td><td>Miscellaneous Symbols</td></tr><tr><td>47</td><td>Dingbats</td></tr><tr><td>48</td><td>CJK Symbols And Punctuation</td></tr><tr><td>49</td><td>Hiragana</td></tr><tr><td>50</td><td>Katakana</td></tr><tr><td> </td><td>Katakana Phonetic Extensions</td></tr><tr><td>51</td><td>Bopomofo</td></tr><tr><td> </td><td>Bopomofo Extended</td></tr><tr><td> </td><td>  Extended Bopomofo</td></tr><tr><td>52</td><td>Hangul Compatibility Jamo</td></tr><tr><td>53</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>54</td><td>Enclosed CJK Letters And Months</td></tr><tr><td>55</td><td>CJK Compatibility</td></tr><tr><td>56</td><td>Hangul Syllables</td></tr><tr><td>57</td><td>Non-Plane 0<a href="#ftn.idm363762186112" class="footnote" id="idm363762186112"><sup class="footnote">[a]</sup></a></td></tr><tr><td>58</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>59</td><td>CJK Unified Ideographs</td></tr><tr><td> </td><td>CJK Radicals Supplement</td></tr><tr><td> </td><td>Kangxi Radicals</td></tr><tr><td> </td><td>Ideographic Description Characters</td></tr><tr><td> </td><td>CJK Unified Ideograph Extension A</td></tr><tr><td> </td><td>CJK Unified Ideograph Extension B</td></tr><tr><td> </td><td>Kanbun</td></tr><tr><td>60</td><td>Private Use Area</td></tr><tr><td>61</td><td>CJK Compatibility Ideographs</td></tr><tr><td> </td><td>CJK Compatibility Ideographs Supplement</td></tr><tr><td>62</td><td>Alphabetic Presentation Forms</td></tr><tr><td>63</td><td>Arabic Presentation Forms-A</td></tr><tr><td>64</td><td>Combining Half Marks</td></tr><tr><td>65</td><td>CJK Compatibility Forms</td></tr><tr><td>66</td><td>Small Form Variants</td></tr><tr><td>67</td><td>Arabic Presentation Forms-B</td></tr><tr><td>68</td><td>Halfwidth And Fullwidth Forms</td></tr><tr><td>69</td><td>Specials</td></tr><tr><td>70</td><td>Tibetan</td></tr><tr><td>71</td><td>Syriac</td></tr><tr><td>72</td><td>Thaana</td></tr><tr><td>73</td><td>Sinhala</td></tr><tr><td>74</td><td>Myanmar</td></tr><tr><td>75</td><td>Ethiopic</td></tr><tr><td>76</td><td>Cherokee</td></tr><tr><td>77</td><td>Unified Canadian Aboriginal Syllabics</td></tr><tr><td>78</td><td>Ogham</td></tr><tr><td>79</td><td>Runic</td></tr><tr><td>80</td><td>Khmer</td></tr><tr><td>81</td><td>Mongolian</td></tr><tr><td>82</td><td>Braille Patterns</td></tr><tr><td>83</td><td>Yi Syllables</td></tr><tr><td> </td><td>Yi Radicals</td></tr><tr><td>84</td><td>Tagalog</td></tr><tr><td> </td><td>Hanunoo</td></tr><tr><td> </td><td>Buhid</td></tr><tr><td> </td><td>Tagbanwa</td></tr><tr><td>85</td><td>Old Italic</td></tr><tr><td>86</td><td>Gothic</td></tr><tr><td>87</td><td>Deseret</td></tr><tr><td>88</td><td>Byzantine Musical Symbols</td></tr><tr><td> </td><td>Musical Symbols</td></tr><tr><td>89</td><td>Mathematical Alphanumeric Symbols</td></tr><tr><td>90</td><td>Private Use (plane 15)</td></tr><tr><td> </td><td>Private Use (plane 16)</td></tr><tr><td>91</td><td>Variation Selectors</td></tr><tr><td>92</td><td>Tags</td></tr><tr><td>93-127</td><td>Reserved for Unicode SubRanges</td></tr></tbody><tbody class="footnotes"><tr><td colspan="2"><div id="ftn.idm363762186112" class="footnote"><p><a href="#idm363762186112" class="para"><sup class="para">[a] </sup></a>Setting bit 57 implies that there is
                      at least one codepoint beyond the Basic
                      Multilingual Plane that is supported by this
                      font.</p></div></td></tr></tbody></table></div><h5><a name="idm363762128816"></a>achVendID</h5><p>Format: 4-byte character array</p><p>Title: Font Vendor Identification</p><p>Description: The four character identifier for the
          vendor of the given type face.</p><p>Comments: This is not the royalty owner of the original
          artwork. This is the company responsible for the marketing
          and distribution of the typeface that is being classified.
          It is reasonable to assume that there will be 6 vendors of
          ITC Zapf Dingbats for use on desktop platforms in the near
          future (if not already). It is also likely that the vendors
          will have other inherent benefits in their fonts (more kern
          pairs, unregularized data, hand hinted, etc.). This
          identifier will allow for the correct vendor's type to be
          used over another, possibly inferior, font file. The Vendor
          ID value is not required.</p><p>Microsoft has assigned values for some font suppliers as
          listed below. Uppercase vendor ID's are reserved by
          Microsoft. Other suppliers can choose their own mixed case
          or lowercase ID's, or leave the field blank.</p><p>For a list of registered Vendor id's see our <a class="ulink" href="http://www.microsoft.com/typography/links/vendorlist.asp" target="_top">Registered
            'vendors'</a> links page.</p><h5><a name="idm363762124176"></a>fsSelection</h5><p>Format: 2-byte bit field.</p><p>Title: Font selection flags.</p><p>Description: Contains information concerning the nature
          of the font patterns, as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="8pc"/><col width="10pc"/></colgroup><thead><tr><th>Bit #</th><th>macStyle bit</th><th>C Definition</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>bit 1</td><td>ITALIC</td><td>Font contains Italic characters, otherwise they
                  are upright.</td></tr><tr><td>1</td><td> </td><td>UNDERSCORE</td><td>Characters are underscored.</td></tr><tr><td>2</td><td> </td><td>NEGATIVE</td><td>Characters have their foreground and background
                  reversed.</td></tr><tr><td>3</td><td> </td><td>OUTLINED</td><td>Outline (hollow) characters, otherwise they are
                  solid.</td></tr><tr><td>4</td><td> </td><td>STRIKEOUT</td><td>Characters are overstruck</td></tr><tr><td>5</td><td>bit 0</td><td>BOLD</td><td>Characters are emboldened.</td></tr><tr><td>6</td><td> </td><td>REGULAR</td><td>Characters are in the standard weight/style for
                  the font.</td></tr></tbody></table></div><p>Comments: All undefined bits must be zero.</p><p>This field contains information on the original design
          of the font. Bits 0 &amp; 5 can be used to determine if the font
          was designed with these features or whether some type of
          machine simulation was performed on the font to achieve this
          appearance. Bits 1-4 are rarely used bits that indicate the
          font is primarily a decorative or special purpose
          font.</p><p>If bit 6 is set, then bits 0 and 5 must be clear, else
          the behavior is undefined. As noted above, the settings of
          bits 0 and 1 must be reflected in the macStyle bits in the
          <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a> table. While bit 6 on implies that
          bits 0 and 1 of macStyle are clear (along with bits 0 and 5
          of fsSelection), the reverse is not true. Bits 0 and 1 of
          macStyle (and 0 and 5 of fsSelection) may be clear and that
          does not give any indication of whether or not bit 6 of
          fsSelection is clear (e.g., Arial Light would have all bits
          cleared; it is not the regular version of Arial). </p><h5><a name="idm363762099904"></a>usFirstCharIndex</h5><p>Format: 2-byte USHORT</p><p>Description: The minimum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and platform- specific encoding ID 0 or 1. For most fonts
          supporting Win-ANSI or other character sets, this value
          would be 0x0020. This field cannot represent supplementary
	  character values (codepoints greater than 0xFFFF). Fonts that
	  support supplementary characters should set the value in this
	  field to 0xFFFF if the minimum index value is a supplementary
	  character.</p><h5><a name="idm363762098144"></a>usLastCharIndex</h5><p>Format: 2-byte USHORT</p><p>Description: The maximum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and encoding ID 0 or 1. This value depends on which
          character sets the font supports. This field cannot
	  represent supplementary character values (codepoints greater
	  than 0xFFFF). Fonts that support supplementary characters
	  should set the value in this field to 0xFFFF. </p><h5><a name="idm363762096512"></a>sTypoAscender</h5><p>Format: SHORT</p><p>Description: The typographic ascender for this font.
          Remember that this is not the same as the Ascender value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoAscender in
          Latin based fonts is the Ascender value from an AFM file.
          For CJK fonts see below.</p><p>The suggested usage for sTypoAscender is that it be used
          in conjunction with unitsPerEm to compute a typographically
          correct default line spacing. The goal is to free
          applications from Macintosh or Windows-specific metrics
          which are constrained by backward compatibility
          requirements. These new metrics, when combined with the
          character design widths, will allow applications to lay out
          documents in a typographically correct and portable fashion.
          These metrics will be exposed through Windows APIs.
          Macintosh applications will need to access the 'sfnt'
          resource and parse it to extract this data from the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table.</p><p>For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoAscender is
          that which describes the top of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoAscender must be set to
          880. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p>Also see the Recommendations Section for more on this
          field. </p><h5><a name="idm363762091088"></a>sTypoDescender</h5><p>Format: SHORT</p><p>Description: The typographic descender for this font.
          Remember that this is not the same as the Descender value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoDescender in
          Latin based fonts is the Descender value from an AFM file.
          For CJK fonts see below.</p><p>The suggested usage for sTypoDescender is that it be
          used in conjunction with unitsPerEm to compute a
          typographically correct default line spacing. The goal is to
          free applications from Macintosh or Windows-specific metrics
          which are constrained by backward compatability
          requirements. These new metrics, when combined with the
          character design widths, will allow applications to lay out
          documents in a typographically correct and portable fashion.
          These metrics will be exposed through Windows APIs.
          Macintosh applications will need to access the 'sfnt'
          resource and parse it to extract this data from the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API).</p><p>For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoDescender
          is that which describes the bottom of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoDescender must be set to
          -120. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p>Also see the Recommendations Section for more on this
          field. </p><h5><a name="idm363762085680"></a>sTypoLineGap</h5><p>Format: 2-byte SHORT</p><p>Description: The typographic line gap for this font.
          Remember that this is not the same as the LineGap value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner.</p><p>The suggested usage for usTypoLineGap is that it be used
          in conjunction with unitsPerEm to compute a typographically
          correct default line spacing. Typical values average 7-10%
          of units per em. The goal is to free applications from
          Macintosh or Windows-specific metrics which are constrained
          by backward compatability requirements (see chapter,
          "Recommendations for CommonType Fonts"). These new metrics, when
          combined with the character design widths, will allow
          applications to lay out documents in a typographically
          correct and portable fashion. These metrics will be exposed
          through Windows APIs. Macintosh applications will need to
          access the 'sfnt' resource and parse it to extract this data
          from the <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes
          the <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API) </p><h5><a name="idm363762081040"></a>usWinAscent</h5><p>Format: 2-byte USHORT</p><p>Description: The ascender metric for Windows. This, too,
          is distinct from Apple's Ascender value and from the
          usTypoAscender values. usWinAscent is computed as the yMax
          for all characters in the Windows ANSI character set.
          usWinAscent is used to compute the Windows font height and
          default line spacing. For platform 3 encoding 0 fonts, it is
          the same as yMax. Windows will clip the bitmap of any
          portion of a glyph that appears above this value. Some
          applications use this value to determine default line
          spacing. This is strongly discouraged. The typographic
          ascender, descender and line gap fields in conjunction with
          unitsPerEm should be used for this purpose. Developers
          should set this field keeping the above factors in
          mind.</p><p>If any clipping is unacceptable, then the value should
          be set to yMax.</p><p>However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against CommonType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped.</p><h5><a name="idm363762077744"></a>usWinDescent</h5><p>Format: 2-byte USHORT</p><p>Description: The descender metric for Windows. This,
          too, is distinct from Apple's Descender value and from the
          usTypoDescender values. usWinDescent is computed as the
          -yMin for all characters in the Windows ANSI character set.
          usWinDescent is used to compute the Windows font height and
          default line spacing. For platform 3 encoding 0 fonts, it is
          the same as -yMin. Windows will clip the bitmap of any
          portion of a glyph that appears below this value. Some
          applications use this value to determine default line
          spacing. This is strongly discouraged. The typographic
          ascender, descender and line gap fields in conjunction with
          unitsPerEm should be used for this purpose. Developers
          should set this field keeping the above factors in
          mind.</p><p>If any clipping is unacceptable, then the value should
          be set to yMin.</p><p>However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against CommonType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped. </p><h5><a name="idm363762074432"></a>ulCodePageRange1 Bits 0-31</h5><h5><a name="idm363762074016"></a>ulCodePageRange2 Bits 32-63 </h5><p>Format: 32-bit unsigned long(2 copies) totaling 64
          bits.</p><p>Title: Code Page Character Range</p><p>Description: This field is used to specify the code
        pages encompassed by the font file in the
        <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable for platform 3, encoding ID 1
        (Microsoft platform). If the font file is encoding ID 0, then
        the Symbol Character Set bit should be set. If the bit is set
        (1) then the code page is considered functional. If the bit is
        clear (0) then the code page is not considered
        functional. Each of the bits is treated as an independent flag
        and the bits can be set in any combination. The determination
        of "functional" is left up to the font designer, although
        character set selection should attempt to be functional by
        code pages if at all possible.</p><p>Symbol character sets have a special meaning. If the
        symbol bit (31) is set, and the font file contains a
        <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable for platform of 3 and
        encoding ID of 1, then all of the characters in the Unicode
        range 0xF000 - 0xF0FF (inclusive) will be used to enumerate
        the symbol character set. If the bit is not set, any
        characters present in that range will not be enumerated as a
        symbol character set.</p><p>All reserved fields must be zero. Each long is in
          Big-Endian form. </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="6pc"/><col width="6pc"/><col width="18pc"/></colgroup><thead><tr><th>Bit</th><th>Code</th><th>Page Description</th></tr></thead><tbody><tr><td>0</td><td>1252</td><td>Latin 1</td></tr><tr><td>1</td><td>1250</td><td>Latin 2: Eastern Europe</td></tr><tr><td>2</td><td>1251</td><td>Cyrillic</td></tr><tr><td>3</td><td>1253</td><td>Greek</td></tr><tr><td>4</td><td>1254</td><td>Turkish</td></tr><tr><td>5</td><td>1255</td><td>Hebrew</td></tr><tr><td>6</td><td>1256</td><td>Arabic</td></tr><tr><td>7</td><td>1257</td><td>Windows Baltic</td></tr><tr><td>8</td><td>1258</td><td>Vietnamese</td></tr><tr><td>9-15</td><td> </td><td>Reserved for Alternate ANSI</td></tr><tr><td>16</td><td>874</td><td>Thai</td></tr><tr><td>17</td><td>932</td><td>JIS/Japan</td></tr><tr><td>18</td><td>936</td><td>Chinese: Simplified chars--PRC and
                  Singapore</td></tr><tr><td>19</td><td>949</td><td>Korean Wansung</td></tr><tr><td>20</td><td>950</td><td>Chinese: Traditional chars--Taiwan and Hong
                  Kong</td></tr><tr><td>21</td><td>1361</td><td>Korean Johab</td></tr><tr><td>22-28</td><td> </td><td>Reserved for Alternate ANSI &amp; OEM</td></tr><tr><td>29</td><td> </td><td>Macintosh Character Set (US Roman)</td></tr><tr><td>30</td><td> </td><td>OEM Character Set</td></tr><tr><td>31</td><td> </td><td>Symbol Character Set</td></tr><tr><td>32-47</td><td> </td><td>Reserved for OEM</td></tr><tr><td>48</td><td>869</td><td>IBM Greek</td></tr><tr><td>49</td><td>866</td><td>MS-DOS Russian</td></tr><tr><td>50</td><td>865</td><td>MS-DOS Nordic</td></tr><tr><td>51</td><td>864</td><td>Arabic</td></tr><tr><td>52</td><td>863</td><td>MS-DOS Canadian French</td></tr><tr><td>53</td><td>862</td><td>Hebrew</td></tr><tr><td>54</td><td>861</td><td>MS-DOS Icelandic</td></tr><tr><td>55</td><td>860</td><td>MS-DOS Portuguese</td></tr><tr><td>56</td><td>857</td><td>IBM Turkish</td></tr><tr><td>57</td><td>855</td><td>IBM Cyrillic; primarily Russian</td></tr><tr><td>58</td><td>852</td><td>Latin 2</td></tr><tr><td>59</td><td>775</td><td>MS-DOS Baltic</td></tr><tr><td>60</td><td>737</td><td>Greek; former 437 G</td></tr><tr><td>61</td><td>708</td><td>Arabic; ASMO 708</td></tr><tr><td>62</td><td>850</td><td>WE/Latin 1</td></tr><tr><td>63</td><td>437</td><td>US</td></tr></tbody></table></div><h5><a name="idm363762006848"></a>sxHeight</h5><p>Format: SHORT</p><p>Description: This metric specifies the distance between
          the baseline and the approximate height of non-ascending
          lowercase letters measured in FUnits. This value would
          normally be specified by a type designer but in situations
          where that is not possible, for example when a legacy font
          is being converted, the value may be set equal to the top of
          the unscaled and unhinted glyph bounding box of the glyph
          encoded at U+0078 (LATIN SMALL LETTER X). If no glyph is
          encoded in this position the field should be set to
          0.</p><p>This metric, if specified, can be used in font
          substitution: the xHeight value of one font can be scaled to
          approximate the apparent size of another. </p><h5><a name="idm363762004496"></a>sCapHeight</h5><p>Format: SHORT</p><p>Description: This metric specifies the distance between
          the baseline and the approximate height of uppercase letters
          measured in FUnits. This value would normally be specified
          by a type designer but in situations where that is not
          possible, for example when a legacy font is being converted,
          the value may be set equal to the top of the unscaled and
          unhinted glyph bounding box of the glyph encoded at U+0048
          (LATIN CAPITAL LETTER H). If no glyph is encoded in this
          position the field should be set to 0.</p><p>This metric, if specified, can be used in systems that
          specify type size by capital height measured in millimeters.
          It can also be used as an alignment metric; the top of a
          drop capital, for instance, can be aligned to the sCapHeight
          metric of the first line of text. </p><h5><a name="idm363762002016"></a>usDefaultChar</h5><p>Format: USHORT</p><p>Description: Whenever a request is made for a character
          that is not in the font, Windows provides this default
          character. If the value of this field is zero, glyph ID 0 is
          to be used for the default character otherwise this is the
          Unicode encoding of the glyph that Windows uses as the
          default character. This field cannot represent supplementary
          character values (codepoints greater than 0xFFFF).</p><h5><a name="idm363762000368"></a>usBreakChar</h5><p>Format: USHORT</p><p>Description: This is the Unicode encoding of the glyph
          that Windows uses as the break character. The break
          character is used to separate words and justify text. Most
          fonts specify 'space' as the break character. This field
          cannot represent supplementary character values (codepoints
          greater than 0xFFFF).</p><h5><a name="idm363761998816"></a>usMaxContext</h5><p>Format: USHORT</p><p>Description: The maximum length of a target glyph
          context for any feature in this font. For example, a font
          which has only a pair kerning feature should set this field
          to 2. If the font also has a ligature feature in which the
          glyph sequence 'f f i' is substituted by the ligature 'ffi',
          then this field should be set to 3. This field could be
          useful to sophisticated line-breaking engines in determining
          how far they should look ahead to test whether something
          could change that effects the line breaking. For chaining
          contextual lookups, the length of the string (covered glyph)
          + (input sequence) + (lookahead sequence) should be
          considered.</p></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.11.1.2"></a>Specification</h4></div></div></div><p>The OS/2 table consists of a set of metrics that are
          required in CommonType fonts. The fourth version of the OS/2
          table (version 3) follows:</p><div class="table"><a name="idm363761995056"></a><p class="title"><strong>Table 10.2. </strong></p><div class="table-contents"><table class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>version</td><td>0x0003</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>xAvgCharWidth</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWeightClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWidthClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>fsType</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptXSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptYSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptXOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySubscriptYOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptXSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptYSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptXOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>ySuperscriptYOffset</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yStrikeoutSize</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>yStrikeoutPosition</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sFamilyClass</td><td> </td><td class="auto-generated"> </td></tr><tr><td>BYTE</td><td>panose[10]</td><td> </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange1</td><td>Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange2</td><td>Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange3</td><td>Bits 64-95</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulUnicodeRange4</td><td>Bits 96-127</td><td class="auto-generated"> </td></tr><tr><td>CHAR</td><td>achVendID[4]</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>fsSelection</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usFirstCharIndex</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usLastCharIndex</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoAscender</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoDescender</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sTypoLineGap</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWinAscent</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usWinDescent</td><td> </td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulCodePageRange1</td><td>Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulCodePageRange2</td><td>Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sxHeight</td><td> </td><td class="auto-generated"> </td></tr><tr><td>SHORT</td><td>sCapHeight</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usDefaultChar</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usBreakChar</td><td> </td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usMaxContext</td><td> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><h5><a name="idm363761943296"></a>version</h5><p>Format: 2-byte unsigned short</p><p>Units: n/a</p><p>Title: OS/2 table version number.</p><p>Description: The version number for this OS/2
          table.</p><p>Comments: The version number allows for identification
          of the precise contents and layout for the OS/2 table. The
          version number for this layout is two (2). Versions one (1)
          and zero (0) have been used previously, in rev.1.66 and 1.5,
          respectively, of the TrueType specification.</p><h5><a name="idm363761940496"></a>xAvgCharWidth</h5><p>Format: 2-byte signed short</p><p>Units: Pels / em units</p><p>Title: Average weighted escapement.</p><p>Description: The Average Character Width parameter
          specifies the arithmetic average of the escapement (width)
          of all of the 26 lowercase letters a through z of the Latin
          alphabet and the space character. If any of the 26 lowercase
          letters are not present, this parameter should equal the
          weighted average of all glyphs in the font. For non-UGL
          (platform 3, encoding 0) fonts, use the unweighted
          average.</p><p>Comments: This parameter is a descriptive attribute of
          the font that specifies the spacing of characters for
          comparing one font to another for selection or substitution.
          For proportionally spaced fonts, this value is useful in
          estimating the length for lines of text. The weighting
          factors provided with this example are only valid for Latin
          lowercase letters. If other character sets, or capital
          letters are used, the corresponding frequency of use values
          should be used. One needs to be careful when comparing fonts
          that use different frequency of use values for font mapping.
          The average character width for the following set of upper
          and lowercase letters only, is calculated according to this
          formula: Sum the individual character widths multiplied by
          the following weighting factors and then divide by 1000. For
          example:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="15pc"/><col width="15pc"/><col/><col/></colgroup><thead><tr><th>Letter</th><th>Weight Factor</th><td class="auto-generated"> </td><td class="auto-generated"> </td></tr></thead><tbody><tr><td>a</td><td>64</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>b</td><td>14</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>c</td><td>27</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>d</td><td>35</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>e</td><td>100</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>f</td><td>20</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>g</td><td>14</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>h</td><td>42</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>i</td><td>63</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>j</td><td>3</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>k</td><td>6</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>l</td><td>35</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>m</td><td>20</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>n</td><td>56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>o</td><td>56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>p</td><td>17</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>q</td><td>4</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>r</td><td>49</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>s</td><td>56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>t</td><td>71</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>u</td><td>31</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>v</td><td>10</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>w</td><td>18</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>x</td><td>3</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>y</td><td>18</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>z</td><td>2</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td>space</td><td>166</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr></tbody></table></div><h5><a name="idm363761901488"></a>usWeightClass</h5><p>Format: 2-byte unsigned short</p><p>Title: Weight class. </p><p>Description: Indicates the visual weight (degree of
          blackness or thickness of strokes) of the characters in the
          font. </p><p>Comments:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="18pc"/></colgroup><thead><tr><th>Value</th><th>Description</th><th>C Definition (from windows.h)</th></tr></thead><tbody><tr><td>100</td><td>Thin</td><td>FW_THIN</td></tr><tr><td>200</td><td>Extra-light (Ultra-light)</td><td>FW_EXTRALIGHT</td></tr><tr><td>300</td><td>Light</td><td>FW_LIGHT</td></tr><tr><td>400</td><td>Normal (Regular)</td><td>FW_NORMAL</td></tr><tr><td>500</td><td>Medium</td><td>FW_MEDIUM</td></tr><tr><td>600</td><td>Semi-bold (Demi-bold)</td><td>FW_SEMIBOLD</td></tr><tr><td>700</td><td>Bold</td><td>FW_BOLD</td></tr><tr><td>800</td><td>Extra-bold (Ultra-bold)</td><td>FW_EXTRABOLD</td></tr><tr><td>900</td><td>Black (Heavy)</td><td>FW_BLACK</td></tr></tbody></table></div><h5><a name="idm363761880336"></a>usWidthClass </h5><p>Format: 2-byte unsigned short</p><p>Title: Width class. </p><p>Description: Indicates a relative change from the normal
          aspect ratio (width to height ratio) as specified by a font
          designer for the glyphs in a font. </p><p>Comments:  Although every character in a font may have a
          different numeric aspect ratio, each character in a font of
          normal width has a relative aspect ratio of one. When a new
          type style is created of a different width class (either by
          a font designer or by some automated means) the relative
          aspect ratio of the characters in the new font is some
          percentage greater or less than those same characters in the
          normal font -- it is this difference that this parameter
          specifies. </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="14pc"/><col width="4pc"/></colgroup><thead><tr><th>Value</th><th>Description</th><th>C Definition</th><th>% of normal</th></tr></thead><tbody><tr><td>1</td><td>Ultra-condensed</td><td>FWIDTH_ULTRA_CONDENSED</td><td>50</td></tr><tr><td>2</td><td>Extra-condensed</td><td>FWIDTH_EXTRA_CONDENSED</td><td>62.5</td></tr><tr><td>3</td><td>Condensed</td><td>FWIDTH_CONDENSED</td><td>75</td></tr><tr><td>4</td><td>Semi-condensed</td><td>FWIDTH_SEMI_CONDENSED</td><td>87.5</td></tr><tr><td>5</td><td>Medium (normal)</td><td>FWIDTH_NORMAL</td><td>100</td></tr><tr><td>6</td><td>Semi-expanded</td><td>FWIDTH_SEMI_EXPANDED</td><td>112.5</td></tr><tr><td>7</td><td>Expanded</td><td>FWIDTH_EXPANDED</td><td>125</td></tr><tr><td>8</td><td>Extra-expanded</td><td>FWIDTH_EXTRA_EXPANDED</td><td>150</td></tr><tr><td>9</td><td>Ultra-expanded</td><td>FWIDTH_ULTRA_EXPANDED</td><td>200</td></tr></tbody></table></div><h5><a name="idm363761854192"></a>fsType</h5><p>Format: 2-byte unsigned short</p><p>Title: Type flags. </p><p>Description: Indicates font embedding licensing rights
          for the font. Embeddable fonts may be stored in a document.
          When a document with embedded fonts is opened on a system
          that does not have the font installed (the remote system),
          the embedded font may be loaded for temporary (and in some
          cases, permanent) use on that system by an embedding-aware
          application. Embedding licensing rights are granted by the
          vendor of the font.</p><p>The CommonType Font Embedding DLL Specification and DLL
          release notes describe the APIs used to implement support
          for CommonType font embedding and loading.
          <span class="emphasis"><em>Applications that implement support for font
            embedding, either through use of the Font Embedding DLL or
            through other means, must not embed fonts which are not
            licensed to permit embedding. Further, applications
            loading embedded fonts for temporary use (see Preview
            &amp; Print and Editable embedding below) must delete the
            fonts when the document containing the embedded font is
            closed.</em></span></p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="1cm"/><col width="2cm"/><col width="10cm"/></colgroup><thead><tr><th>Bit</th><th>BitMask</th><th>Description</th></tr></thead><tbody><tr><td> </td><td>0x0000</td><td>Installable Embedding: No fsType bit is set.
                  Thus fsType is zero. Fonts with this setting
                  indicate that they may be embedded and permanently
                  installed on the remote system by an application.
                  The user of the remote system acquires the identical
                  rights, obligations and licenses for that font as
                  the original purchaser of the font, and is subject
                  to the same end-user license agreement, copyright,
                  design patent, and/or trademark as was the original
                  purchaser.</td></tr><tr><td>0</td><td>0x0001</td><td>Reserved, must be zero.</td></tr><tr><td>1</td><td>0x0002</td><td>Restricted License embedding: Fonts that have
                  <span class="emphasis"><em>only</em></span> this bit set must not be
                  <span class="emphasis"><em>modified, embedded or exchanged in any
                    manner</em></span> without first obtaining
                  permission of the legal owner. Caution: For
                  Restricted License embedding to take effect, it must
                  be the only level of embedding selected.</td></tr><tr><td>2</td><td>0x0004</td><td>Preview &amp; Print embedding: When this bit is
                  set, the font may be embedded, and temporarily
                  loaded on the remote system. Documents containing
                  Preview &amp; Print fonts must be opened "read-only;" no
                  edits can be applied to the document.</td></tr><tr><td>3</td><td>0x0008</td><td>Editable embedding: When this bit is set, the
                  font may be embedded but must only be installed
                  <span class="emphasis"><em>temporarily</em></span> on other systems.
                  In contrast to Preview &amp; Print fonts, documents
                  containing Editable fonts <span class="emphasis"><em>may</em></span>
                  be opened for reading, editing is permitted, and
                  changes may be saved.</td></tr><tr><td>4-7</td><td> </td><td>Reserved, must be zero.</td></tr><tr><td>8</td><td>0x0100</td><td>No subsetting: When this bit is set, the font
                  may not be subsetted prior to embedding. Other
                  embedding restrictions specified in the lower byte
                  also apply.</td></tr><tr><td>9</td><td>0x0200</td><td>Bitmap embedding only: When this bit is set,
                  only bitmaps contained in the font may be embedded.
                  No outline data may be embedded. If there are no
                  bitmaps available in the font, then the font is
                  considered unembeddable and the embedding services
                  will fail. Other embedding restrictions specified in
                  the lower byte also apply.</td></tr><tr><td>10-15</td><td> </td><td>Reserved, must be zero.</td></tr></tbody></table></div><p>Comments: If multiple embedding bits are set, the least
          restrictive license granted takes precedence. For example,
          if bits 1 and 3 are set, bit 3 takes precedence over bit
          1 and the font may be embedded with Editable rights. For
          compatibility purposes, most vendors granting Editable
          embedding rights are also setting the Preview &amp; Print bit
          (0x000C). This will permit an application that only supports
          Preview &amp; Print embedding to detect that font embedding is
          allowed.</p><h5><a name="idm363761826608"></a>ySubscriptXSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript horizontal font size. </p><p>Description: The recommended horizontal size in font
          design units for subscripts for this font.  </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the em square
          size of the font being used for a subscript. The horizontal
          font size specifies a font designer's recommended horizontal
          font size for subscript characters associated with this
          font. If a font does not include all of the required
          subscript characters for an application, and the application
          can substitute characters by scaling the character of a font
          or by substituting characters from another font, this
          parameter specifies the recommended em square for those
          subscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySubScriptXSize is set to 205, then the horizontal size for
          a simulated subscript character would be 1/10th the size of
          the normal character.</p><h5><a name="idm363761822672"></a>ySubscriptYSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript vertical font size. </p><p>Description: The recommended vertical size in font
          design units for subscripts for this font.  </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g. numerics and other, the numeric sizes
          should be stressed. This size field maps to the emHeight of
          the font being used for a subscript. The horizontal font
          size specifies a font designer's recommendation for
          horizontal font size of subscript characters associated with
          this font. If a font does not include all of the required
          subscript characters for an application, and the application
          can substitute characters by scaling the characters in a
          font or by substituting characters from another font, this
          parameter specifies the recommended horizontal EmInc for
          those subscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySubScriptYSize is set to 205, then the vertical size for a
          simulated subscript character would be 1/10th the size of
          the normal character.</p><h5><a name="idm363761818752"></a>ySubscriptXOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript x offset.</p><p>Description: The recommended horizontal offset in font
          design untis for subscripts for this font. </p><p>Comments: The Subscript X Offset parameter specifies a
          font designer's recommended horizontal offset -- from the
          character origin of the font to the character origin of the
          subscript's character -- for subscript characters associated
          with this font. If a font does not include all of the
          required subscript characters for an application, and the
          application can substitute characters, this parameter
          specifies the recommended horizontal position from the
          character escapement point of the last character before the
          first subscript character. For upright characters, this
          value is usually zero; however, if the characters of a font
          have an incline (italic characters) the reference point for
          subscript characters is usually adjusted to compensate for
          the angle of incline.</p><h5><a name="idm363761815296"></a>ySubscriptYOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Subscript y offset. </p><p>Description: The recommended vertical offset in font
          design units from the baseline for subscripts for this font.
        </p><p>Comments: The Subscript Y Offset parameter specifies a
          font designer's recommended vertical offset from the
          character baseline to the character baseline for subscript
          characters associated with this font. Values are expressed
          as a positive offset below the character baseline. If a font
          does not include all of the required subscript for an
          application, this parameter specifies the recommended
          vertical distance below the character baseline for those
          subscript characters.</p><h5><a name="idm363761812160"></a>ySuperscriptXSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript horizontal font size.</p><p>Description: The recommended horizontal size in font
          design units for superscripts for this font. </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the em square
          size of the font being used for a subscript. The horizontal
          font size specifies a font designer's recommended horizontal
          font size for superscript characters associated with this
          font. If a font does not include all of the required
          superscript characters for an application, and the
          application can substitute characters by scaling the
          character of a font or by substituting characters from
          another font, this parameter specifies the recommended em
          square for those superscript characters.</p><p>For example, if the em square for a font is 2048 and
          ySuperScriptXSize is set to 205, then the horizontal size
          for a simulated superscript character would be 1/10th the
          size of the normal character.</p><h5><a name="idm363761808960"></a>ySuperscriptYSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript vertical font size.</p><p>Description: The recommended vertical size in font
          design units for superscripts for this font. </p><p>Comments: If a font has two recommended sizes for
          subscripts, e.g., numerics and other, the numeric sizes
          should be stressed. This size field maps to the emHeight of
          the font being used for a subscript. The vertical font size
          specifies a font designer's recommended vertical font size
          for superscript characters associated with this font. If a
          font does not include all of the required superscript
          characters for an application, and the application can
          substitute characters by scaling the character of a font or
          by substituting characters from another font, this parameter
          specifies the recommended EmHeight for those superscript
          characters.</p><p>For example, if the em square for a font is 2048 and
          ySuperScriptYSize is set to 205, then the vertical size for
          a simulated superscript character would be 1/10th the size
          of the normal character.</p><h5><a name="idm363761805008"></a>ySuperscriptXOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript x offset.</p><p>Description: The recommended horizontal offset in font
          design units for superscripts for this font. </p><p>Comments: The Superscript X Offset parameter specifies a
          font designer's recommended horizontal offset -- from the
          character origin to the superscript character's origin for
          the superscript characters associated with this font. If a
          font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended horizontal position from the escapement point of
          the character before the first superscript character. For
          upright characters, this value is usually zero; however, if
          the characters of a font have an incline (italic characters)
          the reference point for superscript characters is usually
          adjusted to compensate for the angle of incline.</p><h5><a name="idm363761801648"></a>ySuperscriptYOffset</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Superscript y offset.</p><p>Description: The recommended vertical offset in font
          design units from the baseline for superscripts for this
          font. </p><p>Comments: The Superscript Y Offset parameter specifies a
          font designer's recommended vertical offset -- from the
          character baseline to the superscript character's baseline
          associated with this font. Values for this parameter are
          expressed as a positive offset above the character baseline.
          If a font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended vertical distance above the character baseline
          for those superscript characters.</p><h5><a name="idm363761798480"></a>yStrikeoutSize</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Strikeout size.</p><p>Description: Width of the strikeout stroke in font
          design units. </p><p>Comments: This field should normally be the width of the
          em dash for the current font. If the size is one, the
          strikeout line will be the line represented by the strikeout
          position field. If the value is two, the strikeout line will
          be the line represented by the strikeout position and the
          line immediately above the strikeout position. For a Roman
          font with a 2048 em square, 102 is suggested.</p><h5><a name="idm363761795536"></a>yStrikeoutPosition</h5><p>Format: 2-byte signed short</p><p>Units: Font design units</p><p>Title: Strikeout position.</p><p>Description: The position of the top of the strikeout
          stroke relative to the baseline in font design units.
        </p><p>Comments: Positive values represent distances above the
          baseline, while negative values represent distances below
          the baseline. A value of zero falls directly on the
          baseline, while a value of one falls one pel above the
          baseline. The value of strikeout position should not
          interfere with the recognition of standard characters, and
          therefore should not line up with crossbars in the font. For
          a Roman font with a 2048 em square, 460 is suggested.</p><h5><a name="idm363761792448"></a>sFamilyClass</h5><p>Format: 2-byte signed short</p><p>Title: Font-family class and subclass.</p><p>Description: This parameter is a classification of
          font-family design. </p><p>Comments: The font class and font subclass are
          registered values assigned by IBM to each font family. This
          parameter is intended for use in selecting an alternate font
          when the requested font is not available. The font class is
          the most general and the font subclass is the most specific.
          The high byte of this field contains the family class, while
          the low byte contains the family subclass. More information
          about this field.  </p><h5><a name="idm363761789824"></a>Panose</h5><p>Format: 10 byte array</p><p>Title: PANOSE classification number</p><p>International: Additional specifications are required
          for PANOSE to classify non-Latin character sets.</p><p>Description: This 10 byte series of numbers is used to
          describe the visual characteristics of a given typeface.
          These characteristics are then used to associate the font
          with other fonts of similar appearance having different
          names. The variables for each digit are listed below. The
          Panose values are fully described in the Panose "greybook"
          reference, currently owned by Agfa-Monotype. </p><p>Comments: The PANOSE definition contains ten digits each
          of which currently describes up to sixteen variations.
          Windows uses bFamilyType, bSerifStyle and bProportion in the
          font mapper to determine family type. It also uses
          bProportion to determine if the font is monospaced. If the
          font is a symbol font, the first byte of the PANOSE number
          (bFamilyType) must be set to "pictorial." Good PANOSE values
          in fonts are very valuable to users of the Windows fonts
          folder. The specification for assigning PANOSE values is
          located at http://www.fonts.com/hp/panose/greybook/</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th>Type</th><th>Name</th></tr></thead><tbody><tr><td>BYTE</td><td>bFamilyType</td></tr><tr><td>BYTE</td><td>bSerifStyle</td></tr><tr><td>BYTE</td><td>bWeight</td></tr><tr><td>BYTE</td><td>bProportion</td></tr><tr><td>BYTE</td><td>bContrast</td></tr><tr><td>BYTE</td><td>bStrokeVariation</td></tr><tr><td>BYTE</td><td>bArmStyle</td></tr><tr><td>BYTE</td><td>bLetterform</td></tr><tr><td>BYTE</td><td>bMidline</td></tr><tr><td>BYTE</td><td>bXHeight</td></tr></tbody></table></div><h5><a name="idm363761754144"></a>ulUnicodeRange1 (Bits 0-31)</h5><h5><a name="idm363761753728"></a>ulUnicodeRange2 (Bits 32-63)</h5><h5><a name="idm363761753312"></a>ulUnicodeRange3 (Bits 64-95)</h5><h5><a name="idm363761752896"></a>ulUnicodeRange4 (Bits 96-127)</h5><p>Format: 32-bit unsigned long(4 copies) totaling 128
          bits.</p><p>Title: Unicode Character Range</p><p>Description: This field is used to specify the Unicode
          blocks or ranges encompassed by the font file in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform 3, encoding ID 1 (Microsoft platform).
          If the bit is set (1) then the Unicode range is considered
          functional. If the bit is clear (0) then the range is not
          considered functional. Each of the bits is treated as an
          independent flag and the bits can be set in any combination.
          The determination of "functional" is left up to the font
          designer, although character set selection should attempt to
          be functional by ranges if at all possible.</p><p>
          All reserved fields must be zero. Each long is in Big-Endian
          form. See the Basic Multilingual Plane of ISO/IEC 10646-1 or
          the Unicode Standard v.3.0 for the list of Unicode ranges
          and characters.  </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th>Bit</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>Basic Latin</td></tr><tr><td>1</td><td>Latin-1 Supplement</td></tr><tr><td>2</td><td>Latin Extended-A</td></tr><tr><td>3</td><td>Latin Extended-B</td></tr><tr><td>4</td><td>IPA Extensions</td></tr><tr><td>5</td><td>Spacing Modifier Letters</td></tr><tr><td>6</td><td>Combining Diacritical Marks</td></tr><tr><td>7</td><td>Greek</td></tr><tr><td>8</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>9</td><td>Cyrillic</td></tr><tr><td>10</td><td>Armenian</td></tr><tr><td>11</td><td>Hebrew</td></tr><tr><td>12</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>13</td><td>Arabic</td></tr><tr><td>14</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>15</td><td>Devanagari</td></tr><tr><td>16</td><td>Bengali</td></tr><tr><td>17</td><td>Gurmukhi</td></tr><tr><td>18</td><td>Gujarati</td></tr><tr><td>19</td><td>Oriya</td></tr><tr><td>20</td><td>Tamil</td></tr><tr><td>21</td><td>Telugu</td></tr><tr><td>22</td><td>Kannada</td></tr><tr><td>23</td><td>Malayalam</td></tr><tr><td>24</td><td>Thai</td></tr><tr><td>25</td><td>Lao</td></tr><tr><td>26</td><td>Georgian</td></tr><tr><td>27</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>28</td><td>Hangul Jamo</td></tr><tr><td>29</td><td>Latin Extended Additional</td></tr><tr><td>30</td><td>Greek Extended</td></tr><tr><td>31</td><td>General Punctuation</td></tr><tr><td>32</td><td>Superscripts And Subscripts</td></tr><tr><td>33</td><td>Currency Symbols</td></tr><tr><td>34</td><td>Combining Diacritical Marks For Symbols</td></tr><tr><td>35</td><td>Letterlike Symbols</td></tr><tr><td>36</td><td>Number Forms</td></tr><tr><td>37</td><td>Arrows</td></tr><tr><td>38</td><td>Mathematical Operators</td></tr><tr><td>39</td><td>Miscellaneous Technical</td></tr><tr><td>40</td><td>Control Pictures</td></tr><tr><td>41</td><td>Optical Character Recognition</td></tr><tr><td>42</td><td>Enclosed Alphanumerics</td></tr><tr><td>43</td><td>Box Drawing</td></tr><tr><td>44</td><td>Block Elements</td></tr><tr><td>45</td><td>Geometric Shapes</td></tr><tr><td>46</td><td>Miscellaneous Symbols</td></tr><tr><td>47</td><td>Dingbats</td></tr><tr><td>48</td><td>CJK Symbols And Punctuation</td></tr><tr><td>49</td><td>Hiragana</td></tr><tr><td>50</td><td>Katakana</td></tr><tr><td>51</td><td>Bopomofo</td></tr><tr><td> </td><td>  Extended Bopomofo</td></tr><tr><td>52</td><td>Hangul Compatibility Jamo</td></tr><tr><td>53</td><td>CJK Miscellaneous</td></tr><tr><td>54</td><td>Enclosed CJK Letters And Months</td></tr><tr><td>55</td><td>CJK Compatibility</td></tr><tr><td>56</td><td>Hangul</td></tr><tr><td>57</td><td>Surrogates<a href="#ftn.idm363761676768" class="footnote" id="idm363761676768"><sup class="footnote">[a]</sup></a></td></tr><tr><td>58</td><td>Reserved for Unicode SubRanges</td></tr><tr><td>59</td><td>CJK Unified Ideographs</td></tr><tr><td> </td><td> CJK Radicals Supplement</td></tr><tr><td> </td><td>  Kangxi Radicals</td></tr><tr><td> </td><td>  Ideographic Description</td></tr><tr><td> </td><td>  CJK Unified Ideograph Extension A</td></tr><tr><td>60</td><td>Private Use Area</td></tr><tr><td>61</td><td>CJK Compatibility Ideographs</td></tr><tr><td>62</td><td>Alphabetic Presentation Forms</td></tr><tr><td>63</td><td>Arabic Presentation Forms-A</td></tr><tr><td>64</td><td>Combining Half Marks</td></tr><tr><td>65</td><td>CJK Compatibility Forms</td></tr><tr><td>66</td><td>Small Form Variants</td></tr><tr><td>67</td><td>Arabic Presentation Forms-B</td></tr><tr><td>68</td><td>Halfwidth And Fullwidth Forms</td></tr><tr><td>69</td><td>Specials</td></tr><tr><td>70</td><td>Tibetan</td></tr><tr><td>71</td><td>Syriac</td></tr><tr><td>72</td><td>Thaana</td></tr><tr><td>73</td><td>Sinhala</td></tr><tr><td>74</td><td>Myanmar</td></tr><tr><td>75</td><td>Ethiopic</td></tr><tr><td>76</td><td>Cherokee</td></tr><tr><td>77</td><td>Unified Canadian Syllabics</td></tr><tr><td>78</td><td>Ogham</td></tr><tr><td>79</td><td>Runic</td></tr><tr><td>80</td><td>Khmer</td></tr><tr><td>81</td><td>Mongolian</td></tr><tr><td>82</td><td>Braille</td></tr><tr><td>83</td><td>Yi</td></tr><tr><td> </td><td>  Yi Radicals</td></tr><tr><td>84-127</td><td>Reserved for Unicode SubRanges</td></tr></tbody><tbody class="footnotes"><tr><td colspan="2"><div id="ftn.idm363761676768" class="footnote"><p><a href="#idm363761676768" class="para"><sup class="para">[a] </sup></a>Setting bit 57 implies that there is
                      at least one codepoint beyond the Basic
                      Multilingual Plane that is supported by this
                      font.</p></div></td></tr></tbody></table></div><h5><a name="idm363761638512"></a>achVendID</h5><p>Format: 4-byte character array</p><p>Title: Font Vendor Identification</p><p>Description: The four character identifier for the
          vendor of the given type face.</p><p>Comments: This is not the royalty owner of the original
          artwork. This is the company responsible for the marketing
          and distribution of the typeface that is being classified.
          It is reasonable to assume that there will be 6 vendors of
          ITC Zapf Dingbats for use on desktop platforms in the near
          future (if not already). It is also likely that the vendors
          will have other inherent benefits in their fonts (more kern
          pairs, unregularized data, hand hinted, etc.). This
          identifier will allow for the correct vendor's type to be
          used over another, possibly inferior, font file. The Vendor
          ID value is not required.</p><p>Microsoft has assigned values for some font suppliers as
          listed below. Uppercase vendor ID's are reserved by
          Microsoft. Other suppliers can choose their own mixed case
          or lowercase ID's, or leave the field blank.</p><p>For a list of registered Vendor id's see our <a class="ulink" href="http://www.microsoft.com/typography/links/vendorlist.asp" target="_top">Registered
            'vendors'</a> links page.</p><h5><a name="idm363761633872"></a>fsSelection</h5><p>Format: 2-byte bit field.</p><p>Title: Font selection flags.</p><p>Description: Contains information concerning the nature
          of the font patterns, as follows:</p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="8pc"/><col width="10pc"/></colgroup><thead><tr><th>Bit #</th><th>macStyle bit</th><th>C Definition</th><th>Description</th></tr></thead><tbody><tr><td>0</td><td>bit 1</td><td>ITALIC</td><td>Font contains Italic characters, otherwise they
                  are upright.</td></tr><tr><td>1</td><td> </td><td>UNDERSCORE</td><td>Characters are underscored.</td></tr><tr><td>2</td><td> </td><td>NEGATIVE</td><td>Characters have their foreground and background
                  reversed.</td></tr><tr><td>3</td><td> </td><td>OUTLINED</td><td>Outline (hollow) characters, otherwise they are
                  solid.</td></tr><tr><td>4</td><td> </td><td>STRIKEOUT</td><td>Characters are overstruck</td></tr><tr><td>5</td><td>bit 0</td><td>BOLD</td><td>Characters are emboldened.</td></tr><tr><td>6</td><td> </td><td>REGULAR</td><td>Characters are in the standard weight/style for
                  the font.</td></tr></tbody></table></div><p>Comments: All undefined bits must be zero.</p><p>This field contains information on the original design
          of the font. Bits 0 &amp; 5 can be used to determine if the font
          was designed with these features or whether some type of
          machine simulation was performed on the font to achieve this
          appearance. Bits 1-4 are rarely used bits that indicate the
          font is primarily a decorative or special purpose
          font.</p><p>If bit 6 is set, then bits 0 and 5 must be clear, else
          the behavior is undefined. As noted above, the settings of
          bits 0 and 1 must be reflected in the macStyle bits in the
          <a class="link" href="chapter.head.html" title="Chapter 5. head - Font Header">head</a> table. While bit 6 on implies that
          bits 0 and 1 of macStyle are clear (along with bits 0 and 5
          of fsSelection), the reverse is not true. Bits 0 and 1 of
          macStyle (and 0 and 5 of fsSelection) may be clear and that
          does not give any indication of whether or not bit 6 of
          fsSelection is clear (e.g., Arial Light would have all bits
          cleared; it is not the regular version of Arial). </p><h5><a name="idm363761609600"></a>usFirstCharIndex</h5><p>Format: 2-byte USHORT</p><p>Description: The minimum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and platform- specific encoding ID 0 or 1. For most fonts
          supporting Win-ANSI or other character sets, this value
          would be 0x0020. </p><h5><a name="idm363761608080"></a>usLastCharIndex</h5><p>Format: 2-byte USHORT</p><p>Description: The maximum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and encoding ID 0 or 1. This value depends on which
          character sets the font supports. </p><h5><a name="idm363761606640"></a>sTypoAscender</h5><p>Format: SHORT</p><p>Description: The typographic ascender for this font.
          Remember that this is not the same as the Ascender value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoAscender in
          Latin based fonts is the Ascender value from an AFM file.
          For CJK fonts see below.</p><p>The suggested usage for sTypoAscender is that it be used
          in conjunction with unitsPerEm to compute a typographically
          correct default line spacing. The goal is to free
          applications from Macintosh or Windows-specific metrics
          which are constrained by backward compatibility
          requirements. These new metrics, when combined with the
          character design widths, will allow applications to lay out
          documents in a typographically correct and portable fashion.
          These metrics will be exposed through Windows APIs.
          Macintosh applications will need to access the 'sfnt'
          resource and parse it to extract this data from the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table.</p><p>For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoAscender is
          that which describes the top of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoAscender must be set to
          880. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p>Also see the Recommendations Section for more on this
          field. </p><h5><a name="idm363761601936"></a>sTypoDescender</h5><p>Format: SHORT</p><p>Description: The typographic descender for this font.
          Remember that this is not the same as the Descender value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoDescender in
          Latin based fonts is the Descender value from an AFM file.
          For CJK fonts see below.</p><p>The suggested usage for sTypoDescender is that it be
          used in conjunction with unitsPerEm to compute a
          typographically correct default line spacing. The goal is to
          free applications from Macintosh or Windows-specific metrics
          which are constrained by backward compatability
          requirements. These new metrics, when combined with the
          character design widths, will allow applications to lay out
          documents in a typographically correct and portable fashion.
          These metrics will be exposed through Windows APIs.
          Macintosh applications will need to access the 'sfnt'
          resource and parse it to extract this data from the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes the
          <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API).</p><p>For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoDescender
          is that which describes the bottom of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoDescender must be set to
          -120. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p>Also see the Recommendations Section for more on this
          field. </p><h5><a name="idm363761595808"></a>sTypoLineGap</h5><p>Format: 2-byte SHORT</p><p>Description: The typographic line gap for this font.
          Remember that this is not the same as the LineGap value in
          the <a class="link" href="chapter.hhea.html" title="Chapter 6. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner.</p><p>The suggested usage for usTypoLineGap is that it be used
          in conjunction with unitsPerEm to compute a typographically
          correct default line spacing. Typical values average 7-10%
          of units per em. The goal is to free applications from
          Macintosh or Windows-specific metrics which are constrained
          by backward compatability requirements (see chapter,
          "Recommendations for Windows Fonts). These new metrics, when
          combined with the character design widths, will allow
          applications to lay out documents in a typographically
          correct and portable fashion. These metrics will be exposed
          through Windows APIs. Macintosh applications will need to
          access the 'sfnt' resource and parse it to extract this data
          from the <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes
          the <a class="link" href="chapter.OS2.html" title="Chapter 10. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API) </p><h5><a name="idm363761592000"></a>usWinAscent</h5><p>Format: 2-byte USHORT</p><p>Description: The ascender metric for Windows. This, too,
          is distinct from Apple's Ascender value and from the
          usTypoAscender values. usWinAscent is computed as the yMax
          for all characters in the Windows ANSI character set.
          usWinAscent is used to compute the Windows font height and
          default line spacing. For platform 3 encoding 0 fonts, it is
          the same as yMax. Windows will clip the bitmap of any
          portion of a glyph that appears above this value. Some
          applications use this value to determine default line
          spacing. This is strongly discouraged. The typographic
          ascender, descender and line gap fields in conjunction with
          unitsPerEm should be used for this purpose. Developers
          should set this field keeping the above factors in
          mind.</p><p>If any clipping is unacceptable, then the value should
          be set to yMax.</p><p>However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against CommonType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped.</p><h5><a name="idm363761588704"></a>usWinDescent</h5><p>Format: 2-byte USHORT</p><p>Description: The descender metric for Windows. This,
          too, is distinct from Apple's Descender value and from the
          usTypoDescender values. usWinDescent is computed as the
          -yMin for all characters in the Windows ANSI character set.
          usWinDescent is used to compute the Windows font height and
          default line spacing. For platform 3 encoding 0 fonts, it is
          the same as -yMin. Windows will clip the bitmap of any
          portion of a glyph that appears below this value. Some
          applications use this value to determine default line
          spacing. This is strongly discouraged. The typographic
          ascender, descender and line gap fields in conjunction with
          unitsPerEm should be used for this purpose. Developers
          should set this field keeping the above factors in
          mind.</p><p>If any clipping is unacceptable, then the value should
          be set to yMin.</p><p>However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against CommonType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped. </p><h5><a name="idm363761585392"></a>ulCodePageRange1 Bits 0-31</h5><h5><a name="idm363761584976"></a>ulCodePageRange2 Bits 32-63 </h5><p>Format: 32-bit unsigned long(2 copies) totaling 64
          bits.</p><p>Title: Code Page Character Range</p><p>Description: This field is used to specify the code
          pages encompassed by the font file in the <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable
          for platform 3, encoding ID 1 (Microsoft platform). If the
          font file is encoding ID 0, then the Symbol Character Set
          bit should be set. If the bit is set (1) then the code page
          is considered functional. If the bit is clear (0) then the
          code page is not considered functional. Each of the bits is
          treated as an independent flag and the bits can be set in
          any combination. The determination of "functional" is left
          up to the font designer, although character set selection
          should attempt to be functional by code pages if at all
          possible.</p><p>Symbol character sets have a special meaning. If the
          symbol bit (31) is set, and the font file contains a <a class="link" href="chapter.cmap.html" title="Chapter 4. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform of 3 and encoding ID of 1, then all of
          the characters in the Unicode range 0xF000 - 0xF0FF
          (inclusive) will be used to enumerate the symbol character
          set. If the bit is not set, any characters present in that
          range will not be enumerated as a symbol character
          set.</p><p>All reserved fields must be zero. Each long is in
          Big-Endian form. </p><div class="informaltable"><table class="informaltable" border="1"><colgroup><col width="6pc"/><col width="6pc"/><col width="18pc"/></colgroup><thead><tr><th>Bit</th><th>Code</th><th>Page Description</th></tr></thead><tbody><tr><td>0</td><td>1252</td><td>Latin 1</td></tr><tr><td>1</td><td>1250</td><td>Latin 2: Eastern Europe</td></tr><tr><td>2</td><td>1251</td><td>Cyrillic</td></tr><tr><td>3</td><td>1253</td><td>Greek</td></tr><tr><td>4</td><td>1254</td><td>Turkish</td></tr><tr><td>5</td><td>1255</td><td>Hebrew</td></tr><tr><td>6</td><td>1256</td><td>Arabic</td></tr><tr><td>7</td><td>1257</td><td>Windows Baltic</td></tr><tr><td>8</td><td>1258</td><td>Vietnamese</td></tr><tr><td>9-15</td><td> </td><td>Reserved for Alternate ANSI</td></tr><tr><td>16</td><td>874</td><td>Thai</td></tr><tr><td>17</td><td>932</td><td>JIS/Japan</td></tr><tr><td>18</td><td>936</td><td>Chinese: Simplified chars--PRC and
                  Singapore</td></tr><tr><td>19</td><td>949</td><td>Korean Wansung</td></tr><tr><td>20</td><td>950</td><td>Chinese: Traditional chars--Taiwan and Hong
                  Kong</td></tr><tr><td>21</td><td>1361</td><td>Korean Johab</td></tr><tr><td>22-28</td><td> </td><td>Reserved for Alternate ANSI &amp; OEM</td></tr><tr><td>29</td><td> </td><td>Macintosh Character Set (US Roman)</td></tr><tr><td>30</td><td> </td><td>OEM Character Set</td></tr><tr><td>31</td><td> </td><td>Symbol Character Set</td></tr><tr><td>32-47</td><td> </td><td>Reserved for OEM</td></tr><tr><td>48</td><td>869</td><td>IBM Greek</td></tr><tr><td>49</td><td>866</td><td>MS-DOS Russian</td></tr><tr><td>50</td><td>865</td><td>MS-DOS Nordic</td></tr><tr><td>51</td><td>864</td><td>Arabic</td></tr><tr><td>52</td><td>863</td><td>MS-DOS Canadian French</td></tr><tr><td>53</td><td>862</td><td>Hebrew</td></tr><tr><td>54</td><td>861</td><td>MS-DOS Icelandic</td></tr><tr><td>55</td><td>860</td><td>MS-DOS Portuguese</td></tr><tr><td>56</td><td>857</td><td>IBM Turkish</td></tr><tr><td>57</td><td>855</td><td>IBM Cyrillic; primarily Russian</td></tr><tr><td>58</td><td>852</td><td>Latin 2</td></tr><tr><td>59</td><td>775</td><td>MS-DOS Baltic</td></tr><tr><td>60</td><td>737</td><td>Greek; former 437 G</td></tr><tr><td>61</td><td>708</td><td>Arabic; ASMO 708</td></tr><tr><td>62</td><td>850</td><td>WE/Latin 1</td></tr><tr><td>63</td><td>437</td><td>US</td></tr></tbody></table></div><h5><a name="idm363761517888"></a>sxHeight</h5><p>Format: SHORT</p><p>Description: This metric specifies the distance between
          the baseline and the approximate height of non-ascending
          lowercase letters measured in FUnits. This value would
          normally be specified by a type designer but in situations
          where that is not possible, for example when a legacy font
          is being converted, the value may be set equal to the top of
          the unscaled and unhinted glyph bounding box of the glyph
          encoded at U+0078 (LATIN SMALL LETTER X). If no glyph is
          encoded in this position the field should be set to
          0.</p><p>This metric, if specified, can be used in font
          substitution: the xHeight value of one font can be scaled to
          approximate the apparent size of another. </p><h5><a name="idm363761515536"></a>sCapHeight</h5><p>Format: SHORT</p><p>Description: This metric specifies the distance between
          the baseline and the approximate height of uppercase letters
          measured in FUnits. This value would normally be specified
          by a type designer but in situations where that is not
          possible, for example when a legacy font is being converted,
          the value may be set equal to the top of the unscaled and
          unhinted glyph bounding box of the glyph encoded at U+0048
          (LATIN CAPITAL LETTER H). If no glyph is encoded in this
          position the field should be set to 0.</p><p>This metric, if specified, can be used in systems that
          specify type size by capital height measured in millimeters.
          It can also be used as an alignment metric; the top of a
          drop capital, for instance, can be aligned to the sCapHeight
          metric of the first line of text. </p><h5><a name="idm363761513056"></a>usDefaultChar</h5><p>Format: USHORT</p><p>Description: Whenever a request is made for a character
          that is not in the font, Windows provides this default
          character. If the value of this field is zero, glyph ID 0 is
          to be used for the default character otherwise this is the
          Unicode encoding of the glyph that Windows uses as the
          default character. </p><h5><a name="idm363761511504"></a>usBreakChar</h5><p>Format: USHORT</p><p>Description: This is the Unicode encoding of the glyph
          that Windows uses as the break character. The break
          character is used to separate words and justify text. Most
          fonts specify 'space' as the break character.</p><h5><a name="idm363761510064"></a>usMaxContext</h5><p>Format: USHORT</p><p>Description: The maximum length of a target glyph
          context for any feature in this font. For example, a font
          which has only a pair kerning feature should set this field
          to 2. If the font also has a ligature feature in which the
          glyph sequence 'f f i' is substituted by the ligature 'ffi',
          then this field should be set to 3. This field could be
          useful to sophisticated line-breaking engines in determining
          how far they should look ahead to test whether something
          could change that effects the line breaking. For chaining
          contextual lookups, the length of the string (covered glyph)
          + (input sequence) + (lookahead sequence) should be
          considered.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.11.1.3"></a>Annotation</h4></div></div></div><p>Note that the usFirstCharIndex and usLastCharIndex are
        no longer very useful, since these fields are not big enough
        to represent Unicode supplemental characters.</p></div></div></div>