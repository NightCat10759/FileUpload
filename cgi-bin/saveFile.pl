#!"C:\xampp\perl\bin\perl.exe"

#  將資料切為日期時間、內容存到資料表中供查詢
#  ex. [maillog][2021-11-23 11:00:00] cheryl login.


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
use File::Slurp;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');

###   Object init   
my $CGI = CGI->new;
my $file = new HandleFile();
my $filename = '../files/data01.txt';
$file->setFile($filename);

#savefile
#parse
#save to db
print "Content-type: text/html\n\n";
print "filename = $filename";
print "<br>";
my $content = read_file($filename);
print "$content <br>";
# parsefile 傳入txt內容
# 傳入operation運算子 回傳相對應的內容
my ($datetime,$contents) = $file->parseFile($content);

print "$datetime <br>";
print "$contents <br>";
#readfile

#saveFile to db



