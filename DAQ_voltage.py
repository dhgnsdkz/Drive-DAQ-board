########################################################################################################
# Initiated and completed by YJ
# Code creation year: 2023
#
# DAQ board (PCI-6704) is controlled by PyDAQmx
# Reference link: https://pythonhosted.org/PyDAQmx/
# Board spec: -10 ~ 10 V voltage range, 16 analog output channel
#
# @ Copyright is belonged to Photonics Research Lab at Kwangwoon University, South Korea
# 
# Update: 2024-03-26 YJ
########################################################################################################

from PyDAQmx import Task
import PyDAQmx, time
import numpy as np

voltages = np.zeros(16)
task = Task()
task.CreateAOVoltageChan('/PCI-6704/ao0:15', '', -10, 10, PyDAQmx.DAQmx_Val_Volts, None)
task.StartTask()

written = PyDAQmx.int32()
task.WriteAnalogF64(1, 1, 10.0, PyDAQmx.DAQmx_Val_GroupByChannel, voltages, written, None)

time.sleep(1)

# Terminate DAQ board
voltages = np.zeros(16)
task.WriteAnalogF64(1, 1, 10.0, PyDAQmx.DAQmx_Val_GroupByChannel, voltages, written, None)
task.StopTask()
task.ClearTask()
