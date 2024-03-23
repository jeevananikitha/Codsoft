import tkinter as tk
from tkinter import simpledialog, messagebox


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        return self.contacts

    def search_contact(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]

    def update_contact(self, name, phone, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone = phone
                contact.email = email
                contact.address = address
                return True
        return False

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                return True
        return False


def add_contact():
    name = simpledialog.askstring("Name", "Enter contact name:")
    phone = simpledialog.askstring("Phone", "Enter contact phone number:")
    email = simpledialog.askstring("Email", "Enter contact email:")
    address = simpledialog.askstring("Address", "Enter contact address:")
    contact = Contact(name, phone, email, address)
    contact_book.add_contact(contact)
    messagebox.showinfo("Success", "Contact added successfully!")


def view_contacts():
    contacts = contact_book.view_contacts()
    contacts_str = "\n".join(
        [f"{contact.name} - {contact.phone}" for contact in contacts])
    messagebox.showinfo("Contacts", contacts_str)


def search_contacts():
    search_term = simpledialog.askstring(
        "Search", "Enter name or phone number to search:")
    results = contact_book.search_contact(search_term)
    results_str = "\n".join(
        [f"{contact.name} - {contact.phone}" for contact in results])
    messagebox.showinfo("Search Results", results_str)


def update_contact():
    name = simpledialog.askstring(
        "Update", "Enter the name of the contact to update:")
    phone = simpledialog.askstring("Phone", "Enter new phone number:")
    email = simpledialog.askstring("Email", "Enter new email:")
    address = simpledialog.askstring("Address", "Enter new address:")
    if contact_book.update_contact(name, phone, email, address):
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")


def delete_contact():
    name = simpledialog.askstring(
        "Delete", "Enter the name of the contact to delete:")
    if contact_book.delete_contact(name):
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")


root = tk.Tk()
root.title("Contact Book")

contact_book = ContactBook()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(fill=tk.X, padx=10, pady=5)

view_button = tk.Button(root, text="View Contacts", command=view_contacts)
view_button.pack(fill=tk.X, padx=10, pady=5)

search_button = tk.Button(
    root, text="Search Contacts", command=search_contacts)
search_button.pack(fill=tk.X, padx=10, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack(fill=tk.X, padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(fill=tk.X, padx=10, pady=5)

root.mainloop()
