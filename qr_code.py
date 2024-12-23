import qrcode as qr

img = qr.make('https://www.tiktok.com/@polarisdance_?lang=es')
img.save('polarisdance.png')
