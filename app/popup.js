chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
  if (changeInfo.status === "complete") {
    var currentUrl = tab.url;
    sendLinkToServer(currentUrl);
  }
});

function sendLinkToServer(url) {
  fetch("http://localhost:8000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  })
    .then(function (res) {
      console.log("Link sent successfully");
    })
    .catch(function (error) {
      console.error("Error sending link:", error);
    });
}
