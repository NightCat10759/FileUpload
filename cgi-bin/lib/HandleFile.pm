package HandleFile;
### File用於讀取已儲存的檔案 ###
# 建構子:
# new File(file)
# 方法:
# setFile(file)
# getFILE()
# writeFILE(words)
# readFILE()

### 使用module、中文處理
use utf8;
use Encode;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


# 等於constructor
sub new{
    $class = shift;
    $self = {
        file => shift,
    };
    bless $self,$class;
    return $self;
}

sub setFile{
    my ($self, $new_file) = @_;
    $self->{file} = $new_file if defined ($new_file);
    return $self->{file};
}

sub getFile{
    my ($self) = @_;
    return $self->{file};
}

sub writeFile{
    my ($self, $new_words) = @_;
    $words = $new_words if defined ($new_words);
    #寫入
    open(FILE, '>:encoding(utf8)' ,$self->{file}) or die "$!";
    print FILE $words;
    close(FILE);
    return FILE;
}

sub readFile{
    # 讀原檔
    my ($self) = @_;
    if ($self->{file}) {
        open(FILE, $self->{file}) or die "$!";
        $str = "";
        while( defined( $line = <FILE> )){
            Encode::_utf8_on($line);
             print ("$line\n");
        }
        close(FILE);
    } else {
        print "No such FILE";
    }
}

sub parseFile
{
    my ($content);
    # [maillog][2021-11-23 11:00:00](內容)
    # 用]把字串拆開
      @pairs = split(']',$content);
      print "$content";
    # 得到[maillog] [2021-11-23 11:00:00] (內容)
    # 把date跟內容跟檔案名存到資料庫
}




1;