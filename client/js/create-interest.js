$(document).ready(function() {
  $("button").click(function() {
    var name = document.getElementById("name").value;
    var categories = document.getElementById("category").value.split(",").map(function(item) {
      return item.trim();
    });
    var description = document.getElementById("description").value;
    var image = document.getElementById("image").value;
    
    var url = "http://localhost:8000/createinterest";
    var data = {
      name: name,
      categories: categories,
      description: description,
      image: image
    }

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        alert("New Interest Created Successfully!");
        
        var interestid = data["interestid"];
        
        window.location.href="interest.html#" + interestid;
      }, 
      error: function(error) {
        alert("Could not create interest :(");
        console.log(error);
      }
    });
  });
});