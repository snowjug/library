package com.library.system;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import javax.swing.event.*;
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

                if (selectedIndex == 0) getContentPane().add(bookPanel, BorderLayout.NORTH);
                else if (selectedIndex == 1) getContentPane().add(borrowerPanel, BorderLayout.NORTH);
                else if (selectedIndex == 2) getContentPane().add(checkoutPanel, BorderLayout.NORTH);

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

        bookTitleField = new JTextField(20);
        authorField = new JTextField(20);
        genreField = new JTextField(20);
        pubDateField = new JTextField(10);
        isbnField = new JTextField(13);
        availableField = new JCheckBox("Available", true);
        deleteBookField = new JTextField(5);
        searchBookField = new JTextField(20);

        panel.add(new JLabel("Book Title:")); panel.add(bookTitleField);
        panel.add(new JLabel("Author:")); panel.add(authorField);
        panel.add(new JLabel("Genre:")); panel.add(genreField);
        panel.add(new JLabel("Publication Date (YYYY-MM-DD):")); panel.add(pubDateField);
        panel.add(new JLabel("ISBN:")); panel.add(isbnField);
        panel.add(new JLabel("Available:")); panel.add(availableField);

        JButton addBookButton = new JButton("Add Book");
        addBookButton.setBackground(new Color(60, 179, 113)); addBookButton.setForeground(Color.WHITE);
        addBookButton.addActionListener(e -> {
            if (bookTitleField.getText().trim().isEmpty() || authorField.getText().trim().isEmpty()) {
                JOptionPane.showMessageDialog(LibraryManagement.this, "Please fill in at least Title and Author fields.", "Missing Information", JOptionPane.WARNING_MESSAGE);
                return;
            }
            Database.addBook(bookTitleField.getText().trim(), authorField.getText().trim(),
                             genreField.getText().trim(), pubDateField.getText().trim(),
                             isbnField.getText().trim(), availableField.isSelected());
            refreshAllTables();
            clearBookFields();
            JOptionPane.showMessageDialog(LibraryManagement.this, "Book added successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
        });

        JButton removeBookButton = new JButton("Remove Book");
        removeBookButton.setBackground(new Color(220, 20, 60)); removeBookButton.setForeground(Color.WHITE);
        removeBookButton.addActionListener(e -> {
            if (!deleteBookField.getText().trim().isEmpty()) {
                Database.delete("books", deleteBookField.getText().trim());
                refreshAllTables();
                deleteBookField.setText("");
                JOptionPane.showMessageDialog(LibraryManagement.this, "Book deleted successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(LibraryManagement.this, "Enter Book ID to delete.", "Warning", JOptionPane.WARNING_MESSAGE);
            }
        });

        JButton searchBookButton = new JButton("Search Books");
        searchBookButton.setBackground(new Color(30, 144, 255)); searchBookButton.setForeground(Color.WHITE);
        searchBookButton.addActionListener(e -> {
            String searchTerm = searchBookField.getText().trim();
            if (!searchTerm.isEmpty()) Database.searchBooks((DefaultTableModel) bookTable.getModel(), searchTerm);
        });

        JButton refreshBooksButton = new JButton("Refresh All Books");
        refreshBooksButton.setBackground(new Color(255, 165, 0)); refreshBooksButton.setForeground(Color.WHITE);
        refreshBooksButton.addActionListener(e -> refreshAllTables());

        panel.add(addBookButton); panel.add(removeBookButton);
        panel.add(new JLabel("Search (Title/Author):")); panel.add(searchBookField);
        panel.add(searchBookButton); panel.add(refreshBooksButton);
        panel.add(new JLabel("Delete Book ID:")); panel.add(deleteBookField);

        return panel;
    }

    private JPanel createBorrowerPanel() {
        JPanel panel = new JPanel(new GridLayout(0, 2, 10, 5));
        panel.setBorder(new EmptyBorder(10, 10, 10, 10)); panel.setBackground(new Color(255, 248, 220));

        nameField = new JTextField(20); emailField = new JTextField(20);
        phoneField = new JTextField(15); addressField = new JTextField(30);
        deleteBorrowerField = new JTextField(5);

        panel.add(new JLabel("Name:")); panel.add(nameField);
        panel.add(new JLabel("Email:")); panel.add(emailField);
        panel.add(new JLabel("Phone:")); panel.add(phoneField);
        panel.add(new JLabel("Address:")); panel.add(addressField);

        JButton addBorrowerButton = new JButton("Add Borrower");
        addBorrowerButton.setBackground(new Color(60, 179, 113)); addBorrowerButton.setForeground(Color.WHITE);
        addBorrowerButton.addActionListener(e -> {
            if (!nameField.getText().trim().isEmpty() && !emailField.getText().trim().isEmpty()) {
                Database.addBorrower(nameField.getText().trim(), emailField.getText().trim(),
                                     phoneField.getText().trim(), addressField.getText().trim());
                refreshAllTables(); clearBorrowerFields();
                JOptionPane.showMessageDialog(LibraryManagement.this, "Borrower added successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        JButton removeBorrowerButton = new JButton("Remove Borrower");
        removeBorrowerButton.setBackground(new Color(220, 20, 60)); removeBorrowerButton.setForeground(Color.WHITE);
        removeBorrowerButton.addActionListener(e -> {
            if (!deleteBorrowerField.getText().trim().isEmpty()) {
                Database.delete("borrowers", deleteBorrowerField.getText().trim());
                refreshAllTables(); deleteBorrowerField.setText("");
                JOptionPane.showMessageDialog(LibraryManagement.this, "Borrower deleted successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        JButton refreshBorrowersButton = new JButton("Refresh All");
        refreshBorrowersButton.setBackground(new Color(255, 165, 0)); refreshBorrowersButton.setForeground(Color.WHITE);
        refreshBorrowersButton.addActionListener(e -> refreshAllTables());

        panel.add(addBorrowerButton); panel.add(removeBorrowerButton);
        panel.add(new JLabel("Delete Borrower ID:")); panel.add(deleteBorrowerField);
        panel.add(refreshBorrowersButton); panel.add(new JLabel(""));

        return panel;
    }

    private JPanel createCheckoutPanel() {
        JPanel panel = new JPanel(new GridLayout(0, 2, 10, 5));
        panel.setBorder(new EmptyBorder(10, 10, 10, 10)); panel.setBackground(new Color(240, 248, 255));

        bookIDField = new JTextField(10); borrowerIDField = new JTextField(10);
        checkoutDateField = new JTextField(10); dueDateField = new JTextField(10);
        returnDateField = new JTextField(10); deleteCheckoutField = new JTextField(5);

        panel.add(new JLabel("Book ID:")); panel.add(bookIDField);
        panel.add(new JLabel("Borrower ID:")); panel.add(borrowerIDField);
        panel.add(new JLabel("Checkout Date (YYYY-MM-DD):")); panel.add(checkoutDateField);
        panel.add(new JLabel("Due Date (YYYY-MM-DD):")); panel.add(dueDateField);
        panel.add(new JLabel("Return Date (YYYY-MM-DD):")); panel.add(returnDateField);

        JButton addCheckoutButton = new JButton("Add Checkout");
        addCheckoutButton.setBackground(new Color(60, 179, 113)); addCheckoutButton.setForeground(Color.WHITE);
        addCheckoutButton.addActionListener(e -> {
            if (!bookIDField.getText().trim().isEmpty() && !borrowerIDField.getText().trim().isEmpty() &&
                !checkoutDateField.getText().trim().isEmpty() && !dueDateField.getText().trim().isEmpty()) {
                Database.addCheckout(bookIDField.getText().trim(), borrowerIDField.getText().trim(),
                                     checkoutDateField.getText().trim(), dueDateField.getText().trim(),
                                     returnDateField.getText().trim().isEmpty() ? null : returnDateField.getText().trim());
                refreshAllTables(); clearCheckoutFields();
                JOptionPane.showMessageDialog(LibraryManagement.this, "Checkout added successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        JButton removeCheckoutButton = new JButton("Remove Checkout");
        removeCheckoutButton.setBackground(new Color(220, 20, 60)); removeCheckoutButton.setForeground(Color.WHITE);
        removeCheckoutButton.addActionListener(e -> {
            if (!deleteCheckoutField.getText().trim().isEmpty()) {
                Database.delete("checkouts", deleteCheckoutField.getText().trim());
                refreshAllTables(); deleteCheckoutField.setText("");
                JOptionPane.showMessageDialog(LibraryManagement.this, "Checkout deleted successfully!", "Success", JOptionPane.INFORMATION_MESSAGE);
            }
        });

        JButton refreshCheckoutsButton = new JButton("Refresh All");
        refreshCheckoutsButton.setBackground(new Color(255, 165, 0)); refreshCheckoutsButton.setForeground(Color.WHITE);
        refreshCheckoutsButton.addActionListener(e -> refreshAllTables());

        panel.add(addCheckoutButton); panel.add(removeCheckoutButton);
        panel.add(new JLabel("Delete Checkout ID:")); panel.add(deleteCheckoutField);
        panel.add(refreshCheckoutsButton); panel.add(new JLabel(""));

        return panel;
    }

    private void refreshAllTables() {
        Database.refreshTables((DefaultTableModel) bookTable.getModel(),
                               (DefaultTableModel) borrowerTable.getModel(),
                               (DefaultTableModel) checkoutTable.getModel());
    }

    private void clearBookFields() { bookTitleField.setText(""); authorField.setText(""); genreField.setText(""); pubDateField.setText(""); isbnField.setText(""); availableField.setSelected(true);}
    private void clearBorrowerFields() { nameField.setText(""); emailField.setText(""); phoneField.setText(""); addressField.setText(""); }
    private void clearCheckoutFields() { bookIDField.setText(""); borrowerIDField.setText(""); checkoutDateField.setText(""); dueDateField.setText(""); returnDateField.setText(""); }

    public static void main(String[] args) {
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
        } catch (Exception e) { }

        SwingUtilities.invokeLater(() -> new LibraryManagement().setVisible(true));
    }
}
