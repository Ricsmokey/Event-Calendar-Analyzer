# The Calendar Navigator 

A Python web scraper that navigates through an interactive calendar to collect all available showtimes for **Masquerade NYC** — an immersive theater experience.

---

## What It Does

- Navigates through 6 months of an interactive calendar automatically
- Collects all show dates with **Limited** availability
- Collects all show dates with **Good** availability
- Prints a clean, deduplicated, and sorted final list of all shows

---

## Target Website

https://masqueradenyc.com/buy-tickets/

---

## Requirements

- Python 3.x
- BeautifulSoup4

### Install dependencies

```bash
pip install pandas
pip install beautifulSoup4
```

---

## How to Run

```bash
python "The Calendar Navigaor.py"
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
7. Deduplicates and prints the final results

---

## Tools Used

- Pandas
- BeautifulSoup4



