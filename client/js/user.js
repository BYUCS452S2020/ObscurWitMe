$(document).ready(function() {
  $("info").ready(function() {
    getUser();
  });

  $("interests").ready(function() {
    getInterests();
  });
});


function getUser() {
  var username = window.location.hash.substring(1);
  console.log(username);

  // connect to server

  var user = { firstName: "Mike", lastName: "Jones", age: "25", location: "84604"};

  for (let key in user) {
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(key + ": " + user[key]));
    document.getElementById("info").appendChild(p);
  }
}

function goToInterestPage(interest) {
  console.log(interest);

  // TODO: change to interestid 
  window.location.href="interest.html#" + interest;
}

function createClickableList(list) {
  for (var i = 0; i < list.length; i++) {
    var span = document.createElement("span");
    span.appendChild(document.createTextNode(list[i]));
    span.addEventListener("click", function() { goToInterestPage(this.innerText) });
    document.getElementById("interests").appendChild(span);
  }
}

function getInterests() {
  // connect to server

  var url = "http://localhost:8000/getuserinterests";
  // TODO: get userid somehow
  var userid = sessionStorage.getItem("userinterest";)
  var data = {
    userid: userid
  }

  $.ajax({
    url: url,
    data: JSON.stringify(data),
    success: function(data, success) {
      var list = data["interests"];
      createClickableList(list);
    },
    error: function(error) {
      console.warn(error)
    }
  });
}

function newMessage() {
  console.log("sending message")
  // TODO: change into userid
  var username = window.location.hash.substring(1);
  sessionStorage.setItem("recipient", username);
  window.location.href="new-message.html";
}