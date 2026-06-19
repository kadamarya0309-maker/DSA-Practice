contacts = {}
favourites = set()

def main():
    print("🎀🎀🎀 WELCOME TO PHONE BOOK 📞 🎀🎀🎀")
    
    while True:  
        print("1.Add Contact")
        print("2.Delete Contact")
        print("3.View All the Contacts")
        print("4.Mark Favourite Contact")
        print("5.View Favourite Contacts")
        print("6.Search Contact")
        print("7.See Contact Statistics")
        print("8.Update Contact")
        print("9.Exit")

        choice = int(input("Enter your choice(1-9): "))
       
        if choice == 1:
            add_contact()
        elif choice == 2:
            delete_contact()
        elif choice == 3:
            view_contact()
        elif choice == 4:
            mark_favourite()
        elif choice == 5:
            view_favourite()
        elif choice == 6:
            search_contact()
        elif choice == 7:
            statistics_contact()
        elif choice == 8:
            update_contact()
        elif choice == 9:
            break  
        else:
            print("Enter the Valid choice❗")

def add_contact():
    name = input("Enter the name: ")
    if name in contacts:
        print("Already a Contact !!!")
    else:
        number = input("Enter the phone number: ")
        contacts[name] = number
        print("Contact Saved Successfully✅☺️")

def delete_contact():
    name = input("Enter the name u Wanted to delete: ")
    if name not in contacts:
        print("Name is not in phonebook/contact is already deleted")
    else:
        del contacts[name]  
        print(f"{name} contact deleted successfully")

def view_contact():
    print("-"*30)
    print("📃📞Your Contact List📞📃")
    for key, value in contacts.items():
        print(f"{key} {value}")
    print("-"*30)


def mark_favourite():
    name = input("Enter the name to mark as favourite: ")
    if name in favourites:
        print("Name is already marked as the favourite")
    else:
        favourites.add(name)
        print("Name added in the Favourites💛")

def update_contact():
    name = input("Enter name to update: ")
    if name not in contacts:
        print("❌ Contact not found!")
        return
    
    new_phone = input(f"Enter new number for {name}: ")
    contacts[name] = new_phone
    print(f"{name} updated!✅")

def view_favourite():
    if not favourites:
        print("⭐ No favorites!")
        return 
    
    print("\n⭐ FAVORITES ⭐")
    print("-" * 30)
    for name in favourites:
        if name in contacts:
            print(f"{name}: {contacts[name]}")
    print("-" * 30)

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print("-"*30)
        print(f"📞 {name}: {contacts[name]}")
        print("-"*30)
    else:
        print(f"❌ {name} not found in phone book!")

def statistics_contact():
    print("\n📊 STATISTICS 📊")
    print(f"Total contacts: {len(contacts)}")
    print(f"Favorites: {len(favourites)}")

if __name__ == "__main__":
    main()