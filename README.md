# PROJECT: Simple-Book-Store


A command line inventory system for a book store that uses SQLite to store the data in a local database file `ebookstore.db`. Once running, the application allows for the user to add books into the inventory, update the inventory, delete books, and search for books in the inventory.  

## Usage

The application if run by using:

```sh
python ebookstore.py
```

On first start-up, the database file `ebookstore.db` will be generated containing a few preloaded books:

Title|Author|Quantity
---|---|:---:
A Tale of Two Cities|Charles Dickens|30
Harry Potter and the Philosopher's Stone|J.K. Rowling|40
The Lion, THE Witch and the Wardrobe|C.S.Lewis|25
The Lord of the Rings|J.R.R. Tolkien|37
Alice in Wonderland|Lewis Carroll|12

Once the program is running the user will be presented with a menu. This menu is where the user selects which action they want to do.

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

While in the menus of the program `-1` can be used to go back to the main menu.

### 1. Enter book

This function allows the user to add a book directly to the database. The user will be asked to provide the title of the book, the author and the quantity they are adding to the inventory.

If the user inputs a book that already exists in the database, they will be prompted whether they would like to update the quantity of that book or return back to the main menu.

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

### 2. Update book

This function allows the user to edit a book that is currently in the database. This includes the title, author, and quantity. Similarly, if the user inputs a book that already exists, they will be prompted to change the quantity of the original book in the database instead.

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

### 3. Delete book

This function gives the user the ability to remove a book from the database by giving the books title and author.

### 4. Search book

This function allows the user to input a books title and author, and that book entry in the database will be shown, including its quantity and unique ID.

```console
======SEARCHING BOOK=====
Title: a tale of two cities
Author: charles dickens
=ID=|=================Title==================|=================Author=================|Qty|
----|----------------------------------------|----------------------------------------|---|
3001|          A Tale of Two Cities          |            Charles Dickens             | 30|
----|----------------------------------------|----------------------------------------|---|
```

### 5. Show inventory

This function is similar to the search function, however, it will print out all of the books in the database, including their quantity and unique ID.

```console
=ID=|=================Title==================|=================Author=================|Qty|
----|----------------------------------------|----------------------------------------|---|
3001|          A Tale of Two Cities          |            Charles Dickens             | 30|
3002|Harry Potter and the Philosopher's Stone|              J.K. Rowling              | 40|
3003|  The Lion, the Witch and the Wardrobe  |               C.S. Lewis               | 25|
3004|         The Lord of the Rings          |             J.R.R. Tolkien             | 37|
3005|          Alice in Wonderland           |             Lewis Carroll              | 12|
```


