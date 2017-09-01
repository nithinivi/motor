import sys

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
        # self.serialBrowser_update()

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

    @QtCore.pyqtSlot(str)
    def serialBrowser_update(self, serial_data):
        if serial_data is not None:
            self.serialBrowser.append(serial_data)


class BrowserThread(QtCore.QThread):
    """Thread handles all serial methods
    # TODO:  http://pyqt.sourceforge.net/Docs/PyQt5/signals_slots.html

    """
    serialout = QtCore.pyqtSignal(str)  # sig fpr serialBrowser_update

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
