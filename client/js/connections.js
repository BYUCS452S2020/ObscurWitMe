document.getElementById("connections").addEventListener("load", getPotentialConnections());

function goToUserPage(username) {
  console.log(username);

  // change to userid eventually

  window.location.href="user.html#" + username;
}

function createClickableList(list) {
  for (var i = 0; i < list.length; i++) {
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(list[i]));
    p.addEventListener("click", function() { goToUserPage(this.innerText) });
    document.getElementById("connections").appendChild(p);
  }
}

function getPotentialConnections() {
  console.log("getting connections");
  // connect to server

  list = []
  list.push("Mike");
  list.push("Sarah");
  list.push("Joey");
  list.push("Jessica");

  createClickableList(list);
}