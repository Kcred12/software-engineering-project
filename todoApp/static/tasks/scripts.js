const modal = document.getElementById("taskModal");
function openModal(el) {
    document.getElementById("modalTitle").textContent = el.dataset.title;
    document.getElementById("modalDescription").textContent = el.dataset.description;
    document.getElementById("modalDue").textContent = el.dataset.dueDate || "No due date";
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