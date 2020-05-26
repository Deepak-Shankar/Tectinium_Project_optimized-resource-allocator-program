'''
Write an optimized resource allocator program that can be used for cost planning. The program takes the below 2 inputs:

Hours: No of hours the machine is required to run

Capacity: No of units are required (Will always be multiple of 10)

Based on these inputs, the program should optimally allocate the resources such that the cost of the capacity required is minimum. 

Calculated this for every region and showed them as the below.
'''
#Code:-

input_st = input('Enter the input: ') # Here getting the input in string format

list_ =[int(i) for i in input_st.split() if i.isdigit()] # Extracting the capacity & hour integers from the input string 

capacity = list_[0] # Assign Capacity 
hour = list_[1] # Assign Hours

country = ['New York','India','China'] # Creating the Country list 

capacity_ny = capacity
capacity_ind = capacity
capacity_chi = capacity

print('"Output : "')
for i in country:
    if i == 'New York':
        capacity_dict_ny = {'10XLarge':320,'8XLarge':160,'4XLarge':80,'2XLarge':40,'XLarge':20,'Large':10} 
        cost_dict_ny = {'10XLarge':2820,'8XLarge':1400,'4XLarge':774,'2XLarge':450,'XLarge':230,'Large':120}
        dict_ny = {}
        for i in capacity_dict_ny:
            capacity_ny = capacity_ny
            if capacity_dict_ny[i] <= capacity_ny:
                mod = capacity_ny// capacity_dict_ny[i]
                div = capacity_ny % capacity_dict_ny[i]
                capacity_ny = div
                key_ny = i
                value_ny = mod
                dict_ny.update({key_ny:value_ny})
        total_ny = 0
        for key in cost_dict_ny:
            if key in dict_ny:
                value_ny = cost_dict_ny[key] * dict_ny[key]
                total_ny = total_ny+value_ny
        print("'Total_cost': $",total_ny*hour)
        print("'Region': 'New York'")
        print('Machines',dict_ny)
        print()
        


    if i == 'India':
        capacity_dict_ind = {'10XLarge':320,'8XLarge':160,'4XLarge':80,'2XLarge':40,'Large':10} 
        cost_dict_ind = {'10XLarge':2970,'8XLarge':1300,'4XLarge':890,'2XLarge':413,'Large':140}
        dict_ind = {}
        for i in capacity_dict_ind:
            capacity_ind = capacity_ind
            if capacity_dict_ind[i] <= capacity_ind:
                mod = capacity_ind// capacity_dict_ind[i]
                div = capacity_ind % capacity_dict_ind[i]
                capacity_ind = div
                key_ind = i
                value_ind = mod
                dict_ind.update({key_ind:value_ind})
        total_ind = 0
        for key in cost_dict_ind:
            if key in dict_ind:
                value_ind = cost_dict_ind[key] * dict_ind[key]
                total_ind = total_ind+value_ind
        print("'Total_cost': $",total_ind*hour)
        print("'Region': 'India'")
        print('Machines',dict_ind)
        print()
        


        
    if i == 'China':
        capacity_dict_chi = {'8XLarge':160,'4XLarge':80,'XLarge':20,'Large':10} 
        cost_dict_chi = {'8XLarge':1180,'4XLarge':670,'XLarge':200,'Large':110}
        dict_chi = {}
        for i in capacity_dict_chi:
            capacity_chi = capacity_chi
            if capacity_dict_chi[i] <= capacity_chi:
                mod = capacity_chi// capacity_dict_chi[i]
                div = capacity_chi % capacity_dict_chi[i]
                capacity_chi = div
                key_chi = i
                value_chi = mod
                dict_chi.update({key_chi:value_chi})
        total_chi = 0
        for key in cost_dict_chi:
            if key in dict_chi:
                value_chi = cost_dict_chi[key] * dict_chi[key]
                total_chi = total_chi+value_chi
        print("'Total_cost': $",total_chi*hour)
        print("'Region': 'China'")
        print('Machines',dict_chi)
        print()

