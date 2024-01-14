# CryptoNews-DiscordBot 🌍💬

![GitHub stars](https://img.shields.io/github/stars/p3tr1nn1/CryptoNews-DiscordBot?style=social) ![GitHub forks](https://img.shields.io/github/forks/p3tr1nn1/CryptoNews-DiscordBot?style=social) ![GitHub watchers](https://img.shields.io/github/watchers/p3tr1nn1/CryptoNews-DiscordBot?style=social) ![License](https://img.shields.io/github/license/p3tr1nn1/CryptoNews-DiscordBot)

**CryptoNews-DiscordBot** is a Python-based automation tool for crypto enthusiasts. It fetches the latest news from various cryptocurrency RSS feeds and relays this information through Discord notifications, HTML pages, and JSON files.

## 🚀 Features

- 📰 Fetches crypto news from multiple RSS feeds.
- 📄 Creates JSON files for offline processing.
- 📢 Sends updates to Discord channels.
- 🌐 Generates an HTML page with the latest news.


## 📋 Installation and Configuration

### Prerequisites

- 🐍 Python 3.x
- 📦 pip (Python package manager)
- 🗃️ SQLite3
- 🎮 Discord account for webhook setup

### 🐧 Setup on Ubuntu

1. **Clone the repository:**
   ```bash
   git clone https://github.com/p3tr1nn1/CryptoNews-DiscordBot.git
   cd CryptoNews-DiscordBot
   ```

2. **Install dependencies:**
   ```bash
   pip3 install feedparser requests
   ```

3. **Discord Webhook Setup:**
   - Navigate to your Discord server settings ➡️ 'Integrations'.
   - Click 'Create Webhook' and set your preferred channel.
   - Copy the webhook URL.

4. **Configure environment variables:**
   ```bash
   export DISCORD_WEBHOOK_URL='your_discord_webhook_url'
   ```

### 🚀 Usage

Run the main script:
```bash
python main.py
```
## 🗃️ Database Schema

The application utilizes an SQLite database to store fetched articles. Below is the schema for the `articles` table:

- `title` TEXT: The title of the article.
- `link` TEXT PRIMARY KEY: The unique link to the article.
- `description` TEXT: A short description or summary of the article.
- `publication_date` TEXT: The date and time of the article's publication.
- `content_url` TEXT: The URL of the article's main content or image.
- `sent_to_discord` BOOLEAN: Indicates if the article has been sent to Discord.
- `source` TEXT: The name of the RSS feed source.

## 📡 Supported RSS Feeds

The script fetches and aggregates news from the following cryptocurrency news sources:

1. **Coindesk**: `https://www.coindesk.com/arc/outboundfeeds/rss/`
2. **The Defiant**: `https://thedefiant.io/feed/`
3. **Investing.com**: `https://www.investing.com/rss/news_301.rss`
4. **Bitcoin Magazine**: `https://bitcoinmagazine.com/feed`
5. **Decrypt.co**: `https://decrypt.co/feed`
6. **CryptoSlate**: `https://cryptoslate.com/feed`
7. **Crypto Briefing**: `https://cryptobriefing.com/feed`
8. **Crypto News**: `https://cryptonews.com/feed/`
9. **Bitcoinist**: `https://bitcoinist.com/feed`
10. **The Blockchain**: `https://www.the-blockchain.com/feed`
11. **NewsBTC**: `https://www.newsbtc.com/feed`
12. **Bitcoin News**: `https://news.bitcoin.com/feed`

---

## 🌐 Generating HTML Report with `generate_html_page.py`

The `generate_html_page.py` script is designed to create a visually appealing HTML page that displays the latest cryptocurrency news articles. Here's how it works:

1. **Fetching Data**: The script connects to the SQLite database (`central_rss_articles.db`) and fetches the latest 100 articles sorted by their publication date in descending order.

2. **HTML Generation**: It then generates an HTML file (`crypto_news.html`) with a sleek and readable layout. This includes:
   - A styled list of articles, each with a title, link, description, publication date, and associated image.
   - Each article is displayed within a styled block, containing an image at the top followed by the title, description, and publication date.
   - The HTML page is styled with CSS for readability, using a dark theme (dark background with light text) that is gentle on the eyes.

3. **Output**: The final output is an HTML file that provides a user-friendly way to browse through the latest 100 cryptocurrency news articles.

This script enhances the accessibility of the news data by presenting it in a well-structured and visually appealing web page format, making it easy for users to navigate and read through the latest updates in the world of cryptocurrency.

--- 

## 📜 License
Distributed under the MIT License. See `LICENSE.md` for more information.
--- 
