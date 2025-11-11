from models import Owners, session

#View profile function
#displays the current users info
# def view_owner(current_user):
#     print("Name: ", current_user.name)
#     print("Email: ", current_user.email)
#     print("Phone: ", current_user.phone)
#     print("Password: ", current_user.password)

def view_owner(current_user):
    current_user.display()

#Update profile function
#displays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user
def update_owner(current_user):
    current_user.display()
    print("Fill in desired changes, to keep current value leave blank")
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    password = input("Password: ")

    if name:
        current_user.name = name
    if email:
        current_user.email = email
    if phone:
        current_user.phone = phone
    if password:
        current_user.password = password
    
    session.commit() #Commit changes to the db
    print("---------- Updated Info --------------")
    current_user.display()
    return current_user

#Update profile function
#Ask user to confirm they want to delete
#if so delete the current user from the session
#commits changes 
#call main() to start the program over