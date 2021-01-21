from PIL import Image
import os

def convert_to_sprite_bitmap(image, islevel):
    bitmap = []
    cur_row = ''
    
    index = 0
    for pixel in image:
        cur_row += ('1' if pixel == (255, 255, 255) else '0')
        index += 1

        if index >= 8:
            index = 0
            if islevel:
                bitmap.append(cur_row)
            else:
                bitmap.append(cur_row[::-1]) # reverse row, bitmaps are drawn in reverse
            cur_row = ''
    
    # convert string with bits to hexadecimal ('10011' -> 0x13)
    bitmap = [hex(int(num, 2)) for num in bitmap] 
    
    # make sure redundant zeros are present (0x7 -> 0x07)
    bitmap = ['0x0' + num[-1] if len(num) == 3 else num for num in bitmap]
    
    # convert list to nicely styled line
    bitmap = str(bitmap)
    bitmap = bitmap.replace("'", "").replace("[", "{").replace("]", "}")
    
    return bitmap

# get all .png files in current directory
files = os.listdir()
files = [(file, 'level' in file) for file in files if '.png' in file]


# convert and print bitmaps of images to bitmaps.txt
with open('bitmaps.txt', 'w') as output_file:
    for file in files:
        image = Image.open(file[0], 'r')
        pixels = list(image.getdata())
        
        bitmap = convert_to_sprite_bitmap(pixels, file[1])
        
        # format bitmap so that it's ready to be copy-pasted directly
        if file[1]:
            output_file.write("static unsigned char level_" + file[0][:-4] + "[]" + bitmap + ";\n")
        else:
            output_file.write("static unsigned char sprite_" + file[0][:-4] + "[]" + bitmap + ";\n")