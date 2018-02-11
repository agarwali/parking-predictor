import random

def generate_random_surround_list(surround_list,garage_loc):

    random_preserve_number_start=random.randint(0,len(surround_list)-1)
    random_preserve_number_end=random.randint(random_preserve_number_start,len(surround_list)-1)
    temp=surround_list
    surround_list_1=surround_list[random_preserve_number_start:random_preserve_number_end]

    #count=0

    # if len(temp) < len(surround_list_1):
    #     temp_1=[(0,0)]*(len(surround_list_1)-len(temp))
    #     temp=temp+temp_1
    #     for i in range(len(surround_list_1)):
    #         if temp[i]==surround_list_1[i]:
    #             count=count+1
    #
    # elif len(temp)> len(surround_list_1):
    #     temp_2=[(0,0)]*(len(temp)-len(surround_list_1))
    #     temp=temp+temp_2
    #     for i in range(len(temp)):
    #         if temp[i]==surround_list_1[i]:
    #             count=count+1

    random_length=random.randint(random_preserve_number_end,len(surround_list))

    for i in range(random_preserve_number_end,random_length):
        latDiff = (garage_loc[0]-100, garage_loc[0]+100)
        lngDiff = (garage_loc[1]-100, garage_loc[1]+100)
        tuple_1=(float("{0:.10f}".format(random.uniform(latDiff[0], latDiff[1]))),float("{0:.10f}".format(random.uniform(lngDiff[0], lngDiff[1]))))
        #tuple_2=(float("{0:.10f}".format(random.uniform(garage_loc[0]-100, garage_loc[0]+100))),float("{0:.10f}".format(random.uniform(garage_loc[1]-100, garage_loc[1]+100))))
        surround_list_1.append(tuple_1)

    return surround_list

def compute_occupied_spaces(location, capacity):
    empty_list=[]
    delta = 0.0000100
    surround_list = calc_list_sorround(location, capacity)
    for i in surround_list:
        if (location[0]-delta) < i[0] < (location[0]+delta) and (location[1]-delta) < i[1] < (location[1]+delta) :
            empty_list.append(location)
    count=len(empty_list)  #count=number of cars inside the garage
    return count

def calc_list_sorround(garage_location, capacity):
    list_1=[]
    for i in range(random.randint(1,capacity)):
        delta = 0.0000100
        temp_tuple=(float("{0:.10f}".format(random.uniform(garage_location[0]-delta, garage_location[0]+delta))),float("{0:.10f}".format(random.uniform(garage_location[1]-delta, garage_location[1]+delta))))
        list_1.append(temp_tuple)
    list_sorround=generate_random_surround_list(list_1,garage_location)
    return list_sorround

def probability_empty_spaces(garage_location,capacity):
    lis = calc_list_sorround(garage_location, capacity)
    occupied_spaces=compute_occupied_spaces(garage_location, capacity)
    remaining_spaces=capacity - occupied_spaces
    probability_of_empty_spaces=remaining_spaces*1.0/capacity
    return probability_of_empty_spaces

def main():
    garage_location=(float("{0:.10f}".format(random.uniform(1, 100))),float("{0:.10f}".format(random.uniform(1, 100))))
    print("The probability of empty spaces is", probability_empty_spaces(garage_location,50))
main()