class PageTable:
    def __init__(self,num_frames):
        self.num_frames = num_frames
        self.frames = []
        self.page_fault = 0
        self.access_logs = []


    def access_page(self, page_number):
        if page_number in self.frames:
            self.frames.remove(page_number)
            self.frames.append(page_number)
            status = "HIT"

        else:
            self.page_fault += 1
            if len(self.frames) >= self.num_frames:
                self.frames.pop(0)
            self.frames.append(page_number)
            status = "FAULT"
        self.access_logs.append((page_number, status,list(self.frames)))

    def print_stats(self):
        print("\n--- Memory Stats ---")
        print(f"Total Accesses: {len(self.access_logs)}")
        print(f"Page Faults:    {self.page_fault}")
        print(f"Current RAM:    {self.frames}")
        print("\nAccess History:")
        for page, status, state in self.access_logs:
            print(f"  Page {page} -> {status} | RAM: {state}")

if __name__ == "__main__":
    ram = PageTable(num_frames=3)

    pages_requested = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3]

    for page in pages_requested:
        ram.access_page(page)

    ram.print_stats()