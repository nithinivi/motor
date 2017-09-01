import sys
import codecs

from collections import deque
from PyQt5 import QtWidgets, QtCore

from boardSerial import SerialBoard, serialPorts
from ui.model import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Controls the model
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.ser = SerialBoard()
        self.comPort.addItems([str(var) for var in serialPorts()])
        self.comPort.highlighted.connect(self.boardConnect)

        self.plot.showGrid(x=True, y=True, alpha=1)
        self.plot.setWindowTitle("test")
        self.plot.setInteractive(True)
        # self.plot.setConfigOptions(antialias=True)
        self.data = 1
        self.curve = self.plot.plot(pen=(255, 240, 0), name="Serial_curve1 ")
        self.curve1 = self.plot.plot(pen=(255, 40, 30), name="Serial_curve1 ")

        self.d = deque([0] * 100, 100)
        self.d1 = deque([0] * 100, 100)

    def boardConnect(self):
        """Connects to hardware intializes the therad
        """
        port = self.comPort.currentText()
        self.ser = SerialBoard(port, buadrate=9600)
        try:
            self.ser.open_port()
            self.BrowserThread = BrowserThread(self.ser)
            self.BrowserThread.start()
            self.BrowserThread.serialout.connect(self.serialBrowser_update)

            return True
        except Exception:
            return False  # TODO: need to raise expection

    @QtCore.pyqtSlot(bytes)
    def serialBrowser_update(self, serial_data):
        """update SerialBrowser
        """
        if serial_data is not None:
            datastr = self.pretty_update(serial_data)
            self.serialBrowser.append(datastr)
            self.d.popleft
            self.d1.popleft # TODO: make to func
            val = datastr.split(" ")
            val[-1] = val[-1].strip()
            self.d.append(float(val[0]))
            self.d1.append(float(val[1]))
            self.curve.setData(list(self.d))
            self.curve1.setData(list(self.d1))

    def pretty_update(self, bitarray):
        return str(codecs.decode(bitarray, 'ascii'))


class BrowserThread(QtCore.QThread):
    """Thread handles all serial methods
    # TODO:  http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html

    """
    serialout = QtCore.pyqtSignal(bytes)  # sig fpr serialBrowser_update

    def __init__(self, ser, parent=None):
        super(BrowserThread, self).__init__(parent=parent)
        self.ser = ser

    def run(self):
        """emits the sig for connecting to slots
        """
        while True:
            val = self.ser.str_port()
            self.serialout.emit(val)


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
