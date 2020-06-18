<div xmlns="http://www.w3.org/1999/xhtml" class="chapter"><div class="titlepage"><div><div><h2 class="title"><a name="chapter.DSIG"></a>Chapter 29. DSIG - Digital Signature Table</h2></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm79886109280"></a>Overview</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.30.1.1"></a>Specification</h4></div></div></div><p>The DSIG table contains the digital signature of the
          CommonType font. Signature formats are widely documented and
          rely on a key pair architecture. Software developers, or
          publishers posting material on the Internet, create
          signatures using a private key. Operating systems or
          applications authenticate the signature using a public
          key.</p><p>The W3C and major software and operating system
          developers have specified security standards that describe
          signature formats, specify secure collections of web
          objects, and recommend authentication architecture. CommonType
          fonts with signatures will support these standards.</p><p>CommonType fonts offer many security features:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>Operating systems and browsing applications can
              identify the source and integrity of font files before
              using them,</p></li><li class="listitem"><p>Font developers can specify embedding restrictions
              in CommonType fonts, and these restrictions cannot be
              altered in a font signed by the developer. </p></li></ul></div><p>The enforcement of signatures is an administrative
          policy, enabled by the operating system. Windows will soon
          require installed software components, including fonts, to
          be signed. Internet browsers will also give users and
          administrators the ability to screen out unsigned objects
          obtained on-line, including web pages, fonts, graphics, and
          software components.</p><p>Anyone can obtain identity certificates and encryption
          keys from a certifying agency, such as Verisign or GTE's
          Cybertrust, free or at a very low cost.</p><p>The DSIG table is organized as follows. The first
          portion of the table is the header:</p><div class="table"><a name="idm79886101536"></a><p class="title"><strong>Table 29.1. DSIG Header</strong></p><div class="table-contents"><table class="table" summary="DSIG Header" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>ulVersion</td><td>Version number of the DSIG
              table (0x00000001)</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usNumSigs</td><td>Number of signatures in the
              table</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usFlag</td><td>
            <p>permission flags</p>
            <p>Bit 0: cannot be resigned</p>
            <p>Bit 1-7: Reserved (Set to 0)</p>
          </td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The version of the DSIG table is expressed as a ULONG,
	  beginning at 0. The version of the DSIG table currently used
	  is version 1 (0x00000001).</p><p>Permission bit 0 allows a party signing the font to
	  prevent any other parties from also signing the font
	  (counter-signatures). If this bit is set to zero (0) the
	  font may have a signature applied over the existing digital
	  signature(s). A party who wants to ensure that their
	  signature is the last signature can set this bit.</p><p>The DSIG header information is followed by entries for each
          of the signatures in the table specifying format and offset
          information:</p><div class="table"><a name="idm79886091712"></a><p class="title"><strong>Table 29.2. Format/Offset Table</strong></p><div class="table-contents"><table class="table" summary="Format/Offset Table" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>ULONG</td><td>ulFormat</td><td>format of the signature</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulLength</td><td>Length of signature in bytes</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>ulOffset</td><td>Offset to the signature block from the
              beginning of the table</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>This information is then followed by one or more
          signature blocks:</p><div class="table"><a name="idm79886084448"></a><p class="title"><strong>Table 29.3. Signature Block</strong></p><div class="table-contents"><table class="table" summary="Signature Block" border="1"><colgroup><col/><col/><col/><col/></colgroup><thead><tr><th>Type</th><th>Name</th><th>Description</th><td class="auto-generated"> </td></tr></thead><tbody><tr><td>USHORT</td><td>usReserved1</td><td>Reserved for later use; 0 for
              now</td><td class="auto-generated"> </td></tr><tr><td>USHORT</td><td>usReserved2</td><td>Reserved for later use; 0 for
              now</td><td class="auto-generated"> </td></tr><tr><td>ULONG</td><td>cbSignature</td><td>Length (in bytes) of the PKCS#7 packet in
              pbSignature</td><td class="auto-generated"> </td></tr><tr><td>BYTE[]</td><td>bSignature</td><td>PKCS#7 packet</td><td class="auto-generated"> </td></tr></tbody></table></div></div><br class="table-break"/><p>The format identifier specifies both the format of the
          signature object, as well as the hashing algorithm used to
          create and authenticate the signature. Currently only one
          format is defined, but at least one other format will soon
          be defined to handle subsetting scenarios. Format 1 supports
          PKCS#7 signatures with X.509 certificates and
          counter-signatures, as these signatures have been
          standardized for use by the W3C with the participation of
          numerous software developers.</p><p>For more information about PKCS#7 signatures, see <a class="ulink" href="ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-7.asc" target="_top">ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-7.asc</a>.</p><p>For more information about counter-signatures, see
          <a class="ulink" href="ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-9.asc" target="_top">ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-9.asc</a>.</p></div><div role="annotation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.30.1.2"></a>Annotation</h4></div></div></div><p>It is unclear what is measured by the field ulLength in
	a Format/Offset table: it is the length of the Signature Block
	table, or the length of the bSignature array in that table? In
	either case, this seems to be a redundant value, and its
	correlation to the cbSignature field should be noted. Looking
	at Adobe fonts, it seems that we interpreted it as the length
	of the signature block.</p><p>The Format/Offset Table is a misnommer. This is actually
	a <span class="emphasis"><em>record</em></span>, not a
	<span class="emphasis"><em>table</em></span>, since it is not
	pointed. Similarly, the DSIG header should be augmented by an
	array of those records.</p><p>The reference point of the ulOffset field in the
        Format/Offset is unclear. It is from the beginning of the DSIG
        table, or from the beginning of the Format/Offset record (thus
        being inconsistent with the layout tables)? Looking at Adobe
        fonts, it seems that we interpreted it as the relative to the
        beginning of the DSIG table.</p><p>The Signature Block is a misnommer. This is actually a
	<span class="emphasis"><em>table</em></span>, not a <span class="emphasis"><em>block</em></span>.</p></div><div role="zzzxml-representation" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.30.1.3"></a>XML Representation</h4></div></div></div><pre class="programlisting"><a name="d1e67207"></a><code class="classname"/> ==
      
  DSIG =
    element DSIG {
      attribute version { "1" },
      attribute flags { text },
      element signature {
        attribute format { text },
        text
      }*
    }
