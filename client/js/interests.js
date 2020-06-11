$(document).ready(function() {
  sessionStorage.setItem("search_startat", "0");


  $("interests").ready(function() {
    // TODO: fix
    var url = "http://localhost:8000/getallinterests";
    // var url = "http://localhost:8000/getsearchinterests";
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
        var list = data["interests"];
        createClickableList(list, $("#interests"));
      }, 
      error: function(error) {
        console.log(error);
      }
    });
  });

  $("#sports_btn").click(function() {
    // TODO: fix
    var url = "http://localhost:8000/getallinterests";
    // var url = "http://localhost:8000/getsearchinterests";
    var startat = parseInt(sessionStorage.getItem("sports_startat"));
    
    var data = {
      startat: startat,
      count: 10,
      query: "sports"
    }

    $.ajax({
      url: url,
      type: "GET",
      data: JSON.stringify(data),
      success: function(data, status) {
        var list = data["interests"];
        console.log(list);
        createClickableList(list, $("#results"));

        if ($("#results ul li").length < data["totalcount"]) {
          sessionStorage.setItem("sports_startat", (startat + 10).toString());
          toggleMoreButton(false);
        } else {
          toggleMoreButton(true);
        }
      },
      error: function(error) {
        console.warn(error);
      }
    });
  });

  $("#movies_btn").click(function() {
    // TODO: fix
    var url = "http://localhost:8000/getallinterests";
    // var url = "http://localhost:8000/getsearchinterests";
    var startat = parseInt(sessionStorage.getItem("movies_startat"));
    
    var data = {
      startat: startat,
      count: 10,
      query: "movies"
    }

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        var list = data["interests"];
        console.log(list);
        createClickableList(list, $("#results"));

        if ($("#results ul li").length < data["totalcount"]) {
          sessionStorage.setItem("movies_startat", (startat + 10).toString());
          toggleMoreButton(false);
        } else {
          toggleMoreButton(true);
        }
      },
      error: function(error) {
        console.warn(error);
      }
    });
  });

  $("#nature_btn").click(function() {
    // TODO: fix
    var url = "http://localhost:8000/getallinterests";
    // var url = "http://localhost:8000/getsearchinterests";
    var startat = parseInt(sessionStorage.getItem("nature_startat"));
    
    var data = {
      startat: startat,
      count: 10,
      query: "nature"
    }

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {
        var list = data["interests"];
        console.log(list);
        createClickableList(list, $("#results"));

        if ($("#results ul li").length < data["totalcount"]) {
          sessionStorage.setItem("nature_startat", (startat + 10).toString());
          toggleMoreButton(false);
        } else {
          toggleMoreButton(true);
        }
      },
      error: function(error) {
        console.warn(error);
      }
    });
  });

  $("#search_btn").click(function() {
    var text = $("#search").val();
    console.log("searching for: " + text);

    // TODO: fix
    var url = "http://localhost:8000/getallinterests";
    // var url = "http://localhost:8000/getsearchinterests";
    var startat = parseInt(sessionStorage.getItem("search_startat"));

    var data = {
      startat: startat,
      count: 10,
      query: text
    };

    $.ajax({
      url: url,
      type: "POST",
      data: JSON.stringify(data),
      success: function(data, status) {    
        console.log("success, data: " + JSON.stringify(data));

        var list = data["interests"];
        console.log(list);
        createClickableList(list, $("#results"));

        if ($("#results ul li").length < data["totalcount"]) {
          sessionStorage.setItem("search_startat", (startat + 10).toString());
          toggleMoreButton(false);
        } else {
          toggleMoreButton(true);
        }
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

function goToInterestPage(interestid) {
  console.log(interestid);

  window.location.href="interest.html#" + interestid;
}

function createClickableList(list, element) {
  var $ul = $("<ul></ul>");
  element.append($ul);

  $(list).each(function(i) {
    var $li = $("<li></li>").text(list[i].name);
    $li.click(function(e) {
      e.preventDefault();
      goToUserPage(list[i].interestid);
    });
    $($ul).append($li);
  });
}

function toggleMoreButton(hide) {
  if (hide) {
    $("#more").hide();
  } else {
    $("#more").show();
  }
}