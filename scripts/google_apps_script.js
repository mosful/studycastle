/**
 * 🏰 學習城堡 — 意見反饋 Google Apps Script 雲端處理腳本
 * 
 * 【使用說明】
 * 1. 前往 Google 雲端硬碟建立一份新的「Google 試算表」（例如：學習城堡_意見反饋記錄）。
 * 2. 點擊頂端選單「擴充功能」 -> 「Apps Script」。
 * 3. 將本檔案全部內容複製並貼上到 Apps Script 編輯器中。
 * 4. 將下方 NOTIFICATION_EMAIL 改成您欲接收通知的電子信箱。
 * 5. 點擊右上角「部署」 -> 「新增部署作業」：
 *    - 種類選擇：網頁應用程式 (Web App)
 *    - 說明：Feedback API
 *    - 執行身分：我 (您的帳號)
 *    - 誰可以存取：所有人 (Anyone)  <--- 務必選「所有人」，訪客才能免登入直接送出
 * 6. 點擊「部署」，授權存取後，複製產生的「網頁應用程式網址 (Web App URL)」。
 * 7. 將取得的 URL 貼回 index.html 與 portal.html 中的 GOOGLE_FEEDBACK_API_URL 變數中即可！
 */

// ====== 設定區 ======
// 請在此填入您要接收通知信件的 Email 地址
const NOTIFICATION_EMAIL = "your-email@example.com";
// ====================

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // 若工作表第 1 列為空，自動建立標題列
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(["時間戳記", "反饋類型", "相關單元", "填寫者", "意見內容", "來源網頁"]);
      sheet.getRange(1, 1, 1, 6).setFontWeight("bold").setBackground("#f0f4f8");
    }

    // 解析前端傳來的 JSON 資料
    const data = JSON.parse(e.postData.contents);
    const time = new Date().toLocaleString("zh-TW", { timeZone: "Asia/Taipei" });
    const type = data.type || "未指定";
    const unit = data.unit || "全站 / 一般建議";
    const name = data.name || "熱心冒險家";
    const content = data.content || "";
    const sourceUrl = data.sourceUrl || "首頁";

    // 1. 寫入 Google 試算表新增一列
    sheet.appendRow([time, type, unit, name, content, sourceUrl]);

    // 2. 發送 Email 通知給管理者
    if (NOTIFICATION_EMAIL && NOTIFICATION_EMAIL !== "your-email@example.com") {
      const subject = `🏰【學習城堡】收到新的意見反饋：[${type}] 來自 ${name}`;
      const htmlBody = `
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e0e7ff; border-radius: 12px; background-color: #ffffff;">
          <h2 style="color: #4338ca; margin-top: 0;">🏰 學習城堡 — 收到新的意見反饋</h2>
          <p style="color: #64748b; font-size: 14px;">收件時間：${time}</p>
          <hr style="border: none; border-top: 1px solid #e2e8f0; margin: 15px 0;">
          
          <table style="width: 100%; border-collapse: collapse; margin-bottom: 20px;">
            <tr>
              <td style="padding: 8px 0; color: #475569; width: 90px; font-weight: bold;">反饋類型：</td>
              <td style="padding: 8px 0; color: #0f172a;"><span style="background: #e0e7ff; color: #3730a3; padding: 3px 8px; border-radius: 6px; font-size: 13px;">${type}</span></td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #475569; font-weight: bold;">相關單元：</td>
              <td style="padding: 8px 0; color: #0f172a;">${unit}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #475569; font-weight: bold;">填寫者：</td>
              <td style="padding: 8px 0; color: #0f172a;">${name}</td>
            </tr>
            <tr>
              <td style="padding: 8px 0; color: #475569; font-weight: bold;">來源網址：</td>
              <td style="padding: 8px 0; color: #64748b; font-size: 13px;">${sourceUrl}</td>
            </tr>
          </table>

          <div style="background-color: #f8fafc; border-left: 4px solid #6366f1; padding: 15px; border-radius: 6px; margin-bottom: 20px;">
            <p style="margin: 0 0 6px 0; font-weight: bold; color: #334155;">反饋內容：</p>
            <p style="margin: 0; color: #1e293b; white-space: pre-wrap; line-height: 1.6;">${content}</p>
          </div>
          
          <p style="font-size: 12px; color: #94a3b8; text-align: center; margin-top: 20px;">
            本信件由 學習城堡 Google Apps Script 自動發送
          </p>
        </div>
      `;

      MailApp.sendEmail({
        to: NOTIFICATION_EMAIL,
        subject: subject,
        htmlBody: htmlBody
      });
    }

    // 回傳 JSON 成功響應
    return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
