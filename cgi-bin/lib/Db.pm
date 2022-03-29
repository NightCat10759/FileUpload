package Db;

use strict;
use DBI;

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
sub showDb{
       my ($self) = @_;
       my $dbh = $self->{db};
       if ( ! $dbh->ping ) {
              $dbh = $dbh->clone() or die "cannot connect to db";
       }
       my $sth = $dbh->prepare("SELECT * FROM file;");   # 待處理SQL句子q
       $sth->execute();    # 執行SQL

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

sub searchDb{
       # 輸入搜尋的內容
       my ($self,$words) = @_;

}      


1;