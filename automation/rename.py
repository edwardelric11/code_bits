import os

os.chdir('/Users/username/Downloads/planets')

# Verify if I am in the correct directory
print(os.getcwd())
           
# Print all the current file names
for f in os.listdir():
    (file_name, file_ext) = os.path.splitext(f)
    # print(file_name)
    
    # Split filenames by the hyphens present
    (planet, common, number) = (file_name.split('-'))
    
    # Remove whitespace
    planet = planet.strip()
    common = common.strip()[1:]
    # Padding the numbers (1 -> 01, 2-> 02 and so on)
    number = number.strip().zfill(2)
    
    new_name = ('{}_{}{}'.format(number, planet, file_ext))
    
    os.rename(f, new_name)
