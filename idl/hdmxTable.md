<pre class='idl'>
interface hdmxTable {
	attribute USHORT tableVersion /* ==0 */;
	attribute USHORT numRecords;
	attribute ULONG sizeDeviceRecord;
	attribute DeviceRecord[] records;
};
interface DeviceRecord {
	attribute uint8 pixelSize;
	attribute uint8 maxWidth;
	attribute uint8[] widths;
};
</pre>
