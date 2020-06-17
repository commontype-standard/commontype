<?xml version="1.0" encoding="ASCII"?><!--This file was created automatically by html2xhtml--><!--from the HTML stylesheets.--><xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:exsl="http://exslt.org/common" xmlns="http://www.w3.org/1999/xhtml" version="1.0" exclude-result-prefixes="exsl">

<!-- ********************************************************************
     $Id: chunk.xsl 9801 2013-09-06 19:23:43Z bobstayton $
     ********************************************************************

     This file is part of the XSL DocBook Stylesheet distribution.
     See ../README or http://docbook.sf.net/release/xsl/current/ for
     copyright and other information.

     ******************************************************************** -->

<!-- ==================================================================== -->


<!-- First import the non-chunking templates that format elements
     within each chunk file. In a customization, you should
     create a separate non-chunking customization layer such
     as mydocbook.xsl that imports the original docbook.xsl and
     customizes any presentation templates. Then your chunking
     customization should import mydocbook.xsl instead of
     docbook.xsl.  -->
<xsl:import href="docbook.xsl"/>

<!-- chunk-common.xsl contains all the named templates for chunking.
     In a customization file, you import chunk-common.xsl, then
     add any customized chunking templates of the same name. 
     They will have import precedence over the original 
     chunking templates in chunk-common.xsl. -->
<xsl:import href="chunk-common.xsl"/>

<!-- The manifest.xsl module is no longer imported because its
     templates were moved into chunk-common and chunk-code -->

<!-- chunk-code.xsl contains all the chunking templates that use
     a match attribute.  In a customization it should be referenced
     using <xsl:include> instead of <xsl:import>, and then add
     any customized chunking templates with match attributes. But be sure
     to add a priority="1" to such customized templates to resolve
     its conflict with the original, since they have the
     same import precedence.
     
     Using xsl:include prevents adding another layer
     of import precedence, which would cause any
     customizations that use xsl:apply-imports to wrongly
     apply the chunking version instead of the original
     non-chunking version to format an element.  -->
<xsl:include href="chunk-code.xsl"/>

<xsl:template name="chunk-element-content">
  <xsl:param name="prev"/>
  <xsl:param name="next"/>
  <xsl:param name="nav.context"/>
  <xsl:param name="content">
    <xsl:apply-imports/>
  </xsl:param>
 <xsl:copy-of select="$content"/>
</xsl:template>

<xsl:template name="make.toc">
  <xsl:param name="toc-context" select="."/>
  <xsl:param name="toc.title.p" select="true()"/>
  <xsl:param name="nodes" select="/NOT-AN-ELEMENT"/>
</xsl:template>

<!-- hack to preserve role attributes -->
<xsl:template match="*" mode="html.lang.attribute">
  <xsl:attribute name="role">
    <xsl:value-of select="@role"/>
  </xsl:attribute>
  <!-- match the attribute name to the output type -->
  <xsl:choose>
    <xsl:when test="@lang and $stylesheet.result.type = 'html'">
      <xsl:attribute name="lang">
        <xsl:value-of select="@lang"/>
      </xsl:attribute>
    </xsl:when>
    <xsl:when test="@lang and $stylesheet.result.type = 'xhtml'">
      <xsl:attribute name="xml:lang">
        <xsl:value-of select="@lang"/>
      </xsl:attribute>
    </xsl:when>
  </xsl:choose>
</xsl:template>

<!-- Use HTML not XHTML anchors -->
<xsl:template name="anchor">
  <xsl:param name="node" select="."/>
  <xsl:param name="conditional" select="1"/>

  <xsl:choose>
    <xsl:when test="$generate.id.attributes != 0">
      <!-- No named anchors output when this param is set -->
    </xsl:when>
    <xsl:when test="$conditional = 0 or $node/@id or $node/@xml:id">
      <a>
        <xsl:attribute name="name">
          <xsl:call-template name="object.id">
            <xsl:with-param name="object" select="$node"/>
          </xsl:call-template>
        </xsl:attribute>
        <xsl:comment></xsl:comment>
      </a>
    </xsl:when>
  </xsl:choose>
</xsl:template>

</xsl:stylesheet>
