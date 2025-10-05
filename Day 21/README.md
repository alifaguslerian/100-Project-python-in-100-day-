<h1 align="center">🌐 Day 21 - Wikipedia Content Scraper</h1>

<p align="center">
  A Python script that scrapes and extracts useful information from Wikipedia articles — including title, summary, headings, and related links — using <b>urllib</b>, <b>regex</b>, and a custom <b>HTML parser</b>.
</p>

---

## 📖 About the Project
This project is part of my **100 Days of Python Projects Challenge**.  
The goal of this project is to explore how web scraping works without relying on third-party libraries like BeautifulSoup or Requests-HTML.  
Instead, it uses **Python’s built-in modules**: `urllib`, `re`, and `html.parser` to fetch and parse Wikipedia pages.

---

## 🚀 Features
✅ Fetches Wikipedia article content directly from the web  
✅ Extracts the page **title** and **summary paragraphs**  
✅ Detects **headings (H2 sections)** using regex  
✅ Finds up to 5 **related Wikipedia links**  
✅ Handles invalid topics or connection errors gracefully  

---

Run with:
   ```bash
   python main.py
