from robobrowser import RoboBrowser
import time
import pygsheets
from datetime import datetime

parser = 'html.parser'

desktop_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47'
mobile_agent = 'Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36'

# if you wana check keyword from mobile agent replace desktop_agent with mobile_agent
def keyword_tracker(keyword, total_count, sites):
    browser = RoboBrowser(history = False, user_agent = desktop_agent, parser = parser)
    browser.open(f"https://www.google.com/search?num={total_count}&q={keyword}")
    
    time.sleep(0.5)
    
    top_ads = browser.select(".qGXjvb .qzEoUe.NVWord")
    no_ads = browser.select(".TbwUpd.NJjxre cite")
    bottom_ads = browser.select("#bottomads .qzEoUe.NVWord")
    
    links = []
    links.extend(top_ads)
    links.extend(no_ads)
    links.extend(bottom_ads)
    
    result = []
    
    for i in range(len(sites)):
        result.append({"site": sites[i], "index": 0})
    
    index = 0;
    for i in range(len(links)):
        for j in range(len(sites)): 
            if links[i].get_text().lower().find(sites[j].lower()) != -1:
                index = i + 1
                if result[j]["index"] == 0:
                    result[j]["index"] = [index]
                else:
                    result[j]["index"].append(index)
    
    has_ads = len(top_ads) + len(bottom_ads) != 0
    return has_ads, result



keywords = open("keywords.txt","r", encoding="utf=8").read().split("\n")
sites = open("website.txt","r", encoding="utf=8").read().split("\n")

# Your json file path
gc = pygsheets.authorize(service_file='Your json file path')

# The name of the Google Sheet where you want the data to be stored 
sh = gc.open('google sheet name')


wks = sh[0]


for i in range(len(keywords)):
    print(f"\b\r{int((i/len(keywords))*100)}",end="%")
    wks.update_value((i+2,1), keywords[i])    

    # if you want search more than 20 results edit line below
    has_ads, res = keyword_tracker(keywords[i],20,sites)

    for j in range(len(sites)):
        index = res[j]["index"]
        if index == 0 :
            wks.update_value((i+2, j+2), "Not found")
        else:
            wks.update_value((i+2, j+2), f"{index[0]}")

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")
wks.update_value((1, 3), f"{current_time}")

print(f"\b\r{100}",end="% successfully completed")


