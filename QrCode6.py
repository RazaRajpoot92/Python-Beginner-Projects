"""
        QR CODE GENERATOR
        
        Qrcode generator for given text or link.
        You need qrcode and Image, if you don't have then simply install by
        commond: pip install qrcode Image
"""


import qrcode

def QrCode_generator(text):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size= 10,
        border= 4,
        
    )
    
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color="white")
    
    img.save("qrImage.png")
    
text = "https://www.google.com"
QrCode_generator(text)
    