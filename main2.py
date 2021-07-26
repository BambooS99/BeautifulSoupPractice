from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file: 
    content = html_file.read()            
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div',class_='card') #searches for each div with the class card. remember to put underscore after card, not to conflate with py syntax 
    for course in course_cards:
        course_name = course.h5.text #this will store the h1 text within each iteration the program runs through
        course_price = course.a.text.split()[-1] #this will gather the a  tags and also return the final element or piece of text

        print(f'{course_name} costs {course_price}')