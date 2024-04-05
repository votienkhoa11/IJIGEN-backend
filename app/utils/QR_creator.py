import qrcode
from PIL import Image

def make_qr_ticket(id, name):
    try:
        print('Making QR ticket for', name)
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            border=4,
        )

        qr.add_data(id)
        qr.make(fit=True)
        qrImg = qr.make_image(
            back_color = 'white').convert('RGB')

        qrImg.save('app/tickets/' + id + '_' + name +'.png')
        print('QR generated!')
    
        return True
    except:
        return False
