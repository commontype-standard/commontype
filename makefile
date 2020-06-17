JAVAC=javac
JAVA=java

xslt = $(JAVA) -jar jars/saxon9he.jar

all::

clean::
	rm -fr html docbook

htmls: html/opentype.html html/cff.html html/type2.html

docbooks: docbook/opentype.docbook docbook/cff.docbook docbook/type2.docbook

docbook/%.docbook : src/%.xml
	mkdir -p docbook
	$(xslt) -s:$< -xsl:xsl/aots2docbook.xsl -o:$@ fontdir=../tests/ tracedir=../tests/

html/%.html : docbook/%.docbook
	$(xslt) -s:$< -xsl:xsl/docbook2html.xsl -o:$@ imagedir=../src/images

all:: htmls

