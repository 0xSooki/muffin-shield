const div = document.createElement("div");

function messageListener(message) {
  console.log(message);
  if (message && message.data) {
    div.innerText = message.data;
  }
}

chrome.runtime.onMessage.addListener(messageListener);

div.style.position = "fixed";
div.style.top = "0px";
div.style.left = "0px";
div.style.zIndex = "9999";

document.body.appendChild(div);
