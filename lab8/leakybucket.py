bucket_capacity = input("enter bucket capacity = ")
output_rate = input("enter output rate = ")
bucket_content = 0
while(1):
    packet_size = input("enter packet size = ")
    if(packet_size > bucket_capacity):
        print("packet size exceeded")
        print("current bucket content = ", str(bucket_content))
        continue
    elif(int(packet_size)+bucket_content > int(bucket_capacity)):
        print("bucket is already full")
        bucket_content = bucket_content - int(output_rate)
        print(bucket_content)
        continue
    else:
        bucket_content = bucket_content + int(packet_size)
        bucket_content = bucket_content - int(output_rate)
        print("current bucket content = "+str(bucket_content))
    
