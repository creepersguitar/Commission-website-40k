document.addEventListener("DOMContentLoaded", () => {

    console.log("Small Scale Studios loaded");

});


const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-toggle-label");

navToggle.addEventListener("click", () => {
    navMenu.classList.toggle("active");
});