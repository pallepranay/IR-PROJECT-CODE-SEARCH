import requests
from bs4 import BeautifulSoup
import pandas as pd

def getTags(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    tags = soup.find_all("a")
    href = [tags.get("href") for tags in tags]
    href = [i for i in href if ".c.php" in i]
    return href

def getCodes(links):
    codes = []
    for link in links:
        print(links.index(link), link)
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        code = soup.find_all("code")
        code = [i.text for i in code]
        for i in code:
            codes.append(i)
    return codes

def main():
    links = ['https://code2care.org/c-programming/c_programs_66_to120.php' ,'https://code2care.org/c-programming' ]
    codes = []
    for link in links:
        codes.extend(getCodes(getTags(link)))
    df = pd.DataFrame(codes)
    df.to_csv("codes2.csv")
    
if __name__ == "__main__":
    main()

    
    
