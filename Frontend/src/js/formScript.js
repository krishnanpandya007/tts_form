document.getElementById("hero-button").addEventListener("click", function() {
    document.getElementById("myModal").style.display = "block";
    document.body.classList.add("modal-open");
});

document.getElementsByClassName("close")[0].addEventListener("click", function() {
    document.getElementById("myModal").style.display = "none";
    document.body.classList.remove("modal-open");
});

function disableSubmit() {
    document.getElementById("hero-button").disabled = true;
}

function activateButton(checkbox) {
    var button = document.getElementById('hero-button');
    if (checkbox.checked) {
        button.disabled = false;
    } else {
        button.disabled = true;
    }
}

function activateButton(checkbox) {
    var button = document.getElementById('hero-button');

    if (checkbox.checked) {
        button.disabled = false;
        button.style.pointerEvents = "auto";
    } else {
        button.disabled = true;
        button.style.pointerEvents = "none";
        alert('Please agree to the terms and conditions.');
    }
}