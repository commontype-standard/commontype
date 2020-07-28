JAVA=java

# On Mac OS X / Homebrew with coreutils installed.
# On Linux, change this to csplit
CSPLIT = gcsplit
DB = $(shell brew --prefix docbook-xsl)/docbook-xsl/

SPECFILES= $(shell find src/chapter* -name '*xml')
xslt = $(JAVA) -jar jars/saxon9he.jar

all::

clean::
	rm -fr html docbook

htmls: html/commontype.html html/cff.html html/type2.html

publish:
	make mdhtml
	git add docs/*.md
	git commit -m "Rebuild" docs/*.md

docbooks: docbook/commontype.docbook docbook/cff.docbook docbook/type2.docbook

# markdown: docbook/commontype.docbook
# 	mkdir -p markdown
# 	pandoc --from docbook --to gfm --section-divs $< > markdown/commontype.md
# 	gcsplit --prefix='aots' --suffix-format='%03d.md' markdown/commontype.md "/^# /" "{*}"

docbook/commontype.docbook : src/commontype.xml xsl/aots2docbook.xsl $(SPECFILES)
	mkdir -p docbook
	$(xslt) -s:src/commontype.xml -xi -xsl:xsl/aots2docbook.xsl -o:docbook/commontype.docbook fontdir=../tests/ tracedir=../tests/

mdhtml : docbook/commontype.docbook
	xsltproc \
		--path "$(DB) $(DB)/xhtml" \
		--stringparam chunk.section.depth 0 \
		--stringparam chunker.output.doctype-public "" \
		--stringparam chunker.output.doctype-system "" \
		--stringparam chunker.standalone 1 \
		--stringparam chunker.output.omit-xml-declaration yes \
		--stringparam use.id.as.filename 1 \
        --stringparam base.dir docs/ \
		 xsl/mychunk.xsl docbook/commontype.docbook
	perl src/build-navigation.pl
	rename -f 's/.html/.md/' *.html

all:: htmls

