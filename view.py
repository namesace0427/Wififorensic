import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMessageBox,QRadioButton,QComboBox,QTextBrowser


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.btn1_group = []
        self.btn2_group = []
        self.btn3_group = []
        self.btn4_group = []
        self.btn5_group = []
        self.wifiuse={}
        self.wificonnect={}
        self.wificonnectlist=[]
        self.forensic()
        self.initUI()

    def forensic(self):
        self.wifiuse['SoMa Center']=[119745,[[0,0,0,31122,72434],[0,0,0,3,8],[0,229536,0,67747,86841],[0,1,0,7,38]]]
        self.wifiuse['olleh_GiGA_WiFi_0CB6']=[233544,[[0,0,0,18848,27064],[0,0,0,2,1],[0,0,28564,75520,154647],[0,0,9,15,10]]]
        self.wifiuse['조영호의 iPhone']=[25996,[[0,0,0,0,0],[0,0,0,0,0],[0,2276,0,11913,82851],[0,2,0,8,10]]]
        self.wifiuse['U+zone']=[5521,[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,21656],[0,0,0,0,3]]]
        self.wifiuse['KHU Wi-Fi']=[9733,[[0,0,0,0,0],[0,0,0,0,0],[0,0,5992,19260,32971],[0,0,1,5,5]]]

        self.wificonnect['2022-11-09 02:11:42']=[['KT_WiFi_5G_417E','88:3c:1c:7c:41:81'],['[air purifier]_E30AJT1013042H','40:ca:63:68:ba:4c'],['SK_WiFiGIGA93EE','b4:a9:4f:c4:93:f1'],
        ['SK_WiFiGIGA93EE_2.4G','c6:a9:4f:c4:93:f1'],['KT_GiGA_2G_Wave2_152A','00:07:89:d3:15:2d'],['U+NetEDE8','80:ca:4b:2b:ed:ea'],['KT_GiGA_5G_02','60:29:d5:3e:02:98'],['ww2_5G','70:5d:cc:e9:ff:b4'],
        ['iptime5G','88:36:6c:6e:ae:5a']]

        self.wificonnectlist=[['11-09 02:08:10','U+zone','Disconnect'],['11-09 02:21:13.401','SoMa Center','Connect']]

# '2022-11-09 02:17:44'
# '2022-11-09 02:21:13'
# '2022-11-09 02:31:17'

    def initUI(self):
        self.btn1 = QPushButton('분석 대상 기기\n기초 정보', self)
        self.btn1.move(20, 13)
        self.btn1.clicked.connect(self.btn1_clicked)

        self.btn2 = QPushButton('마지막 위치의\nWIFI 스캔 현황', self)
        self.btn2.move(140, 13)
        self.btn2.clicked.connect(self.btn2_clicked)

        self.btn3 = QPushButton('WIFI별\n데이터 사용 현황', self)
        self.btn3.move(260, 13)
        self.btn3.clicked.connect(self.btn3_clicked)

        self.btn4 = QPushButton('WIFI별\n접속시도 분석', self)
        self.btn4.move(380, 13)
        self.btn4.clicked.connect(self.btn4_clicked)

        self.btn5 = QPushButton('WIFI별\n접속 기록', self)
        self.btn5.move(500, 13)
        self.btn5.clicked.connect(self.btn5_clicked)

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
        
        self.label7 = QLabel('해당 WIFI 리스트는 신호가 큰 순서대로 정렬됩니다.',self)
        self.label7.move(20,60)
        self.label7.setHidden(True)
        self.btn2_group.append(self.label7)

        self.label8 = QLabel('SoMa Center\nskiptime\nDTD 5G\nhanseo\nKT_GiGA_46FC\n \
iptmie\nRM418\nSoma_iot\nhanseo5G\niptime\nsl\nU+NetCFC0_5G\nDS\nSoMa Center\n \
KT_GiGA_E955\nKT_GiGA_FDE9\nFREE_U+zone\nKT_GiGA_5G_Wave2_7328\nKT_GiGA_5G_Wave2_2B85\n',self)
        self.label8.move(20,100)
        self.label8.setHidden(True)
        self.btn2_group.append(self.label8)

        self.cb = QComboBox(self)
        self.cb.addItem("SoMa Center")
        self.cb.addItem("olleh_GiGA_WiFi_0CB6")
        self.cb.addItem("조영호의 iPhone")
        self.cb.addItem("U+zone")
        self.cb.addItem("KHU Wi-Fi")
        self.cb.move(20,60)
        self.cb.setHidden(True)
        self.cb.activated[str].connect(self.onActivated)
        self.btn3_group.append(self.cb)

        self.label9 = QLabel('총 접속 시간',self)
        self.label9.move(20,100)
        self.label9.setHidden(True)
        self.btn3_group.append(self.label9)

        self.tb = QLabel('                            ',self)
        self.tb.setHidden(True)
        self.tb.move(100,100)
        self.btn3_group.append(self.tb)

        self.tb2 = QTextBrowser(self)
        self.tb2.setHidden(True)
        self.tb2.move(20,150)
        self.btn3_group.append(self.tb2)

        self.cb2 = QComboBox(self)
        self.cb2.addItem('2022-11-09 02:11:42')
        self.cb2.addItem('2022-11-09 02:17:44')
        self.cb2.addItem('2022-11-09 02:21:13')
        self.cb2.addItem('2022-11-09 02:31:17')
        self.cb2.setHidden(True)
        self.cb2.move(20,60)
        self.cb2.activated[str].connect(self.onActivated2)
        self.btn4_group.append(self.cb2)
        
        self.tb3 = QTextBrowser(self)
        self.tb3.setHidden(True)
        self.tb3.setAcceptRichText(True)
        self.tb3.setOpenExternalLinks(True)
        self.tb3.move(20,150)
        self.btn4_group.append(self.tb3)

        self.tb4 = QTextBrowser(self)
        self.tb4.setHidden(True)
        self.tb4.setAcceptRichText(True)
        self.tb4.setOpenExternalLinks(True)
        self.tb4.move(20,150)
        for p in  self.wificonnectlist:
            self.tb4.append(p[0].__str__() + " : " + p[1].__str__() + " : " + p[2].__str__())
        self.btn5_group.append(self.tb4)

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

    def onActivated(self, text):
        self.tb.setText(self.wifiuse[text][0].__str__() + "초")
        self.tb2.clear()
        for p in self.wifiuse[text][1]:
            self.tb2.append(p.__str__())

    def onActivated2(self,text):
        self.tb3.clear()
        for p in self.wificonnect[text]:
            self.tb3.append(p[0].__str__() + ":" + p[1].__str__())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())