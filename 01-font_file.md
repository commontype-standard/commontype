<h3 id="font-file-structure">Font File Structure</h3>

* Data in the font file is stored in big-endian byte order. All types in this specification therefore refer to big-endian types.

<pre class="idl">
    typedef byte int8;
    typedef unsigned short USHORT;
    typedef short SHORT;
    typedef unsigned short F2DOT14;
    typedef unsigned short Offset16;
    typedef long LONG;
    typedef unsigned long ULONG;
    typedef unsigned long Offset32;
    typedef byte[] Tag;
</pre>
