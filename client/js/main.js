document.getElementById("search")
    .addEventListener("keyup", function(event) {
  event.preventDefault();
  if (event.keyCode === 13) {
      alert("enter");
  }
});