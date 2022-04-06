$(document).ready(function() {

    
    $(".contents__but__edit").click(function(){
        let ID = this.value;
        let editContent = document.querySelector(`editContent${ID}`);
        alert("ID:" + ID);
        alert("content:" + `editContent${ID}`);

        $.ajax({
                type: 'GET',
                url: './cgi-bin/editFile.pl',
                datatype : "json",
                data: { 'ID': ID ,
                        'content': editContent},
                success: function(res) {
                    alert("EDIT SUCCESSFUL! " + res.edit_id)
                },
                error: function(e) {
                    alert("EDIT FAILED " + e)
                }
        });

    });

    $(".contents__but__dele").click(function(){
        let ID = this.value;
        alert("ID:" + ID);

        $.ajax({
                type: 'GET',
                url: './cgi-bin/editFile.pl',
                datatype : "json",
                data: { 'delete': ID },
                success: function(res) {
                    alert("DELETE SUCCESSFUL! " + res.delete_ID)
                },
                error: function(e) {
                    alert("DELETE FAILED " + e)
                }
        });

    });
});