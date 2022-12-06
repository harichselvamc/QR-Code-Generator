from PIL import Image as Im #pip install qrcode
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr_code.png")
    
url = input("Enter your url: ")
generate_qrcode(url)