<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.IBM"></a>Chapter 12. IBM Font Class Parameters</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5548"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.1.1"></a>Specification</h4></div></div></div><p>This section defines the IBM Font Class and the IBM Font
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.IBM"></a>Chapter 12. IBM Font Class Parameters</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299527680"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.1.1"></a>Specification</h4></div></div></div><p>This section defines the IBM Font Class and the IBM Font
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.IBM"></a>Chapter 12. IBM Font Class Parameters</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62732106336"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.1.1"></a>Specification</h4></div></div></div><p>This section defines the IBM Font Class and the IBM Font
>>>>>>> Rebuild
=======
<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.IBM"></a>Chapter 12. IBM Font Class Parameters</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835991376"></a>Introduction</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.1.1"></a>Specification</h4></div></div></div><p>This section defines the IBM Font Class and the IBM Font
>>>>>>> Rebuild
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
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	  similar appearance of the presented document.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5559"></a>Class ID = 0 No Classification</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.2.1"></a>Specification</h4></div></div></div><p>This class ID is used to indicate that the associated
	font has no design classification or that the design
	classification is not of significance to the creator or user
	of the font resource.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5564"></a>Class ID = 1 Oldstyle Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.3.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
=======
	  similar appearance of the presented document.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299521648"></a>Class ID = 0 No Classification</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.2.1"></a>Specification</h4></div></div></div><p>This class ID is used to indicate that the associated
	font has no design classification or that the design
	classification is not of significance to the creator or user
	of the font resource.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299518896"></a>Class ID = 1 Oldstyle Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.3.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
=======
	  similar appearance of the presented document.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62732100464"></a>Class ID = 0 No Classification</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.2.1"></a>Specification</h4></div></div></div><p>This class ID is used to indicate that the associated
	font has no design classification or that the design
	classification is not of significance to the creator or user
	of the font resource.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62732097792"></a>Class ID = 1 Oldstyle Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.3.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
=======
	  similar appearance of the presented document.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835985024"></a>Class ID = 0 No Classification</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.2.1"></a>Specification</h4></div></div></div><p>This class ID is used to indicate that the associated
	font has no design classification or that the design
	classification is not of significance to the creator or user
	of the font resource.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835982048"></a>Class ID = 1 Oldstyle Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.3.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
	style of the 15th to 17th century, with a mild diagonal
	contrast in stroke emphasis (lighter in upper left to lower
	right, heavier in upper right to lower left) and bracketed
	serifs. This IBM Class reflects the ISO Serif Class, Oldstyle
	and Legibility Subclasses as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5569"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	subclassification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5571"></a>Subclass ID = 1 : IBM Rounded Legibility</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299516432"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	subclassification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm189299515456"></a>Subclass ID = 1 : IBM Rounded Legibility</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732095328"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	subclassification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm62732094352"></a>Subclass ID = 1 : IBM Rounded Legibility</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835979456"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	subclassification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm465835978432"></a>Subclass ID = 1 : IBM Rounded Legibility</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with short ascenders and descenders. Specifically,
	it is distinguished by a medium resolution, hand tuned, bitmap
	rendition of the more general rounded legibility subclass. An
	example of this font style is the IBM Sonoran Serif
	family. This IBM Subclass reflects the ISO Serif Class,
	Legibility Subclass, and Rounded Specific Group as documented
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5573"></a>Subclass ID = 2 : Garalde</h5><p>This style is generally characterized by a medium
	x-height, with tall ascenders. An example of this font style
	is the ITC Garamond family. This IBM Subclass reflects the ISO
	Serif Class, Oldstyle Subclass, and Garalde Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5575"></a>Subclass ID = 3 : Venetian</h5><p>This style is generally characterized by a medium
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299514224"></a>Subclass ID = 2 : Garalde</h5><p>This style is generally characterized by a medium
	x-height, with tall ascenders. An example of this font style
	is the ITC Garamond family. This IBM Subclass reflects the ISO
	Serif Class, Oldstyle Subclass, and Garalde Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299513152"></a>Subclass ID = 3 : Venetian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732093120"></a>Subclass ID = 2 : Garalde</h5><p>This style is generally characterized by a medium
	x-height, with tall ascenders. An example of this font style
	is the ITC Garamond family. This IBM Subclass reflects the ISO
	Serif Class, Oldstyle Subclass, and Garalde Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732092048"></a>Subclass ID = 3 : Venetian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835977152"></a>Subclass ID = 2 : Garalde</h5><p>This style is generally characterized by a medium
	x-height, with tall ascenders. An example of this font style
	is the ITC Garamond family. This IBM Subclass reflects the ISO
	Serif Class, Oldstyle Subclass, and Garalde Specific Group as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835976048"></a>Subclass ID = 3 : Venetian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
	x-height, with a relatively monotone appearance and sweeping
	tails based on the designs of the early Venetian printers. An
	example of this font style is the Goudy family. This IBM
	Subclass reflects the ISO Serif Class, Oldstyle Subclass, and
	Venetian Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5577"></a>Subclass ID = 4 : Modified Venetian</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299512000"></a>Subclass ID = 4 : Modified Venetian</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732090896"></a>Subclass ID = 4 : Modified Venetian</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835974864"></a>Subclass ID = 4 : Modified Venetian</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with a relatively monotone appearance and sweeping
	tails based on the designs of the early Venetian printers. An
	example of this font style is the Allied Linotype Palatino
	family. This IBM Subclass reflects the ISO Serif Class,
	Transitional Subclass, and Modified Specific Group as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5579"></a>Subclass ID = 5 : Dutch Modern</h5><p>This style is generally characterized by a large
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299510816"></a>Subclass ID = 5 : Dutch Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732089712"></a>Subclass ID = 5 : Dutch Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835973632"></a>Subclass ID = 5 : Dutch Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with wedge shaped serifs and a circular appearance
	to the bowls similar to the Dutch Traditional Subclass below,
	but with lighter stokes. An example of this font style is the
	Monotype Times New Roman family. This IBM Subclass reflects
	the ISO Serif Class, Oldstyle Subclass, and Dutch Specific
	Group as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5581"></a>Subclass ID = 6 : Dutch Traditional</h5><p>This style is generally characterized by a large
