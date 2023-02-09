# PROJECT: Simple-Book-Store

### A simple database project

*😊😊😊 Show some :heart: by giving the repo a ⭐*

## 💠 What is Simple-Book-Store ?<br>

⭐ It is a command line inventory system for a book store that uses **SQLite** to store the data in a local database file `ebookstore.db`.

⭐ On running , it allows the user to:

      1. Add books into the inventory
      2. Update the inventory
      3. Delete books
      4. Search for books in the inventory.  

## 💠 Usage

The application is run by using:
```sh
python ebookstore.py
```

## 💠 What does the original database table look like ?

✔️ On first start-up, the database file `ebookstore.db` will be generated containing a few preloaded books:

ID|Title|Author|Quantity
---|---|---|:---:
7001|A Tale of Two Cities|Charles Dickens|30
7002|Adventures of Tom Sawyer|J.K. Rowling|40
7003|The Merchant of Venice|Shakespeare|25
7004|The Lord of the Rings|J.R.R. Tolkien|37
7005|Alice in Wonderland|Lewis Carroll|12

* Once the program is running the user will be presented with a menu. 
* This menu is where the user selects which action they want to do.

```console
========MAIN MENU========
1. Enter book
2. Update book
3. Delete book
4. Search book
5. Show inventory
0. Exit
========SELECTION========
Selection:
```

* While in the menus of the program `-1` can be used to go back to the main menu.

## 💠 Functions

### 📒 Feature 1: Enter book 

This function allows the user to add a book directly to the database. 
The user will be asked to provide the title of the book, the author and the quantity they want to add to the inventory.

There can be 2 possibilities: 
      1. The book and the author (combined) does not exist in the database:
      Then the database gets updated with the entries.
      
      ```console
      ========SELECTION========
      Selection: 1
      ========ENTER BOOK=======
      Title: Talkative Man
      Author: R. K. Narayan
      Quantity: 15
      =ID=|=================Title==================|=================Author=================|Qty|
      ----|----------------------------------------|----------------------------------------|---|
      7001|          A Tale of Two Cities          |            Charles Dickens             | 30|
      7002|        Adventures of Tom Sawyer        |              J.K. Rowling              | 40|
      7003|         The Merchant of Venice         |              Shakespeare               | 25|
      7004|         The Lord of the Rings          |             J.R.R. Tolkien             | 37|
      7005|          Alice in Wonderland           |             Lewis Carroll              | 12|
      7006|             Talkative Man              |             R. K. Narayan              | 15|
      ```
      It also displays that the new book has been added in the inventory.
      
      {console}
      
      2. The book already exists in the database:
      The user will be prompted either to update the quantity of that book or return back to the main menu.
      
      {console}

```console
========SELECTION========
Selection: 1
========ENTER BOOK=======
Title: a tale of two cities 
Author: Charles Dickens
Quantity: 9

==========ERROR==========
Book already exists.
Would you like to update its stock?
=========================

1. Yes
2. No
Selection:
```

### 📒 Feature 2: Update book

This function allows the user to edit a book that is currently in the database. 
This includes the title, author, and quantity. 
      1. If the new title or author is different then the entry corresponding is updated according to the new entries:
      
      {console}
      
      2. If the new title and author is same as the original title and author then the user is prompted if they want to update the quantity of the book:
      
      {console}
      
      Similarly, if the user inputs a book that already exists, they will be prompted to change the quantity of the original book in the database instead.

```console
=======UPDATE BOOK=======
Title: a tale of two cities 
Author: charles dickens
=ID=|=================Title==================|=================Author=================|Qty|
----|----------------------------------------|----------------------------------------|---|
3001|          A Tale of Two Cities          |            Charles Dickens             | 30|
----|----------------------------------------|----------------------------------------|---|
New title: A Tale of Two Cities
New author: Charles Dickens
New Qty: 30

==========ERROR==========
Book already exists.
Would you like to update its stock?
=========================

1. Yes
2. No
Selection:
```

### 📒 Feature 3: Delete book

This function allows the user to remove a book from the database by giving the book title and author.

{console}

### 📒 Feature 4: Search book

This function allows the user to input a book's title and author, and the corresponding entry in the database will be shown:

```console
======SEARCHING BOOK=====
Title: a tale of two cities
Author: charles dickens
=ID=|=================Title==================|=================Author=================|Qty|
----|----------------------------------------|----------------------------------------|---|
3001|          A Tale of Two Cities          |            Charles Dickens             | 30|
----|----------------------------------------|----------------------------------------|---|
```

### 📒 Feature 5: Show inventory

This function is similar to the search function, however, it will print out all the entries of books in the database.

```console
=ID=|=================Title==================|=================Author=================|Qty|
----|----------------------------------------|----------------------------------------|---|
3001|          A Tale of Two Cities          |            Charles Dickens             | 30|
3002|Harry Potter and the Philosopher's Stone|              J.K. Rowling              | 40|
3003|  The Lion, the Witch and the Wardrobe  |               C.S. Lewis               | 25|
3004|         The Lord of the Rings          |             J.R.R. Tolkien             | 37|
3005|          Alice in Wonderland           |             Lewis Carroll              | 12|
```

### 📒 Feature 0: Exit




