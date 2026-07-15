document.addEventListener("DOMContentLoaded", () => {

    console.log("Small Scale Studios loaded");

    const navToggle = document.querySelector(".nav-toggle");
    const navMenu = document.querySelector(".nav-menu");

    console.log(navToggle);
    console.log(navMenu);

    navToggle.addEventListener("click", () => {
        navMenu.classList.toggle("active");
    });

});