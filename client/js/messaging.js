$(document).ready(function() {
  $("inbox").ready(function() {
    getInbox();
  });

  $("outbox").ready(function() {
    getOutbox();
  });
});


function getInbox() {
  console.log("getting inbox");
  // connect to server

  var url = "http://localhost:8000/getreceivedmessages";
  var data = {
    userid: sessionStorage.getItem("userid")
  }

  $.ajax({
    url: url,
    data: JSON.stringify(data),
    success: function(data, status) {
      var list = data["receivedmessages"];
      buildInbox(list);
    },
    error: function(error) {
      console.warn(`error while getting inbox: ${error}`)
    }
  });  
}

// TODO: format properly
function buildInbox(list) {
  for (var i = 0; i < list.length; i++) {
    var details = document.createElement("details");
    var summary = document.createElement("summary");
    summary.appendChild(document.createTextNode(list[i].fromUser + "------" + list[i].timestamp));
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(list[i].body));
    details.appendChild(summary);
    details.appendChild(p);

    document.getElementById("inbox").appendChild(details);
  }
}

function getOutbox() {
  console.log("getting outbox");
  // connect to server

  var url = "http://localhost:8000/getsentmessages";
  var data = {
    userid: sessionStorage.getItem("userid")
  }

  $.ajax({
    url: url,
    data: JSON.stringify(data),
    success: function(data, status) {
      var list = data["sentmessages"];
      buildOutbox(list);
    },
    error: function(error) {
      console.warn(`error while getting inbox: ${error}`)
    }
  });
}

// TODO: format properly
function buildOutbox() {
  for (var i = 0; i < list.length; i++) {
    var details = document.createElement("details");
    var summary = document.createElement("summary");
    summary.appendChild(document.createTextNode(list[i].toUser + "------" + list[i].timestamp));
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(list[i].body));
    details.appendChild(summary);
    details.appendChild(p);

    document.getElementById("outbox").appendChild(details);
  }
}
