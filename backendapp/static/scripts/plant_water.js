console.log("Hullo!")

document.querySelector("body").addEventListener("click", (evt) => {
  // alert("The water button was just clicked.")
  if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})

// let mainNav = document.getElementById('menu-items');
// let hamburgerContainer = document.getElementById('hamburger-container');

// hamburgerContainer.addEventListener('click', () => {
//     mainNav.classList.toggle('active');
// });

const responsiveNav = () => {
    let menu = document.getElementById("menu-items");
    if (menu.className === "topnav") {
      menu.className += " responsive";
    } else {
      menu.className = "topnav";
    }
  }

