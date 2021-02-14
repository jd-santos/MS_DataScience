# R_Reference
## Insert Images
- Import IRdisplay:
	`library ("IRdisplay")`
- Call with relative path:
	`display_png(file="Images/example.png")
- No leading slash if relative, use from current working directory

## Escape Dollar Signs
- Use two backslashes
- \\$ 

## Relative Paths with `here()`
Reference: https://www.amelia.mn/STAT360/slides/17-Filepaths.pdf
`library(here)`
- Console output:
	- here() starts at (current working directory)
- `here()`
	[1] "/Users/Jdsantos/iCloud/Documents/Projects"
- `here("data", "labike.csv")`
	- First argument is a subdirectory, so this calls the path:
		- “"/Users/Jdsantos/iCloud/Documents/Projects/data/labike.csv"
- Example use
	- read_csv(here("data", "labike.csv"))

## Reuse Code Chunks
https://bookdown.org/yihui/rmarkdown-cookbook/reuse-chunks.html#ref-label

## Knit to Word from Console
In case you get missing object errors
`rmarkdown::render("Path-to-file.Rmd")`