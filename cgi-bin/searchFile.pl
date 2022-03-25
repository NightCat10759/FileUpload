#!"C:\xampp\perl\bin\perl.exe"
#把files裡面的文件掃描一次，parse完丟到資料庫。
#在前端show出資料，並照日期排序


# /* Code */
#掃描files資料夾的檔案
#parse [maillog][日期時間] 內容 存入Database
#由前端從Db把資料調用出來並排序

# forms-lib.pl
# Decodes URLs and unpacks from input.
# Read the form contents into $input, decodes it, unpacks it,
# and returns it as an associative array.

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
require './lib/HandleForm.pl';
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');

my %input = &GetFormInput();
my $keyword = $input{'keyword'};
my $date = $input{'date'};

print "content-type: text/html\n\n";
print "keyword = $keyword";
print "<br />";
print "date = $date";

