use strict;


open(FH, ".env") or die $!;
my %secrets;
foreach my $line (<FH>) {
	chomp($line);
	my ($key, $value) = split(/=/, $line);
	$secrets{$key} = $value;
}
close(FH);

open(FH, "mongo/create_admin.js");
my @output;
foreach my $line (<FH>) {
	$line =~ s/admin/$secrets{'MONGO_DB'}/;
	$line =~ s/username/$secrets{'MONGO_USER'}/;
	$line =~ s/password/$secrets{'MONGO_PASS'}/;
	push(@output, $line);
}
close(FH);

open(OUT, ">mongo/create_admin.js") or die $!;
print OUT join('', @output);
close(OUT);
