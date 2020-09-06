/**
 * Sumbit the form of checkbox
 * @param {Event} e 
 */
function markTodoFinish(e){
    //Geting todo id from its checkbox
    var targetForm = e.target.dataset.id

    //Geting the form of todo
    var form = document.getElementById(`${targetForm}`)
    form.submit()
}


//When the DOM be ready 
document.addEventListener("DOMContentLoaded" , (e)=>{
    //Get all checkbox in Todo
    var checkboxs = document.querySelectorAll("input[type=checkbox]")

    for (const checkbox of checkboxs) {
        checkbox.addEventListener("change", markTodoFinish)
    }

})


