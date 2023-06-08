// document.getElementById("openModal").addEventListener("click", function() {
//     document.getElementById("myModal").style.display = "block";
//     document.body.classList.add("modal-open");
// });

// document.getElementsByClassName("close")[0].addEventListener("click", function() {
//     document.getElementById("myModal").style.display = "none";
//     document.body.classList.remove("modal-open");
// });


// $('.menu-toggle').click(function() {
//     $('.menu-items').toggleClass('open');
// });

// function disableSubmit() {
//     document.getElementById("hero-button").disabled = true;

//     document.onclick(alert("Please accept your fate"))
// }

// function activateButton(element) {

//     if (element.checked) {
//         document.getElementById("hero-button").disabled = false;
//     } else {
//         document.getElementById("hero-button").disabled = true;
//     }

// }

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



// import {
//     MediaPermissionsError,
//     MediaPermissionsErrorType,
//     requestAudioPermissions,
//     requestVideoPermissions,
//     requestMediaPermissions
// } from 'mic-check';

// // Requesting AUDIO permission only:
// requestAudioPermissions()
//     .then(() => {})
//     .catch((err: MediaPermissionsError) => {});

// // another way to request AUDIO only...
// requestMediaPermissions({ audio: true, video: false })
//     .then(() => {})
//     .catch((err: MediaPermissionsError) => {});

// // Requesting VIDEO permission only:
// requestVideoPermissions()
//     .then(() => {})
//     .catch((err: MediaPermissionsError) => {});

// // another way to request VIDEO only...
// requestMediaPermissions({ audio: false, video: true })
//     .then(() => {})
//     .catch((err: MediaPermissionsError) => {});