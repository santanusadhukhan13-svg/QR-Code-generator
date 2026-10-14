# import qrcode


# #taking input
# up_id = input("Enter your UPI ID: ")


# # defing payment url based on the upi id and the payment app
# # you can modify these urls based on the payment apps you want to support

# phonepe_url = f"upi://pay?pa={up_id}&pn=Recipient%20Name"
# paytm_url = f"upi://pay?pa={up_id}&pn=Recipient%20Name"
# google_pay_url = f"upi://pay?pa={up_id}&pn=Recipient%20Name"
# bhim_url = f"upi://pay?pa={up_id}&pn=Recipient%20Name"

# # create qrs
# phonepe_qr = qrcode.make(phonepe_url)
# paytm_qr = qrcode.make(paytm_url)
# google_pay_qr = qrcode.make(google_pay_url)
# bhim_qr = qrcode.make(bhim_url)

# # save the qr code to image file
# phonepe_qr.save('phonepe_qr.png')
# paytm_qr.save('paytm_qr.png')
# google_pay_qr.save('google_pay_qr.png')
# bhim_qr.save('bhim_qr.png')

# # display the qr codes
# phonepe_qr.show()
# paytm_qr.show()
# google_pay_qr.show()
# bhim_qr.show()


import qrcode
from PIL import Image, ImageDraw, ImageFont

# Taking UPI ID as input
upi_id = input("Enter your UPI ID: ")

# Creating UPI payment URL
payment_url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name"

# Generating QR code
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(payment_url)
qr.make(fit=True)

qr_image = qr.make_image(
    fill_color="black",
    back_color="white"
).convert("RGB")

# Image dimensions
width = 400
height = 520

# Creating a white background
final_image = Image.new("RGB", (width, height), "white")

# Drawing tools
draw = ImageDraw.Draw(final_image)

# Loading fonts
try:
    title_font = ImageFont.truetype("arial.ttf", 28)
    text_font = ImageFont.truetype("arial.ttf", 18)
except OSError:
    title_font = ImageFont.load_default()
    text_font = ImageFont.load_default()

# Adding heading
title = "SCAN & PAY"
bbox = draw.textbbox((0, 0), title, font=title_font)
title_width = bbox[2] - bbox[0]

draw.text(
    ((width - title_width) // 2, 20),
    title,
    fill="#183153",
    font=title_font
)

# Resizing QR code
qr_image = qr_image.resize((300, 300))

# Pasting QR code onto background
qr_x = (width - 300) // 2
final_image.paste(qr_image, (qr_x, 75))

# Adding UPI ID label
label = "UPI ID"
bbox = draw.textbbox((0, 0), label, font=text_font)
label_width = bbox[2] - bbox[0]

draw.text(
    ((width - label_width) // 2, 390),
    label,
    fill="gray",
    font=text_font
)

# Adding actual UPI ID
bbox = draw.textbbox((0, 0), upi_id, font=text_font)
upi_width = bbox[2] - bbox[0]

draw.text(
    ((width - upi_width) // 2, 420),
    upi_id,
    fill="black",
    font=text_font
)

# Saving final image
final_image.save("upi_qr.png")

# Displaying image
final_image.show()

print("UPI QR code generated successfully!")
print("Saved as upi_qr.png")

