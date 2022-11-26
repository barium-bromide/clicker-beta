const shop = {
    workers: 15,
    farm: 100,
    factory: 1000,
    store: 2000,
    trucks: 5000,
    ship: 10000,
    aeroplane: 30000,
    tradeCenter: 50000,
    computer: 100000,
    rocketShip: 200000,
};

let apple = 0;
let claim_apple = 0;
let lastClick = Date.now();
let appleButton = document.getElementById("IncreaseApple");
let username = localStorage.getItem("username");

if (!username) {
    // TODO: handle unlogined users
}

document.getElementById("username").innerText = `Username: ${username}`;

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
    console.count("Clicked");
};

let inventory = {};

function buy(name) {
    socket.emit("buy", name);
}

setInterval(() => {
    socket.emit("add", username, claim_apple);
    claim_apple = 0;

    console.time("Claimed");
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
