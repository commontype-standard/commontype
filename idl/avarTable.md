<pre class='idl'>
interface avarTable {
	attribute USHORT tableMajorVersion;
	attribute USHORT tableMinorVersion;
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
