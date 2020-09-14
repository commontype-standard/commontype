<pre class='idl'>
typedef (maxpTableCFF or maxpTableTT) maxpTable;
interface maxpTableCFF {
	attribute VERSION version /* ==0.5 */;
	attribute USHORT numGlyphs;
};
interface maxpTableTT {
	attribute VERSION version /* ==1.0 */;
	attribute USHORT numGlyphs;
	attribute USHORT maxPoints;
	attribute USHORT maxContours;
	attribute USHORT maxCompositePoints;
	attribute USHORT maxCompositeContours;
	attribute USHORT maxZones /* ==2 */;
	attribute USHORT maxTwilightPoints;
	attribute USHORT maxStorage;
	attribute USHORT maxFunctionDefs;
	attribute USHORT maxInstructionDefs;
	attribute USHORT maxStackElements;
	attribute USHORT maxSizeOfInstructions;
	attribute USHORT maxComponentElements;
	attribute USHORT maxComponentDepth;
};
</pre>
