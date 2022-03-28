#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
use Db;
use DBI;
use HandleFile;
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');

### 顯示test資料
my $CGI = CGI->new;
my $Db = Db->new;

#my $sth = $dbh->prepare("SELECT * FROM file");   # 待處理SQL句子q
#$sth->execute();    # 執行SQL

# repeat output data
#while ( my @row = $sth->fetchrow_array() )
#{
#       print join('\t', @row)."\n";
#}

## 插入資料
#  datetime,$content,$filename
$Db->insertDb("2011-10-10"," IA AM CONTENT ","filename.txt");
$Db->showDb();
print $CGI->redirect("../index.cgi");
