JAVA=java

# On Mac OS X / Homebrew with coreutils installed.
# On Linux, change this to csplit
CSPLIT = gcsplit

xslt = $(JAVA) -jar jars/saxon9he.jar

all::

clean::
	rm -fr html docbook

htmls: html/opentype.html html/cff.html html/type2.html

docbooks: docbook/opentype.docbook docbook/cff.docbook docbook/type2.docbook

markdown: docbook/opentype.docbook
	mkdir -p markdown
	pandoc --from docbook --to gfm $< > markdown/opentype.md
	gcsplit --prefix='aots' --suffix-format='%03d.md' markdown/opentype.md "/^# /" "{*}"
	perl src/build-navigation.pl

docbook/%.docbook : src/%.xml xsl/aots2docbook.xsl
	mkdir -p docbook
	$(xslt) -s:$< -xsl:xsl/aots2docbook.xsl -o:$@ fontdir=../tests/ tracedir=../tests/

html/%.html : docbook/%.docbook
	$(xslt) -s:$< -xsl:xsl/docbook2html.xsl -o:$@ imagedir=../src/images

all:: htmls

