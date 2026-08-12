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

const contactForm = document.querySelector(".contact form");

if (contactForm) {
    contactForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(contactForm);

        const data = {
            name: formData.get("name"),
            email: formData.get("email"),
            commission_type: formData.get("commission-type"),
            game_system: formData.get("game-system"),
            project: formData.get("project"),
            number_of_miniatures: formData.get("number-of-miniatures"),
            deadline: formData.get("deadline")
        };

        try {
            const response = await fetch("/api/contact/submit-commission/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (response.ok) {
                alert("Commission request sent successfully!");
                contactForm.reset();
            } else {
                alert(`Something went wrong: ${result.error}`);
            }

        } catch (error) {
            console.error("Error submitting commission:", error);
            alert("Unable to submit your commission request. Please try again.");
        }
    });
}