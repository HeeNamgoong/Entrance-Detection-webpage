import sys
import playsound
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMessageBox, QLineEdit, QInputDialog, QApplication
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import paho.mqtt.client as mqtt


class Button(QWidget):
    data = "ON"

    def __init__(self):
        super().__init__()
        self.UIinit()
        vbox = QVBoxLayout()
        vbox.addLayout(self.vbox1)
        vbox.addLayout(self.vbox2)
        vbox.addLayout(self.vbox3)

        self.btn1.clicked.connect(self.mqtt_pub)
        self.btn1.clicked.connect(self.disconnect_mqtt)
        self.btn1.clicked.connect(self.Text)

        self.btn2.clicked.connect(self.Player)
        self.btn2.clicked.connect(self.disconnect_mqtt)

        self.btn3.clicked.connect(self.passwordClass)
        self.btn3.clicked.connect(self.disconnect_mqtt)

        self.mqtt_sub()

    def passwordClass(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def mqtt_pub(self):
        mqttc = mqtt.Client("python_pub")
        mqttc.connect("192.168.137.55", 1883)
        mqttc.publish("test", "box")
        print("pub")
        mqttc.disconnect()
        print("disconnect")

    def mqtt_sub(self):
        client = mqtt.Client("python_sub")
        client.connect("192.168.137.55", 1883, 60)  # MQTT server connect
        client.on_connect = self.on_connect
        client.on_message = self.on_message  # on_message callback set
        client.subscribe("security")  # subscribe topic
        print("sub")
        client.loop_start()  # start loop to process received messages

    def disconnect_mqtt(self):
        client = mqtt.Client("python_sub")
        client.disconnect()
        print("disconnect")
        client.loop_stop()
        print("loop_stop")

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result cod", str(rc))
        # self.subscribe("security")

    def on_message(self, client, userdata, msg):
        byteToStr = msg.payload
        result = byteToStr.decode('utf-8')
        if result == "1":
            Button.data = "ON"
            print(Button.data)
            self.label1.setText(Button.data)

        if result == "2":
            Button.data = "OFF"
            print(Button.data)
            self.label1.setText(Button.data)

    def UIinit(self):

        self.label1 = QLabel(Button.data, self)
        self.label1.move(310, 100)
        font1 = self.label1.font()
        font1.setPointSize(30)
        font1.setFamily('Bodoni MT Black')
        font1.setBold(True)
        self.label1.setFont(font1)

        self.label2 = QLabel("택배 아저씨 버튼 눌러 주세요~", self)
        self.label2.move(3, 5)
        font2 = self.label2.font()
        font2.setPointSize(15)
        self.label2.setFont(font2)

        self.label1.adjustSize()
        self.label2.adjustSize()

        self.btn1 = QPushButton('택배/배달', self)
        self.btn2 = QPushButton('도둑', self)
        self.btn3 = QPushButton('풀기', self)

        self.btn1.move(50, 600)
        self.btn2.move(300, 600)
        self.btn3.move(550, 600)
        self.btn1.setFixedSize(210, 100)
        self.btn2.setFixedSize(210, 100)
        self.btn3.setFixedSize(210, 100)

        self.btn1.setFont(QtGui.QFont("휴먼모음T", 30))
        self.btn2.setFont(QtGui.QFont("휴먼모음T", 30))
        self.btn3.setFont(QtGui.QFont("휴먼모음T", 30))

        self.vbox1 = QHBoxLayout()
        self.vbox2 = QHBoxLayout()
        self.vbox3 = QHBoxLayout()

        self.vbox1.addWidget(self.label1)
        self.vbox2.addWidget(self.label2)
        self.vbox3.addWidget(self.btn1)
        self.vbox3.addWidget(self.btn2)
        self.vbox3.addWidget(self.btn3)

        self.setGeometry(500, 300, 800, 700)
        self.setWindowTitle('Main Door')
        self.show()

    def Player(self):
        playsound.playsound('pyqt_ad/curse.mp3', True)

    def Text(self):
        QMessageBox.about(self, "BOX", "택배 왔습니다~~")


class password(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        # self.end_meeting.clicked.connect(self.End_buttonOnActivated)

    def initUI(self):
        self.btn = QPushButton('Password', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.setWindowTitle('Input password')
        self.setGeometry(400, 400, 400, 400)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(
            self, 'Input password', 'Enter password:')

        if ok:
            self.le.setText(str(text))

        if text == "koss":
            QMessageBox.about(self, "OK", "Correct!")
            self.passwordCorrect()

        else:
            QMessageBox.warning(self, "NO", "Incorrect!!!")
            playsound.playsound('pyqt_ad/curse.mp3', True)

    def passwordCorrect(self):
        my_instance = Updater(button.label1)
        run_mqtt = Updater(button)
        my_instance.settext()
        run_mqtt.start()
        widget.setCurrentIndex(widget.currentIndex() - 1)


class Updater:
    def __init__(self, label):
        self.label = label

    def settext(self):
        self.label.setText('off')

    def start(self):
        button.mqtt_sub()


if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # 화면 전환용 Widget 설정
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    button = Button()
    passWord = password()

    # Widget 추가
    widget.addWidget(button)
    widget.addWidget(passWord)

    # 프로그램 화면을 보여주는 코드
    widget.setFixedHeight(1000)
    widget.setFixedWidth(1000)
    widget.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    sys.exit(app.exec_())
