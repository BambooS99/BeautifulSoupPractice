from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
jobs = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx') #using find instead of find_all will bring us the first match
company_name = jobs.find('h3', class_ = 'joblist-comp-name').text.replace(' ','')
skills2 = jobs.find('span', class_ = 'srp-skills').text.replace(' ','').replace(',',', ')

print(company_name)
print(skills2)