#!"C:\xampp\perl\bin\perl.exe"

### 使用module、中文處理
use utf8;
use Encode;
use strict;
use CGI;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');

my $cgi = CGI->new();


print $cgi->header('text/html');
print $cgi->start_html('Extract the text'),
print $cgi->h1({-style=>'color:red;background-color:#eee;'},'Extract CGI'),
print $cgi->start_form(
    -name   => 'main_form',
    -action => './cgi-bin/txt_upload.pl' ,
    -method => 'GET' ,
    -enctype => &CGI::MULTIPART
    );
print 'Upload your text File:',
print $cgi->filefield(
    -name => 'file',
    -accept => '.txt'
    ),
print $cgi->submit(-value=>'Submit'),
print $cgi->end_form;
print $cgi->end_html;









