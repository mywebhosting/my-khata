const loader = new Loader();
const myalert = new MycustomAlert();

$(document).ready(function(){
	// $(".email_otp_loader").show();
});

class CustomerValidation{
	constructor(){
		let resp = this.getinput();
	}

	getinput = () => {
		const first_name = $("[name='first_name']").val();
		const middel_name = $("[name='second_name']").val();
		const last_name = $("[name='last_name']").val();
		const per_address = $("[name='permanent_address']").val();
		const alt_address = $("[name='altanative_address']").val();
		const phone_no = $("[name='phone_no']").val();
		const email_id = $("[name='email_id']").val();

		if(first_name == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("First name mantetory", "red");
			return false;
		}
		if(last_name == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("Last name mantetory", "red");
			return false;
		}
		if(per_address == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("Permanent address mantetory", "red");
			return false;
		}
		if(alt_address == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("Altanative address mantetory", "red");
			return false;
		}
		if(phone_no == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("Phone no mantetory", "red");
			return false;
		}
		if(email_id == ""){
			loader.Hide(className="create_customer_loader");
			myalert.ShowAlert("Email id mantetory", "red");
			return false;
		}


		// loader.Hide(className="create_customer_loader");
	}	
}

$(".create_customer").on("click", function(){
	loader.Show(className="create_customer_loader");
	setTimeout( () => {
		const customervalidation = new CustomerValidation();
	},2000);
});