import sqlite3
import re
#Object to carry out database operations
class BookDB:
    def __init__(self):
        self.db = sqlite3.connect("ebookstore.db")
        self.cursor = self.db.cursor()
        
        #Generates the table if it does not exist
        if not self.tableExists():
            self.generateTable()
    
    def __str__(self):
        """
        Overloads print statement to allow for the whole database to be shown
        """
        
        #Selects all rows and puts them into the cursor object
        select_rows = """
        SELECT * FROM ebookstore"""
        self.sqlCommand(select_rows)

        #Header formatting
        output = f"{'ID':=^4}|{'Title':=^40}|{'Author':=^40}|{'Qty'}|\n{'':-^4}|{'':-^40}|{'':-^40}|{'':-^3}|\n"

        #Formats each row
        for row in self.cursor:
            output += f"{row[0]:4}|{row[1]:^40}|{row[2]:^40}|{row[3]:3}|\n"

        return output
    
    def sqlCommand(self,command,inputs=()):
        """
        Executes a given SQL command using the defined cursor and database object
        """
        try:
            #Checks if multiple a list of tuples are being given
            if isinstance(inputs,list):
                self.cursor.executemany(command,inputs)
            else:
                self.cursor.execute(command,inputs)
            
            self.db.commit()
        
        #If an error occures, roll back
        except Exception as e:
            self.db.rollback()
            raise e
        
    def generateTable(self):
        """
        Generates the initial table and fills it
        """

        #Creates empty table
        generate = """
        CREATE TABLE IF NOT EXISTS ebookstore (
            id int,
            Title varchar(255),
            Author varchar(255),
            Qty int,
            PRIMARY KEY (id))"""
        self.sqlCommand(generate)

        #Populates table
        books = [
            (7001,"A Tale of Two Cities","Charles Dickens",30),
            (7002,"Adventures of Tom Sawyer","J.K. Rowling",40),
            (7003,"The Merchant of Venice","Shakespeare",25),
            (7004,"The Lord of the Rings","J.R.R. Tolkien",37),
            (7005,"Alice in Wonderland","Lewis Carroll",12)
            ]
        populate = """
        INSERT INTO ebookstore VALUES
        (?,?,?,?)"""
        self.sqlCommand(populate,books)
    
    def tableExists(self):
        """
        Checks if the table already exists
        """
        
        #Gets a the name of the table
        check_exists = """
        SELECT name FROM sqlite_master WHERE type='table' AND name='ebookstore'"""
        self.sqlCommand(check_exists)

        #Checks if the table exists
        if self.cursor.fetchone() == None:
            return False
        return True
    
    def getBooks(self):
        """
        Generates a list of all books in the database
        """
        #Gets all rows and attributes
        select = """
            SELECT * FROM ebookstore"""
        self.sqlCommand(select)

        #Initialise all books in database
        collection = []
        for item in self.cursor:
            collection.append(Book(self,item[1],item[2],item[3],item[0]))

        return collection

    def addBook(self,book):
        """
        Adds given book into the database
        """

        #Gets the tuple of book information
        book_info = book.getInfo()

        #Inserts it into the database
        add = "INSERT INTO ebookstore VALUES (?,?,?,?)"
        self.sqlCommand(add,book_info)
        return True
    
    def updateBook(self,book):
        """
        Allows user to update the information of a book in the database
        """
        try:
            #Gets the book information
            book_info = book.getInfo(["title","author","qty","id"])

            #Changes the values for the given book with the same ID
            update = """
                UPDATE ebookstore
                SET title = ?,
                    author = ?,
                    qty = ?
                WHERE id = ?"""
            self.sqlCommand(update,book_info)
            
        except Exception as e:
            raise e
    
    def deleteBook(self,book):
        """
        Deletes a given book from the database
        """

        #Gets the id of the given book
        book_id = book.getInfo(["id"])

        #Removes book from database
        delete = """
            DELETE FROM ebookstore
            WHERE id = ?"""

        self.sqlCommand(delete,book_id)
        return True
    
    def findBook(self,title:str,author:str):
        """
        Searches for given book in the database and returns it if it exists
        """

        #Removes all characters that arent letters
        title_clean = re.sub(r"[^\w\s]","",title)
        author_clean = re.sub(r"[^\w\s]","",author)

        #Makes user inputs all uppercase and strips trailing spaces
        input = set([title_clean.strip().upper(),author_clean.strip().upper()])
        
        #Generates a list of book in the database
        library = self.getBooks()
        
        #Loops through all books
        for book in library:
            #Gets the title and author for each book
            book_title,book_author = book.getInfo(["title","author"])

            #Removes all none letter characters and trailing spaces
            book_title = re.sub(r"[^\w\s]","",book_title)
            book_title = book_title.strip().upper()
            book_author = re.sub(r"[^\w\s]","",book_author)
            book_author = book_author.strip().upper()

            #Puts into a set for comparison
            book_info = set([book_title,book_author])

            #Return the book if a match is found
            if input == book_info:
                return book

        return False

