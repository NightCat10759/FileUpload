#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
use HandleFile; 
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');

###   CGI Limits setting   ###
$CGI::POST_MAX = 1024 * 5000;

###   Object init   ###
my $query = new CGI;
my $file = new HandleFile();

##
my ($data, $i, @data, $key, $val, %FORM);

if ($ENV{'REQUEST_METHOD'} eq "GET") {
$data = $ENV{'QUERY_STRING'};
} elsif ($ENV{'REQUEST_METHOD'} eq "POST") {
read(STDIN,$data,$ENV{'CONTENT_LENGTH'});
}
##

###   儲存檔案目錄   ###
my $upload_dir = "../files";

###   filename   ###
my $filename = $query->param("file");


###  CGI Get the file  ###
my $upload_filehandle = $query->upload("file");

###  CGI Save the file  ###
open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;

###  CGI print file  ###
while ( <$upload_filehandle> )
{
    print UPLOADFILE;
}
close UPLOADFILE;


###   test   ###
#my $os_file = File::Spec->catfile("./test-file","test.txt");
#$file->setFile($os_file);

###   set file   ###
#$file->setFile($upload_file);

###   test print file   ###

print "Content-type: text/html\n\n";
print $data;

###  limit condition  ###
if (!$filename)
{
    print $query->header();
    print "There was a problem uploading your photo (try a smaller file).";
    exit;
} else {
    print "\nGet";
}
#$file->readFILE();



