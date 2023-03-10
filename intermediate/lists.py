"""
Python lists
Lists are used to store multiple items in a single variable.
"""
list_of_names = []
list_of_num = list()

# add to list

list_of_names.append("DevOps")
print(list_of_names)

# remove from list
list_of_names.remove("DevOps")
print(list_of_names)

# insert at index
list_of_names.insert(0, "DevOps")
print(list_of_names)

# pop from index
list_of_names.pop(0)
print(list_of_names)

# iterate List

list_of_cloud = ["AWS", "Azure", "GCP"]

for cloud in list_of_cloud:
    print(cloud)

# output:
# ['DevOps']
# []
# ['DevOps']
# []
# AWS
# Azure
# GCP



