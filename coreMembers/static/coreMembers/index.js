function deleteOperation(event) {
    const id = Number(event.target.parentElement.id.slice(1));
    const deletePage = document.getElementById('delete');
    const deleteForm = document.getElementById('delete-form');
    deleteForm.setAttribute("action", 'delete/' + id + '/');
    deletePage.style.display = "block";
}


function cancleDelete() {
    const deletePage = document.getElementById('delete');
    deletePage.style.display = "none";
}
