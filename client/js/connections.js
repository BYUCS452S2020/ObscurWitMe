$(document).ready(function() {
  $("connections").ready(function() {
    getPotentialConnections();
  });
});



function goToUserPage(userid) {
  console.log(userid);

  window.location.href="user.html#" + userid;
}

function createClickableList(list) {
  $ul = $("<ul></ul>");
  $("#connections").append($ul);

  $(list).each(function(i) {
    var $li = $("<li></li>").text(list[i].username);
    $li.click(function(e) {
      e.preventDefault();
      goToUserPage(list[i].userid);
    });
    $($ul).append($li);
  });
}

function getPotentialConnections() {
  console.log("getting connections");
  
  // // TODO: does this exist?
  // var url = "http://localhost:8000/getconnections";
  // var userid = sessionStorage.getItem("userid");
  // var data = {
  //   userid: userid
  // }

  // $.ajax({
  //   url: url,
  //   data: JSON.stringify(data),
  //   success: function(data, status) {
  //     createClickableList(data["connections"]);
  //   },
  //   error: function(error) {
  //     console.warn(error);
  //   }
  // });

  list = []
  list.push({ "username": "Mike", "userid": "1" });
  list.push({ "username": "Sarah", "userid": "2" });
  list.push({ "username": "Joey", "userid": "3" });
  list.push({ "username": "Jessica", "userid": "4" });

  console.log(list)
  createClickableList(list);
}