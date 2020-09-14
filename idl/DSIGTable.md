<pre class='idl'>
interface DSIGTable {
	attribute ULONG tableVersion;
	attribute USHORT numSignatures;
	attribute USHORT flags;
	attribute SignatureRecord[] signatureRecords;
};
interface SignatureRecord {
	attribute ULONG format;
	attribute ULONG length;
	attribute Offset32 offset /* SignatureBlock */;
};
interface SignatureBlock {
	attribute USHORT reserved1;
	attribute USHORT reserved2;
	attribute ULONG signatureLength;
	attribute byte[] signature;
};
</pre>
