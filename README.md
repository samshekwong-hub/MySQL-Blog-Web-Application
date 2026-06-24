# MySQL-Blog-Web-Application
A MySQL Blog web application with using flask allowing adding or deleting blogs
The SQL script could be found in **db_backup** folder

### Steps
Import the SQL script
  - In MySQL, create table **blog_db**, ensuring grant privileges to the user and import **blog_db.sql** to your database
  - Remember to change the **user** and **password** to yours (shown as below)
  - <img width="403" height="177" alt="flask_blog1" src="https://github.com/user-attachments/assets/ecfba919-71dd-4517-b279-9f016ea0ef2f" />
Inside the project, create a Python virtual environmentOpen the terminal, activate the program by typing ``` python app.py ```
After the application run successfully, click the ``` Running on http://localhost:5000 ``` and you will successfully open the main page
  
### Walkthrough
#### Main Page of the Web
<img width="1916" height="951" alt="flask_blog2" src="https://github.com/user-attachments/assets/57189954-a372-4db3-b112-86434572f0b2" />

#### Editing Blogs
Please go to **blogs** to add, remove and edit blogs

##### Adding Blogs ####

1. Click **add blog** in blogs page
2. Input the information of your blog in the form and submit it

Input your information of your blog<img width="1919" height="954" alt="flask_blog4" src="https://github.com/user-attachments/assets/e6d9118a-99c9-465b-9fff-9dddf5b9cd32" />

Now the blog you added is shown and you can click **Delete** to remove the blog from database (Notice: the **Edit** button of the blog is currently unavailable)
<img width="1911" height="951" alt="flask_blog5" src="https://github.com/user-attachments/assets/cd3a9219-6dc7-49c1-ae29-d7258e19c701" />
