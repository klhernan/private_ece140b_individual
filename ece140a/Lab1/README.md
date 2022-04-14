# ECE 140A: Lab 1

## Karen Hernandez
## A16118872
 Winter 2022

# Tutorial 1
Undertanding github and how to push files onto our repository 

# Tutorial 2
Using Anaconda as an environment to use jupyter notebook, which is good for block running. It can also be used to add markdown in between code blocks. 

# Tutorial 3
Leaning python, from types, lists, loops, and functions. 

# Tutorial 4
The Web scrapping tutorial helped understand the process of obtaining data from an html file, and some important python functions to obtain the document from an URL. Once the data has been obtained from the servers by using the *requests* library, we use the *BeautifulSoup.bs4* library to extract the text from the requests output as a plain text. This plain text can be seen with or without indetation with the function soup.prettify(), where soup is the text extracted from the content of the HTML file. *BeautifulSoup* has additional function to sort through the data such as *find_all()* where the inputs are a HTML tag and particular class (i.e. text or author for the tutorial). We can print the the output as text by calling the attribute *.text* from the *soup.find_all(tag, class)* output.


# Challenge 1

## ANS1

#### Q1. Is "DOCTYPE html" an HTML tag? What is it doing in an HTML file?
It is not a tag, it is a declaration at the beginning of the file to specify the format version of HTML to be used to build the document. It informs the browser to use the specific format and version with respect to the initial declaration, allowing it to handdle and load the document properly. 

## ANS2

#### Q2. Change title to your name. Explain what changed in the webpage display.

By simply changing *title* nothing changed, as we can see the main title displayed on the web page is the main header tag, not the title. 

## ANS3

#### Q3. *hr* tag for both opening and closing a break line 
The *hr* tag can be used without necessarily having a closing tah. Thus, the same expression is used for opening and closing in this case the section, as it is just a line marking a break between sections. 

## ANS4

###d# Editing file in browser
When the document is changed in inspect section in the browser, the changes can be seen as implemented. However, the changes are done temporarily and will not modify the original document, so if the page is refreshed then the format will go back to how it was on the original file. 

### Extra additions:
 1. Changed the header color (to aquamarine)
 2. Set the image height as well 
 3. Added a link from music back to main
 4. Link to social media(Extra)

# Challenge 2

Answer the questions below

### In which year did Barack Obama get the Nobel Peace Prize?
* 2009

### When and for what did Ernest Rutherford win the Nobel Prize?
* 1908
* Chemistry
* for his investigations into the disintegration of the elements, and the chemistry of radioactive substances

### Who got the prize for Physics in 1939?
* Ernest Orlando Lawrence