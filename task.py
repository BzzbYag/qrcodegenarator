import qrcode
import image
print("QR CODE GENERATOR")
a= input("https://github.com/")

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = a

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("QrCodeImage1.png")