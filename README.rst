=====================
Django Zakat QR Code 
=====================

Zakat QR Code is used in for Saudi Arabia invoicing system .


Quick Start
=============

1. this is the class ::
    from zakatqr import Zakatqr
    Zakatqr(seller_name, tax_number, timestamp, total_with_vat, total_vat)


2. make an instance of the class ::
    zakat = Zakatqr("seller name", "123456789", "2021-06-25 07:58:56.550604", "115", "15")

3. to make data as base64 ::
        base64 = zakat.tlv_as_base64()

4. to make qr code image ::
        qr_code = zakat.qr_code()
        qr_code.save("qr_code_img.png")

5. to get a qr image as base64 that can be used in templates for examble ::
        url = zakat.qr_image_encoded_uri()
        <img src="{{url}}"></img>