=======
	standard.</p><h5><a name="idm189299509616"></a>Subclass ID = 6 : Dutch Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm62732088512"></a>Subclass ID = 6 : Dutch Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835972400"></a>Subclass ID = 6 : Dutch Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with wedge shaped serifs and a circular appearance
	of the bowls. An example of this font style is the IBM Press
	Roman family. This IBM Subclass reflects the ISO Serif Class
	and Legibility Subclass as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5583"></a>Subclass ID = 7 : Contemporary</h5><p>This style is generally characterized by a small
	x-height, with light stokes and serifs. An example of this
	font style is the University family. This IBM Subclass
	reflects the ISO Serif Class and Contemporary Subclass as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5585"></a>Subclass ID = 8 : Calligraphic</h5><p>This style is generally characterized by the fine hand
	writing style of calligraphy, while retaining the
	characteristic Oldstyle appearance. This IBM Subclass is not
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5587"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5589"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5591"></a>Class ID = 2 Transitional Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.4.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
=======
	9541-5 draft standard.</p><h5><a name="idm189299508528"></a>Subclass ID = 7 : Contemporary</h5><p>This style is generally characterized by a small
=======
	9541-5 draft standard.</p><h5><a name="idm62732087424"></a>Subclass ID = 7 : Contemporary</h5><p>This style is generally characterized by a small
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835971264"></a>Subclass ID = 7 : Contemporary</h5><p>This style is generally characterized by a small
>>>>>>> Rebuild
	x-height, with light stokes and serifs. An example of this
	font style is the University family. This IBM Subclass
	reflects the ISO Serif Class and Contemporary Subclass as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835970176"></a>Subclass ID = 8 : Calligraphic</h5><p>This style is generally characterized by the fine hand
	writing style of calligraphy, while retaining the
	characteristic Oldstyle appearance. This IBM Subclass is not
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835969152"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835968224"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
<<<<<<< HEAD
<<<<<<< HEAD
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299504240"></a>Class ID = 2 Transitional Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.4.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
=======
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62732083216"></a>Class ID = 2 Transitional Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.4.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
=======
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835966720"></a>Class ID = 2 Transitional Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.4.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
>>>>>>> Rebuild
	style of the 18th to 19th century, with a pronounced vertical
	contrast in stroke emphasis (vertical strokes being heavier
	than the horizontal strokes) and bracketed serifs. This IBM
	Class reflects the ISO Serif Class, Transitional Subclass as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5596"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5598"></a>Subclass ID = 1 : Direct Line</h5><p>This style is generally characterized by a medium
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299501792"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm189299500816"></a>Subclass ID = 1 : Direct Line</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732080768"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm62732079792"></a>Subclass ID = 1 : Direct Line</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835964128"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm465835963104"></a>Subclass ID = 1 : Direct Line</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
	x-height, with fine serifs, noticeable contrast, and capitol
	letters of approximately the same width. An example of this
	font style is the Monotype Baskerville family. This IBM
	Subclass reflects the ISO Serif Class, Transitional Subclass,
	and Direct Line Specific Group as documented in the 12/87
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5600"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299499664"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732078640"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835961920"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
	script appearance while retaining the Transitional Direct Line
	style. An example of this font style is the IBM Nasseem
	(Arabic) family. This IBM Subclass is not specifically
	reflected in the 12/87 ISO/IEC 9541-5 draft standard, though
	the ISO Serif Class, Transitional Subclass, and Direct Line
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	Specific Group would be a close approximation.</p><h5><a name="idm5602"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5604"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5606"></a>Class ID = 3 Modern Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.5.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
	style of the 20th century, with an extreme contrast between
	the thick and thin portion of the strokes. This IBM Class
	reflects the ISO Serif Class, Modern Subclass as documented in
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5611"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5613"></a>Subclass ID = 1 : Italian</h5><p>This style is generally characterized by a medium
=======
	Specific Group would be a close approximation.</p><h5><a name="idm189299498480"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299497600"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
=======
	Specific Group would be a close approximation.</p><h5><a name="idm62732077456"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732076576"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
=======
	Specific Group would be a close approximation.</p><h5><a name="idm465835960704"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835959776"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835958272"></a>Class ID = 3 Modern Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.5.1"></a>Specification</h4></div></div></div><p>This style is generally based upon the Latin printing
	style of the 20th century, with an extreme contrast between
	the thick and thin portion of the strokes. This IBM Class
	reflects the ISO Serif Class, Modern Subclass as documented in
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835955776"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
<<<<<<< HEAD
<<<<<<< HEAD
	user of the font resource.</p><h5><a name="idm189299492896"></a>Subclass ID = 1 : Italian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm62732071952"></a>Subclass ID = 1 : Italian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm465835954752"></a>Subclass ID = 1 : Italian</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
	x-height, with thin hairline serifs. An example of this font
	style is the Monotype Bodoni family. This IBM Subclass
	reflects the ISO Serif Class, Modern Subclass, and Italian
	Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5615"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
=======
	standard.</p><h5><a name="idm189299491824"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm62732070880"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835953648"></a>Subclass ID = 2 : Script</h5><p>This style is generally characterized by a hand written
