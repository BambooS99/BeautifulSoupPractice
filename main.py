from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: #this will read the HTML file. 1) specify the target, 2) r command allows us to read
    content = html_file.read()            #this will execute the reading option  
    
    
    soup = BeautifulSoup(content, 'lxml') #the type of content chosen is lxml, aka string within our previously defined content, the HTML file
    anchor_html_tags = soup.find_all('a')                #this will search for all h5 tags in the document
    for anchor in anchor_html_tags:                    
        print(anchor.text)
#this could be transferred to a DB and stored into a file
#another idea, this could be used for tweets/fb posts/ any social post to gather onto a single page 
