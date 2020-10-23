# 1 Intro to Web Scraping and Ethics
## Overview
- Web scraping: Downloading and parsing data from the web
	- Scraping applies to getting data directly off a site and doesn't include the use of APIs
		- Most websites do not have APIs or they will cost money
	- Web scraping essentially simulates a browser in code
- Multiple steps:
	- Accessing data
	- Downloading data
	- Parsing
	- Extracting value
### Web Browser Process
- When user types in URL:
	- Browser resolves the URL to an IP address
	- IP identifies the host server, where the content is actually hosted
	- The browser makes a REQUEST to the server for a page
	- Server does some work and sends back HTML and CSS
- Browser begins parsing the HTML and CSS for viewing
	- May be prompted for scripting libraries or other files
		- If so, make another request for the assets
- Render page to user
## Ethics and Legal Concerns
- Why do ethics matter?
	- Livelihood
	- Brand
		- How much can you be trusted
	- Trust is difficult to regain
- Data scientists have a duty to safeguard any data that is collected
### Legal Items
- Can we use all data that is publicly available? 
- Some data is protected by law
	- FERPA
		- Who has access to academic data and records in a college setting
	- HIPAA
		- Pertains to medical/health data
	- GDPR
		- European law pertaining to data privacy in the EU
- Does secure access grant me the right to 'pass on' data? 
	- Secure access = paid data
	- Check the TOS to see if you can share it to nonpaying customers
- Check if TOS grants free usage of all data you can access
	- Could affect your access to the website
### Usable Data from a Site
- Check the Terms of Service (TOS)
- Examine the Robot.txt file
	- Identifies the pages the site wants cached by a search engine
	- Can also be Robots.txt
- Public vs secured area of the site
	- If you've paid for access to an area of a site
- Does the site require payment to access site API? 
	- E.g. Twitter
	- If you're scraping more than the API would give, you may be in TOS violation
### Being a Good Citizen
- Making one vs one million requests per second
	- Don't hammer a site or your access could be banned or worse
	- Technically this is a DoS attack
- Denial-of-Service Attack
	- Technique used to bring down web servers by overloading the server with requests
	- Classified as a cyber attack
	- Avoid people in suits at your door because you wrote bad code
## Throttling and Timing
- Review: Web scraping requires a programmatic request for data to a server
- Goals: Gather data without
	- Causing a DoS attack
	- Hindering the site's ability to function
	- Having our account/IP banned or blocked
- Two limiting techniques: throttling and timing
### Throttling
- Limiting the request intervals
- Equate to simulating a user
	- Users don't read a full page in a second
	- They don't click on a link exactly every two seconds
- Avoid **parallelism** in requests
	- Requests coming from the same IP
	- Doing two or more page requests simultaneously
	- Normal users make serial requests
- Set an interval between requests 
	- For large pulls: 4-6 seconds between requests 
- Vary your requests
	- Add a random interval to your set intervals
	- Jitter
		- Random variation you can apply to your intervals
#### Throttling Example:
- Total pages to parse: 100
- Standard interval between requests: 4 seconds
- Request method: Serial
- Random jitter: 0 to 1.5 seconds
- Time to pull all pages: 400-550 seconds
### Timing
- Limiting when we make requests 
- When the scrape is initiated
	- Ideally you time for the website's non-peak hours 
- Understand the type of business and think about when the load on the site is likely the lowest
- If not possible:
	- Adjust throttling
	- Increase your base request interval
	- Increase your jitter
- Remember the goal is to not hinder the site from doing business 
## A Basic Scraper
### Overview
- Python can be used to download and parse HTML data
- Scraping
	- Downloading a page then extracting data
- Crawling
	- Automated scraping
	- Typically following all links after scraping and scraping those as well
	- Throttling and timing tend to matter more for crawling than scraping
- Requests data can be in multiple formats
	- Text/HTML: Standard content
	- Image/JPEG: Image format 
	- Application/JSON: JSON data format
	- Understanding the format will aid in parsing
- **HTML Response Codes**
	- Returned by the server
	- Identifies the outcome of the request
	- Common codes:
		- 200: Request OK
		- 301: Redirect
		- 400: Bad Request
		- 403: Forbidden (need authentication)
		- 404: Not found
		- 500: Server error
	- 