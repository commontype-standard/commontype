<pre class='idl'>
interface gaspTable {
	attribute USHORT version /* ==1 */;
	attribute USHORT numRanges;
	attribute GaspRange[] gaspRanges;
};
interface GaspRange {
	attribute USHORT rangeMaxPPEM;
	attribute USHORT rangeGaspBehavior;
};
</pre>
