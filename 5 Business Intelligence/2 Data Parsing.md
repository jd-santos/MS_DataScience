# 2 Data Parsing
## HTML
### Overview
- HTML is language that structures a webpage
- It is only the structure, it is not:
	- What makes dynamic actions occur
	- Dynamic content loading (usually javascript)
	- Styles of the webpage 
		- Fonts, colors, etc
- For our purposes it is merely the structure that allows for parsing
### Basics of HTML
- HTML Attributes
	- Node based (referred to as tags)
	- Hierarchical in nature
		- Nodes inside of nodes
- Tags contain information
	- As an attribute of a tag
	- Within the open and close of the tag
### Tags and Attributes
- The anchor tag is important because we will often be crawling web pages to find links to other pages, we'll use it as an example
	- Used in HTML for web hyperlinks
`<a href="https://google.com>Google!</a>`
	- <a 
		- The opening of the tag, in this case an a (anchor) tag
	- href
		- Attribute of the tag 
		- You may also see attributes like name, id, class, etc
	- ="https://google.com"
		- The value held in the href attribute
	- Google!
		- Text displayed by the browser
		- Sometimes called inner HTML
	- </a/> 
		- Closing tag of the link (escape character for my markdown app) 
- Common tags
	- `<a>` anchor tag
		- Represents hyperlinks
		- Can be embedded in image to make it clickable
			- `<a href=""><img...></img></a>`
	- `<img>` Image tag
	- `<div>` and `<span>`
		- Divisions for areas that contain tags or text
		- Allow programmers to manipulate chunks more easily
	- `<p>` Paragraph
		- Used for large areas of text
	- `<table>` Tables
		- Requires the following
			- `<tr></tr>` defines a row
				- `<th>` inside of tr, identifies a header row
				- `<td>` inside of tr, identifies a cell in a row
	- `<ul>` Unordered list
		- Bullets
		- Requires:
			- `<li>` List item, use for each item in the list
### Hierarchical Structure
- HTML defines tags within tags
- Represented similar to a tree
/Images/2_HTML_Structure.png

## CSS
### Overview
- Cascading Style Sheets
	- Controls the aesthetic design of a web page
	- Placement of information
		- Much of this is not reflected in the HTML
	- Hiding or displaying certain information
	- Color and font
- For parsing purposes
	- Represents tag attributes that can be useful for parsing
- Affects the "look" of a tag
	- How it renders in a browser
	- Not all browsers handle CSS the same
- CSS might be remote
	- Typically it is held in a separate file that is referenced within the HTML
### Application
/Images/2.2_CSS_Examples.png
- Styles are applied via the 'class' attribute
	- You can also modify the HTML with the 'style' attribute inline, but that's not CSS
	- In CSS, classes are identified with a period in front of it
		- This period is not used in the HTML 
- Multiple classes can be applied
Example:
```
# CSS
.row {
		width: 200px;
		margin-top: 3px;
}
# HTML
<div class="row">...
```

## Parsing HTML
- Inspect element on web page to identify the attribute (span/div/class) of particular elements
	- This is helpful for parsing HTML for specific items on the page
### BeautifulSoup
- A Python library for parsing HTML
- Can extract based on:
	- HTML Tags
	- Attributes of tags
	- CSS class designations
- Can extract:
	- Attribute values
	- InnerHTML
	- Collection of HTML tags
## Parsing in Python