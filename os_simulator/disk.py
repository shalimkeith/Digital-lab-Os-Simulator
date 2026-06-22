class DiskScheduler:
    def __init__(self, initial_head=50):
        self.head = initial_head
        self.log = []

    def sstf(self, requests):
        remaining = requests.copy()
        order = []
        current = self.head
        while remaining:
            closest = min(remaining, key=lambda x: abs(x - current))
            order.append(closest)
            self.log.append(f"Head moved to {closest} | Distance: {abs(closest - current)}")
            current = closest
            remaining.remove(closest)
        self.log.append(f"Final head position: {current}")
        return order

    def print_log(self):
        print("\n--- Disk Scheduler Log ---")
        for entry in self.log:
            print(f"  {entry}")

if __name__ == "__main__":
    ds = DiskScheduler(initial_head=50)
    requests = [95, 180, 34, 119, 11, 123, 62, 64]
    order = ds.sstf(requests)
    print(f"Service Order: {order}")
    ds.print_log()