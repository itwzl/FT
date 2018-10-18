n=1;
m=0.3;
p=1;
index=3;
function t1(){

    n-=0.01;
    var i = document.getElementById('i2');
    i.style.opacity=n;
    ss1=setTimeout("t1()",60);
    if(n<=0.5){
        index+=1;
        t2();
        clearTimeout(ss1)
    }

}
function t2(){
    n+=0.01;
    var j = document.getElementById('i1');
    j.style.opacity=n;
    j.style.zIndex=index;
    ss2=setTimeout("t2()",60);
    if(n>=1){
        clearTimeout(ss2);
        index+=1;
        t3()
    }
}
function t3(){
    var i = document.getElementById("i1");
    n-=0.01;
    i.style.opacity=n;
    i.style.zIndex=index;
    ss3=setTimeout('t3()',60);
    if(n<=0.5){
        clearTimeout(ss3);
        index+=1;
        t4()
    }
}
function t4(){
    var i = document.getElementById("i2");
    n+=0.01;
    i.style.opacity=n;
    i.style.zIndex=index;
    ss4=setTimeout("t4()",60);
    if(n>=1){
        clearTimeout(ss4);
        t1()
    }
}