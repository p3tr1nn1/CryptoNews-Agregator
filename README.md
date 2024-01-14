# CryptoNews-DiscordBot 🌍💬

![Python Logo](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python) ![SQLite Logo](https://img.shields.io/badge/SQLite-Database-lightgrey?style=flat&logo=sqlite) ![Discord Logo](https://img.shields.io/badge/Discord-Bot-purple?style=flat&logo=discord) ![RSS Logo](https://img.shields.io/badge/RSS-Feeds-orange?style=flat&logo=rss)

**CryptoNews-DiscordBot** is a  Python-based automation tool specifically designed for cryptocurrency enthusiasts and digital finance communities. As a comprehensive crypto news aggregator, this bot efficiently collects the latest news from a wide array of prominent cryptocurrency RSS feeds. Its primary aim is to streamline the dissemination of cryptocurrency-related news and updates by utilizing modern digital platforms.

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
---

## 📄 Generating JSON Report with `generate_json.py`

The `generate_json.py` script is designed to export cryptocurrency news articles that have not yet been sent to Discord into a JSON file. This script performs the following functions:

1. **Fetching Unsent Articles**: It retrieves articles from the SQLite database (`central_rss_articles.db`) that have not been marked as sent to Discord. These articles are selected in ascending order by their publication date.

2. **JSON File Creation**: The script then converts these articles into a JSON format and writes them to a file (`unsent_to_discord.json`). This process includes:
   - Conversion of each article record (a tuple) into a dictionary.
   - Serialization of the list of article dictionaries into JSON format.
   - Writing the JSON data to a file with proper indentation for readability.

3. **Updating Sent Status**: After successfully writing the JSON file, the script updates the `sent_to_discord` status of these articles in the database to mark them as sent.

4. **Output and Logging**: The script outputs a message indicating the number of articles processed and the name of the JSON file created. If no new articles are available, it notifies the user accordingly.

This script is particularly useful for batch processing and transferring article data to external systems or for keeping a record of articles yet to be shared on Discord.

---
---

## 📢 Sending Discord Notifications with `generate_discord_notifications.py`

The `generate_discord_notifications.py` script automates the process of sending Discord notifications for new cryptocurrency news articles. Here's an overview of its functionality:

1. **Creating Discord Embeds**: For each unsent article, the script creates a Discord embed with a randomly generated color. The embed includes the article's title, description, publication date, and a "Read more" link.

2. **Batch Processing**: Articles are sent in batches to avoid rate limiting, with a configurable batch size (`MESSAGE_BATCH_SIZE`) and delay between batches (`BATCH_DELAY_SECONDS`).

3. **Error Handling and Retry Mechanism**: The script includes robust error handling with retries for failed messages. It will attempt to resend a message up to a specified number of times (`MAX_RETRIES`) with a delay between retries (`RETRY_DELAY_SECONDS`).

4. **Reading from JSON**: The script reads the articles to be sent from a JSON file (`unsent_to_discord.json`), allowing for easy integration with other parts of your system that may generate this file.

5. **Clearing JSON File**: After successful dispatch, the script clears the contents of the JSON file to prepare for the next batch of articles.

6. **Environment Variables**: It uses an environment variable (`DISCORD_WEBHOOK_URL`) for the Discord webhook URL, ensuring secure and flexible configuration.

7. **Usage**: To run the script, simply set the `DISCORD_WEBHOOK_URL` environment variable and execute the script. It will process all articles in the JSON file and send them as Discord notifications.

This script is essential for keeping your Discord channel updated with the latest cryptocurrency news in an automated and efficient manner.

---

## 📜 License
Distributed under the MIT License. See `LICENSE.md` for more information.
--- 
