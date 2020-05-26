function createUL(list) {
  var ul = document.createElement("ul");

  for (var i = 0; i < list.length; i++) {
    var item = document.createElement("li");

    item.appendChild(document.createTextNode(list[i]));

    ul.append(item);
  }

  console.log(ul);
  return ul;
}
