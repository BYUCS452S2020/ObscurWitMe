document.getElementById("info").addEventListener("load", getUser());
document.getElementById("interests").addEventListener("load", getInterests());


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

  // change to interestid eventually?

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

  list = []
  list.push("Basketball");
  list.push("Golfing");
  list.push("Chess");
  list.push("Frisbee Throwing");
  list.push("Hammocking");
  list.push("Running");
  list.push("Painting");
  list.push("Collecting Flags");
  list.push("Paper Planes");
  list.push("Hotdog-eating");

  createClickableList(list);
}

function newMessage() {
  console.log("sending message")
  // change into userid eventually
  var username = window.location.hash.substring(1);
  sessionStorage.setItem("recipient", username);
  window.location.href="new-message.html";
}