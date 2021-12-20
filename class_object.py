class student():
    def __init__(self,id,name,address):
        self.id=id
        self.name=name
        self.address=address

    def show(self):
        print(self.id)
        print(self.name)
        print(self.address)
obj=student(104,'saurabh','pune')
obj.show()




