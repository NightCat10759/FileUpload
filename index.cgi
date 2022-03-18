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

print "Content-type: text/html\n\n";
print my $html_template = <<HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css?v=<?=time()?>">
    <title>file_upload</title>
</head>
<body>
    <main>
        <form action="./cgi-bin/txt_upload.pl" method="get" enctype="multipart/form-data">
            <div class="col_upload">
                <span class="upload"><input type="file" accept=".txt" id="file" name="file">上傳檔案</button></span>
                <span class="upload__logo"><button type="submit"><img src="./img/upload.webp" width="20px"></button></span>
            </div>
        </form>
            <div class="col_search">
                <span class="keyword"><button>關鍵字</button></span>
                <span class="date"><button>日期</button></span>
                <span class="search__logo"><button type="submit"><img src="./img/search.png" width="20px"></button></span>
            </div>
            <div class="col_title">
                <span class="title__No"><h3>No</h3></span>
                <span class="title__date"><h3>日期時間</h3></span>
                <span class="title__content"><h3>內容</h3></span>
                <span class="title__move"><h3>動作</h3></span>
            </div>
        <section>

        </section>
    </div>
</body>
</html>
HTML







