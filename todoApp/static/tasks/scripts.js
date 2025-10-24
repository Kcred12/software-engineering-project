const modal = document.getElementById("taskModal");
const completeButton = document.getElementById("completeButton");
const editButton = document.getElementById("editButton");
const deleteButton = document.getElementById("deleteButton");

function openModal(el) {

    document.getElementById("modalTitle").textContent = el.dataset.title;
    document.getElementById("modalDescription").textContent = el.dataset.description;
    document.getElementById("modalDue").textContent = el.dataset.due;

    completeButton.href = el.dataset.complete_url;
    editButton.href = el.dataset.edit_url;
    deleteButton.href = el.dataset.delete_url;

    modal.style.display = "block";
}

function closeModal() {
    document.getElementById("taskModal").style.display = "none";
}

window.onclick = function (event) {
    const modal = document.getElementById("taskModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
}