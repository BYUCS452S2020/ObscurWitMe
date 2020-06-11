$(document).ready(function() {
  $("button").click(function() {
    var email = document.getElementById("email").value;
    var passwd = document.getElementById("passwd").value;
  
    var url = "http://localhost:8000/login";
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
        if (data["success"]) {
          sessionStorage.setItem("userid", data["userid"]);
          window.location.href="main.html";
        } else {
          alert("Invalid username or password");
        } 
      }, 
      error: function(error) {
        // TODO: invalid password?
        console.log("error while logging in: ${error}");
      }
    });
  });
});