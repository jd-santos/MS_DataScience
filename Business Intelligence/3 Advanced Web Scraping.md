## Post Method
### Get Method Review
- Until now we have only been working with GET statements
	- In Get statements data is passed via the URL
	- Benefit is that the resource can be:
		- Cached
		- Bookmarked
		- Save as browser history
	- However it is not very secure
		- ‘Parameters’ are all passed in the URL
### Post vs. Get
- Post statements pass data via the request Header
	- Not shown in the URL
	- A lot of info sent by browser by default
	- Typically seen in webform
		- Data input form with a submit button
- Back buttons do not play nice with Post
- Items are not:
	- Cached
	- Bookmarked
	- Saved in history
		- You can save the URL, but not values passed
### Sync vs Async
- Early web was mostly synchronous
	- You made a request to the site and the entire website was loaded
- Now many sites are asynchronous
	- Only portion of the site loads
- Async requires client side programming
	- Follows the request > response model 
	- Considerations
		- More difficult to find HTML
		- May need to save response.content to file to see HTML
		- Might have to read through other code like javascript
		- Depends on your browser parsing tools
## HTML Forms
### Form Overview
- Standard HTML forms have a <form> tag
- Typical action is called a POST
	- Via Javascript (Async) it is possible to post without a form tag
- Standard Tag:`<form action="post_to_here.php" method="POST"`></form>
	- All data input tags within form sent to action page
	- Method can also be set to GET
		- Will send data over URL
- The file in action="" is where the form will send the data when you hit submit
### HTML Data Fields
- `<input>` tag
	- 'Type' attribute determines rendering 
- Type examples:
	- button (non-submitting)
	- text
	- checkbox
	- submit (button that executes post to action page)
	- select (dropdown list)
		- Similar style to unordered list
		- Can be rendered as multiselect with other attributes
		- These values can be scraped
	- textarea (large text area)
		- Will pass carriage returns when pulled
### Client-Side Data
- Non-free text values are always available for scraping
- Example:
	- `<select>`
		- visible text values and 'value' attribute for tag
	- Checkbox similar to `<select>` except separate `<input>` tags
	- Radio similar to `<select>` except
		- 'name' attribute will be the same to relate the radio buttons
- Lookup tables
	- Lists that render in dropdown 
	- May give you insight to website backend database design
## URL Parsing and Querystrings
### Querystrings
- Method for passing variables in via the URL
- Everything you see after a question mark (?) in a URL
- Variables are separated by ampersands (&)
- Example:
	- https://duckduckgo.com/?q=dogs&t=h_&ia=news
	- q = dogs
	- t = h_
	- ia = news
- This means you can change query just by changing the querystring
- Some sites use custom URLs for Parameters
	- Especially in MVC development style
	- Slashes aren't necessarily directories
### Cookies and Session
- Both are methods of storage
- Useful because the web is stateless
	- There is no 'always on' monitoring of server connections
	- No data is saved by default
- Session
	- Variables held server side
	- User can't access
		- "Secure" from the website perspective 
#### Cookies
- Data stored on client browser
- Used for tracking
- Insecure from website perspective
	- We can change values on them and pass them back to the server
- Can be used to identify user session
	- Ex: ASP.net web forms
- Sites can identify how you travel around their site
	- Identify your actions
	- Expects cookies to be passed back on each request
	- May assume you are not a user if there are no cookies
- Consider checking cookies when scraping
	- See if they exist
	- Check effect of no cookies on request
	- Important if we're disguising ourselves asa user
### Browser Headers
- Website track which browsers connect to their site
	- Useful to make sure browsers render correctly
	- Also for tracking
- The USER_AGENT gives information about the browser connected to the server
	- Has a bunch of information like browser, browser version, your OS, and more
- Impact on scraping:
	- Websites may sniff to ensure you have a browser user agent
	- We may need to simulate a browser header
### JavaScript and Client Scraping
- For websites that use JS to dynamically build a webpage
- HTML will not match what you see
- May need to extract data:
	- From client code
	- From dynamic content
	- Python library: Selenium
		- Will render information as if it is in a browser