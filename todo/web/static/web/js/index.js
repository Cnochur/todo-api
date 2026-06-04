// Get elements
const form = document.getElementById("task-form");
const titleInput = document.getElementById("title-input");
const descriptionInput = document.getElementById("description-input");
const modalEl = document.getElementById("taskModal");

// Bootstrap modal instance
const modal = new bootstrap.Modal(modalEl);

// CSRF helper (Django)
function getCSRFToken() {
    return document.cookie
        .split("; ")
        .find(row => row.startsWith("csrftoken"))
        ?.split("=")[1];
}

// Auto-focus when modal opens
modalEl.addEventListener("shown.bs.modal", () => {
    titleInput.focus();
});

// Handle form submit
form.addEventListener("submit", function (e) {
    e.preventDefault();

    const title = titleInput.value.trim();
    const description = descriptionInput.value.trim();

    // Basic validation
    if (!title) {
        alert("Title is required");
        return;
    }

    fetch("/tasks/add/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken()
        },
        body: JSON.stringify({
            title: title,
            description: description
        })
    })
    .then(res => {
        if (!res.ok) throw new Error("Failed to create task");
        return res.json();
    })
    .then(data => {
        console.log("Task created:", data);
        modal.hide();
        form.reset();
        location.reload();
    })
    .catch(err => {
        console.error(err);
        alert("Something went wrong");
    });
});