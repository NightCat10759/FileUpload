$(document).ready(function() {
    $("#upload__but").click(function() { //ID 為 submitExample 的按鈕被點擊時
        
//        e.preventDefault();  // 阻止鏈接跳轉
//        var url = this.href;  // 保存點擊的地址

        $.ajax({
            type: "POST", //傳送方式
            url: "./cgi-bin/upload.cgi", //傳送目的地
            dataType: "multipart/form-data", //資料格式
            data: { //傳送資料
                uploadfile: $(".upload__input").val(), //表單欄位 ID nickname
            },
        /*    success: function(data) {
                if (data.nickname) { //如果後端回傳 json 資料有 nickname
                    $("#demo")[0].reset(); //重設 ID 為 demo 的 form (表單)
                    $("#result").html('<font color="#007500">您的暱稱為「<font color="#0000ff">' + data.nickname + '</font>」，性別為「<font color="#0000ff">' + data.gender + '</font>」！</font>');
                } else { //否則讀取後端回傳 json 資料 errorMsg 顯示錯誤訊息
                    $("#demo")[0].reset(); //重設 ID 為 demo 的 form (表單)
                    $("#result").html('<font color="#ff0000">' + data.errorMsg + '</font>');
                }
            },
            error: function(jqXHR) {
                $("#demo")[0].reset(); //重設 ID 為 demo 的 form (表單)
                $("#result").html('<font color="#ff0000">發生錯誤：' + jqXHR.status + '</font>');
            }*/
        })
//        $('.container').remove();                          
//        $('.contents').load(url + ' .container').fadeIn('slow'); // 載入新內容,url地址與該地址下的選擇器之間要有空格,表示該url下的#container
    })        
});