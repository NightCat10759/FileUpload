$(document).ready(function() {


    $(".upload__but").click(function(){

        let file_name = $('.upload__input').val();

        if (file_name == null || file_name == ""){
                
            alert ("請上傳檔案!");
        
        } else {

            alert("okay")

            let form = new FormData($('.upload__form')[0]);
            let file = document.querySelector('.upload__input').files[0];
            form.append("file", file);
            form.append("filename", file_name);

            alert("filename: " + form.get('filename'));
            alert("file: " + form.get('file'));

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
                    
                    $(".search__but").get(0).click();

                },

                error: function(e) {

                    alert("FILE loading Failed:" + e)

                }



            });



        }

    });

});