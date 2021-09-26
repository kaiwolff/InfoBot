from bs4 import BeautifulSoup
import requests
import json

class VulnScraper(): 

    def scrape_mitre(self,search_term):
        cve_list = []
        description_list = []
        page_list = []
        

        getpage = requests.get("https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=" + search_term)
        
        getpage_soup = BeautifulSoup(getpage.text, 'html.parser')
        info = getpage_soup.find("div",{"id":"TableWithRules"})
        for i in info.findAll("td"):
            #print(i.text)
            page_list.append(i.text)
        

        #As shown by Tyree, need to encase this in try-except to catch issue with low number of vulns
        counter = 0
        try:
            
            for item in page_list:
                while counter <10:
                    #use while loop to limit to 5 response and prevent spam
                    #Even numbers are CVE numbers, odd numbers are descriptions
                    cve_list.append(page_list[counter])
                    counter +=1
                    description_list.append((page_list[counter])[:280])
                    counter +=1
            
            return cve_list, description_list
        except IndexError:
            return cve_list,description_list


if __name__ == "__main__":
    import os

    scraper = VulnScraper()
    response = scraper.scrape_mitre("Windows 10")
    print(response)
    counter = 0
    for item in response[0]:
        print(item, response[1][counter])
        counter +=1