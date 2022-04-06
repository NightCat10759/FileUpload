$(document).ready(function() {

    $(".search__but").click(function(){
        var keyword = document.querySelector("#keyword").value;
        var date = document.querySelector(".date__input").value;
        alert("keyword:" + keyword);
        alert("date:" + date);
        $.ajax({
                type: 'GET',
                url: './cgi-bin/showFile.cgi',
                data: { 'keyword': keyword,
                        'date': date},
                success: function(res) {
                    alert("This is your content: " + res.content);
                    alert("This is your date: " + res.date);
                    alert("This is your id: " + res.id);
                    addElement( res.content, res.date, res.id );
                },
                error: function(e) {
                    alert("did not work" + e);
                }
        });

    });

    function addElement(content , date , id) {
        // 把後端資料顯示在前端
        alert('更新')               

        var el = document.querySelector('.contents');
        el.innerHTML = `
        <div class='container'>
            <form class='content__form' action='./cgi-bin/editFile.pl'method='GET' enctype='multipart/form-data'>
                <span class='contents__No'><h3> ${id} </h3></span>
                <span class='contents__date'><h3> ${date} </h3></span>
                <span class='contents__content'>

                <input name='editContent' value= "${content}" />
                </span>
                <span class='contents__move'>               
                    <button  class='contents__but__edit' name='edit'  value=${id}>修改</button>
                    <button  class='contents__but__dele' name='delete' value=${id}>刪除</button>
                </span>
            </form>
        </div>
        `;
        alert("ok")
                        
        $('.contents').load('.container').fadeIn('slow'); // 載入新內容,url地址與該地址下的選擇器之間要有空格,表示該url下的#container
    
    }

});