import tkinter as tk
from tkinter import messagebox
import json
import os

contacts = {}

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
            display_contacts()

# Save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "":
        messagebox.showerror("Error", "Name is required!")
        return

    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    save_contacts()
    messagebox.showinfo("Success", f"Contact for '{name}' added.")
    clear_fields()
    display_contacts()

# Search contact
def search_contact():
    name = name_entry.get()
    if name in contacts:
        c = contacts[name]
        result = f"Name: {name}\nPhone: {c['Phone']}\nEmail: {c['Email']}\nAddress: {c['Address']}"
        messagebox.showinfo("Contact Found", result)
    else:
        messagebox.showerror("Not Found", f"No contact found for '{name}'")

# Delete contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        save_contacts()
        messagebox.showinfo("Deleted", f"Contact for '{name}' deleted.")
        display_contacts()
    else:
        messagebox.showerror("Error", f"No contact found for '{name}'")

# Display all contacts
def display_contacts():
    contact_listbox.delete(0, tk.END)
    for name, info in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {info['Phone']}")

# Clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

# Input fields
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Address").pack()
address_entry = tk.Entry(root)
address_entry.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search Contact", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)
tk.Button(root, text="Clear Fields", command=clear_fields).pack(pady=5)

# Contact list display
tk.Label(root, text="Contact List:").pack(pady=5)
contact_listbox = tk.Listbox(root, width=40, height=10)
contact_listbox.pack(pady=10)

# Load contacts when app starts
load_contacts()

# Run GUI
root.mainloop()