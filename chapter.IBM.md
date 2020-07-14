<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.IBM"></a>Chapter 12. IBM Font Class Parameters</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796415568"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.1.1"></a>Specification</h4></div></div></div><p>This section defines the IBM Font Class and the IBM Font
	  Subclass parameter values to be used in the classification
	  of font designs by the font designer or supplier. This
	  information is stored in the sFamilyClass field of a font's
	  OS/2 table.</p><p>sFamilyClass</p><p>Format: 2-byte signed short</p><p>Title: Font-family class and subclass. Also see section 3.4.</p><p>Description: This parameter is a classification of
	  font-family design.</p><p>Comments: The font class and font subclass are
	  registered values assigned by IBM to each font family. This
	  parameter is intended for use in selecting an alternate font
	  when the requested font is not available. The font class is
	  the most general and the font subclass is the most
	  specific. The high byte of this field contains the family
	  class, while the low byte contains the family
	  subclass.</p><p>These values classify a font design as to its
	  appearance, but do not identify the specific font family,
	  typeface variation, designer, supplier, size, or metric
	  table differences. It should be noted that some font designs
	  may be classified equally well into more than IBM Font Class
	  or Subclass. Such designs should be matched to a
	  classification for which substitution of another font design
	  from the same class or subclass would generally result in a
	  similar appearance of the presented document.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796409216"></a>Class ID = 0 No Classification</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.2.1"></a>Specification</h4></div></div></div><p>This class ID is used to indicate that the associated
	font has no design classification or that the design
	classification is not of significance to the creator or user
	of the font resource.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796406240"></a>Class ID = 1 Oldstyle Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.3.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
	style of the 15th to 17th century, with a mild diagonal
	contrast in stroke emphasis (lighter in upper left to lower
	right, heavier in upper right to lower left) and bracketed
	serifs. This IBM Class reflects the ISO Serif Class, Oldstyle
	and Legibility Subclasses as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272796403648"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	subclassification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272796402624"></a>Subclass ID = 1 : IBM Rounded Legibility</h5><p>This style is generally characterized by a large
	x-height, with short ascenders and descenders. Specifically,
	it is distinguished by a medium resolution, hand tuned, bitmap
	rendition of the more general rounded legibility subclass. An
	example of this font style is the IBM Sonoran Serif
	family. This IBM Subclass reflects the ISO Serif Class,
	Legibility Subclass, and Rounded Specific Group as documented
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796401344"></a>Subclass ID = 2 : Garalde</h5><p>This style is generally characterized by a medium
	x-height, with tall ascenders. An example of this font style
	is the ITC Garamond family. This IBM Subclass reflects the ISO
	Serif Class, Oldstyle Subclass, and Garalde Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796400240"></a>Subclass ID = 3 : Venetian</h5><p>This style is generally characterized by a medium
	x-height, with a relatively monotone appearance and sweeping
	tails based on the designs of the early Venetian printers. An
	example of this font style is the Goudy family. This IBM
	Subclass reflects the ISO Serif Class, Oldstyle Subclass, and
	Venetian Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272796399056"></a>Subclass ID = 4 : Modified Venetian</h5><p>This style is generally characterized by a large
	x-height, with a relatively monotone appearance and sweeping
	tails based on the designs of the early Venetian printers. An
	example of this font style is the Allied Linotype Palatino
	family. This IBM Subclass reflects the ISO Serif Class,
	Transitional Subclass, and Modified Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796397824"></a>Subclass ID = 5 : Dutch Modern</h5><p>This style is generally characterized by a large
	x-height, with wedge shaped serifs and a circular appearance
	to the bowls similar to the Dutch Traditional Subclass below,
	but with lighter stokes. An example of this font style is the
	Monotype Times New Roman family. This IBM Subclass reflects
	the ISO Serif Class, Oldstyle Subclass, and Dutch Specific
	Group as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272796396592"></a>Subclass ID = 6 : Dutch Traditional</h5><p>This style is generally characterized by a large
	x-height, with wedge shaped serifs and a circular appearance
	of the bowls. An example of this font style is the IBM Press
	Roman family. This IBM Subclass reflects the ISO Serif Class
	and Legibility Subclass as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272796395456"></a>Subclass ID = 7 : Contemporary</h5><p>This style is generally characterized by a small
	x-height, with light stokes and serifs. An example of this
	font style is the University family. This IBM Subclass
	reflects the ISO Serif Class and Contemporary Subclass as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796394368"></a>Subclass ID = 8 : Calligraphic</h5><p>This style is generally characterized by the fine hand
	writing style of calligraphy, while retaining the
	characteristic Oldstyle appearance. This IBM Subclass is not
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796393344"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272796392416"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796390912"></a>Class ID = 2 Transitional Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.4.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
	style of the 18th to 19th century, with a pronounced vertical
	contrast in stroke emphasis (vertical strokes being heavier
	than the horizontal strokes) and bracketed serifs. This IBM
	Class reflects the ISO Serif Class, Transitional Subclass as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796388320"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272796387296"></a>Subclass ID = 1 : Direct Line</h5><p>This style is generally characterized by a medium
	x-height, with fine serifs, noticeable contrast, and capitol
	letters of approximately the same width. An example of this
	font style is the Monotype Baskerville family. This IBM
	Subclass reflects the ISO Serif Class, Transitional Subclass,
	and Direct Line Specific Group as documented in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796386112"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
	script appearance while retaining the Transitional Direct Line
	style. An example of this font style is the IBM Nasseem
	(Arabic) family. This IBM Subclass is not specifically
	reflected in the 12/87 ISO/IEC 9541-5 draft standard, though
	the ISO Serif Class, Transitional Subclass, and Direct Line
	Specific Group would be a close approximation.</p><h5><a name="idm272796384896"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272796383968"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796382464"></a>Class ID = 3 Modern Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.5.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
	style of the 20th century, with an extreme contrast between
	the thick and thin portion of the strokes. This IBM Class
	reflects the ISO Serif Class, Modern Subclass as documented in
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796379968"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272796378944"></a>Subclass ID = 1 : Italian</h5><p>This style is generally characterized by a medium
	x-height, with thin hairline serifs. An example of this font
	style is the Monotype Bodoni family. This IBM Subclass
	reflects the ISO Serif Class, Modern Subclass, and Italian
	Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272796377840"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
	script appearance while retaining the Modern Italian style. An
	example of this font style is the IBM Narkissim (Hebrew)
	family. This IBM Subclass is not specifically reflected in the
	12/87 ISO/IEC 9541-5 draft standard, though the ISO Serif
	Class, Modern Subclass, and Italian Specific Group would be a
	close approximation.</p><h5><a name="idm272796376640"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272796375712"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272796374208"></a>Class ID = 4 Clarendon Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.6.1"></a>Specification</h4></div></div></div><p>This style is a variation of the Oldstyle Serifs and the
	Transitional Serifs, with a mild vertical stroke contrast and
	bracketed serifs. This IBM Class reflects the ISO Serif Class,
	Square Serif Subclass as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272796371728"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272796370704"></a>Subclass ID = 1 : Clarendon</h5><p>This style is generally characterized by a large
	x-height, with serifs and strokes of equal weight. An example
	of this font style is the Allied Linotype Clarendon
	family. This IBM Subclass reflects the ISO Serif Class, Square
	Serif Subclass, and Clarendon Specific Group as documented in
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796369568"></a>Subclass ID = 2 : Modern</h5><p>This style is generally characterized by a large
	x-height, with serifs of a lighter weight than the strokes and
	the strokes of a lighter weight than the Traditional. An
	example of this font style is the Monotype Century Schoolbook
	family. This IBM Subclass reflects the ISO Serif Class, Square
	Serif Subclass, and Clarendon Specific Group as documented in
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272796368352"></a>Subclass ID = 3 : Traditional</h5><p>This style is generally characterized by a large
	x-height, with serifs of a lighter weight than the strokes. An
	example of this font style is the Monotype Century family.This
	IBM Subclass reflects the ISO Serif Class, Square Serif
	Subclass, and Clarendon Specific Group as documented in the
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272798637376"></a>Subclass ID = 4 : Newspaper</h5><p>This style is generally characterized by a large
	x-height, with a simpler style of design and serifs of a
	lighter weight than the strokes. An example of this font style
	is the Allied Linotype Excelsior Family. This IBM Subclass
	reflects the ISO Serif Class, Square Serif Subclass, and
	Clarendon Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272857933104"></a>Subclass ID = 5 : Stub Serif</h5><p>This style is generally characterized by a large
	x-height, with short stub serifs and relatively bold stems. An
	example of this font style is the Cheltenham Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Short Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272857998336"></a>Subclass ID = 6 : Monotone</h5><p>This style is generally characterized by a large
	x-height, with monotone stems. An example of this font style
	is the ITC Korinna Family. This IBM Subclass reflects the ISO
	Serif Class, Square Serif Subclass, and Monotone Specific
	Group as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272809516960"></a>Subclass ID = 7 : Typewriter</h5><p>This style is generally characterized by a large
	x-height, with moderate stroke thickness characteristic of a
	typewriter. An example of this font style is the Prestige
	Elite Family. This IBM Subclass reflects the ISO Serif Class,
	Square Serif Subclass, and Typewriter Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809528176"></a>Subclass ID = 8-14: (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809535008"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809550016"></a>Class ID = 5 Slab Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.7.1"></a>Specification</h4></div></div></div><p>This style is characterized by serifs with a square
	transition between the strokes and the serifs (no
	brackets). This IBM Class reflects the ISO Serif Class, Square
	Serif Subclass (except the Clarendon Specific Group) as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809571904"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272809581280"></a>Subclass ID = 1 : Monotone</h5><p>This style is generally characterized by a large
	x-height, with serifs and strokes of equal weight. An example
	of this font style is the ITC Lubalin Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809587392"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
	x-height, with serifs of lighter weight that the strokes. An
	example of this font style is the Candida Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809597888"></a>Subclass ID = 3 : Geometric</h5><p>This style is generally characterized by a large
	x-height, with serifs and strokes of equal weight and a
	geometric (circles and lines) design. An example of this font
	style is the Monotype Rockwell Family. This IBM Subclass
	reflects the ISO Serif Class, Square Serif Subclass, and
	Monotone Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809602768"></a>Subclass ID = 4 : Swiss</h5><p>This style is generally characterized by a large
	x-height, with serifs and strokes of equal weight and an
	emphasis on the white space of the characters. An example of
	this font style is the Allied Linotype Serifa Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809608480"></a>Subclass ID = 5 : Typewriter</h5><p>This style is generally characterized by a large
	x-height, with serifs and strokes of equal but moderate
	thickness, and a geometric design. An example of this font
	style is the IBM Courier Family. This IBM Subclass reflects
	the ISO Serif Class, Square Serif Subclass, and Monotone
	Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272809617024"></a>Subclass ID = 6-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809624352"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272810039360"></a>Class ID = 6 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.8.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809914320"></a>Class ID = 7 Freeform Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.9.1"></a>Specification</h4></div></div></div><p>This style includes serifs, but which expresses a design
	freedom that does not generally fit within the other serif
	design classifications. This IBM Class reflects the remaining
	ISO Serif Class subclasses as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809802432"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272810025536"></a>Subclass ID = 1 : Modern</h5><p>This style is generally characterized by a medium
	x-height, with light contrast in the strokes and a round full
	design. An example of this font style is the ITC Souvenir
	Family. This IBM Subclass is not reflected in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809517664"></a>Subclass ID = 2-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809527088"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809537184"></a>Class ID = 8 Sans Serif</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.10.1"></a>Specification</h4></div></div></div><p>This style includes most basic letter forms (excluding
	Scripts and Ornamentals) that do not have serifs on the
	strokes. This IBM Class reflects the ISO Sans Serif Class as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809559904"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272809573472"></a>Subclass ID = 1 : IBM Neo-grotesque Gothic</h5><p>This style is generally characterized by a large
	x-height, with uniform stroke width and a simple one story
	design distinguished by a medium resolution, hand tuned,
	bitmap rendition of the more general Neo-grotesque Gothic
	Subclass. An example of this font style is the IBM Sonoran
	Sans Serif family. This IBM Subclass reflects the ISO Sans
	Serif Class, Gothic Subclass, and Neo-grotesque Specific Group
	as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272809575776"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
	x-height, with light contrast in the strokes and a classic
	Roman letterform. An example of this font style is the Allied
	Linotype Optima family. This IBM Subclass reflects the ISO
	Sans Serif Class, Humanist Subclass as documented in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809580576"></a>Subclass ID = 3 : Low-x Round Geometric</h5><p>This style is generally characterized by a low x-height,
	with monotone stroke weight and a round geometric design. An
	example of this font style is the Fundicion Tipograficia
	Neufville Futura family. This IBM Subclass reflects the ISO
	Sans Serif Class, Geometric Subclass, Round Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809586208"></a>Subclass ID = 4 : High-x Round Geometric</h5><p>This style is generally characterized by a high
	x-height, with uniform stroke weight and a round geometric
	design. An example of this font style is the ITC Avant Garde
	Gothic family. This IBM Subclass reflects the ISO Sans Serif
	Class, Geometric Subclass, Round Specific Group as documented
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809597280"></a>Subclass ID = 5 : Neo-grotesque Gothic</h5><p>This style is generally characterized by a high
	x-height, with uniform stroke width and a simple one story
	design. An example of this font style is the Allied Linotype
	Helvetica family. This IBM Subclass reflects the ISO Sans
	Serif Class, Gothic Subclass, Neo-grotesque Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809603376"></a>Subclass ID = 6 : Modified Neo-grotesque Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
	with design variations to the G and Q. An example of this font
	style is the Allied Linotype Univers family. This IBM Subclass
	reflects the ISO Sans Serif Class, Gothic Subclass,
	Neo-grotesque Specific Group as documented in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809610528"></a>Subclass ID = 7-8 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809612704"></a>Subclass ID = 9 : Typewriter Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
	with moderate stroke thickness characteristic of a
	typewriter. An example of this font style is the IBM Letter
	Gothic family. This IBM Subclass reflects the ISO Sans Serif
	Class, Gothic Subclass, Typewriter Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809617504"></a>Subclass ID = 10 : Matrix</h5><p>This style is generally a simple design characteristic
	of a dot matrix printer. An example of this font style is the
	IBM Matrix Gothic family. This IBM Subclass is not reflected
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272810031536"></a>Subclass ID = 11-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809613696"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809595584"></a>Class ID = 9 Ornamentals</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.11.1"></a>Specification</h4></div></div></div><p>This style includes highly decorated or stylized
	character shapes that are typically used in headlines. This
	IBM Class reflects the ISO Ornamental Class and the ISO
	Blackletter Class as documented in the 12/87 ISO/IEC 9541-5
	draft standard.</p><h5><a name="idm272809512848"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272809511872"></a>Subclass ID = 1 : Engraver</h5><p>This style is characterized by fine lines or lines
	engraved on the stems. An example of this font style is the
	Copperplate family. This IBM Subclass reflects the ISO
	Ornamental Class and Inline Subclass, or the Serif Class and
	Engraving Subclass as documented in the 12/87 ISO/IEC 9541-5
	draft standard.</p><h5><a name="idm272809510784"></a>Subclass ID = 2 : Black Letter</h5><p>This style is generally based upon the printing style of
	the German monasteries and printers of the 12th to 15th
	centuries. An example of this font style is the Old English
	family. This IBM Subclass reflects the ISO Blackletters Class
	as documented in the 12/87 ISO/IEC 9541-5 draft
	standard.</p><h5><a name="idm272809509712"></a>Subclass ID = 3 : Decorative</h5><p>This style is characterized by ornamental designs
	(typically from nature, such as leaves, flowers, animals,
	etc.) incorporated into the stems and strokes of the
	characters. An example of this font style is the Saphire
	family. This IBM Subclass reflects the ISO Ornamental Class
	and Decorative Subclass as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm272809508576"></a>Subclass ID = 4 : Three Dimensional</h5><p>This style is characterized by a three dimensional
	(raised) appearance of the characters created by shading or
	geometric effects. An example of this font style is the Thorne
	Shaded family. This IBM Subclass reflects the ISO Ornamental
	Class and Three Dimensional Subclass as documented in the
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809507472"></a>Subclass ID = 5-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272809506592"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809505312"></a>Class ID = 10 Scripts</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.12.1"></a>Specification</h4></div></div></div><p>This style includes those typefaces that are
	    designed to simulate handwriting. This IBM Class reflects
	    the ISO Script Class and Uncial Class as documented in the
	    12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809503008"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the
	    associated font has no design sub-classification or that
	    the design sub-classification is not of significance to
	    the creator or user of the font resource.</p><h5><a name="idm272809502016"></a>Subclass ID = 1 : Uncial</h5><p>This style is characterized by unjoined
	    (nonconnecting) characters that are generally based on the
	    hand writing style of Europe in the 6th to 9th
	    centuries. An example of this font style is the Libra
	    family. This IBM Subclass reflects the ISO Uncial Class as
	    documented in the 12/87 ISO/IEC 9541-5 draft
	    standard.</p><h5><a name="idm272809500896"></a>Subclass ID = 2 : Brush Joined</h5><p>This style is characterized by joined (connecting)
	    characters that have the appearance of being painted with
	    a brush, with moderate contrast between thick and thin
	    strokes. An example of this font style is the Mistral
	    family. This IBM Subclass reflects the ISO Script Class,
	    Joined Subclass, and Informal Specific Group as documented
	    in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809499712"></a>Subclass ID = 3 : Formal Joined</h5><p>This style is characterized by joined (connecting)
	    characters that have a printed (or drawn with a stiff
	    brush) appearance with extreme contrast between the thick
	    and thin strokes. An example of this font style is the
	    Coronet family. This IBM Subclass reflects the ISO Script
	    Class, Joined Subclass, and Formal Specific Group as
	    documented in the 12/87 ISO/IEC 9541-5 draft
	    standard.</p><h5><a name="idm272809498096"></a>Subclass ID = 4 : Monotone Joined</h5><p>This style is characterized by joined (connecting)
	    characters that have a uniform appearance with little or
	    no contrast in the strokes. An example of this font style
	    is the Kaufmann family. This IBM Subclass reflects the ISO
	    Script Class, Joined Subclass, and Monotone Specific Group
	    as documented in the 12/87 ISO/IEC 9541-5 draft
	    standard.</p><h5><a name="idm272809496944"></a>Subclass ID = 5 : Calligraphic</h5><p>This style is characterized by beautifully hand
	    drawn, unjoined (non-connecting) characters that have an
	    appearance of being drawn with a broad edge pen. An
	    example of this font style is the Thompson Quillscript
	    family. This IBM Subclass reflects the ISO Script Class,
	    Unjoined Subclass, and Calligraphic Specific Group as
	    documented in the 12/87 ISO/IEC 9541-5 draft
	    standard.</p><h5><a name="idm272809495760"></a>Subclass ID = 6 : Brush Unjoined</h5><p>This style is characterized by unjoined
	    (non-connecting) characters that have the appearance of
	    being painted with a brush, with moderate contrast between
	    thick and thin strokes. An example of this font style is
	    the Saltino family. This IBM Subclass reflects the ISO
	    Script Class, Unjoined Subclass, and Brush Specific Group
	    as documented in the 12/87 ISO/IEC 9541-5 draft
	    standard.</p><h5><a name="idm272809494560"></a>Subclass ID = 7 : Formal Unjoined</h5><p>This style is characterized by unjoined
	    (non-connecting) characters that have a printed (or drawn
	    with a stiff brush) appearance with extreme contrast
	    between the thick and thin strokes. An example of this
	    font style is the Virtuosa family. This IBM Subclass
	    reflects the ISO Script Class, Unjoined Subclass, and
	    Formal Specific Group as documented in the 12/87 ISO/IEC
	    9541-5 draft standard.</p><h5><a name="idm272809493360"></a>Subclass ID = 8 : Monotone Unjoined</h5><p>This style is characterized by unjoined
	    (non-connecting) characters that have a uniform appearance
	    with little or no contrast in the strokes. An example of
	    this font style is the Gilles Gothic family. This IBM
	    Subclass reflects the ISO Script Class, Unjoined Subclass,
	    and Monotone Specific Group as documented in the 12/87
	    ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272809492192"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future
	    assignment, and shall not be used without formal
	    assignment by IBM.</p><h5><a name="idm272809491296"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	  the associated design class that are not covered by another
	  Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809490000"></a>Class ID = 11 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.13.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272809487424"></a>Class ID = 12 Symbolic</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.14.1"></a>Specification</h4></div></div></div><p>This style is generally design independent, making it
	suitable for Pi and special characters (icons, dingbats,
	technical symbols, etc.) that may be used equally well with
	any font. This IBM Class reflects various ISO Specific Groups,
	as noted below and documented in the 12/87 ISO/IEC 9541-5
	draft standard.</p><h5><a name="idm272809484704"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm272798652000"></a>Subclass ID = 1-2 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272798664624"></a>Subclass ID = 3 : Mixed Serif</h5><p>This style is characterized by either both or a
	combination of serif and sans serif designs on those
	characters of the font for which design is important (e.g.,
	superscript and subscript characters, numbers, copyright or
	trademark symbols, etc.). An example of this font style is
	found in the IBM Symbol family. This IBM Subclass is not
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm272798514128"></a>Subclass ID = 4-5 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272798549664"></a>Subclass ID = 6 : Oldstyle Serif</h5><p>This style is characterized by a Oldstyle Serif IBM
	Class design on those characters of the font for which design
	is important (e.g., superscript and subscript characters,
	numbers, copyright or trademark symbols, etc.). An example of
	this font style is found in the IBM Sonoran Pi Serif
	family. This IBM Subclass is not directly reflected in the
	12/87 ISO/IEC 9541-5 draft standard, though it is indirectly
	by the ISO Serif Class and Legibility Subclass (implies that
	all characters of the font exhibit the design appearance,
	while only a subset of the characters actually exhibit the
	design).</p><h5><a name="idm272798542064"></a>Subclass ID = 7 : Neo-grotesque Sans Serif</h5><p>This style is characterized by a Neo-grotesque Sans
	Serif IBM Font Class and Subclass design on those characters
	of the font for which design is important (e.g., superscript
	and subscript characters, numbers, copyright or trademark
	symbols, etc.). An example of this font style is found in the
	IBM Sonoran Pi Sans Serif family. This IBM Subclass is not
	directly reflected in the 12/87 ISO/IEC 9541-5 draft standard,
	though it is indirectly by the ISO Sans Serif Class and Gothic
	Subclass (implies that all characters of the font exhibit the
	design appearance, while only a subset of the characters
	actually exhibit the design).</p><h5><a name="idm272798569792"></a>Subclass ID = 8-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm272798563024"></a>Subclass ID = 15 :Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272798598816"></a>Class ID = 13 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.15.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm272798470736"></a>Class ID = 14 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.16.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div></div>