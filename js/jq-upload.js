$(document).ready(function() {

    $(".upload__but").click(function(){
        let formData = new FormData($(".upload__form")[0]);
    //    alert("keyword:" + keyword);
    //    alert("date:" + date);
        $.ajax({
                type: 'POST',
                contentType: false,
                async: false,
                cache: false,
                processData: false,
                url: './cgi-bin/upload.cgi',
                datatype : "json",
                data: formData,
                success: function(res) {
                    alert("FILE loading SUCCESSFUL! ")
                },
                error: function(e) {
                    alert("FILE loading Failed")
//                    alert("Data length: " + e.length)
//                    alert("This is your content: " + e.content);
//                    alert("This is your date: " + e.date);
//                    alert("This is your id: " + e.id);
                }
        });

    });



});