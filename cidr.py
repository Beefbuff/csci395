# Kyle Kalbach
# csci395 Computer Networks
# 04/01/2024
# helper
def create_subnet_rep(cidr:str):
    mask_array_string = createBinaryOctetArray(cidr)
    mask_array_base_ten = binaryStringArray_To_BaseTenArray(mask_array_string)
    
    return mask_array_base_ten
# helper
def createBinaryOctetArray(cidr:str):
    # calc # zeroes
    zeroes = 32 - int(cidr)
    
    binary_num = ""

    # build string representation of binary
    # 1's
    i=0
    while i < int(cidr):
        if i % 8 == 0 and i != 0:
            binary_num = binary_num + '.'
          
        binary_num = binary_num + '1'
        i += 1
    #  0's
    i=0
    while i < zeroes:
        binary_num = binary_num + '0'    
        i += 1
    
    # Make an array of string representations of binary octets
    mask_array_string = binary_num.split('.')
    return mask_array_string
# helper
def binaryStringArray_To_BaseTenArray(binary_num_array):
    for i in range(0,len(binary_num_array)):
        binary_num_array[i] = int(binary_num_array[i], 2)
    return binary_num_array
# helper
def baseTenStringArray_To_BaseTenArray(array):
    for i in range(0,len(array)):
        array[i] = int(array[i])
    return array
# helper
def baseTenArray_To_BinaryArray(array):
    for i in range(0,len(array)):
        array[i] = format(array[i],'b')
    return array
# calculate subnet mask
def subnet_Mask(cidr: str) :

    mask_array = create_subnet_rep(cidr)

    # build output string
    output = ""

    for i in range(0,len(mask_array)):
        mask_array[i] = str(mask_array[i])
    
    for i in range(0,len(mask_array)):
        if i < len(mask_array) - 1:
            output = output + mask_array[i] + '.'
        else:
            output = output + mask_array[i]

    return output  
# helper
def baseTenArrayToString(array):
    outputString = ''
    for i in range(0,len(array)):
        if i < len(array) - 1:
            outputString = outputString + str(array[i]) + '.'
        else:
            outputString = outputString + str(array[i])

    return outputString
# helper for broadcast addr
def singleOctetMask(cidr:str):
    ones = 32 - int(cidr)
    zeroes = 8 - ones

    outputString =""

    i=0
    while i < 8 :
        if i < zeroes:
            outputString = outputString + '0'
        else:
            outputString = outputString + '1' 
        i+=1
    return outputString
# calculate network Id
def network_Id(ip,cidr:str) :
    ip = ip.split('.')

    ip = baseTenStringArray_To_BaseTenArray(ip)
    ip = baseTenArray_To_BinaryArray(ip)
    
    mask_array = createBinaryOctetArray(cidr)

    networkId = []
    for i in range(0,len(ip)):
        networkId.append(int(ip[i],2) & int(mask_array[i],2)) 
    
    return baseTenArrayToString(networkId)
# calculate broadcast addr
def broadcastaddr(ip,cidr:str):
    ip = ip.split('.')

    ip = baseTenStringArray_To_BaseTenArray(ip)
    ip = baseTenArray_To_BinaryArray(ip)

    broadcast_Addr = []
    broadcast_Addr_Mask = ['00000000','00000000','00000000', singleOctetMask(cidr)]
    for i in range(0,len(ip)):
        broadcast_Addr.append(int(ip[i],2) | int(broadcast_Addr_Mask[i],2))
    return baseTenArrayToString(broadcast_Addr)
# calculate total hosts
def total_Hosts(cidr:str):
    host_Bits = 32 - int(cidr)
    total_Hosts = pow(2,host_Bits) 
    return total_Hosts
# calculate host range 
def host_Range(networkId,broadcastaddr):
    networkId = networkId.split('.')
    networkId = baseTenStringArray_To_BaseTenArray(networkId)
    broadcastaddr = broadcastaddr.split('.')
    broadcastaddr = baseTenStringArray_To_BaseTenArray(broadcastaddr)

    networkId[3] = networkId[3] + 1
    broadcastaddr[3] = broadcastaddr[3] - 1
    
    outputString = ""
    outputString = outputString + baseTenArrayToString(networkId) + '-' + baseTenArrayToString(broadcastaddr)
    return outputString
# validate Ip input
def validIp(ip):
    if len(ip) > 4:
        print('Invalid ip use form x.x.x.x')
        return False
    for i in range(0,len(ip)):
        if int(ip[i]) > 255 or int(ip[i]) < 0 :
            print('Invalid Octet, Octet range is 0 to 255')
            return False
    return True
# validate cidr input
def validCidr(cidrValue):
    if int(cidrValue) < 1 or int(cidrValue) > 32:
            print('Input a valid CIDR number 1 to 32')
            return False
    else:
        return True
# user input loop
while True:
        cidr = input('Enter an IP address in CIDR notation (x.x.x.x/y):');
        userInput = cidr.split('/')
        ip = userInput[0]
        ip = ip.split('.')
        if(validIp(ip) and validCidr(userInput[1])):
            break

# User Input good Calculate and print
print("Network ID: " + network_Id(userInput[0],userInput[1]))
print("Subnet mask: " + subnet_Mask(userInput[1]))
print("Broadcast address: " + broadcastaddr(userInput[0],userInput[1]))
print("Total hosts: " + str(total_Hosts(userInput[1])))
print("Usable hosts: " + str(total_Hosts(userInput[1]) - 2))
print("Host range: " + host_Range( network_Id(userInput[0],userInput[1]) , broadcastaddr(userInput[0],userInput[1])))

