<h3 id="consumer-color"><dfn>Processing Color Fonts</dfn></h3>

<h4 id="consumer-colr">Processing a COLR/CPAL table</h4>

When rendering glyphs in a font containing a [=COLR table=] and [=CPAL table=], the font consumer should perform the following procedure:

* If the user has selected a color palette, set `paletteID` to this value. Otherwise set `paletteID` to zero. Set `paletteBase` to `paletteID` multiplied by the {{numPaletteEntries}} value from the `CPAL` table.

* Determine, by binary search of the {{BaseGlyphRecord}} array in the `COLR` table, whether there is a {{BaseGlyphRecord}} with {{BaseGlyphRecord/gid}} equal to the glyph ID being rendered. If no such {{BaseGlyphRecord}} exists, the glyph is rendered as normal.

* Extract the slice from the {{LayerRecord}} array with indices {{firstLayerIndex}} to {{firstLayerIndex}}+{{numLayers}} inclusive.

* For each {{LayerRecord}} entry, in order:
    * Retrieve the glyph indexed by {{gid}}.
    * If the {{paletteIndex}} is `0xFFFF`, render the glyph in the current foreground text color.
    * If not, use {{paletteIndex}} + `paletteBase` to index the {{colorRecordIndices}} array in the `CPAL` table, and use the resulting value to index the {{ColorRecord}} array. Render the glyph in the color returned.
