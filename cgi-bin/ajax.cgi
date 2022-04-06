#!"C:\xampp\perl\bin\perl.exe"

use strict;
use warnings;

use JSON; 
use CGI;

binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


my $cgi = CGI->new;

print $cgi->header('application/json;charset=UTF-8');

my $keyword = $cgi->param('keyword');    
my $date = $cgi->param('date');  

unless (($keyword eq '') || ($date eq '')){
    my $op = JSON -> new -> utf8 ;
    my $json = $op -> encode({
        keyword => $keyword,
        date => $date
    });
    print $json;
}

#convert  data to JSON

#my $op = JSON -> new -> utf8 -> pretty(1);