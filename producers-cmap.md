
If a platform ID 4 (custom), encoding ID 0-255 (OTF Windows NT
compatibility mapping) cmap encoding is present in an CommonType font
with CFF outlines, then the OTF font driver in Windows NT will: (a)
superimpose the glyphs encoded at character codes 0-255 in the encoding
on the corresponding Windows ANSI (code page 1252) Unicode values in the
Unicode encoding it reports to the system; (b) add Windows ANSI (CharSet
0) to the list of CharSets supported by the font; and (c) consider the
value of the encoding ID to be a Windows CharSet value and add it to the
list of CharSets supported by the font.

This cmap encoding provides a compatibility mechanism for non-Unicode
applications that use the font as if it were Windows ANSI encoded.
