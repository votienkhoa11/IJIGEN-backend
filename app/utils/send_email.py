from flask_mail import Message
from string import Template
from flask import render_template
from app import mail
from app import app
from app.utils.QR_creator import make_qr_ticket

def send_email(id, name, email):
    #respone template
    html = '''
            <head>
                <style>
                    p {
                        font-size: 15px;
                        color: '#000';
                    }

                    a {
                        font-size: 15px;
                        font-weight: 600;
                        color: '#000';
                    }

                    h3 {
                        font-size: 16px;
                        color: '#000';
                    }

                    h4 {
                        font-size: 15px;
                        color: '#000';
                    }
                </style>
            </head>
            <div>
                <h1>Thông báo tham dự Event IJIGEN OFFLINE</h1>
                <p>Xin chào, $name</p>
                <p>Cảm ơn bạn đã đăng ký tham dự Event Offline Ijigen do bọn mình tổ chức, dưới đây là QR Code để check-in tại quán, vui lòng giữ kỹ Mail và mã này. Mong chúng ta sẽ có quãng thời gian giao lưu thật vui vẻ với nhau.</p>
                <p><a>Thời gian tổ chức:</a> 15:00, Chủ Nhật ngày 10/12/2023</p>
                <p><a>Địa điểm:</a> NOW Coffee & Tea - 190 Trương Công Định, Phường 14, Q.Tân Bình, TP.HCM</p>
                <p><a>Mã vé của bạn là:</a> $id</p>
                <h3>Lưu ý:</h3>
                <p>1. <a>Tuyệt đối không quay video hoặc stream buổi offline dưới mọi hình thức,</a> nếu có phát hiện thì tụi mình sẽ lập tức mời ra ngoài.<br>2. Quán cho phép mang bánh kẹo và trái cây, nhưng <a>không cho phép mang theo các loại nước từ bên ngoài vào.</a></p>
                <h3>Thông tin liên lạc nếu bạn cần hỗ trợ:</h3>
                <h4>Facebook:</h4>
                <p>- <a href='https://www.facebook.com/idolmaster.vietnam'>Fanbase THE iDOLM@STER VN</a></p>
                <p>- <a href='https://www.facebook.com/LLVNFanpage'>Fanbase Love Live! VN</a></p>
                <h4>Discord:</h4>
                <p>- Garuru: minhkhai31</p>
            </div>
    '''

     #make qr ticket
    qr_img = make_qr_ticket(id=id, name=name)

    if qr_img == True:
        try:
            print('Sending email to ' + email)
            body = Template(html).safe_substitute(name=name, id=id)
            msg = Message(
                recipients=[email],
                sender='lovemaki1904@gmail.com',
                html=body,
                subject='Thông báo về vé tham dự và thông tin event.'
            )

            with app.open_resource('tickets/' + id + '_' + name + '.png') as fp:
                msg.attach(id + '.png', 'image/png', fp.read())

            mail.send(msg)
            print('Email sent!\n')
        except:
            print('Error occured when sending email!\n')
    else:
        print('error occured when gerenerating ticket')