#https://www.interviewcake.com/question/highest-product-of-3
'''Given an array_of_ints, find the highest_product you can get from three of the integers.
The input array_of_ints will always have at least three integers.
'''
#brute force solution
#create a dict {product: (int1,int2,int3)}
#sort dict to find highest
#run O(n^3)

#Input - array= [1, 10, -5, 1, -100]
#Output -> 10 , -5 , -100

def findHighestProduct():
    array= [1, 10, -5, 1, -100]
    products = {}
    length = len(array)
    for x in range(length-2):
        for y in range(x+1, length):
            for z in range(y+1, length):
                temp = array[x] * array[y] * array[z]
                print array[x], array[y], array[z]
                products[temp] = (array[x], array[y], array[z])

    #sort dictionary into list.
    sorted_list= sorted(products.keys())
    #Take highest value by taking last element and find it's keys in the dict
    ans= products[sorted_list[len(sorted_list)-1]]
    print products
    print "the products are " + str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2])

    


###############################

# Final complexity -> O(n logn)
#Effiecent solution
def findHighestProduct2():
    array = [1, 10, -5, 1, -100]
    #sort array  -> [-100, -5, 1, 1, 10]
    sorted_array = sorted(array)

    #ensure list is at least 3 elements 
    length_array= len(sorted_array)

    if length_array > 3:
        #pick fist and last elements 
        num1 = sorted_array[0]  #-100
        num2 = sorted_array[-1] #10

        partial_sum = num1 * num2

        #now pick 2nd to last vs 2nd element 
        # -100 * 10 = -1000

        if partial_sum * sorted_array[1] > partial_sum * sorted_array[-2]:
            num3 = sorted_array[1]
        else:
            num3 = sorted_array[-2]

        print "The products are " + str(num1) + " " + str(num2) + " " + str(num3)

    #error checking 
    elif length_array == 3:
        print sorted_array

    else:
        print "error with number in array"



findHighestProduct2()

def findHighestProduct():
	array= [1, 10, -5, 1, -100]
	products = {}
	length=len(array)
	for x in range(length-2):
		for y in range(x+1,length):
			for z in range(y+1,length):
				temp=array[x] * array[y] * array[z]
				print array[x],array[y],array[z]
				products[temp]= (array[x],array[y],array[z])

	#sort dictionary into list.
	sorted_list= sorted(products.keys())
	#Take highest value by taking last element and find it's keys in the dict
	ans= products[sorted_list[len(sorted_list)-1]]
	print products
	print "the products are " + str(ans[0]) + " " + str(ans[1]) + " " + str(ans[2])

	
findHighestProduct()
