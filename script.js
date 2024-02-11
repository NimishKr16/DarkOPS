async function executeFunctionsSequentially() {
  try {
      const tabs = await new Promise((resolve, reject) => {
          chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
              if (tabs && tabs.length > 0) {
                  resolve(tabs);
              } else {
                  reject(new Error('No active tabs found'));
              }
          });
      });

      const currentURL = tabs[0].url;

      // Function URL SCAN
      const response3 = await fetch("http://localhost:1100/scanweb", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ url: currentURL }),
      });
      const result3 = await response3.json();
      maliciousRes(result3.message);
      if(result3.message != "Webpage is : Safe & Trusted" && result3.message != "Webpage is : Mildly Risky"
      && result3.message != "Webpage is : Slightly Risky" ){
        return;
      }

      // Function REVIEW + ATTRIBUTE SCAN
      const response2 = await fetch("http://localhost:1100/scan", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ url: currentURL }),
      });
      const result2 = await response2.json();
      reviewRes(result2.message1, result2.message2);

      // Function UI SCAN
      const response1 = await fetch("http://localhost:1100/uiscan", {
          method: "POST",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({ url: currentURL }),
      });
      const result1 = await response1.json();
      displayImage(result1.message2);

  } catch (error) {
      console.error("Error:", error);
  }
}

document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("scan").addEventListener("click", executeFunctionsSequentially);
});


document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("scan").addEventListener("click", executeFunctionsSequentially);
});


// -------------------- AI IMAGE CHECKER -------------------- #

document.getElementById('aichkbtn').addEventListener('click', function() {
    event.preventDefault();
    const imageUrl = document.getElementById('imageUrl').value;
    // Send the image URL to the backend
    fetch('http://localhost:1100/check', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ imageUrl })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        // Display the result on the web app interface
        displayResult(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
    
});


function displayResult(result) {
    const resultContainer = document.getElementById('AIresult');
    resultContainer.innerHTML = "Image is: "+result.status;
    // const status = document.createElement('p');
    // status.textContent = 'Status: ' + result.status;
    // resultContainer.appendChild(status);

    // const message = document.createElement('p');
    // message.textContent = 'Message: ' + result.message;
    // resultContainer.appendChild(message);

}


// ------------------------- OTHER FUNCS ---------------------------- #

function maliciousRes(message) {
  var resDiv = document.getElementById("maliciousScanDiv");
  resDiv.innerHTML = message;
}
function reviewRes(message1, message2) {
  var resDiv = document.getElementById("reviewResultDiv");
  resDiv.innerHTML = message1 + "<br>" + message2;
}


function displayImage(message) {
    var resDiv = document.getElementById("UIelementDiv");
    resDiv.innerHTML = message;
//   var imgElement = document.createElement("img");
//   imgElement.src = imagePath;

//   // On error, log to the console
//   imgElement.onerror = function() {
//       console.error("Error loading image:", imagePath);
//   };

//   // Append the image element to the body of the web page
//   document.body.appendChild(imgElement);
}