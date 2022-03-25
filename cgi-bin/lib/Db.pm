package Db;

use strict;
use DBI;

my $host = "localhost:3307";         # 主機位址
my $driver = "mysql";           # 執行資料庫類型
my $database = "myperl";        # 資料庫
# 執行程式的句子
my $dsn = "DBI:$driver:database=$database:$host";  
my $userid = "root";            # 資料庫username
my $password = "";        # 資料庫密碼

# 連接資料庫
my $dbh = DBI->connect($dsn,$userid,$password ) or die $DBI::errstr;
my $sth = $dbh->prepare("SELECT * FROM Websites");   # 待處理SQL句子q
$sth->execute();    # 執行SQL

# repeat output data
while ( my @row = $sth->fetchrow_array() )
{
       print join('\t', @row)."\n";
}

sub getContent{

}



$sth->finish();
$dbh->disconnect();


1;