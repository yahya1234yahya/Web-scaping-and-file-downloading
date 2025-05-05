import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

def main():
    url = "https://www.ncei.noaa.gov/data/local-climatological-data/access/2021/"
    folder_name = "downloads"
    biggest = 0
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        target_date = "2024-01-19 10:27"
        all_text = soup.get_text(separator="\n")
        lines = all_text.splitlines()
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        for i, line in enumerate(lines):
            if target_date in line:
                content = requests.get(url + lines[i -1], stream=True)
                with open(folder_name + "/" + lines[i - 1], "wb") as f:
                    for chunk in content.iter_content(chunk_size=8000):
                        f.write(chunk)
                df = pd.read_csv(folder_name + "/" + lines[i - 1], low_memory=False)
                if "HourlyDryBulbTemperature" in df.columns:
                    df = df.dropna(subset=["HourlyDryBulbTemperature"])
                    df["HourlyDryBulbTemperature"] = pd.to_numeric(df["HourlyDryBulbTemperature"], errors="coerce")
                    max_temp = df["HourlyDryBulbTemperature"].max()
                if (max_temp > biggest):
                    biggest = max_temp
        print(biggest)

                
                    


if __name__ == "__main__":
    main()
