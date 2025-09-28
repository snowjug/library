# Library Management System

A **Java-based Library Management System** built using **Swing** for the GUI and **SQLite** for the database. This project allows users to manage books, borrowers, and checkout records efficiently, with an intuitive and responsive interface.

---

## Features

- **Book Management**
  - Add, remove, search, and refresh book records.
  - Track availability of books.
  - View all books in a tabular format.

- **Borrower Management**
  - Add and remove borrowers.
  - Manage borrower information (name, email, phone).
  - View all borrowers in a table.

- **Checkout Management**
  - Add and remove checkout records.
  - Record checkout, due, and return dates.
  - Automatically link books to borrowers.

- **Database**
  - Powered by **SQLite** (file-based, no server required).
  - Automatically creates necessary tables if they don’t exist.
  - Provides refresh functionality to update GUI tables dynamically.

- **GUI**
  - Built with **Java Swing**.
  - Responsive and user-friendly tabbed interface.
  - Color-coded buttons for actions (add, remove, refresh).

---

## Technologies Used

- Java 21 (JDK)
- Swing for GUI
- SQLite for database
- SQLite JDBC driver (`sqlite-jdbc-3.50.3.0.jar`)

---

## Installation & Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system
   ```

2. **Download SQLite JDBC Driver** (if not already included):

   - [Download sqlite-jdbc-3.50.3.0.jar](https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.50.3.0/sqlite-jdbc-3.50.3.0.jar)
   - Place it in the root project folder.

3. **Compile and run** using the provided batch file (`setup.bat`):

   ```bash
   setup.bat
   ```

   This script:
   - Checks if Java is installed.
   - Compiles the Java files.
   - Launches the Library Management System.

---

## Project Structure

```
LibraryManagementSystem/
├─ src/
│  └─ com/library/system/
│     ├─ LibraryManagement.java
│     └─ Database.java
├─ build/
├─ sqlite-jdbc-3.50.3.0.jar
└─ setup.bat
```

- `LibraryManagement.java`: Main GUI and application logic.  
- `Database.java`: Handles SQLite database connections and operations.  
- `setup.bat`: Batch file for compilation and running the application.  

---

## Usage

1. **Books Tab**
   - Add new books with details like title, author, genre, publication date, and ISBN.
   - Remove books by entering the Book ID.
   - Search books by title or author.
   - Refresh the table to see updated data.

2. **Borrowers Tab**
   - Add new borrowers with their information.
   - Remove borrowers by entering the Borrower ID.
   - Refresh table to see updated data.

3. **Checkouts Tab**
   - Add checkout records linking books and borrowers.
   - Remove checkout records by entering the Checkout ID.
   - Refresh table to see latest checkout information.

---

## Contributing

Contributions are welcome!  
If you want to suggest features or fix bugs:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a Pull Request.

---

## License

This project is **MIT Licensed**. See `LICENSE` for details.

---

## Screenshots

![Books Tab](screenshots/books_tab.png)  
![Borrowers Tab](screenshots/borrowers_tab.png)  
![Checkouts Tab](screenshots/checkouts_tab.png)  

---

## Author

**Your Name** – [Your GitHub](https://github.com/your-username)  

---

> Built with ❤️ using Java, Swing & SQLite

