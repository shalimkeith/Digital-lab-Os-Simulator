class SecurityManager:
    def __init__(self):
        self.users = {
            "admin":   {"password": "admin123", "role": "Admin"},
            "student": {"password": "stu456",   "role": "Student"},
            "guest":   {"password": "guest789", "role": "Guest"}
        }
        self.permissions = {
            "Admin":   ["read", "write", "delete"],
            "Student": ["read", "write"],
            "Guest":   ["read"]
        }
        self.log = []

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            role = self.users[username]["role"]
            self.log.append(f"LOGIN SUCCESS: {username} as {role}")
            return role
        self.log.append(f"LOGIN FAILED: {username}")
        return None

    def check_permission(self, role, action):
        if role and action in self.permissions.get(role, []):
            self.log.append(f"ACCESS GRANTED: {role} -> {action}")
            return True
        self.log.append(f"ACCESS DENIED: {role} -> {action}")
        return False

    def print_log(self):
        print("\n--- Security Log ---")
        for entry in self.log:
            print(f"  {entry}")

if __name__ == "__main__":
    sm = SecurityManager()

    role = sm.login("admin", "admin123")
    sm.check_permission(role, "delete")

    role2 = sm.login("guest", "guest789")
    sm.check_permission(role2, "delete")
    sm.check_permission(role2, "read")

    sm.login("hacker", "wrongpass")

    sm.print_log()