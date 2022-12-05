import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton,QMessageBox,QRadioButton,QComboBox,QTextBrowser
import os

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
        self.latestwificonnectlist=[]
        self.forensic()
        self.initUI()

    def forensic(self):
        dir = './log'

        files = os.listdir(dir)
        log_file = []

        for file in files:
            name, ext = os.path.splitext(file)
            if ext == ".log":
                if "dumpState" in name:
                    log_file.append(file)
        if len(log_file) == 0:
            exit(0)
        log_data=[]
        print(log_file[0])
        f = open(dir + "/" + log_file[0], 'r', encoding="UTF-8")
        while True:
            line = f.readline()
            if not line: break
            log_data.append(line)
        f.close()
        # WifiConfigManagerStartLine = log_data.index("WifiConfigManager - Configured networks Begin ----\n")
        # WifiConfigManagerEndLine = log_data.index("WifiConfigManager - Configured networks End ----\n")
        WifiConnectivityManagerStartLine = log_data.index("WifiConnectivityManager - Log Begin ----\n")
        WifiConnectivityManagerEndLine = log_data.index("WifiConnectivityManager - Log End ----\n")
        LatestScanResultsStart = log_data.index("Latest scan results:\n")
        WifiHealthMonitorStart = log_data.index("WifiHealthMonitor - Log Begin ----\n")
        WifiHealthMonitorEnd = log_data.index("WifiHealthMonitor - Log End ----\n")

        for i in range(LatestScanResultsStart+2,LatestScanResultsStart+24):
            self.latestwificonnectlist.append([log_data[i][2:20],log_data[i][64:90].strip()])
        
        for i in range(WifiConnectivityManagerStartLine+1,WifiConnectivityManagerEndLine):
            if "Networks filtered out due to low signal strength" in log_data[i]:
                index = log_data[i][:19].replace('T',' ')
                self.wificonnect[index]=log_data[i][79:].split('/')

        for i in range(WifiHealthMonitorStart+1,WifiHealthMonitorEnd):
            if "SSID:" in log_data[i]:
                index = log_data[i][7:-2]
                time_st = log_data[i+2].index("ConnectDurSec:")
                time_en = log_data[i+2].index("AssocRej:")
                self.wifiuse[index] = [log_data[i+2][time_st+15:time_en],[log_data[i+10][11:],log_data[i+11][9:],log_data[i+12][11:],log_data[i+13][9:]]]
        
        self.log_collect = log_data[1][14:]
        self.log_Network = log_data[8][9:]
        self.log_upTime = log_data[13][11:]

        self.wificonnectlist=[['11-09 02:08:10','U+zone','Disconnect'],['11-09 02:21:13.401','SoMa Center','Connect']]

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
        
        self.label2 = QLabel(self.log_collect,self)
        self.label2.move(200,60)
        self.label2.setHidden(True)
        self.btn1_group.append(self.label2)
        
        self.label3 = QLabel('사용 네트워크',self)
        self.label3.move(20,100)
        self.label3.setHidden(True)
        self.btn1_group.append(self.label3)
        
        self.label4 = QLabel(self.log_Network,self)
        self.label4.move(200,100)
        self.label4.setHidden(True)
        self.btn1_group.append(self.label4)
        
        self.label5 = QLabel('핸드폰 사용 시간',self)
        self.label5.move(20,140)
        self.label5.setHidden(True)
        self.btn1_group.append(self.label5)
        
        self.label6 = QLabel(self.log_upTime,self)
        self.label6.move(200,140)
        self.label6.setHidden(True)
        self.btn1_group.append(self.label6)
        
        self.label7 = QLabel('해당 WIFI 리스트는 신호가 큰 순서대로 정렬됩니다.',self)
        self.label7.move(20,60)
        self.label7.setHidden(True)
        self.btn2_group.append(self.label7)

        self.tb5 = QTextBrowser(self)
        self.tb5.setHidden(True)
        self.tb5.resize(500,400)
        self.tb5.move(20,100)
        self.tb5.setAcceptRichText(True)
        self.tb5.setOpenExternalLinks(True)
        for p in  self.latestwificonnectlist:
            self.tb5.append(p[1].__str__() + " : " + p[0].__str__())
        self.btn2_group.append(self.tb5)

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
        self.tb2.resize(500,350)
        self.tb2.move(20,150)
        self.tb2.setHidden(True)
        self.btn3_group.append(self.tb2)

        self.cb2 = QComboBox(self)
        for p in self.wificonnect.keys():
            self.cb2.addItem(p)
        self.cb2.setHidden(True)
        self.cb2.move(20,60)
        self.cb2.activated[str].connect(self.onActivated2)
        self.btn4_group.append(self.cb2)
        
        self.tb3 = QTextBrowser(self)
        self.tb3.resize(500,400)
        self.tb3.move(20,100)
        self.tb3.setHidden(True)
        self.tb3.setAcceptRichText(True)
        self.tb3.setOpenExternalLinks(True)
        self.btn4_group.append(self.tb3)

        self.tb4 = QTextBrowser(self)
        self.tb4.resize(500,400)
        self.tb4.move(20,100)
        self.tb4.setHidden(True)
        self.tb4.setAcceptRichText(True)
        self.tb4.setOpenExternalLinks(True)
        
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
            self.tb3.append(p)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())