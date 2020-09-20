import requests as r
from bs4 import BeautifulSoup
import csv

#base URL
urltoget = 'http://drd.ba.ttu.edu/isqs6339/ex/l1.1/gamers'
#change FP to match your directory.
fp = '/home/isqsdac/Desktop/'
filename1 = 'file1.csv'
filename2 = 'file2.csv'
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

with open(fp + filename1, 'w') as file1:
    with open(fp + filename2, 'w') as file2:
        file1datawriter = csv.writer(file1, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        file1datawriter.writerow(['gcode', 'handle', 'agg_score', 'class', 'role'])
        file2datawriter = csv.writer(file2, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        file2datawriter.writerow(['gcode', 'raid', 'completed', 'dkp_earned', 'best_rating'])  
        
        for row in rowresults:
            #Locate the cells in the row
            cells = row.find_all("td")
            #This checks to see if we have a header row.  Notice the first row of the
            #table is using <th> instead of <td> tags.  
            if len(cells) != 0:

                prof = r.get(urltoget + '/' + cells[3].find('a')['href'])
                profsoup = BeautifulSoup(prof.content,'lxml')               

                
                file1datawriter.writerow([cells[0].text, 
                                          cells[1].text, 
                                          cells[2].text, 
                                          profsoup.find('span', attrs={'id': 'pclass'}).text, 
                                          profsoup.find('span', attrs={'id': 'prole'}).text])
                
                raids = profsoup.find('fieldset', attrs={'id' : 'Raids'}).find_all('div', attrs={'class' : 'raidcore'})

                for raid in raids:
                    raidstats = raid.find_all('span', attrs={'class' : 'rdata'})
                    file2datawriter.writerow([cells[0].text, 
                                              raid.find('h5').text, 
                                              raidstats[0].text, 
                                              raidstats[1].text, 
                                              raidstats[2].text]) 

            

    
