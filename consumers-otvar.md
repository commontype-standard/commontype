<h3 id="processing-variable-fonts" rel="off-new-10.4">Processing Variable Fonts</h3>

When processing variable fonts, font consumers must take note of the following requirements:

* XXX rounding

<h4 id="axis-coordinate-normalization">Axis Coordinate Normalization</h4>

To normalise an axis value from a [=user coordinate=] to a [=normalized coordinate=], the following algorithm should be used:

* The user coordinate value should be converted if necessary to a fixed-point 16.16 value. All arithmetic manipulation must be done using fixed-point 16.16 values.
* The [=fvar table=] {{VariationAxisRecord}} for the appropriate axis should be located.
* If the user value is less than the {{defaultValue}}, then the normalized value should be set to `-(axisDefault - userValue) / (axisDefault - axisMin)`; if it is more than the {{defaultValue}}, then the normalized value should be set to `(userValue - axisDefault) / (axisMax - axisDefault)`; else, it is set to zero.
* The normalized value should be clamped to a minimum of -1 and a maximum of 1.
* If an [=avar table=] is present, then further transformation is performed:
	- Find the {{SegmentMaps}} for the appropriate axis.
	- If an {{AxisValueMap}} entry has a {{fromCoordinate}} equal to the current normalized value `v`, then return its {{toCoordinate}}.
	- Otherwise, find the segment `a` with the largest {{fromCoordinate}} strictly lower than `v` and the segment `b` with the smaller {{fromCoordinate}} strictly higher than `v`.
	- The normalized value value is then set to `a.toCoordinate + (b.toCoordinate - a.toCoordinate) * (v - a.fromCoordinate) / (b.fromCoordinate - a.fromCoordinate)`.
* Finally the 16.16 value should be converted to an `F2DOT16` by adding 0x00000002, and shifting the value to the right by 2 with sign extension.
