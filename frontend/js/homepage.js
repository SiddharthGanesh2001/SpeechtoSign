
window.onresize = function(){
	if(window.outerWidth<1000 || window.outerHeight < 800){
		window.resizeTo(1000,800);
	}
	else{
		if(window.outerWidth>1000 || window.outerHeight > 800){
			window.resizeTo(1000,800);
		}
	}
}
// window.onresize = function(){
// 	if(window.outerWidth>1200 || window.outerHeight > 800){
// 		window.resizeTo(1200,800);
// 	}
// }

function loadingScreen(){
    var ele = document.getElementById("loading");
    ele.style.display = 'none';
    // ele.classList += "hidden";
}

const mnav = document.getElementsByClassName("mobile-nav");
const togglenav = document.getElementsByClassName("toggle-nav");
const marvel = document.getElementsByClassName("marvel");


function myFunction(x) {
	for (var i = 0; i < mnav.length; i++) {
		mnav[i].classList.toggle("open");
	}
	x.classList.toggle("change");
}

function togglemenu(){
	let nav = document.querySelector('.nav');
	let toggle = document.querySelector('.toggle');
	nav.classList.toggle('active');
	toggle.classList.toggle('active');

}

function MicOn(){
	document.getElementById("speak-on-but").style.display="none";
	document.getElementById("speak-off-but").style.display="inline";
	eel.getTextfromSpeech()
}

eel.expose(MicOff);
function MicOff(){
	document.getElementById("speak-on-but").style.display="inline";
	document.getElementById("speak-off-but").style.display="none";
}

eel.expose(displayText)
function displayText(text){
	console.log(text);
	document.getElementById("textarea").innerHTML=text;
}

eel.expose(displayImg)
function displayImg(alttext,imglink){
	var ele = document.createElement("img");
	ele.src = imglink;
	ele.alt = alttext;
	ele.setAttribute('height','100%');
	ele.setAttribute('width','100%');
	document.getElementById("image-display").appendChild(ele);
}

eel.expose(deleteImg)
function deleteImg(){
	var ele = document .getElementById("image-display");
	ele.removeChild(ele.lastChild);
}