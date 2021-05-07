# ISI_Project
Home assignment for ISI

README
1. Created server 'local' under the hostname 'localhost' in pgAdmin4.
2.Created database named 'task' in pgAdmin4.
•	Create a Flask-SQLAlchemy instance called “db”.
•	Initialized db using these commands 
	>>flask db init, 
	>>flask db migrate, 
	>>flask db upgrade.
3. Created 3 tables using flask-sqlalchemy (with automatic increment if id's named
•	Products with the following fields: 
  o	id, 
  o	name, 
  o	description.
•	Users with the following fields: 
  o	id, 
  o	name.
•	Reviews with the following fields: 
  o	id, 
  o	user_id (Foreign Key: Users Table), 
  o	product_id (Foreign Key: Products Table),
  o	review, 
  o	rating.
4. Populated the Users table with 5 users using Postman:
5. README
1. Created server 'local' under the hostname 'localhost' in pgAdmin4.
2.Created database named 'task' in pgAdmin4.
•	Create a Flask-SQLAlchemy instance called “db”.
•	Initialized db using these commands 
	>>flask db init, 
	>>flask db migrate, 
	>>flask db upgrade.
3. Created 3 tables using flask-sqlalchemy (with automatic increment if id's named
•	Products with the following fields: 
o	id, 
o	name, 
o	description.
•	Users with the following fields: 
o	id, 
o	name.
•	Reviews with the following fields: 
o	id, 
o	user_id (Foreign Key: Users Table), 
o	product_id (Foreign Key: Products Table),
o	review, 
o	rating.
4. Populated the Users table with 5 users using Postman:
 README
1. Created server 'local' under the hostname 'localhost' in pgAdmin4.
2.Created database named 'task' in pgAdmin4.
•	Create a Flask-SQLAlchemy instance called “db”.
•	Initialized db using these commands 
	>>flask db init, 
	>>flask db migrate, 
	>>flask db upgrade.
3. Created 3 tables using flask-sqlalchemy (with automatic increment if id's named
•	Products with the following fields: 
o	id, 
o	name, 
o	description.
•	Users with the following fields: 
o	id, 
o	name.
•	Reviews with the following fields: 
o	id, 
o	user_id (Foreign Key: Users Table), 
o	product_id (Foreign Key: Products Table),
o	review, 
o	rating.
4. Populated the Users table with 5 users using Postman:
 ![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/4.png)

5. Populated the Products table with the following using Postman:
![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/5.png)
 
6. Populated Reviews Table with the following in Postman:
![alt text](https://github.com/vidhubala-selvaraj/ISI_Project/blob/main/screenshots/6.png)
 
7. Created endpoints in flask and queried results using sqlalchemy.
8. The “Display” option allows the user to input the required id’s to fetch the respective results and the user is free to select any option in the dropdown menu: Reviews, Products and User.
9. Checked if all endpoints are working and re-confirmed the same through Postman for the updates as per the modifications submitted in the form.






5. Populated the Products table with the following using Postman:
 
6. Populated Reviews Table with the following in Postman:
 
7. Created endpoints in flask and queried results using sqlalchemy.
8. The “Display” option allows the user to input the required id’s to fetch the respective results and the user is free to select any option in the dropdown menu: Reviews, Products and User.
9. Checked if all endpoints are working and re-confirmed the same through Postman for the updates as per the modifications submitted in the form.



5. Populated the Products table with the following using Postman:
 
6. Populated Reviews Table with the following in Postman:
 
7. Created endpoints in flask and queried results using sqlalchemy.
8. The “Display” option allows the user to input the required id’s to fetch the respective results and the user is free to select any option in the dropdown menu: Reviews, Products and User.
9. Checked if all endpoints are working and re-confirmed the same through Postman for the updates as per the modifications submitted in the form.


