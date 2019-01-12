from PyQt5 import uic, QtWidgets
import sys
from Model import Model
from Member import Member
#import view
from Stock import Stock

class Ui(QtWidgets.QDialog):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('cro.ui', self)

class Login(QtWidgets.QDialog):
    def __init__(self):
        super(Login, self).__init__()
        uic.loadUi('login.ui', self)
        self.pushButton.clicked.connect(self.submitLogin)

    def submitLogin(self):
        init_email = self.email.text()
        init_pwd = self.pwd.text()
        print('login')
        print(init_email)
        print(init_pwd)

class Sign(QtWidgets.QDialog):
    def __init__(self):
        super(Sign, self).__init__()
        uic.loadUi('sign.ui', self)


if __name__ == '__main__':
   
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()

    window2 = Login()
    window2.show()

    window3 = Sign()
    window3.show()
   
       
    '''
    model = Model()
    url = "https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181114"
    model.exec(url)
    '''

    '''
    member = Member()
    member.exec(1,1234)
    '''

    stock = Stock()
    stock.exec()
    stock.read_head()


    sys.exit(app.exec_())
