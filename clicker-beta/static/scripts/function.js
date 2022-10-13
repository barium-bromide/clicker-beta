let apple = 0;

document.getElementById("IncreaseApple").onclick = function(){
    apple +=1;
    document.getElementById("countLabel").innerHTML = apple;
}