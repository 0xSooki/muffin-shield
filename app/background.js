chrome.runtime.onInstalled.addListener(function () {});

chrome.tabs.onActivated.addListener(function (activeInfo) {
  chrome.tabs.get(activeInfo.tabId, async function (tab) {
    let res = await CheckValidity(tab.url);
    console.log(res);
  });
});

async function CheckValidity(url) {
  fetch(`http://localhost:8000/?url=${url}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then(async function (res) {
      console.log("Link sent successfully");
      let data = await res.json();
      console.log(data);
    })
    .catch(function (error) {
      console.error("Error sending link:", error);
    });
}
