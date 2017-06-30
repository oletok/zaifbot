import sys
import subprocess
import os
from zaifbot.common.errors import ZaifBotError


class ZaifBot:
    _process = []

    def add_running_process(self, auto_trade_process):
        self._process.append(auto_trade_process)

    def start(self):
        running_processes = []
        for process in self._process:
            process.start()
            running_processes.append(process)
        [x.join() for x in running_processes]


def install_ta_lib():
    parent_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(parent_path + "/setup")
    if sys.platform.startswith('linux'):
        subprocess.call(["./install_ta_lib.sh"])
    elif sys.platform.startswith('mac'):
        subprocess.call(["brew", "install", "ta-lib"])
    elif sys.platform.startswith('win'):
        bits = '32' if sys.maxsize < 2 ** 31 else '64'
        python_v = str(sys.version_info.major) + str(sys.version_info.minor)
        __install_talib_for_windows(bits, python_v)


def __install_talib_for_windows(bits, python_v):
    if bits == 32:
        file = os.path.join(os.path.dirname(__file__),
                            "setup/TA_Lib-0.4.10-cp{v}-cp{v}m-win32.whl".format(v=python_v))
    else:
        file = os.path.join(os.path.dirname(__file__),
                            "setup/TA_Lib-0.4.10-cp{v}-cp{v}m-win_amd64.whl".format(v=python_v))

    if os.path.isfile(file):
        subprocess.call(["pip", "install", file])
    else:
        raise ZaifBotError('this library does not  support your platform')
