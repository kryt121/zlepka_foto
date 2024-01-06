from PIL import Image
from datetime import datetime

pre=Image.open("fotka.jpg")

#3.5x4.5 cm / 10x15 cm
#419x540, całość 1795x1205
temp = pre.resize((419, 540))
#print( temp.format, f"{temp.size}x{temp.mode}")
filename="out_"
out=Image.open(filename+".jpg")

#print( out.format, f"{out.size}x{out.mode}")
#rgb_in = in.convert('RGB')
#rgb_im.save(outfile)
x_coord = [32,462,892,1324]
y_coord =[20, 632]
for x in x_coord:
    for y in y_coord:
        #print(x,y)  
        out.paste(temp, (x,y))

rest=str(datetime.now()).replace("-","").replace(" ","").replace(":","").replace(".","")
out.show()
out.save(filename+rest+".jpg")