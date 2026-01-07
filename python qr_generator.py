import qrcode

data = input("Enter the text or url: ").strip()
filename = input("Enter the file name: ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)  # ensures QR code fits the data
image = qr.make_image(fill_color="black", back_color="white")
image.save(f"{filename}.png")

print(f"QR code generated successfully as {filename}.png")
