class TimeMap:

    def __init__(self):
        # do I need a dictionary where the key is name and value is array
        self.dictionary = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionary:
            self.dictionary[key] = []
        
        self.dictionary[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionary:
            return ""
        
        array = self.dictionary[key]
        l, r = 0, len(array)-1
        result = ""
            
        while l <= r:
            mid = (l+r)//2
            current_time, current_val = array[mid]
            if current_time <= timestamp:
                result = current_val
                l = mid + 1
            else:
                r = mid - 1
        return result

            
