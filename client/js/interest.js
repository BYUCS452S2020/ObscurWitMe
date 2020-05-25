document.getElementById("header").addEventListener("load", getHeader());
document.getElementById("info").addEventListener("load", getInterest());

function getHeader() {
  var header = window.location.hash.substring(1);
  console.log(header);

  document.getElementById("header").innerText = decodeURI(header);
}

function getInterest() {
  var name = window.location.hash.substring(1);

  // connect to server

  interest = {category: "Coolness", description: "Cool activity!", thumbnail: "url" };

  for (let key in interest) {
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(key + ": " + interest[key]));
    document.getElementById("info").appendChild(p);
  }
}