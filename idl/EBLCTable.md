<pre class='idl'>
interface EBLCTable {
	attribute VERSION tableVersion /* ==2.0 */;
	attribute ULONG numSizes;
	attribute BitmapSize[] strikes;
};
interface BitmapSize {
	attribute Offset32 indexSubTableArrayOffset /* IndexSubTableArrayElement[] */;
	attribute ULONG indexTablesSize;
	attribute ULONG numberOfIndexSubTables;
	attribute ULONG unused;
	attribute SbitLineMetrics hori;
	attribute SbitLineMetrics vert;
	attribute USHORT startGlyphIndex;
	attribute USHORT endGlyphIndex;
	attribute uint8 ppemX;
	attribute uint8 ppemY;
	attribute uint8 bitDepth;
	attribute int8 flags;
};
interface IndexSubTableArrayElement {
	attribute USHORT firstGlyphIndex;
	attribute USHORT lastGlyphIndex;
	attribute Offset32 additionalOffsetToIndexSubtable /* IndexSubTable */;
};
typedef (IndexSubtable1 or IndexSubtable2 or IndexSubtable3 or IndexSubtable4 or IndexSubtable5) IndexSubTable;
interface IndexSubtable1 {
	attribute IndexSubtableHeader indexSubtableHeader;
	attribute Offset32[] offsetArray;
};
interface IndexSubtable2 {
	attribute IndexSubtableHeader indexSubtableHeader;
	attribute ULONG imageSize;
	attribute BigGlyphMetrics bigMetrics;
};
interface IndexSubtable3 {
	attribute IndexSubtableHeader indexSubtableHeader;
	attribute Offset32[] offsetArray;
};
interface IndexSubtable4 {
	attribute IndexSubtableHeader indexSubtableHeader;
	attribute ULONG numGlyphs;
	attribute GlyphIdOffsetPair[] glyphArray;
};
interface GlyphIdOffsetPair {
	attribute USHORT glyphID;
	attribute Offset16 offset;
};
interface IndexSubtable5 {
	attribute IndexSubtableHeader indexSubtableHeader;
	attribute ULONG imageSize;
	attribute BigGlyphMetrics bigMetrics;
	attribute ULONG numGlyphs;
	attribute USHORT[] glyphArray;
};
interface SbitLineMetrics {
	attribute int8 ascender;
	attribute int8 descender;
	attribute uint8 widthMax;
	attribute int8 caretSlopeNumerator;
	attribute int8 caretSlopeDenominator;
	attribute int8 caretOffset;
	attribute int8 minOriginSB;
	attribute int8 minAdvanceSB;
	attribute int8 maxBeforeBL;
	attribute int8 minAfterBL;
	attribute int8 pad1;
	attribute int8 pad2;
};
</pre>
