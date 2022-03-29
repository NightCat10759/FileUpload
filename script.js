

function nohidden(){
    let editInput = document.getElementById("editInput");
    editInput.removeAttribute("hidden")
}

function close(){
    let editInput = document.getElementsByClassName("editInput");
    editInput.setAttribute("hidden",true)
}