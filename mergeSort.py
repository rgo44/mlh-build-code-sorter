# credit to https://www.geeksforgeeks.org/merge-sort/

def mergeSort(arr):
    if len(arr) > 1:
        # finds the middle of the array
        mid = len(arr)//2

        # divides array into different 2 array, for the left half and right half
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            
            if isinstance(left[i], int):
                temp_left = left[i]
            if isinstance(right[j], int):
                temp_right = right[j]
            else:
                temp_left = left[i].replace(" ", "").lower()
                temp_right = right[j].replace(" ", "").lower()

            if temp_left < temp_right:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    
    return arr

'''
mlh = ["CruzHacks", "Elle Hacks", "Hack the Northeast Beyond", 
                    "SB Hacks", "HackDavis", "Rose Hack", "BoilerMake", 
                    "Hack Your Portfolio", "QHacks", "TechTogether Seatle",
                    "CUNY Hackathon", "Hack@Brown", "HEX Cambridge 2021",
                    "QWER Hacks", "cuHacking", "Hoya Hacks", "SwampHacks",
                    "CUhackit", "HackViolet", "Hacklytics", "KU HackFest 2021",
                    "Pearl Hacks", "BrickHack 7", "StormHacks"]

print(mergeSort(mlh))
'''