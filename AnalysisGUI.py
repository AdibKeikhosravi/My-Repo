from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class analyzer(QWidget):

    def __init__(self, centralwidget):
        super().__init__(centralwidget)
        
        self.AnalysisLbl = QtWidgets.QLabel(centralwidget)
        self.AnalysisLbl.setGeometry(QtCore.QRect(730, 10, 98, 30))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        font.setKerning(False)
        self.AnalysisLbl.setFont(font)
        self.AnalysisLbl.setObjectName("AnalysisLbl")
        
        ##### APPLY, RESET, CLOSE BUTTONS
        self.progressBar = QtWidgets.QProgressBar(centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(770, 800, 201, 20))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        
        self.ApplyButton = QtWidgets.QPushButton(centralwidget)
        self.ApplyButton.setGeometry(QtCore.QRect(850, 770, 100, 32))
        self.ApplyButton.setObjectName("ApplyButton")
        
        self.ResetButton = QtWidgets.QPushButton(centralwidget)
        self.ResetButton.setGeometry(QtCore.QRect(730, 770, 100, 32))
        self.ResetButton.setObjectName("ResetButton")
        
#         self.CloseButton = QtWidgets.QPushButton(centralwidget)
#         self.CloseButton.setGeometry(QtCore.QRect(610, 770, 100, 32))
#         self.CloseButton.setObjectName("CloseButton")

        
        self.AnalysisMode = QtWidgets.QToolBox(centralwidget)
        self.AnalysisMode.setGeometry(QtCore.QRect(590, 50, 381, 311))
        self.gridLayout_AnalysisMode = QtWidgets.QGridLayout(self.AnalysisMode)
        self.gridLayout_AnalysisMode.setObjectName("gridLayout_AnalysisMode")
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.AnalysisMode.setFont(font)
        self.AnalysisMode.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AnalysisMode.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AnalysisMode.setObjectName("AnalysisMode")
        self.NucleiDetection = QtWidgets.QWidget()
        self.gridLayout_NucleiDetection = QtWidgets.QGridLayout(self.NucleiDetection)
        self.gridLayout_NucleiDetection.setObjectName("gridLayout_NucleiDetection")
#         self.NucleiDetection.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.gridLayout_AnalysisMode.addWidget(self.NucleiDetection, 0, 0, 1, 1)
        
        self.NucleiDetection.setObjectName("NucleiDetection")
        self.NucleiChLbl = QtWidgets.QLabel(self.NucleiDetection)
