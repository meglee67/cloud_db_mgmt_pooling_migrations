# cloud_db_mgmt_pooling_migrations
* HHA 504 HW 4C
* Due 10/27
* OG Instructions below
## **1. Connection Pooling Setup**
### Creating databases on Google Cloud Platform (GCP) and Azure 
### GCP
* Login on the [Cloud Console](https://console.cloud.google.com/) and click on the button new project. Name it something relevant to the task at hand.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/f9dcf680-5ad7-4ceb-9b2a-834f7c871f6f)
* Then when on the page to create a new project, make sure to designate the location of the new project as AHI - GCP.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/cad03e37-6540-4a02-b80e-27ef4b204a35)
* Once you have created a new project, make sure you are clicked into the right project. Go to the dashboard and check.
* Then click on the navigation menu in the top left and find the tab that is called SQL near the bottom. Once you have clicked on this tab, you'll be taken to a page and you will see a button that says "Create Instance". CLick on it.
  * Then you will see 3 database engine options. Choose the MySQL option.
  ![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/aa6e3304-6f01-4c3b-916d-9af10041fac1)
  * You will then have to click the button on screen to enable API.
  * After this, keep the database version as MySQL 8,0
  * For the "Choose Cloud SQL edition" choose <ins>Enterprise<ins>.
  * When choosing a preset, choose <ins>Sandbox<ins>.
  * Under "Customize your instance", go to machine configuration and choose <ins>Shared core;1 vCPU, 0.614 GB<ins>
  * At "Connections" choose a Public IP, and add a network. Name the network AllowAll and set it to 0.0.0.0/0 and then click the button to create your instance.

### Azure
* Login on the [Azure Portal](https://azure.microsoft.com/en-us/get-started/azure-portal) and search in the bar for Azure Database for MySQL. Click on it and then click create.
* You will be brough to a page with two options, choose the Flexible Server.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/fefe900f-cce5-452a-9e1f-b557d0d094a0)
* Choose an existing resource group or create a new one
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/58af9f5d-c6be-4edb-811e-1c4fd59f3995)
* Create a server name relevant to the assignment (mine was hha504-hw4C)
* Fill out all required fields
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/0e9f0669-a360-4de4-87df-c7a806223c1d)
* Under Networking make sure to enable public access, and to allow public access under Firewall rules. For the start and end IP address, use 0.0.0.0 and 255.255.255.255
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/0314e284-320b-46e2-9e09-1b4f58275210)
* Configure connection pooling for the Azure databases.
  * Define appropriate pool size and timeout settings.
    * `max_connections`: 20
    * `connect_timeout`: 3 
* Then press the button to create.

## Connecting the GCP and Azure Database to MySQL Workbench
### GCP
* To connect your GCP database to MySQL Workbench, find the public IP to your instance you created. This can be found on the dashboard.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/0a33af7b-13a9-47ef-8edc-49be27210e0d)
* Then within your MySQL Workbench, click on the tiny plus sign.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/15866b9a-d6b9-4d75-934e-705d04f55d76)
* A window will pop-up to setup a new connection. Name your connection and in the field for Hostname, input your public IP for the instance. The username should match the username you set up when creating your instance.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/cf64eebd-8e8d-4ce9-9efa-deddf6d99bd9)
* Once you have filled out all the fields, hit the button to test connection. You will be prompted to input a password, which you designated when creating your instance. If you input the correct password, you should see a successful connection message.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/91c35b6e-8ec9-4d58-86c5-10c863da3a29)
* Then you should be able to view this new connection on the homescreen.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/76ef4b63-53df-4c2f-8b35-c5dda26d31b2)

### Azure
* To connect my Azure databased to the MySQL Workbench, I followed the instructions found in this [quickstart guide](https://learn.microsoft.com/en-us/azure/mysql/flexible-server/connect-workbench).
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/eee5526e-935f-455c-ba2c-38c74dbebac3)
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/25566c91-abdd-4045-98bd-def38aef6d93)

## **2a. Database Schema and Data**
* I copied and modified code from [Week 4 gcp.py](https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/gcp.py)


