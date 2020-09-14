<pre class='idl'>
interface ItemVariationStore {
	attribute USHORT format;
	attribute Offset32 varRegionList /* VarRegionList */;
	attribute USHORT varDataCount;
	attribute Offset32[] varData /* VarData */;
};
interface VarRegionList {
	attribute USHORT regionAxisCount;
	attribute USHORT regionCount;
	attribute VarRegion[] regions;
};
interface VarRegion {
	attribute VarRegionAxis[] varRegionAxes;
};
interface VarRegionAxis {
	attribute F2Dot14 startCoord;
	attribute F2Dot14 peakCoord;
	attribute F2Dot14 endCoord;
};
interface VarData {
	attribute USHORT itemCount;
	attribute USHORT numShorts;
	attribute USHORT varRegionCount;
	attribute USHORT[] varRegionIndices;
	attribute VarDataValue[] items;
};
interface VarDataValue {
};
</pre>
