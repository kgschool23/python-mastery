# Write a function `analyze_list(data)` that accepts a single list argument.
# Use a `for` loop to iterate through the data to find the highest value.
# Use a `for` loop to iterate through the data to find the lowest value.
# Calculate the sum of all elements and divide by the total count to find the average.
# Return the final dictionary.

def analyze_list(data):
    if not isinstance(data, list):
        return "Must pass in a list"
    
    sum = 0
    count = 0
    smallest = data[0]
    biggest = data[0]
    for i in range(len(data)):
        sum += data[i]

        if data[i] > biggest:
            biggest = data[i]
        
        if data[i] < smallest:
            smallest =  data[i]
        
        count += 1
    
    avg = sum / count

    list_dict = {
        "largest": biggest,
        "smallest": smallest,
        "sum": sum,
        "average": avg
    }

    return list_dict

print(analyze_list([1,2,3,4,5]))


