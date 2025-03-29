document.addEventListener("DOMContentLoaded", () => {
  fetch("/api/news")
    .then((res) => res.json())
    .then((data) => {
      const container = document.getElementById("news-list");
      container.innerHTML = "";

      if (data.length === 0) {
        container.innerHTML = "<p>目前沒有新聞。</p>";
        return;
      }

      data.forEach((news) => {
        const item = document.createElement("div");
        item.innerHTML = `<p><a href="/${news.id}">${news.title}</a></p>`;
        container.appendChild(item);
      });
    })
    .catch((err) => {
      document.getElementById("news-list").innerText = "無法取得新聞資料。";
      console.error(err);
    });
});