import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMessageBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btn1_group = []
        self.btn2_group = []
        self.btn3_group = []
        self.btn4_group = []
        self.btn5_group = []
        self.initUI()


    def initUI(self):
        self.btn1 = QPushButton('분석 대상 기기\n기초 정보', self)
        self.btn1.move(20, 13)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton('마지막 위치의\nWIFI 스캔 현황', self)
        self.btn2.move(140, 13)

        self.btn3 = QPushButton('WIFI별\n데이터 사용 현황', self)
        self.btn3.move(260, 13)

        self.btn4 = QPushButton('WIFI별\n접속시도 분석', self)
        self.btn4.move(380, 13)

        self.btn5 = QPushButton('WIFI별\n접속 기록', self)
        self.btn5.move(500, 13)

        self.label1 = QLabel('분석 대상 기기 정보 수집 시간',self)
        self.label1.move(20,60)
        self.label1.setHidden(True)
        self.btn1_group.append(self.label1)
        
        self.label2 = QLabel('2022-11-09 03:09:00',self)
        self.label2.move(200,60)
        self.label2.setHidden(True)
        self.btn1_group.append(self.label2)
        
        self.label3 = QLabel('사용 네트워크',self)
        self.label3.move(20,100)
        self.label3.setHidden(True)
        self.btn1_group.append(self.label3)
        
        self.label4 = QLabel('LG U+',self)
        self.label4.move(200,100)
        self.label4.setHidden(True)
        self.btn1_group.append(self.label4)
        
        self.label5 = QLabel('핸드폰 사용 시간',self)
        self.label5.move(20,140)
        self.label5.setHidden(True)
        self.btn1_group.append(self.label5)
        
        self.label6 = QLabel('0 week(s), 1 day(s), 12 hour(s), 38 minute(s)',self)
        self.label6.move(200,140)
        self.label6.setHidden(True)
        self.btn1_group.append(self.label6)
        

        self.setWindowTitle('갤럭시 WIFI 포렌식')
        self.setGeometry(300, 300, 600, 500)
        self.show()
    
    def btn1_clicked(self):
        for p in self.btn1_group:
            p.setHidden(False)
            
        for p in self.btn2_group:
            p.setHidden(True)
            
        for p in self.btn3_group:
            p.setHidden(True)
            
        for p in self.btn4_group:
            p.setHidden(True)
            
        for p in self.btn5_group:
            p.setHidden(True)

    def btn2_clicked(self):
        for p in self.btn1_group:
            p.setHidden(True)
            
        for p in self.btn2_group:
            p.setHidden(False)
            
        for p in self.btn3_group:
            p.setHidden(True)
            
        for p in self.btn4_group:
            p.setHidden(True)
            
        for p in self.btn5_group:
            p.setHidden(True)

    def btn3_clicked(self):
        for p in self.btn1_group:
            p.setHidden(True)
            
        for p in self.btn2_group:
            p.setHidden(True)
            
        for p in self.btn3_group:
            p.setHidden(False)
            
        for p in self.btn4_group:
            p.setHidden(True)
            
        for p in self.btn5_group:
            p.setHidden(True)

    def btn4_clicked(self):
        for p in self.btn1_group:
            p.setHidden(True)
            
        for p in self.btn2_group:
            p.setHidden(True)
            
        for p in self.btn3_group:
            p.setHidden(True)
            
        for p in self.btn4_group:
            p.setHidden(False)
            
        for p in self.btn5_group:
            p.setHidden(True)

    def btn5_clicked(self):
        for p in self.btn1_group:
            p.setHidden(True)
            
        for p in self.btn2_group:
            p.setHidden(True)
            
        for p in self.btn3_group:
            p.setHidden(True)
            
        for p in self.btn4_group:
            p.setHidden(True)
            
        for p in self.btn5_group:
            p.setHidden(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())