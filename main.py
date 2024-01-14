import feedparser
import sqlite3
import html
import re
from datetime import datetime
from email.utils import parsedate_tz, mktime_tz

# ------------------------------
# RSS Feed URLs
# ------------------------------
COINDESK_RSS_URL = 'https://www.coindesk.com/arc/outboundfeeds/rss/'
DEFIANT_RSS_URL = 'https://thedefiant.io/feed/'
INVESTING_RSS_URL = 'https://www.investing.com/rss/news_301.rss'
BITCOINMAGAZINE_RSS_URL = 'https://bitcoinmagazine.com/feed'
DECRYPT_RSS_URL = 'https://decrypt.co/feed'
CRYPTOSLATE_RSS_URL = 'https://cryptoslate.com/feed'
CRYPTO_BRIEFING_RSS_URL = 'https://cryptobriefing.com/feed'
CRYPTO_NEWS_RSS_URL = 'https://cryptonews.com/feed/'
BITCOINIST_RSS_URL = 'https://bitcoinist.com/feed'
THE_BLOCKCHAIN_RSS_URL = 'https://www.the-blockchain.com/feed'
NEWSBTC_RSS_URL = 'https://www.newsbtc.com/feed'  # NewsBTC RSS URL
BITCOIN_NEWS_RSS_URL = 'https://news.bitcoin.com/feed'  # Bitcoin News RSS URL

# ------------------------------
# Database Setup
# ------------------------------
DATABASE_PATH = 'central_rss_articles.db'
def setup_database():
    """Sets up the database for storing articles."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            title TEXT,
            link TEXT PRIMARY KEY,
            description TEXT,
            publication_date TEXT,
            content_url TEXT,
            sent_to_discord BOOLEAN DEFAULT 0,
            source TEXT
        )
    ''')
    conn.commit()
    conn.close()

# ------------------------------
# Data Formatting Functions
# ------------------------------
def format_pub_date(pub_date_str):
    """Formats the publication date to a sortable format."""
    #Date is in this format: Fri, 12 Jan 2024 13:47:21 +0000
    try:
        return datetime.strptime(pub_date_str, '%a, %d %b %Y %H:%M:%S %z').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return None
    
def format_defiant_pub_date(pub_date_str):
    """Formats the publication date for The Defiant's feed."""
    #Date is in this format: Tue, 12 Dec 2023 14:27:00 GMT
    try:
        # Convert to datetime object, considering the timezone
        time_tuple = parsedate_tz(pub_date_str)
        dt = datetime.fromtimestamp(mktime_tz(time_tuple))
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        return 'Unknown'

def clean_html(raw_html):
    """Removes HTML tags and decodes HTML entities."""
    # Using regular expressions to remove HTML tags
    tag_free = re.sub('<.*?>', '', raw_html)
    # Decoding HTML entities
    decoded = html.unescape(tag_free)
    return decoded
# ------------------------------    
# ------------------------------
# RSS Feed Fetching Functions
# ------------------------------
# ------------------------------
def fetch_and_store_coindesk_rss_feed():
    """Fetches RSS feed from Coindesk and stores articles in the database."""
    feed = feedparser.parse(COINDESK_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_pub_date(entry.published)
        content_url = entry.get('media_content', [{}])[0].get('url', 'No Image')

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Coindesk'))

    conn.commit()
    conn.close()

def fetch_and_store_defiant_rss_feed():
    """Fetches RSS feed from The Defiant and stores articles in the database."""
    feed = feedparser.parse(DEFIANT_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_defiant_pub_date(entry.get('published', 'Unknown'))
        thumbnail_url = entry.get('media_thumbnail', [{}])[0].get('url', 'No Image')

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, thumbnail_url, False, 'The Defiant'))

    conn.commit()
    conn.close()

def fetch_and_store_investing_rss_feed():
    """Fetches RSS feed from Investing and stores articles in the database."""
    feed = feedparser.parse(INVESTING_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        publication_date = datetime.strptime(entry.published, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        content_url = entry.enclosures[0].href if entry.enclosures else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, '', publication_date, content_url, False, 'Investing.com'))

    conn.commit()
    conn.close()

