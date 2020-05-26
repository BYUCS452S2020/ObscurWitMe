$(document).ready(function() {
  $("button").click(function() {
    var name = document.getElementById("name").value;
    var category = document.getElementById("category").value;
    var description = document.getElementById("description").value;
    var thumbnail = document.getElementById("thumbnail").value;
    
    var url = "http://localhost:8000/createinterest";
    var data = {
      name: name,
      description: description
    }

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        console.log(data)
        
        window.location.href="interests.html";
      }, 
      error: function(error) {
        console.log(error);
      }
    });
  });
});