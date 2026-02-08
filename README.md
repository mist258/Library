
## INSTALLATION AND LAUNCHING GUIDE


```bash
    1) git clone https://github.com/mist258/Library.git

    2) poetry shell  (#initaialize environment)

    3) poetry install  (#install dependencies)

    4) Create a .env file and set the variables according to .env.example.

    5) psql -h [your-host] -p [your-port] -U [your-username] (#execute current cmd in console to create db (example: psql -h localhost -p 5432 -U postgres))

    6) CREATE DATABASE [your-db-name];

    7) exit;

    9) python manage.py migrate(#apply migrations)

    10) python manage.py createsuperuser(# create superuser to get access to admin page)

    


```
## If you are using PyCharm, after creating the database you can connect to it by entering the data from the .env file into the appropriate fields.
<img width="1008" height="860" alt="image" src="https://github.com/user-attachments/assets/10c0c938-a51f-4d41-98be-2f652059534b" />

## RESULT  
<img width="2030" height="1003" alt="image" src="https://github.com/user-attachments/assets/df5de720-72cf-482f-8285-6aa374b95187" />
<img width="2030" height="1003" alt="image" src="https://github.com/user-attachments/assets/67a93553-afba-453d-b9fa-75632b96883e" />
<img width="2030" height="1003" alt="image" src="https://github.com/user-attachments/assets/6320161c-f027-4e52-b23e-5631dcf9dbdc" />
<img width="2030" height="1003" alt="image" src="https://github.com/user-attachments/assets/588d719c-bb03-499e-9814-8811e54bb8f9" />


