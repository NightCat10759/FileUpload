#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
use HandleFile;
#use Db; 
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');


###   Object init   
my $CGI = CGI->new;
my $file = new HandleFile();

###   CGI Limits setting   
$CGI::POST_MAX = 5000 * 5000;
$CGI::DISABLE_UPLOADS = 1;

###  CGI Get the file  
my $upload_dir = "../files";  
my $filename = $CGI->param("uploadfile");
my $upload_filehandle = $CGI->upload("uploadfile"); 

###  CGI Save the file  
open ( UPLOADFILE,">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;

while ( <$upload_filehandle> ) {
    print UPLOADFILE;
}

close UPLOADFILE;


###   測試將已儲存資料打開 
my $os_file = File::Spec->catfile("../files",$filename);

#   set file   
$file->setFile($os_file);

# redirect
#print $CGI->redirect("../index.cgi");

###  print file   

print "Content-Type: multipart/form-data\n\n";
print "filename: $filename"
print "<br>";

#  limit condition  
if (!$filename)
{
    print "There was a problem uploading your photo (try a smaller file).";
    print "<br>";
    exit;
} else {
    print "Get";
    print "<br>";
}
print "file content: ";
print "<br>";







