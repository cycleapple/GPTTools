[English](https://github.com/cycleapple/GPTTools) | 繁體中文
# GPT 工具

這是一個使用 Flask 框架建立的網頁應用程式，提供了多種使用 OpenAI GPT-3 API 的工具。

## 目錄
- [概述](#概述)
- [安裝](#安裝)
- [使用](#使用)
- [工具](#工具)
  - [電子郵件生成工具](#電子郵件生成工具)
  - [Excel 公式生成工具](#excel-公式生成工具)
  - [正則表達式生成工具](#正則表達式生成工具)
- [貢獻](#貢獻)
- [授權](#授權)

# 概述
這個網頁應用程式提供了使用 OpenAI GPT-3 API 生成電子郵件、Excel 公式和正則表達式的工具。它還包括一個基於提供的 PDF 文件生成問題和答案的工具。

# 安裝
1. 將該存儲庫複製到本地計算機：
```bash
git clone https://github.com/your_username/gpt-tool.git
```
2. 進入專案的根目錄：
```bash
cd gpt-tool
```
3. 安裝所需的依賴項：
```bash
pip install -r requirements.txt
```
4. 在專案的根目錄中創建一個 .env 文件並添加您的 OpenAI API 密鑰：

```
OPENAI_API_KEY=your_api_key_here
```
5. 啟動 Flask 開發服務器：
```bash
python app.py
```

6. 在您的 Web 瀏覽器中打開 http://localhost:5000 以訪問網頁應用程式。
使用方法
啟動應用程式後，您可以通過點擊主頁面上相應的連結來訪問各種工具。

# 工具
## 電子郵件產生器
此工具基於用戶提供的發件人、收件人、主題和語言生成電子郵件。使用 OpenAI GPT-3 API 創建生成的電子郵件。

## Excel 公式產生器
此工具基於用戶提供的要求和選擇（Google Sheet 或 Excel）生成 Excel 公式。使用 OpenAI GPT-3 API 創建生成的公式。

## 正規表達式生成工具
此工具根據用戶提供的要求生成正規表達式。所生成的正規表達式是使用 Python 套件 regex 創建的，並使用在線正規表達式測試器 Regex101 測試了樣本輸入。

# 貢獻
歡迎任何貢獻！如果您有任何改進或新功能的想法，請隨時創建拉取請求。

# 授權
本專案根據 MIT 授權條款許可。