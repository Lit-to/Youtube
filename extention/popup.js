document.addEventListener("DOMContentLoaded", function () {
    console.log("DOMContentLoaded event triggered");
    document.getElementById("collectButton").addEventListener("click", function () {
        console.log("Button clicked");
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
            console.log("Tab ID:", tabs[0].id);
            chrome.scripting.executeScript({
                target: { tabId: tabs[0].id },
                files: ["content.js"],
            });
        });
    });
});