>>>>>>> Rebuild
	script appearance while retaining the Modern Italian style. An
	example of this font style is the IBM Narkissim (Hebrew)
	family. This IBM Subclass is not specifically reflected in the
	12/87 ISO/IEC 9541-5 draft standard, though the ISO Serif
	Class, Modern Subclass, and Italian Specific Group would be a
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	close approximation.</p><h5><a name="idm5617"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5619"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5621"></a>Class ID = 4 Clarendon Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.6.1"></a>Specification</h4></div></div></div><p>This style is a variation of the Oldstyle Serifs and the
	Transitional Serifs, with a mild vertical stroke contrast and
	bracketed serifs. This IBM Class reflects the ISO Serif Class,
	Square Serif Subclass as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm5626"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5628"></a>Subclass ID = 1 : Clarendon</h5><p>This style is generally characterized by a large
=======
	close approximation.</p><h5><a name="idm189299490656"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299489776"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
=======
	close approximation.</p><h5><a name="idm62732069712"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732068832"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
=======
	close approximation.</p><h5><a name="idm465835952448"></a>Subclass ID = 3-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835951520"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835950016"></a>Class ID = 4 Clarendon Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.6.1"></a>Specification</h4></div></div></div><p>This style is a variation of the Oldstyle Serifs and the
	Transitional Serifs, with a mild vertical stroke contrast and
	bracketed serifs. This IBM Class reflects the ISO Serif Class,
	Square Serif Subclass as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm465835947536"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
<<<<<<< HEAD
<<<<<<< HEAD
	user of the font resource.</p><h5><a name="idm189299485088"></a>Subclass ID = 1 : Clarendon</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm62732064224"></a>Subclass ID = 1 : Clarendon</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm465835946512"></a>Subclass ID = 1 : Clarendon</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs and strokes of equal weight. An example
	of this font style is the Allied Linotype Clarendon
	family. This IBM Subclass reflects the ISO Serif Class, Square
	Serif Subclass, and Clarendon Specific Group as documented in
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5630"></a>Subclass ID = 2 : Modern</h5><p>This style is generally characterized by a large
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299483984"></a>Subclass ID = 2 : Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732063120"></a>Subclass ID = 2 : Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835945376"></a>Subclass ID = 2 : Modern</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs of a lighter weight than the strokes and
	the strokes of a lighter weight than the Traditional. An
	example of this font style is the Monotype Century Schoolbook
	family. This IBM Subclass reflects the ISO Serif Class, Square
	Serif Subclass, and Clarendon Specific Group as documented in
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5632"></a>Subclass ID = 3 : Traditional</h5><p>This style is generally characterized by a large
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299482800"></a>Subclass ID = 3 : Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732061936"></a>Subclass ID = 3 : Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835944160"></a>Subclass ID = 3 : Traditional</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs of a lighter weight than the strokes. An
	example of this font style is the Monotype Century family.This
	IBM Subclass reflects the ISO Serif Class, Square Serif
	Subclass, and Clarendon Specific Group as documented in the
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5634"></a>Subclass ID = 4 : Newspaper</h5><p>This style is generally characterized by a large
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299481696"></a>Subclass ID = 4 : Newspaper</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732060832"></a>Subclass ID = 4 : Newspaper</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835943024"></a>Subclass ID = 4 : Newspaper</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with a simpler style of design and serifs of a
	lighter weight than the strokes. An example of this font style
	is the Allied Linotype Excelsior Family. This IBM Subclass
	reflects the ISO Serif Class, Square Serif Subclass, and
	Clarendon Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5636"></a>Subclass ID = 5 : Stub Serif</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299480544"></a>Subclass ID = 5 : Stub Serif</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732059680"></a>Subclass ID = 5 : Stub Serif</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835941840"></a>Subclass ID = 5 : Stub Serif</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with short stub serifs and relatively bold stems. An
	example of this font style is the Cheltenham Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Short Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5638"></a>Subclass ID = 6 : Monotone</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299479440"></a>Subclass ID = 6 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732058576"></a>Subclass ID = 6 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835940704"></a>Subclass ID = 6 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with monotone stems. An example of this font style
	is the ITC Korinna Family. This IBM Subclass reflects the ISO
	Serif Class, Square Serif Subclass, and Monotone Specific
	Group as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5640"></a>Subclass ID = 7 : Typewriter</h5><p>This style is generally characterized by a large
=======
	standard.</p><h5><a name="idm189299478064"></a>Subclass ID = 7 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm62732057200"></a>Subclass ID = 7 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835939296"></a>Subclass ID = 7 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with moderate stroke thickness characteristic of a
	typewriter. An example of this font style is the Prestige
	Elite Family. This IBM Subclass reflects the ISO Serif Class,
	Square Serif Subclass, and Typewriter Specific Group as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5642"></a>Subclass ID = 8-14: (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5644"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5646"></a>Class ID = 5 Slab Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.7.1"></a>Specification</h4></div></div></div><p>This style is characterized by serifs with a square
	transition between the strokes and the serifs (no
	brackets). This IBM Class reflects the ISO Serif Class, Square
	Serif Subclass (except the Clarendon Specific Group) as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5651"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5653"></a>Subclass ID = 1 : Monotone</h5><p>This style is generally characterized by a large
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299476944"></a>Subclass ID = 8-14: (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299476064"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732056080"></a>Subclass ID = 8-14: (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732055200"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835938144"></a>Subclass ID = 8-14: (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835937216"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835935712"></a>Class ID = 5 Slab Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.7.1"></a>Specification</h4></div></div></div><p>This style is characterized by serifs with a square
	transition between the strokes and the serifs (no
	brackets). This IBM Class reflects the ISO Serif Class, Square
	Serif Subclass (except the Clarendon Specific Group) as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835933216"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
<<<<<<< HEAD
<<<<<<< HEAD
	user of the font resource.</p><h5><a name="idm189299471360"></a>Subclass ID = 1 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm62732050576"></a>Subclass ID = 1 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm465835932192"></a>Subclass ID = 1 : Monotone</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs and strokes of equal weight. An example
	of this font style is the ITC Lubalin Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5655"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
