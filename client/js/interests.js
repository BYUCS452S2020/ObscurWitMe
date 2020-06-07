$(document).ready(function() {
  $("interests").ready(function() {
    var url = "http://localhost:8000/getuserinterests";
    var data = {
      userid: sessionStorage.getItem("userid")
    }

    console.log(data);

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {              
        console.log("success, data: " + JSON.stringify(data));
        var list = data['interests'];
        var ul = createUL(list);

        document.getElementById("interests").appendChild(ul);
      }, 
      error: function(error) {
        console.log(error);
      }
    });
  });

  $("#search_btn").click(function() {
    console.log("in search");
    var text = $("#search").val();
    console.log("searching for: " + text);
    
    var url = "http://localhost:8000/getallinterests";
    var data = {};

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {              
        console.log("success, data: " + JSON.stringify(data));

        var list = data['interests'];
        console.log(list);
        createClickableList(list);
        // var ul = createUL(list);

        // document.getElementById("results").appendChild(ul);
      }, 
      error: function(error) {
        console.log(error);
      }
    });
  });

  $("#search").keyup(function() {
    $("search_btn").click();
  });
});

function goToInterestPage(interest) {
  console.log(interest);

  // TODO: change to interestid

  window.location.href="interest.html#" + interest;
}

function createClickableList(list) {
  for (var i = 0; i < list.length; i++) {
    var span = document.createElement("span");
    span.appendChild(document.createTextNode(list[i].name));
    span.addEventListener("click", function() { goToInterestPage(this.innerText) });
    document.getElementById("results").appendChild(span);
  }
}

function createUL(list) {
  var ul = document.createElement("ul");

  for (var i = 0; i < list.length; i++) {
    var item = document.createElement("li");

    item.appendChild(document.createTextNode(list[i].name));

    ul.append(item);
  }

  console.log(ul);
  return ul;
}
