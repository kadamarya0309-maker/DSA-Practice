def main():
    browser = BrowserHistory()  
    while True:
        print("-"*30)
        print("Browser History")
        print("-"*30)
        print("1.Visit a page ")
        print("2.Go Back")
        print("3.Go Forward")
        print("4.Show Current Page")
        print("5.Show Full History ")
        print("6.Exit")
        print("-"*30)

        choice = int(input("Enter your choice:"))

        if choice == 1:
            browser.visit()
        elif choice == 2:
            browser.backpage()
        elif choice == 3:
            browser.forwardpage()
        elif choice == 4:
            browser.show_current()
        elif choice == 5:
            browser.fullhistory()
        elif choice == 6:
            break
        else:
            print("Enter the Valid choice..!!!!")

class BrowserHistory:
    def __init__(self):
        self.back = []
        self.forward = []
        self.currentpage = None
    
    def visit(self):
        url = input("Enter the url (e.g., google.com):")
        if self.currentpage:
            self.back.append(self.currentpage)
        self.currentpage = url  
        self.forward.clear()
        print("-"*30)
        print(f"🌐 Visited: {self.currentpage}")
        print("-"*30)
    
    def backpage(self):
        if not self.back:
            print("There is no Back History/ Page available")
            return
        self.forward.append(self.currentpage)
        self.currentpage = self.back.pop()
        print("-"*30)
        print(f"🌐 Visited: {self.currentpage}")
        print("-"*30)
    
    def forwardpage(self):
        if not self.forward:
            print("There is no Forward History/ Page available")
            return
        self.back.append(self.currentpage)  
        self.currentpage = self.forward.pop()
        print("-"*30)
        print(f"🌐 Visited: {self.currentpage}")
        print("-"*30)
    
    def show_current(self):
        print("-"*30)
        print(f"🌐 Current Page : {self.currentpage}")
        print("-"*30)
    
    def fullhistory(self):
        print("-"*30)
        print("\n📊 HISTORY STATUS:")
        print(f"  Back Stack: {self.back}")  
        print(f"  Forward Stack: {self.forward}")  
        print(f"  Current: {self.currentpage}\n")  
        print("-"*30)

if __name__ == "__main__":
    main()