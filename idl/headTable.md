<pre class='idl'>
interface headTable {
	attribute VERSION tableVersion /* ==1.0 */;
	attribute VERSION fontRevision;
	attribute ULONG checkSumAdjustment;
	attribute ULONG magicNumber /* ==1594834165 */;
	attribute USHORT flags;
	attribute USHORT unitsPerEm;
	attribute LONGDATETIME created;
	attribute LONGDATETIME modified;
	attribute SHORT xMin;
	attribute SHORT yMin;
	attribute SHORT xMax;
	attribute SHORT yMax;
	attribute USHORT macStyle;
	attribute USHORT lowestRecPPEM;
	attribute SHORT fontDirectionHint;
	attribute SHORT indexToLocFormat;
	attribute SHORT unused;
};
</pre>
