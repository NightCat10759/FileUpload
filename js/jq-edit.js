$(document).ready(function() {

    
    $(".contents__but__edit").click(function(){
        let ID = this.value;
        let editContent = document.querySelector(`#editContent${ID}`).value;
        //alert("ID:" + ID);
        alert("content:" + editContent);

        $.ajax({
                type: 'POST',
                url: './cgi-bin/editFile.pl',
                datatype : "json",
                data: { 'edit': ID ,
                        'content': editContent},
                success: function(res) {
                    alert("EDIT SUCCESSFUL! " + res.edit_ID)
                    alert("ADDED content: " + res.editContent)

                    $(".search__but").get(0).click();
                },
                error: function(e) {
                    alert("EDIT FAILED " + e)
                }
        });

    });

    $(".contents__but__dele").click(function(){
        let ID = this.value;
        //alert("ID:" + ID);

        $.ajax({
                type: 'POST',
                url: './cgi-bin/editFile.pl',
                datatype : "json",
                data: { 'delete': ID },
                success: function(res) {
                    //alert("DELETE SUCCESSFUL! " + res.delete_ID)

                    $(".search__but").get(0).click();
                },
                error: function(e) {
                    alert("DELETE FAILED " + e)
                }
        });

    });


});