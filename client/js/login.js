$(document).ready(function() {
  $("button").click(function() {
    var email = document.getElementById("email").value;
    var passwd = document.getElementById("passwd").value;
  
    var url = "http://127.0.0.1:8000/login";
    var data = {
      email: email,
      password: passwd
    }

    console.log(data);

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        sessionStorage.setItem("userid", data["userid"]);
        window.location.href="main.html";
      }, 
      error: function(error) {
        console.log("error occurred: ${error}");
      }
    });
  });
});