=======
	9541-5 draft standard.</p><h5><a name="idm189299470272"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732049488"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835931072"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
	x-height, with serifs of lighter weight that the strokes. An
	example of this font style is the Candida Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5657"></a>Subclass ID = 3 : Geometric</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299469168"></a>Subclass ID = 3 : Geometric</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732048384"></a>Subclass ID = 3 : Geometric</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835929936"></a>Subclass ID = 3 : Geometric</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs and strokes of equal weight and a
	geometric (circles and lines) design. An example of this font
	style is the Monotype Rockwell Family. This IBM Subclass
	reflects the ISO Serif Class, Square Serif Subclass, and
	Monotone Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5659"></a>Subclass ID = 4 : Swiss</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299468016"></a>Subclass ID = 4 : Swiss</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732047232"></a>Subclass ID = 4 : Swiss</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835928752"></a>Subclass ID = 4 : Swiss</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs and strokes of equal weight and an
	emphasis on the white space of the characters. An example of
	this font style is the Allied Linotype Serifa Family. This IBM
	Subclass reflects the ISO Serif Class, Square Serif Subclass,
	and Monotone Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5661"></a>Subclass ID = 5 : Typewriter</h5><p>This style is generally characterized by a large
=======
	9541-5 draft standard.</p><h5><a name="idm189299466864"></a>Subclass ID = 5 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732046080"></a>Subclass ID = 5 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835927568"></a>Subclass ID = 5 : Typewriter</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with serifs and strokes of equal but moderate
	thickness, and a geometric design. An example of this font
	style is the IBM Courier Family. This IBM Subclass reflects
	the ISO Serif Class, Square Serif Subclass, and Monotone
	Specific Group as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5663"></a>Subclass ID = 6-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5665"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5667"></a>Class ID = 6 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.8.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5672"></a>Class ID = 7 Freeform Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.9.1"></a>Specification</h4></div></div></div><p>This style includes serifs, but which expresses a design
	freedom that does not generally fit within the other serif
	design classifications. This IBM Class reflects the remaining
	ISO Serif Class subclasses as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm5677"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5679"></a>Subclass ID = 1 : Modern</h5><p>This style is generally characterized by a medium
	x-height, with light contrast in the strokes and a round full
	design. An example of this font style is the ITC Souvenir
	Family. This IBM Subclass is not reflected in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5681"></a>Subclass ID = 2-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5683"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5685"></a>Class ID = 8 Sans Serif</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.10.1"></a>Specification</h4></div></div></div><p>This style includes most basic letter forms (excluding
	Scripts and Ornamentals) that do not have serifs on the
	strokes. This IBM Class reflects the ISO Sans Serif Class as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5690"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5692"></a>Subclass ID = 1 : IBM Neo-grotesque Gothic</h5><p>This style is generally characterized by a large
=======
	standard.</p><h5><a name="idm189299465728"></a>Subclass ID = 6-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299464848"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
=======
	standard.</p><h5><a name="idm62732044944"></a>Subclass ID = 6-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732044064"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835926400"></a>Subclass ID = 6-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835925472"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835923968"></a>Class ID = 6 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.8.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835921072"></a>Class ID = 7 Freeform Serifs</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.9.1"></a>Specification</h4></div></div></div><p>This style includes serifs, but which expresses a design
	freedom that does not generally fit within the other serif
	design classifications. This IBM Class reflects the remaining
	ISO Serif Class subclasses as documented in the 12/87 ISO/IEC
	9541-5 draft standard.</p><h5><a name="idm465835918592"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm465835917568"></a>Subclass ID = 1 : Modern</h5><p>This style is generally characterized by a medium
	x-height, with light contrast in the strokes and a round full
	design. An example of this font style is the ITC Souvenir
	Family. This IBM Subclass is not reflected in the 12/87
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835916496"></a>Subclass ID = 2-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835915568"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835914064"></a>Class ID = 8 Sans Serif</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.10.1"></a>Specification</h4></div></div></div><p>This style includes most basic letter forms (excluding
	Scripts and Ornamentals) that do not have serifs on the
	strokes. This IBM Class reflects the ISO Sans Serif Class as
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835911616"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
<<<<<<< HEAD
<<<<<<< HEAD
	user of the font resource.</p><h5><a name="idm189299450928"></a>Subclass ID = 1 : IBM Neo-grotesque Gothic</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm62732030384"></a>Subclass ID = 1 : IBM Neo-grotesque Gothic</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm465835910592"></a>Subclass ID = 1 : IBM Neo-grotesque Gothic</h5><p>This style is generally characterized by a large
>>>>>>> Rebuild
	x-height, with uniform stroke width and a simple one story
	design distinguished by a medium resolution, hand tuned,
	bitmap rendition of the more general Neo-grotesque Gothic
	Subclass. An example of this font style is the IBM Sonoran
	Sans Serif family. This IBM Subclass reflects the ISO Sans
	Serif Class, Gothic Subclass, and Neo-grotesque Specific Group
	as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5694"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
=======
	standard.</p><h5><a name="idm189299449680"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm62732029136"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835909296"></a>Subclass ID = 2 : Humanist</h5><p>This style is generally characterized by a medium
