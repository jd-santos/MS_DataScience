# Test 1 
1. Import request
2. Import BeautifulSoup
3. Import CSV
4. Set search page url to variable searchURL
5. Set results url to variable resultsURL (No action URL since we are submitting with Post)
6. Create filepath and filename variables for CSVs
7. Perform get request, store in object 'res'
8. Check status code to confirm request
9. Get the cookies from this request, store in secret_cookies variable
10. Create post_data dictionary with method of POST, rb = 31415926, q = mysterybox, forecasttype = 1
11. Create 'weather_post' request with url of searchURL, post_data, and cookies = secret_cookies, headers = headers
12. Create 'soup' object with weather_post.content
13. Create 'weather_threeday' object by finding fieldset with id of "threeday" in soup
14. Create forecast_threeday object using find_all span with class of "forecast" in weather_threeday
15. Open first CSV with filepath + filename as dataout
	16. Create csv.writer object 'datawriter', pass in dataout, delimiter ',', quotechar '"', and nonnumeric quoting
	17. Use datawriter writerow to create headers 
	18. Create for loop of forecast_threeday
		19. Write row finding class of 'dt', split string at ", ", index 1
		20. Write row finding class of 'dt', split string at ", ", index 0
		21. Write row finding class of 'temp_hi'
		22. Write row finding class of 'temp_low'
		23. Write row of forecast_threeday.src
			24. Split string at ., index 0 
'''
Not sure the most efficient way to write the second CSV, I'm assuming I can just open a new writeable file immediately after

Reusing same object names is probably bad practice. 
'''
25. Create post_data_2 as post_data with forecasttype=2
26. Create weather post request as before
27. Create 'weather_fiveday' object by finding fieldset with id of "fiveday" in soup
28. Create forecast_fiveday object using find_all span with class of "forecast" in weather_fiveday
29. Open second CSV with filepath + filename as dataout
	30. Create csv.writer object as before with same parameters
	31. writerow for headers
	32. Create for loop of forecast_fiveday
		33. Create variable 'temp_dif' equal to int(find span: class = hi) - int(find span: class = low)
		33. Write row finding class of 'dt', split string at ", ", index 1
		34. Write row finding class of 'dt', split string at ", ", index 0
		35. Write row of forecast_fiveday.src
			36. Split string at ., index 0
		37. Write row temp_dif


