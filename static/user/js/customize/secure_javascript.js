$(document).ready(function(){
	// document.oncontextmenu = new Function("return false");
	let my_alert = new MycustomAlert();
	$(document).bind("contextmenu",function(e){
		my_alert.ShowAlert("Right button disable", 'red');
      return false;
   });
});

class MycustomAlert{
	constructor(){
		console.log("Welcome to my khata");
	}

	ShowAlert(message, type){
		$("#custom_alert").show();
		let message_structure = `<div class="custom-notification-div">
						            <div class="alert-success-myalert">
						                <span class="alert-message `+type+`">`+message+`</span>
						            </div>
						        </div>`;
		$("#custom_alert").html(message_structure);
		setTimeout(function(){ $("#custom_alert").hide(500) }, 4000);
	}
};


class PasswordHash{
	constructor(){
		this.password_key = "SDMYKHATA";
	}

	HasPassword(password){
		let modify_password = btoa(password+this.password_key);
		return modify_password;
	}
};

class Loader{
	constructor(){
		$(".loader").hide();
	}

	Show(className="loader"){
		$("."+className).fadeIn(500);
	}

	Hide(className="loader"){
		$("."+className).fadeOut(500);
	}
}