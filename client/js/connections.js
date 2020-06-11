$(document).ready(function() {
  sessionStorage.setItem("conn_startat", "0");

  $("connections").ready(function() {
    getPotentialConnections();
  });
});



function goToUserPage(userid) {
  console.log(userid);

  window.location.href="user.html#" + userid;
}

function createClickableList(list) {
  var $ul = $("<ul></ul>");
  $("#connections").append($ul);

  $(list).each(function(i) {
    var $li = $("<li></li>").text(`${list[i].firstname} ${list[i].lastname}`);
    $li.click(function(e) {
      e.preventDefault();
      goToUserPage(list[i].userid);
    });
    $($ul).append($li);
  });
}

function getPotentialConnections() {
  console.log("getting connections");
  
  var url = "http://localhost:8000/getconnections";
  var userid = sessionStorage.getItem("userid");
  var startat = parseInt(sessionStorage.getItem("conn_startat"));
   
  var data = {
    userid: userid,
    startat: startat,
    count: 10
  }

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, status) {
      console.log(data);
      createClickableList(data["users"]);

      if ($("#connections ul li").length < data["totalcount"]) {
        sessionStorage.setItem("conn_startat", (startat + 10).toString());
      }
      // TODO: more button
    },
    error: function(error) {
      console.warn(error);
    }
  });
}