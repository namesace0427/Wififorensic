import time
from com.dtmilano.android.viewclient import ViewClient
import os

vc = ViewClient(*ViewClient.connectToDeviceOrExit())
vc.traverse()
vc.findViewById('com.sec.android.app.launcher:id/hotseat_icon').touch()

vc = ViewClient(*ViewClient.connectToDeviceOrExit())
vc.traverse()
vc.findViewById('com.samsung.android.dialer:id/star').touch()
vc.findViewById('com.samsung.android.dialer:id/pound').touch()
vc.findViewById('com.samsung.android.dialer:id/nine').touch()
vc.findViewById('com.samsung.android.dialer:id/nine').touch()
vc.findViewById('com.samsung.android.dialer:id/zero').touch()
vc.findViewById('com.samsung.android.dialer:id/zero').touch()
vc.findViewById('com.samsung.android.dialer:id/pound').touch()

vc = ViewClient(*ViewClient.connectToDeviceOrExit())
vc.traverse()
vc.findViewById('com.sec.android.app.servicemodeapp:id/run_dump').touch()

time.sleep(300)

vc = ViewClient(*ViewClient.connectToDeviceOrExit())
vc.traverse()
vc.findViewById('android:id/button1').touch()

vc = ViewClient(*ViewClient.connectToDeviceOrExit())
vc.traverse()
vc.findViewById('com.sec.android.app.servicemodeapp:id/copy_to_sdcard').touch()

time.sleep(10)

os.system("adb pull /sdcard/log")
