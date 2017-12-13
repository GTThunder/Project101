/**
 **   Filename     : eguide.js
 **   Version      : 1.00
 **   Last Updated : 20 october 2000
 **
 **   Logic/Details: utility functions for eguide section
 **
Points to observe
-----------------
Modifications / Bug Fixes
-------------------------
 **/
/*
  Global variable definition
*/
var debugOn=1;  //debug flag
/**
 ** Function name : setService(servicelist)
 ** Logic         : writes the selected value of listbox object
 **                 textbox
 ** Input         : listbox object
 **
 **/
function setService(servicelist)
{
  var opt_idx;
  var opt_val;

  opt_idx=servicelist.selectedIndex;
  opt_val=servicelist.options[opt_idx].value;
  if(opt_idx) {
    document.frmservice.service.value = opt_val;
    //alert(opt_val);
  }
  else
      document.frmservice.service.value = "";
}

function setBsCode(bscodelist)
{
  var opt_idx;
  var opt_val;

  opt_idx=bscodelist.selectedIndex;
  opt_val=bscodelist.options[opt_idx].value;
  if(opt_idx) {
    document.formbscode.bscode.value = opt_val;
    //alert(opt_val);
  }
  else
      document.frmservice.bscode.value = "";

}


function isFilled(result_page)
{
	var msg = "";
	var valid = 0;
	//frmservice
	if(result_page=='frmservice') {

		if(document.forms[result_page].service.value=="") {

			msg+="\nPlease enter a bus Service Number";
			document.forms[result_page].service.focus();
			alert(msg);
			return false;

		}
	}

	//formroad
	if(result_page=='formroad') {

		if(document.forms[result_page].road_idx.value=="") {

			msg+="\nPlease enter or click on the first letter of the road name";
			document.forms[result_page].road_idx.focus();
			alert(msg);
			return false;
		}
	}


	//formmrt
	if(result_page=='formmrt') {

		if(document.forms[result_page].mrtcode_start.value=="index")
		{
			msg+="\nPlease select the Boarding Station";
			document.forms[result_page].mrtcode_start.focus();
			valid = 1;
		}
		if(document.forms[result_page].mrtcode_end.value=="index")
		{
			msg+="\nPlease select the Alighting Station";
			document.forms[result_page].mrtcode_end.focus();
			valid = 1;
		}
		if (valid == 1)
		{
			alert(msg);
			return false;
		}
	}

	//frminterchange
	if(result_page=='frminterchange') {

		if(document.forms[result_page].interchange.value=="-") {

			msg+="\nPlease select an Interchange";
			document.forms[result_page].interchange.focus();
			alert(msg);
			return false;
		}
	}

	//formbscode
	if(result_page=='formbscode') {

		if(document.forms[result_page].bscode.value=="") {

			msg+="\nPlease enter the 5-digit bus stop code";
			document.forms[result_page].bscode.focus();
			alert(msg);
			return false;
		}
	}

	return true;
}

function countCheckboxes(val, dir)
{
	if (dir == 1) chkcal = "calc1[]"; //for direction 1 variable
	else chkcal = "calc2[]"; //for direction 2

	var chk_arr =  document.getElementsByName(chkcal);
	var chklength = chk_arr.length;
	//alert(chklength);
	var chkval_arr = [];
	count = 0;
	for (i=0; i<chklength; i++)
	{
		if (chk_arr[i].checked==true) //alert("Checkbox at index "+i+" is checked!")
		{
			count ++;
			chkval_arr[i] = chk_arr[i].value;
		}
	}

	if (count > 2)
	{
	 	alert('You cannot check more than two boxes for fare calculation.');
		for (i=0; i<chklength; i++)
		{
			 if (chkval_arr[i] == val)
				chk_arr[i].checked = false;
		}
	}
}

function verifyRoute(dir)
{
	var chkcal;
	if (dir == 1) chkcal = "calc1[]"; //for direction 1 variable
	else chkcal = "calc2[]"; //for direction 2

	var chk_arr =  document.getElementsByName(chkcal);
	var chklength = chk_arr.length;

	count = 0;
	for (i=0; i<chklength; i++)
	{
		if (chk_arr[i].checked==true)
			count ++;
	}
	if (count < 2)
	{
		alert("Please check two boxes for fare calculation.");
		return false;
	}
	else return true;
}