class Book:
    def __init__(self,database:BookDB,title:str,author:str,quantity:int,id=None):
        self.title = title
        self.author = author
        self.qty = quantity
        self.id = id

        #Only give ID if one is not given
        if not self.id:
            self.setId(database)

    def __str__(self):
        """
        Print function override
        """
        headers = f"{'ID':=^4}|{'Title':=^40}|{'Author':=^40}|{'Qty'}|\n"
        border = f"{'':-^4}|{'':-^40}|{'':-^40}|{'':-^3}|\n"
        info = f"{self.id:4}|{self.title:^40}|{self.author:^40}|{self.qty:3}|\n"
        return headers + border + info + border.rstrip("\n")
        
    def setId(self,database:BookDB):
        """
        Determines the ID the the book object
        """

        #Gets the last (largest) id in the database
        get_id = """
        SELECT MAX(id) FROM ebookstore"""
        database.sqlCommand(get_id)

        #Increments by 1
        self.id = database.cursor.fetchone()[0] + 1
    
    def getInfo(self,info=["id","title","author","qty"]):
        """
        Returns all the information 
        """
        output = []
        #Loops through watned attributes
        for attribute in info:
            output.append(getattr(self,attribute))

        return tuple(output)
    
    def setInfo(self,new_title=None,new_author=None,new_qty=None):
        """
        Allows for attributes of a book to be changed
        """

        if new_title != None:
            self.title = new_title
        
        if new_author != None:
            self.author = new_author
        
        if new_qty != None:
            self.qty = new_qty

def printError(message:str):
    """
    Prints an errors message
    """
    print()
    print("ERROR".center(25,'='))
    print(message)
    print("".center(25,'='))
    print()

def updateStockInfo(database:BookDB,book:Book):
    """
    Gets the user input for the new stock value
    """
    while True:
        print("UPDATE STOCK".center(25,"="))
        #Gets current info of book
        info = book.getInfo(["qty"])
        print("Current stock: ",info[0])

        try:
            #Get new stock value
            qty = int(input("New stock: "))
        except ValueError:
            printError("Invalid quantity\nPlease enter a number.")
            continue
        break
    return qty

def updateStock(database:BookDB,book:Book):
    """
    Allows the user to update just the stock value of a given book
    """
    while True:

        #Gets user selection
        printError("Book already exists.\nWould you like to update its stock?")
        print("1. Yes")
        print("2. No")

        try:
            update_qty = int(input("Selection: "))
        except ValueError:
            printError("Invalid selection.")
            continue

        #User wants to update the stock
        if update_qty == 1:
            new_qty = updateStockInfo(database,book)
            #Change book object
            book.setInfo(new_qty=new_qty)
            
            #Update book in the database
            database.updateBook(book)
            print("Book updated...")
            break
        elif update_qty == 2:
            break
        else:
            printError("Invalid selection")
            continue

