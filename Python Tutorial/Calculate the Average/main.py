def main():

    def calculate_avg(my_list):
        
        sum = 0
        for item in my_list:
            sum += item
        avg = sum / len(my_list)
        return avg
    
    my_list = [1,2,3,4,5]
    result  = calculate_avg(my_list)
    return result


res = main()
print(f'avg={res}')