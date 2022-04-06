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

use URI::URL;
use JSON;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


###   Object init   
my $cgi = CGI->new();
my $db = Db->new();

print $cgi->header('application/json;charset=UTF-8');
my $keyword = $cgi->param('keyword');    
my $date = $cgi->param('date');



# 輸入不為空值
unless (($keyword eq '') || ($date eq '')){

     ($date ,my $time) = split('T',$date,2);
     $time = $time . ":00";
     my $datetime = $date ." ". $time;

     # 輸入關鍵字跟日期查詢資料
     my ($dbh, $sth) = $db->showDb($datetime, $keyword);
     &getContentId($keyword, $sth);
     $sth->finish();
     $dbh->disconnect();

} else {
# 頁尾
     my ($dbh, $sth) = $db->showDbs();
     &getContents($sth);
     $sth->finish();
     $dbh->disconnect();
}

sub getContentId{
     #get
     my ($keyword,$sth) = @_;
     ##while
     if(my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};
          # 如果包含關鍵字印出
          if ( $content =~ /$keyword/ ){
               $content =~ s/{ }//;
               my $res = JSON -> new -> utf8 -> pretty(1);
               my $json = $res -> encode({
                    content => $content,
                    date => $date,
                    id => $id
               });
   #            my $result = $result + $json;
               print $json;
          }
    #      return $result;
     }

}

sub getContents{
     #gets
     my ($sth) = @_;
     ##while
     if (my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};

          my $res = JSON -> new -> utf8 -> pretty(1);
          my $json = $res -> encode({
               content => $content,
               date => $date,
               id => $id
          });
          print $json;
#          &printout($id, $date, $content);
     }

}

#sub printout{
#     my($id, $date, $content) = @_;
#     # 如果內容有特殊字元 做轉換
#     $content =~ s/{ }//;
#     print "<div class='container'>";
#     print "<form class='content__form' action='./cgi-bin/editFile.pl'method='GET' enctype='multipart/form-data'>";
#     print "     <span class='contents__No'><h3>$id</h3></span>";
#     print "     <span class='contents__date'><h3>$date</h3></span>";
#     print "     <span class='contents__content'>";
#     print               $cgi->textfield(-name => 'editContent' ,-default => $content);
#     #<input name='editContent' value='$content' />
#     print "     </span>";
#     print "     <span class='contents__move'>";                    
#     print "        <button  class='contents__but__edit' name='edit'  value='$id'>修改</button>";
#     print "        <button  class='contents__but__dele' name='delete' value='$id'>刪除</button>";
#     print "     </span>";
#     print "</form>";
##     &footer();
#     print "</div>";
#}
#
#sub footer{
#     print "<div class='footer'>";
#     print "</div'>";
#}