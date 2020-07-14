#!/usr/bin/perl
use warnings; use strict; use File::Slurp;
mkdir "_data";
open OUT, ">_data/navigation.yml" or die $!;
print OUT "chapters:\n";
open IN, "docbook/commontype.docbook" or die $!;
my $last_url;
while (<IN>) {
    next unless /chapter|title/;
    if (m{<chapter.*id="(chapter.[^"]+)".*>}) { $last_url = $1; }
    if (m{<title.*>(.*)</title>} and $last_url) {
        print OUT qq{    - title: "$1"\n};
        print OUT qq{      url: "$last_url"\n};
        $last_url = "";
    }
}
close OUT;
