function sendotp(subjecttype){
    var email=document.getElementById('id_email').value;
    if(!email)
    {
        alert('Fill in all details before sending OTP');
        return;
    }
    javascript:incTimer();
    $.ajax({
        url : "/yelagiritravels/triggerotp", // the endpoint
        type : "GET", // http method
        data : { email : email,
                subjecttype : subjecttype
                 }, // data sent with the get request
        // handle a successful response
        success : function(json) {
            console.log("success"); // another sanity check
        },
        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};