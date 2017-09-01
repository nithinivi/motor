import codecs
import serial
import serial.tools.list_ports as serialTool


def serialPorts():
    """Generator for ports
    """
    list = serialTool.comports()
    for ports in list:
        yield ports.device


class SerialBoard:
    """Documentation for SerialBooard

    """

    def __init__(self, port=None, buadrate=None):
        super(SerialBoard, self).__init__()
        self.buadrate = buadrate
        self.port = port

    def open_port(self):
        if self.port is not None:
            self.ser = serial.Serial(self.port, self.buadrate)
            self.ser.close()
            self.ser.open()

    def read_port(self):
        if self.port is not None:
            try:
                return codecs.decode((self.ser.readline()), 'ascii')
            except Exception:
                pass  # TODO: serialexpection

    def str_port(self):
        if self.port is not None:
            return self.ser.readline()

    def __call__(self, *args, **kargs):
        self.open_port(self)

    def __str__(self):
        return '({0.port!s}, {0.buadrate!s})'.format(self)

    def __repr__(self):
        return 'SerialBoard({0.port!s}, {0.buadrate!s})'.format(self)
