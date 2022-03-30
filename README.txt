使用 Perl CGI 實現上傳 txt 檔，並從上傳的檔案中 Parse 出指定資料，存入資料庫

概述

(完成)1. 請提供上傳介面，限制僅能上傳 txt (OK)
(進行)
	0000 upload txt && save to dir(暫停) 、 parse txt data (OK)
	2. 由上傳的 txt 中， parse 出有 "[maillog]" 關鍵字的資料列，{}
    	若該列格式為：[maillog][日期時間] 內容，

	
	0328 parsedata (OK) 、 insert db(OK) 、 parsedata save to db (OK)
	將資料切為日期時間、內容存到資料表中供查詢
       ex. [maillog][2021-11-23 11:00:00] cheryl login.

	0329 show data front (OK) 、 sort data(by db or backend??) (OK)
	(進行)3. 資料列表、預設列出所有資料，依照日期時間降冪排序
	
	0329 keyword&date search&show (OK)
	4. 列表提供關鍵字查詢與日期查詢，依照使用者輸入的關鍵字+日期去查詢、列出符合的資料

	0329 edit data (OK)、 delete data (OK)
	5. 列表每列資料提供內容的編輯以及刪除資料列功能

	0000 AJAX。(待辦)
	6. 查詢、新增、編輯、刪除資料後，僅 refresh 列表，不進行整頁重整

額外:
	(ok)
	找出資料夾中所有檔案
	()
	把所有檔案parse 且找出有maillog的部分
	將有maillog的部分存入資料庫
	編輯或刪除按鈕按下時 要能更動檔案的內容
