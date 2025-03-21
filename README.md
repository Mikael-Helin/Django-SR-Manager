# Django-SR-Manager

A minimal Django-based system for managing SR (Superuser/Service Requests).

## Create a SR

Run the following to create an admin user:

    python manage.py createsuperuser

## Change Password

A quick script to reset the admin's password and generate a new one.

    # Generate a new password and save it to a file
    python3 change_pw.py <admin name> > temp.txt

    # View the new password
    cat temp.txt

    # Clean up
    rm temp.txt