## **2b. Using MySQl Workbench to Generate ERD**
* To create the ERD, I navigated to the Database button in the options ribbon and chose the button "Reverse Engineer", also accesisble by hitting CTRL+R
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/1c70e289-580d-4adb-abc4-973295945507)
* You will then be taken to a window that asks you to choose a stored connection (I chose my GCP and then did the same process for my Azure afterwards). You may have to re-input the password again.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/f0676117-e35e-4d1b-8245-53bb465fc90b)
* Then you can keep clicking the next button as the program goes through the process of Connect to DBMS, Select Schemas, Retrieve Objects, Select Objects, Reverse Engineer and Results.
* On your results page, scroll around to find your generated ERD. The program automatically creates relationships but they may not be correct (one-to-one, or one-to-many). If you need to change the relationship type, follow the steps in the image below.
![image](https://github.com/meglee67/mysql_cloudmanaged_databases/assets/123908362/0a80ab53-a7f0-44dd-81b3-7ebb00cefdad)

## **3. SQLAlchemy and Flask Integration**
* To set up a Flask app I copied over my [app.py and templates](https://github.com/meglee67/flask_4_databases_mysql_vm/blob/main/app.py) from HHA 504 HW 4B.

## **Database Migrations with Alembic**
* I ran the command ``alembic init migrations`` which created an alembic.ini file and a migrations folder
* I added the alembic.ini to my .gitignore file
* Within alembic.ini I edited ``sqlalchemy.url = driver://user:pass@localhost/dbname`` to ``sqlalchemy.url = mysql+mysqlconnector://usernamehere:passwordhere@IPaddresshere/databasenamehere``
* Then within the env.py file that is found under the migrations folder, I added in ``from gcp import Base`` as the file I used to create the tables is named gcp.py
* then I changed ``target_metadata = none`` into ``target_metadata = Base.metadata`` and commented out the none one
* Then to create the migration I did ``alembic revision --autogenerate -m "create tables"``
* Next I ran the migration using ``alembic upgrade head``
* To save I ran ``alembic upgrade head --sql > migration.sql``. This created a file named migration.sql

<br>


## **Databases Part 4c Assignment: Cloud Database Management with Connection Pooling and Migrations**

### **Objective**:
Gain practical experience in managing a cloud-based MySQL database with a focus on implementing connection pooling and performing database migrations. You will work with both Azure and Google Cloud Platform (GCP) for this assignment.

### **Instructions**:

#### **1. Connection Pooling Setup**:
- **Azure**: Spin up an Azure MySQL Database instance.
- **GCP**: Create a Google Cloud SQL MySQL instance.
- Configure connection pooling for the Azure databases.
  - Define appropriate pool size and timeout settings.
    - `max_connections`: 20
    - `connect_timeout`: 3 

**Reminder**: Please be sure that the appropriate network/firewall rules are established to ensure inbound/outbound traffic to your database on either Azure or GCP.

#### **2a. Database Schema and Data**:
- **Azure**: Create a database schema with at least two tables on your Azure MySQL instance.
- **GCP**: Create an equivalent database schema with the same structure on your Google Cloud SQL MySQL instance.
- Populate the tables with sample data.
  - Ensure there is a foreign key relationship between the tables.
  - Document the schema structure and data population process for both Azure and GCP instances.
- For GCP example: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/gcp.py 
- For Azure example: https://github.com/hantswilliams/HHA_504_2023/blob/main/WK4/code/migrations/azure.py 

#### **2b. Using MySQL Workbench to Generate ERD**:
- Launch MySQL workbench adn connect it to your mySQL instance
- Using the 'reverse engineer' function, retrieve the database schema structure 
- Modify the schema to ensure the foreign key relationship is properly documented
- Generate an ERD for your database using MySQL Workbench and save a photo of it in your repo

#### **3. SQLAlchemy and Flask Integration**:
- Modify or create a Python Flask application to connect to both the Azure and GCP MySQL databases.
- Implement SQLAlchemy for connection pooling in the Flask application.
- Develop endpoints to retrieve and display data from both databases.
- Ensure the Flask application works seamlessly with both databases.
- Provide screenshots or videos showcasing the Flask application connected to Azure and GCP databases.

#### **4. Database Migrations with Alembic**:
- Set up Alembic for database migrations on both Azure and GCP MySQL instances.
- Create an initial migration script for each database to capture the current schema.
- Implement a migration that alters the schema in a meaningful way (e.g., add a new table or modify an existing one) for both databases.
- Run the migrations and document the process, including any challenges faced and how you resolved them.

#### **5. Documentation and Error Handling**:
- Prepare a detailed README.md file in your GitHub repository:
  - Explain the setup and configuration of connection pooling for Azure and GCP databases.
  - Describe the database schema structure, including the rationale behind it.
  - Document the steps and challenges encountered during the database migration process.
  - Include screenshots or videos demonstrating the Flask application's interaction with both databases.
- If you encounter any errors or challenges, document them thoroughly, providing screenshots, descriptions of your troubleshooting steps, and potential root causes.

### **Submission**:
- Create a new GitHub repository named `cloud_db_mgmt_pooling_migrations` in your GitHub account.
- Include all your code, scripts, and documentation in the repository.
- Share the link to your repository as your assignment submission.
- Ensure your repository is public so that it's accessible for review.

**Tip**: Pay special attention to security when managing cloud-based databases. Never expose sensitive credentials or data, and use secure practices throughout the assignment.
