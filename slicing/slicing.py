my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list[start:end:step]

print my_list[-1:2:-1]
# [9, 8, 7, 6, 5, 4, 3]


sample_url = 'http://github.com'
print sample_url

# Reverse the url
print sample_url[::-1]

# Get the top level domain (.com)
print sample_url[-4:]

# # Print the url without the http://
# print sample_url[7:]

# # Print the url without the http:// or the top level domain
print sample_url[7:-4]
