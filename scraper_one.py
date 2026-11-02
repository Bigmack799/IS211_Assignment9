# IS 211 - Week 9 Assignment
# Script 1: NASA Human Spaceflight Programs
# Source: https://en.wikipedia.org/wiki/List_of_NASA_missions

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# Website containing the NASA mission information
url = "https://en.wikipedia.org/wiki/List_of_NASA_missions"

# Request the webpage
request = Request(
    url,
    headers={"User-Agent": "IS211EducationalScraper/1.0 (student project)"}
)

try:
    with urlopen(request, timeout=20) as response:
        html = response.read()

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(html, "lxml")

    # Find the table containing NASA human spaceflight programs
    nasa_table = None

    for table in soup.find_all("table"):
        headers = [
            th.get_text(" ", strip=True)
            for th in table.find_all("th")
        ]

        if "Program" in headers and "Start date" in headers:
            nasa_table = table
            break

    if nasa_table is None:
        print("NASA human spaceflight table not found.")

    else:
        print("=" * 95)
        print("NASA HUMAN SPACEFLIGHT PROGRAMS")
        print("=" * 95)

        print(
            f"{'Program':<32}"
            f"{'Start':<10}"
            f"{'First Flight':<15}"
            f"{'End':<12}"
            f"{'Missions':<10}"
        )

        print("-" * 95)

        mission_count = 0

        for row in nasa_table.find_all("tr"):
            cells = row.find_all("td")

            if len(cells) >= 6:
                values = [
                    cell.get_text(" ", strip=True)
                    for cell in cells
                ]

    # Remove Wikipedia footnote markers from mission counts
                import re
                values[4] = re.sub(r"\s*\[[^\]]+\]", "", values[4])

                program = values[0]
                start = values[1]
                first_flight = values[2]
                end = values[3]
                missions = values[4]

                print(
                    f"{program:<32}"
                    f"{start:<10}"
                    f"{first_flight:<15}"
                    f"{end:<12}"
                    f"{missions:<10}"
                )

                mission_count += 1

        print("-" * 95)
        print(f"Total programs found: {mission_count}")
        print(f"Source: {url}")

except Exception as error:
    print(f"An error occurred: {error}")



