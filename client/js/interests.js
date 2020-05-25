document.getElementById("search").addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode === 13) {
    search();
  }
});

document.getElementById("interests").addEventListener("load", getInterests());


function createUL(list) {
  var ul = document.createElement('ul');

  for (var i = 0; i < list.length; i++) {
    var item = document.createElement('li');

    item.appendChild(document.createTextNode(list[i]));

    ul.append(item);
  }

  console.log(ul);
  return ul;
}

function search() {
  var text = document.getElementById("search").innerHTML;
  console.log(text);
  // connect to server
  

  var list = []
  list.push("Basketball");
  list.push("Football");
  list.push("Volleyball");

  var ul = createUL(list);

  document.getElementById("results").appendChild(ul);
}

function getInterests() {
  // connect to server
  console.log("getting interests")

  var list = []
  list.push("Basketball");
  list.push("Football");
  list.push("Volleyball");
  list.push("Music");
  list.push("Books");
  list.push("Art");

  var ul = createUL(list);

  document.getElementById("interests").appendChild(ul);
}