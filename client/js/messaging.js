document.getElementById("inbox").addEventListener("load", getInbox());
document.getElementById("outbox").addEventListener("load", getOutbox());



function getInbox() {
  console.log("getting inbox");
  // connect to server

  var list = []
  list.push({fromUser: "Mike", body: "Hello, this is Mike", timestamp: "May 17, 6:04 pm"});
  list.push({fromUser: "Sarah", body: "Hello, this is Sarah", timestamp: "May 22, 10:43 am"});
  list.push({fromUser: "David", body: "Hello, this is David", timestamp: "May 20, 12:15 pm"});

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

  var list = []
  list.push({toUser: "Mike", body: "Hi there!", timestamp: "May 17, 6:15 pm"});
  list.push({toUser: "Sarah", body: "Nice to meet you :)", timestamp: "May 22, 11:22 am"});
  list.push({toUser: "David", body: "Hi David, how are you?", timestamp: "May 20, 11:59 am"});

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
