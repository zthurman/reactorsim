import random
from subprocess import Popen, PIPE


random.seed()


def get_signal_value(signal_low, signal_high):
    return random.uniform(signal_low, signal_high)


class ProcessValue:
    def __init__(self, name, signal_low, signal_high):
        self.name = name
        self.value = get_signal_value(signal_low=signal_low, signal_high=signal_high)


simulator_spec = {
    "przlvl": ProcessValue(name="pressurizer:level", signal_low=0.0, signal_high=5.0),
    "przprs": ProcessValue(
        name="pressurizer:pressure", signal_low=0.01, signal_high=0.15
    ),
    "rc1flow": ProcessValue(
        name="reactorcoolant:flow1", signal_low=0.01, signal_high=0.15
    ),
    "rc2flow": ProcessValue(
        name="reactorcoolant:flow2", signal_low=0.01, signal_high=0.15
    ),
    "rc3flow": ProcessValue(
        name="reactorcoolant:flow3", signal_low=0.01, signal_high=0.15
    ),
    "rc4flow": ProcessValue(
        name="reactorcoolant:flow4", signal_low=0.01, signal_high=0.15
    ),
    "sg1lvl": ProcessValue(
        name="steamgenerator:level1", signal_low=2.5, signal_high=10.0
    ),
    "sg2lvl": ProcessValue(
        name="steamgenerator:level2", signal_low=2.5, signal_high=10.0
    ),
    "sg3lvl": ProcessValue(
        name="steamgenerator:level3", signal_low=2.5, signal_high=10.0
    ),
    "sg4lvl": ProcessValue(
        name="steamgenerator:level4", signal_low=2.5, signal_high=10.0
    ),
}


caput_path = "/home/epics/epics-base/bin/linux-x86_64/caput"


def simulate():
    for each_device, each_pv in simulator_spec.items():
        with Popen([caput_path, each_pv.name, f"{each_pv.value}"], stdout=PIPE) as proc:
            proc.wait()


simulate()
