document.getElementById("recipient").addEventListener("load", checkRecipient())

function sendMessage() {
  console.log("sending message");

  // var userid = sessionStorage.getItem("userid");
  // var toid = document.getElementById("recipient").value;
  // var body = document.getElementById("body").value;

  // var url = "http://localhost:8000/createmessage";
  // var data = {
  //   fromid: userid,
  //   toid: toid,
  //   body: body
  // };

  // $.ajax({
  //   url: url,
  //   type: "POST",
  //   data: JSON.stringify(data),
  //   success: function(data, status) {
  //     console.log(data)
      
  //     window.location.href="messaging.html";
  //   }, 
  //   error: function(error) {
  //     console.log(error);
  //   }
  // });  

  window.location.href="messaging.html";

}

function checkRecipient() {
  var recipient = sessionStorage.getItem("recipient");
  if (recipient != null) {
    document.getElementById("recipient").value = recipient;
    sessionStorage.removeItem("recipient");
  }
}