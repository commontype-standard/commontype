<pre class='idl'>
typedef (postTableVersion10 or postTableVersion20 or postTableVersion25 or postTableVersion30) postTable;
interface postTableVersion10 {
	attribute VERSION version /* ==1.0 */;
	attribute postTableCommon postTableCommon;
};
interface postTableCommon {
	attribute FIXED italicAngle;
	attribute SHORT underlinePosition;
	attribute SHORT underlineThickness;
	attribute ULONG isFixedPitch;
	attribute ULONG minMemType42;
	attribute ULONG maxMemType42;
	attribute ULONG minMemType1;
	attribute ULONG maxMemType1;
};
interface postTableVersion20 {
	attribute VERSION version /* ==2.0 */;
	attribute postTableCommon postTableCommon;
	attribute USHORT numGlyphs;
	attribute USHORT[] glyphNameIndex;
	attribute PascalString[] names;
};
interface PascalString {
	attribute uint8 length;
	attribute byte[] string;
};
interface postTableVersion25 {
	attribute VERSION version /* ==2.5 */;
	attribute postTableCommon postTableCommon;
	attribute USHORT numGlyphs;
	attribute byte[] offset;
};
interface postTableVersion30 {
	attribute VERSION version /* ==3.0 */;
	attribute postTableCommon postTableCommon;
};
</pre>
