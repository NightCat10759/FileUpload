#!"C:\xampp\perl\bin\perl.exe"

###   使用module、中文處理   ###
use utf8;
use Encode;
use strict;
use CGI;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


###   Object init   
my $CGI = CGI->new();

print "Content-type: text/html\n\n'";
print "<!DOCTYPE html>";
print "<html lang='en'>";
print "<head>";
print "    <meta charset='UTF-8'>";
print "    <meta http-equiv='X-UA-Compatible' content='IE=edge'>";
print "    <meta name='viewport' content='width=device-width, initial-scale=1.0'>";
print "    <link rel='stylesheet' href='style.css?v=<?=time(1)?>'>";
print "    <title>file_upload</title>";
print "</head>";
print "<body>";
print "    <main>";
print "        <form action='./cgi-bin/testDb.pl' method='get' enctype='multipart/form-data'>";
print "            <button type='submit'>testDb</button>";
print "        </form>";
print "        <form action='./cgi-bin/saveFile.pl' method='get' enctype='multipart/form-data'>";
print "            <button type='submit'>SAVE</button>";
print "        </form>";
print "        <form action='./cgi-bin/server.cgi' method='get' enctype='multipart/form-data'>";
print "            <div class='col_upload'>";
print "                <span class='upload'><input type='file' accept='txt' name='uploadfile'>上傳檔案</button></span>";
print "                <span class='upload__logo'><button type='submit'><img src='./img/upload.webp' alt=''></button></span>";
print "            </div>";
print "        </form>";
print "        <form action='./cgi-bin/searchFile.pl' method='GET' enctype='multipart/form-data'>";
print "            <div class='col_search'>";
print "                <span class='keyword'><input type='text' name='keyword' placeholder='關鍵字' /></span>";
print "                <span class='date'><input type='text' name='date' placeholder='日期' /></span>";
print "                <span class='search__logo'><button type='submit'><img src='./img/search.png' alt=''></i></button></span>";
print "            </div>";
print "        </form>";
print "            <div class='col_title'>";
print "                <span class='title__No'><h3>No</h3></span>";
print "                <span class='title__date'><h3>日期時間</h3></span>";
print "                <span class='title__content'><h3>內容</h3></span>";
print "                <span class='title__move'><h3>動作</h3></span>";
print "            </div> ";
print "</div>";
print "</body>";
print "</html>";














