
# ISI_Project
### Home assignment for ISI

Please install the following libraries:
			
		    $ pip install psycopg2-binary  
		    $ pip install flask-sqlalchemy  
		    $ pip install Flask-Migrate

1. Created server 'local' under the hostname 'localhost' in pgAdmin4.
2. Created database named 'task' in pgAdmin4.
Create a Flask-SQLAlchemy instance called “db”.
Initialized db using these commands after running "python app.py" command to run flask.

				*flask db init, 
				*flask db migrate, 
				*flask db upgrade.
	
3. Created 3 tables using flask-sqlalchemy (with automatic increment if id's named

				-Products with the following fields: 
				*id, 
				*name, 
				*description.
				-Users with the following fields: 
				*id, 
				*name.
				-Reviews with the following fields: 
				*id, 
				*user_id (Foreign Key: Users Table), 
				*product_id (Foreign Key: Products Table),
				*review, 
				*rating.

5. ** Populated the Users table with 5 users using Postman: (/user) 

 ![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/4.png)


6. ** Populated the Products table with the following using Postman: (/product) 

 ![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/5.png)
 
7. ** Populated Reviews Table with the following in Postman: (/review) 
 ![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/6.png)
 
8. Created endpoints in flask and queried results using sqlalchemy.
9. The “Display” option allows the user to input the required id’s to fetch the respective results and the user is free to select any option in the dropdown menu: Reviews, Products and User.
10. Checked if all endpoints are working and re-confirmed the same through Postman for the updates as per the modifications submitted in the form.

** - Please Note: Populated in Postman by selecting "raw" and type "JSON" under heading "Body".
![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/postman.png)
