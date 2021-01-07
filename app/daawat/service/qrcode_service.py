import pyqrcode
import png
import qrcode
from pathlib import Path
import os
from pyqrcode import QRCode
BASE_DIR = Path(__file__).resolve().parent.parent

def GenerateQR(qr_string,image_name):
    path_for_storage = os.path.join(BASE_DIR,'qr_images')
    url = pyqrcode.create(qr_string)
    url.png(path_for_storage+'/'+image_name+'.png',scale=6)
# qr = qrcode.QRCode(version=None,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
# qr.add_data(s)
# qr.make(fit=True)
# img = qr.make_image()
# storage.child("QRImage/qrimage.png").put(img)
