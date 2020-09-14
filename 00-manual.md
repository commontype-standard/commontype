Ignore this file. Its purpose is to make make-idl.py produce some files
which we are not planning to use (because we will be writing them
manually in the spec, because they require more discussion or breaking
down into separate units than most tables), the side-effect of which is
that definitions for any subtables they contain will not be output
*again* when referenced from other places. e.g. we are manually writing
out the EBLC IDL, which contains a reference to (and definition for)
SbitLineMetrics. But we are automatically generating the EBSC IDL, which
*also* contains a reference to SbitLineMetrics. By generating a dummy
auto-EBLC IDL here, we output SbitLineMetrics and so when make-idl comes
to EBSC, it doesn't output that definition again.

<pre class=include>path: idl/EBLCTable.md</pre>

