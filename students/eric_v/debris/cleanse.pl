#!/usr/bin/perl
use strict;
use warnings;
use diagnostics;
use Getopt::Long qw(GetOptions);

# The purpose of this script is to fix the UTF-8 values that sneak in when
# a file is pulled down from the web.
# The typical use is: perl cleanse.pl <file to be cleansed>
#
# Switch options are:
# Identify input file: input|i|f <file to be cleansed>
# Help:   help|h 
# Don't overwrite file, rather preserve and create an additional _out file: no_overwrite|n
#
# Created: Eric Vegors 2 April 2015


#Initialization
########################

my $input_file;
my $help;
my $no_overwrite;
GetOptions(
'input|i|f=s' => \$input_file,
'help|h' => \$help,
'no_overwrite|n' => \$no_overwrite,
) or die "Expected usage: $0 -hnf --input <input_file>\n";

my $fh_in;
my $fh_out;
my $filename_in = $ARGV[0];
	Input_filename_overwrite ();
my $filename_out = "";
	if ($filename_in) {$filename_out = $filename_in.'_out';}
my $line = "";
my $good_line = "";
my $bad_line_flag = 0;
my $fix_count = 0;

#improper UTF-8 values that can be pulled in from a webpage or .pdf book
########################
my %bad_juju = (
   chr(0x00A0) => ' ',
   chr(0x0091) => "'",
   chr(0x0092) => "'",
   chr(0x0093) => '"',
   chr(0x0094) => '"',
   chr(0x0097) => '-',
   chr(0x00AB) => '"',
   chr(0x00A9) => '/',
   chr(0x00AE) => '/',
   chr(0x2018) => "'",
   chr(0x2019) => "'",
   chr(0x201C) => '"',
   chr(0x201D) => '"',
   chr(0x2022) => '/',
   chr(0x2013) => '-',
   chr(0x2014) => '-',
   chr(0x2122) => '/',
);


#User input processing
########################

# As an option, print the acceptable options to the screen
Help_Options ();

# No file provided by user to cleanse
if (!$filename_in) {
	print "\nno input file provided\n";
	print "expected use:   perl $0 <file to be cleansed>\n";
	print "\nexiting program so user can try again\n";
	exit;
	}
	
#Open files for reading and writing
########################
open($fh_in, "<", $filename_in)  		# open input file
	or die "$0 can't open $filename_in for reading: $!";

open($fh_out, ">", $filename_out)  		# open output file
	or die "$0 can't open $filename_out for writing: $!";

#Begin processing
########################
print "\nRefining $filename_in\n\n";
while ($line = <$fh_in>) {  	#loop through each line of input file
	chomp $line;
	$good_line = $line;
	$bad_line_flag = 0;
	
	for my $bad ( keys %bad_juju ) {
		my $good = $bad_juju {$bad};
		if ($good_line =~ m/\Q$bad\E/) {		#identify bad line
			$good_line =~ s/\Q$bad\E/$good/g;	#fix bad line
			$bad_line_flag = 1;					#set bad line flag
			$fix_count++;						#update cleanse action count
		}
	}
	
	print "$line\n" if ($bad_line_flag == 1) ;  			#Notify user of bad line found
	print "$good_line\n\n" if ($bad_line_flag == 1) ;   	#Notify user of bad line fixed
	print $fh_out "$line\n" if ($bad_line_flag == 0) ;		#print unchanged lines to output file
	print $fh_out "$good_line\n" if ($bad_line_flag == 1) ;	#print modified lines to output file
}

#Close files
########################
close($fh_in) 
	or die "$0 can't close $filename_in after reading: $!";
	
close($fh_out)
	or die "$0 can't close $filename_out after writing: $!";

#Replace original file with new cleansed file, unless otherwise directed (-n switch)
########################
if (!$no_overwrite) {
	system("rm $filename_in");
	system("mv $filename_out $filename_in");
	system("chmod 755 $filename_in"); #assure executability of cleansed script
	}

#Notify user of results
########################
print "\nno cleanse actions performed\n" if ($fix_count == 0);
print "\n$fix_count cleanse actions performed in updating $filename_in\n" if ($fix_count >= 1);

###################
#Subroutines	
##################

##########
# As an option, print the acceptable switch options to the screen
#####
sub Help_Options {
if ($help) {
	print "\n\nHelp information:\n";
	print "expected use:   perl $0 <file to be cleansed>\n";
	exit;
	}
}

##########
# Assign $input_file value to $filename_in
#####
sub Input_filename_overwrite {	
	if ($input_file and $ARGV[0]) {
		print "User provided multiple input file values";
		print "Using $input_file as input file";
		$filename_in = $input_file;
		}
	elsif ($input_file) {
		$filename_in = $input_file;
		}
}
