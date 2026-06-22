class FileSystem:
    def __init__(self):
        self.tree = {"root": {}}
        self.permissions = {}
        self.logs = []

    def create_file(self, path, content="", permission="rw"):
        parts = path.strip("/").split("/")
        folder = self.tree["root"]

        for part in parts[:-1]:
            if part not in folder:
                folder[part] = {}
            folder = folder[part]

        filename = parts[-1]
        folder[filename] = content

        self.permissions[path] = permission
        self.logs.append(f"CREATED: {path} | Permission: {permission}")

    def create_folder(self, path):
        parts = path.strip("/").split("/")
        folder = self.tree["root"]

        for part in parts:
            if part not in folder:
                folder[part] = {}
            folder = folder[part]

        self.logs.append(f"FOLDER CREATED: {path}")

    def read_file(self, path, role):
        if path not in self.permissions:
            self.logs.append(f"READ FAILED: {path} does not exist")
            return "File Not Found"

        folder = self.tree["root"]
        parts = path.strip("/").split("/")

        try:
            for part in parts:
                folder = folder[part]

            self.logs.append(f"READ: {path} by {role}")
            return folder

        except KeyError:
            self.logs.append(f"READ FAILED: {path} missing")
            return "File Not Found"

    def write_file(self, path, content, role):
        if path not in self.permissions:
            self.logs.append(f"WRITE FAILED: {path} does not exist")
            return "File not found"

        if self.permissions[path] == "r":
            self.logs.append(f"WRITE DENIED: {path} is read-only | by {role}")
            return "Permission denied"

        parts = path.strip("/").split("/")
        folder = self.tree["root"]

        for part in parts[:-1]:
            folder = folder[part]

        folder[parts[-1]] = content

        self.logs.append(f"WRITE: {path} by {role}")
        return "Write successful"

    def delete_file(self, path, role):
        if path not in self.permissions:
            self.logs.append(f"DELETE FAILED: {path} does not exist")
            return "File not found"

        parts = path.strip("/").split("/")
        folder = self.tree["root"]

        for part in parts[:-1]:
            folder = folder[part]

        del folder[parts[-1]]
        del self.permissions[path]

        self.logs.append(f"DELETED: {path} by {role}")
        return "File deleted"

    def print_logs(self):
        print("\n--- File System Log ---")

        for entry in self.logs:
            print(entry)


if __name__ == "__main__":
    fs = FileSystem()

    fs.create_folder("students")

    fs.create_file("students/notes.txt", "Hello World", "rw")
    fs.create_file("students/readonly.txt", "Cannot edit", "r")

    print(fs.read_file("students/notes.txt", "Student"))

    print(fs.write_file(
        "students/notes.txt",
        "Updated!",
        "Student"
    ))

    print(fs.write_file(
        "students/readonly.txt",
        "Try edit",
        "Guest"
    ))

    print(fs.delete_file(
        "students/notes.txt",
        "Admin"
    ))

    fs.print_logs()