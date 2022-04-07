#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
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

### 過濾edit content 特殊字元
my $safe_filename_characters = "a-zA-Z0-9_.-";

if ($editContent){
    $editContent =~ tr/ /_/;
    $editContent =~ s/[^$safe_filename_characters]//g;

    if ( $editContent =~ /^([$safe_filename_characters]+)$/ )
    {
        $editContent = $1;
        $editContent =~ tr/_/ /;
    }
    else
    {
        print "File content contains invalid characters";
        exit;
    }
}


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

