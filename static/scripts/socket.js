const socket = io();

socket.on("connect", () => {
    socket.emit("init", username);
});

socket.on("apple", epal => {
    apple = epal;
    document.getElementById("countPara").innerHTML = apple;
});

socket.on("inv", inv => {
    inventory = inv;
});

socket.on("shop", shop => {
    let main = document.getElementById("main");

    while (main.firstChild) main.remove(main.lastChild);

    for (let [i, [itemName, price]] of Object.entries(shop).entries()) {
        let container = document.createElement("div");
        container.className = "slot";

        let nameELement = document.createElement("p");
        let displayName = itemName.replace(/([A-Z])/g, " $1");
        nameELement.innerText =
            displayName[0].toUpperCase() + displayName.slice(1).toLowerCase();

        let buyBtn = document.createElement("button");
        buyBtn.className = "Buy";
        buyBtn.innerText = "Buy";
        buyBtn.onclick = `buy(${itemName})`;

        let priceElement = document.createElement("p");
        priceElement.className = "price";
        priceElement.id = `price${i}`;
        priceElement.innerText = `Price: ${price * 1.1 ** inventory[itemName]}`;

        let invElement = document.createElement("p");
        invElement.className = "inv";
        invElement.id = `inv${i}`;
        invElement.innerText = inventory[itemName];

        container.appendChild(nameELement);
        container.appendChild(buyBtn);
        container.appendChild(priceElement);
        container.appendChild(invElement);

        main.appendChild(container);
    }
});