>>>>>>> Rebuild
	x-height, with light contrast in the strokes and a classic
	Roman letterform. An example of this font style is the Allied
	Linotype Optima family. This IBM Subclass reflects the ISO
	Sans Serif Class, Humanist Subclass as documented in the 12/87
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5696"></a>Subclass ID = 3 : Low-x Round Geometric</h5><p>This style is generally characterized by a low x-height,
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299448576"></a>Subclass ID = 3 : Low-x Round Geometric</h5><p>This style is generally characterized by a low x-height,
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732028032"></a>Subclass ID = 3 : Low-x Round Geometric</h5><p>This style is generally characterized by a low x-height,
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835908160"></a>Subclass ID = 3 : Low-x Round Geometric</h5><p>This style is generally characterized by a low x-height,
>>>>>>> Rebuild
	with monotone stroke weight and a round geometric design. An
	example of this font style is the Fundicion Tipograficia
	Neufville Futura family. This IBM Subclass reflects the ISO
	Sans Serif Class, Geometric Subclass, Round Specific Group as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5698"></a>Subclass ID = 4 : High-x Round Geometric</h5><p>This style is generally characterized by a high
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299447440"></a>Subclass ID = 4 : High-x Round Geometric</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732026896"></a>Subclass ID = 4 : High-x Round Geometric</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835906976"></a>Subclass ID = 4 : High-x Round Geometric</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
	x-height, with uniform stroke weight and a round geometric
	design. An example of this font style is the ITC Avant Garde
	Gothic family. This IBM Subclass reflects the ISO Sans Serif
	Class, Geometric Subclass, Round Specific Group as documented
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5700"></a>Subclass ID = 5 : Neo-grotesque Gothic</h5><p>This style is generally characterized by a high
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299446320"></a>Subclass ID = 5 : Neo-grotesque Gothic</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732025776"></a>Subclass ID = 5 : Neo-grotesque Gothic</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
=======
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835905808"></a>Subclass ID = 5 : Neo-grotesque Gothic</h5><p>This style is generally characterized by a high
>>>>>>> Rebuild
	x-height, with uniform stroke width and a simple one story
	design. An example of this font style is the Allied Linotype
	Helvetica family. This IBM Subclass reflects the ISO Sans
	Serif Class, Gothic Subclass, Neo-grotesque Specific Group as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5702"></a>Subclass ID = 6 : Modified Neo-grotesque Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299445200"></a>Subclass ID = 6 : Modified Neo-grotesque Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732024656"></a>Subclass ID = 6 : Modified Neo-grotesque Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835904640"></a>Subclass ID = 6 : Modified Neo-grotesque Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
	with design variations to the G and Q. An example of this font
	style is the Allied Linotype Univers family. This IBM Subclass
	reflects the ISO Sans Serif Class, Gothic Subclass,
	Neo-grotesque Specific Group as documented in the 12/87
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5704"></a>Subclass ID = 7-8 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5706"></a>Subclass ID = 9 : Typewriter Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299444096"></a>Subclass ID = 7-8 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299443216"></a>Subclass ID = 9 : Typewriter Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732023552"></a>Subclass ID = 7-8 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732022672"></a>Subclass ID = 9 : Typewriter Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
=======
	ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835903488"></a>Subclass ID = 7-8 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835902560"></a>Subclass ID = 9 : Typewriter Gothic</h5><p>This style is similar to the Neo-grotesque Gothic style,
>>>>>>> Rebuild
	with moderate stroke thickness characteristic of a
	typewriter. An example of this font style is the IBM Letter
	Gothic family. This IBM Subclass reflects the ISO Sans Serif
	Class, Gothic Subclass, Typewriter Specific Group as
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5708"></a>Subclass ID = 10 : Matrix</h5><p>This style is generally a simple design characteristic
	of a dot matrix printer. An example of this font style is the
	IBM Matrix Gothic family. This IBM Subclass is not reflected
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5710"></a>Subclass ID = 11-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5712"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5714"></a>Class ID = 9 Ornamentals</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.11.1"></a>Specification</h4></div></div></div><p>This style includes highly decorated or stylized
	character shapes that are typically used in headlines. This
	IBM Class reflects the ISO Ornamental Class and the ISO
	Blackletter Class as documented in the 12/87 ISO/IEC 9541-5
	draft standard.</p><h5><a name="idm5719"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5721"></a>Subclass ID = 1 : Engraver</h5><p>This style is characterized by fine lines or lines
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299442096"></a>Subclass ID = 10 : Matrix</h5><p>This style is generally a simple design characteristic
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732021552"></a>Subclass ID = 10 : Matrix</h5><p>This style is generally a simple design characteristic
>>>>>>> Rebuild
=======
	documented in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835901392"></a>Subclass ID = 10 : Matrix</h5><p>This style is generally a simple design characteristic
>>>>>>> Rebuild
	of a dot matrix printer. An example of this font style is the
	IBM Matrix Gothic family. This IBM Subclass is not reflected
	in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835900352"></a>Subclass ID = 11-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835899424"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835897920"></a>Class ID = 9 Ornamentals</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.11.1"></a>Specification</h4></div></div></div><p>This style includes highly decorated or stylized
	character shapes that are typically used in headlines. This
	IBM Class reflects the ISO Ornamental Class and the ISO
	Blackletter Class as documented in the 12/87 ISO/IEC 9541-5
	draft standard.</p><h5><a name="idm465835895456"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
<<<<<<< HEAD
<<<<<<< HEAD
	user of the font resource.</p><h5><a name="idm189299435536"></a>Subclass ID = 1 : Engraver</h5><p>This style is characterized by fine lines or lines
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm62732015072"></a>Subclass ID = 1 : Engraver</h5><p>This style is characterized by fine lines or lines
>>>>>>> Rebuild
=======
	user of the font resource.</p><h5><a name="idm465835894432"></a>Subclass ID = 1 : Engraver</h5><p>This style is characterized by fine lines or lines
>>>>>>> Rebuild
	engraved on the stems. An example of this font style is the
	Copperplate family. This IBM Subclass reflects the ISO
	Ornamental Class and Inline Subclass, or the Serif Class and
	Engraving Subclass as documented in the 12/87 ISO/IEC 9541-5
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	draft standard.</p><h5><a name="idm5723"></a>Subclass ID = 2 : Black Letter</h5><p>This style is generally based upon the printing style of
=======
	draft standard.</p><h5><a name="idm189299434448"></a>Subclass ID = 2 : Black Letter</h5><p>This style is generally based upon the printing style of
