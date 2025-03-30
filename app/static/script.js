document.addEventListener("DOMContentLoaded", () => {
  const newsContainer = document.getElementById("news-list");
  const refreshBtn = document.getElementById("refresh-btn");

  const fetchNews = () => {
    fetch("/api/news")
      .then((res) => res.json())
      .then((data) => {
        newsContainer.innerHTML = "";
        if (data.length === 0) {
          newsContainer.innerHTML = "<p>目前沒有新聞。</p>";
          return;
        }

        data.forEach((news) => {
          const item = document.createElement("div");
          item.innerHTML = `<p><a href="/${news.id}">${news.title}</a></p>`;
          newsContainer.appendChild(item);
        });
      })
      .catch((err) => {
        newsContainer.innerText = "無法取得新聞資料。";
        console.error(err);
      });
  };

  // 初始載入
  fetchNews();

  refreshBtn.addEventListener("click", () => {
    refreshBtn.disabled = true;
    refreshBtn.innerText = "更新中...";

    fetch("/api/news/crawl-news/")
      .then((res) => res.json())
      .then((data) => {
        fetchNews();
      })
      .catch((err) => {
        console.error("刷新失敗", err);
        alert("更新失敗，請稍後再試");
      })
      .finally(() => {
        refreshBtn.disabled = false;
        refreshBtn.innerText = "🔄 取得最新新聞";
      });
  });
});
