    //document.getElementById('btn').addEventListener("click",
      // function (e) {
      //     alert("ss")
      // });
    document.getElementById('clicklist').onclick=function (){
        $.ajax({
            type:"get",
            url:"/ajaxjson",
            dataType:"json",
            success:function (data,status) {
                console.log(data);
            }
        })
    }