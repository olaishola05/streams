const message = document.getElementById("explore");

function displayMessage(e) {
    e.preventDefault();
    message = Swal.fire({
        icon: "Welcome",
        title: "<h6>Coming Soon...</h6>",
        text: "Try again in few months",
    });
}

message.addEventListener("click", displayMessage);
