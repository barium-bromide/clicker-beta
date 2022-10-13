let count = 0;

document.getElementById("IncreaseApple").onclick = function(){
    count +=1;
    document.getElementById("countLabel").innerHTML = count;
}