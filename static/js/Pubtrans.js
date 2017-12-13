var registration_fee = 140
var private_lesson = 1792
var nonprivate_lesson = 2787
var toyota_wish = 109888
var toyota_vios = 89988
var hdsd = 19900

function showInput(){
    if (document.getElementById("private").checked = true){
        if (document.getElementById("wish")){
            omv = 19960
            total = toyota_wish + registration_fee + private_lesson + omv
        }
        else if (document.getElementById("vios")){
            omv = 15416
            total = toyota_wish + registration_fee + private_lesson + omv
        }
        else if (document.getElementById("hdsd")){
            omv = 7977
            total = toyota_wish + registration_fee + private_lesson + omv
        }
    }
    else if (document.getElementById("nonprivate").checked = true){
        if (document.getElementById("wish")){
            omv = 19960
            total = toyota_wish + registration_fee + nonprivate_lesson + omv
        }
        else if(document.getElementById("vios")){
            omv = 15416
            total = toyota_wish + registration_fee + nonprivate_lesson + omv
        }
        else if (document.getElementById("hdsd")){
            omv = 7977
            total = toyota_wish + registration_fee + nonprivate_lesson + omv
        }

    }
    document.getElementById("displayresults").innerHTML = total;

}

