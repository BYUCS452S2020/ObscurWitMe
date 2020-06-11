$(document).ready(function() {
  $("inbox").ready(function() {
    getInbox();
  });

  $("outbox").ready(function() {
    getOutbox();
  });
});

function getTime(time) {
  var timestamp = time.substring(10, time.length - 1);

  var date = new Date(timestamp * 1000);
  var day = date.getDate();
  var month = date.getMonth();
  // Hours part from the timestamp
  var hours = date.getHours();
  // Minutes part from the timestamp
  var minutes = "0" + date.getMinutes();
  // Seconds part from the timestamp
  var seconds = "0" + date.getSeconds();

  // Will display time in 10:30:23 format
  var formattedTime = month + '/' + day + ", " + hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
  console.log(formattedTime);

  return formattedTime;
}

function getInbox() {
  console.log("getting inbox");
  // connect to server

  var url = "http://localhost:8000/getreceivedmessages";
  var data = {
    userid: sessionStorage.getItem("userid")
  }

  $.ajax({
    url: url,
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, status) {
      console.log(data);
      var list = data["receivedmessages"];
      buildInbox(list);
    },
    error: function(error) {
      console.warn(`error while getting inbox: ${error}`)
    }
  });  
}

function buildInbox(list) {
  for (var i = 0; i < list.length; i++) {
    var formattedTime = getTime(list[i].time);

    var details = document.createElement("details");
    var summary = document.createElement("summary");
    summary.appendChild(document.createTextNode(list[i].fromid + "------" + formattedTime));
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
    type: "POST",
    data: JSON.stringify(data),
    success: function(data, status) {
      console.log(data);
      var list = data["sentmessages"];
      buildOutbox(list);
    },
    error: function(error) {
      console.warn(`error while getting outbox: ${error}`)
    }
  });
}

function buildOutbox(list) {
  for (var i = 0; i < list.length; i++) {
    var formattedTime = getTime(list[i].time);

    var details = document.createElement("details");
    var summary = document.createElement("summary");
    summary.appendChild(document.createTextNode(list[i].toid + "------" + formattedTime));
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(list[i].body));
    details.appendChild(summary);
    details.appendChild(p);

    document.getElementById("outbox").appendChild(details);
  }
}
