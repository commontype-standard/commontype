#!/usr/bin/perl
use warnings; use strict; use File::Slurp;
mkdir "_data";
open OUT, ">_data/navigation.yml";
print OUT "chapters:\n";
for (<aots*.md>) {
    my $contents = read_file($_);
    my ($header) = ($contents =~/^# (.*)/) or next;
    # Rename tables
    my $newfile = $_;
    if ($header =~ /^(\S+)\s*-/) {
    	$newfile = $1.".md";
    	$newfile =~ s{/}{_}; # OS/2
    	rename $_, $newfile;
    }
    $newfile =~ s/.md$//;
    print OUT qq{    - title: "$header"\n};
    print OUT qq{      url: "$newfile"\n};
}
close OUT;
