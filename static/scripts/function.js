//All comments send to database
//apple = 0
//claim_apple = 0
let lastClick = Date.now();

let appleButton = document.getElementById("IncreaseApple");

appleButton.onclick = function IncreaseApple() {
    let now = Date.now();
    if ((now - lastClick) / 100 < 0.05) {
        alert("You are clicking too fast");
        return;
    }
    lastClick = Date.now();
    //apple += 1

    appleButton.classList.add("large");

    setTimeout(() => {
        appleButton.classList.remove("large");
    }, 500);

    document.getElementById("countPara").innerHTML = apple;
    console.log("Clicked");
};

//Price = [15, 100, 1000, 2000, 5000, 10000, 30000, 50000, 100000, 200000] => Price get expensive if buy more *1.10 everytime
//Player_Inventory = [] => after player buy stuff from shop they got
for (let i = 0; i < 10; i++) {
    document.getElementById("buy" + i).onclick = function () {
        if (apple < Price[i]) {
            return;
        } else {
            //apple -=Price[i];
            //Player_Inventory = [Got smtg]
            //Price[*1.10]
            //Change claim_apple by 1, Player must claim or gone, get elemet btn claim to autoclick thingy
            //document.getElementById("countPara").innerHTML = apple;
            console.log("bought item" + i);
        }
    };
}

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
