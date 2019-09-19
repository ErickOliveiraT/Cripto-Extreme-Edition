function encrypt() {
	var tesseractKey = document.getElementById("TesseractPass").value
	var msg = document.getElementById("message").value
	//var fileInput = document.getElementById('file-input')
	//var filename = fileInput.files[0].name

	eel.encrypt(tesseractKey,msg)(function(ret){console.log(ret)})
}