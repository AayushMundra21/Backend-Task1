import requests
import csv
from bs4 import BeautifulSoup
#print(ab)
'''name=soup.find_all('a')
print(name)
for link in name:
    if 'CV' in link.text:
        print(link)
        print(link.attrs['href'])'''
#file=open("D:data3.txt","w")
#file.write(a)
#file.close
urls=[]
count = 0
for i in range (1,12):
    URL='https://www.myvisajobs.com/CV/Candidates.aspx?P='+str(i)
    page= requests.get(URL)
    html=page.content
    soup=BeautifulSoup(html,'html.parser')
    ab=soup.prettify()
    for b_tag in soup.find_all("b"):
        a_tag = b_tag.find('a')
        urls.append('https://www.myvisajobs.com'+a_tag.attrs['href'])
for i in range (0,4):
    urls.pop()
#print (urls)
#print(len(urls))
a=[['SN','name','degree','careerlevel','skills']]
for url in urls:
    single_user = []
    count=count+1
    page1 = requests.get(url)
    html1 = page1.content
    soup1 = BeautifulSoup(html1,'html.parser')
    try:
        name = soup1.body.find("span", itemprop="name").text
    except:
        name = 'NA'
    image = "https://www.myvisajobs.com" + soup1.body.find("img",
            itemprop="photo")['src']
    filename = name +'.jpeg'
    try:
        r = requests.get(image, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    except:
        filename= name+'-1'+'.jpeg'
        r = requests.get(image, allow_redirects=True)
        open(filename, 'wb').write(r.content)
    try:
        degree = soup1.body.find('td', text='Degree: ').find_next('td').text
    except:
        degree = 'NA'
    try:
        career_level = soup1.body.find('td', text='Career Level: ').find_next('td').text
    except:
        career_level = 'NA'
    try:
        skills = soup1.body.find('td', text='Skills: ').find_next('td').text
    except:
        skills='NA'
    try:
        goal = soup1.body.find('td', text='Goal: ').find_next('td').text
    except:
        goal = 'NA'
    try:
        membership = soup1.body.find('td', text='Membership: ').find_next('td').text
    except:
        membership = 'NA'
    try:
        certification = soup1.body.find('td', text='Certification: ').find_next('td').text
    except:
        certification = 'NA'
    single_user.append(count)
    single_user.append(name)
    single_user.append(degree)
    single_user.append(career_level)
    single_user.append(skills)
    single_user.append(goal)
    single_user.append(membership)
    single_user.append(certification)
    a.append(single_user)
    print (single_user)
print(a)
with open('D:temp.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(a)
