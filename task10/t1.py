import datetime


class Files:
    files_list = []

    def __init__(self, name, extension, size, date, attributes):
        self.name = name
        self.extension = extension
        self.size = size
        self.date = date
        self.attributes = attributes

    def show(self):
        return (f"\nName: {self.name}"
        f"\nExtension: {self.extension}"
        f"\nSize: {self.size}"
        f"\nDate: {self.date.strftime('%Y-%m-%d %H:%M:%S')}"
        f"\nAttributes: {' '.join(self.attributes)}")

    @classmethod
    def add_file(cls):
        name = input("Enter file name: ")
        extension = input("Example: (.txt / .pdf / .doc / etc)\nEnter file extension: ")
        size = input("Enter file size: ")

        date = datetime.datetime.now()

        attributes = []
        attr = input("(To stop entering, enter STOP)\nEnter file attributes: ")
        while attr != "STOP":
            attributes.append(attr)
            attr = input("(To stop entering, enter STOP)\nEnter file attributes: ")

        if not name or not extension or not size:
            return "The fields must be filled in"
        else:
            new_file = cls(name, extension, size, date, attributes)
            cls.files_list.append(new_file)
            return f"File Added! {new_file.show()}"

    @classmethod
    def sort_by_extension(cls):
        if not cls.files_list:
            return "No files to sort"

        sorted_files = sorted(cls.files_list, key=lambda x: x.extension)

        result = "Sorted extension List:"
        for file_obj in sorted_files:
            result += file_obj.show() + "\n"

        return result.strip()

    @classmethod
    def search_by_date(cls,):
        search_date = input("Enter date to search (yyyy-mm-dd): ")

        matching_files = []
        for file_obj in cls.files_list:
            if file_obj.date.strftime("%Y-%m-%d") == search_date:
                matching_files.append(file_obj)

        if not matching_files:
            return f"No files found for date: {search_date}"

        result = f"Files found for date {search_date}:"
        for file_obj in matching_files:
            result += file_obj.show() + "\n"

        return result.strip()



if __name__ == "__main__":
    print("Add Files")
    print(Files.add_file())

    print("\nSorted by Extension")
    print(Files.sort_by_extension())

    print("\nSearch by Date")
    print(Files.search_by_date())