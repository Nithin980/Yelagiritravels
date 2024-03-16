
//setTimeout (function(){
//document.getElementById('btnsendotp').disabled = null;
//},30000);

var countdownNum = 30;
//incTimer();

function incTimer(){
setTimeout (function(){
    if(countdownNum != 0){
    countdownNum--;
    document.getElementById('timeLeft').innerHTML = 'Time left: ' + countdownNum + ' seconds';
    incTimer();document.getElementById('btnsendotp').disabled = true;

    } else {
    document.getElementById('timeLeft').innerHTML = 'Ready!';
    document.getElementById('btnsendotp').disabled = null;
    countdownNum=30;
    }
},1000);
}


