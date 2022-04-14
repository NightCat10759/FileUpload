# FileUpload
  FileUpload made by perl & javascript , purpose to practice practical perl and jquery ajax used.
  
  FileUpload is a web app to managed txt file with certain format contents.
  execute CRUD function to search or change the contents of the information in the database.

## Features
* [File-format](#file-format)
* [Content](#content)
* [How-to-run-this-app](#how-to-run-this-app)
* [Database](#database)


## File-format
  
  file.txt:
```
  [maillog][2022-3-25 21:30:00] HI I'm Content 1
  [maillog][2022-3-25 21:30:00] HI I'm Content 2
.
.
.
```

## Content

* Upload txt file:

  * it's only can Upload txt file, and parse line by line with keyword "maillog" in the txt files.
  * it will save the contents and filename and datetime into database.
  

* Search txt file:
  * key in keyword will print out the contents , which include the certain keyword.
  * key in datetime will print out the contents , which include the certain datetime.
  * key in datetime & keyword will print out the contents , which include the certain datetime & keyword.
  

* Edit txt file:

  input the contents, and press edit button contents will change the contents and send to database.
  

* Delete txt file:
 
  press the delete button will delete this line of all information , and remove this contents from database.
  

## How-to-run-this-app

  clone this app to **xampp htdocs** directory , and setup Database
  
## Database
* DB name:
  ```
  files
  ```
* DB table:
  ```
  id int(20) AUTO_INCREMENT PRIMARY KEY
  
  date datetime
  
  content varchar(200)
  
  filename varchar(20)
  ```
