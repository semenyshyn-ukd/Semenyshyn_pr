from task10.t1 import Files
import datetime

class Files2(Files):
    def __init__(self, name, extension, size, date, attributes, author, security_lvl):
        super().__init__(name, extension, size, date, attributes)
        self.author = author
        self.security_lvl = security_lvl

    def show_info(self):
        return (self.show() +
                f"\nAuthor: {self.author}" +
                f"\nSecurity Level: {self.security_lvl}")

    @classmethod
    def add_details(cls):
        name = input("Enter file name: ")
        extension = input("Enter file extension: ")
        size = input("Enter file size: ")
        date = datetime.datetime.now()

        attributes = []
        attr = input("Enter attribute (STOP to stop): ")
        while attr != "STOP":
            attributes.append(attr)
            attr = input("Enter attribute (STOP to stop): ")

        author = input("Enter author: ")
        security_lvl = input("Enter security level (private/public): ")

        new_details = cls(name, extension, size, date, attributes, author, security_lvl)
        cls.files_list.append(new_details)
        return f"Added details:\n{new_details.show_info()}"

    @classmethod
    def change_lvl(cls):
        for el in cls.files_list:
            if el.security_lvl == 'private':
                el.security_lvl = 'public'
            elif el.security_lvl == 'public':
                el.security_lvl = 'private'
        return "Security level changed successfully!"


if __name__ == "__main__":
    print(Files2.add_details())
    print(Files2.change_lvl())