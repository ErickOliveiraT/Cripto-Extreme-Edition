function decrypt() {
	var tesseractKey = document.getElementById("TesseractPass").value
	var qnt = document.getElementById("filesCont").value

	eel.decrypt(tesseractKey,qnt)(function(ret){console.log(ret)})
}