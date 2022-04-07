$(document).ready(function() {

    $(".search__but").click(function(){
        let keyword = document.querySelector("#keyword").value;
        let date = document.querySelector(".date__input").value;
        //alert("keyword:" + keyword);
        //alert("date:" + date);

        $.ajax({
                type: 'POST',
                url: './cgi-bin/showFile.cgi',
                datatype : "json",
                data: { 'keyword': keyword,
                        'date': date},
                success: function(res) {
                    //alert("DATA loading SUCCESS!")
                    for (let index = 0; index < res.length; index++) {
//                        alert("Data length: " + res.length)
//                        alert("This is your content: " + res[index].content);
//                        alert("This is your date: " + res[index].date);
//                        alert("This is your id: " + res[index].id);
    
                        addElement( res[index].content, res[index].date, res[index].id );
                    }
                    addScript()
                },
                error: function(e) {
                    alert("DATA loading Failed")
//                    alert("Data length: " + e.length)
//                    alert("This is your content: " + e.content);
//                    alert("This is your date: " + e.date);
//                    alert("This is your id: " + e.id);
                }
        });

    });


    function addElement( content , date , id) {
        // 把後端資料顯示在前端
        //alert('更新')               

        var el = document.querySelector('.contents');
        $(el).append ( `
        <div class='container'>
            <div class='content__form'>
                <span class='contents__No'><h3> ${id} </h3></span>
                <span class='contents__date'><h3> ${date} </h3></span>
                <span class='contents__content'>
                    <input type='text' id = 'editContent${id}' name = 'editContent' value= "${content}" />
                </span>
                <span class='contents__move'>               
                    <button class='contents__but__edit' name='edit'  value= ${id}>修改</button>
                    <button class='contents__but__dele' name='delete' value= ${id}>刪除</button>
                </span>
            </div>
        </div>
        `)

     //   alert("ok")
                        
    }

    function addScript() {
        var el = document.querySelector('.contents');
        $(el).append (`
                <script src='./js/jq-edit.js'></script>
            `)
    }

});