import requests as r
from bs4 import BeautifulSoup

#base URL
urltoget = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.1/gamers'

#Let's request hte base URL
res = r.get(urltoget)

res.status_code

#Soup Object 
soup = BeautifulSoup(res.content,'lxml')

#Let's find the table.  Note, there is only 1 table so this works well.  
#Similar to other options using a div with an ID attribute.
results = soup.find("table")

#Now, let's find all rows within the table
rowresults = results.find_all("tr")

#Now, let's iterate on all the rows within the table.  Note, if you wanted to 
#write this to a csv file rather than the console, you would want to open your 
#file handle prior to this loop
for row in rowresults:
    #Locate the cells in the row
    cells = row.find_all("td")
    #This checks to see if we have a header row.  Notice the first row of the
    #table is using <th> instead of <td> tags.  
    if len(cells) != 0:
        #Access the data.  Note, the cells[#] syntax.  Since this is an array
        #I can reference it as such.  In other examples, these may be spans
        #where you could search by id, or any of another form of tags.  
        print('\n*************PLAYER INFO************\n')
        print("GCode:  " + cells[0].text)
        print("Handle:  " + cells[1].text)
        print("Aggregated Score:  " + cells[2].text)
        print(cells[3].find('a')['href'])
        #print("Profile URL:  " + urltoget + '/' +  cells[3].find('a')['href'])
        
        #Here I have written a function to get the information for the sub page.  
        #In the event you wanted to write this to a csv, you would likely not 
        #use a function, but would instead do the steps you see in the function
        #here within the loop.  Also notice, that I concatenate the urltoget
        #with the value for the href.  This is because the URL is not the full
        #url to the page.  
        #GetProfile(urltoget + '/' + cells[3].find('a')['href'])
        prof = r.get(urltoget + '/' + cells[3].find('a')['href'])
        profsoup = BeautifulSoup(prof.content,'lxml')
        
        print('Class:  ' + profsoup.find('span', attrs={'id': 'pclass'}).text)
        print('Role:  ' + profsoup.find('span', attrs={'id': 'prole'}).text)
        
        raids = profsoup.find('fieldset', attrs={'id' : 'Raids'}).find_all('div', attrs={'class' : 'raidcore'})
        print('\nRAID INFORMATION\n  ')
        for raid in raids:
            raidstats = raid.find_all('span', attrs={'class' : 'rdata'})
            print('Raid:  ' + raid.find('h5').text)
            print('Completed:  ' + raidstats[0].text)
            print('DKP Earned:  ' + raidstats[1].text)
            print('Best Rating:  ' + raidstats[2].text)
            print('------------------------------')
            

    
