#!"C:\xampp\perl\bin\perl.exe"

use warnings;
use strict;
use CGI;
use CGI::Carp qw ( fatalsToBrowser );
use lib 'lib';
use HandleFile;
use Db; 
use File::Basename;
use File::Slurp;
use JSON;



# init Object
my $query = new CGI;
my $handlefile = new HandleFile();
my $db = new Db();


$CGI::POST_MAX = 1024 * 5000;
my $safe_filename_characters = "a-zA-Z0-9_.-";
my $safe_content_characters = "a-zA-Z0-9_.-";
my $upload_dir = "../files";
my $filename = $query->param("filename");

print $query->header('application/json;charset=UTF-8');
my $res = JSON -> new -> utf8 -> pretty(1);
my $json = $res -> encode({
    filename => $filename
});

print $json;


if ( !$filename )
{
print $query->header('');
die "There was a problem uploading your file (try a smaller file). file: fre${filename}few";
exit;
}

my ( $name, $path, $extension ) = fileparse ( $filename, '..*' );
$filename = $name . $extension;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;

if ( $filename =~ /^([$safe_filename_characters]+)$/ )
{
    $filename = $1;
}
else
{
    print "Filename contains invalid characters";
    exit;
}

my $upload_filehandle = $query->upload("file");

open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
binmode UPLOADFILE;

while ( <$upload_filehandle> )
{
    print UPLOADFILE;
}

close UPLOADFILE;

#打開file 進行parse
my $files = "../files/$filename";
&Main($files);

sub Main{

    my ($files)= @_;

    $handlefile->setFile($files);

    my $contents = read_file($files);

    # parse
    my ($key,$datetime,$content) = $handlefile->parseFile($contents);

    # 檢查內容是否有特殊字元
    $content =~ tr/ /_/;
    $content =~ s/[^$safe_content_characters]//g;

    if ( $content =~ /^([$safe_content_characters]+)$/ )
    {
        $content = $1;
        $content =~ tr/_/ /;
    }
    else
    {
        print "file content contains invalid characters";
        exit;
    }

    # 找出有maillog的部分 
    if ($handlefile->isformat($key)){

        #有就存入db
        $db->insertDb($datetime,$content,$filename);

    } else {

        #沒有就刪除
        my $file = $handlefile->getFile($files);
        $handlefile->deleteFile($file);

    }
 
}
