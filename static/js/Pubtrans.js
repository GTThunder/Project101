var registration_fee = 140;
var private_lesson = 1792;
var nonprivate_lesson = 2787;
var toyota_wish = 109888;
var toyota_vios = 89988;
var hdsd = 19900;

function showInput(){
    if (document.getElementById("private").checked){
        if (document.getElementById("wish").checked){
            omv = 19960;
            total = toyota_wish += registration_fee += private_lesson += omv;
        }
        else if (document.getElementById("vios").checked){
            omv = 15416;
            total = toyota_vios += registration_fee += private_lesson += omv;
        }
        else{
            omv = 7977;
            total = hdsd += registration_fee += private_lesson += omv;
        }
    }
    else{
        if (document.getElementById("wish").checked){
            omv = 19960;
             total = toyota_wish += registration_fee += nonprivate_lesson += omv;
        }
        else if(document.getElementById("vios").checked){
            omv = 15416;
             total = toyota_vios += registration_fee += nonprivate_lesson += omv;
        }
        else{
            omv = 7977;
             total = hdsd += registration_fee += nonprivate_lesson += omv;
        }

    }
    document.getElementById("displayresults").innerHTML = "Total Cost: $" + total;


}

