import qrcode

data = 'https://www.instagram.com/tech_phishers/'
#data can be any data you want on your qrcode

img = qrcode.make(data)

img.save('my_qr_using_py.png')