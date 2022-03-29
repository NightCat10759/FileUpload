#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
use HandleForm;
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
use Db;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


###   Object init   
my $cgi = CGI->new();
my $db = Db->new();

# get
my $cgi = CGI->new;



if( my %input = HandleForm->GetFormInput() ){
     my $keyword = $input{'keyword'};
     my $date = $input{'date'};
     print "keyword = $keyword";
     print "<br />";
     print "date = $date<br />";
     ($date ,my $time) = split('T',$date,2);
     $time = $time . ":00";
     my $datetime = $date ." ". $time;
     print "date = $datetime<br />";
     # 輸入關鍵字跟日期查詢資料
     #  showDb(date, content) = @_;
     my ($dbh, $sth) = $db->showDb($datetime, $keyword);
     while(my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};
          # 如果包含關鍵字印出
          if ( $content =~ /$keyword/ ){
               print "                <form class='contents__form' action='./cgi-bin/searchFile.pl' method='GET' enctype='multipart/form-data'>";
               print "                     <span class='contents__No'><h3>$id</h3></span>";
               print "                     <span class='contents__date'><h3>$date</h3></span>";
               print "                     <span class='contents__content'><h3>$content</h3></span>";
               print "                     <span class='contents__move'><button>修改</button>";
               print "                                                  <button>刪除</button></span>";
               print "                </form>";
          }
     }
$sth->finish();
$dbh->disconnect();
} unless (my %input = HandleForm->GetFormInput()) {
#gets
     my ($dbh, $sth) = $db->showDbs();
     while(my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};
          print "                <form class='contents__form' action='./cgi-bin/searchFile.pl' method='GET' enctype='multipart/form-data'>";
          print "                     <span class='contents__No'><h3>$id</h3></span>";
          print "                     <span class='contents__date'><h3>$date</h3></span>";
          print "                     <span class='contents__content'><h3>$content</h3></span>";
          print "                     <span class='contents__move'><button>修改</button>";
          print "                                                  <button>刪除</button></span>";
          print "                </form>";
     }
$sth->finish();
$dbh->disconnect();
} else {
     print "ERROR";
}