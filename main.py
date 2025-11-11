from src.scrapper import scrape_hackernews
from src.utils import save_to_excel


if __name__ == "__main__":
    print("Se porneste Hacker News Scrapper")

    df = scrape_hackernews()

    save_to_excel(df)

    print("Datele au fost salvate")

