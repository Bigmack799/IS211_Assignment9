
# IS 211 - Week 9 Assignment
# Script 2: Renewable Electricity Production by Country
# Source: https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/List_of_countries_by_renewable_electricity_production"

# Retrieve the webpage using HTTP
request = Request(
    url,
    headers={"User-Agent": "IS211EducationalScraper/1.0 (student project)"}
)

try:
    with urlopen(request, timeout=20) as response:
        html = response.read()

    # Parse the webpage using BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # Locate the renewable electricity production table
    energy_table = None

    for table in soup.find_all("table"):
        headers = [
            th.get_text(" ", strip=True)
            for th in table.find_all("th")
        ]

        header_text = " ".join(headers).lower()

        if all(word in header_text for word in
               ["location", "hydro", "wind", "solar"]):
            energy_table = table
            break

    if energy_table is None:
        print("Renewable electricity table not found.")

    else:
        print("=" * 125)
        print("RENEWABLE ELECTRICITY PRODUCTION BY COUNTRY")
        print("Electricity generation measured in terawatt-hours (TWh)")
        print("=" * 125)

        print(
            f"{'Country':<46}"
            f"{'Renewables':>14}"
            f"{'Hydro':>12}"
            f"{'Wind':>12}"
            f"{'Solar':>12}"
            f"{'Year':>10}"
        )

        print("-" * 125)

        country_count = 0

        # Extract individual rows from the table
        for row in energy_table.find_all("tr"):
            cells = row.find_all(["th", "td"])

            if len(cells) != 8:
                continue

            values = [
                cell.get_text(" ", strip=True)
                for cell in cells
            ]

            # Remove Wikipedia footnote references
            values = [
                re.sub(r"\s*\[[^\]]+\]", "", value)
                for value in values
            ]

            country = values[0]
            renewables = values[1]
            hydro = values[2] or "N/A"
            wind = values[3] or "N/A"
            solar = values[4] or "N/A"
            year = values[7]

            # Skip headings and the worldwide summary
            if country.lower() in ("location", "world"):
                continue

            if not re.fullmatch(r"\d{4}", year):
                continue

            print(
                f"{country:<46}"
                f"{renewables:>14}"
                f"{hydro:>12}"
                f"{wind:>12}"
                f"{solar:>12}"
                f"{year:>10}"
            )

            country_count += 1

        print("-" * 125)
        print(f"Total countries/territories found: {country_count}")
        print(f"Source: {url}")

except Exception as error:
    print(f"An error occurred: {error}")
