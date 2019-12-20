from tkinter import *
import webbrowser
import time, datetime
import re
from PIL import Image
import os
import os.path
import base64

img = Image.open("drawLine.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("drawLine.png", 'png')
open_icon = open("drawLine.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data1 = "drawLineicon=%s" % b64str

img = Image.open("drawEllipse.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("drawEllipse.png", 'png')
open_icon = open("drawEllipse.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data2 = "drawEllipseicon=%s" % b64str

img = Image.open("drawPolygon.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("drawPolygon.png", 'png')
open_icon = open("drawPolygon.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data3 = "drawPolygonicon=%s" % b64str

img = Image.open("drawCurve.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("drawCurve.png", 'png')
open_icon = open("drawCurve.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data4 = "drawCurveicon=%s" % b64str

img = Image.open("drawCurve.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("drawCurve.png", 'png')
open_icon = open("drawCurve.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data4 = "drawCurveicon=%s" % b64str

img = Image.open("Translate.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("Translate.png", 'png')
open_icon = open("Translate.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data5 = "Translateicon=%s" % b64str

img = Image.open("Rotate.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("Rotate.png", 'png')
open_icon = open("Rotate.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data6 = "Rotateicon=%s" % b64str

img = Image.open("Scale.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("Scale.png", 'png')
open_icon = open("Scale.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data7 = "Scaleicon=%s" % b64str

img = Image.open("Color.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("Color.png", 'png')
open_icon = open("Color.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data8 = "Coloricon=%s" % b64str

img = Image.open("open.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("open.png", 'png')
open_icon = open("open.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data9 = "openicon=%s" % b64str

img = Image.open("clear.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("clear.png", 'png')
open_icon = open("clear.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data10 = "clearicon=%s" % b64str

img = Image.open("exit.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("exit.png", 'png')
open_icon = open("exit.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data11 = "exiticon=%s" % b64str

img = Image.open("clip.png")
out = img.resize((20, 20), Image.ANTIALIAS) #resize image with high-quality
out.save("clip.png", 'png')
open_icon = open("clip.png", "rb")
b64str = base64.b64encode(open_icon.read())  #以base64的格式读出
open_icon.close()
write_data12 = "clipicon=%s" % b64str

f = open("imgs.py", "w+")
f.write(write_data1)
f.write('\n')
f.write(write_data2)
f.write('\n')
f.write(write_data3)
f.write('\n')
f.write(write_data4)
f.write('\n')
f.write(write_data5)
f.write('\n')
f.write(write_data6)
f.write('\n')
f.write(write_data7)
f.write('\n')
f.write(write_data8)
f.write('\n')
f.write(write_data9)
f.write('\n')
f.write(write_data10)
f.write('\n')
f.write(write_data11)
f.write('\n')
f.write(write_data12)
f.write('\n')
f.close()
