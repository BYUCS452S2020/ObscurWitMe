document.getElementById("info").addEventListener("load", getUser());


function getUser() {
  var username = window.location.hash.substring(1);
  console.log(username);
}