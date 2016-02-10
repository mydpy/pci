# Download PIL 
#
# http://www.pythonware.com/products/pil/
# For Windows: Install the Windows binary
# For non-windows: 
#   Download source (Imaging-1.1.1.tar.gz)
#   Move the file to your project directory 
#   Unpackage the software
#     gunzip Imaging-1.1.7.tar.gz
#     tar -xvf Imaging-1.1.7.tar 
#     cd Imaging-1.1.7
#     sudo python setup.py install

# Test PIL Installation
from PIL import Image,ImageDraw
img=Image.new('RGB',(200,200),(255,255,255))  # 200x200 white background
draw=ImageDraw.Draw(img)
draw.line((20,50,150,80),fill=(255,0,0))
draw.line((150,150,20,200),fill=(0,255,0))
draw.text((40,80),'Hello!',(0,0,0))
img.show()
img.save('test.jpg','JPEG')
