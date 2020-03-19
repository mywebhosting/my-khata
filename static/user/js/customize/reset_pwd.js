$(document).ready(function(){
	$(".show_hide_newpwd").on("click", function(){
		if($("#newpassword").get(0).type == "password"){
			$("#newpassword").prop("type", "text");
			$(".show_hide_newpwd").html(`<i class="fa fa-eye-slash" aria-hidden="true"></i>`);
		}
		else{
			$("#newpassword").prop("type", "password");
			$(".show_hide_newpwd").html(`<i class="fa fa-eye" aria-hidden="true"></i>`);
		}
		
	});

	$(".show_hide_confpwd").on("click", function(){
		if($("#confpassword").get(0).type == "password"){
			$("#confpassword").prop("type", "text");
			$(".show_hide_confpwd").html(`<i class="fa fa-eye-slash" aria-hidden="true"></i>`);
		}
		else{
			$("#confpassword").prop("type", "password");
			$(".show_hide_confpwd").html(`<i class="fa fa-eye" aria-hidden="true"></i>`);
		}
		
	});

	$(".resetpwd").on("click", function(){
		let newpassword = $("#newpassword").val();
		let confpassword = $("#confpassword").val();

		let obj = new resetpwd(newpassword,confpassword);
		obj.check();
		return false;
	});
});

class resetpwd{
	constructor(newpassword,confpassword){
		this.newpassword = newpassword;
		this.confpassword = confpassword;
		this.host = location.protocol+`//`+window.location.host;

		// this.check();
	}

	check(){
		if(this.newpassword == ""){
			this.show_message({"status_code":0, "msg":"New password not be blank"})
			return false;
		}

		if(this.newpassword !== this.confpassword){
			this.show_message({"status_code":0, "msg":"Confirm password not match"})
			return false;
		}else{
			this.show_message({"status_code":2, "msg":"Verifying..."})

			let obj = new PasswordHash();
			let make_hash = obj.HasPassword(this.newpassword);
			this.sendpassword(make_hash);
			return false;
		}
	}

	sendpassword(hash_pwd){
		let key = $('input[name=csrfmiddlewaretoken]').val();
		$.ajax({
			url: this.host+"/my-khata/reset-password/",
			method: "POST",
			data: {
				"csrfmiddlewaretoken": key,
				"password": hash_pwd
			},
			success: function(r){
				if(r === "1"){
					console.log("success");
					new resetpwd().show_message({"status_code":3, "msg":"Password reset. Please login again and continue"})
				}
			}
		});
		// console.log($.cookie(hash_pwd));
	}

	show_message(msg){
		if(msg.status_code==0){
			$(".message").text(msg.msg);
			$(".message").show();
			$(".message").removeClass('green').removeClass('blue').addClass('red');
		}
		if(msg.status_code==2){
			$(".message").text(msg.msg);
			$(".message").show();
			$(".message").removeClass('green').removeClass('blue').addClass('yellow');
		}
		if(msg.status_code==3){
			$(".message").text(msg.msg);
			$(".message").show();
			$(".message").removeClass('green').removeClass('blue').addClass('green');

			let url = this.host+`/login/`;
			setTimeout(function(){window.location.href=url;},2000);
		}
	}
}