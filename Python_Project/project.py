class Block: 
    def __init__(self, start, size, free=True): 
        self.start = start 
        self.size = size 
        self.free = free 
        self.next = None 
class MemoryAllocator: 
    def __init__(self, total_size): 
        self.head = Block(0, total_size, True) 
    # Display memory blocks 
    def display(self): 
        temp = self.head 
        print("\nMemory Status:") 
        print("Start\tSize\tStatus") 
        while temp: 
            status = "Free" if temp.free else "Allocated" 
            print(f"{temp.start}\t{temp.size}\t{status}") 
            temp = temp.next 
    # First Fit Allocation 
    def allocate(self, size): 
        temp = self.head 
        while temp: 
            if temp.free and temp.size >= size: 
 
                if temp.size == size: 
                    temp.free = False 
                else: 
                    new_block = Block(temp.start + size, temp.size - size, True) 
                    new_block.next = temp.next 
                    temp.size = size 
                    temp.free = False 
                    temp.next = new_block 
                print(f"\nAllocated {size} units at address {temp.start}") 
                return 
            temp = temp.next 
        print("\nMemory Allocation Failed!") 
    # Deallocate block 
    def deallocate(self, start_address): 
        temp = self.head 
        while temp: 
            if temp.start == start_address and not temp.free: 
                temp.free = True 
                print(f"\nDeallocated block at address {start_address}") 
                self.merge() 
                return 
            temp = temp.next 
        print("\nInvalid Address or Already Free!") 
    # Merge adjacent free blocks 
 
    def merge(self): 
        temp = self.head 
        while temp and temp.next: 
            if temp.free and temp.next.free: 
                temp.size += temp.next.size 
                temp.next = temp.next.next 
            else: 
                temp = temp.next 
 
# ------------------ Driver Code ------------------ 
def main(): 
    try: 
        total_memory = int(input("Enter total memory size: ")) 
    except ValueError: 
        print("Invalid input! Enter a number.") 
        return 
    allocator = MemoryAllocator(total_memory) 
    while True: 
        print("\n1. Allocate") 
        print("2. Deallocate") 
        print("3. Display Memory") 
        print("4. Exit") 
        try: 
            choice = int(input("Enter choice: ")) 
        except ValueError: 
            print("Enter a valid number!") 
            continue 
        if choice == 1: 
            try: 
                size = int(input("Enter block size: ")) 
                allocator.allocate(size) 
            except ValueError: 
                print("Invalid size!") 
        elif choice == 2: 
            try: 
                addr = int(input("Enter starting address: ")) 
                allocator.deallocate(addr) 
            except ValueError: 
                print("Invalid address!") 
        elif choice == 3: 
            allocator.display() 
        elif choice == 4: 
            print("Exiting program...") 
            break 
        else: 
            print("Invalid choice!") 
if __name__ == "__main__": 
    main()