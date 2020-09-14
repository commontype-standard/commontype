<pre class='idl'>
interface avarTable {
	attribute USHORT tableMajorVersion /* ==1 */;
	attribute USHORT tableMinorVersion /* ==0 */;
	attribute USHORT reserved;
	attribute USHORT axisCount;
	attribute SegmentMaps[] axisSegmentMaps;
};
interface SegmentMaps {
	attribute USHORT positionMapCount;
	attribute AxisValueMap[] axisValueMaps;
};
interface AxisValueMap {
	attribute F2DOT14 fromCoordinate;
	attribute F2DOT14 toCoordinate;
};
</pre>
