def binary_search(arr, x):
    left = 0
    right = len(arr)-1
    
    mid = (left + right) // 2
    while left<=right and arr[mid] != x:
        if arr[mid] > x: # x must be located in the first half
            #arr[mid].__gt__(x)
          
            right = mid - 1

        elif arr[mid] < x: # x must be located in second half
            left = mid + 1

        mid = (left + right) // 2

    if left <= right:
        return mid
    else:
        raise ValueError("Not found.")


class Customer:

    def __init__(self, customer_id, name): 
        self.customer_id = customer_id
        self.name = name
        # could add other information about the customer here

    def get_name(self): # "getter" method ensures encapsulation
        return self.name

    def get_id(self): 
        return self.customer_id

    def __gt__(self, other): 
        if not isinstance(other, Customer):
            raise TypeError("cannot compare Customer to", type(other))
        return self.customer_id > other.get_id()
    
    def __lt__(self, other): 
        if not isinstance(other, Customer):
            raise TypeError("cannot compare Customer to", type(other))
        return self.customer_id < other.get_id()

    def __eq__(self, other): 
        if not isinstance(other, Customer):
            raise TypeError("cannot compare Customer to", type(other))
        return self.customer_id == other.get_id()


c1 = Customer(1,"Marge")
c2 = Customer(4,"Homer")
c3 = Customer(8,"Bart")
c4 = Customer(11,"Lisa")
c5 = Customer(32,"Maggie")

arr = [c1, c2, c3, c4, c5]

found_idx = binary_search(arr,c4)
print(found_idx)

print(arr[found_idx].get_name())