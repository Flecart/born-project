document.addEventListener("DOMContentLoaded", function() {
    const contributionMap = document.querySelector(".contribution-map");
    const dateDisplay = document.getElementById("date-display");

    const startDate = new Date('2002-01-01');
    const endDate = new Date('2002-12-31');

    function date_to_index(date) {
        return Math.floor((date - startDate) / (1000 * 60 * 60 * 24));
    }

    const allClicked = [];
    let currentDate = new Date(startDate);

    while (currentDate <= endDate) {
        const box = document.createElement("div");
        box.className = `contribution-box`;
        
        // Assigning a random level for demonstration purposes
        const level = Math.floor(0);
        if (level > 0) {
            box.classList.add(`level-${level}`);
        }

        box.dataset.date = currentDate.toISOString().split('T')[0];

        box.addEventListener("click", function() {
            if (box.classList.contains("level-4")) {
                box.classList.remove("level-4");
                box.classList.add("level-0");
                allClicked.splice(allClicked.indexOf(box.dataset.date), 1);
                return;
            }
            box.classList.remove("level-0");
            box.classList.add("level-4");
            allClicked.push(box.dataset.date);
            console.log(allClicked);
        });

        contributionMap.appendChild(box);

        // Move to the next day
        currentDate.setDate(currentDate.getDate() + 1);
    }

});
