class parent:
    def __init__(self):
        print("Parent Class")
    def display(self):
        print("display func in parent child")
    
class child(parent):
    def __init__(self):
        print("child class")

class grandchild(child):
    def show(self):
        parent.__init__(self)
        super.show()
        print('print the grand child')
        

