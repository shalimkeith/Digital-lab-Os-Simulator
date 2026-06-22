from memory import PageTable
from filesystem import FileSystem
from disk import DiskScheduler
from security import SecurityManager
from logger import Logger

logger = Logger()

def run_memory():
    print("\n--- Memory Module ---")
    ram = PageTable(num_frames=3)
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3]
    for page in pages:
        ram.access_page(page)
    ram.print_stats()
    logger.log("MEMORY", f"Page faults: {ram.page_fault}")

def run_filesystem():
    print("\n--- File System Module ---")
    fs = FileSystem()
    fs.create_folder("students")
    fs.create_file("students/notes.txt", "Hello World", "rw")
    fs.create_file("students/readonly.txt", "Cannot edit", "r")
    print(fs.read_file("students/notes.txt", "Student"))
    print(fs.write_file("students/readonly.txt", "Try edit", "Guest"))
    fs.print_logs()
    logger.log("FILESYSTEM", "File system simulation complete")

def run_disk():
    print("\n--- Disk Scheduler Module ---")
    ds = DiskScheduler(initial_head=50)
    order = ds.sstf([95, 180, 34, 119, 11, 123, 62, 64])
    print(f"Service Order: {order}")
    ds.print_log()
    logger.log("DISK", f"Service order: {order}")

def run_security():
    print("\n--- Security Module ---")
    sm = SecurityManager()
    role = sm.login("admin", "admin123")
    sm.check_permission(role, "delete")
    role2 = sm.login("guest", "guest789")
    sm.check_permission(role2, "delete")
    sm.login("hacker", "wrongpass")
    sm.print_log()
    logger.log("SECURITY", "Security simulation complete")

while True:
    print("\n===== OS Simulator =====")
    print("1. Memory Management")
    print("2. File System")
    print("3. Disk Scheduling")
    print("4. Security")
    print("5. Exit")

    choice = input("Select option: ")

    if choice == "1":
        run_memory()
    elif choice == "2":
        run_filesystem()
    elif choice == "3":
        run_disk()
    elif choice == "4":
        run_security()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid option")