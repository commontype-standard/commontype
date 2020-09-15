<pre class='idl'>
interface STATTable {
	attribute Version version;
	attribute USHORT designAxisRecordSize;
	attribute USHORT designAxisCount;
	attribute Offset32 designAxisRecord /* AxisRecordArray */;
	attribute USHORT axisValueCount;
	attribute Offset32 axisValueArray /* AxisValueArray */;
	attribute NameID elidedFallbackNameID /* if version >= 0x00010001 */;
};
interface AxisRecordArray {
	attribute AxisRecord[] axes;
};
interface AxisRecord {
	attribute Tag axisTag;
	attribute NameID axisNameID;
	attribute USHORT axisOrdering;
};
interface AxisValueArray {
	attribute Offset16[] axisValues /* AxisValue */;
};
typedef (AxisValueFormat1 or AxisValueFormat2 or AxisValueFormat3 or AxisValueFormat4) AxisValue;
interface AxisValueFormat1 {
	attribute USHORT format /* ==1 */;
	attribute USHORT axisIndex;
	attribute USHORT flags;
	attribute NameID valueNameID;
	attribute Fixed value;
};
interface AxisValueFormat2 {
	attribute USHORT format /* ==2 */;
	attribute USHORT axisIndex;
	attribute USHORT flags;
	attribute NameID valueNameID;
	attribute Fixed nominalValue;
	attribute Fixed rangeMinValue;
	attribute Fixed rangeMaxValue;
};
interface AxisValueFormat3 {
	attribute USHORT format /* ==3 */;
	attribute USHORT axisIndex;
	attribute USHORT flags;
	attribute NameID valueNameID;
	attribute Fixed value;
	attribute Fixed linkedValue;
};
interface AxisValueFormat4 {
	attribute USHORT format /* ==4 */;
	attribute USHORT axisCount;
	attribute USHORT flags;
	attribute NameID valueNameID;
	attribute AxisValueRecord[] axisValueRecords;
};
interface AxisValueRecord {
	attribute USHORT axisIndex;
	attribute Fixed value;
};
</pre>