>>>>>>> Rebuild
=======
	draft standard.</p><h5><a name="idm62732013984"></a>Subclass ID = 2 : Black Letter</h5><p>This style is generally based upon the printing style of
>>>>>>> Rebuild
=======
	draft standard.</p><h5><a name="idm465835893312"></a>Subclass ID = 2 : Black Letter</h5><p>This style is generally based upon the printing style of
>>>>>>> Rebuild
	the German monasteries and printers of the 12th to 15th
	centuries. An example of this font style is the Old English
	family. This IBM Subclass reflects the ISO Blackletters Class
	as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	standard.</p><h5><a name="idm5725"></a>Subclass ID = 3 : Decorative</h5><p>This style is characterized by ornamental designs
=======
	standard.</p><h5><a name="idm189299433376"></a>Subclass ID = 3 : Decorative</h5><p>This style is characterized by ornamental designs
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm62732012912"></a>Subclass ID = 3 : Decorative</h5><p>This style is characterized by ornamental designs
>>>>>>> Rebuild
=======
	standard.</p><h5><a name="idm465835892208"></a>Subclass ID = 3 : Decorative</h5><p>This style is characterized by ornamental designs
>>>>>>> Rebuild
	(typically from nature, such as leaves, flowers, animals,
	etc.) incorporated into the stems and strokes of the
	characters. An example of this font style is the Saphire
	family. This IBM Subclass reflects the ISO Ornamental Class
	and Decorative Subclass as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	9541-5 draft standard.</p><h5><a name="idm5727"></a>Subclass ID = 4 : Three Dimensional</h5><p>This style is characterized by a three dimensional
=======
	9541-5 draft standard.</p><h5><a name="idm189299432240"></a>Subclass ID = 4 : Three Dimensional</h5><p>This style is characterized by a three dimensional
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm62732011776"></a>Subclass ID = 4 : Three Dimensional</h5><p>This style is characterized by a three dimensional
>>>>>>> Rebuild
=======
	9541-5 draft standard.</p><h5><a name="idm465835891040"></a>Subclass ID = 4 : Three Dimensional</h5><p>This style is characterized by a three dimensional
>>>>>>> Rebuild
	(raised) appearance of the characters created by shading or
	geometric effects. An example of this font style is the Thorne
	Shaded family. This IBM Subclass reflects the ISO Ornamental
	Class and Three Dimensional Subclass as documented in the
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5729"></a>Subclass ID = 5-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5731"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5733"></a>Class ID = 10 Scripts</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.12.1"></a>Specification</h4></div></div></div><p>This style includes those typefaces that are
	    designed to simulate handwriting. This IBM Class reflects
	    the ISO Script Class and Uncial Class as documented in the
	    12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5738"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the
	    associated font has no design sub-classification or that
	    the design sub-classification is not of significance to
	    the creator or user of the font resource.</p><h5><a name="idm5740"></a>Subclass ID = 1 : Uncial</h5><p>This style is characterized by unjoined
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299431136"></a>Subclass ID = 5-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299430256"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732010672"></a>Subclass ID = 5-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62732009792"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
=======
	12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835889888"></a>Subclass ID = 5-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835888960"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
>>>>>>> Rebuild
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835887456"></a>Class ID = 10 Scripts</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.12.1"></a>Specification</h4></div></div></div><p>This style includes those typefaces that are
	    designed to simulate handwriting. This IBM Class reflects
	    the ISO Script Class and Uncial Class as documented in the
	    12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835868768"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the
	    associated font has no design sub-classification or that
	    the design sub-classification is not of significance to
<<<<<<< HEAD
<<<<<<< HEAD
	    the creator or user of the font resource.</p><h5><a name="idm189299425600"></a>Subclass ID = 1 : Uncial</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    the creator or user of the font resource.</p><h5><a name="idm62732005216"></a>Subclass ID = 1 : Uncial</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    the creator or user of the font resource.</p><h5><a name="idm465835867728"></a>Subclass ID = 1 : Uncial</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
	    (nonconnecting) characters that are generally based on the
	    hand writing style of Europe in the 6th to 9th
	    centuries. An example of this font style is the Libra
	    family. This IBM Subclass reflects the ISO Uncial Class as
	    documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    standard.</p><h5><a name="idm5742"></a>Subclass ID = 2 : Brush Joined</h5><p>This style is characterized by joined (connecting)
=======
	    standard.</p><h5><a name="idm189299424480"></a>Subclass ID = 2 : Brush Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm62732004096"></a>Subclass ID = 2 : Brush Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm465835866576"></a>Subclass ID = 2 : Brush Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
	    characters that have the appearance of being painted with
	    a brush, with moderate contrast between thick and thin
	    strokes. An example of this font style is the Mistral
	    family. This IBM Subclass reflects the ISO Script Class,
	    Joined Subclass, and Informal Specific Group as documented
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5744"></a>Subclass ID = 3 : Formal Joined</h5><p>This style is characterized by joined (connecting)
=======
	    in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299423296"></a>Subclass ID = 3 : Formal Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62732002912"></a>Subclass ID = 3 : Formal Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835865360"></a>Subclass ID = 3 : Formal Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
	    characters that have a printed (or drawn with a stiff
	    brush) appearance with extreme contrast between the thick
	    and thin strokes. An example of this font style is the
	    Coronet family. This IBM Subclass reflects the ISO Script
	    Class, Joined Subclass, and Formal Specific Group as
	    documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    standard.</p><h5><a name="idm5746"></a>Subclass ID = 4 : Monotone Joined</h5><p>This style is characterized by joined (connecting)
