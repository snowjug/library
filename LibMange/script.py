# Create the Database.java file for the Library Management System
database_java_content = '''package com.library.system;

import javax.swing.table.DefaultTableModel;
import java.sql.*;

public class Database {
    // declaring the database path - SQLite database will be created in project root
    private final static String DB_URL = "jdbc:sqlite:library.db";
    
    // Method to create database with the three tables: books, borrowers and checkouts
    static void createDatabase() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             Statement stmt = conn.createStatement()) {
            
            // Create Books table
            String createBooksTable = "CREATE TABLE IF NOT EXISTS books (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "title TEXT NOT NULL, " +
                    "author TEXT NOT NULL, " +
                    "genre TEXT, " +
                    "publication_date TEXT, " +
                    "isbn TEXT, " +
                    "available INTEGER DEFAULT 1" +
                    ")";
            stmt.executeUpdate(createBooksTable);
            
            // Create Borrowers table
            String createBorrowersTable = "CREATE TABLE IF NOT EXISTS borrowers (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "name TEXT NOT NULL, " +
                    "email TEXT UNIQUE NOT NULL, " +
                    "phone TEXT, " +
                    "address TEXT" +
                    ")";
            stmt.executeUpdate(createBorrowersTable);
            
            // Create Checkouts table
            String createCheckoutsTable = "CREATE TABLE IF NOT EXISTS checkouts (" +
                    "id INTEGER PRIMARY KEY AUTOINCREMENT, " +
                    "book_id INTEGER NOT NULL, " +
                    "borrower_id INTEGER NOT NULL, " +
                    "checkout_date TEXT NOT NULL, " +
                    "due_date TEXT NOT NULL, " +
                    "return_date TEXT, " +
                    "FOREIGN KEY (book_id) REFERENCES books(id), " +
                    "FOREIGN KEY (borrower_id) REFERENCES borrowers(id)" +
                    ")";
            stmt.executeUpdate(createCheckoutsTable);
            
            System.out.println("Database and tables created successfully!");
            
        } catch (SQLException e) {
            System.err.println("Error creating database: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // Method to add the book into the database
    static void addBook(String title, String author, String genre, 
                       String publicationDate, String isbn, boolean available) throws SQLException {
        String insertBookQuery = "INSERT INTO books (title, author, genre, publication_date, isbn, available) VALUES (?, ?, ?, ?, ?, ?)";
        
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement insertBookStmt = conn.prepareStatement(insertBookQuery)) {
            
            insertBookStmt.setString(1, title);
            insertBookStmt.setString(2, author);
            insertBookStmt.setString(3, genre);
            insertBookStmt.setString(4, publicationDate);
            insertBookStmt.setString(5, isbn);
            insertBookStmt.setBoolean(6, available);
            insertBookStmt.executeUpdate();
            
            System.out.println("Book added successfully: " + title);
        }
    }
    
    // Method to add the borrower into the database
    static void addBorrower(String name, String email, String phone, String address) throws SQLException {
        String query = "INSERT INTO borrowers (name,email,phone,address) VALUES (?, ?, ?, ?)";
        
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement insertBorrower = conn.prepareStatement(query)) {
            
            insertBorrower.setString(1, name);
            insertBorrower.setString(2, email);
            insertBorrower.setString(3, phone);
            insertBorrower.setString(4, address);
            insertBorrower.executeUpdate();
            
            System.out.println("Borrower added successfully: " + name);
        }
    }
    
    // Method to add checkout into the database
    static void addCheckout(String bookID, String borrowerID, String checkoutDate,
                           String dueDate, String returnDate) throws SQLException {
        String query = "INSERT INTO checkouts(book_id,borrower_id,checkout_date,due_date,return_date) VALUES (?, ?, ?, ?, ?)";
        
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement insertCheckout = conn.prepareStatement(query)) {
            
            insertCheckout.setInt(1, Integer.valueOf(bookID));
            insertCheckout.setInt(2, Integer.valueOf(borrowerID));
            insertCheckout.setString(3, checkoutDate);
            insertCheckout.setString(4, dueDate);
            insertCheckout.setString(5, returnDate);
            insertCheckout.executeUpdate();
            
            System.out.println("Checkout added successfully!");
        }
    }
    
    // Method to delete the entry from the database given the id and the table name
    static void delete(String tableName, String id) throws SQLException {
        String query = "DELETE FROM " + tableName + " WHERE id = ?";
        
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement deleteStmt = conn.prepareStatement(query)) {
            
            deleteStmt.setInt(1, Integer.valueOf(id));
            deleteStmt.executeUpdate();
            
            System.out.println("Record deleted successfully from " + tableName);
        }
    }
    
    // Method to refresh the tables with the updated data from the database
    static void refreshTables(DefaultTableModel bookModel, DefaultTableModel borrowerModel, 
                             DefaultTableModel checkoutModel) {
        // Clear existing data
        bookModel.setRowCount(0);
        borrowerModel.setRowCount(0);
        checkoutModel.setRowCount(0);
        
        try (Connection conn = DriverManager.getConnection(DB_URL)) {
            
            // Refresh Books table
            String selectBooksQuery = "SELECT id, title, author, genre, publication_date, isbn, available FROM books";
            try (PreparedStatement selectBooksStmt = conn.prepareStatement(selectBooksQuery);
                 ResultSet bookResults = selectBooksStmt.executeQuery()) {
                
                while (bookResults.next()) {
                    Object[] bookData = {
                        bookResults.getInt("id"),
                        bookResults.getString("title"),
                        bookResults.getString("author"),
                        bookResults.getString("genre"),
                        bookResults.getString("publication_date"),
                        bookResults.getString("isbn"),
                        bookResults.getBoolean("available") ? "Yes" : "No"
                    };
                    bookModel.addRow(bookData);
                }
            }
            
            // Refresh Borrowers table
            String selectBorrowersQuery = "SELECT id, name, email, phone, address FROM borrowers";
            try (PreparedStatement selectBorrowersStmt = conn.prepareStatement(selectBorrowersQuery);
                 ResultSet borrowerResults = selectBorrowersStmt.executeQuery()) {
                
                while (borrowerResults.next()) {
                    Object[] borrowerData = {
                        borrowerResults.getInt("id"),
                        borrowerResults.getString("name"),
                        borrowerResults.getString("email"),
                        borrowerResults.getString("phone"),
                        borrowerResults.getString("address")
                    };
                    borrowerModel.addRow(borrowerData);
                }
            }
            
            // Refresh Checkouts table
            String selectCheckoutsQuery = "SELECT id, book_id, borrower_id, checkout_date, due_date, return_date FROM checkouts";
            try (PreparedStatement selectCheckoutsStmt = conn.prepareStatement(selectCheckoutsQuery);
                 ResultSet checkoutResults = selectCheckoutsStmt.executeQuery()) {
                
                while (checkoutResults.next()) {
                    Object[] checkoutData = {
                        checkoutResults.getInt("id"),
                        checkoutResults.getInt("book_id"),
                        checkoutResults.getInt("borrower_id"),
                        checkoutResults.getString("checkout_date"),
                        checkoutResults.getString("due_date"),
                        checkoutResults.getString("return_date")
                    };
                    checkoutModel.addRow(checkoutData);
                }
            }
            
        } catch (SQLException e) {
            System.err.println("Error refreshing tables: " + e.getMessage());
            e.printStackTrace();
        }
    }
    
    // Method to search books by title or author
    static void searchBooks(DefaultTableModel bookModel, String searchTerm) {
        bookModel.setRowCount(0);
        
        String query = "SELECT id, title, author, genre, publication_date, isbn, available FROM books WHERE title LIKE ? OR author LIKE ?";
        
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement searchStmt = conn.prepareStatement(query)) {
            
            searchStmt.setString(1, "%" + searchTerm + "%");
            searchStmt.setString(2, "%" + searchTerm + "%");
            
            try (ResultSet results = searchStmt.executeQuery()) {
                while (results.next()) {
                    Object[] bookData = {
                        results.getInt("id"),
                        results.getString("title"),
                        results.getString("author"),
                        results.getString("genre"),
                        results.getString("publication_date"),
                        results.getString("isbn"),
                        results.getBoolean("available") ? "Yes" : "No"
                    };
                    bookModel.addRow(bookData);
                }
            }
            
        } catch (SQLException e) {
            System.err.println("Error searching books: " + e.getMessage());
        }
    }
}'''

# Save the Database.java file
with open("Database.java", "w", encoding="utf-8") as f:
    f.write(database_java_content)

print("Database.java file created successfully!")
print("File size:", len(database_java_content), "characters")