def fetch_and_store_bitcoinmagazine_rss_feed():
    """Fetches RSS feed from Bitcoin Magazine and stores articles in the database."""
    feed = feedparser.parse(BITCOINMAGAZINE_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_defiant_pub_date(entry.published)        
        content_url = entry.enclosures[0].url if entry.enclosures else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Bitcoin Magazine'))

    conn.commit()
    conn.close()

def fetch_and_store_decrypt_rss_feed():
    """Fetches RSS feed from Decrypt.co and stores articles in the database."""
    feed = feedparser.parse(DECRYPT_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_pub_date(entry.published)
        content_url = entry.enclosures[0].url if entry.enclosures else 'No Image'
        
        cursor.execute('''
        INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Decrypt'))

    conn.commit()
    conn.close()

def fetch_and_store_cryptoslate_rss_feed():
    """Fetches RSS feed from CryptoSlate and stores articles in the database."""
    feed = feedparser.parse(CRYPTOSLATE_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link        
        description = clean_html(entry.description)        
        pub_date = format_pub_date(entry.published)
        content_url = entry.enclosures[0].url if entry.enclosures else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'CryptoSlate'))

    conn.commit()
    conn.close()

def fetch_and_store_crypto_briefing_rss_feed():
    """Fetches RSS feed from Crypto Briefing and stores articles in the database."""
    feed = feedparser.parse(CRYPTO_BRIEFING_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_pub_date(entry.published)
        # Extract content_url from media:content tag
        content_url = entry.media_content[0]['url'] if 'media_content' in entry and len(entry.media_content) > 0 else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Crypto Briefing'))

    conn.commit()
    conn.close()

def fetch_and_store_crypto_news_rss_feed():
    """Fetches RSS feed from Crypto News and stores articles in the database."""
    feed = feedparser.parse(CRYPTO_NEWS_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = clean_html(entry.description)
        pub_date = format_pub_date(entry.published)
        content_url = entry.enclosures[0].url if entry.enclosures else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Crypto News'))

    conn.commit()
    conn.close()

def fetch_and_store_bitcoinist_rss_feed():
    """Fetches RSS feed from Bitcoinist and stores articles in the database."""
    feed = feedparser.parse(BITCOINIST_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = entry.description
        pub_date = format_pub_date(entry.published)
        content_url = entry.media_content[0]['url'] if 'media_content' in entry and len(entry.media_content) > 0 else 'No Image'

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Bitcoinist'))

    conn.commit()
    conn.close()

def fetch_and_store_the_blockchain_rss_feed():
    """Fetches RSS feed from The Blockchain and stores articles in the database."""
    feed = feedparser.parse(THE_BLOCKCHAIN_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = clean_html(entry.description)
        pub_date = format_pub_date(entry.published)
        content_url = feed.feed.image.url

        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'The Blockchain'))

    conn.commit()
    conn.close()

def fetch_and_store_newsbtc_rss_feed():
    """Fetches RSS feed from NewsBTC and stores articles in the database."""    
    feed = feedparser.parse(NEWSBTC_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        description = clean_html(entry.description)
        first_sentence = description.split('.')[0] if '.' in description else description
        description = first_sentence
        pub_date = format_pub_date(entry.published)
        # Extract the content URL from the media:content tag
        media_content = entry.get('media_content', [])
        if media_content:
            content_url = media_content[0]['url']
        else:
            content_url = 'No Image'
        
        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'NewsBTC'))

    conn.commit()
    conn.close()

def fetch_and_store_bitcoin_news_rss_feed():
    """Fetches RSS feed from Bitcoin News and stores articles in the database."""
    feed = feedparser.parse(BITCOIN_NEWS_RSS_URL)
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        # Extracting the content URL from the 'description' tag
        content_url = 'No Image'
        description = entry.description
        match = re.search(r'src="([^"]+)"', description)
        if match:
            content_url = match.group(1)

        description = clean_html(entry.description)
        pub_date = format_pub_date(entry.published)  
        
        cursor.execute('''
            INSERT OR IGNORE INTO articles (title, link, description, publication_date, content_url, sent_to_discord, source)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (title, link, description, pub_date, content_url, False, 'Bitcoin News'))

    conn.commit()
    conn.close()
# ------------------------------
# Main Function
# ------------------------------
def main():
    setup_database()
    fetch_and_store_coindesk_rss_feed()
    fetch_and_store_defiant_rss_feed()
    fetch_and_store_investing_rss_feed()
    fetch_and_store_bitcoinmagazine_rss_feed()
    fetch_and_store_decrypt_rss_feed()
    fetch_and_store_cryptoslate_rss_feed()
    fetch_and_store_crypto_briefing_rss_feed()
    fetch_and_store_crypto_news_rss_feed()
    fetch_and_store_bitcoinist_rss_feed()
    fetch_and_store_the_blockchain_rss_feed()
    fetch_and_store_newsbtc_rss_feed()
    fetch_and_store_bitcoin_news_rss_feed()    

if __name__ == '__main__':
    main()