=======
	    standard.</p><h5><a name="idm189299422096"></a>Subclass ID = 4 : Monotone Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm62732001712"></a>Subclass ID = 4 : Monotone Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm465835864128"></a>Subclass ID = 4 : Monotone Joined</h5><p>This style is characterized by joined (connecting)
>>>>>>> Rebuild
	    characters that have a uniform appearance with little or
	    no contrast in the strokes. An example of this font style
	    is the Kaufmann family. This IBM Subclass reflects the ISO
	    Script Class, Joined Subclass, and Monotone Specific Group
	    as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    standard.</p><h5><a name="idm5748"></a>Subclass ID = 5 : Calligraphic</h5><p>This style is characterized by beautifully hand
=======
	    standard.</p><h5><a name="idm189299420944"></a>Subclass ID = 5 : Calligraphic</h5><p>This style is characterized by beautifully hand
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm62732000560"></a>Subclass ID = 5 : Calligraphic</h5><p>This style is characterized by beautifully hand
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm465835862928"></a>Subclass ID = 5 : Calligraphic</h5><p>This style is characterized by beautifully hand
>>>>>>> Rebuild
	    drawn, unjoined (non-connecting) characters that have an
	    appearance of being drawn with a broad edge pen. An
	    example of this font style is the Thompson Quillscript
	    family. This IBM Subclass reflects the ISO Script Class,
	    Unjoined Subclass, and Calligraphic Specific Group as
	    documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    standard.</p><h5><a name="idm5750"></a>Subclass ID = 6 : Brush Unjoined</h5><p>This style is characterized by unjoined
=======
	    standard.</p><h5><a name="idm189299419760"></a>Subclass ID = 6 : Brush Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm62731999376"></a>Subclass ID = 6 : Brush Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm465835861712"></a>Subclass ID = 6 : Brush Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
	    (non-connecting) characters that have the appearance of
	    being painted with a brush, with moderate contrast between
	    thick and thin strokes. An example of this font style is
	    the Saltino family. This IBM Subclass reflects the ISO
	    Script Class, Unjoined Subclass, and Brush Specific Group
	    as documented in the 12/87 ISO/IEC 9541-5 draft
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    standard.</p><h5><a name="idm5752"></a>Subclass ID = 7 : Formal Unjoined</h5><p>This style is characterized by unjoined
=======
	    standard.</p><h5><a name="idm189299418560"></a>Subclass ID = 7 : Formal Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm62731998176"></a>Subclass ID = 7 : Formal Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    standard.</p><h5><a name="idm465835860464"></a>Subclass ID = 7 : Formal Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
	    (non-connecting) characters that have a printed (or drawn
	    with a stiff brush) appearance with extreme contrast
	    between the thick and thin strokes. An example of this
	    font style is the Virtuosa family. This IBM Subclass
	    reflects the ISO Script Class, Unjoined Subclass, and
	    Formal Specific Group as documented in the 12/87 ISO/IEC
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    9541-5 draft standard.</p><h5><a name="idm5754"></a>Subclass ID = 8 : Monotone Unjoined</h5><p>This style is characterized by unjoined
=======
	    9541-5 draft standard.</p><h5><a name="idm189299417360"></a>Subclass ID = 8 : Monotone Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    9541-5 draft standard.</p><h5><a name="idm62731996976"></a>Subclass ID = 8 : Monotone Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
=======
	    9541-5 draft standard.</p><h5><a name="idm465835859216"></a>Subclass ID = 8 : Monotone Unjoined</h5><p>This style is characterized by unjoined
>>>>>>> Rebuild
	    (non-connecting) characters that have a uniform appearance
	    with little or no contrast in the strokes. An example of
	    this font style is the Gilles Gothic family. This IBM
	    Subclass reflects the ISO Script Class, Unjoined Subclass,
	    and Monotone Specific Group as documented in the 12/87
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	    ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5756"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future
	    assignment, and shall not be used without formal
	    assignment by IBM.</p><h5><a name="idm5758"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	  the associated design class that are not covered by another
	  Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5760"></a>Class ID = 11 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.13.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5765"></a>Class ID = 12 Symbolic</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.14.1"></a>Specification</h4></div></div></div><p>This style is generally design independent, making it
=======
	    ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299416192"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future
=======
	    ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62731995808"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future
>>>>>>> Rebuild
=======
	    ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835858000"></a>Subclass ID = 9-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future
>>>>>>> Rebuild
	    assignment, and shall not be used without formal
	    assignment by IBM.</p><h5><a name="idm465835857056"></a>Subclass ID = 15 : Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	  the associated design class that are not covered by another
<<<<<<< HEAD
<<<<<<< HEAD
	  Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299413920"></a>Class ID = 11 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.13.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299411264"></a>Class ID = 12 Symbolic</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.14.1"></a>Specification</h4></div></div></div><p>This style is generally design independent, making it
>>>>>>> Rebuild
=======
	  Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62731993616"></a>Class ID = 11 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.13.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62731991040"></a>Class ID = 12 Symbolic</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.14.1"></a>Specification</h4></div></div></div><p>This style is generally design independent, making it
>>>>>>> Rebuild
=======
	  Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835855536"></a>Class ID = 11 (reserved for future use)</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.13.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835852640"></a>Class ID = 12 Symbolic</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.14.1"></a>Specification</h4></div></div></div><p>This style is generally design independent, making it
>>>>>>> Rebuild
	suitable for Pi and special characters (icons, dingbats,
	technical symbols, etc.) that may be used equally well with
	any font. This IBM Class reflects various ISO Specific Groups,
	as noted below and documented in the 12/87 ISO/IEC 9541-5
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	draft standard.</p><h5><a name="idm5770"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm5772"></a>Subclass ID = 1-2 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5774"></a>Subclass ID = 3 : Mixed Serif</h5><p>This style is characterized by either both or a
=======
	draft standard.</p><h5><a name="idm189299408864"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm189299407888"></a>Subclass ID = 1-2 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299407008"></a>Subclass ID = 3 : Mixed Serif</h5><p>This style is characterized by either both or a
