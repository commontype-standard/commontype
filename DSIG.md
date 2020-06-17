# DSIG - Digital Signature Table

## Overview

### Specification

The DSIG table contains the digital signature of the OpenType font.
Signature formats are widely documented and rely on a key pair
architecture. Software developers, or publishers posting material on the
Internet, create signatures using a private key. Operating systems or
applications authenticate the signature using a public key.

The W3C and major software and operating system developers have
specified security standards that describe signature formats, specify
secure collections of web objects, and recommend authentication
architecture. OpenType fonts with signatures will support these
standards.

OpenType fonts offer many security features:

  - Operating systems and browsing applications can identify the source
    and integrity of font files before using them,

  - Font developers can specify embedding restrictions in OpenType
    fonts, and these restrictions cannot be altered in a font signed by
    the developer.

The enforcement of signatures is an administrative policy, enabled by
the operating system. Windows will soon require installed software
components, including fonts, to be signed. Internet browsers will also
give users and administrators the ability to screen out unsigned objects
obtained on-line, including web pages, fonts, graphics, and software
components.

Anyone can obtain identity certificates and encryption keys from a
certifying agency, such as Verisign or GTE's Cybertrust, free or at a
very low cost.

The DSIG table is organized as follows. The first portion of the table
is the header:

<table>
<caption>DSIG Header</caption>
<thead>
<tr class="header">
<th>Type</th>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ULONG</td>
<td>ulVersion</td>
<td>Version number of the DSIG table (0x00000001)</td>
</tr>
<tr class="even">
<td>USHORT</td>
<td>usNumSigs</td>
<td>Number of signatures in the table</td>
</tr>
<tr class="odd">
<td>USHORT</td>
<td>usFlag</td>
<td><p>permission flags</p>
<p>Bit 0: cannot be resigned</p>
<p>Bit 1-7: Reserved (Set to 0)</p></td>
</tr>
</tbody>
</table>

The version of the DSIG table is expressed as a ULONG, beginning at 0.
The version of the DSIG table currently used is version 1 (0x00000001).

Permission bit 0 allows a party signing the font to prevent any other
parties from also signing the font (counter-signatures). If this bit is
set to zero (0) the font may have a signature applied over the existing
digital signature(s). A party who wants to ensure that their signature
is the last signature can set this bit.

The DSIG header information is followed by entries for each of the
signatures in the table specifying format and offset information:

| Type  | Name     | Description                                                   |
| ----- | -------- | ------------------------------------------------------------- |
| ULONG | ulFormat | format of the signature                                       |
| ULONG | ulLength | Length of signature in bytes                                  |
| ULONG | ulOffset | Offset to the signature block from the beginning of the table |

Format/Offset Table

This information is then followed by one or more signature blocks:

| Type     | Name        | Description                                            |
| -------- | ----------- | ------------------------------------------------------ |
| USHORT   | usReserved1 | Reserved for later use; 0 for now                      |
| USHORT   | usReserved2 | Reserved for later use; 0 for now                      |
| ULONG    | cbSignature | Length (in bytes) of the PKCS\#7 packet in pbSignature |
| BYTE\[\] | bSignature  | PKCS\#7 packet                                         |

Signature Block

The format identifier specifies both the format of the signature object,
as well as the hashing algorithm used to create and authenticate the
signature. Currently only one format is defined, but at least one other
format will soon be defined to handle subsetting scenarios. Format 1
supports PKCS\#7 signatures with X.509 certificates and
counter-signatures, as these signatures have been standardized for use
by the W3C with the participation of numerous software developers.

For more information about PKCS\#7 signatures, see
<ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-7.asc>.

For more information about counter-signatures, see
<ftp://ftp.rsa.com/pub/pkcs/ascii/pkcs-9.asc>.

### Annotation

It is unclear what is measured by the field ulLength in a Format/Offset
table: it is the length of the Signature Block table, or the length of
the bSignature array in that table? In either case, this seems to be a
redundant value, and its correlation to the cbSignature field should be
noted. Looking at Adobe fonts, it seems that we interpreted it as the
length of the signature block.

The Format/Offset Table is a misnommer. This is actually a *record*, not
a *table*, since it is not pointed. Similarly, the DSIG header should be
augmented by an array of those records.

The reference point of the ulOffset field in the Format/Offset is
unclear. It is from the beginning of the DSIG table, or from the
beginning of the Format/Offset record (thus being inconsistent with the
layout tables)? Looking at Adobe fonts, it seems that we interpreted it
as the relative to the beginning of the DSIG table.

The Signature Block is a misnommer. This is actually a *table*, not a
*block*.

### XML Representation

``` 
 ==
      
  DSIG =
    element DSIG {
      attribute version { "1" },
      attribute flags { text },
      element signature {
        attribute format { text },
        text
      }*
    }
```

## Format 1: For whole fonts, with either TrueType outlines and/or CFF data

### Specification

PKCS\#7 or PKCS\#9. The signed content digest is created as follows:

  - If there is an existing DSIG table in the font,
    
      - Remove DSIG table from font.
        
        Remove DSIG table entry from sfnt Table Directory.
        
        Adjust table offsets as necessary.
        
        Zero out the file checksum in the head table.
        
        Add the usFlag (reserved, set at 1 for now) to the stream of
        bytes

  - Hash the full stream of bytes using a secure one-way hash (such as
    MD5) to create the content digest.

  - Create the PKCS\#7 signature block using the content digest.

  - Create a new DSIG table containing the signature block.

  - Add the DSIG table to the font, adjusting table offsets as
    necessary.

  - Add a DSIG table entry to the sfnt Table Directory.

  - Recalculate the checksum in the head table.

Prior to signing a font file, ensure that all the following attributes
are true.

  - The magic number in the head table is correct.

  - Given the number of tables value in the offset table, the other
    values in the offset table are consistent.

  - The tags of the tables are ordered alphabetically and there are no
    duplicate tags.

  - The offset of each table is a multiple of 4. (That is, tables are
    long word aligned.)

  - The first actual table in the file comes immediately after the
    directory of tables.

  - If the tables are sorted by offset, then for all tables i (where
    index 0 means the the table with the smallest offset), Offset\[i\] +
    Length\[i\] \<= Offset\[i+1\] and Offset\[i\] + Length\[i\] \>=
    Offset\[i+1\] - 3. In other words, the tables do not overlap, and
    there are at most 3 bytes of padding between tables.

  - The pad bytes between tables are all zeros.

  - The offset of the last table in the file plus its length is not
    greater than the size of the file.

  - The checksums of all tables are correct.

  - The head table's checkSumAdjustment field is correct.

## Signatures for TrueType Collections

### Specification

The [DSIG](#chapter.DSIG) table for a TrueType Collection (TTC) must be
the last table in the TTC file. The offset and checksum to the table is
put in the TTCHeader (version 2). Signatures of TTC files are expected
to be Format 1 signatures.

The signature of a TTC file applies to the entire file, not to the
individual fonts contained within the TTC. Signing the TTC file ensures
that other contents are not added to the TTC.

Individual fonts included in a TrueType collection should not be
individually signed as the process of making the TTC could invalidate
the signature on the font.

