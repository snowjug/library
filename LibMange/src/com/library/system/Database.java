package com.library.system;

import java.sql.*;
import javax.swing.table.DefaultTableModel;

public class Database {
    private static final String DB_URL = "jdbc:sqlite:library.db";

    // Create database and tables if they don't exist
    public static void createDatabase() {
        try (Connection conn = DriverManager.getConnection(DB_URL);
             Statement stmt = conn.createStatement()) {

            stmt.execute("CREATE TABLE IF NOT EXISTS books (" +
                    "id TEXT PRIMARY KEY, " +
                    "title TEXT, " +
                    "author TEXT, " +
                    "genre TEXT, " +
                    "pubDate TEXT, " +
                    "isbn TEXT, " +
                    "available INTEGER)");

            stmt.execute("CREATE TABLE IF NOT EXISTS borrowers (" +
                    "id TEXT PRIMARY KEY, " +
                    "name TEXT, " +
                    "email TEXT, " +
                    "phone TEXT, " +
                    "address TEXT)");

            stmt.execute("CREATE TABLE IF NOT EXISTS checkouts (" +
                    "id TEXT PRIMARY KEY, " +
                    "bookId TEXT, " +
                    "borrowerId TEXT, " +
                    "checkoutDate TEXT, " +
                    "dueDate TEXT, " +
                    "returnDate TEXT, " +
                    "FOREIGN KEY(bookId) REFERENCES books(id), " +
                    "FOREIGN KEY(borrowerId) REFERENCES borrowers(id))");

            System.out.println("Database created and ready.");

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Refresh JTable models
    public static void refreshTables(DefaultTableModel bookModel,
                                     DefaultTableModel borrowerModel,
                                     DefaultTableModel checkoutModel) {
        loadTable(bookModel, "books");
        loadTable(borrowerModel, "borrowers");
        loadTable(checkoutModel, "checkouts");
    }

    private static void loadTable(DefaultTableModel model, String tableName) {
        model.setRowCount(0);
        try (Connection conn = DriverManager.getConnection(DB_URL);
             Statement stmt = conn.createStatement();
             ResultSet rs = stmt.executeQuery("SELECT * FROM " + tableName)) {

            int columnCount = rs.getMetaData().getColumnCount();
            while (rs.next()) {
                Object[] row = new Object[columnCount];
                for (int i = 1; i <= columnCount; i++) {
                    row[i - 1] = rs.getObject(i);
                }
                model.addRow(row);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Add book
    public static void addBook(String title, String author, String genre, String pubDate, String isbn, boolean available) {
        String sql = "INSERT INTO books (id, title, author, genre, pubDate, isbn, available) VALUES (?, ?, ?, ?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement ps = conn.prepareStatement(sql)) {

            String id = "B" + System.currentTimeMillis(); // generate unique ID
            ps.setString(1, id);
            ps.setString(2, title);
            ps.setString(3, author);
            ps.setString(4, genre);
            ps.setString(5, pubDate);
            ps.setString(6, isbn);
            ps.setInt(7, available ? 1 : 0);

            ps.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Add borrower
    public static void addBorrower(String name, String email, String phone, String address) {
        String sql = "INSERT INTO borrowers (id, name, email, phone, address) VALUES (?, ?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement ps = conn.prepareStatement(sql)) {

            String id = "U" + System.currentTimeMillis(); // unique ID
            ps.setString(1, id);
            ps.setString(2, name);
            ps.setString(3, email);
            ps.setString(4, phone);
            ps.setString(5, address);

            ps.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Add checkout
    public static void addCheckout(String bookId, String borrowerId, String checkoutDate, String dueDate, String returnDate) {
        String sql = "INSERT INTO checkouts (id, bookId, borrowerId, checkoutDate, dueDate, returnDate) VALUES (?, ?, ?, ?, ?, ?)";
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement ps = conn.prepareStatement(sql)) {

            String id = "C" + System.currentTimeMillis(); // unique ID
            ps.setString(1, id);
            ps.setString(2, bookId);
            ps.setString(3, borrowerId);
            ps.setString(4, checkoutDate);
            ps.setString(5, dueDate);
            ps.setString(6, returnDate); // can be null

            ps.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Delete record by table and ID
    public static void delete(String table, String id) {
        String sql = "DELETE FROM " + table + " WHERE id = ?";
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement ps = conn.prepareStatement(sql)) {

            ps.setString(1, id);
            ps.executeUpdate();

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Search books
    public static void searchBooks(DefaultTableModel bookModel, String searchTerm) {
        bookModel.setRowCount(0);
        String sql = "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR genre LIKE ? OR isbn LIKE ?";
        try (Connection conn = DriverManager.getConnection(DB_URL);
             PreparedStatement ps = conn.prepareStatement(sql)) {

            String term = "%" + searchTerm + "%";
            ps.setString(1, term);
            ps.setString(2, term);
            ps.setString(3, term);
            ps.setString(4, term);

            ResultSet rs = ps.executeQuery();
            int columnCount = rs.getMetaData().getColumnCount();
            while (rs.next()) {
                Object[] row = new Object[columnCount];
                for (int i = 1; i <= columnCount; i++) row[i - 1] = rs.getObject(i);
                bookModel.addRow(row);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
