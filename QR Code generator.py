import pyqrcode

url = input("Enter url here: ")

qrcode = pyqrcode.create(url)

qrcode.svg("qrcode.svg", scale = 7)
