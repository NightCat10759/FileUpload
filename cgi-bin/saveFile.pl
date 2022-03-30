#!"C:\xampp\perl\bin\perl.exe" -w

#  將資料切為日期時間、內容存到資料表中供查詢
#  ex. [maillog][2021-11-23 11:00:00] cheryl login.


###   使用module、中文處理   ###
use utf8;
use Encode;
use lib 'lib';
use HandleFile;
use Db; 
use File::Spec;
use strict;
use CGI;
use CGI::Carp qw( fatalsToBrowser );
use File::basename;
use File::Slurp;
use File::Find;
binmode(STDIN,':encoding(big5)');
binmode(STDOUT,':encoding(big5)');
binmode(STDERR,':encoding(big5)');

###   Object init   
my $Db = Db->new;
my $CGI = CGI->new;
my $file = new HandleFile();


## Find 找出所有檔案
print "Content-type: text/html\n\n";
print "All files:  ";

# 找資料夾中所有檔案
my $files = find( \&wanted, "../files");
sub wanted() {

    my ($self) = @_;
    # 列出檔案的絕對路徑
    my $files = $File::Find::name . "\n";
    print $files;
    ## Main ##
    my @files = split(" ",$files);
    # 把每個檔案找出

}

#for(my $i=0; $i <= @files; $i++){
#
#       print "<br>";
#       print $files[$i];
#       $file->setFile($files[$i]);
#       my $content = $file->readFile();
#       # parse
#       my ($key,$datetime,$contents) = $file->parseFile($content);
#       # 找出有maillog的部分 
#
#       if ($file->isformat($key)){
#
#           my ($dir1,$dir2,$fname) = split('/',$files[$i],3);
#           $file->showFile($key, $datetime, $contents, $fname);
#
#       } else {
#
#           print "incorrect";
#
#       }
#
#   }
#





##my $filename = '../files/data01.txt';
##$file->setFile($filename);

#savefile
#parse
#save to db
#print "filename = $filename";
#print "<br>";
#my $content = read_file($filename);
#print "$content <br>";
# parsefile 傳入txt內容
# 傳入operation運算子 回傳相對應的內容
#print "format:";
#print "<br>";
#$file->showFile($key,$datetime,$contents)
## 插入資料
#  datetime,$content,$filename
#$Db->insertDb($datetime, $contents, $fname);




#readfile

#saveFile to db



