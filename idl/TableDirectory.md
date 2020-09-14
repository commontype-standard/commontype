<pre class='idl'>
interface TableDirectory {
	attribute LONG sfntVersion;
	attribute USHORT numTables;
	attribute USHORT searchRange;
	attribute USHORT entrySelector;
	attribute USHORT rangeShift;
	attribute TableDirectoryEntry[] entries;
};
interface TableDirectoryEntry {
	attribute Tag tableTag;
	attribute ULONG checksum;
	attribute Offset32 offset;
	attribute ULONG length;
};
</pre>
