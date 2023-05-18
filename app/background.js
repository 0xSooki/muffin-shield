chrome.runtime.onInstalled.addListener(function () {});

chrome.tabs.onActivated.addListener(function (activeInfo) {
  chrome.tabs.get(activeInfo.tabId, async function (tab) {
    let res = await CheckValidity(tab.url);
    console.log(res);
  });
});

async function CheckValidity(url) {
  fetch("http://localhost:8000/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ url: url }),
  })
    .then(function (res) {
      console.log("Link sent successfully");
      console.log(res);
    })
    .catch(function (error) {
      console.error("Error sending link:", error);
    });
}
