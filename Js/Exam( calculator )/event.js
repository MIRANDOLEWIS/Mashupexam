function ans(){

const firnum = parseInt(document.getElementById('firnum').value)

const secnum = parseInt(document.getElementById('secnum').value)

const sele = document.getElementById('sele').value

var adds,subs,muls,divis;


adds = function(){
	if (sele == "add"){
		document.getElementById("answer").value = firnum + secnum
	}

}

// function call
adds()

subs = function(){
	if (sele === "sub"){
		document.getElementById("answer").value = firnum - secnum
	}

}

// function call
subs()

muls = function(){
	if (sele === "mul"){
		document.getElementById("answer").value = firnum * secnum
	}

}

// function call
muls()

divis = function(){
	if (sele === "divi"){
		document.getElementById("answer").value = firnum / secnum
	}

}

// function call
divis()

} 