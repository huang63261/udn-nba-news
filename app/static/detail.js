document.addEventListener("DOMContentLoaded", () => {
  console.log("successful in")
  const pathParts = window.location.pathname.split("/");
  const newsId = pathParts[pathParts.length - 1];

  fetch(`/api/news/${newsId}`)
    .then((res) => res.json())
    .then((data) => {
      document.title = data.title;
      document.getElementById("news-title").innerText = data.title;
      document.getElementById("news-content").innerText = data.content;
      if (data.image_url) {
        document.getElementById("news-image").src = data.image_url;
      } else {
        document.getElementById("news-image").style.display = "none";
      }
    })
    .catch((err) => {
      document.getElementById("news-title").innerText = "載入失敗";
      console.error(err);
    });
});
