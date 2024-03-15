
setTimeout (function(){
document.getElementById('submitButton').disabled = null;
},30000);

var countdownNum = 30;
incTimer();

function incTimer(){
setTimeout (function(){
    if(countdownNum != 0){
    countdownNum--;
    document.getElementById('timeLeft').innerHTML = 'Time left: ' + countdownNum + ' seconds';
    incTimer();
    } else {
    document.getElementById('timeLeft').innerHTML = 'Ready!';
    }
},1000);
}


