$(document).ready(function() {
  $("#add").click(function() {
    var interestid = window.location.hash.substring(1);
    var userid = sessionStorage.getItem("userid");

    var url = "http://localhost:8000/addinterest"
    var data = {
      interestid: interestid,
      userid: userid
    }

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        alert("New Interest Added Successfully!");
      },
      error: function(error) {
        console.warn(error);
        alert("Could not add interest :(");
      }
    });

    // window.location.href = "interests.html";
  });

  $("info").ready(getInterest());
});

function getInterest() {
  var interestid = window.location.hash.substring(1);

  var url = "http://localhost:8000/getinterest";
  var data = {
    interestid: interestid
  };

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, status) {
      console.log(data);
      $("#header").append(data["name"]);

      var categories = data["categories"].join(", ");

      var $p_categories = $("<p></p>").text("Categories: " + categories);
      var $p_description = $("<p></p>").text("Description: " + data["description"]);
      var $img = $(`<img src=${data["imageURL"]} alt="Image of Activity" style="width:500px;height:500px">`);

      $("#info").append($p_categories);
      $("#info").append($p_description);
      $("#info").append($img);
    }, 
    error: function(error) {
      console.warn(error);
    }
  });  
}