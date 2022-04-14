# ECE 140A - Lab 5

### Karen Hernandez 
### PID: A16118872

### Winter Quarter 2022 
January, 26th, 2022

# Tutorials

## Tutorial 1 - MySQL-Python Connector

Now that we are familiar with MySQL, we incorporated it within a Python environment. This allows us to generate the same processes we would from MySQL directly, with the advantadge that we can incorporate other libraries within python to possibly connect our databases in a webserver. 


Output from our python file generated
> init-db.py

!['Python terminal output'](Tutorials/images/tutorial1.png)

Instead of using MySQL alone, we will create and modify MySQL databases in a pytho environment. 

By using a python MySQL library we utilize a connector that allows us to run SQL commands in python lenguage. 

In order to maintain our data protected, we have to specify our credentials to access our database within a website in a separa file from the main python file. 

> ~/Tutorials/Tutorial1/credentials.env

The file above contains my specific MySQL credentials, that is *host, user, password, and database*. These will be loaded using a **dotenv.load_dotenv** library. 

All MySQL commands can be used just as before, however they must be *wrapped* within a **"cursor"**. 

> cursor = db.cursor()
> cursor.execute(" CREATE / SELECT / INSERT / UPDATE)
> db.commit

Note: The *db.commit** is needed to actually make and save all changes to the database/table. 


## Tutorial 2 : RESTful Databases

In this tutorial we learned how to *combine Pyramid styled webpages with SQL databases*, in order to display necesary data onto our website. 


**Building from past tutorials** the goal was to create a webpage that tracks and displays information of students on the browser. 

In addition to have a dynamic implementation of the certain data (i.e. a dynamic table) within a the HTML document, we use **Jinja2**. 

### Jinja2 
Jinja2 is a rendering engine, to add flexibility to the content displayed on the server side. We implement this as a *programming logic* withinthe HTML file, so as other other programming lenguages' logic it is able to perform conditional statements, loops, variable extraction, etc. 

Writting a fucntion inside the HTML file can be expressed within **{% %}**, where to extract a variable is simple **{{ variable_item }}** . For example:

> {% for student in students %}
>       {{ student[0] }} 
> {% endfor %}

## Tutorial 3 : Fully Functional Website

# Challenges 

## Challenge 1


