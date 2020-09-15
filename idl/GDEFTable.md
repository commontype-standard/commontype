<pre class='idl'>
interface GDEFTable {
	attribute VERSION version;
	attribute Offset16 glyphClassDef /* ClassDef */;
	attribute Offset16 attachList /* AttachList */;
	attribute Offset16 ligCaretList /* LigCaretList */;
	attribute Offset16 markAttachClassDef /* ClassDef */;
	attribute Offset16 markGlyphSetsDef /* if version >= 0x00010002 */ /* MarkGlyphSetsDef */;
	attribute Offset32 varStore /* if version >= 0x00010003 */ /* ItemVariationStore */;
};
typedef (ClassDefFormat1 or ClassDefFormat2) ClassDef;
interface ClassDefFormat1 {
	attribute USHORT classFormat /* ==1 */;
	attribute GlyphID startGlyph;
	attribute USHORT glyphCount;
	attribute USHORT[] classValueArrays;
};
interface ClassDefFormat2 {
	attribute USHORT classFormat /* ==2 */;
	attribute USHORT classRangeCount;
	attribute ClassRangeRecord[] classRangeRecords;
};
interface ClassRangeRecord {
	attribute GlyphID start;
	attribute GlyphID end;
	attribute USHORT class;
};
interface AttachList {
	attribute Offset16 coverage /* Coverage */;
	attribute USHORT glyphCount;
	attribute Offset16[] attachPoints /* AttachPoint */;
};
typedef (CoverageFormat1 or CoverageFormat2) Coverage;
interface CoverageFormat1 {
	attribute USHORT coverageFormat /* ==1 */;
	attribute USHORT glyphCount;
	attribute GlyphID[] glyphArrays;
};
interface CoverageFormat2 {
	attribute USHORT coverageFormat /* ==2 */;
	attribute USHORT rangeCount;
	attribute RangeRecord[] rangeRecords;
};
interface RangeRecord {
	attribute GlyphID start;
	attribute GlyphID end;
	attribute USHORT startCoverageIndex;
};
interface AttachPoint {
	attribute USHORT pointCount;
	attribute USHORT[] pointIndexs;
};
interface LigCaretList {
	attribute Offset16 coverage /* Coverage */;
	attribute USHORT ligGlyphCount;
	attribute Offset16[] ligGlyphs /* LigGlyph */;
};
interface LigGlyph {
	attribute USHORT caretCount;
	attribute Offset16[] caretValues /* CaretValue */;
};
typedef (CaretValueFormat1 or CaretValueFormat2 or CaretValueFormat3) CaretValue;
interface CaretValueFormat1 {
	attribute USHORT caretValueFormat /* ==1 */;
	attribute int16 coordinate;
};
interface CaretValueFormat2 {
	attribute USHORT caretValueFormat /* ==2 */;
	attribute USHORT caretValuePoint;
};
interface CaretValueFormat3 {
	attribute USHORT caretValueFormat /* ==3 */;
	attribute int16 coordinate;
	attribute Offset16 deviceTable /* Device */;
};
interface Device {
	attribute USHORT startSize;
	attribute USHORT endSize;
	attribute USHORT deltaFormat;
	attribute DeltaValue deltaValue /* if deltaFormat in (1,2,3) */;
};
interface MarkGlyphSetsDef {
	attribute USHORT markSetTableFormat;
	attribute USHORT markSetCount;
	attribute Offset32[] coverages /* Coverage */;
};
</pre>
