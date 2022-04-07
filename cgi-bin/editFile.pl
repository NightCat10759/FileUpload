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



### 顯示test資料
my $cgi = CGI->new;
my $db = Db->new;

my $delete_ID = $cgi->param('delete');   
my $edit_ID = $cgi->param('edit');    
my $editContent = $cgi->param('content'); 

print $cgi->header('application/json;charset=UTF-8');
my $res = JSON -> new -> utf8 -> pretty(1);

unless ($delete_ID eq '') {

    $db->deleteDb($delete_ID);

    my $json = $res -> encode({
        delete_ID => $delete_ID,
    #    edit => $edit_ID,
    });
    print $json;
}

unless ($edit_ID eq '') {

    $db->editDb($editContent, $edit_ID);

    my $json = $res -> encode({
        edit_ID => $edit_ID,
        content => $editContent
    });
    print $json;
}


### 處理json資料


#if ( %input && (my $id = $input{'delete'}) ) {
# 刪除指定的id
    #($self, $id)
#    $db->deleteDb($id);
#}
#
#if ( %input && (my $id = $input{'edit'}) ){
## 編輯內容，將輸入內容替換原先內容
#    #(content, id)
#    my $editContent = $input{'editContent'};
#    $db->editDb($editContent, $id);
#    print $cgi->redirect('../index.cgi');
#}
