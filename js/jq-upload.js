$(document).ready(function() {


    $(".upload__but").click(function(){
        alert("okay")
        let form = new FormData();
        let file_data = $('.upload__input').prop('files')[0];
        alert(file_data);
        form.append("file", file_data);



        $.ajax({
                type: 'POST',
                async: false,
                cache: false,
                contentType: false,
                processData: false,
                url: './cgi-bin/upload.cgi',
                data: form,
                success: function(res) {
                    alert("FILE loading SUCCESSFUL! :" + res.filename)
                    
                },
                error: function(e) {
                    alert("FILE loading Failed:" + e)
//                    alert("Data length: " + e.length)
//                    alert("This is your content: " + e.content);
//                    alert("This is your date: " + e.date);
//                    alert("This is your id: " + e.id);
                }
        });

    });



});