const slidePage = document.querySelector(".slidepage");
const firstNextBtn = document.querySelector(".nextBtn");
const prevBtnSec = document.querySelector(".prev1");
const nextBtnSec = document.querySelector(".next1");
const prevBtnThird = document.querySelector(".prev2");
const nextBtnThird = document.querySelector(".next2");
const prevBtnFourth = document.querySelector(".prev3");
const submit = document.querySelector(".submit");
const progressText = document.querySelectorAll(".step p");
const progressCheck = document.querySelectorAll(".step .check");
const bullet = document.querySelectorAll(".step .bullet");
let max = 4;
let current = 1;


firstNextBtn.addEventListener("click", function() {
    slidePage.style.marginLeft = "-25%";
    slidePage.style.transition = "0.2s ease-in";
    bullet[current - 1].classList.add("active");
    progressCheck[current - 1].classList.add("active");
    current += 1;
})

nextBtnSec.addEventListener("click", function() {
    slidePage.style.marginLeft = "-50%";
})

nextBtnThird.addEventListener("click", function() {
    slidePage.style.marginLeft = "-75%";
})

prevBtnSec.addEventListener("click", function() {
    slidePage.style.marginLeft = "0%";
})

prevBtnThird.addEventListener("click", function() {
    slidePage.style.marginLeft = "-25%";
})
prevBtnFourth.addEventListener("click", function() {
    slidePage.style.marginLeft = "-50%";
})