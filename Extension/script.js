document.addEventListener("DOMContentLoaded", function () {
  document
    .getElementById("maliciousScan")
    .addEventListener("click", function () {
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var currentURL = tabs[0].url;

        fetch("http://localhost:1100/scanweb", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ url: currentURL }),
        })
          .then((response) => response.json())
          .then((result) => {
            maliciousRes(result.message);
          })
          .catch((error) => {
            console.error("Error:", error);
          });
      });
    });

  document.getElementById("reviewScan").addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var currentURL = tabs[0].url;

      fetch("http://localhost:1100/scan", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: currentURL }),
      })
        .then((response) => response.json())
        .then((result) => {
          reviewRes(result.message1, result.message2);
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });
});
function maliciousRes(message) {
  var resDiv = document.getElementById("maliciousScanDiv");
  resDiv.innerHTML = message;
}
function reviewRes(message1, message2) {
  var resDiv = document.getElementById("reviewResultDiv");
  resDiv.innerHTML = message1 + "<br>" + message2;
}
