let apple = 0;
let claim_apple = 0;
let lastClick = Date.now();
let appleButton = document.getElementById("IncreaseApple");
const username =
    document.getElementById("real-username").innerText ||
    localStorage.getItem("username");
const inventory = {};

localStorage.setItem("username", username);

document.getElementById("username").innerText = `Username: ${username}`;

document.querySelector("#settings").onclick = () => {
    let temp = 0
    temp++
    const settingMenu = document.querySelector("#setting-menu");
    console.log(settingMenu.style);
    if temp % 2 === 1:
        settingMenu.style.opacity = "1"
        settingMenu.style.visibility = "visible"
    else:
        settingMenu.style.opacity = "0"
        settingMenu.style.visibility = "hidden"
}

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

    document.getElementById("countPara").innerHTML = apple;
    console.count("click");
};

appleButton.addEventListener("keydown", e => {
    e.preventDefault();
    if(e.keyCode === 13){
        return;
    }
})

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
