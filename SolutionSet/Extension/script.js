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

  document.getElementById("UIScan").addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var currentURL = tabs[0].url;

        fetch("http://localhost:1100/uiscan", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ url: currentURL }),
        })
        .then((response) => response.json())
        .then((result) => {
            // Assuming result.path contains the path to the "prediction.jpg" file
            displayImage(result.path);
        })
        .catch((error) => {
            console.error("Error:", error);
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
  // Get the image element
  var imgElement = document.getElementById('displayedImage');

  // Set the image source (replace 'path/to/your/image.jpg' with the actual path)
  var imagePath = '/Users/nimish/Desktop/dpbh/extension/prediction.jpg';
  imgElement.src = chrome.extension.getURL(imagePath);
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


function displayImage(imagePath) {
  var imgElement = document.createElement("img");
  imgElement.src = imagePath;

  // On error, log to the console
  imgElement.onerror = function() {
      console.error("Error loading image:", imagePath);
  };

  // Append the image element to the body of the web page
  document.body.appendChild(imgElement);
}