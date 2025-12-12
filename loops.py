list_of_cloud = ["AWS", "Azure", "GCP", "IBM Cloud", "Oracle Cloud"]

print(list_of_cloud)

# add a new cloud digital ocean 

list_of_cloud.append("Digital Ocean")

print(list_of_cloud)

# add a new cloud IBM

list_of_cloud.append("IBM")

print(list_of_cloud)

list_of_cloud.insert(2,"heroku")

print(list_of_cloud)

len(list_of_cloud)

print(len(list_of_cloud))

list_of_cloud.insert(0, "hello cloud")

print(list_of_cloud)

for cloud in list_of_cloud:
    print (" ")
    print(cloud)
    
for i in range(0,10):
    print(i)
    