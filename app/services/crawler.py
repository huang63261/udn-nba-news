import requests
import bs4
from typing import List, Dict
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
}


def fetch_feature_news() -> List[Dict]:
    feature_news_list = []

    response = requests.get("https://tw-nba.udn.com/nba/index", headers=headers)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    feature_news = soup.find("ul", class_="splide__list")
    if not feature_news:
        logger.warning("Cannot Find Featured News Section")
        return []

    for a_tag in feature_news.find_all("a"):
        h1_tag = a_tag.find("h1")
        title = h1_tag.text.strip() if h1_tag else "No Title"
        href = a_tag.get("href")
        img_tag = a_tag.select_one("picture img")
        image_url = img_tag["src"] if img_tag else None

        if not href or not href.startswith("https"):
            href = "https://tw-nba.udn.com" + href

        try:
            detail_resp = requests.get(href, headers=headers)
            detail_soup = bs4.BeautifulSoup(detail_resp.text, "html.parser")

            contents_dom = (
                detail_soup.find("div", id="story_body_content")
                .find(id="story_end")
                .parent
            )

            content_parts = []
            for tag in contents_dom.find_all("p"):
                if (
                    tag.find("div", class_="embedded-content")
                    or tag.get("dir") == "ltr"
                    or tag.find("figure")
                ):
                    continue

                text = tag.get_text(strip=True)
                if text:
                    content_parts.append(text)

            full_content = "\n\n".join(content_parts)

            feature_news_list.append(
                {
                    "title": title,
                    "url": href,
                    "content": full_content,
                    "image_url": image_url,
                }
            )

        except Exception as e:
            logger.warning(f"Error Handle News Link {href}: {e}")

    return feature_news_list
