# get a tags from a link beautify soup
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

# iterate over links and get codes from each link and store in a list 
def getCodes(links):
    codes = []
    for link in links:
        # print link with counter
        print(links.index(link), link)
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html.parser")
        code = soup.find_all("code")
        code = [i.text for i in code]
        # print(len(code))
        # destructure code and append to codes
        for i in code:
            codes.append(i)
    return codes

# print(len(getCodes(getTags("https://code2care.org/c-programming/"))))
# get codes and make a csv file with pandas
def main():
    links = ['https://code2care.org/c-programming/c_programs_66_to120.php' ,'https://code2care.org/c-programming' ]
    # build a list of codes from links and store in a single csv file
    codes = []
    for link in links:
        codes.extend(getCodes(getTags(link)))
    df = pd.DataFrame(codes)
    df.to_csv("codes2.csv")
    
    
    
    # links = getTags("https://code2care.org/c-programming/")
    # codes = getCodes(links)
    # df = pd.DataFrame(codes)
    # df.to_csv("codes1.csv")
    
if __name__ == "__main__":
    main()
    
# getCodes(getTags("https://code2care.org/c-programming/")[:1])

# links = getTags("https://code2care.org/c-programming/")

# def getCode(link):
#     r = requests.get(link)
#     soup = BeautifulSoup(r.text, "html.parser")
#     code = soup.find_all("code")
#     code = [i.text for i in code]
#     return code

# #  iterate over links and get codes from each link and store in a list
# def getCodes(links):
#     codes = []
#     for link in links:
#         code = getCode(link)
#         codes.append(code)
#     return codes

# codes = getCodes(links[])


# import pandas as pd

# def getCodes(links):
#     codes = []
#     for link in links:
#         code = getCode(link)
#         codes.append(code)
#     return codes

# def main():
#     links = getTags("https://code2care.org/c-programming/")
#     codes = getCodes(links)
#     df = pd.DataFrame(codes)
#     # df.to_csv("codes.csv")
    
    
# if __name__ == "__main__":
#     main()
    
    
