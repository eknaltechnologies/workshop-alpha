class ContactManager:
    """Simple contact management system"""
    
    def __init__(self):
        self.contacts = {}
    
    def add_contact(self, name, phone, email):
        """Add a new contact"""
        self.contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"✅ Contact '{name}' added!")
    
    def find_contact(self, name):
        """Find a contact by name"""
        if name in self.contacts:
            contact = self.contacts[name]
            return f"{name}: {contact['phone']}, {contact['email']}"
        return f"❌ Contact '{name}' not found"
    
    def list_all(self):
        """List all contacts"""
        if not self.contacts:
            print("No contacts yet!")
            return
        
        for name, info in self.contacts.items():
            print(f"{name}: {info['phone']}")
    
    def delete_contact(self, name):
        """Delete a contact"""
        if name in self.contacts:
            del self.contacts[name]
            print(f"✅ Contact '{name}' deleted!")
        else:
            print(f"❌ Contact '{name}' not found")

# USAGE:
manager = ContactManager()

manager.add_contact("Alice", "555-1234", "alice@example.com")
manager.add_contact("Bob", "555-5678", "bob@example.com")
manager.add_contact("Charlie", "555-9999", "charlie@example.com")

print("\n--- All Contacts ---")
manager.list_all()

print("\n--- Find Contact ---")
print(manager.find_contact("Alice"))

print("\n--- Delete Contact ---")
manager.delete_contact("Bob")

print("\n--- Updated List ---")
manager.list_all()