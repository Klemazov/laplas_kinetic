from glob import glob
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QDialog, QFileDialog

import sys
import numpy as np
from scipy.stats import linregress

from handlers import change_to_linear

from matplotlib.backends.backend_qt5agg import (NavigationToolbar2QT as NavigationToolbar)

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        # super(Ui, self).__init__()
        # uic.loadUi('design.py', self)
        QtWidgets.QMainWindow.__init__(self)
        uic.loadUi("design.py",self)

        self.open = self.findChild(QtWidgets.QMenu, 'menuopen')
        self.open.addAction('Open DSC curves',self.browse_file)
        self.addToolBar(NavigationToolbar(self.widgetDSC.canvas, self))
        self.addToolBar(NavigationToolbar(self.MplWidget.canvas, self))

        #activation Energy Button
        self.calculate_button = self.findChild(QtWidgets.QPushButton, 'ActivationEnergyButton')
        self.calculate_button.clicked.connect(self.calculateActivationEnergy)
        
        self.HeatingRate1 = self.findChild(QtWidgets.QLineEdit, 'HeatingRate1')
        self.HeatingRate2 = self.findChild(QtWidgets.QLineEdit, 'HeatingRate2')
        self.HeatingRate3 = self.findChild(QtWidgets.QLineEdit, 'HeatingRate3')

        self.Temperature1 = self.findChild(QtWidgets.QLineEdit, 'Temperature1')
        self.Temperature2 = self.findChild(QtWidgets.QLineEdit, 'Temperature2')
        self.Temperature3 = self.findChild(QtWidgets.QLineEdit, 'Temperature3')
        self.EnergyOutput = self.findChild(QtWidgets.QLCDNumber, 'lcdEnergy')
        self.StdOutput = self.findChild(QtWidgets.QLCDNumber, 'lcdNumberSTD')
        self.R2Output = self.findChild(QtWidgets.QLCDNumber, 'lcdNumberR2')

        # self.menuopen.clicked.connect(self.browse_file)

        #DSC Buttons and utils
        self.combo_box_dsc = self.findChild(QtWidgets.QComboBox, 'comboBoxSelectDsc')
        self.combo_list = [] #glob('*.txt')
        

        
        self.pushDscButton = self.findChild(QtWidgets.QPushButton, 'pushDscButton')
        self.pushDscButton.clicked.connect(self.plot_dsc_graph)

        self.lineTemperatureMin = self.findChild(QtWidgets.QLineEdit, 'lineTemperatureMin')
        self.lineTemperatureMax = self.findChild(QtWidgets.QLineEdit, 'lineTemperatureMax')

        self.pushButtonFindTemperature = self.findChild(QtWidgets.QPushButton, 'pushButtonFindTemperature')
        self.pushButtonFindTemperature.clicked.connect(self.find_extremum)

        self.lcdNumberExtremumTemperature = self.findChild(QtWidgets.QLCDNumber, 'lcdNumberExtremumTemperature')


        self.show()

    def browse_file(self):
        self.filenames = QFileDialog.getOpenFileNames(self, 'Open File', filter='TXT files (*txt)') 
        self.combo_list = self.filenames[0]
        self.combo_box_dsc.addItems(self.combo_list)


    def plot_dsc_graph(self):
        self.extremum_temperature = None
        self.data = np.genfromtxt(self.combo_box_dsc.currentText(), encoding='utf-16', skip_header=48).T
        self.Temperature = self.data[1]
        self.Heat_flow = self.data[2]
        self.plot_dsc()

    def calculateActivationEnergy(self):
        heating_rate_1 = float(self.HeatingRate1.text())
        heating_rate_2 = float(self.HeatingRate2.text())
        heating_rate_3 = float(self.HeatingRate3.text())
        Temperature_1 = float(self.Temperature1.text())
        Temperature_2 = float(self.Temperature2.text())
        Temperature_3 = float(self.Temperature3.text())

        dsc_T = np.array([Temperature_1, Temperature_2, Temperature_3])+273.15
        heating_rate = np.array([heating_rate_1,heating_rate_2,heating_rate_3])
        self.x, self.y = change_to_linear(dsc_T, heating_rate)
        self.result = linregress(self.x, self.y)
        self.Ea_dsc = -self.result.slope*8.31
        self.EnergyOutput.display(self.Ea_dsc)
        self.StdOutput.display(self.result.stderr)
        self.R2Output.display(self.result.rvalue**2)
        self.plot_Ea()
    def plot_Ea(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.scatter(self.x,self.y)
        self.MplWidget.canvas.axes.plot(self.x, self.result.intercept+self.result.slope*self.x, color = 'red')
        self.MplWidget.canvas.axes.legend(('input data', 'linear regression'),loc='upper right')
        self.MplWidget.canvas.axes.set_title('Kissinger')
        self.MplWidget.canvas.axes.set_xlabel(r'$1000/T$', fontsize=10)
        self.MplWidget.canvas.axes.set_ylabel(r'$\ln(\beta)/T^2$', fontsize=10)
        self.MplWidget.canvas.draw()
    def plot_dsc(self):
        if self.extremum_temperature:
            self.widgetDSC.canvas.axes.clear()

            self.widgetDSC.canvas.axes.plot(self.Temperature,self.Heat_flow)
            self.widgetDSC.canvas.axes.plot(self.Temperature[self.mask],self.Heat_flow[self.mask])
            self.widgetDSC.canvas.axes.scatter(self.extremum_temperature, np.max(self.Heat_flow[self.mask]),color = 'r')
            self.widgetDSC.canvas.axes.set_title('DSC data')
            self.widgetDSC.canvas.axes.set_xlabel('Temperature, C')
            self.widgetDSC.canvas.axes.set_ylabel('Heat Flow, W')
            self.widgetDSC.canvas.draw()

        else:
            self.widgetDSC.canvas.axes.clear()
            self.widgetDSC.canvas.axes.plot(self.Temperature,self.Heat_flow)
            self.widgetDSC.canvas.axes.set_title('DSC data')
            self.widgetDSC.canvas.axes.set_xlabel('Temperature, C')
            self.widgetDSC.canvas.axes.set_ylabel('Heat Flow, W')
            self.widgetDSC.canvas.draw()

    def find_extremum(self):
        temperature_min = float(self.lineTemperatureMin.text())
        temperature_max = float(self.lineTemperatureMax.text())
        self.mask = np.where((temperature_min<self.Temperature) & (self.Temperature<temperature_max))
        self.extremum_temperature = self.Temperature[np.where(self.Heat_flow == np.max(self.Heat_flow[self.mask]))]
        self.lcdNumberExtremumTemperature.display(self.extremum_temperature[0])
        self.plot_dsc()
        





app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
