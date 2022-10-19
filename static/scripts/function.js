let apple = 0;

document.getElementById("IncreaseApple").onclick = function IncreaseApple(){
    apple +=1;
    document.getElementById("countPara").innerHTML = apple;
}

Price = [15, 100, 1000, 2000, 5000, 10000, 30000, 50000, 100000, 200000]
Inventory = []
function Invcount(){
    for(i = 0;i<10; i++){
        Inventory.push(0)
    }
}

document.getElementById("buy0").onclick = function(){
    if (apple < Price[0]){
        return
    }
    else{
            apple -=Price[0];
            document.getElementById("countPara").innerHTML = apple;
        }
    }

    document.getElementById("buy1").onclick = function(){
        if (apple < Price[1]){
            return
        }
        else{
                apple -=Price[1];
                document.getElementById("countPara").innerHTML = apple;
            }
        }

    document.getElementById("buy2").onclick = function(){
        if (apple < Price[2]){
            return
        }
        else{
                apple -=Price[2];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy3").onclick = function(){
        if (apple < Price[3]){
            return
        }
        else{
                apple -=Price[3];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy4").onclick = function(){
        if (apple < Price[4]){
            return
        }
        else{
                apple -=Price[4];
                document.getElementById("countPara").innerHTML = apple;
            }
        }    
    document.getElementById("buy5").onclick = function(){
        if (apple < Price[5]){
            return
        }
        else{
                apple -=Price[5];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy6").onclick = function(){
        if (apple < Price[6]){
            return
        }
        else{
                apple -=Price[6];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy7").onclick = function(){
        if (apple < Price[7]){
            return
        }
        else{
                apple -=Price[7];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy8").onclick = function(){
        if (apple < Price[8]){
            return
        }
        else{
                apple -=Price[8];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy9").onclick = function(){
        if (apple < Price[9]){
            return
        }
        else{
                apple -=Price[9];
                document.getElementById("countPara").innerHTML = apple;
            }
        }