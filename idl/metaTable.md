<pre class='idl'>
interface metaTable {
	attribute ULONG version /* ==1 */;
	attribute ULONG flags /* ==0 */;
	attribute ULONG reserved /* ==0 */;
	attribute ULONG dataMapsCount;
	attribute DataMap[] dataMaps;
};
interface DataMap {
	attribute Tag tag;
	attribute Offset32 dataOffset;
	attribute ULONG dataLength;
};
</pre>
