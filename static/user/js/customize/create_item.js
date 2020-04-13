const loader = new Loader();
const myalert = new MycustomAlert();

class ItemValidation{
	constructor(){
		$(".product_image").hide();
		this.host = location.protocol+`//`+window.location.host;
	}

	CheckName(){
		let product_name = $(".product_name").val();
		if(product_name == ""){
			myalert.ShowAlert("Product name mantetory", "red");
			$(".product_name").focus();
			loader.Hide();
			return false;
		}
		return true;
	}

	CheckDetails(){
		let qty_type = $(".qty_type").val();
		let qty = $(".qty").val();
		let qty_price = $(".price").val();
		if(qty_type == ""){
			myalert.ShowAlert("Product qty type mantetory", "red");
			$(".qty_type").focus();
			loader.Hide();
			return false;
		}
		if(qty == ""){
			myalert.ShowAlert("Product qty mantetory", "red");
			$(".qty").focus();
			loader.Hide();
			return false;
		}
		if(qty_price == ""){
			myalert.ShowAlert("Product price mantetory", "red");
			$(".price").focus();
			loader.Hide();
			return false;
		}

		return true;
	}

	ShowImage(input){
		if(input.files && input.files[0]){
			var render = new FileReader();

			render.onload = function (e){
				$(".product_image").show();
				$('.product_image').attr('src', e.target.result);
			}
			render.readAsDataURL(input.files[0]);
		}

		/*if (input.files && input.files[0]) {
	        var reader = new FileReader();

	        reader.onload = function (e) {
	        	$(".product_image").show();
	            $('.product_image').attr('src', e.target.result);
	        }

	        reader.readAsDataURL(input.files[0]);
	    }*/
	}

	ReadFileContent(input){
		if(input.files && input.files[0]){
			var render = new FileReader();
			input.filedata = {"files_data": []};
			render.onload = function (e){
				input.filedata.files_data.push({
					"file_name": input.files[0].name,
					"file_type": input.files[0].type,
					"dataurl": e.target.result
				});
			}
			render.readAsDataURL(input.files[0]);
		}
	}

	SendValue(){
		// let image_data = $(".product_image_attach").prop('filedata');
		// image_data.files_data.length
		let product_img_data = "";
		if($(".product_image_attach").prop('filedata') != undefined){
			product_img_data = $(".product_image_attach").prop('filedata').files_data[0];
			/*console.log(product_img_data);
			console.log("Image present");*/
		}
		/*else{
			console.log("No Image");
		}*/

		const data = {
			"csrfmiddlewaretoken": $('input[name=csrfmiddlewaretoken]').val(),
			"product_name": $(".product_name").val(),
			"quantity_type": $(".qty_type").val(),
			"quantity": $(".qty").val(),
			"price": $(".price").val(),
			"product_img_name": product_img_data.file_name,
			"product_img_data": product_img_data.dataurl
		};

		$.ajax({
			url: this.host+"/my-khata/item/create/",
			method: "POST",
			data: data,
			async: false,
			success: function (r){
				console.log(r);
				if(r === "1"){
					myalert.ShowAlert("Product inserted.", "green");
					loader.Hide();
				}
			}
		})
	}
}

const itemvalidate = new ItemValidation();
$(document).ready(function(){
	
});

$(".create-item").on("click", function(){
	// $(".loader").fadeIn(500);
	/*let image_data = $(".product_image_attach").prop('filedata');
	console.log(image_data.files_data.length);*/

	loader.Show();
	setTimeout( () => {
		if(itemvalidate.CheckName() != false){
			if(itemvalidate.CheckDetails() === true){
				// console.log("Send value ready");
				itemvalidate.SendValue();
			}
		}
	},2000);

	return false;
	// itemvalidate.CheckName();
});

$(".product_image_attach").on("change", function(){
	// console.log(this.files);
	itemvalidate.ShowImage(this);
	itemvalidate.ReadFileContent(this);
});