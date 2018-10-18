/*此处为账号验证*/
$(document).ready(function () {
    $("#lg_count").blur(function () {
        // alert("sdas")
        lgcount = document.getElementById("lg_count").value;
        $.ajax({
            url: "/ftapp/getlgcount/",
            method: "post",
            dataType: "json",
            data: {"lgcount": lgcount},
            success: function (response) {
                var status = response['status']
                if (status == "0") {
                    countVerify("block","您输入的密码格式不正确")
                }
                if (status=="2"){
                    countVerify("block","您输入的账号不存在")
                }
            }
        });

    })
});
function countVerify(display,inner) {
    document.getElementById('login_grid_error').style.display =display;
    document.getElementById("login_grid_p").innerHTML = inner;
}
$(document).ready(function () {
    $("#lg_count").focus(function () {
        countVerify("none","")
    })
});
//密码验证如下
$(document).ready(function () {
   $("#lg_password").blur(function () {
       lgpassword=document.getElementById("lg_password").value;

       $.ajax({
           url:'/ftapp/getlgpassword/',
           method:"post",
           data:{"lgpassword":lgpassword},
           dataType:"json",
           success:function (response) {
               var status = response['status'];
               if(status=="2"){
                   countVerify("block","您输入的密码不能为空")
               }
               if(status=="0"){
                   countVerify("block","您输入的密码格式不正确")
               }
               if(status=="1"){
                   countVerify("none","")
               }
           }

       })
   })

});
$(document).ready(function () {
   $("#lg_password").focus(function () {
       countVerify("none","")
   })
});
/*点击登录的验证*/
$(document).ready(function () {
    $("#lg_button").click(function () {
        lgcount1=document.getElementById('lg_count').value;
        lgpassword1=document.getElementById('lg_password').value;
        $.ajax({
            url:"/ftapp/loginverify/",
            method:"post",
            dataType:"json",
            data:{"lgcount":lgcount1,"lgpassword":lgpassword1},
            success:function (response) {
                var status = response['status'];
                if(status=="1"){
                    document.getElementById("success").style.display="block";

                    nickname=response['nickname'];
                    setTimeout("skip()",2000)

                }else {
                    countVerify("block","您输入的账号或密码不正确")
                }

            }
        })
    })
});

function skip() {
    document.getElementById("login_fog").style.opacity="0";
    document.getElementById("login_grid").style.display="none";
    document.getElementById("success").style.display="none";
    document.getElementById("login_pickname").innerHTML=nickname;
    document.getElementById("button_login").value="注销";
    document.getElementById('button_register').style.display="none"
}