import sys
def add_book():
    book_ID = input("Enter Book ID: ").strip()
    try:
        with open("books.txt","r") as f:
            books = f.readlines()
            for book in books:
                data = book.strip().split(",")
                if book_ID == data[0]:
                    print("Book ID already exists.")
                    return
    except FileNotFoundError:
        pass
    title = input("Enter Title: ").strip()
    author = input("Enter Author: ").strip()
    available = True
    with open("books.txt", "a") as f:
        f.write(f"{book_ID},{title},{author},{available}\n")
    print("Book added successfully!")


def view_books():
    try:
        with open("books.txt", "r") as f:
            books = f.readlines()
            if not books:
                print("No books available.")
                return
            print("\nAvailable Books:\n")
            for book in books:
                book_id, title, author, available = book.strip().split(",")
                print(f"Book ID: {book_id}")
                print(f"Title: {title}")
                print(f"Author: {author}")
                status = "Yes" if available == "True" else "No"
                print(f"Available: {status}")
                print(f"{'-' * 40}\n\n")
    except FileNotFoundError:
        print("No books available.")


def search_book():
    try:
        search_id = input("Enter Book ID: ").strip()
        found = False
        with open("books.txt","r") as f:
            books = f.readlines()
            if not books:
                print("No books available.")
                return
            for book in books:
                book_id, title, author, available = book.strip().split(",")
                if search_id == book_id:
                    found = True
                    print("\nBook:")
                    print(f"Book ID: {book_id}")
                    print(f"Title: {title}")
                    print(f"Author: {author}")
                    status = "Yes" if available == "True" else "No"
                    print(f"Available: {status}")
                    break
        if not found:
            print("\nBook Not Found\n")
    except FileNotFoundError:
        print("No books available.\n")


def update_book():
    try:
        with open("books.txt","r") as f:
            books = f.readlines()

            if not books:
                print("No books available.")
                return
            found = False
            updated = False
            search_ID = input("Enter Book ID: ").strip()
            
            for i, book in enumerate(books):
                data = book.strip().split(",")

                if data[0] == search_ID:
                    found = True
                    print("------Update Book Record------")
                    print("1. Title")
                    print("2. Author")
                    print("3. Available")

                    match input("Enter choice: "):
                        case "1": 
                            data[1] = input("Enter New Title: ").strip()
                            updated = True
                        case "2": 
                            data[2] = input("Enter New Author: ").strip()
                            updated = True
                        case "3": 
                            while True: 
                                availability = input("Please enter 'yes' or 'no': ").strip().lower()
                                if availability == "yes":
                                    data[3] = "True" 
                                    updated = True
                                    break
                                elif availability == "no":
                                    data[3] = "False"
                                    updated = True
                                    break
                                else:
                                    print("Invalid input. Please enter 'yes' or 'no'.")
                                    continue
                        case _:
                            print("Enter Valid Choice")

        if updated:
            books[i] = ",".join(data) + "\n"
            with open("books.txt","w") as f:
                f.writelines(books)
            print("Record updated successfully.")

        elif not found:
            print("Book not found")
                                
    except FileNotFoundError:
        print("No books available.")


def delete_book():
    try:
        with open("books.txt","r") as f:
            books = f.readlines()

            if not books:
                print("No books available.")
                return
            found = False

            book_ID = input("Enter book ID: ").strip()

            for i,book in enumerate(books):
                data = book.strip().split(",")

                if data[0] == book_ID:
                    found = True
                    del books[i]
                    break
            
            if found:
                with open("books.txt","w") as f:
                    f.writelines(books)
                    print("Record deleted successfully.")
            else:
                print("Book not found")
    except FileNotFoundError:
        print("No books available.")


def borrow_book():
    try:
        with open("books.txt","r") as f:
            books = f.readlines()

            if not books:
                print("No books available.")
                return
            
            search_id = input("Enter Book ID: ").strip()
            found = False
            changed = False

            for i, book in enumerate(books):
                data = book.strip().split(",")
                book_id, title, author, available = data

                if search_id == book_id:
                    found = True

                    if available == "True":
                        changed = True
                        data[3] = "False"
                        books[i] = ",".join(data) + "\n" 
                        print("\nBook borrowed successfully!\n")
                        print(f"Book ID: {book_id}")
                        print(f"Title: {title}")
                        print(f"Author: {author}")

                    else:
                        print("\nBook is already borrowed.\n") 
                        print(f"Title: {title}")  
                    break 

            if changed:
                with open("books.txt","w") as f:
                    f.writelines(books)

            if not found:
                print("\nBook Not Found\n")

    except FileNotFoundError:
        print("No books available.\n")


def return_book():
    try:
        with open("books.txt","r") as f:
            books = f.readlines()

            if not books:
                print("No books available.")
                return
            
            search_id = input("Enter Book ID: ").strip()
            found = False
            changed = False
            for i, book in enumerate(books):
                data = book.strip().split(",")
                book_id, title, author, available = data

                if search_id == book_id:
                    found = True
    
                    if available == "False":
                        changed = True
                        data[3] = "True"
                        books[i] = ",".join(data) + "\n" 
                        print("\nBook returned successfully!\n")
                        print(f"Book ID: {book_id}")
                        print(f"Title: {title}")
                        print(f"Author: {author}")

                    else:
                        print("\nBook is already returned.\n") 
                        print(f"Title: {title}")  
                    break 

            if changed:
                with open("books.txt","w") as f:
                    f.writelines(books)

            if not found:
                print("\nBook Not Found\n")

    except FileNotFoundError:
        print("No books available.\n")



def menu():
    while True:
        print("===== Library Management System =====\n")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Borrow Book")
        print("7. Return Book")
        print("8. Exit")

        match input("\nEnter your choice (1-8): "):
            case "1":
                add_book()
            case "2":
                view_books()
            case "3":
                search_book()
            case "4":
                update_book()
            case "5":
                delete_book()
            case "6":
                borrow_book()
            case "7":
                return_book()
            case "8":
                print("Exiting the program. Goodbye!")
                sys.exit()
            case _:
                print("Invalid choice. Please try again.")


menu()