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
 
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');

### 顯示test資料
my $cgi = CGI->new;
my $db = Db->new;
my %input = HandleForm->GetFormInput();

if ( %input && (my $id = $input{'delete'}) ) {
# 刪除指定的id
    #($self, $id)
    $db->deleteDb($id);
    print $cgi->redirect('../index.cgi');
}

if ( %input && (my $id = $input{'edit'}) ){
# 編輯內容，將輸入內容替換原先內容
    #(content, id)
    my $editContent = $input{'editContent'};
    $db->editDb($editContent, $id);
    print $cgi->redirect('../index.cgi');
}
