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
unless ( ($keyword eq '') && ($date eq '') ){

     ($date ,my $time) = split('T',$date,2);
     $time = $time . ":00";
     my $datetime = $date ." ". $time;

     # 輸入關鍵字跟日期查詢資料
     my ($dbh, $sth) = $db->get($datetime, $keyword);
     &getContentId($keyword, $sth);
     $sth->finish();
     $dbh->disconnect();

} else {
# 頁尾
     my ($dbh, $sth) = $db->gets();
     &getContents($sth);
     $sth->finish();
     $dbh->disconnect();
}

sub getContentId{
     #get
     my ($keyword,$sth) = @_;
     my @arr = ();

     ##while
     while(my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};
          # 如果包含關鍵字印出
          # 加上上箭頭跟錢字
          if ( $content =~ /$keyword/ ){

              push @arr, {
                    content => $content,
                    date => $date,
                    id => $id
               } ;
          }
    #      return $result;
     }

     # 轉換成JSON輸出
     my $res = JSON -> new -> utf8 -> pretty(1);
     my $json_text = to_json \@arr, {ascii => 1, pretty => 1};
     
     print $json_text;

}

sub getContents{
     #gets
     my ($sth) = @_;
     my @arr = ();

     while (my $ref = $sth->fetchrow_hashref()){
          my $id = $ref->{id};
          my $date = $ref->{date};
          my $content =  $ref->{content};

          # 將hash放入array
          push @arr, {
               content => $content,
               date => $date,
               id => $id
          } ;

     }

     # 轉換成JSON輸出
     my $res = JSON -> new -> utf8 -> pretty(1);
     my $json_text = to_json \@arr, {ascii => 1, pretty => 1};

     print $json_text;

}


#sub footer{
#     print "<div class='footer'>";
#     print "</div'>";
#}