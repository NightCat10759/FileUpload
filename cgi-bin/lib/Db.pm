package Db;


use DBI;
###   使用module、中文處理   ###
use utf8;
use Encode;
use strict;
use CGI;
use lib './cgi-bin/lib';
use Db;
binmode(STDIN,':encoding(utf8)');
binmode(STDOUT,':encoding(utf8)');
binmode(STDERR,':encoding(utf8)');

sub new{
       my $class = shift;
       my $host = "localhost:3307";         # 主機位址
       my $driver = "mysql";           # 執行資料庫類型
       my $database = "files";        # 資料庫
       # 執行程式的句子
       my $dsn = "DBI:$driver:database=$database:$host";  
       my $userid = "root";            # 資料庫username
       my $password = "";        # 資料庫密碼

       # 連接資料庫
       my $dbh = DBI->connect($dsn,$userid,$password ) or die $DBI::errstr;

       my $self = {
              db => $dbh,
       };
       bless $self,$class;
       return $self;
}


sub getDb{    
       my ($self) = @_;
       return $self->{db};
}

sub showDbs{
       my ($self) = @_;
       my $dbh = $self->{db};
       if ( ! $dbh->ping ) {
              $dbh = $dbh->clone() or die "cannot connect to db";
       }
       my $sth = $dbh->prepare("SELECT * FROM file ORDER BY date DESC;");   # 待處理SQL句子q
       $sth->execute();    # 執行SQL

       return ($dbh, $sth);  
}

sub showDb{
       # 輸入關鍵字跟日期查詢資料
       my ($self,$date,$keyword) = @_;
       my $dbh = $self->{db};
       if ( ! $dbh->ping ) {
              $dbh = $dbh->clone() or die "cannot connect to db";
       }
       my $sth = $dbh->prepare("SELECT * FROM file where date = ? OR content = ? ORDER BY date DESC;");   # 待處理SQL句子q
       $sth->execute($date,$keyword);    # 執行SQL

       return ($dbh, $sth);  
}

sub insertDb{
       my ($self,$datetime,$content,$filename) = @_;
       my $dbh = $self->{db};
       my $sth = $dbh->prepare("Insert into file
                                (date,content,filename)
                                values(?,?,?);");   # 待處理SQL句子q
       $sth->execute($datetime,$content,$filename);    # 執行SQL
       $sth->finish();
       $dbh->disconnect();
}

sub editDb{
       my ($self,$content, $id) = @_;
       my $dbh = $self->{db};
       my $sth = $dbh->prepare("UPDATE file SET content = ?
                                where id = ? ;");   # 待處理SQL句子q
       $sth->execute($content,$id);    # 執行SQL
       $sth->finish();
       $dbh->disconnect();  
}

sub deleteDb{
       my ($self, $id) = @_;
       my $dbh = $self->{db};
       my $sth = $dbh->prepare("delete from file where id = ?");   # 待處理SQL句子q
       $sth->execute($id);    # 執行SQL
       $sth->finish();
       $dbh->disconnect();
}


1;