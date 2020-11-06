# Run the following command after cloning this repo

## Windows

1. Change directory into the cloned folder with

    ```cd django_orm```

2. Activate virtual environment 
    
    ```env\Scripts\activate```

3. change directory into the main django folder
    
    ```cd orm_manage_user```

4. Run the django server

    ```python manage.py runserver```

5. Now open the localhost:8000 in your browser of choice

6. create a staff account with this link localhost:8000/register/staff

7. create a normal user account with this link localhost:8000/register/user

# Now test out the functionality


## Mac or Linux (Unix based machines)

1. Change directory into the cloned folder with

    ```cd django_orm```

2. delete the env folder (because it was for a windows pc)

3. create a new virtual environment whiles in the directory of the cloned folder (~/django_orm)

    ```virtualenv env```
    
    Note: Make sure you have virtualenv as a part of your python packages or install it with
        ```pip install virtualenv```

4. Activate virtual environment 
    
    ```source env/bin/activate```
    


5. change directory into the main django folder
    
    ```cd orm_manage_user```
    
6. Install the needed python packages

        ```pip install -r requirements.txt```

6. Run the django server

    ```python manage.py runserver```

7. Now open the localhost:8000 in your browser of choice

8. create a staff account with this link localhost:8000/register/staff

9. create a normal user account with this link localhost:8000/register/user

# Now test out the functionality