#         self.NucleiChLbl.setGeometry(QtCore.QRect(10, 0, 61, 31))
        self.gridLayout_NucleiDetection.addWidget(self.NucleiChLbl, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NucleiChLbl.setFont(font)
        self.NucleiChLbl.setObjectName("NucleiChLbl")
        self.CellTypeLabel = QtWidgets.QLabel(self.NucleiDetection)
#         self.CellTypeLabel.setGeometry(QtCore.QRect(10, 30, 71, 31))
        self.gridLayout_NucleiDetection.addWidget(self.CellTypeLabel, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CellTypeLabel.setFont(font)
        self.CellTypeLabel.setObjectName("CellTypeLabel")
        self.NucDetectMethodLbl = QtWidgets.QLabel(self.NucleiDetection)
#         self.NucDetectMethodLbl.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.gridLayout_NucleiDetection.addWidget(self.NucDetectMethodLbl, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NucDetectMethodLbl.setFont(font)
        self.NucDetectMethodLbl.setObjectName("NucDetectMethodLbl")
        self.NucleiChannel = QtWidgets.QComboBox(self.NucleiDetection)
#         self.NucleiChannel.setGeometry(QtCore.QRect(80, 0, 211, 31))
        self.gridLayout_NucleiDetection.addWidget(self.NucleiChannel, 0, 1, 1, 2)
        self.NucleiChannel.setObjectName("NucleiChannel")
        self.NucleiChannel.addItem("Channel 1")
        self.NucleiChannel.addItem("Channel 2")
        self.NucleiChannel.addItem("Channel 3")
        self.NucleiChannel.addItem("Channel 4")
        self.NucCellType = QtWidgets.QComboBox(self.NucleiDetection)
#         self.NucCellType.setGeometry(QtCore.QRect(80, 30, 211, 31))
        self.gridLayout_NucleiDetection.addWidget(self.NucCellType, 1, 1, 1, 2)
        self.NucCellType.setObjectName("NucCellType")
        self.NucCellType.addItem("Fibroblasts")
        self.NucCellType.addItem("MCF10A")
        self.NucCellType.addItem("HCT116")
        self.NucCellType.addItem("U2OS")
        self.NucCellType.addItem("MouseMammarycancer")
        self.NucDetectMethod = QtWidgets.QComboBox(self.NucleiDetection)
#         self.NucDetectMethod.setGeometry(QtCore.QRect(80, 60, 211, 31))
        self.gridLayout_NucleiDetection.addWidget(self.NucDetectMethod, 2, 1, 1, 2)
        self.NucDetectMethod.setObjectName("NucDetectMethod")
        self.NucDetectMethod.addItem("ImageProc")
        self.NucDetectMethod.addItem("CNN")
        self.NucMaxZprojectCheckBox = QtWidgets.QCheckBox(self.NucleiDetection)
#         self.NucMaxZprojectCheckBox.setGeometry(QtCore.QRect(156, 100, 151, 20))
        self.gridLayout_NucleiDetection.addWidget(self.NucMaxZprojectCheckBox, 3, 2, 1, 1)
        self.NucMaxZprojectCheckBox.setObjectName("NucMaxZprojectCheckBox")
        self.ThreeDNucSeg = QtWidgets.QCheckBox(self.NucleiDetection)
#         self.ThreeDNucSeg.setGeometry(QtCore.QRect(10, 100, 131, 20))
        self.gridLayout_NucleiDetection.addWidget(self.ThreeDNucSeg, 3, 0, 1, 2)
        self.ThreeDNucSeg.setObjectName("ThreeDNucSeg")
        self.AnalysisMode.addItem(self.NucleiDetection, "")
        
        #### Cell Boundary GUI
        self.CellBoundary = QtWidgets.QWidget()
#         self.CellBoundary.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.gridLayout_AnalysisMode.addWidget(self.CellBoundary, 1, 0, 1, 1)
        self.gridLayout_CellBoundary = QtWidgets.QGridLayout(self.CellBoundary)
        self.gridLayout_CellBoundary.setObjectName("gridLayout_CellBoundary")
        
        self.CellBoundary.setObjectName("CellBoundary")
        self.CytoChLbl = QtWidgets.QLabel(self.CellBoundary)
#         self.CytoChLbl.setGeometry(QtCore.QRect(20, 0, 61, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoChLbl, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CytoChLbl.setFont(font)
        self.CytoChLbl.setObjectName("CytoChLbl")
        self.CytoCellTypeLbl = QtWidgets.QLabel(self.CellBoundary)
#         self.CytoCellTypeLbl.setGeometry(QtCore.QRect(20, 30, 61, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoCellTypeLbl, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CytoCellTypeLbl.setFont(font)
        self.CytoCellTypeLbl.setObjectName("CytoCellTypeLbl")
        self.CytoDetectMethodLbl = QtWidgets.QLabel(self.CellBoundary)
#         self.CytoDetectMethodLbl.setGeometry(QtCore.QRect(20, 60, 61, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoDetectMethodLbl, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.CytoDetectMethodLbl.setFont(font)
        self.CytoDetectMethodLbl.setObjectName("CytoDetectMethodLbl")
        self.CytoChannel = QtWidgets.QComboBox(self.CellBoundary)
        self.CytoChannel.setGeometry(QtCore.QRect(90, 0, 211, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoChannel, 0, 1, 1, 2)
        
        self.CytoChannel.setObjectName("CytoChannel")
        self.CytoChannel.addItem("")
        self.CytoChannel.addItem("")
        self.CytoChannel.addItem("")
        self.CytoChannel.addItem("")
        self.CytoDetectMethod = QtWidgets.QComboBox(self.CellBoundary)
#         self.CytoDetectMethod.setGeometry(QtCore.QRect(90, 60, 211, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoDetectMethod, 2, 1, 1, 2)
        self.CytoDetectMethod.setObjectName("CytoDetectMethod")
        self.CytoDetectMethod.addItem("")
        self.CytoCellType = QtWidgets.QComboBox(self.CellBoundary)
#         self.CytoCellType.setGeometry(QtCore.QRect(90, 30, 211, 31))
        self.gridLayout_CellBoundary.addWidget(self.CytoCellType, 1, 1, 1, 2)
        self.CytoCellType.setObjectName("CytoCellType")
        self.CytoCellType.addItem("")
        
        
        self.AnalysisMode.addItem(self.CellBoundary, "")
        #############################################################################
        #### Spot Detection 
        self.SpotDetection = QtWidgets.QWidget()
#         self.SpotDetection.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.gridLayout_AnalysisMode.addWidget(self.SpotDetection, 2, 0, 1, 1)
        self.gridLayout_SpotDetection = QtWidgets.QGridLayout(self.SpotDetection)
        self.gridLayout_SpotDetection.setObjectName("gridLayout_SpotDetection")
        self.SpotDetection.setObjectName("SpotDetection")
#         shift = 70

        self.SpotCh1CheckBox = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotCh1CheckBox.setGeometry(QtCore.QRect(10 + shift, 10, 51, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotCh1CheckBox, 0, 1, 1, 1)
        self.SpotCh1CheckBox.setObjectName("Ch1CheckBox")
        self.SpotCh1CheckBox.setStyleSheet("color: gray")
        
        self.SpotPerCh1SpinBox = QtWidgets.QSpinBox(self.SpotDetection)
#         self.SpotPerCh1SpinBox.setGeometry(QtCore.QRect(10 + shift, 35, 51, 24))
        self.gridLayout_SpotDetection.addWidget(self.SpotPerCh1SpinBox, 1, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SpotPerCh1SpinBox.setFont(font)
        self.SpotPerCh1SpinBox.setObjectName("SpotPerCh1SpinBox")
        self.SpotPerCh1SpinBox.setStyleSheet("color: gray")
        
        self.SpotCh2CheckBox = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotCh2CheckBox.setGeometry(QtCore.QRect(70 + shift, 10, 51, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotCh2CheckBox, 0, 2, 1, 1)
        self.SpotCh2CheckBox.setObjectName("Ch2CheckBox")
        self.SpotCh2CheckBox.setStyleSheet("color: red")
        
        self.SpotPerCh2SpinBox = QtWidgets.QSpinBox(self.SpotDetection)
#         self.SpotPerCh2SpinBox.setGeometry(QtCore.QRect(70 + shift, 35, 51, 24))
        self.gridLayout_SpotDetection.addWidget(self.SpotPerCh2SpinBox, 1, 2, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SpotPerCh2SpinBox.setFont(font)
        self.SpotPerCh2SpinBox.setObjectName("SpotPerCh2SpinBox")
        self.SpotPerCh2SpinBox.setStyleSheet("color: red")
        
        self.SpotCh3CheckBox = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotCh3CheckBox.setGeometry(QtCore.QRect(130 + shift, 10, 51, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotCh3CheckBox, 0, 3, 1, 1)
        self.SpotCh3CheckBox.setObjectName("Ch3CheckBox")
        self.SpotCh3CheckBox.setStyleSheet("color: green")
        
        self.SpotPerCh3SpinBox = QtWidgets.QSpinBox(self.SpotDetection)
#         self.SpotPerCh3SpinBox.setGeometry(QtCore.QRect(130 + shift, 35, 51, 24))
        self.gridLayout_SpotDetection.addWidget(self.SpotPerCh3SpinBox, 1, 3, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SpotPerCh3SpinBox.setFont(font)
        self.SpotPerCh3SpinBox.setObjectName("SpotPerCh3SpinBox")
        self.SpotPerCh3SpinBox.setStyleSheet("color: green")
        
        self.SpotCh4CheckBox = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotCh4CheckBox.setGeometry(QtCore.QRect(190 + shift, 10, 51, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotCh4CheckBox, 0, 4, 1, 1)
        self.SpotCh4CheckBox.setObjectName("Ch4CheckBox")
        self.SpotCh4CheckBox.setStyleSheet("color: blue")
        
        self.SpotPerCh4SpinBox = QtWidgets.QSpinBox(self.SpotDetection)
#         self.SpotPerCh4SpinBox.setGeometry(QtCore.QRect(190 + shift, 35, 51, 24))
        self.gridLayout_SpotDetection.addWidget(self.SpotPerCh4SpinBox, 1, 4, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SpotPerCh4SpinBox.setFont(font)
        self.SpotPerCh4SpinBox.setObjectName("SpotPerCh4SpinBox")
        self.SpotPerCh4SpinBox.setStyleSheet("color: blue")
        
        self.SpotCh5CheckBox = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotCh5CheckBox.setGeometry(QtCore.QRect(250 + shift, 10, 51, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotCh5CheckBox, 0, 5, 1, 1)
        self.SpotCh5CheckBox.setObjectName("Ch5CheckBox")
        self.SpotCh5CheckBox.setStyleSheet("color: orange")
        
        self.SpotPerCh5SpinBox = QtWidgets.QSpinBox(self.SpotDetection)
#         self.SpotPerCh5SpinBox.setGeometry(QtCore.QRect(250 + shift, 35, 51, 24))
        self.gridLayout_SpotDetection.addWidget(self.SpotPerCh5SpinBox, 1, 5, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.SpotPerCh5SpinBox.setFont(font)
        self.SpotPerCh5SpinBox.setObjectName("SpotPerCh5SpinBox")
        self.SpotPerCh5SpinBox.setStyleSheet("color: orange")
        
        self.SpotperchannelLbl = QtWidgets.QLabel(self.SpotDetection)
#         self.SpotperchannelLbl.setGeometry(QtCore.QRect(3, 35, 80, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotperchannelLbl, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)
        
        self.SpotLocationLbl = QtWidgets.QLabel(self.SpotDetection)
#         self.SpotLocationLbl.setGeometry(QtCore.QRect(3, 75, 80, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotLocationLbl, 2, 0, 1, 2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.SpotLocationCbox = QtWidgets.QComboBox(self.SpotDetection)
#         self.SpotLocationCbox.setGeometry(QtCore.QRect(90, 70, 211, 31))
        self.gridLayout_SpotDetection.addWidget(self.SpotLocationCbox, 2, 2, 1, 3)
        self.SpotLocationCbox.setObjectName("SpotLocationCbox")
        self.SpotLocationCbox.addItem("Center Of Mass")
        self.SpotLocationCbox.addItem("Max Intensity")
        self.SpotLocationCbox.addItem("Cnetroid")
       
        
        self.SpotMaxZProject = QtWidgets.QCheckBox(self.SpotDetection)
#         self.SpotMaxZProject.setGeometry(QtCore.QRect(160, 110, 131, 20))
        self.gridLayout_SpotDetection.addWidget(self.SpotMaxZProject, 3, 0, 1, 3)
        self.SpotMaxZProject.setObjectName("SpotMaxZProject")
        self.AnalysisMode.addItem(self.SpotDetection, "")
        #######################################################
        #### Spot Analysis
        self.SpotAnalysis = QtWidgets.QWidget()
#         self.SpotAnalysis.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.gridLayout_AnalysisMode.addWidget(self.SpotAnalysis, 3, 0, 1, 1)
        self.gridLayout_SpotAnalysis = QtWidgets.QGridLayout(self.SpotAnalysis)
        self.SpotAnalysis.setObjectName("gridLayout_SpotAnalysis")

        self.SpotAnalysis.setObjectName("SpotAnalysis")
        
        self.spotanalysismethodLbl = QtWidgets.QLabel(self.SpotAnalysis)
#         self.spotanalysismethodLbl.setGeometry(QtCore.QRect(5, 0, 121, 31))
        self.gridLayout_SpotAnalysis.addWidget(self.spotanalysismethodLbl, 0, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.spotanalysismethodLbl.setFont(font)
        self.spotanalysismethodLbl.setObjectName("spotanalysismethodLbl")
        self.thresholdmethodLbl = QtWidgets.QLabel(self.SpotAnalysis)
#         self.thresholdmethodLbl.setGeometry(QtCore.QRect(5, 30, 121, 31))
        self.gridLayout_SpotAnalysis.addWidget(self.thresholdmethodLbl, 1, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thresholdmethodLbl.setFont(font)
        self.thresholdmethodLbl.setObjectName("thresholdmethodLbl")
        self.thresholdvalueLbl = QtWidgets.QLabel(self.SpotAnalysis)
#         self.thresholdvalueLbl.setGeometry(QtCore.QRect(5, 60, 121, 31))
        self.gridLayout_SpotAnalysis.addWidget(self.thresholdvalueLbl, 2, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thresholdvalueLbl.setFont(font)
        self.thresholdvalueLbl.setObjectName("thresholdvalueLbl")
        
        self.spotanalysismethod = QtWidgets.QComboBox(self.SpotAnalysis)
#         self.spotanalysismethod.setGeometry(QtCore.QRect(130, 0, 211, 31))
        self.gridLayout_SpotAnalysis.addWidget(self.spotanalysismethod, 0, 1, 1, 1)
        self.spotanalysismethod.setObjectName("NucleiChannel")
        self.spotanalysismethod.addItem("LOG")
        self.spotanalysismethod.addItem("Gaussian")
        
        
        self.thresholdmethod = QtWidgets.QComboBox(self.SpotAnalysis)
#         self.thresholdmethod.setGeometry(QtCore.QRect(130, 30, 211, 31))
        self.gridLayout_SpotAnalysis.addWidget(self.thresholdmethod, 1, 1, 1, 1)
        self.thresholdmethod.setObjectName("thresholdmethod")
        self.thresholdmethod.addItem("Auto")
        self.thresholdmethod.addItem("Manual")
        
        self.ThresholdSlider = QtWidgets.QSlider(self.SpotAnalysis)
#         self.ThresholdSlider.setGeometry(QtCore.QRect(126, 65 , 181, 22))
        self.gridLayout_SpotAnalysis.addWidget(self.ThresholdSlider, 2, 1, 1, 1)
        self.ThresholdSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ThresholdSlider.setObjectName("ThresholdSlider")
        self.ThresholdSpinBox = QtWidgets.QSpinBox(self.SpotAnalysis)
#         self.ThresholdSpinBox.setGeometry(QtCore.QRect(310, 65, 48, 24))
        self.gridLayout_SpotAnalysis.addWidget(self.ThresholdSpinBox, 2, 2, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.ThresholdSpinBox.setFont(font)
        self.ThresholdSpinBox.setObjectName("ThresholdSpinBox")
        
        
        self.ThresholdSlider.setMaximum(255)
        self.ThresholdSlider.setMinimum(0)
        self.ThresholdSlider.setValue(0)

        self.ThresholdSpinBox.setMaximum(255)
        self.ThresholdSpinBox.setMinimum(0)
        self.ThresholdSpinBox.setValue(0)
        
        
        self.AnalysisMode.addItem(self.SpotAnalysis, "")
        
        #### Resutls
        self.Results = QtWidgets.QWidget()
#         self.Results.setGeometry(QtCore.QRect(0, 0, 381, 171))
        self.gridLayout_AnalysisMode.addWidget(self.Results, 4, 0, 1, 1)
        self.Results.setObjectName("Results")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Results)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NucMaskCheckBox = QtWidgets.QCheckBox(self.Results)
        self.NucMaskCheckBox.setObjectName("NucMaskCheckBox")
        self.gridLayout_3.addWidget(self.NucMaskCheckBox, 0, 0, 1, 1)
        self.SpotsDistance = QtWidgets.QCheckBox(self.Results)
        self.SpotsDistance.setObjectName("SpotsDistance")
        self.gridLayout_3.addWidget(self.SpotsDistance, 0, 1, 1, 1)
        self.SpotsCircles = QtWidgets.QCheckBox(self.Results)
        self.SpotsCircles.setObjectName("SpotsCircles")
        self.gridLayout_3.addWidget(self.SpotsCircles, 1, 1, 1, 1)
        self.NucInfoChkBox = QtWidgets.QCheckBox(self.Results)
        self.NucInfoChkBox.setObjectName("NucInfoChkBox")
        self.gridLayout_3.addWidget(self.NucInfoChkBox, 1, 0, 1, 1)
        self.SpotsLocation = QtWidgets.QCheckBox(self.Results)
        self.SpotsLocation.setObjectName("SpotsLocation")
        self.gridLayout_3.addWidget(self.SpotsLocation, 0, 2, 1, 1)
#         self.checkBox_13 = QtWidgets.QCheckBox(self.Results)
#         self.checkBox_13.setObjectName("checkBox_13")
#         self.gridLayout_3.addWidget(self.checkBox_13, 1, 2, 1, 1)
        self.AnalysisMode.addItem(self.Results, "")
        
        _translate = QtCore.QCoreApplication.translate
        self.AnalysisLbl.setText(_translate("MainWindow", "Analysis"))
        self.ApplyButton.setText(_translate("MainWindow", "Apply"))
        self.ResetButton.setText(_translate("MainWindow", "Reset"))
       # self.CloseButton.setText(_translate("MainWindow", "Close"))
        ### nuclei detection
        self.NucleiChLbl.setText(_translate("MainWindow", "Channel"))
        self.CellTypeLabel.setText(_translate("MainWindow", "Cell Type"))
        self.NucDetectMethodLbl.setText(_translate("MainWindow", "Method"))
        self.NucleiChannel.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.NucleiChannel.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.NucleiChannel.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.NucleiChannel.setItemText(3, _translate("MainWindow", "Channel 4"))
        self.NucCellType.setItemText(0, _translate("MainWindow", "Fibroblasts"))
        self.NucCellType.setItemText(1, _translate("MainWindow", "MCF10A"))
        self.NucCellType.setItemText(2, _translate("MainWindow", "HCT116"))
        self.NucCellType.setItemText(3, _translate("MainWindow", "U2OS"))
        self.NucCellType.setItemText(4, _translate("MainWindow", "Mouse Mammary Tumor"))
        self.NucDetectMethod.setItemText(0, _translate("MainWindow", "Image Processing"))
        self.NucDetectMethod.setItemText(1, _translate("MainWindow", "DL-MRCNN"))
        self.NucMaxZprojectCheckBox.setText(_translate("MainWindow", "Max Z-projection"))
        self.ThreeDNucSeg.setText(_translate("MainWindow", "3D Segmentation"))
        self.AnalysisMode.setItemText(self.AnalysisMode.indexOf(self.NucleiDetection), _translate("MainWindow", 
                                                                                                  "Nuclei Detection"))
        
        #### spot detection
        self.SpotCh1CheckBox.setText(_translate("MainWindow", "Ch1"))
        self.SpotCh2CheckBox.setText(_translate("MainWindow", "Ch2"))
        self.SpotCh3CheckBox.setText(_translate("MainWindow", "Ch3"))
        self.SpotCh4CheckBox.setText(_translate("MainWindow", "Ch4"))
        self.SpotCh5CheckBox.setText(_translate("MainWindow", "Ch5"))
#         self.Coor_CenterOfMass.setText(_translate("MainWindow", "Center of Mass"))
#         self.Coor_MaxIntensity.setText(_translate("MainWindow", "Maximum Intensity"))
#         self.Coor_SpotCentroid.setText(_translate("MainWindow", "Spot Centroid"))
        self.SpotperchannelLbl.setText(_translate("MainWindow", "Spots/CH:"))
        self.SpotMaxZProject.setText(_translate("MainWindow", "Max Z-projection"))
        self.SpotLocationLbl.setText(_translate("MainWindow", "Coordinates:"))
        
        self.SpotLocationCbox.setItemText(0, _translate("MainWindow", "CenterOfMass"))
        self.SpotLocationCbox.setItemText(1, _translate("MainWindow", "MaxIntensity"))
        self.SpotLocationCbox.setItemText(2, _translate("MainWindow", "Cnetroid"))
        
        ### spot analysis
        self.spotanalysismethodLbl.setText(_translate("MainWindow", "Detection Method"))
        self.thresholdmethodLbl.setText(_translate("MainWindow", "Threshold Method"))
        self.thresholdvalueLbl.setText(_translate("MainWindow", "Threshold Value"))
        
        self.spotanalysismethod.setItemText(0, _translate("MainWindow", "Laplacian of Gaussian"))
        self.spotanalysismethod.setItemText(1, _translate("MainWindow", "Gaussian"))
        self.thresholdmethod.setItemText(0, _translate("MainWindow", "Auto"))
        self.thresholdmethod.setItemText(1, _translate("MainWindow", "Manual"))
        
        #### cytoplasm analysis
        self.CytoChLbl.setText(_translate("MainWindow", "Channel"))
        self.CytoCellTypeLbl.setText(_translate("MainWindow", "Cell Type"))
        
        self.CytoDetectMethodLbl.setText(_translate("MainWindow", "Method"))
        self.CytoChannel.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.CytoChannel.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.CytoChannel.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.CytoChannel.setItemText(3, _translate("MainWindow", "Channel 4"))
        self.CytoDetectMethod.setItemText(0, _translate("MainWindow", "Cell Specific"))
        self.CytoCellType.setItemText(0, _translate("MainWindow", "Human Cell"))
        self.AnalysisMode.setItemText(self.AnalysisMode.indexOf(self.CellBoundary), _translate("MainWindow", "Cell Boundary"))
        
        ### results 
        self.AnalysisMode.setItemText(self.AnalysisMode.indexOf(self.SpotDetection), _translate("MainWindow", "Spot Detection"))
        self.AnalysisMode.setItemText(self.AnalysisMode.indexOf(self.SpotAnalysis), _translate("MainWindow", "Spot Analysis"))
        self.NucMaskCheckBox.setText(_translate("MainWindow", "Nuclei Mask"))
        self.SpotsDistance.setText(_translate("MainWindow", "Spots' Distances"))
        self.SpotsCircles.setText(_translate("MainWindow", "Spots Mask(circles)"))
        self.NucInfoChkBox.setText(_translate("MainWindow", "Nuceli Info"))
        self.SpotsLocation.setText(_translate("MainWindow", "Spots Location"))
#         self.checkBox_13.setText(_translate("MainWindow", "Spots Intensity"))
        self.AnalysisMode.setItemText(self.AnalysisMode.indexOf(self.Results), _translate("MainWindow", "Results"))