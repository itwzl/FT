m=0
num=1
function test1(){

setTimeout('alternate(1,2)',2000)
setTimeout('alternate(2,3)',6000)
setTimeout('alternate(3,1)',10000)
setTimeout("test1()",12000)
}
function alternate(num1,num2){
	
	document.getElementById("i"+num1).style.left=String(m)+"px"
	document.getElementById("i"+num2).style.left=String(m+document.getElementById("i1").width)+"px"

	m-=10
	var s1=setTimeout("alternate("+num1+","+num2+")",10)
	if(m<-(document.getElementById("i1").width)){
		clearTimeout(s1)
		m=0					
	}
}