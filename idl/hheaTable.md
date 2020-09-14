<pre class='idl'>
interface hheaTable {
	attribute VERSION tableVersion /* ==1.0 */;
	attribute SHORT ascender;
	attribute SHORT descender;
	attribute SHORT linegap;
	attribute USHORT advanceWidthMax;
	attribute SHORT minLeftSideBearing;
	attribute SHORT minRightSideBearing;
	attribute SHORT xMaxExtent;
	attribute SHORT caretSlopeRise;
	attribute SHORT caretSlopeRun;
	attribute SHORT caretOffset;
	attribute SHORT reserved1;
	attribute SHORT reserved2;
	attribute SHORT reserved3;
	attribute SHORT reserved4;
	attribute SHORT metricDataFormat /* ==0 */;
	attribute USHORT numberofHMetrics;
};
</pre>
