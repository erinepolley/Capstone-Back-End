console.log("Hullo!")

document.querySelector(".thirsty-plant").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`${name} has been watered!`)
    }
})