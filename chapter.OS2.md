<div xmlns="http://www.w3.org/1999/xhtml" role="" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.OS2"></a>Chapter 11. OS/2 - OS/2 and Windows Metrics</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h2 class="title" style="clear: both"><a name="idm320134349488"></a>Introduction</h2></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.11.1.1"></a>Specification</h3></div></div></div><p role="">The OS/2 table consists of a set of metrics that are
          required in OpenType fonts. The fourth version of the OS/2
          table (version 3) follows:</p><div class="table"><a name="idm320134347296"></a><p class="title"><strong>Table 11.1. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">0x0003</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xAvgCharWidth</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWeightClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWidthClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">fsType</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptXSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptYSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptXOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptYOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptXSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptYSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptXOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptYOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yStrikeoutSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yStrikeoutPosition</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sFamilyClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">panose[10]</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange1</td><td role="">Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange2</td><td role="">Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange3</td><td role="">Bits 64-95</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange4</td><td role="">Bits 96-127</td><td class="auto-generated"> </td></tr><tr><td role="">CHAR</td><td role="">achVendID[4]</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">fsSelection</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usFirstCharIndex</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usLastCharIndex</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoAscender</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoDescender</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoLineGap</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWinAscent</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWinDescent</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulCodePageRange1</td><td role="">Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulCodePageRange2</td><td role="">Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sxHeight</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sCapHeight</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usDefaultChar</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usBreakChar</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usMaxContext</td><td role=""> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><h4><a name="idm320133301744"></a>version</h4><p role="">Format: 2-byte unsigned short</p><p role="">Units: n/a</p><p role="">Title: OS/2 table version number.</p><p role="">Description: The version number for this OS/2
          table.</p><p role="">Comments: The version number allows for identification
          of the precise contents and layout for the OS/2 table. The
          version number for this layout is three (3). Versions zero
          (0, TrueType rev 1.5), one (1, TrueType rev 1.66) and two
          (2, OpenType rev 1.2) have been used previously.</p><h4><a name="idm320133298944"></a>xAvgCharWidth</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Pels / em units</p><p role="">Title: Average weighted escapement.</p><p role="">Description: The Average Character Width parameter
          specifies the arithmetic average of the escapement (width)
          of all non-zero width glyphs in the font.</p><p role="">Comments: The value of xAvgCharWidth is calculated by
	  obtaining the arithmetic average of the width of all
	  non-zero width glyphs in the font. Furthermore, it is
	  strongly recommended that implementers do not rely on this
	  value for computing layout for lines of text. Especially,
	  for cases where complex scripts are used.</p><h4><a name="idm320135204528"></a>usWeightClass</h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Weight class. </p><p role="">Description: Indicates the visual weight (degree of
          blackness or thickness of strokes) of the characters in the
          font. </p><p role="">Comments:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="18pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th><th role="">C Definition (from windows.h)</th></tr></thead><tbody><tr><td role="">100</td><td role="">Thin</td><td role="">FW_THIN</td></tr><tr><td role="">200</td><td role="">Extra-light (Ultra-light)</td><td role="">FW_EXTRALIGHT</td></tr><tr><td role="">300</td><td role="">Light</td><td role="">FW_LIGHT</td></tr><tr><td role="">400</td><td role="">Normal (Regular)</td><td role="">FW_NORMAL</td></tr><tr><td role="">500</td><td role="">Medium</td><td role="">FW_MEDIUM</td></tr><tr><td role="">600</td><td role="">Semi-bold (Demi-bold)</td><td role="">FW_SEMIBOLD</td></tr><tr><td role="">700</td><td role="">Bold</td><td role="">FW_BOLD</td></tr><tr><td role="">800</td><td role="">Extra-bold (Ultra-bold)</td><td role="">FW_EXTRABOLD</td></tr><tr><td role="">900</td><td role="">Black (Heavy)</td><td role="">FW_BLACK</td></tr></tbody></table></div><h4><a name="idm320135183280"></a>usWidthClass </h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Width class. </p><p role="">Description: Indicates a relative change from the normal
          aspect ratio (width to height ratio) as specified by a font
          designer for the glyphs in a font. </p><p role="">Comments:  Although every character in a font may have a
          different numeric aspect ratio, each character in a font of
          normal width has a relative aspect ratio of one. When a new
          type style is created of a different width class (either by
          a font designer or by some automated means) the relative
          aspect ratio of the characters in the new font is some
          percentage greater or less than those same characters in the
          normal font -- it is this difference that this parameter
          specifies. </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="14pc"/><col width="4pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th><th role="">C Definition</th><th role="">% of normal</th></tr></thead><tbody><tr><td role="">1</td><td role="">Ultra-condensed</td><td role="">FWIDTH_ULTRA_CONDENSED</td><td role="">50</td></tr><tr><td role="">2</td><td role="">Extra-condensed</td><td role="">FWIDTH_EXTRA_CONDENSED</td><td role="">62.5</td></tr><tr><td role="">3</td><td role="">Condensed</td><td role="">FWIDTH_CONDENSED</td><td role="">75</td></tr><tr><td role="">4</td><td role="">Semi-condensed</td><td role="">FWIDTH_SEMI_CONDENSED</td><td role="">87.5</td></tr><tr><td role="">5</td><td role="">Medium (normal)</td><td role="">FWIDTH_NORMAL</td><td role="">100</td></tr><tr><td role="">6</td><td role="">Semi-expanded</td><td role="">FWIDTH_SEMI_EXPANDED</td><td role="">112.5</td></tr><tr><td role="">7</td><td role="">Expanded</td><td role="">FWIDTH_EXPANDED</td><td role="">125</td></tr><tr><td role="">8</td><td role="">Extra-expanded</td><td role="">FWIDTH_EXTRA_EXPANDED</td><td role="">150</td></tr><tr><td role="">9</td><td role="">Ultra-expanded</td><td role="">FWIDTH_ULTRA_EXPANDED</td><td role="">200</td></tr></tbody></table></div><h4><a name="idm320135157104"></a>fsType</h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Type flags. </p><p role="">Description: Indicates font embedding licensing rights
          for the font. Embeddable fonts may be stored in a document.
          When a document with embedded fonts is opened on a system
          that does not have the font installed (the remote system),
          the embedded font may be loaded for temporary (and in some
          cases, permanent) use on that system by an embedding-aware
          application. Embedding licensing rights are granted by the
          vendor of the font.</p><p role="">The OpenType Font Embedding DLL Specification and DLL
          release notes describe the APIs used to implement support
          for OpenType font embedding and loading.
          <span role="" class="emphasis"><em>Applications that implement support for font
            embedding, either through use of the Font Embedding DLL or
            through other means, must not embed fonts which are not
            licensed to permit embedding. Further, applications
            loading embedded fonts for temporary use (see Preview
            &amp; Print and Editable embedding below) must delete the
            fonts when the document containing the embedded font is
            closed.</em></span></p><p role="">This version of the OS/2 table makes bits 0 - 3 a set of
	  exclusive bits. In other words, at most one bit in this
	  range may be set at a time. The purpose is to remove
	  misunderstandings caused by previous behavior of using the
	  least restrictive of the bits that are set.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="1cm"/><col width="2cm"/><col width="10cm"/></colgroup><thead><tr><th role="">Bit</th><th role="">BitMask</th><th role="">Description</th></tr></thead><tbody><tr><td role=""> </td><td role="">0x0000</td><td role="">Installable Embedding: No fsType bit is set.
                  Thus fsType is zero. Fonts with this setting
                  indicate that they may be embedded and permanently
                  installed on the remote system by an application.
                  The user of the remote system acquires the identical
                  rights, obligations and licenses for that font as
                  the original purchaser of the font, and is subject
                  to the same end-user license agreement, copyright,
                  design patent, and/or trademark as was the original
                  purchaser.</td></tr><tr><td role="">0</td><td role="">0x0001</td><td role="">Reserved, must be zero.</td></tr><tr><td role="">1</td><td role="">0x0002</td><td role="">Restricted License embedding: Fonts that have
                  <span role="" class="emphasis"><em>only</em></span> this bit set must not be
                  <span role="" class="emphasis"><em>modified, embedded or exchanged in any
                    manner</em></span> without first obtaining
                  permission of the legal owner. Caution: For
                  Restricted License embedding to take effect, it must
                  be the only level of embedding selected.</td></tr><tr><td role="">2</td><td role="">0x0004</td><td role="">Preview &amp; Print embedding: When this bit is
                  set, the font may be embedded, and temporarily
                  loaded on the remote system. Documents containing
                  Preview &amp; Print fonts must be opened "read-only;" no
                  edits can be applied to the document.</td></tr><tr><td role="">3</td><td role="">0x0008</td><td role="">Editable embedding: When this bit is set, the
                  font may be embedded but must only be installed
                  <span role="" class="emphasis"><em>temporarily</em></span> on other systems.
                  In contrast to Preview &amp; Print fonts, documents
                  containing Editable fonts <span role="" class="emphasis"><em>may</em></span>
                  be opened for reading, editing is permitted, and
                  changes may be saved.</td></tr><tr><td role="">4-7</td><td role=""> </td><td role="">Reserved, must be zero.</td></tr><tr><td role="">8</td><td role="">0x0100</td><td role="">No subsetting: When this bit is set, the font
                  may not be subsetted prior to embedding. Other
                  embedding restrictions specified in bits 0-3 and 9
                  also apply.</td></tr><tr><td role="">9</td><td role="">0x0200</td><td role="">Bitmap embedding only: When this bit is set,
                  only bitmaps contained in the font may be embedded.
                  No outline data may be embedded. If there are no
                  bitmaps available in the font, then the font is
                  considered unembeddable and the embedding services
                  will fail. Other embedding restrictions specified in
                  bits 0-3 and 8 also apply.</td></tr><tr><td role="">10-15</td><td role=""> </td><td role="">Reserved, must be zero.</td></tr></tbody></table></div><h4><a name="idm320135129936"></a>ySubscriptXSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript horizontal font size. </p><p role="">Description: The recommended horizontal size in font
          design units for subscripts for this font.  </p><p role="">Comments: If a font has two recommended sizes for
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
          subscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySubScriptXSize is set to 205, then the horizontal size for
          a simulated subscript character would be 1/10th the size of
          the normal character.</p><h4><a name="idm320135126000"></a>ySubscriptYSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript vertical font size. </p><p role="">Description: The recommended vertical size in font
          design units for subscripts for this font.  </p><p role="">Comments: If a font has two recommended sizes for
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
          those subscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySubScriptYSize is set to 205, then the vertical size for a
          simulated subscript character would be 1/10th the size of
          the normal character.</p><h4><a name="idm320135122080"></a>ySubscriptXOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript x offset.</p><p role="">Description: The recommended horizontal offset in font
          design untis for subscripts for this font. </p><p role="">Comments: The Subscript X Offset parameter specifies a
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
          the angle of incline.</p><h4><a name="idm320135118624"></a>ySubscriptYOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript y offset. </p><p role="">Description: The recommended vertical offset in font
          design units from the baseline for subscripts for this font.
        </p><p role="">Comments: The Subscript Y Offset parameter specifies a
          font designer's recommended vertical offset from the
          character baseline to the character baseline for subscript
          characters associated with this font. Values are expressed
          as a positive offset below the character baseline. If a font
          does not include all of the required subscript for an
          application, this parameter specifies the recommended
          vertical distance below the character baseline for those
          subscript characters.</p><h4><a name="idm320133296592"></a>ySuperscriptXSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript horizontal font size.</p><p role="">Description: The recommended horizontal size in font
          design units for superscripts for this font. </p><p role="">Comments: If a font has two recommended sizes for
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
          square for those superscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySuperScriptXSize is set to 205, then the horizontal size
          for a simulated superscript character would be 1/10th the
          size of the normal character.</p><h4><a name="idm320133292640"></a>ySuperscriptYSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript vertical font size.</p><p role="">Description: The recommended vertical size in font
          design units for superscripts for this font. </p><p role="">Comments: If a font has two recommended sizes for
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
          characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySuperScriptYSize is set to 205, then the vertical size for
          a simulated superscript character would be 1/10th the size
          of the normal character.</p><h4><a name="idm320133288688"></a>ySuperscriptXOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript x offset.</p><p role="">Description: The recommended horizontal offset in font
          design units for superscripts for this font. </p><p role="">Comments: The Superscript X Offset parameter specifies a
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
          adjusted to compensate for the angle of incline.</p><h4><a name="idm320133285328"></a>ySuperscriptYOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript y offset.</p><p role="">Description: The recommended vertical offset in font
          design units from the baseline for superscripts for this
          font. </p><p role="">Comments: The Superscript Y Offset parameter specifies a
          font designer's recommended vertical offset -- from the
          character baseline to the superscript character's baseline
          associated with this font. Values for this parameter are
          expressed as a positive offset above the character baseline.
          If a font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended vertical distance above the character baseline
          for those superscript characters.</p><h4><a name="idm320133282160"></a>yStrikeoutSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Strikeout size.</p><p role="">Description: Width of the strikeout stroke in font
          design units. </p><p role="">Comments: This field should normally be the width of the
          em dash for the current font. If the size is one, the
          strikeout line will be the line represented by the strikeout
          position field. If the value is two, the strikeout line will
          be the line represented by the strikeout position and the
          line immediately above the strikeout position. For a Roman
          font with a 2048 em square, 102 is suggested.</p><h4><a name="idm320133279200"></a>yStrikeoutPosition</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Strikeout position.</p><p role="">Description: The position of the top of the strikeout
          stroke relative to the baseline in font design units.
        </p><p role="">Comments: Positive values represent distances above the
          baseline, while negative values represent distances below
          the baseline. A value of zero falls directly on the
          baseline, while a value of one falls one pel above the
          baseline. The value of strikeout position should not
          interfere with the recognition of standard characters, and
          therefore should not line up with crossbars in the font. For
          a Roman font with a 2048 em square, 460 is suggested.</p><h4><a name="idm320133276112"></a>sFamilyClass</h4><p role="">Format: 2-byte signed short</p><p role="">Title: Font-family class and subclass.</p><p role="">Description: This parameter is a classification of
          font-family design. </p><p role="">Comments: The font class and font subclass are
          registered values assigned by IBM to each font family. This
          parameter is intended for use in selecting an alternate font
          when the requested font is not available. The font class is
          the most general and the font subclass is the most specific.
          The high byte of this field contains the family class, while
          the low byte contains the family subclass. More information
          about this field.  </p><h4><a name="idm320133272992"></a>Panose</h4><p role="">Format: 10 byte array</p><p role="">Title: PANOSE classification number</p><p role="">International: Additional specifications are required
          for PANOSE to classify non-Latin character sets.</p><p role="">Description: This 10 byte series of numbers is used to
          describe the visual characteristics of a given typeface.
          These characteristics are then used to associate the font
          with other fonts of similar appearance having different
          names. The variables for each digit are listed below. The
          Panose values are fully described in the Panose "greybook"
          reference, currently owned by Agfa-Monotype. </p><p role="">Comments: The PANOSE definition contains ten digits each
          of which currently describes up to sixteen variations.
          Windows uses bFamilyType, bSerifStyle and bProportion in the
          font mapper to determine family type. It also uses
          bProportion to determine if the font is monospaced. If the
          font is a symbol font, the first byte of the PANOSE number
          (bFamilyType) must be set to "pictorial." Good PANOSE values
          in fonts are very valuable to users of the Windows fonts
          folder. The specification for assigning PANOSE values is
          located at <a role="" class="ulink" href="http://www.panose.com/hardware/pan2.asp" target="_top">http://www.panose.com/hardware/pan2.asp</a>.</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th></tr></thead><tbody><tr><td role="">BYTE</td><td role="">bFamilyType</td></tr><tr><td role="">BYTE</td><td role="">bSerifStyle</td></tr><tr><td role="">BYTE</td><td role="">bWeight</td></tr><tr><td role="">BYTE</td><td role="">bProportion;</td></tr><tr><td role="">BYTE</td><td role="">bContrast</td></tr><tr><td role="">BYTE</td><td role="">bStrokeVariation</td></tr><tr><td role="">BYTE</td><td role="">bArmStyle</td></tr><tr><td role="">BYTE</td><td role="">bLetterform</td></tr><tr><td role="">BYTE</td><td role="">bMidline</td></tr><tr><td role="">BYTE</td><td role="">bXHeight</td></tr></tbody></table></div><h4><a name="idm320133252912"></a>ulUnicodeRange1 (Bits 0-31)</h4><h4><a name="idm320133252496"></a>ulUnicodeRange2 (Bits 32-63)</h4><h4><a name="idm320133252080"></a>ulUnicodeRange3 (Bits 64-95)</h4><h4><a name="idm320133251664"></a>ulUnicodeRange4 (Bits 96-127)</h4><p role="">Format: 32-bit unsigned long(4 copies) totaling 128
          bits.</p><p role="">Title: Unicode Character Range</p><p role="">Description: This field is used to specify the Unicode
          blocks or ranges encompassed by the font file in the <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform 3, encoding ID 1 (Microsoft platform).
          If the bit is set (1) then the Unicode range is considered
          functional. If the bit is clear (0) then the range is not
          considered functional. Each of the bits is treated as an
          independent flag and the bits can be set in any combination.
          The determination of "functional" is left up to the font
          designer, although character set selection should attempt to
          be functional by ranges if at all possible.</p><p role="">All reserved fields must be zero. Each long is in Big-Endian
          form. See the Basic Multilingual Plane of ISO/IEC 10646-1 or
          the Unicode Standard v.3.0 for the list of Unicode ranges
          and characters.  </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Bit</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">Basic Latin</td></tr><tr><td role="">1</td><td role="">Latin-1 Supplement</td></tr><tr><td role="">2</td><td role="">Latin Extended-A</td></tr><tr><td role="">3</td><td role="">Latin Extended-B</td></tr><tr><td role="">4</td><td role="">IPA Extensions</td></tr><tr><td role="">5</td><td role="">Spacing Modifier Letters</td></tr><tr><td role="">6</td><td role="">Combining Diacritical Marks</td></tr><tr><td role="">7</td><td role="">Greek and Coptic</td></tr><tr><td role="">8</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">9</td><td role="">Cyrillic</td></tr><tr><td role=""> </td><td role="">Cyrillic Supplementary</td></tr><tr><td role="">10</td><td role="">Armenian</td></tr><tr><td role="">11</td><td role="">Hebrew</td></tr><tr><td role="">12</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">13</td><td role="">Arabic</td></tr><tr><td role="">14</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">15</td><td role="">Devanagari</td></tr><tr><td role="">16</td><td role="">Bengali</td></tr><tr><td role="">17</td><td role="">Gurmukhi</td></tr><tr><td role="">18</td><td role="">Gujarati</td></tr><tr><td role="">19</td><td role="">Oriya</td></tr><tr><td role="">20</td><td role="">Tamil</td></tr><tr><td role="">21</td><td role="">Telugu</td></tr><tr><td role="">22</td><td role="">Kannada</td></tr><tr><td role="">23</td><td role="">Malayalam</td></tr><tr><td role="">24</td><td role="">Thai</td></tr><tr><td role="">25</td><td role="">Lao</td></tr><tr><td role="">26</td><td role="">Georgian</td></tr><tr><td role="">27</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">28</td><td role="">Hangul Jamo</td></tr><tr><td role="">29</td><td role="">Latin Extended Additional</td></tr><tr><td role="">30</td><td role="">Greek Extended</td></tr><tr><td role="">31</td><td role="">General Punctuation</td></tr><tr><td role="">32</td><td role="">Superscripts And Subscripts</td></tr><tr><td role="">33</td><td role="">Currency Symbols</td></tr><tr><td role="">34</td><td role="">Combining Diacritical Marks For Symbols</td></tr><tr><td role="">35</td><td role="">Letterlike Symbols</td></tr><tr><td role="">36</td><td role="">Number Forms</td></tr><tr><td role="">37</td><td role="">Arrows</td></tr><tr><td role=""> </td><td role="">Supplemental Arrows-A</td></tr><tr><td role=""> </td><td role="">Supplemental Arrows-B</td></tr><tr><td role="">38</td><td role="">Mathematical Operators</td></tr><tr><td role=""> </td><td role="">Supplemental Mathematical Operators</td></tr><tr><td role=""> </td><td role="">Miscellaneous Mathematical Symbols-A</td></tr><tr><td role=""> </td><td role="">Miscellaneous Mathematical Symbols-B</td></tr><tr><td role="">39</td><td role="">Miscellaneous Technical</td></tr><tr><td role="">40</td><td role="">Control Pictures</td></tr><tr><td role="">41</td><td role="">Optical Character Recognition</td></tr><tr><td role="">42</td><td role="">Enclosed Alphanumerics</td></tr><tr><td role="">43</td><td role="">Box Drawing</td></tr><tr><td role="">44</td><td role="">Block Elements</td></tr><tr><td role="">45</td><td role="">Geometric Shapes</td></tr><tr><td role="">46</td><td role="">Miscellaneous Symbols</td></tr><tr><td role="">47</td><td role="">Dingbats</td></tr><tr><td role="">48</td><td role="">CJK Symbols And Punctuation</td></tr><tr><td role="">49</td><td role="">Hiragana</td></tr><tr><td role="">50</td><td role="">Katakana</td></tr><tr><td role=""> </td><td role="">Katakana Phonetic Extensions</td></tr><tr><td role="">51</td><td role="">Bopomofo</td></tr><tr><td role=""> </td><td role="">Bopomofo Extended</td></tr><tr><td role=""> </td><td role="">  Extended Bopomofo</td></tr><tr><td role="">52</td><td role="">Hangul Compatibility Jamo</td></tr><tr><td role="">53</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">54</td><td role="">Enclosed CJK Letters And Months</td></tr><tr><td role="">55</td><td role="">CJK Compatibility</td></tr><tr><td role="">56</td><td role="">Hangul Syllables</td></tr><tr><td role="">57</td><td role="">Non-Plane 0<a href="#ftn.idm320133167008" class="footnote" id="idm320133167008"><sup class="footnote">[a]</sup></a></td></tr><tr><td role="">58</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">59</td><td role="">CJK Unified Ideographs</td></tr><tr><td role=""> </td><td role="">CJK Radicals Supplement</td></tr><tr><td role=""> </td><td role="">Kangxi Radicals</td></tr><tr><td role=""> </td><td role="">Ideographic Description Characters</td></tr><tr><td role=""> </td><td role="">CJK Unified Ideograph Extension A</td></tr><tr><td role=""> </td><td role="">CJK Unified Ideograph Extension B</td></tr><tr><td role=""> </td><td role="">Kanbun</td></tr><tr><td role="">60</td><td role="">Private Use Area</td></tr><tr><td role="">61</td><td role="">CJK Compatibility Ideographs</td></tr><tr><td role=""> </td><td role="">CJK Compatibility Ideographs Supplement</td></tr><tr><td role="">62</td><td role="">Alphabetic Presentation Forms</td></tr><tr><td role="">63</td><td role="">Arabic Presentation Forms-A</td></tr><tr><td role="">64</td><td role="">Combining Half Marks</td></tr><tr><td role="">65</td><td role="">CJK Compatibility Forms</td></tr><tr><td role="">66</td><td role="">Small Form Variants</td></tr><tr><td role="">67</td><td role="">Arabic Presentation Forms-B</td></tr><tr><td role="">68</td><td role="">Halfwidth And Fullwidth Forms</td></tr><tr><td role="">69</td><td role="">Specials</td></tr><tr><td role="">70</td><td role="">Tibetan</td></tr><tr><td role="">71</td><td role="">Syriac</td></tr><tr><td role="">72</td><td role="">Thaana</td></tr><tr><td role="">73</td><td role="">Sinhala</td></tr><tr><td role="">74</td><td role="">Myanmar</td></tr><tr><td role="">75</td><td role="">Ethiopic</td></tr><tr><td role="">76</td><td role="">Cherokee</td></tr><tr><td role="">77</td><td role="">Unified Canadian Aboriginal Syllabics</td></tr><tr><td role="">78</td><td role="">Ogham</td></tr><tr><td role="">79</td><td role="">Runic</td></tr><tr><td role="">80</td><td role="">Khmer</td></tr><tr><td role="">81</td><td role="">Mongolian</td></tr><tr><td role="">82</td><td role="">Braille Patterns</td></tr><tr><td role="">83</td><td role="">Yi Syllables</td></tr><tr><td role=""> </td><td role="">Yi Radicals</td></tr><tr><td role="">84</td><td role="">Tagalog</td></tr><tr><td role=""> </td><td role="">Hanunoo</td></tr><tr><td role=""> </td><td role="">Buhid</td></tr><tr><td role=""> </td><td role="">Tagbanwa</td></tr><tr><td role="">85</td><td role="">Old Italic</td></tr><tr><td role="">86</td><td role="">Gothic</td></tr><tr><td role="">87</td><td role="">Deseret</td></tr><tr><td role="">88</td><td role="">Byzantine Musical Symbols</td></tr><tr><td role=""> </td><td role="">Musical Symbols</td></tr><tr><td role="">89</td><td role="">Mathematical Alphanumeric Symbols</td></tr><tr><td role="">90</td><td role="">Private Use (plane 15)</td></tr><tr><td role=""> </td><td role="">Private Use (plane 16)</td></tr><tr><td role="">91</td><td role="">Variation Selectors</td></tr><tr><td role="">92</td><td role="">Tags</td></tr><tr><td role="">93-127</td><td role="">Reserved for Unicode SubRanges</td></tr></tbody><tbody class="footnotes"><tr><td colspan="2"><div id="ftn.idm320133167008" role="" class="footnote"><p role=""><a href="#idm320133167008" class="para"><sup class="para">[a] </sup></a>Setting bit 57 implies that there is
                      at least one codepoint beyond the Basic
                      Multilingual Plane that is supported by this
                      font.</p></div></td></tr></tbody></table></div><h4><a name="idm320133109456"></a>achVendID</h4><p role="">Format: 4-byte character array</p><p role="">Title: Font Vendor Identification</p><p role="">Description: The four character identifier for the
          vendor of the given type face.</p><p role="">Comments: This is not the royalty owner of the original
          artwork. This is the company responsible for the marketing
          and distribution of the typeface that is being classified.
          It is reasonable to assume that there will be 6 vendors of
          ITC Zapf Dingbats for use on desktop platforms in the near
          future (if not already). It is also likely that the vendors
          will have other inherent benefits in their fonts (more kern
          pairs, unregularized data, hand hinted, etc.). This
          identifier will allow for the correct vendor's type to be
          used over another, possibly inferior, font file. The Vendor
          ID value is not required.</p><p role="">Microsoft has assigned values for some font suppliers as
          listed below. Uppercase vendor ID's are reserved by
          Microsoft. Other suppliers can choose their own mixed case
          or lowercase ID's, or leave the field blank.</p><p role="">For a list of registered Vendor id's see our <a role="" class="ulink" href="http://www.microsoft.com/typography/links/vendorlist.asp" target="_top">Registered
            'vendors'</a> links page.</p><h4><a name="idm320133104816"></a>fsSelection</h4><p role="">Format: 2-byte bit field.</p><p role="">Title: Font selection flags.</p><p role="">Description: Contains information concerning the nature
          of the font patterns, as follows:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="8pc"/><col width="10pc"/></colgroup><thead><tr><th role="">Bit #</th><th role="">macStyle bit</th><th role="">C Definition</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">bit 1</td><td role="">ITALIC</td><td role="">Font contains Italic characters, otherwise they
                  are upright.</td></tr><tr><td role="">1</td><td role=""> </td><td role="">UNDERSCORE</td><td role="">Characters are underscored.</td></tr><tr><td role="">2</td><td role=""> </td><td role="">NEGATIVE</td><td role="">Characters have their foreground and background
                  reversed.</td></tr><tr><td role="">3</td><td role=""> </td><td role="">OUTLINED</td><td role="">Outline (hollow) characters, otherwise they are
                  solid.</td></tr><tr><td role="">4</td><td role=""> </td><td role="">STRIKEOUT</td><td role="">Characters are overstruck</td></tr><tr><td role="">5</td><td role="">bit 0</td><td role="">BOLD</td><td role="">Characters are emboldened.</td></tr><tr><td role="">6</td><td role=""> </td><td role="">REGULAR</td><td role="">Characters are in the standard weight/style for
                  the font.</td></tr></tbody></table></div><p role="">Comments: All undefined bits must be zero.</p><p role="">This field contains information on the original design
          of the font. Bits 0 &amp; 5 can be used to determine if the font
          was designed with these features or whether some type of
          machine simulation was performed on the font to achieve this
          appearance. Bits 1-4 are rarely used bits that indicate the
          font is primarily a decorative or special purpose
          font.</p><p role="">If bit 6 is set, then bits 0 and 5 must be clear, else
          the behavior is undefined. As noted above, the settings of
          bits 0 and 1 must be reflected in the macStyle bits in the
          <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a> table. While bit 6 on implies that
          bits 0 and 1 of macStyle are clear (along with bits 0 and 5
          of fsSelection), the reverse is not true. Bits 0 and 1 of
          macStyle (and 0 and 5 of fsSelection) may be clear and that
          does not give any indication of whether or not bit 6 of
          fsSelection is clear (e.g., Arial Light would have all bits
          cleared; it is not the regular version of Arial). </p><h4><a name="idm320133080544"></a>usFirstCharIndex</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The minimum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and platform- specific encoding ID 0 or 1. For most fonts
          supporting Win-ANSI or other character sets, this value
          would be 0x0020. This field cannot represent supplementary
	  character values (codepoints greater than 0xFFFF). Fonts that
	  support supplementary characters should set the value in this
	  field to 0xFFFF if the minimum index value is a supplementary
	  character.</p><h4><a name="idm320133078784"></a>usLastCharIndex</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The maximum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and encoding ID 0 or 1. This value depends on which
          character sets the font supports. This field cannot
	  represent supplementary character values (codepoints greater
	  than 0xFFFF). Fonts that support supplementary characters
	  should set the value in this field to 0xFFFF. </p><h4><a name="idm320133077152"></a>sTypoAscender</h4><p role="">Format: SHORT</p><p role="">Description: The typographic ascender for this font.
          Remember that this is not the same as the Ascender value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoAscender in
          Latin based fonts is the Ascender value from an AFM file.
          For CJK fonts see below.</p><p role="">The suggested usage for sTypoAscender is that it be used
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
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table.</p><p role="">For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoAscender is
          that which describes the top of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoAscender must be set to
          880. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p role="">Also see the Recommendations Section for more on this
          field. </p><h4><a name="idm320133071728"></a>sTypoDescender</h4><p role="">Format: SHORT</p><p role="">Description: The typographic descender for this font.
          Remember that this is not the same as the Descender value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoDescender in
          Latin based fonts is the Descender value from an AFM file.
          For CJK fonts see below.</p><p role="">The suggested usage for sTypoDescender is that it be
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
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes the
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API).</p><p role="">For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoDescender
          is that which describes the bottom of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoDescender must be set to
          -120. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p role="">Also see the Recommendations Section for more on this
          field. </p><h4><a name="idm320133066320"></a>sTypoLineGap</h4><p role="">Format: 2-byte SHORT</p><p role="">Description: The typographic line gap for this font.
          Remember that this is not the same as the LineGap value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner.</p><p role="">The suggested usage for usTypoLineGap is that it be used
          in conjunction with unitsPerEm to compute a typographically
          correct default line spacing. Typical values average 7-10%
          of units per em. The goal is to free applications from
          Macintosh or Windows-specific metrics which are constrained
          by backward compatability requirements (see chapter,
          "Recommendations for OpenType Fonts"). These new metrics, when
          combined with the character design widths, will allow
          applications to lay out documents in a typographically
          correct and portable fashion. These metrics will be exposed
          through Windows APIs. Macintosh applications will need to
          access the 'sfnt' resource and parse it to extract this data
          from the <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes
          the <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API) </p><h4><a name="idm320133061680"></a>usWinAscent</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The ascender metric for Windows. This, too,
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
          mind.</p><p role="">If any clipping is unacceptable, then the value should
          be set to yMax.</p><p role="">However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against OpenType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped.</p><h4><a name="idm320133058032"></a>usWinDescent</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The descender metric for Windows. This,
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
          mind.</p><p role="">If any clipping is unacceptable, then the value should
          be set to yMin.</p><p role="">However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against OpenType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped. </p><h4><a name="idm320133054720"></a>ulCodePageRange1 Bits 0-31</h4><h4><a name="idm320133054304"></a>ulCodePageRange2 Bits 32-63 </h4><p role="">Format: 32-bit unsigned long(2 copies) totaling 64
          bits.</p><p role="">Title: Code Page Character Range</p><p role="">Description: This field is used to specify the code
        pages encompassed by the font file in the
        <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable for platform 3, encoding ID 1
        (Microsoft platform). If the font file is encoding ID 0, then
        the Symbol Character Set bit should be set. If the bit is set
        (1) then the code page is considered functional. If the bit is
        clear (0) then the code page is not considered
        functional. Each of the bits is treated as an independent flag
        and the bits can be set in any combination. The determination
        of "functional" is left up to the font designer, although
        character set selection should attempt to be functional by
        code pages if at all possible.</p><p role="">Symbol character sets have a special meaning. If the
        symbol bit (31) is set, and the font file contains a
        <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable for platform of 3 and
        encoding ID of 1, then all of the characters in the Unicode
        range 0xF000 - 0xF0FF (inclusive) will be used to enumerate
        the symbol character set. If the bit is not set, any
        characters present in that range will not be enumerated as a
        symbol character set.</p><p role="">All reserved fields must be zero. Each long is in
          Big-Endian form. </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="6pc"/><col width="6pc"/><col width="18pc"/></colgroup><thead><tr><th role="">Bit</th><th role="">Code</th><th role="">Page Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">1252</td><td role="">Latin 1</td></tr><tr><td role="">1</td><td role="">1250</td><td role="">Latin 2: Eastern Europe</td></tr><tr><td role="">2</td><td role="">1251</td><td role="">Cyrillic</td></tr><tr><td role="">3</td><td role="">1253</td><td role="">Greek</td></tr><tr><td role="">4</td><td role="">1254</td><td role="">Turkish</td></tr><tr><td role="">5</td><td role="">1255</td><td role="">Hebrew</td></tr><tr><td role="">6</td><td role="">1256</td><td role="">Arabic</td></tr><tr><td role="">7</td><td role="">1257</td><td role="">Windows Baltic</td></tr><tr><td role="">8</td><td role="">1258</td><td role="">Vietnamese</td></tr><tr><td role="">9-15</td><td role=""> </td><td role="">Reserved for Alternate ANSI</td></tr><tr><td role="">16</td><td role="">874</td><td role="">Thai</td></tr><tr><td role="">17</td><td role="">932</td><td role="">JIS/Japan</td></tr><tr><td role="">18</td><td role="">936</td><td role="">Chinese: Simplified chars--PRC and
                  Singapore</td></tr><tr><td role="">19</td><td role="">949</td><td role="">Korean Wansung</td></tr><tr><td role="">20</td><td role="">950</td><td role="">Chinese: Traditional chars--Taiwan and Hong
                  Kong</td></tr><tr><td role="">21</td><td role="">1361</td><td role="">Korean Johab</td></tr><tr><td role="">22-28</td><td role=""> </td><td role="">Reserved for Alternate ANSI &amp; OEM</td></tr><tr><td role="">29</td><td role=""> </td><td role="">Macintosh Character Set (US Roman)</td></tr><tr><td role="">30</td><td role=""> </td><td role="">OEM Character Set</td></tr><tr><td role="">31</td><td role=""> </td><td role="">Symbol Character Set</td></tr><tr><td role="">32-47</td><td role=""> </td><td role="">Reserved for OEM</td></tr><tr><td role="">48</td><td role="">869</td><td role="">IBM Greek</td></tr><tr><td role="">49</td><td role="">866</td><td role="">MS-DOS Russian</td></tr><tr><td role="">50</td><td role="">865</td><td role="">MS-DOS Nordic</td></tr><tr><td role="">51</td><td role="">864</td><td role="">Arabic</td></tr><tr><td role="">52</td><td role="">863</td><td role="">MS-DOS Canadian French</td></tr><tr><td role="">53</td><td role="">862</td><td role="">Hebrew</td></tr><tr><td role="">54</td><td role="">861</td><td role="">MS-DOS Icelandic</td></tr><tr><td role="">55</td><td role="">860</td><td role="">MS-DOS Portuguese</td></tr><tr><td role="">56</td><td role="">857</td><td role="">IBM Turkish</td></tr><tr><td role="">57</td><td role="">855</td><td role="">IBM Cyrillic; primarily Russian</td></tr><tr><td role="">58</td><td role="">852</td><td role="">Latin 2</td></tr><tr><td role="">59</td><td role="">775</td><td role="">MS-DOS Baltic</td></tr><tr><td role="">60</td><td role="">737</td><td role="">Greek; former 437 G</td></tr><tr><td role="">61</td><td role="">708</td><td role="">Arabic; ASMO 708</td></tr><tr><td role="">62</td><td role="">850</td><td role="">WE/Latin 1</td></tr><tr><td role="">63</td><td role="">437</td><td role="">US</td></tr></tbody></table></div><h4><a name="idm320136719232"></a>sxHeight</h4><p role="">Format: SHORT</p><p role="">Description: This metric specifies the distance between
          the baseline and the approximate height of non-ascending
          lowercase letters measured in FUnits. This value would
          normally be specified by a type designer but in situations
          where that is not possible, for example when a legacy font
          is being converted, the value may be set equal to the top of
          the unscaled and unhinted glyph bounding box of the glyph
          encoded at U+0078 (LATIN SMALL LETTER X). If no glyph is
          encoded in this position the field should be set to
          0.</p><p role="">This metric, if specified, can be used in font
          substitution: the xHeight value of one font can be scaled to
          approximate the apparent size of another. </p><h4><a name="idm320136791792"></a>sCapHeight</h4><p role="">Format: SHORT</p><p role="">Description: This metric specifies the distance between
          the baseline and the approximate height of uppercase letters
          measured in FUnits. This value would normally be specified
          by a type designer but in situations where that is not
          possible, for example when a legacy font is being converted,
          the value may be set equal to the top of the unscaled and
          unhinted glyph bounding box of the glyph encoded at U+0048
          (LATIN CAPITAL LETTER H). If no glyph is encoded in this
          position the field should be set to 0.</p><p role="">This metric, if specified, can be used in systems that
          specify type size by capital height measured in millimeters.
          It can also be used as an alignment metric; the top of a
          drop capital, for instance, can be aligned to the sCapHeight
          metric of the first line of text. </p><h4><a name="idm320134296400"></a>usDefaultChar</h4><p role="">Format: USHORT</p><p role="">Description: Whenever a request is made for a character
          that is not in the font, Windows provides this default
          character. If the value of this field is zero, glyph ID 0 is
          to be used for the default character otherwise this is the
          Unicode encoding of the glyph that Windows uses as the
          default character. This field cannot represent supplementary
          character values (codepoints greater than 0xFFFF).</p><h4><a name="idm320134294784"></a>usBreakChar</h4><p role="">Format: USHORT</p><p role="">Description: This is the Unicode encoding of the glyph
          that Windows uses as the break character. The break
          character is used to separate words and justify text. Most
          fonts specify 'space' as the break character. This field
          cannot represent supplementary character values (codepoints
          greater than 0xFFFF).</p><h4><a name="idm320134293264"></a>usMaxContext</h4><p role="">Format: USHORT</p><p role="">Description: The maximum length of a target glyph
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
          considered.</p></div><div role="specification" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.11.1.2"></a>Specification</h3></div></div></div><p role="">The OS/2 table consists of a set of metrics that are
          required in OpenType fonts. The fourth version of the OS/2
          table (version 3) follows:</p><div class="table"><a name="idm320134289744"></a><p class="title"><strong>Table 11.2. </strong></p><div class="table-contents"><table role="" class="table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th><th role="">Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">USHORT</td><td role="">version</td><td role="">0x0003</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">xAvgCharWidth</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWeightClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWidthClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">fsType</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptXSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptYSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptXOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySubscriptYOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptXSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptYSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptXOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">ySuperscriptYOffset</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yStrikeoutSize</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">yStrikeoutPosition</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sFamilyClass</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">BYTE</td><td role="">panose[10]</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange1</td><td role="">Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange2</td><td role="">Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange3</td><td role="">Bits 64-95</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulUnicodeRange4</td><td role="">Bits 96-127</td><td class="auto-generated"> </td></tr><tr><td role="">CHAR</td><td role="">achVendID[4]</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">fsSelection</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usFirstCharIndex</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usLastCharIndex</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoAscender</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoDescender</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sTypoLineGap</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWinAscent</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usWinDescent</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulCodePageRange1</td><td role="">Bits 0-31</td><td class="auto-generated"> </td></tr><tr><td role="">ULONG</td><td role="">ulCodePageRange2</td><td role="">Bits 32-63</td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sxHeight</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">SHORT</td><td role="">sCapHeight</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usDefaultChar</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usBreakChar</td><td role=""> </td><td class="auto-generated"> </td></tr><tr><td role="">USHORT</td><td role="">usMaxContext</td><td role=""> </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><h4><a name="idm320134241808"></a>version</h4><p role="">Format: 2-byte unsigned short</p><p role="">Units: n/a</p><p role="">Title: OS/2 table version number.</p><p role="">Description: The version number for this OS/2
          table.</p><p role="">Comments: The version number allows for identification
          of the precise contents and layout for the OS/2 table. The
          version number for this layout is two (2). Versions one (1)
          and zero (0) have been used previously, in rev.1.66 and 1.5,
          respectively, of the TrueType specification.</p><h4><a name="idm320134239072"></a>xAvgCharWidth</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Pels / em units</p><p role="">Title: Average weighted escapement.</p><p role="">Description: The Average Character Width parameter
          specifies the arithmetic average of the escapement (width)
          of all of the 26 lowercase letters a through z of the Latin
          alphabet and the space character. If any of the 26 lowercase
          letters are not present, this parameter should equal the
          weighted average of all glyphs in the font. For non-UGL
          (platform 3, encoding 0) fonts, use the unweighted
          average.</p><p role="">Comments: This parameter is a descriptive attribute of
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
          example:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="15pc"/><col width="15pc"/><col/><col/></colgroup><thead><tr><th role="">Letter</th><th role="">Weight Factor</th><td class="auto-generated"> </td><td class="auto-generated"> </td></tr></thead><tbody><tr><td role="">a</td><td role="">64</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">b</td><td role="">14</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">c</td><td role="">27</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">d</td><td role="">35</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">e</td><td role="">100</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">f</td><td role="">20</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">g</td><td role="">14</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">h</td><td role="">42</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">i</td><td role="">63</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">j</td><td role="">3</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">k</td><td role="">6</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">l</td><td role="">35</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">m</td><td role="">20</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">n</td><td role="">56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">o</td><td role="">56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">p</td><td role="">17</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">q</td><td role="">4</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">r</td><td role="">49</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">s</td><td role="">56</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">t</td><td role="">71</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">u</td><td role="">31</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">v</td><td role="">10</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">w</td><td role="">18</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">x</td><td role="">3</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">y</td><td role="">18</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">z</td><td role="">2</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr><tr><td role="">space</td><td role="">166</td><td class="auto-generated"> </td><td class="auto-generated"> </td></tr></tbody></table></div><h4><a name="idm320134199808"></a>usWeightClass</h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Weight class. </p><p role="">Description: Indicates the visual weight (degree of
          blackness or thickness of strokes) of the characters in the
          font. </p><p role="">Comments:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="18pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th><th role="">C Definition (from windows.h)</th></tr></thead><tbody><tr><td role="">100</td><td role="">Thin</td><td role="">FW_THIN</td></tr><tr><td role="">200</td><td role="">Extra-light (Ultra-light)</td><td role="">FW_EXTRALIGHT</td></tr><tr><td role="">300</td><td role="">Light</td><td role="">FW_LIGHT</td></tr><tr><td role="">400</td><td role="">Normal (Regular)</td><td role="">FW_NORMAL</td></tr><tr><td role="">500</td><td role="">Medium</td><td role="">FW_MEDIUM</td></tr><tr><td role="">600</td><td role="">Semi-bold (Demi-bold)</td><td role="">FW_SEMIBOLD</td></tr><tr><td role="">700</td><td role="">Bold</td><td role="">FW_BOLD</td></tr><tr><td role="">800</td><td role="">Extra-bold (Ultra-bold)</td><td role="">FW_EXTRABOLD</td></tr><tr><td role="">900</td><td role="">Black (Heavy)</td><td role="">FW_BLACK</td></tr></tbody></table></div><h4><a name="idm320134179184"></a>usWidthClass </h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Width class. </p><p role="">Description: Indicates a relative change from the normal
          aspect ratio (width to height ratio) as specified by a font
          designer for the glyphs in a font. </p><p role="">Comments:  Although every character in a font may have a
          different numeric aspect ratio, each character in a font of
          normal width has a relative aspect ratio of one. When a new
          type style is created of a different width class (either by
          a font designer or by some automated means) the relative
          aspect ratio of the characters in the new font is some
          percentage greater or less than those same characters in the
          normal font -- it is this difference that this parameter
          specifies. </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="14pc"/><col width="4pc"/></colgroup><thead><tr><th role="">Value</th><th role="">Description</th><th role="">C Definition</th><th role="">% of normal</th></tr></thead><tbody><tr><td role="">1</td><td role="">Ultra-condensed</td><td role="">FWIDTH_ULTRA_CONDENSED</td><td role="">50</td></tr><tr><td role="">2</td><td role="">Extra-condensed</td><td role="">FWIDTH_EXTRA_CONDENSED</td><td role="">62.5</td></tr><tr><td role="">3</td><td role="">Condensed</td><td role="">FWIDTH_CONDENSED</td><td role="">75</td></tr><tr><td role="">4</td><td role="">Semi-condensed</td><td role="">FWIDTH_SEMI_CONDENSED</td><td role="">87.5</td></tr><tr><td role="">5</td><td role="">Medium (normal)</td><td role="">FWIDTH_NORMAL</td><td role="">100</td></tr><tr><td role="">6</td><td role="">Semi-expanded</td><td role="">FWIDTH_SEMI_EXPANDED</td><td role="">112.5</td></tr><tr><td role="">7</td><td role="">Expanded</td><td role="">FWIDTH_EXPANDED</td><td role="">125</td></tr><tr><td role="">8</td><td role="">Extra-expanded</td><td role="">FWIDTH_EXTRA_EXPANDED</td><td role="">150</td></tr><tr><td role="">9</td><td role="">Ultra-expanded</td><td role="">FWIDTH_ULTRA_EXPANDED</td><td role="">200</td></tr></tbody></table></div><h4><a name="idm320134153648"></a>fsType</h4><p role="">Format: 2-byte unsigned short</p><p role="">Title: Type flags. </p><p role="">Description: Indicates font embedding licensing rights
          for the font. Embeddable fonts may be stored in a document.
          When a document with embedded fonts is opened on a system
          that does not have the font installed (the remote system),
          the embedded font may be loaded for temporary (and in some
          cases, permanent) use on that system by an embedding-aware
          application. Embedding licensing rights are granted by the
          vendor of the font.</p><p role="">The OpenType Font Embedding DLL Specification and DLL
          release notes describe the APIs used to implement support
          for OpenType font embedding and loading.
          <span role="" class="emphasis"><em>Applications that implement support for font
            embedding, either through use of the Font Embedding DLL or
            through other means, must not embed fonts which are not
            licensed to permit embedding. Further, applications
            loading embedded fonts for temporary use (see Preview
            &amp; Print and Editable embedding below) must delete the
            fonts when the document containing the embedded font is
            closed.</em></span></p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="1cm"/><col width="2cm"/><col width="10cm"/></colgroup><thead><tr><th role="">Bit</th><th role="">BitMask</th><th role="">Description</th></tr></thead><tbody><tr><td role=""> </td><td role="">0x0000</td><td role="">Installable Embedding: No fsType bit is set.
                  Thus fsType is zero. Fonts with this setting
                  indicate that they may be embedded and permanently
                  installed on the remote system by an application.
                  The user of the remote system acquires the identical
                  rights, obligations and licenses for that font as
                  the original purchaser of the font, and is subject
                  to the same end-user license agreement, copyright,
                  design patent, and/or trademark as was the original
                  purchaser.</td></tr><tr><td role="">0</td><td role="">0x0001</td><td role="">Reserved, must be zero.</td></tr><tr><td role="">1</td><td role="">0x0002</td><td role="">Restricted License embedding: Fonts that have
                  <span role="" class="emphasis"><em>only</em></span> this bit set must not be
                  <span role="" class="emphasis"><em>modified, embedded or exchanged in any
                    manner</em></span> without first obtaining
                  permission of the legal owner. Caution: For
                  Restricted License embedding to take effect, it must
                  be the only level of embedding selected.</td></tr><tr><td role="">2</td><td role="">0x0004</td><td role="">Preview &amp; Print embedding: When this bit is
                  set, the font may be embedded, and temporarily
                  loaded on the remote system. Documents containing
                  Preview &amp; Print fonts must be opened "read-only;" no
                  edits can be applied to the document.</td></tr><tr><td role="">3</td><td role="">0x0008</td><td role="">Editable embedding: When this bit is set, the
                  font may be embedded but must only be installed
                  <span role="" class="emphasis"><em>temporarily</em></span> on other systems.
                  In contrast to Preview &amp; Print fonts, documents
                  containing Editable fonts <span role="" class="emphasis"><em>may</em></span>
                  be opened for reading, editing is permitted, and
                  changes may be saved.</td></tr><tr><td role="">4-7</td><td role=""> </td><td role="">Reserved, must be zero.</td></tr><tr><td role="">8</td><td role="">0x0100</td><td role="">No subsetting: When this bit is set, the font
                  may not be subsetted prior to embedding. Other
                  embedding restrictions specified in the lower byte
                  also apply.</td></tr><tr><td role="">9</td><td role="">0x0200</td><td role="">Bitmap embedding only: When this bit is set,
                  only bitmaps contained in the font may be embedded.
                  No outline data may be embedded. If there are no
                  bitmaps available in the font, then the font is
                  considered unembeddable and the embedding services
                  will fail. Other embedding restrictions specified in
                  the lower byte also apply.</td></tr><tr><td role="">10-15</td><td role=""> </td><td role="">Reserved, must be zero.</td></tr></tbody></table></div><p role="">Comments: If multiple embedding bits are set, the least
          restrictive license granted takes precedence. For example,
          if bits 1 and 3 are set, bit 3 takes precedence over bit
          1 and the font may be embedded with Editable rights. For
          compatibility purposes, most vendors granting Editable
          embedding rights are also setting the Preview &amp; Print bit
          (0x000C). This will permit an application that only supports
          Preview &amp; Print embedding to detect that font embedding is
          allowed.</p><h4><a name="idm320134126448"></a>ySubscriptXSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript horizontal font size. </p><p role="">Description: The recommended horizontal size in font
          design units for subscripts for this font.  </p><p role="">Comments: If a font has two recommended sizes for
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
          subscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySubScriptXSize is set to 205, then the horizontal size for
          a simulated subscript character would be 1/10th the size of
          the normal character.</p><h4><a name="idm320134122592"></a>ySubscriptYSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript vertical font size. </p><p role="">Description: The recommended vertical size in font
          design units for subscripts for this font.  </p><p role="">Comments: If a font has two recommended sizes for
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
          those subscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySubScriptYSize is set to 205, then the vertical size for a
          simulated subscript character would be 1/10th the size of
          the normal character.</p><h4><a name="idm320134118752"></a>ySubscriptXOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript x offset.</p><p role="">Description: The recommended horizontal offset in font
          design untis for subscripts for this font. </p><p role="">Comments: The Subscript X Offset parameter specifies a
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
          the angle of incline.</p><h4><a name="idm320134116336"></a>ySubscriptYOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Subscript y offset. </p><p role="">Description: The recommended vertical offset in font
          design units from the baseline for subscripts for this font.
        </p><p role="">Comments: The Subscript Y Offset parameter specifies a
          font designer's recommended vertical offset from the
          character baseline to the character baseline for subscript
          characters associated with this font. Values are expressed
          as a positive offset below the character baseline. If a font
          does not include all of the required subscript for an
          application, this parameter specifies the recommended
          vertical distance below the character baseline for those
          subscript characters.</p><h4><a name="idm320134113248"></a>ySuperscriptXSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript horizontal font size.</p><p role="">Description: The recommended horizontal size in font
          design units for superscripts for this font. </p><p role="">Comments: If a font has two recommended sizes for
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
          square for those superscript characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySuperScriptXSize is set to 205, then the horizontal size
          for a simulated superscript character would be 1/10th the
          size of the normal character.</p><h4><a name="idm320134109440"></a>ySuperscriptYSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript vertical font size.</p><p role="">Description: The recommended vertical size in font
          design units for superscripts for this font. </p><p role="">Comments: If a font has two recommended sizes for
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
          characters.</p><p role="">For example, if the em square for a font is 2048 and
          ySuperScriptYSize is set to 205, then the vertical size for
          a simulated superscript character would be 1/10th the size
          of the normal character.</p><h4><a name="idm320134105584"></a>ySuperscriptXOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript x offset.</p><p role="">Description: The recommended horizontal offset in font
          design units for superscripts for this font. </p><p role="">Comments: The Superscript X Offset parameter specifies a
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
          adjusted to compensate for the angle of incline.</p><h4><a name="idm320134102352"></a>ySuperscriptYOffset</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Superscript y offset.</p><p role="">Description: The recommended vertical offset in font
          design units from the baseline for superscripts for this
          font. </p><p role="">Comments: The Superscript Y Offset parameter specifies a
          font designer's recommended vertical offset -- from the
          character baseline to the superscript character's baseline
          associated with this font. Values for this parameter are
          expressed as a positive offset above the character baseline.
          If a font does not include all of the required superscript
          characters for an application, this parameter specifies the
          recommended vertical distance above the character baseline
          for those superscript characters.</p><h4><a name="idm320136774352"></a>yStrikeoutSize</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Strikeout size.</p><p role="">Description: Width of the strikeout stroke in font
          design units. </p><p role="">Comments: This field should normally be the width of the
          em dash for the current font. If the size is one, the
          strikeout line will be the line represented by the strikeout
          position field. If the value is two, the strikeout line will
          be the line represented by the strikeout position and the
          line immediately above the strikeout position. For a Roman
          font with a 2048 em square, 102 is suggested.</p><h4><a name="idm320136709600"></a>yStrikeoutPosition</h4><p role="">Format: 2-byte signed short</p><p role="">Units: Font design units</p><p role="">Title: Strikeout position.</p><p role="">Description: The position of the top of the strikeout
          stroke relative to the baseline in font design units.
        </p><p role="">Comments: Positive values represent distances above the
          baseline, while negative values represent distances below
          the baseline. A value of zero falls directly on the
          baseline, while a value of one falls one pel above the
          baseline. The value of strikeout position should not
          interfere with the recognition of standard characters, and
          therefore should not line up with crossbars in the font. For
          a Roman font with a 2048 em square, 460 is suggested.</p><h4><a name="idm320136712048"></a>sFamilyClass</h4><p role="">Format: 2-byte signed short</p><p role="">Title: Font-family class and subclass.</p><p role="">Description: This parameter is a classification of
          font-family design. </p><p role="">Comments: The font class and font subclass are
          registered values assigned by IBM to each font family. This
          parameter is intended for use in selecting an alternate font
          when the requested font is not available. The font class is
          the most general and the font subclass is the most specific.
          The high byte of this field contains the family class, while
          the low byte contains the family subclass. More information
          about this field.  </p><h4><a name="idm320136710128"></a>Panose</h4><p role="">Format: 10 byte array</p><p role="">Title: PANOSE classification number</p><p role="">International: Additional specifications are required
          for PANOSE to classify non-Latin character sets.</p><p role="">Description: This 10 byte series of numbers is used to
          describe the visual characteristics of a given typeface.
          These characteristics are then used to associate the font
          with other fonts of similar appearance having different
          names. The variables for each digit are listed below. The
          Panose values are fully described in the Panose "greybook"
          reference, currently owned by Agfa-Monotype. </p><p role="">Comments: The PANOSE definition contains ten digits each
          of which currently describes up to sixteen variations.
          Windows uses bFamilyType, bSerifStyle and bProportion in the
          font mapper to determine family type. It also uses
          bProportion to determine if the font is monospaced. If the
          font is a symbol font, the first byte of the PANOSE number
          (bFamilyType) must be set to "pictorial." Good PANOSE values
          in fonts are very valuable to users of the Windows fonts
          folder. The specification for assigning PANOSE values is
          located at http://www.fonts.com/hp/panose/greybook/</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="3cm"/><col width="3cm"/></colgroup><thead><tr><th role="">Type</th><th role="">Name</th></tr></thead><tbody><tr><td role="">BYTE</td><td role="">bFamilyType</td></tr><tr><td role="">BYTE</td><td role="">bSerifStyle</td></tr><tr><td role="">BYTE</td><td role="">bWeight</td></tr><tr><td role="">BYTE</td><td role="">bProportion</td></tr><tr><td role="">BYTE</td><td role="">bContrast</td></tr><tr><td role="">BYTE</td><td role="">bStrokeVariation</td></tr><tr><td role="">BYTE</td><td role="">bArmStyle</td></tr><tr><td role="">BYTE</td><td role="">bLetterform</td></tr><tr><td role="">BYTE</td><td role="">bMidline</td></tr><tr><td role="">BYTE</td><td role="">bXHeight</td></tr></tbody></table></div><h4><a name="idm320136538912"></a>ulUnicodeRange1 (Bits 0-31)</h4><h4><a name="idm320136538528"></a>ulUnicodeRange2 (Bits 32-63)</h4><h4><a name="idm320136538144"></a>ulUnicodeRange3 (Bits 64-95)</h4><h4><a name="idm320136537760"></a>ulUnicodeRange4 (Bits 96-127)</h4><p role="">Format: 32-bit unsigned long(4 copies) totaling 128
          bits.</p><p role="">Title: Unicode Character Range</p><p role="">Description: This field is used to specify the Unicode
          blocks or ranges encompassed by the font file in the <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform 3, encoding ID 1 (Microsoft platform).
          If the bit is set (1) then the Unicode range is considered
          functional. If the bit is clear (0) then the range is not
          considered functional. Each of the bits is treated as an
          independent flag and the bits can be set in any combination.
          The determination of "functional" is left up to the font
          designer, although character set selection should attempt to
          be functional by ranges if at all possible.</p><p role="">
          All reserved fields must be zero. Each long is in Big-Endian
          form. See the Basic Multilingual Plane of ISO/IEC 10646-1 or
          the Unicode Standard v.3.0 for the list of Unicode ranges
          and characters.  </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="10pc"/><col width="20pc"/></colgroup><thead><tr><th role="">Bit</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">Basic Latin</td></tr><tr><td role="">1</td><td role="">Latin-1 Supplement</td></tr><tr><td role="">2</td><td role="">Latin Extended-A</td></tr><tr><td role="">3</td><td role="">Latin Extended-B</td></tr><tr><td role="">4</td><td role="">IPA Extensions</td></tr><tr><td role="">5</td><td role="">Spacing Modifier Letters</td></tr><tr><td role="">6</td><td role="">Combining Diacritical Marks</td></tr><tr><td role="">7</td><td role="">Greek</td></tr><tr><td role="">8</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">9</td><td role="">Cyrillic</td></tr><tr><td role="">10</td><td role="">Armenian</td></tr><tr><td role="">11</td><td role="">Hebrew</td></tr><tr><td role="">12</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">13</td><td role="">Arabic</td></tr><tr><td role="">14</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">15</td><td role="">Devanagari</td></tr><tr><td role="">16</td><td role="">Bengali</td></tr><tr><td role="">17</td><td role="">Gurmukhi</td></tr><tr><td role="">18</td><td role="">Gujarati</td></tr><tr><td role="">19</td><td role="">Oriya</td></tr><tr><td role="">20</td><td role="">Tamil</td></tr><tr><td role="">21</td><td role="">Telugu</td></tr><tr><td role="">22</td><td role="">Kannada</td></tr><tr><td role="">23</td><td role="">Malayalam</td></tr><tr><td role="">24</td><td role="">Thai</td></tr><tr><td role="">25</td><td role="">Lao</td></tr><tr><td role="">26</td><td role="">Georgian</td></tr><tr><td role="">27</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">28</td><td role="">Hangul Jamo</td></tr><tr><td role="">29</td><td role="">Latin Extended Additional</td></tr><tr><td role="">30</td><td role="">Greek Extended</td></tr><tr><td role="">31</td><td role="">General Punctuation</td></tr><tr><td role="">32</td><td role="">Superscripts And Subscripts</td></tr><tr><td role="">33</td><td role="">Currency Symbols</td></tr><tr><td role="">34</td><td role="">Combining Diacritical Marks For Symbols</td></tr><tr><td role="">35</td><td role="">Letterlike Symbols</td></tr><tr><td role="">36</td><td role="">Number Forms</td></tr><tr><td role="">37</td><td role="">Arrows</td></tr><tr><td role="">38</td><td role="">Mathematical Operators</td></tr><tr><td role="">39</td><td role="">Miscellaneous Technical</td></tr><tr><td role="">40</td><td role="">Control Pictures</td></tr><tr><td role="">41</td><td role="">Optical Character Recognition</td></tr><tr><td role="">42</td><td role="">Enclosed Alphanumerics</td></tr><tr><td role="">43</td><td role="">Box Drawing</td></tr><tr><td role="">44</td><td role="">Block Elements</td></tr><tr><td role="">45</td><td role="">Geometric Shapes</td></tr><tr><td role="">46</td><td role="">Miscellaneous Symbols</td></tr><tr><td role="">47</td><td role="">Dingbats</td></tr><tr><td role="">48</td><td role="">CJK Symbols And Punctuation</td></tr><tr><td role="">49</td><td role="">Hiragana</td></tr><tr><td role="">50</td><td role="">Katakana</td></tr><tr><td role="">51</td><td role="">Bopomofo</td></tr><tr><td role=""> </td><td role="">  Extended Bopomofo</td></tr><tr><td role="">52</td><td role="">Hangul Compatibility Jamo</td></tr><tr><td role="">53</td><td role="">CJK Miscellaneous</td></tr><tr><td role="">54</td><td role="">Enclosed CJK Letters And Months</td></tr><tr><td role="">55</td><td role="">CJK Compatibility</td></tr><tr><td role="">56</td><td role="">Hangul</td></tr><tr><td role="">57</td><td role="">Surrogates<a href="#ftn.idm320136463344" class="footnote" id="idm320136463344"><sup class="footnote">[a]</sup></a></td></tr><tr><td role="">58</td><td role="">Reserved for Unicode SubRanges</td></tr><tr><td role="">59</td><td role="">CJK Unified Ideographs</td></tr><tr><td role=""> </td><td role=""> CJK Radicals Supplement</td></tr><tr><td role=""> </td><td role="">  Kangxi Radicals</td></tr><tr><td role=""> </td><td role="">  Ideographic Description</td></tr><tr><td role=""> </td><td role="">  CJK Unified Ideograph Extension A</td></tr><tr><td role="">60</td><td role="">Private Use Area</td></tr><tr><td role="">61</td><td role="">CJK Compatibility Ideographs</td></tr><tr><td role="">62</td><td role="">Alphabetic Presentation Forms</td></tr><tr><td role="">63</td><td role="">Arabic Presentation Forms-A</td></tr><tr><td role="">64</td><td role="">Combining Half Marks</td></tr><tr><td role="">65</td><td role="">CJK Compatibility Forms</td></tr><tr><td role="">66</td><td role="">Small Form Variants</td></tr><tr><td role="">67</td><td role="">Arabic Presentation Forms-B</td></tr><tr><td role="">68</td><td role="">Halfwidth And Fullwidth Forms</td></tr><tr><td role="">69</td><td role="">Specials</td></tr><tr><td role="">70</td><td role="">Tibetan</td></tr><tr><td role="">71</td><td role="">Syriac</td></tr><tr><td role="">72</td><td role="">Thaana</td></tr><tr><td role="">73</td><td role="">Sinhala</td></tr><tr><td role="">74</td><td role="">Myanmar</td></tr><tr><td role="">75</td><td role="">Ethiopic</td></tr><tr><td role="">76</td><td role="">Cherokee</td></tr><tr><td role="">77</td><td role="">Unified Canadian Syllabics</td></tr><tr><td role="">78</td><td role="">Ogham</td></tr><tr><td role="">79</td><td role="">Runic</td></tr><tr><td role="">80</td><td role="">Khmer</td></tr><tr><td role="">81</td><td role="">Mongolian</td></tr><tr><td role="">82</td><td role="">Braille</td></tr><tr><td role="">83</td><td role="">Yi</td></tr><tr><td role=""> </td><td role="">  Yi Radicals</td></tr><tr><td role="">84-127</td><td role="">Reserved for Unicode SubRanges</td></tr></tbody><tbody class="footnotes"><tr><td colspan="2"><div id="ftn.idm320136463344" role="" class="footnote"><p role=""><a href="#idm320136463344" class="para"><sup class="para">[a] </sup></a>Setting bit 57 implies that there is
                      at least one codepoint beyond the Basic
                      Multilingual Plane that is supported by this
                      font.</p></div></td></tr></tbody></table></div><h4><a name="idm320136425632"></a>achVendID</h4><p role="">Format: 4-byte character array</p><p role="">Title: Font Vendor Identification</p><p role="">Description: The four character identifier for the
          vendor of the given type face.</p><p role="">Comments: This is not the royalty owner of the original
          artwork. This is the company responsible for the marketing
          and distribution of the typeface that is being classified.
          It is reasonable to assume that there will be 6 vendors of
          ITC Zapf Dingbats for use on desktop platforms in the near
          future (if not already). It is also likely that the vendors
          will have other inherent benefits in their fonts (more kern
          pairs, unregularized data, hand hinted, etc.). This
          identifier will allow for the correct vendor's type to be
          used over another, possibly inferior, font file. The Vendor
          ID value is not required.</p><p role="">Microsoft has assigned values for some font suppliers as
          listed below. Uppercase vendor ID's are reserved by
          Microsoft. Other suppliers can choose their own mixed case
          or lowercase ID's, or leave the field blank.</p><p role="">For a list of registered Vendor id's see our <a role="" class="ulink" href="http://www.microsoft.com/typography/links/vendorlist.asp" target="_top">Registered
            'vendors'</a> links page.</p><h4><a name="idm320136421264"></a>fsSelection</h4><p role="">Format: 2-byte bit field.</p><p role="">Title: Font selection flags.</p><p role="">Description: Contains information concerning the nature
          of the font patterns, as follows:</p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="4pc"/><col width="8pc"/><col width="8pc"/><col width="10pc"/></colgroup><thead><tr><th role="">Bit #</th><th role="">macStyle bit</th><th role="">C Definition</th><th role="">Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">bit 1</td><td role="">ITALIC</td><td role="">Font contains Italic characters, otherwise they
                  are upright.</td></tr><tr><td role="">1</td><td role=""> </td><td role="">UNDERSCORE</td><td role="">Characters are underscored.</td></tr><tr><td role="">2</td><td role=""> </td><td role="">NEGATIVE</td><td role="">Characters have their foreground and background
                  reversed.</td></tr><tr><td role="">3</td><td role=""> </td><td role="">OUTLINED</td><td role="">Outline (hollow) characters, otherwise they are
                  solid.</td></tr><tr><td role="">4</td><td role=""> </td><td role="">STRIKEOUT</td><td role="">Characters are overstruck</td></tr><tr><td role="">5</td><td role="">bit 0</td><td role="">BOLD</td><td role="">Characters are emboldened.</td></tr><tr><td role="">6</td><td role=""> </td><td role="">REGULAR</td><td role="">Characters are in the standard weight/style for
                  the font.</td></tr></tbody></table></div><p role="">Comments: All undefined bits must be zero.</p><p role="">This field contains information on the original design
          of the font. Bits 0 &amp; 5 can be used to determine if the font
          was designed with these features or whether some type of
          machine simulation was performed on the font to achieve this
          appearance. Bits 1-4 are rarely used bits that indicate the
          font is primarily a decorative or special purpose
          font.</p><p role="">If bit 6 is set, then bits 0 and 5 must be clear, else
          the behavior is undefined. As noted above, the settings of
          bits 0 and 1 must be reflected in the macStyle bits in the
          <a role="" class="link" href="chapter.head.md" title="Chapter 6. head - Font Header">head</a> table. While bit 6 on implies that
          bits 0 and 1 of macStyle are clear (along with bits 0 and 5
          of fsSelection), the reverse is not true. Bits 0 and 1 of
          macStyle (and 0 and 5 of fsSelection) may be clear and that
          does not give any indication of whether or not bit 6 of
          fsSelection is clear (e.g., Arial Light would have all bits
          cleared; it is not the regular version of Arial). </p><h4><a name="idm320136397712"></a>usFirstCharIndex</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The minimum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and platform- specific encoding ID 0 or 1. For most fonts
          supporting Win-ANSI or other character sets, this value
          would be 0x0020. </p><h4><a name="idm320136396256"></a>usLastCharIndex</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The maximum Unicode index (character code)
          in this font, according to the cmap subtable for platform ID
          3 and encoding ID 0 or 1. This value depends on which
          character sets the font supports. </p><h4><a name="idm320136394864"></a>sTypoAscender</h4><p role="">Format: SHORT</p><p role="">Description: The typographic ascender for this font.
          Remember that this is not the same as the Ascender value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoAscender in
          Latin based fonts is the Ascender value from an AFM file.
          For CJK fonts see below.</p><p role="">The suggested usage for sTypoAscender is that it be used
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
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table.</p><p role="">For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoAscender is
          that which describes the top of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoAscender must be set to
          880. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p role="">Also see the Recommendations Section for more on this
          field. </p><h4><a name="idm320136390176"></a>sTypoDescender</h4><p role="">Format: SHORT</p><p role="">Description: The typographic descender for this font.
          Remember that this is not the same as the Descender value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner. One good source for sTypoDescender in
          Latin based fonts is the Descender value from an AFM file.
          For CJK fonts see below.</p><p role="">The suggested usage for sTypoDescender is that it be
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
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes the
          <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API).</p><p role="">For CJK (Chinese, Japanese, and Korean) fonts that are
          intended to be used for vertical writing (in addition to
          horizontal writing), the required value for sTypoDescender
          is that which describes the bottom of the of the ideographic
          em-box. For example, if the ideographic em-box of the font
          extends from coordinates 0,-120 to 1000,880 (that is, a
          1000x1000 box set 120 design units below the Latin
          baseline), then the value of sTypoDescender must be set to
          -120. Failing to adhere to these requirements will result in
          incorrect vertical layout.</p><p role="">Also see the Recommendations Section for more on this
          field. </p><h4><a name="idm320136384256"></a>sTypoLineGap</h4><p role="">Format: 2-byte SHORT</p><p role="">Description: The typographic line gap for this font.
          Remember that this is not the same as the LineGap value in
          the <a role="" class="link" href="chapter.hhea.md" title="Chapter 7. hhea - Horizontal Header">hhea</a> table, which Apple defines in a
          far different manner.</p><p role="">The suggested usage for usTypoLineGap is that it be used
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
          from the <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table (unless Apple exposes
          the <a role="" class="link" href="chapter.OS2.md" title="Chapter 11. OS/2 - OS/2 and Windows Metrics">OS/2</a> table through a new API) </p><h4><a name="idm320136379840"></a>usWinAscent</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The ascender metric for Windows. This, too,
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
          mind.</p><p role="">If any clipping is unacceptable, then the value should
          be set to yMax.</p><p role="">However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against OpenType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped.</p><h4><a name="idm320136376592"></a>usWinDescent</h4><p role="">Format: 2-byte USHORT</p><p role="">Description: The descender metric for Windows. This,
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
          mind.</p><p role="">If any clipping is unacceptable, then the value should
          be set to yMin.</p><p role="">However, if a developer desires to provide appropriate
          default line spacing using this field, for those
          applications that continue to use this field for doing so
          (against OpenType recommendations), then the value should be
          set appropriately. In such a case, it may result in some
          glyph bitmaps being clipped. </p><h4><a name="idm320136373328"></a>ulCodePageRange1 Bits 0-31</h4><h4><a name="idm320136372944"></a>ulCodePageRange2 Bits 32-63 </h4><p role="">Format: 32-bit unsigned long(2 copies) totaling 64
          bits.</p><p role="">Title: Code Page Character Range</p><p role="">Description: This field is used to specify the code
          pages encompassed by the font file in the <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a> subtable
          for platform 3, encoding ID 1 (Microsoft platform). If the
          font file is encoding ID 0, then the Symbol Character Set
          bit should be set. If the bit is set (1) then the code page
          is considered functional. If the bit is clear (0) then the
          code page is not considered functional. Each of the bits is
          treated as an independent flag and the bits can be set in
          any combination. The determination of "functional" is left
          up to the font designer, although character set selection
          should attempt to be functional by code pages if at all
          possible.</p><p role="">Symbol character sets have a special meaning. If the
          symbol bit (31) is set, and the font file contains a <a role="" class="link" href="chapter.cmap.md" title="Chapter 5. cmap - Character to Glyph Index Mapping Table">cmap</a>
          subtable for platform of 3 and encoding ID of 1, then all of
          the characters in the Unicode range 0xF000 - 0xF0FF
          (inclusive) will be used to enumerate the symbol character
          set. If the bit is not set, any characters present in that
          range will not be enumerated as a symbol character
          set.</p><p role="">All reserved fields must be zero. Each long is in
          Big-Endian form. </p><div class="informaltable"><table role="" class="informaltable" border="1"><colgroup><col width="6pc"/><col width="6pc"/><col width="18pc"/></colgroup><thead><tr><th role="">Bit</th><th role="">Code</th><th role="">Page Description</th></tr></thead><tbody><tr><td role="">0</td><td role="">1252</td><td role="">Latin 1</td></tr><tr><td role="">1</td><td role="">1250</td><td role="">Latin 2: Eastern Europe</td></tr><tr><td role="">2</td><td role="">1251</td><td role="">Cyrillic</td></tr><tr><td role="">3</td><td role="">1253</td><td role="">Greek</td></tr><tr><td role="">4</td><td role="">1254</td><td role="">Turkish</td></tr><tr><td role="">5</td><td role="">1255</td><td role="">Hebrew</td></tr><tr><td role="">6</td><td role="">1256</td><td role="">Arabic</td></tr><tr><td role="">7</td><td role="">1257</td><td role="">Windows Baltic</td></tr><tr><td role="">8</td><td role="">1258</td><td role="">Vietnamese</td></tr><tr><td role="">9-15</td><td role=""> </td><td role="">Reserved for Alternate ANSI</td></tr><tr><td role="">16</td><td role="">874</td><td role="">Thai</td></tr><tr><td role="">17</td><td role="">932</td><td role="">JIS/Japan</td></tr><tr><td role="">18</td><td role="">936</td><td role="">Chinese: Simplified chars--PRC and
                  Singapore</td></tr><tr><td role="">19</td><td role="">949</td><td role="">Korean Wansung</td></tr><tr><td role="">20</td><td role="">950</td><td role="">Chinese: Traditional chars--Taiwan and Hong
                  Kong</td></tr><tr><td role="">21</td><td role="">1361</td><td role="">Korean Johab</td></tr><tr><td role="">22-28</td><td role=""> </td><td role="">Reserved for Alternate ANSI &amp; OEM</td></tr><tr><td role="">29</td><td role=""> </td><td role="">Macintosh Character Set (US Roman)</td></tr><tr><td role="">30</td><td role=""> </td><td role="">OEM Character Set</td></tr><tr><td role="">31</td><td role=""> </td><td role="">Symbol Character Set</td></tr><tr><td role="">32-47</td><td role=""> </td><td role="">Reserved for OEM</td></tr><tr><td role="">48</td><td role="">869</td><td role="">IBM Greek</td></tr><tr><td role="">49</td><td role="">866</td><td role="">MS-DOS Russian</td></tr><tr><td role="">50</td><td role="">865</td><td role="">MS-DOS Nordic</td></tr><tr><td role="">51</td><td role="">864</td><td role="">Arabic</td></tr><tr><td role="">52</td><td role="">863</td><td role="">MS-DOS Canadian French</td></tr><tr><td role="">53</td><td role="">862</td><td role="">Hebrew</td></tr><tr><td role="">54</td><td role="">861</td><td role="">MS-DOS Icelandic</td></tr><tr><td role="">55</td><td role="">860</td><td role="">MS-DOS Portuguese</td></tr><tr><td role="">56</td><td role="">857</td><td role="">IBM Turkish</td></tr><tr><td role="">57</td><td role="">855</td><td role="">IBM Cyrillic; primarily Russian</td></tr><tr><td role="">58</td><td role="">852</td><td role="">Latin 2</td></tr><tr><td role="">59</td><td role="">775</td><td role="">MS-DOS Baltic</td></tr><tr><td role="">60</td><td role="">737</td><td role="">Greek; former 437 G</td></tr><tr><td role="">61</td><td role="">708</td><td role="">Arabic; ASMO 708</td></tr><tr><td role="">62</td><td role="">850</td><td role="">WE/Latin 1</td></tr><tr><td role="">63</td><td role="">437</td><td role="">US</td></tr></tbody></table></div><h4><a name="idm320134082000"></a>sxHeight</h4><p role="">Format: SHORT</p><p role="">Description: This metric specifies the distance between
          the baseline and the approximate height of non-ascending
          lowercase letters measured in FUnits. This value would
          normally be specified by a type designer but in situations
          where that is not possible, for example when a legacy font
          is being converted, the value may be set equal to the top of
          the unscaled and unhinted glyph bounding box of the glyph
          encoded at U+0078 (LATIN SMALL LETTER X). If no glyph is
          encoded in this position the field should be set to
          0.</p><p role="">This metric, if specified, can be used in font
          substitution: the xHeight value of one font can be scaled to
          approximate the apparent size of another. </p><h4><a name="idm320134079680"></a>sCapHeight</h4><p role="">Format: SHORT</p><p role="">Description: This metric specifies the distance between
          the baseline and the approximate height of uppercase letters
          measured in FUnits. This value would normally be specified
          by a type designer but in situations where that is not
          possible, for example when a legacy font is being converted,
          the value may be set equal to the top of the unscaled and
          unhinted glyph bounding box of the glyph encoded at U+0048
          (LATIN CAPITAL LETTER H). If no glyph is encoded in this
          position the field should be set to 0.</p><p role="">This metric, if specified, can be used in systems that
          specify type size by capital height measured in millimeters.
          It can also be used as an alignment metric; the top of a
          drop capital, for instance, can be aligned to the sCapHeight
          metric of the first line of text. </p><h4><a name="idm320134077712"></a>usDefaultChar</h4><p role="">Format: USHORT</p><p role="">Description: Whenever a request is made for a character
          that is not in the font, Windows provides this default
          character. If the value of this field is zero, glyph ID 0 is
          to be used for the default character otherwise this is the
          Unicode encoding of the glyph that Windows uses as the
          default character. </p><h4><a name="idm320134076192"></a>usBreakChar</h4><p role="">Format: USHORT</p><p role="">Description: This is the Unicode encoding of the glyph
          that Windows uses as the break character. The break
          character is used to separate words and justify text. Most
          fonts specify 'space' as the break character.</p><h4><a name="idm320134074784"></a>usMaxContext</h4><p role="">Format: USHORT</p><p role="">Description: The maximum length of a target glyph
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
          considered.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="section.11.1.3"></a>Annotation</h3></div></div></div><p role="">Note that the usFirstCharIndex and usLastCharIndex are
        no longer very useful, since these fields are not big enough
        to represent Unicode supplemental characters.</p></div></div></div>