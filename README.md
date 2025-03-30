# 🏀 UDN NBA Featured News Crawler

一個使用 **FastAPI** 開發的小專案，具備爬蟲、資料庫、API、簡易前端畫面。

🔗 Demo 網址：[https://udn-nba-news.onrender.com/](https://udn-nba-news.onrender.com/)

📦 GitHub Repo：[https://github.com/huang63261/udn-nba-news](https://github.com/huang63261/udn-nba-news)

---

## 📸 頁面畫面

- `/` 焦點新聞列表（含刷新按鈕）
- `/news/{id}` 新聞詳情頁面

---

## 🚀 使用技術

| 分類 | 技術 |
|------|------|
| Web Framework | FastAPI |
| ORM / DB | SQLModel + SQLite |
| Migration | Alembic |
| Crawler | requests + BeautifulSoup |
| Frontend | HTML + Jinja2 + 原生 JS (AJAX) |
| Deployment | Render 免費雲平台 |

---

## 📂 專案結構

```
app/
├── main.py                  # FastAPI 入口，含 lifespan + migration
├── database.py              # 資料庫連線設定
├── dependency.py           # get_session 依賴注入
├── models.py               # News 資料表模型
├── crud/
│   └── news.py             # News 資料存取邏輯
├── services/
│   └── crawler.py          # 爬蟲邏輯 fetch_feature_news()
├── routers/
│   ├── news.py             # API 路由（JSON）
│   └── page.py             # 頁面路由（HTML）
├── templates/
│   ├── index.html          # 焦點新聞頁面（含刷新按鈕）
│   └── detail.html         # 新聞詳情頁面
├── static/
│   ├── main.css            # 基本樣式
│   ├── script.js           # 載入新聞列表 + 刷新
│   └── detail.js           # 載入單篇新聞詳情
```

---

## 🛠 快速啟動專案（本地）

```bash
git clone https://github.com/huang63261/udn-nba-news.git
cd udn-nba-news
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 初始化 DB
alembic upgrade head

# 啟動 FastAPI
uvicorn app.main:app --reload
```

---


## 📮 API 路由

| 方法 | 路徑 | 功能 |
|------|------|------|
| GET  | `/api/news` | 取得所有新聞 |
| GET  | `/api/news/{id}` | 取得單篇新聞 |
| GET  | `/api/news/crawl-news/` | 立即爬取新聞並儲存（AJAX 按鈕使用） |
