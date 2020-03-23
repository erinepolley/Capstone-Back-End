console.log("Hullo!")

document.querySelector("form").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})

// document.querySelector("form").addEventListener("click", (event) => {
//     console.log("is this getting hit?")
//     if (event.target.id.startsWith("delete-button")) {
//         confirm(`Are you sure you want to delete this plant?`)
//     }
// })