$(document).ready(function(){
	/*if ($("button[type='submit']").val() == "login"){
		alert('asdsa');
	}*/

	$(".login").on("click", function(){
		let user_id = $("input[name='email']").val();
		let password = $("input[name='password']").val();
		// let flag = login_status.check_user_id(user_id=user_id);
		// let flag = 0;
		// console.log({user_id,password});
		//let login_status = new check_login({user_id, password}); //success = 1, Fail = 0
		let login_status = new check_login_credential();
		/*flag = login_status.check_user_id(user_id=user_id);
		if(flag==1)
			flag = login_status.check_password(password);*/
		login_status.show_message({'status_code':3, 'status':"Verifying..."});
		setTimeout(function(){login_status.check_login(user_id=user_id,password=password)},1000);
		/*console.log(flag);
		if(flag.status_code === 0){
			$(".message").text(flag.status);
			$(".message").show();
			$(".message").removeClass('green').addClass('red');
		}
		else if(flag.status_code === 1){
			$(".message").text(flag.status);
			$(".message").show();
			$(".message").removeClass('red').addClass('green');
		}*/
		return false;
	});

	$(".show_hide_pwd").on("click", function(){
		console.log($("input[name=password]").get(0).type);
		if($("input[name=password]").get(0).type == "password"){
			$("input[name=password]").prop("type", "text");
			$(".show_hide_pwd").html(`<i class="fa fa-eye-slash" aria-hidden="true"></i>`);
		}
		else{
			$("input[name=password]").prop("type", "password");
			$(".show_hide_pwd").html(`<i class="fa fa-eye" aria-hidden="true"></i>`);
		}
		
	});
});

class check_login_credential{
	/*constructor({user_id, password}){
		console.log(user_id);
	}*/
	/*check_user_id(user_id=''){
		console.log(user_id);
		return 1;
	}
	check_password(password=''){
		console.log(password);
		let key = $('input[name=csrfmiddlewaretoken]').val();

		$.ajax({
			url:"http://127.0.0.1:8000/my-khata/check-login/",
			method:"POST",
			data:{
				'csrfmiddlewaretoken': key,
				'fname': "test",
			},
			success: function(e){
				console.log(e);
			}
		});

		return 2;
	}*/
	constructor(){
		/*this.host = location.protocol+`//`+window.location.host+`/my-khata/dash-board/`;*/
		this.host = location.protocol+`//`+window.location.host;
	}
	check_login(user_id='',password=''){
		if(user_id == ""){
			new check_login_credential().show_message({'status_code':0, 'status':"User Id required"});
			return false;
		}
		if(password == ""){
			new check_login_credential().show_message({'status_code':0, 'status':"Password required"});
			return false;
		}
		
		let has_obj = new PasswordHash();
		let has_password = has_obj.HasPassword(password);
		let key = $('input[name=csrfmiddlewaretoken]').val();
		$.ajax({
			url:"http://127.0.0.1:8000/my-khata/check-login/",
			method:"POST",
			data:{
				'csrfmiddlewaretoken': key,
				"user_id": user_id,
				'password': has_password,
			},
			async: false,
			success: function(e){
				// console.log(e);
				if(e === "Success"){
					// return {'status_code':1, 'status':e};
					new check_login_credential().show_message({'status_code':1, 'status':e});
				}
				else if(e === "resetpassword"){
					new check_login_credential().show_message({'status_code':4, 'status':"You need to reset your password"});
				}
				else{
					// return {'status_code':0, 'status':e};
					new check_login_credential().show_message({'status_code':0, 'status':e});
				}
			},
			error: function(e){
				// return {'status_code':0, 'status':"Server error"};
				new check_login_credential().show_message({'status_code':0, 'status':e});
			}
		});
	}

	show_message(resp){
		console.log(resp);
		if(resp.status_code === 0){
			$(".message").text(resp.status);
			$(".message").show();
			$(".message").removeClass('green').removeClass('blue').addClass('red');
		}
		else if(resp.status_code === 1){
			$(".message").text(resp.status);
			$(".message").show();
			$(".message").removeClass('red').removeClass('blue').addClass('green');
			$(".lock_pwd").html(`<i class="fa fa-unlock" aria-hidden="true"></i>`);

			let url = this.host+`/my-khata/dashboard/`;
			// console.log(url);
			setTimeout(function(){window.location.href=url;},2000);
		}
		else if(resp.status_code === 3){
			$(".message").text(resp.status);
			$(".message").show();
			$(".message").removeClass('red').removeClass('green').addClass('blue');
		}
		else if(resp.status_code === 4){
			$(".message").text(resp.status);
			$(".message").show();
			$(".message").removeClass('red').removeClass('green').addClass('blue');

			let url = this.host+`/my-khata/reset-password/`;
			// document.cookie = "user_id="+$("input[name='email']").val();
			// $.cookie("example", "foo");
			setTimeout(function(){window.location.href=url;},2000);
		}
	}
	

	
}