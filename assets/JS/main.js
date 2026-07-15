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


const filterButtons = document.querySelectorAll(".gallery-filters button");
const galleryCards = document.querySelectorAll(".gallery-card");

filterButtons.forEach(button => {

    button.addEventListener("click", () => {

        const filter = button.dataset.filter;

        galleryCards.forEach(card => {

            if (filter === "all" || card.dataset.category === filter) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }

        });

    });

});