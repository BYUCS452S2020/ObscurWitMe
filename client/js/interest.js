$(document).ready(function() {
  $("#add").click(function() {
    // var interestid = sessionStorage.getItem("interestid");
    // var userid = sessionStorage.getItem("userid");

    // var url = "http://localhost:8000/addinterest"
    // var data = {
    //   interestid: interestid,
    //   userid: userid
    // }

    // $.ajax({
    //   url: url,
    //   data: JSON.stringify(data),
    //   type: "POST",
    //   success: function(data, status) {
        
    //   },
    //   error: function(error) {

    //   }
    // });

    window.history.back();
  });

  $("header").ready(getHeader());
  $("info").ready(getInterest());
});

function getHeader() {
  var header = window.location.hash.substring(1);
  console.log(header);

  document.getElementById("header").innerText = decodeURI(header);
}

function getInterest() {
  var name = window.location.hash.substring(1);

  // var url = "http://localhost:8000/getinterest";
  // var data = {
  //   name: name
  // };

  // $.ajax({
  //   url: url,
  //   data: JSON.stringify(data),
  //   type: "POST",
  //   success: function(data, status) {

  //   }, 
  //   error: function(error) {

  //   }
  // });

  interest = {category: "Cool stuff", description: "Really fun activity!", thumbnail: "url" };

  for (let key in interest) {
    var p = document.createElement("p");
    p.appendChild(document.createTextNode(key + ": " + interest[key]));
    document.getElementById("info").appendChild(p);
  }
}