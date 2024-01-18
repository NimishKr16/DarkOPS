document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("fetchButton").addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      var currentURL = tabs[0].url;

      fetch("http://localhost:1100/ff", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: currentURL }),
      })
        .then((response) => response.json())
        .then((result) => {
          // Display the result in the extension
          displayURLResult(result.message); 
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    });
  });

  function displayURLResult(message) {
    // Update the content of the resultContainer
    var resultContainer = document.getElementById("resultContainer");
    resultContainer.innerHTML = "<p>Result from Python:</p><p>" + message + "</p>";
  }
});
