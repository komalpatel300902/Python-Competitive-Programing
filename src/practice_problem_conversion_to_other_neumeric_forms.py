'''This program is Solution of practice problem QUESTION 2.'''



def print_formatted(number):
    hex_set = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    num = 0
    decimal_numbers_list = [str(i) for i in range(1,number+1)]
    octal_number_list = []
    hexadecimal_list = []
    binary_list = []
    for x in range(1,number+1):
    
        # Octal value
        octal_number_list += [str(x+num)]
        if (x+num)%10 == 7:
            num += 2

       
        # Hexadecimal value
        hexa_decimal_number = ""
        num_holder2 = x
        while(num_holder2 >= 16):
            hexa_decimal_number = str(hex_set[num_holder2%16]) + hexa_decimal_number
            num_holder2 = num_holder2//16

        hexadecimal_list += [str(hex_set[num_holder2])+hexa_decimal_number]
     

    
        #Binary values
        num_holder = x
        binary_number = ""
        while(num_holder != 1):
            binary_number = str(num_holder%2) + binary_number
            num_holder = num_holder//2

        binary_list += ["1"+binary_number]

    len_decimal = len(decimal_numbers_list[-1])
    len_binary = len(binary_list[-1])
    len_octal = len(octal_number_list[-1])
    len_hexa = len(hexadecimal_list[-1])

    # Printing with good format
    for x in range(number):
        print((len_decimal-len(decimal_numbers_list[x]))*" "+decimal_numbers_list[x],end = "  ")
        print((len_octal-len(octal_number_list[x]))*" "+octal_number_list[x],end = "  ")  
        print((len_hexa-len(hexadecimal_list[x]))*" "+hexadecimal_list[x],end = "  ")
        print((len_binary-len(binary_list[x]))*" "+binary_list[x])  


n = int(input())
print_formatted(n)