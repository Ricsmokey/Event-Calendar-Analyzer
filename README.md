# The Calendar Navigator 

A Python web scraper that navigates through an interactive calendar to collect all available showtimes for **Masquerade NYC** — a theater experience. It automatically collects all available and limited show dates and exports a CSV dataset.

---

## What It Does

- Navigates through 6 months of an interactive calendar automatically
- Collects all show dates with **Limited** availability
- Collects all show dates with **Good** availability
- Prints a clean and sorted final list of all shows

---

## Target Website

https://masqueradenyc.com/buy-tickets/

---

## Tech Stack

- Python 
- BeautifulSoup4
- Pandas

## Project Structure
```
Event-Calendar-Analyzer/
│
├── Event scraper.py
├── the_events_scraped.csv
└── README.md
```
### Install dependencies

```bash
pip install pandas
pip install beautifulSoup4
```

---

## How to Run

```bash
git clone https://github.com/Ricsmokey/Event-Calendar-Analyzer.git
cd Event-Calendar-Analyzer
pip install beautifulsoup4 pandas
python "Event scraper.py"
```

---

## Example Output

```
Scraping Masquerade - Buy Tickets...

LIMITED DATES (21 shows):
  • March 27
  • March 28
  ...

AVAILABLE SHOWS (72 shows):
  • May 06
  • May 12
  ...

ALL SHOWS (69 total):
  • March 27
  • March 28
  ...
```

---

## How It Works

1. Requests to access the url
2. Visits the Masquerade NYC ticket page
3. Waits for the calendar to fully load
4. Scrapes all Limited and Available dates from the current month
5. Clicks the "Next" button to move to the following month
6. Repeats steps 4–5 for up to 6 months
7. Duplicates and prints the final results

---

## Author

**Akorede Kareem** — [github.com/Ricsmokey](https://github.com/Ricsmokey)


