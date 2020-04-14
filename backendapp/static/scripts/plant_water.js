console.log("Hullo!")

document.querySelector("body").addEventListener("click", (evt) => {
  if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("plant-guide-button");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
btn.onclick = () => {
  event.preventDefault()
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = () => {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

