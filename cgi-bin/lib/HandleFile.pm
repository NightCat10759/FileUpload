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
use strict;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');


# 等於constructor
sub new{
    my $class = shift;
    my $self = {
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
    my $words = $new_words if defined ($new_words);
    #寫入
    open(FILE, '>:encoding(utf8)' ,$self->{file}) or die "$!";
    print FILE $words;
    close(FILE);
}

sub readFile{
    # 讀原檔
    my ($self) = @_;
    if ($self->{file}) {
        open(FILE, $self->{file}) or die "$!";
        my $str = "";
        while( defined( my $line = <FILE> )){
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
    my ($self, $content) = @_;
    # [maillog][2021-11-23 11:00:00](內容)
    # 用]把字串拆開
      my ( $key,  $datetime,  $contents) = split(']', $content, 3);
      $datetime =~ s/\[/ /;
      return ($datetime , $contents);
    # 得到[maillog] [2021-11-23 11:00:00] (內容)
}



1;