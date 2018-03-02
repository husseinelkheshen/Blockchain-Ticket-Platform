console.log("helloooooooo?");

function searchEvents() {
	searchInput =  document.forms["search-form"]["search"].value;
	console.log("Search: " + searchInput);
}

//Prevent auto-submit with enter key
window.onload = function() {
	document.getElementById("search-form").onkeypress = function(e) {
	  var key = e.charCode || e.keyCode || 0;     
	  if (key == 13) {
	    e.preventDefault();
	  }
	}
}



/* ---- Functions for Login/Register User --- */
function loginUser() {
	var valid = true;
	emailInput = document.forms["login-form"]["email-id"].value;
	passwordInput = document.forms["login-form"]["password"].value;
	

	//valid = validLogin(document.forms["login-form"]);

	if(!valid) {
		$("#login-alert").css("visibility", "visible");
	}
	else{
		$("#login-alert").css("visibility", "hidden");
		console.log("do the login dance");
		//if (not a valid login ) {
			//$("#login-alert").css("visibility", "visible");
		//}
	}
}

function registerUser() {
	var valid = true;
	emailInput = document.forms["register-form"]["email-id"].value;
	passwordInput = document.forms["register-form"]["password"].value;
	confirmInput = document.forms["register-form"]["confirm"].value;
	
	if(!validEmail(emailInput)) {
		valid = false;
		$("#register-alert").html("Invalid Email");
	}
	/*
	else if (!validPassword(passwordInput)) {
		valid = false;
		$("#register-alert").html("Invalid Password. Passwords must be between 6 and 64 characters," +
			" contain at least one capital letter and contain at least one number character");
	}*/
	else if (!(passwordInput === confirmInput)) {
		valid = false;
		$("#register-alert").html("Passwords do not match");
	}
	
	/*
	else if(!uniqueid) {
		something about not a unique id
	}
	*/

	//invalid = validLogin(document.forms["login-form"]);

	if(!valid){
		$("#register-alert").css("visibility", "visible");
	}
	else{
		$("#register-alert").css("visibility", "hidden");
		console.log("do the register dance");
		//if(somesort of error ) {
			//$("#register-alert").html("An error has occured");
			// $("#register-alert").css("visibility", "visible");
			//
		//}
	}
}

$('#loginUserButton').click(function() {
	loginUser();
});
$('#registerUserButton').click(function() {
	registerUser();
});

