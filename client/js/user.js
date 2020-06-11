$(document).ready(function() {
  $("info").ready(function() {
    getUser();
  });

  $("interests").ready(function() {
    getInterests();
  });
});


function getUser() {
  var userid = window.location.hash.substring(1);
  console.log("userid: " + userid);

  // connect to server

  var url = "http://localhost:8000/getuser";
  var data = {
    userid: userid
  }

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, success) {
      var name = `${data["firstname"]} ${data["lastname"]}`;
      window.name = name;

      var $p_name = $("<p></p>").text(`Name: ${name}`);
      var $p_age = $("<p></p>").text(`Age: ${data["age"]}`);
      var $p_location = $("<p></p>").text(`Age: ${data["location"]}`);

      // $("#info").append($p_name);
      $("#info").append($p_name);
      $("#info").append($p_age);
      $("#info").append($p_location);
    },
    error: function(error) {
      console.warn(error)
    }
  });
}

function goToInterestPage(interestid) {
  console.log(interestid);

  window.location.href="interest.html#" + interestid;
}

function createClickableList(list) {
  var $ul = $("<ul></ul>");
  $("#interests").append($ul);

  $(list).each(function(i) {
    var $li = $("<li></li>").text(list[i].name);
    $li.click(function(e) {
      e.preventDefault();
      goToUserPage(list[i].interestid);
    });
    $($ul).append($li);
  });
}

function getInterests() {
  // connect to server

  var url = "http://localhost:8000/getuserinterests";
  var userid = sessionStorage.getItem("userid");
  var data = {
    userid: userid
  }

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, success) {
      var interests = data["interests"];
      createClickableList(interests);
    },
    error: function(error) {
      console.warn(error)
    }
  });
}

function newMessage() {
  console.log("sending message")
  var recipientid = window.location.hash.substring(1);
  var recipientname = window.name;
  sessionStorage.setItem("recipientid", recipientid);
  sessionStorage.setItem("recipientname", recipientname);
  window.location.href="new-message.html";
}