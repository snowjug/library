# Create the LibraryManagement.java file for the main GUI application
library_management_content = '''package com.library.system;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.SQLException;
import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTabbedPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;
import javax.swing.table.DefaultTableModel;
import javax.swing.border.EmptyBorder;

public class LibraryManagement extends JFrame {
    
    // Table column definitions
    private final String[] bookColumns = {"ID", "Title", "Author", "Genre", "Publication Date", "ISBN", "Available"};
    private final String[] borrowerColumns = {"ID", "Name", "Email", "Phone", "Address"};
    private final String[] checkoutColumns = {"ID", "Book ID", "Borrower ID", "Checkout Date", "Due Date", "Return Date"};
    
    // GUI components
    private JTabbedPane tabbedPane;
    private JTable bookTable;
    private JTable borrowerTable;
    private JTable checkoutTable;
    
    // Book input fields
    private JTextField bookTitleField;
    private JTextField authorField;
    private JTextField genreField;
    private JTextField pubDateField;
    private JTextField isbnField;
    private JCheckBox availableField;
    private JTextField deleteBookField;
    private JTextField searchBookField;
    
    // Borrower input fields
    private JTextField nameField;
    private JTextField emailField;
    private JTextField phoneField;
    private JTextField addressField;
    private JTextField deleteBorrowerField;
    
    // Checkout input fields
    private JTextField bookIDField;
    private JTextField borrowerIDField;
    private JTextField checkoutDateField;
    private JTextField dueDateField;
    private JTextField returnDateField;
    private JTextField deleteCheckoutField;
    
    public LibraryManagement() {
        initializeComponents();
        setupGUI();
    }
    
    private void initializeComponents() {
        setTitle("Library Management System - Eclipse JDBC & Swing");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1000, 700);
        setLocationRelativeTo(null);
        getContentPane().setBackground(new Color(245, 245, 245));
        
        // Initialize database
        Database.createDatabase();
        
        // Create table models
        DefaultTableModel bookModel = new DefaultTableModel(bookColumns, 0);
        bookTable = new JTable(bookModel);
        bookTable.setRowHeight(25);
        
        DefaultTableModel borrowerModel = new DefaultTableModel(borrowerColumns, 0);
        borrowerTable = new JTable(borrowerModel);
        borrowerTable.setRowHeight(25);
        
        DefaultTableModel checkoutModel = new DefaultTableModel(checkoutColumns, 0);
        checkoutTable = new JTable(checkoutModel);
        checkoutTable.setRowHeight(25);
        
        // Initialize the tables with data
        Database.refreshTables(bookModel, borrowerModel, checkoutModel);
        
        // Create tabbed pane
        tabbedPane = new JTabbedPane();
        tabbedPane.addTab("Books", new JScrollPane(bookTable));
        tabbedPane.addTab("Borrowers", new JScrollPane(borrowerTable));
        tabbedPane.addTab("Checkouts", new JScrollPane(checkoutTable));
    }
    
    private void setupGUI() {
        // Create input panels for each tab
        JPanel bookPanel = createBookPanel();
        JPanel borrowerPanel = createBorrowerPanel();
        JPanel checkoutPanel = createCheckoutPanel();
        
        // Add change listener to tabbed pane
        tabbedPane.addChangeListener(new ChangeListener() {
            public void stateChanged(ChangeEvent e) {
                int selectedIndex = tabbedPane.getSelectedIndex();
                getContentPane().removeAll();
                
                if (selectedIndex == 0) { // Books tab
                    getContentPane().add(bookPanel, BorderLayout.NORTH);
                } else if (selectedIndex == 1) { // Borrowers tab
                    getContentPane().add(borrowerPanel, BorderLayout.NORTH);
                } else if (selectedIndex == 2) { // Checkouts tab
                    getContentPane().add(checkoutPanel, BorderLayout.NORTH);
                }
                
                getContentPane().add(tabbedPane, BorderLayout.CENTER);
                revalidate();
                repaint();
            }
        });
        
        // Set initial layout
        getContentPane().add(bookPanel, BorderLayout.NORTH);
        getContentPane().add(tabbedPane, BorderLayout.CENTER);
    }
    
    private JPanel createBookPanel() {
        JPanel panel = new JPanel(new GridLayout(0, 2, 10, 5));
        panel.setBorder(new EmptyBorder(10, 10, 10, 10));
        panel.setBackground(new Color(230, 230, 250));
        
        // Initialize text fields
        bookTitleField = new JTextField(20);
        authorField = new JTextField(20);
        genreField = new JTextField(20);
        pubDateField = new JTextField(10);
        isbnField = new JTextField(13);
        availableField = new JCheckBox("Available", true);
        deleteBookField = new JTextField(5);
        searchBookField = new JTextField(20);
        
        // Add components
        panel.add(new JLabel("Book Title:"));
        panel.add(bookTitleField);
        
        panel.add(new JLabel("Author:"));
        panel.add(authorField);
        
        panel.add(new JLabel("Genre:"));
        panel.add(genreField);
        
        panel.add(new JLabel("Publication Date (YYYY-MM-DD):"));
        panel.add(pubDateField);
        
        panel.add(new JLabel("ISBN:"));
        panel.add(isbnField);
        
        panel.add(new JLabel("Available:"));
        panel.add(availableField);
        
        // Buttons
        JButton addBookButton = new JButton("Add Book");
        addBookButton.setBackground(new Color(60, 179, 113));
        addBookButton.setForeground(Color.WHITE);
        addBookButton.addActionListener(new AddBookListener());
        
        JButton removeBookButton = new JButton("Remove Book");
        removeBookButton.setBackground(new Color(220, 20, 60));
        removeBookButton.setForeground(Color.WHITE);
        removeBookButton.addActionListener(new RemoveBookListener());
        
        JButton searchBookButton = new JButton("Search Books");
        searchBookButton.setBackground(new Color(30, 144, 255));
        searchBookButton.setForeground(Color.WHITE);
        searchBookButton.addActionListener(new SearchBookListener());
        
        JButton refreshBooksButton = new JButton("Refresh All Books");
        refreshBooksButton.setBackground(new Color(255, 165, 0));
        refreshBooksButton.setForeground(Color.WHITE);
        refreshBooksButton.addActionListener(new RefreshTablesListener());
        
        panel.add(addBookButton);
        panel.add(removeBookButton);
        
        panel.add(new JLabel("Search (Title/Author):"));
        panel.add(searchBookField);
        
        panel.add(searchBookButton);
        panel.add(refreshBooksButton);
        
        panel.add(new JLabel("Delete Book ID:"));
        panel.add(deleteBookField);
        
        return panel;
    }
    
    private JPanel createBorrowerPanel() {
        JPanel panel = new JPanel(new GridLayout(0, 2, 10, 5));
        panel.setBorder(new EmptyBorder(10, 10, 10, 10));
        panel.setBackground(new Color(255, 248, 220));
        
        // Initialize text fields
        nameField = new JTextField(20);
        emailField = new JTextField(20);
        phoneField = new JTextField(15);
        addressField = new JTextField(30);
        deleteBorrowerField = new JTextField(5);
        
        // Add components
        panel.add(new JLabel("Name:"));
        panel.add(nameField);
        
        panel.add(new JLabel("Email:"));
        panel.add(emailField);
        
        panel.add(new JLabel("Phone:"));
        panel.add(phoneField);
        
        panel.add(new JLabel("Address:"));
        panel.add(addressField);
        
        // Buttons
        JButton addBorrowerButton = new JButton("Add Borrower");
        addBorrowerButton.setBackground(new Color(60, 179, 113));
        addBorrowerButton.setForeground(Color.WHITE);
        addBorrowerButton.addActionListener(new AddBorrowerListener());
        
        JButton removeBorrowerButton = new JButton("Remove Borrower");
        removeBorrowerButton.setBackground(new Color(220, 20, 60));
        removeBorrowerButton.setForeground(Color.WHITE);
        removeBorrowerButton.addActionListener(new RemoveBorrowerListener());
        
        JButton refreshBorrowersButton = new JButton("Refresh All");
        refreshBorrowersButton.setBackground(new Color(255, 165, 0));
        refreshBorrowersButton.setForeground(Color.WHITE);
        refreshBorrowersButton.addActionListener(new RefreshTablesListener());
        
        panel.add(addBorrowerButton);
        panel.add(removeBorrowerButton);
        
        panel.add(new JLabel("Delete Borrower ID:"));
        panel.add(deleteBorrowerField);
        
        panel.add(refreshBorrowersButton);
        panel.add(new JLabel("")); // Empty space
        
        return panel;
    }
    
    private JPanel createCheckoutPanel() {
        JPanel panel = new JPanel(new GridLayout(0, 2, 10, 5));
        panel.setBorder(new EmptyBorder(10, 10, 10, 10));
        panel.setBackground(new Color(240, 248, 255));
        
        // Initialize text fields
        bookIDField = new JTextField(10);
        borrowerIDField = new JTextField(10);
        checkoutDateField = new JTextField(10);
        dueDateField = new JTextField(10);
        returnDateField = new JTextField(10);
        deleteCheckoutField = new JTextField(5);
        
        // Add components
        panel.add(new JLabel("Book ID:"));
        panel.add(bookIDField);
        
        panel.add(new JLabel("Borrower ID:"));
        panel.add(borrowerIDField);
        
        panel.add(new JLabel("Checkout Date (YYYY-MM-DD):"));
        panel.add(checkoutDateField);
        
        panel.add(new JLabel("Due Date (YYYY-MM-DD):"));
        panel.add(dueDateField);
        
        panel.add(new JLabel("Return Date (YYYY-MM-DD):"));
        panel.add(returnDateField);
        
        // Buttons
        JButton addCheckoutButton = new JButton("Add Checkout");
        addCheckoutButton.setBackground(new Color(60, 179, 113));
        addCheckoutButton.setForeground(Color.WHITE);
        addCheckoutButton.addActionListener(new AddCheckoutListener());
        
        JButton removeCheckoutButton = new JButton("Remove Checkout");
        removeCheckoutButton.setBackground(new Color(220, 20, 60));
        removeCheckoutButton.setForeground(Color.WHITE);
        removeCheckoutButton.addActionListener(new RemoveCheckoutListener());
        
        JButton refreshCheckoutsButton = new JButton("Refresh All");
        refreshCheckoutsButton.setBackground(new Color(255, 165, 0));
        refreshCheckoutsButton.setForeground(Color.WHITE);
        refreshCheckoutsButton.addActionListener(new RefreshTablesListener());
        
        panel.add(addCheckoutButton);
        panel.add(removeCheckoutButton);
        
        panel.add(new JLabel("Delete Checkout ID:"));
        panel.add(deleteCheckoutField);
        
        panel.add(refreshCheckoutsButton);
        panel.add(new JLabel("")); // Empty space
        
        return panel;
    }
    
    // Event Listeners
    private class AddBookListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (bookTitleField.getText().trim().isEmpty() || authorField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please fill in at least Title and Author fields.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                Database.addBook(
                    bookTitleField.getText().trim(),
                    authorField.getText().trim(),
                    genreField.getText().trim(),
                    pubDateField.getText().trim(),
                    isbnField.getText().trim(),
                    availableField.isSelected()
                );
                
                refreshAllTables();
                clearBookFields();
                
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Book added successfully!", 
                    "Success", JOptionPane.INFORMATION_MESSAGE);
                    
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error adding book: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class RemoveBookListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (deleteBookField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please enter a Book ID to delete.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                int confirm = JOptionPane.showConfirmDialog(LibraryManagement.this, 
                    "Are you sure you want to delete this book?", 
                    "Confirm Deletion", JOptionPane.YES_NO_OPTION);
                    
                if (confirm == JOptionPane.YES_OPTION) {
                    Database.delete("books", deleteBookField.getText().trim());
                    refreshAllTables();
                    deleteBookField.setText("");
                    
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Book deleted successfully!", 
                        "Success", JOptionPane.INFORMATION_MESSAGE);
                }
                
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error deleting book: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class SearchBookListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            String searchTerm = searchBookField.getText().trim();
            if (searchTerm.isEmpty()) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Please enter a search term.", 
                    "Missing Information", JOptionPane.WARNING_MESSAGE);
                return;
            }
            
            DefaultTableModel bookModel = (DefaultTableModel) bookTable.getModel();
            Database.searchBooks(bookModel, searchTerm);
        }
    }
    
    private class AddBorrowerListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (nameField.getText().trim().isEmpty() || emailField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please fill in at least Name and Email fields.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                Database.addBorrower(
                    nameField.getText().trim(),
                    emailField.getText().trim(),
                    phoneField.getText().trim(),
                    addressField.getText().trim()
                );
                
                refreshAllTables();
                clearBorrowerFields();
                
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Borrower added successfully!", 
                    "Success", JOptionPane.INFORMATION_MESSAGE);
                    
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error adding borrower: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class RemoveBorrowerListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (deleteBorrowerField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please enter a Borrower ID to delete.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                int confirm = JOptionPane.showConfirmDialog(LibraryManagement.this, 
                    "Are you sure you want to delete this borrower?", 
                    "Confirm Deletion", JOptionPane.YES_NO_OPTION);
                    
                if (confirm == JOptionPane.YES_OPTION) {
                    Database.delete("borrowers", deleteBorrowerField.getText().trim());
                    refreshAllTables();
                    deleteBorrowerField.setText("");
                    
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Borrower deleted successfully!", 
                        "Success", JOptionPane.INFORMATION_MESSAGE);
                }
                
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error deleting borrower: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class AddCheckoutListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (bookIDField.getText().trim().isEmpty() || borrowerIDField.getText().trim().isEmpty() ||
                    checkoutDateField.getText().trim().isEmpty() || dueDateField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please fill in Book ID, Borrower ID, Checkout Date, and Due Date.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                Database.addCheckout(
                    bookIDField.getText().trim(),
                    borrowerIDField.getText().trim(),
                    checkoutDateField.getText().trim(),
                    dueDateField.getText().trim(),
                    returnDateField.getText().trim()
                );
                
                refreshAllTables();
                clearCheckoutFields();
                
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Checkout added successfully!", 
                    "Success", JOptionPane.INFORMATION_MESSAGE);
                    
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error adding checkout: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class RemoveCheckoutListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            try {
                if (deleteCheckoutField.getText().trim().isEmpty()) {
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Please enter a Checkout ID to delete.", 
                        "Missing Information", JOptionPane.WARNING_MESSAGE);
                    return;
                }
                
                int confirm = JOptionPane.showConfirmDialog(LibraryManagement.this, 
                    "Are you sure you want to delete this checkout record?", 
                    "Confirm Deletion", JOptionPane.YES_NO_OPTION);
                    
                if (confirm == JOptionPane.YES_OPTION) {
                    Database.delete("checkouts", deleteCheckoutField.getText().trim());
                    refreshAllTables();
                    deleteCheckoutField.setText("");
                    
                    JOptionPane.showMessageDialog(LibraryManagement.this, 
                        "Checkout record deleted successfully!", 
                        "Success", JOptionPane.INFORMATION_MESSAGE);
                }
                
            } catch (SQLException ex) {
                JOptionPane.showMessageDialog(LibraryManagement.this, 
                    "Error deleting checkout: " + ex.getMessage(), 
                    "Database Error", JOptionPane.ERROR_MESSAGE);
            }
        }
    }
    
    private class RefreshTablesListener implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            refreshAllTables();
            JOptionPane.showMessageDialog(LibraryManagement.this, 
                "All tables refreshed successfully!", 
                "Refreshed", JOptionPane.INFORMATION_MESSAGE);
        }
    }
    
    // Helper methods
    private void refreshAllTables() {
        DefaultTableModel bookModel = (DefaultTableModel) bookTable.getModel();
        DefaultTableModel borrowerModel = (DefaultTableModel) borrowerTable.getModel();
        DefaultTableModel checkoutModel = (DefaultTableModel) checkoutTable.getModel();
        Database.refreshTables(bookModel, borrowerModel, checkoutModel);
    }
    
    private void clearBookFields() {
        bookTitleField.setText("");
        authorField.setText("");
        genreField.setText("");
        pubDateField.setText("");
        isbnField.setText("");
        availableField.setSelected(true);
    }
    
    private void clearBorrowerFields() {
        nameField.setText("");
        emailField.setText("");
        phoneField.setText("");
        addressField.setText("");
    }
    
    private void clearCheckoutFields() {
        bookIDField.setText("");
        borrowerIDField.setText("");
        checkoutDateField.setText("");
        dueDateField.setText("");
        returnDateField.setText("");
    }
    
    public static void main(String[] args) {
        // Set the look and feel to the system look and feel
        try {
            javax.swing.UIManager.setLookAndFeel(javax.swing.UIManager.getSystemLookAndFeel());
        } catch (Exception e) {
            // If system look and feel is not available, use default
        }
        
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                new LibraryManagement().setVisible(true);
            }
        });
    }
}'''

# Save the LibraryManagement.java file
with open("LibraryManagement.java", "w", encoding="utf-8") as f:
    f.write(library_management_content)

print("LibraryManagement.java file created successfully!")
print("File size:", len(library_management_content), "characters")