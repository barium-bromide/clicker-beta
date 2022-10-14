let apple = 0;

document.getElementById("IncreaseApple").onclick = function IncreaseApple(){
    apple +=1;
    document.getElementById("countPara").innerHTML = apple;
}

Price = [15, 100, 1000, 2000, 5000, 10000, 30000, 50000, 100000, 200000]

document.getElementById("buy0").onclick = function(){
    if (apple < 15){
        return
    }
    else{
            apple -=Price[0];
            document.getElementById("countPara").innerHTML = apple;
        }
    }

    document.getElementById("buy1").onclick = function(){
        if (apple < 100){
            return
        }
        else{
                apple -=Price[1];
                document.getElementById("countPara").innerHTML = apple;
            }
        }

    document.getElementById("buy2").onclick = function(){
        if (apple < 1000){
            return
        }
        else{
                apple -=Price[2];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy3").onclick = function(){
        if (apple < 2000){
            return
        }
        else{
                apple -=Price[3];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy4").onclick = function(){
        if (apple < 5000){
            return
        }
        else{
                apple -=Price[4];
                document.getElementById("countPara").innerHTML = apple;
            }
        }    
    document.getElementById("buy5").onclick = function(){
        if (apple < 10000){
            return
        }
        else{
                apple -=Price[5];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy6").onclick = function(){
        if (apple < 30000){
            return
        }
        else{
                apple -=Price[6];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy7").onclick = function(){
        if (apple < 50000){
            return
        }
        else{
                apple -=Price[7];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy8").onclick = function(){
        if (apple < 100000){
            return
        }
        else{
                apple -=Price[8];
                document.getElementById("countPara").innerHTML = apple;
            }
        }
    document.getElementById("buy9").onclick = function(){
        if (apple < 200000){
            return
        }
        else{
                apple -=Price[9];
                document.getElementById("countPara").innerHTML = apple;
            }
        }