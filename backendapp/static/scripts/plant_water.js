console.log("Hullo!")

document.querySelector("body").addEventListener("click", (evt) => {
  if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})

