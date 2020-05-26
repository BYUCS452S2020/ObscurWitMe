$(document).ready(function() {
  $("button").click(function() {
    var firstName = document.getElementById("firstName").value;
    var lastName = document.getElementById("lastName").value;
    var email = document.getElementById("email").value;
    var age = document.getElementById("age").value;
    var location = document.getElementById("location").value;
    var passwd = document.getElementById("passwd").value;
  
    var url = "http://localhost:8000/createuser";
    var data = {
      first: firstName,
      last: lastName,
      email: email,
      age: age,
      location: location,
      password: passwd
    }

    console.log(data);

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        console.log("success!");

        url = "http://localhost:8000/getuser";
        var new_data = { email: email };
        
        $.ajax({
          url: url,
          type: "POST",
          data: JSON.stringify(new_data),
          success: function(data, status) {
            console.log(data)
            sessionStorage.setItem("email", data["email"]);
            sessionStorage.setItem("userid", data["userid"]);
            window.location.href="main.html";
          }, 
          error: function(error) {
            console.log(error);
          }
        });
      }, 
      error: function(error) {
        console.log("error occurred: ${error}");
      }
    });
  });
});