def adding(database:BookDB):
    """
    Allows the user to enter a book into the database
    """
    while True:
        print("ENTER BOOK".center(25,"="))
        
        #Gets user input and checks if they want to exit 
        book_title = input("Title: ")
        if book_title == "-1":
            break
    
        book_author = input("Author: ")
        if book_author == "-1":
            break
        
        #Checks if a valid value is given
        try:
            book_qty = int(input("Quantity: "))
            if book_qty == -1:
                break
        except ValueError:
            printError("Invalid quantity\nPlease enter a number\nfor quantity.")
            continue

        #Checks if given book exists
        book_exist = database.findBook(book_title,book_author)
    
        if book_exist:
            #Asks if user wants to update already exising book
            updateStock(database,book_exist)
            break    
        else:    

            #Generates book object
            book_new = Book(database,book_title,book_author,book_qty)

            #Adds book to database
            database.addBook(book_new)

            print(database)
            break

def deleting(database:BookDB):
    """
    Deletes a given book from the database
    """
    #Delete loop
    while True:

        print("DELETE BOOK".center(25,"="))

        #Checks if user wants to exit loop
        book_title = input("Title: ")
        if book_title == "-1":
            break
        book_author = input("Author: ")
        if book_author == "-1":
            break
        
        #Gets book from database
        book = database.findBook(book_title,book_author)
        
        #Checks if book exists in database
        if not book:
            printError("Book not found!\nPlease enter a valid book\nor -1 to return to main menu.")
            continue

        print("Deleting...")
        
        #Removes book from database
        database.deleteBook(book)
        print(book)
        break

def updateInfo(database:BookDB):
    """
    Allows user to input new info until valid info is given
    """
    while True:
        #Gets new attributes
        title = input("New title: ")
        author = input("New author: ")

        #Makes sure user input a valud quantity
        try:
            qty = int(input("New Qty: "))
        except ValueError:
            printError("Invalid selection\nPlease enter a number for quantity")
            continue
        break
    return title,author,qty

def updating(database:BookDB):
    """
    Finds given book in database and allows for the user to change its attributes
    """
    while True:
        print("UPDATE BOOK".center(25,"="))

        #Gets book user wants to update
        book_title = input("Title: ")
        if book_title == "-1":
            break
        book_author = input("Author: ")
        if book_author == "-1":
            break

        #Fetches book from database
        book = database.findBook(book_title,book_author)

        #Throw error if the book does not exist
        if not book:
            message = "Book does not exist!\n"
            message += "Please enter a valid book\n"
            message += "or enter -1 to return to main menu"

            printError(message)
            continue

        #Show books current info
        print(book)

        #Gets user input for new title, author and quantity
        new_title,new_author,new_qty = updateInfo(database)
        
        #Gets potential duplicate
        book_dup = database.findBook(new_title,new_author)
        
        #Ask to update quantity if book exists
        if book_dup:
            updateStock(database,book_dup)
            break
        
        #Updates book object and updates it in the database
        book.setInfo(new_title=new_title,new_author=new_author,new_qty=new_qty)
        database.updateBook(book)
        
        print("Updaing to:")
        print(book)
        break

def searching(database:BookDB):
    """
    Allows for the user to search for a given book
    """
    while True:
        print("SEARCHING BOOK".center(25,'='))

        #Gets attributes for book
        book_title = input("Title: ")
        if book_title == '-1':
            break
        book_author = input("Author: ")
        if book_author == '-1':
            break
        
        #Finds the given book in the database
        book = database.findBook(book_title,book_author)

        #Throw error if the book does not exist
        if not book:
            message = "Book not found!\n"
            message += "Please enter a valid book\n"
            message += "or -1 to return to main menu"
            printError(message)
            continue
        
        #Shows book information
        print(book)
        break

#Creates database instance
db = BookDB()

#Main program
select = ""
while select != '0':
    print("MAIN MENU".center(25,"="))
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search book")
    print("5. Show inventory")
    print("0. Exit")
    print("SELECTION".center(25,'='))

    select = input("Selection: ")
    #Enter a book into the database
    if select == '1':
        adding(db)
    
    #Update a book already in the database
    elif select == '2':
        updating(db)

    #Delete book from database
    elif select == '3':
        deleting(db)

    #Search book from database
    elif select == '4':
        searching(db)
    
    #Prints the entire database
    elif select == '5':
        print(db)

    #Exit menu
    elif select == '0':
        print("Shutting down")

    #Catching errors
    else:
        printError("Invalid selection")

db.db.close()
