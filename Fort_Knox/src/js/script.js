function loginEvent(event){
    let formData = new FormData(event.currentTarget);
    let userInput = Object.fromEntries(formData);

    if (userInput.uname == "admin" && userInput.pwd == "hahatrytoguessthispasswordhydra___;;1492"){
        console.log("you got it");
        window.location.replace("./admin.html")
        // fix it!
        localStorage.setItem("backstage_pass", "yeah_this_one's_allowed");
    }
    else {
        console.log("wrong!");
        alert("Incorrect username or password");
        localStorage.setItem("backstage_pass", "nope");
    }

    event.preventDefault();
}

console.log("---Testing Below---");