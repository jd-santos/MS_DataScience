# For this assignment we are scraping our prof's site and exporting the results to CSV:
    # CSV 1: id, model, product_size, color, battery, storage, network, OS
    # CSV 2: id, model, camera_front
    # CSV 3: id, model, camera_back

# Assignment is unfinished, the CSVs are created but not populated
    # I struggled to reorder items with the same class names
        # Missing some loop logic that would make my arrays work
    # The first time the basic scraper segment of this ran was exciting though! 

# Import libraries
import requests as r
from bs4 import BeautifulSoup
import csv

# URL for our target site to scrape
urltoget = 'http://drd.ba.ttu.edu/2020c/isqs6339/hw1/index.php'

# Filepath and names for CSVs 
filepath = '/Users/jdmini/Library/Group Containers/D75L7R8266.com.reinvented.KeepIt/Keep It/Files/MS_DataScience/Business Intelligence/Assignments/'
csv1_name = 'hw1_out1.csv'
csv2_name = 'hw1_out2.csv'
csv3_name = 'hw1_out3.csv'

# Start with simple get request of URL
# Store in 'res'
res = r.get(urltoget)

# Check the status code
res.status_code

# Create Soup object of BeautifulSoup
soup = BeautifulSoup(res.content, 'lxml')

# We need to scrape the table, but there is a sneaky second table in the footer
# Instead we start with the div
mobdiv = soup.find('div', attrs={'id' : 'mobindex'})

# Now we can search the div for the table
mobindex = mobdiv.find('table')

# Get the rows from the table
mob_index_row = mobindex.find_all('tr')

# Get the cells from the row
for row in mob_index_row:
    mob_index_cell = row.find_all('td')

    # If statement checks for header row
    # Extra row is from blank row in the table, possibly filter later
    if len(mob_index_cell) != 0:
        print("Model:   " + mob_index_cell[0].text)
        print("Color:   " + mob_index_cell[1].text)
        print("OS:   " + mob_index_cell[2].text)

# I legitimately did not execute the code until this point
# It was harrowing 

        # GET URL from the first column of each row, store as infopage
        infopage = r.get(urltoget + '/' + mob_index_cell[0].find('a')['href'])
        # Create soup object of info pages
        pagesoup = BeautifulSoup(infopage.content,'lxml')

    # Open CSV files in write mode
        with open(filepath + csv1_name, 'w', encoding='utf-8-sig') as csv1:
            with open(filepath + csv2_name, 'w', encoding='utf-8-sig') as csv2:
                with open(filepath + csv3_name, 'w', encoding='utf-8-sig') as csv3:

                    # Create three CSV files, write first row of column headings
                    csv1datawriter = csv.writer(csv1, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                    csv1datawriter.writerow(['id', 'Model', 'Product_size', 'Color', 'Battery', 'Storage', 'Network', 'OS'])
                
                    csv2datawriter = csv.writer(csv2, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                    csv2datawriter.writerow(['id', 'Model', 'Camera_Front'])
                
                    csv3datawriter = csv.writer(csv3, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                    csv3datawriter.writerow(['id', 'Model', 'Camera_Back'])
                    
                    # Find all spans with class of 'val' inside of divs with id 'PhoneInfo'
                    # Save these into 'info'
                    infodiv = pagesoup.find_all('div', attrs={'id' : 'PhoneInfo'})
                    
                    # Things go downhill from here
                    # Please turn back for your own sake
                    for info in infodiv:
                        info.find_all('span', attrs={'class' : 'val'})

                    # There should definitely be another loop somewhere around here

                    # My best attempt at trying to pass in the values, this should probably be a loop
                        csv1datawriter.writerow([
                            info[0].text,
                            info[1].text,
                            info[2].text,
                            info[3].text,
                            info[6].text,
                            info[7].text,
                            info[8].text,
                            info[9].text
                        ])
                        # Should pull the UL elements out of info[4] and info[5]
                        # Couldn't figure out how to access these in time
                        csv2datawriter.writerow([
                            info[0].text,
                            info[1].text,
                            info[4].text
                        ])
                        # What if the real unordered lists were the friends we made along the way? 
                        csv3datawriter.writerow([
                        info[0].text,
                        info[1].text,
                        info[5].text
                    ])
