<pre class='idl'>
interface EBSCTable {
	attribute VERSION tableVersion /* ==2.0 */;
	attribute ULONG numSizes;
	attribute BitmapScale[] bitmapScales;
};
interface BitmapScale {
	attribute SbitLineMetrics hori;
	attribute SbitLineMetrics vert;
	attribute uint8 ppemX;
	attribute uint8 ppemY;
	attribute uint8 substitutePpemX;
	attribute uint8 substitutePpemY;
};
</pre>
