from uttlv import TLV
import base64
import qrcode
from io import BytesIO

class Zakatqr():

	def __init__(self, seller_name, tax_number, timestamp, total_with_vat, total_vat):
		self.seller_name = seller_name
		self.tax_number = tax_number
		self.timestamp = timestamp
		self.total_with_vat = total_with_vat
		self.total_vat = total_vat

	
	def tlv_to_base64(self):
		tags = TLV()

		tags[0x01] = str( self.seller_name )
		tags[0x02] = str( self.tax_number )
		tags[0x03] = str( self.timestamp )
		tags[0x04] = str( self.total_with_vat )
		tags[0x05] = str( self.total_vat )

		tlv_as_byte_array = tags.to_byte_array()
		tlv_as_base64 = base64.b64encode(tlv_as_byte_array)
		tlv_as_base64 = tlv_as_base64.decode("ascii")
		return tlv_as_base64


	def qr_code(self):
		base64_tlv = self.tlv_to_base64()
		qr_code_img = qrcode.make(base64_tlv)
		return qr_code_img


	def qr_image_encoded_uri(self):
		img = self.qr_code()
		buffered = BytesIO()
		img.save(buffered, format="JPEG")
		img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
		mime = "image/png"
		uri = "data:%s;base64,%s" % (mime, img_str)
		return uri