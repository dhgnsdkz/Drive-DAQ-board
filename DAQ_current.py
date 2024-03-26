########################################################################################################
# Initiated and completed by YJ
# Code creation year: 2023
#
# DAQ board (PCI-6704) is controlled by PyDAQmx
# Reference link: https://pythonhosted.org/PyDAQmx/
# Board spec: 0 ~ 20 mA current range, 16 analog output channel
#
# @ Copyright is belonged to Photonics Research Lab at Kwangwoon University, South Korea
# 
# Update: 2024-03-26 YJ
########################################################################################################

from PyDAQmx import Task
import PyDAQmx, time
import numpy as np

Current = np.array([0.01, 0.011, 0.012, 0.013, 0.014])
task = Task()
task.CreateAOCurrentChan('/PCI-6704/ao16:20', '', 0.0, 0.02, PyDAQmx.DAQmx_Val_Amps, None)
task.StartTask()

written = PyDAQmx.int32()
task.WriteAnalogF64(1, 1, 0.02, PyDAQmx.DAQmx_Val_GroupByChannel, Current, written, None)

time.sleep(1)

# Terminate DAQ board
Current = np.array([0.0])
task.WriteAnalogF64(1, 1, 0.02, PyDAQmx.DAQmx_Val_GroupByChannel, Current, written, None)
task.StopTask()
task.ClearTask()
