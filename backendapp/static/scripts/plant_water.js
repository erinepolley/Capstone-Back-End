document.querySelector(".water-button").addEventListener("click", (evt) => {
    if (evt.target.id.startsWith("water")) {
        const name = evt.target.id.split("--")[1]
        alert(`Are you sure you want to water ${name}?`)
        // message.innerText = `Are you sure you want to water ${name}?`
        // infoDialog.show()
    }
})