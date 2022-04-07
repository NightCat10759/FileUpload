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
#my $filename = $query->param("filename");
my $filename = "data01.txt";


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

#my $upload_filehandle = $query->upload("file");
#
#open ( UPLOADFILE, ">$upload_dir/$filename" ) or die "$!";
#binmode UPLOADFILE;
#
#while ( <$upload_filehandle> )
#{
#    print UPLOADFILE;
#}
#
#close UPLOADFILE;

#打開file 進行parse
my $files = "../files/$filename";



# 主程式處理檔案流程
&Main($files);



# 主程式處理檔案流程
sub Main{

    my ($files)= @_;

    # 將檔案存入物件
    $handlefile->setFile("../files/data01.txt");
#    $handlefile->setFile($files);


    # 讀取檔案進行處理
    # 讀取檔案內容到最後一行跳開
    # read line by line
    my ($contents , $last_line) = &read_input_File();

#    print $query->header('application/json;charset=UTF-8');
#    my $res = JSON -> new -> utf8 -> pretty(1);
#    my $json = $res -> encode({
#        filename => $filename
#    });
#
#    print $json;

}




# 讀取檔案內容
sub read_input_File
{
    my $file = $handlefile->getFile();

    if ( $file ){

        open(FILE, $file ) or die "$!";
        my $str = "";
        print "<br />";

        # 讀每一行字
        while( defined( my $line = <FILE> )){

            Encode::_utf8_on($line);

            # 逐行parse
            my ($key,$datetime,$content) = $handlefile->parseFile($line);

            #showInfo ($key, $datetime, $contents, $fname)
            print $query->header();
            print "key: $key\n";
            print "datetime: $datetime\n";
            print "content: $content\n";

            # 找出有maillog的部分 
            if ($handlefile->isformat($key)){

                #有就存入db
                $db->insertDb($datetime,$content,$filename);

            } else {
                print "key:$key is wrong\n";
                #沒有就刪除
                exit
#                my $file = $handlefile->getFile($files);
#                $handlefile->deleteFile($file);

            }

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

        # 下一行字
        }

        print "<br />";
        close(FILE);

    } else {

        print "No such FILE";

    }

}