</pre></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm79886064448"></a>Format 1: For whole fonts, with either TrueType outlines
        and/or CFF data</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.30.2.1"></a>Specification</h4></div></div></div><p>PKCS#7 or PKCS#9. The signed content digest is created
          as follows:</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>If there is an existing DSIG table in the
              font,</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: circle; "><li class="listitem"><p>Remove DSIG table from font.</p><p>Remove DSIG table entry from sfnt Table
                  Directory.</p><p>Adjust table offsets as necessary.</p><p>Zero out the file checksum in the head
                  table.</p><p>Add the usFlag (reserved, set at 1 for now) to
                  the stream of bytes</p></li></ul></div></li><li class="listitem"><p>Hash the full stream of bytes using a secure one-way
              hash (such as MD5) to create the content digest.</p></li><li class="listitem"><p>Create the PKCS#7 signature block using the content
              digest.</p></li><li class="listitem"><p>Create a new DSIG table containing the signature
              block.</p></li><li class="listitem"><p>Add the DSIG table to the font, adjusting table
              offsets as necessary.</p></li><li class="listitem"><p>Add a DSIG table entry to the sfnt Table
              Directory.</p></li><li class="listitem"><p>Recalculate the checksum in the head table.</p></li></ul></div><p>Prior to signing a font file, ensure that all the
          following attributes are true.</p><div class="itemizedlist"><ul class="itemizedlist" style="list-style-type: disc; "><li class="listitem"><p>The magic number in the head table is
              correct.</p></li><li class="listitem"><p>Given the number of tables value in the offset
              table, the other values in the offset table are
              consistent.</p></li><li class="listitem"><p>The tags of the tables are ordered alphabetically
              and there are no duplicate tags.</p></li><li class="listitem"><p>The offset of each table is a multiple of 4. (That
              is, tables are long word aligned.)</p></li><li class="listitem"><p>The first actual table in the file comes immediately
              after the directory of tables.</p></li><li class="listitem"><p>If the tables are sorted by offset, then for all
              tables i (where index 0 means the the table with the
              smallest offset), Offset[i] + Length[i] &lt;= Offset[i+1]
              and Offset[i] + Length[i] &gt;= Offset[i+1] - 3. In other
              words, the tables do not overlap, and there are at most
              3 bytes of padding between tables.</p></li><li class="listitem"><p>The pad bytes between tables are all zeros.</p></li><li class="listitem"><p>The offset of the last table in the file plus its
              length is not greater than the size of the file.</p></li><li class="listitem"><p>The checksums of all tables are correct.</p></li><li class="listitem"><p>The head table's checkSumAdjustment field is
              correct.</p></li></ul></div></div></div><div role="fragment" class="section"><div class="titlepage"><div><div><h3 class="title"><a name="idm79886025552"></a>Signatures for TrueType Collections</h3></div></div></div><div role="specification" class="section"><div class="titlepage"><div><div><h4 class="title"><a name="section.30.3.1"></a>Specification</h4></div></div></div><p>The <a class="link" href="chapter.DSIG.html" title="Chapter 29. DSIG - Digital Signature Table">DSIG</a> table for a TrueType
	  Collection (TTC) must be the last table in the TTC file. The
	  offset and checksum to the table is put in the TTCHeader
	  (version 2). Signatures of TTC files are expected to be
	  Format 1 signatures.</p><p>The signature of a TTC file applies to the entire file,
	  not to the individual fonts contained within the
	  TTC. Signing the TTC file ensures that other contents are
	  not added to the TTC.</p><p>Individual fonts included in a TrueType collection
	  should not be individually signed as the process of making
	  the TTC could invalidate the signature on the font.</p></div></div></div>