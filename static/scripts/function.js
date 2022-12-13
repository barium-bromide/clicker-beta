//for jy to refer everyone password and username
//https://applefarming-qeag.onrender.com/username_and_pass_api

let apple = 0;
let claim_apple = 0;
let lastClick = Date.now();
const appleButton = document.getElementById("IncreaseApple");
const username =
    document.getElementById("real-username").innerText ||
    localStorage.getItem("username");
const inventory = {};

if (!username) {
    window.location.href= "https://applefarming-qeag.onrender.com/login";
    // window.alert("get rickroll for not login you fucking retard")
    // window.alert("We’re no strangers to love")
    // window.alert("You know the rules and so do I")
    // window.alert("A full commitment’s what I’m thinking of")
    // window.alert("You wouldn’t get this from any other guy")
    // window.alert("I just wanna tell you how I’m feeling")
    // window.alert("Gotta make you understand")
    // window.alert("Never gonna give you up")
    // window.alert(" Never gonna let you down")
    // window.alert(" Never gonna run around and desert you")
    // window.alert(" Never gonna make you cry")
    // window.alert(" Never gonna say goodbye")
    // window.alert(" Never gonna tell a lie and hurt you")
    // window.alert(" We’ve known each other for so long")
    // window.alert(" Your heart’s been aching but you’re too shy to say it")
    // window.alert(" Inside we both know what’s been going on")
    // window.alert(" We know the game and we’re gonna play it")
    // window.alert(" And if you ask me how I’m feeling")
    // window.alert(" Don’t tell me you’re too blind to see")
    // window.alert(" Never gonna give you up")
    // window.alert(" Never gonna let you down")
    // window.alert(" Never gonna run around and desert you")
    // window.alert(" Never gonna make you cry")
    // window.alert(" Never gonna say goodbye")
    // window.alert(" Never gonna tell a lie and hurt you")
    // window.alert("go to login screen or else i will grab your ip address and kill you")
}

localStorage.setItem("username", username);

document.getElementById("username").innerText = `Username: ${username}`;

document.querySelector("#settings").onclick = () => {
    const settingMenu = document.querySelector("#setting-menu");
    if (settingMenu.classList.contains("hide")) {
        settingMenu.classList.remove("hide");
    } else {
        settingMenu.classList.add("hide");
    }
};

appleButton.onclick = () => {
    let now = Date.now();

    if ((now - lastClick) / 100 < 0.05) {
        alert("You are clicking too fast");
        return;
    }

    lastClick = Date.now();
    apple++;
    claim_apple++;

    appleButton.classList.add("large");

    setTimeout(() => {
        appleButton.classList.remove("large");
    }, 100);

    document.getElementById("countPara").innerHTML = apple.toFixed(2);
    console.count("click");
};

appleButton.addEventListener("keydown", e => {
    e.preventDefault();
    if (e.keyCode === 13) {
        return;
    }
});

setInterval(() => {
    socket.emit("add", username, claim_apple);
    console.log(`Claimed ${claim_apple} apple(s)`);

    claim_apple = 0;
}, 10_000);

//workers = increase mouse power by one(click one time + mouse power)
//farm = increase claim before leaving by one
//factory = increase claim before leaving by 1%
//store = increase claim before leaving by 2%
//trucks = increase mouse power by 5%
//ship =  increase claim before leaving by 5%
//aeroplane = increase claim before leaving by 10%
//trade centre = increase mouse power by 10%
//computer = increase claim before leaving by 15%
//rocket ship = increase claim before leaving by 20%
