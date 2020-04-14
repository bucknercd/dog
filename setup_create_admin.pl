use strict;


open(FH, ".env") or die $!;
my %secrets;
foreach my $line (<FH>) {
	chomp($line);
	my ($key, $value) = split(/=/, $line);
	$secrets{$key} = $value;
}
close(FH);

open(OUT, ">mongo/create_admin.js") or die $!;
print OUT "use admin\n";
print OUT "db.createUser({user: \"$secrets{'MONGO_USER'}\", pwd: \"$secrets{'MONGO_PASS'}\", ".
	  "roles: [\"root\"], mechanisms: [\"$secrets{'MONGO_AUTH_TYPE'}\"]})\n";
close(OUT);
