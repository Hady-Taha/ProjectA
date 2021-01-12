(function() {
  var darkSwitch = document.getElementById("darkSwitch");
  if (darkSwitch) {
    initTheme();
    darkSwitch.addEventListener("change", function(event) {
      resetTheme();
    });
    function initTheme() {
      var darkThemeSelected =
        localStorage.getItem("darkSwitch") !== null &&
        localStorage.getItem("darkSwitch") === "dark";
      darkSwitch.checked = darkThemeSelected;
      darkThemeSelected
        ? document.body.setAttribute("data-theme", "dark")
        : document.body.removeAttribute("data-theme");
    }
    function resetTheme() {
      if (darkSwitch.checked) {
        document.body.setAttribute("data-theme", "dark");
        document.body.setAttribute("class", "fade-in");
        localStorage.setItem("darkSwitch", "dark");
        document.getElementById('darkSwitchlabel').innerText='Dark 🌚'
        
      } else {
        document.body.removeAttribute("data-theme");
        document.body.removeAttribute("class");
        localStorage.removeItem("darkSwitch");

        document.getElementById('darkSwitchlabel').innerText='Light 🌕'
      }
    }
  }
})();
