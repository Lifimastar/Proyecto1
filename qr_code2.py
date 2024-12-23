import qrcode
from PIL import Image

# Create qr code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to qr code
qr.add_data('https://www.tiktok.com/@polarisdance_?lang=es')
# Generate qr code
qr.make(fit=True)
# Create an image from the qr code instance
img = qr.make_image(fill_color="green", back_color="black")
# Save the image
img.save('polarisdance.png')