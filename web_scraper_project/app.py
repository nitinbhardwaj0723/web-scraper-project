import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_website(url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Website Title
 
        title = soup.title.text.strip() if soup.title else "No title found"

        print("\n" + "=" * 50)
        print("🌐 WEBSITE TITLE")
        print("=" * 50)
        print(title)

        # Headings

        headings = []
        for tag in soup.find_all(["h1", "h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headings.append(text)

        print("\n" + "=" * 50)
        print("📰 HEADINGS FOUND")
        print("=" * 50)
        if headings:
            for i, h in enumerate(headings, 1):
                print(f"{i}. {h}")
        else:
            print("No headings found.")

        # Paragraphs

        paragraphs = []
        for p in soup.find_all("p"):
            text = p.get_text(strip=True)
            if text:
                paragraphs.append(text)

        print("\n" + "=" * 50)
        print("📄 PARAGRAPHS FOUND")
        print("=" * 50)
        if paragraphs:
            for i, p in enumerate(paragraphs[:10], 1):  # sirf first 10 print
                print(f"{i}. {p[:150]}...")
        else:
            print("No paragraphs found.")

        # Save Title separately

        with open("title.txt", "w", encoding="utf-8") as f:
            f.write(title)

        # Save Headings to CSV

        df_headings = pd.DataFrame({"Headings": headings})
        df_headings.to_csv("headings.csv", index=False, encoding="utf-8")

        # Save Paragraphs to CSV

        df_paragraphs = pd.DataFrame({"Paragraphs": paragraphs})
        df_paragraphs.to_csv("paragraphs.csv", index=False, encoding="utf-8")

        print("\n" + "=" * 50)
        print("✅ DATA SAVED SUCCESSFULLY")
        print("=" * 50)
        print("1. title.txt")
        print("2. headings.csv")
        print("3. paragraphs.csv")

    except requests.exceptions.RequestException as e:
        print("❌ Error fetching website:", e)
    except Exception as e:
        print("❌ Something went wrong:", e)


# Main Program

if __name__ == "__main__":
    print("🔍 PYTHON WEB SCRAPER")
    print("-" * 50)

    url = input("Enter website URL (example: https://example.com): ").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        url = "https://" + url

    scrape_website(url)
