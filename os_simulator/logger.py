import datetime

class Logger:
    def __init__(self):
        self.entries = []

    def log(self, module, event):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] [{module}] {event}"
        self.entries.append(entry)
        print(entry)

    def print_all(self):
        print("\n--- Full System Log ---")
        for entry in self.entries:
            print(f"  {entry}")

if __name__ == "__main__":
    logger = Logger()
    logger.log("MEMORY", "Page fault on page 3")
    logger.log("FILESYSTEM", "File created: students/notes.txt")
    logger.log("DISK", "Head moved to 62")
    logger.log("SECURITY", "Login failed: hacker")
    logger.print_all()