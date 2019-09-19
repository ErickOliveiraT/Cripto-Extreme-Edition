function generateKeys() {
	var tesseractKey = document.getElementById("TesseractPass").value
	var r1k = document.getElementById("keyR1").value
	var r1s = document.getElementById("showingR1").value
	var r2k = document.getElementById("keyR2").value
	var r2s = document.getElementById("showingR2").value
	var r3k = document.getElementById("keyR3").value
	var r3s = document.getElementById("showingR3").value

	eel.generateKeys(tesseractKey,r1k,r1s,r2k,r2s,r3k,r3s)(function(ret){console.log(ret)})
}