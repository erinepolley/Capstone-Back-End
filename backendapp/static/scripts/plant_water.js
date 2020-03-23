console.log("Hullo!")

document.querySelector(".thirsty-plant").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})

document.querySelector(".delete-button").addEventListener("click", () => {
    alert("Are you sure you want to delete this plant?")
})