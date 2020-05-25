document.getElementById("recipient").addEventListener("load", checkRecipient())

function sendMessage() {
  console.log("sending message");

  var recipient = document.getElementById("recipient").value;
  var body = document.getElementById("body").value;

  // connect to server

  window.location.href="messaging.html";
  
}

function checkRecipient() {
  var recipient = sessionStorage.getItem("recipient");
  if (recipient != null) {
    document.getElementById("recipient").value = recipient;
    sessionStorage.removeItem("recipient");
  }
}