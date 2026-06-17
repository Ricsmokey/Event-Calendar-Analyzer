import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://thetivolitheatre.com/events/aymt-presents-chitty-chitty-bang-bang/"

response = requests.get(url)
response.encoding = 'utf-8'

print("Status code:", response.status_code)
if response.status_code != 200:
    print(f"Failed to retrieve page: {response.status_code}")
    exit()

soup = BeautifulSoup(response.content, 'html.parser')

# Getting event title

title_tag = soup.find('h1')
show_title = title_tag.text.strip() if title_tag else "N/A"

# Getting all show dates and times

show_dates = []
show_times = []
show_prices = []

date_headers = soup.find_all('h2')
for header in date_headers:
    header_text = header.text.strip()
 
    if any(month in header_text for month in ['MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']):
        
        time_p = header.find_next('p')
        if time_p and 'pm' in time_p.text:
            show_dates.append(header_text)
            show_times.append(time_p.text.strip())
            
            if '£' in time_p.text:
                show_prices.append(time_p.text.strip())
            else:
                next_p = time_p.find_next('p')
                if next_p and '£' in next_p.text:
                    show_prices.append(next_p.text.strip())
                else:
                    show_prices.append("Price not found")

 # Getting matinee info from the main description
 
description = soup.find('p', string=lambda x: x and 'Matinee:' in str(x))
if description:
    matinee_info = description.text.strip()
else:
     
    for p in soup.find_all('p'):
        if 'Matinee:' in p.text:
            matinee_info = p.text.strip()
            break
        else:
            matinee_info = "No matinee information found"


price_range = "N/A"
for element in soup.find_all(['p', 'div', 'span']):
    if element.text and '£' in element.text and ('-' in element.text or 'from' in element.text.lower()):
        price_range = element.text.strip()
        break

print(f"\nEvent Title: {show_title}")
print(f"Matinee Info: {matinee_info}")
print(f"Price Range: {price_range}")
print(f"\nIndividual Shows Found: {len(show_dates)}")
for i in range(len(show_dates)):
    print(f"  • {show_dates[i]}: {show_times[i]} - {show_prices[i] if i < len(show_prices) else 'Price not found'}")

data = []
for i in range(len(show_dates)):
    data.append({
        "Event Title": show_title,
        "Date": show_dates[i],
        "Time": show_times[i] if i < len(show_times) else "N/A",
        "Price": show_prices[i] if i < len(show_prices) else "N/A",
        "Matinee Info": matinee_info,
        "Overall Price Range": price_range
    })

df = pd.DataFrame([data])
df.to_csv("the_events_scraped.csv", index=False)

print(f"\nData saved to the_events_scraped.csv with {len(data)} records")
