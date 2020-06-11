$(document).ready(function() {
  $("recipient").ready(function() {
    checkRecipient();
  });
});

function sendMessage() {
  console.log("sending message");

  var fromid = sessionStorage.getItem("userid");
  var toid = sessionStorage.getItem("recipientid");
  var body = document.getElementById("body").value;

  var url = "http://localhost:8000/createmessage";
  var data = {
    fromid: fromid,
    toid: toid,
    body: body
  };

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, status) {
      alert("Message sent!");
      sessionStorage.removeItem("recipient");
      
      console.log(data)
      
      window.location.href="messaging.html";
    }, 
    error: function(error) {
      console.log(error);
      alert("Could not send message :(");
    }
  });
}

function checkRecipient() {
  var recipient = sessionStorage.getItem("recipientname");
  if (recipient != null) {
    document.getElementById("recipient").value = recipient;
  }
}