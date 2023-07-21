// 日付を取得する関数
function getCurrentDate() {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, "0");
    const date = String(now.getDate()).padStart(2, "0");
    return `${year}-${month}-${date}`;
}

// 情報を取得する関数
function getInfo() {
    const detailsElement = document.querySelector("div.issue.details");

    if (!detailsElement) {
        return null;
    }

    const id = document.querySelector("span.id em").textContent.trim();
    const url = window.location.href;
    const resolution = detailsElement.querySelector("span.resolution");
    const affectsVersions = detailsElement.querySelector("span.affects-version");
    const confirmationStatus = detailsElement.querySelector(
        "span.confirmation-status"
    );
    const fixVersions = detailsElement.querySelector("span.fix-version");
    const category = detailsElement.querySelector("span.category");

    return {
        date: getCurrentDate(),
        id,
        url,
        resolution: resolution ? resolution.textContent.trim() : "",
        affectsVersions: affectsVersions ? affectsVersions.textContent.trim() : "",
        confirmationStatus: confirmationStatus
            ? confirmationStatus.textContent.trim()
            : "",
        fixVersions: fixVersions ? fixVersions.textContent.trim() : "",
        category: category ? category.textContent.trim() : "",
    };
}

// CSV形式に変換する関数
function convertToCSV(info) {
    const csv = [
        "Date,ID,URL,Resolution,Affects Version/s,Confirmation Status,Fix Version/s,Category",
    ];
    csv.push(
        `${info.date},${info.id},${info.url},"${info.resolution}","${info.affectsVersions}","${info.confirmationStatus}","${info.fixVersions}","${info.category}"`
    );
    return csv.join("\n");
}

// CSVファイルをダウンロードする関数
function downloadCSV(csvContent) {
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "bug_info.csv";
    a.click();
}

// ページがロードされたら情報を取得し、CSVをダウンロード
const info = getInfo();
if (info) {
    const csvContent = convertToCSV(info);
    downloadCSV(csvContent);
}
