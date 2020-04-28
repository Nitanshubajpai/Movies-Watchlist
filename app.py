from user import User

user_name = input("->Enter your name: ")
user = User(user_name)
choice=9

while choice!=0:
    choice = int(input("_______________________________________________________"
                       "\nEnter 1 to add a movie."
                       "\nEnter 2 to delete a movie."
                       "\nEnter 3 to change the movie status(Watched)."
                       "\nEnter 4 to show the list of watched movies."
                       "\nEnter 5 to save the file."
                       "\nEnter 6 to view the file."
                       "\n_______________________________________________________\n"))
    if choice == 1:
        user.add_movie()
    elif choice==2:
        target = input("Enter the name of the movie to be deleted: ")
        user.delete_movie(target)
    elif choice == 3:
        target = input("Enter the name of the movie: ")
        user.movie_status(target)
    elif choice == 4:
        user.watched_movies()
    elif choice == 5:
        user.save_to_file()
    elif choice == 6:
        user.view_saved_file()
    elif choice == 0:
        exit()