>>>>>>> Rebuild
=======
	draft standard.</p><h5><a name="idm62731988640"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm62731987664"></a>Subclass ID = 1-2 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62731986784"></a>Subclass ID = 3 : Mixed Serif</h5><p>This style is characterized by either both or a
>>>>>>> Rebuild
=======
	draft standard.</p><h5><a name="idm465835850112"></a>Subclass ID = 0 : No Classification</h5><p>This subclass ID is used to indicate that the associated
	font has no design sub-classification or that the design
	sub-classification is not of significance to the creator or
	user of the font resource.</p><h5><a name="idm465835849088"></a>Subclass ID = 1-2 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835848160"></a>Subclass ID = 3 : Mixed Serif</h5><p>This style is characterized by either both or a
>>>>>>> Rebuild
	combination of serif and sans serif designs on those
	characters of the font for which design is important (e.g.,
	superscript and subscript characters, numbers, copyright or
	trademark symbols, etc.). An example of this font style is
	found in the IBM Symbol family. This IBM Subclass is not
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm5776"></a>Subclass ID = 4-5 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5778"></a>Subclass ID = 6 : Oldstyle Serif</h5><p>This style is characterized by a Oldstyle Serif IBM
=======
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm189299405840"></a>Subclass ID = 4-5 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299404960"></a>Subclass ID = 6 : Oldstyle Serif</h5><p>This style is characterized by a Oldstyle Serif IBM
>>>>>>> Rebuild
=======
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm62731985616"></a>Subclass ID = 4-5 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62731984736"></a>Subclass ID = 6 : Oldstyle Serif</h5><p>This style is characterized by a Oldstyle Serif IBM
>>>>>>> Rebuild
=======
	reflected in the 12/87 ISO/IEC 9541-5 draft standard.</p><h5><a name="idm465835846960"></a>Subclass ID = 4-5 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835846032"></a>Subclass ID = 6 : Oldstyle Serif</h5><p>This style is characterized by a Oldstyle Serif IBM
>>>>>>> Rebuild
	Class design on those characters of the font for which design
	is important (e.g., superscript and subscript characters,
	numbers, copyright or trademark symbols, etc.). An example of
	this font style is found in the IBM Sonoran Pi Serif
	family. This IBM Subclass is not directly reflected in the
	12/87 ISO/IEC 9541-5 draft standard, though it is indirectly
	by the ISO Serif Class and Legibility Subclass (implies that
	all characters of the font exhibit the design appearance,
	while only a subset of the characters actually exhibit the
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	design).</p><h5><a name="idm5780"></a>Subclass ID = 7 : Neo-grotesque Sans Serif</h5><p>This style is characterized by a Neo-grotesque Sans
=======
	design).</p><h5><a name="idm189299403584"></a>Subclass ID = 7 : Neo-grotesque Sans Serif</h5><p>This style is characterized by a Neo-grotesque Sans
>>>>>>> Rebuild
=======
	design).</p><h5><a name="idm62731983360"></a>Subclass ID = 7 : Neo-grotesque Sans Serif</h5><p>This style is characterized by a Neo-grotesque Sans
>>>>>>> Rebuild
=======
	design).</p><h5><a name="idm465835844608"></a>Subclass ID = 7 : Neo-grotesque Sans Serif</h5><p>This style is characterized by a Neo-grotesque Sans
>>>>>>> Rebuild
	Serif IBM Font Class and Subclass design on those characters
	of the font for which design is important (e.g., superscript
	and subscript characters, numbers, copyright or trademark
	symbols, etc.). An example of this font style is found in the
	IBM Sonoran Pi Sans Serif family. This IBM Subclass is not
	directly reflected in the 12/87 ISO/IEC 9541-5 draft standard,
	though it is indirectly by the ISO Sans Serif Class and Gothic
	Subclass (implies that all characters of the font exhibit the
	design appearance, while only a subset of the characters
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
	actually exhibit the design).</p><h5><a name="idm5782"></a>Subclass ID = 8-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm5784"></a>Subclass ID = 15 :Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5786"></a>Class ID = 13 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.15.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm5791"></a>Class ID = 14 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.16.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
=======
	actually exhibit the design).</p><h5><a name="idm189299402176"></a>Subclass ID = 8-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm189299401296"></a>Subclass ID = 15 :Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299399936"></a>Class ID = 13 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.15.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm189299397280"></a>Class ID = 14 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.16.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
>>>>>>> Rebuild
=======
	actually exhibit the design).</p><h5><a name="idm62731981952"></a>Subclass ID = 8-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm62731981072"></a>Subclass ID = 15 :Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62731979792"></a>Class ID = 13 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.15.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm62731977216"></a>Class ID = 14 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.16.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
>>>>>>> Rebuild
=======
	actually exhibit the design).</p><h5><a name="idm465835843152"></a>Subclass ID = 8-14 : (reserved for future use)</h5><p>These subclass IDs are reserved for future assignment,
	and shall not be used without formal assignment by IBM.</p><h5><a name="idm465835842224"></a>Subclass ID = 15 :Miscellaneous</h5><p>This subclass ID is used for miscellaneous designs of
	the associated design class that are not covered by another
	Subclass.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835840736"></a>Class ID = 13 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.15.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
	shall not be used without formal assignment by IBM.</p></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm465835837856"></a>Class ID = 14 Reserved</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.13.16.1"></a>Specification</h4></div></div></div><p>This class ID is reserved for future assignment, and
>>>>>>> Rebuild
	shall not be used without formal assignment by IBM.</p></div></div></div>