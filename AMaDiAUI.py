# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AMaDiAUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AMaDiA_Main_Window(object):
    def setupUi(self, AMaDiA_Main_Window):
        AMaDiA_Main_Window.setObjectName("AMaDiA_Main_Window")
        AMaDiA_Main_Window.resize(906, 634)
        AMaDiA_Main_Window.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(AMaDiA_Main_Window)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.Tab_1 = QtWidgets.QWidget()
        self.Tab_1.setAutoFillBackground(True)
        self.Tab_1.setObjectName("Tab_1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Tab_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Tab_1_History = QtWidgets.QListWidget(self.Tab_1)
        self.Tab_1_History.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Tab_1_History.setObjectName("Tab_1_History")
        self.gridLayout_2.addWidget(self.Tab_1_History, 0, 0, 1, 1)
        self.Tab_1_InputField = QtWidgets.QLineEdit(self.Tab_1)
        self.Tab_1_InputField.setObjectName("Tab_1_InputField")
        self.gridLayout_2.addWidget(self.Tab_1_InputField, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Tab_1, "")
        self.Tab_2 = QtWidgets.QWidget()
        self.Tab_2.setAutoFillBackground(True)
        self.Tab_2.setObjectName("Tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Tab_2_LowerSplitter = QtWidgets.QSplitter(self.Tab_2)
        self.Tab_2_LowerSplitter.setOrientation(QtCore.Qt.Vertical)
        self.Tab_2_LowerSplitter.setObjectName("Tab_2_LowerSplitter")
        self.Tab_2_UpperSplitter = QtWidgets.QSplitter(self.Tab_2_LowerSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(20)
        sizePolicy.setHeightForWidth(self.Tab_2_UpperSplitter.sizePolicy().hasHeightForWidth())
        self.Tab_2_UpperSplitter.setSizePolicy(sizePolicy)
        self.Tab_2_UpperSplitter.setOrientation(QtCore.Qt.Horizontal)
        self.Tab_2_UpperSplitter.setObjectName("Tab_2_UpperSplitter")
        self.Tab_2_History = QtWidgets.QListWidget(self.Tab_2_UpperSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_2_History.sizePolicy().hasHeightForWidth())
        self.Tab_2_History.setSizePolicy(sizePolicy)
        self.Tab_2_History.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Tab_2_History.setObjectName("Tab_2_History")
        self.layoutWidget = QtWidgets.QWidget(self.Tab_2_UpperSplitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.Tab_2_verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Tab_2_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Tab_2_verticalLayout.setObjectName("Tab_2_verticalLayout")
        self.Tab_2_Viewer = MplWidget_LaTeX(self.layoutWidget)
        self.Tab_2_Viewer.setObjectName("Tab_2_Viewer")
        self.Tab_2_verticalLayout.addWidget(self.Tab_2_Viewer)
        self.Tab_2_LaTeXOutput = QtWidgets.QLineEdit(self.layoutWidget)
        self.Tab_2_LaTeXOutput.setObjectName("Tab_2_LaTeXOutput")
        self.Tab_2_verticalLayout.addWidget(self.Tab_2_LaTeXOutput)
        self.Tab_2_InputField = QtWidgets.QTextEdit(self.Tab_2_LowerSplitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_2_InputField.sizePolicy().hasHeightForWidth())
        self.Tab_2_InputField.setSizePolicy(sizePolicy)
        self.Tab_2_InputField.setObjectName("Tab_2_InputField")
        self.gridLayout_3.addWidget(self.Tab_2_LowerSplitter, 0, 0, 1, 2)
        self.Tab_2_ConvertButton = QtWidgets.QPushButton(self.Tab_2)
        self.Tab_2_ConvertButton.setObjectName("Tab_2_ConvertButton")
        self.gridLayout_3.addWidget(self.Tab_2_ConvertButton, 1, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Tab_2, "")
        self.Tab_3 = QtWidgets.QWidget()
        self.Tab_3.setObjectName("Tab_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.Tab_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.Tab_3_Button_Clear = QtWidgets.QPushButton(self.Tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_Button_Clear.sizePolicy().hasHeightForWidth())
        self.Tab_3_Button_Clear.setSizePolicy(sizePolicy)
        self.Tab_3_Button_Clear.setObjectName("Tab_3_Button_Clear")
        self.gridLayout_10.addWidget(self.Tab_3_Button_Clear, 1, 3, 1, 1)
        self.Tab_3_Formula_Field = QtWidgets.QLineEdit(self.Tab_3)
        self.Tab_3_Formula_Field.setObjectName("Tab_3_Formula_Field")
        self.gridLayout_10.addWidget(self.Tab_3_Formula_Field, 1, 0, 1, 3)
        self.Tab_3_Button_Plot = QtWidgets.QPushButton(self.Tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_Button_Plot.sizePolicy().hasHeightForWidth())
        self.Tab_3_Button_Plot.setSizePolicy(sizePolicy)
        self.Tab_3_Button_Plot.setObjectName("Tab_3_Button_Plot")
        self.gridLayout_10.addWidget(self.Tab_3_Button_Plot, 1, 4, 1, 1)
        self.Tab_3_gridLayout = QtWidgets.QGridLayout()
        self.Tab_3_gridLayout.setObjectName("Tab_3_gridLayout")
        self.Tab_3_splitter = QtWidgets.QSplitter(self.Tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_splitter.sizePolicy().hasHeightForWidth())
        self.Tab_3_splitter.setSizePolicy(sizePolicy)
        self.Tab_3_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.Tab_3_splitter.setObjectName("Tab_3_splitter")
        self.layoutWidget1 = QtWidgets.QWidget(self.Tab_3_splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Tab_3_gridLayout_upper = QtWidgets.QGridLayout(self.layoutWidget1)
        self.Tab_3_gridLayout_upper.setContentsMargins(0, 0, 0, 0)
        self.Tab_3_gridLayout_upper.setObjectName("Tab_3_gridLayout_upper")
        self.Tab_3_TabWidget = QtWidgets.QTabWidget(self.layoutWidget1)
        self.Tab_3_TabWidget.setObjectName("Tab_3_TabWidget")
        self.Tab_3_Tab_1_History = QtWidgets.QWidget()
        self.Tab_3_Tab_1_History.setObjectName("Tab_3_Tab_1_History")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Tab_3_Tab_1_History)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.Tab_3_History = QtWidgets.QListWidget(self.Tab_3_Tab_1_History)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_History.sizePolicy().hasHeightForWidth())
        self.Tab_3_History.setSizePolicy(sizePolicy)
        self.Tab_3_History.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Tab_3_History.setObjectName("Tab_3_History")
        self.gridLayout_5.addWidget(self.Tab_3_History, 0, 0, 1, 1)
        self.Tab_3_TabWidget.addTab(self.Tab_3_Tab_1_History, "")
        self.Tab_3_Tab_2_Config = QtWidgets.QWidget()
        self.Tab_3_Tab_2_Config.setObjectName("Tab_3_Tab_2_Config")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.Tab_3_Tab_2_Config)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.Tab_3_Tab_2_Config_scrollArea = QtWidgets.QScrollArea(self.Tab_3_Tab_2_Config)
        self.Tab_3_Tab_2_Config_scrollArea.setWidgetResizable(True)
        self.Tab_3_Tab_2_Config_scrollArea.setObjectName("Tab_3_Tab_2_Config_scrollArea")
        self.Tab_3_Tab_2_Config_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.Tab_3_Tab_2_Config_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 238, 293))
        self.Tab_3_Tab_2_Config_scrollAreaWidgetContents.setObjectName("Tab_3_Tab_2_Config_scrollAreaWidgetContents")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.Tab_3_YLim_Check = QtWidgets.QCheckBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_YLim_Check.setObjectName("Tab_3_YLim_Check")
        self.gridLayout_11.addWidget(self.Tab_3_YLim_Check, 8, 0, 1, 1)
        self.Tab_3_XLim_max = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_XLim_max.setDecimals(5)
        self.Tab_3_XLim_max.setMinimum(-1000000.0)
        self.Tab_3_XLim_max.setMaximum(1000000.0)
        self.Tab_3_XLim_max.setProperty("value", 5.0)
        self.Tab_3_XLim_max.setObjectName("Tab_3_XLim_max")
        self.gridLayout_11.addWidget(self.Tab_3_XLim_max, 7, 1, 1, 1)
        self.Tab_3_XLim_min = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_XLim_min.setDecimals(5)
        self.Tab_3_XLim_min.setMinimum(-1000000.0)
        self.Tab_3_XLim_min.setMaximum(1000000.0)
        self.Tab_3_XLim_min.setProperty("value", -5.0)
        self.Tab_3_XLim_min.setObjectName("Tab_3_XLim_min")
        self.gridLayout_11.addWidget(self.Tab_3_XLim_min, 7, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_11.addWidget(self.line_2, 4, 0, 1, 2)
        self.Tab_3_Axis_ratio_Checkbox = QtWidgets.QCheckBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Axis_ratio_Checkbox.setObjectName("Tab_3_Axis_ratio_Checkbox")
        self.gridLayout_11.addWidget(self.Tab_3_Axis_ratio_Checkbox, 5, 1, 1, 1)
        self.Tab_3_To_Spinbox = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_To_Spinbox.setDecimals(5)
        self.Tab_3_To_Spinbox.setMinimum(-1000000.0)
        self.Tab_3_To_Spinbox.setMaximum(1000000.0)
        self.Tab_3_To_Spinbox.setProperty("value", 10.0)
        self.Tab_3_To_Spinbox.setObjectName("Tab_3_To_Spinbox")
        self.gridLayout_11.addWidget(self.Tab_3_To_Spinbox, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_11.addItem(spacerItem1, 12, 0, 1, 2)
        self.Tab_3_Steps_comboBox = QtWidgets.QComboBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Steps_comboBox.setObjectName("Tab_3_Steps_comboBox")
        self.Tab_3_Steps_comboBox.addItem("")
        self.Tab_3_Steps_comboBox.addItem("")
        self.gridLayout_11.addWidget(self.Tab_3_Steps_comboBox, 2, 0, 1, 1)
        self.Tab_3_YLim_max = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_YLim_max.setDecimals(5)
        self.Tab_3_YLim_max.setMinimum(-1000000.0)
        self.Tab_3_YLim_max.setMaximum(1000000.0)
        self.Tab_3_YLim_max.setProperty("value", 50.0)
        self.Tab_3_YLim_max.setObjectName("Tab_3_YLim_max")
        self.gridLayout_11.addWidget(self.Tab_3_YLim_max, 9, 1, 1, 1)
        self.Tab_3_From_Spinbox = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_From_Spinbox.setDecimals(5)
        self.Tab_3_From_Spinbox.setMinimum(-1000000.0)
        self.Tab_3_From_Spinbox.setMaximum(1000000.0)
        self.Tab_3_From_Spinbox.setProperty("value", -10.0)
        self.Tab_3_From_Spinbox.setObjectName("Tab_3_From_Spinbox")
        self.gridLayout_11.addWidget(self.Tab_3_From_Spinbox, 0, 1, 1, 1)
        self.Tab_3_Label_from = QtWidgets.QLabel(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Label_from.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Tab_3_Label_from.setObjectName("Tab_3_Label_from")
        self.gridLayout_11.addWidget(self.Tab_3_Label_from, 0, 0, 1, 1)
        self.Tab_3_XLim_Check = QtWidgets.QCheckBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_XLim_Check.setObjectName("Tab_3_XLim_Check")
        self.gridLayout_11.addWidget(self.Tab_3_XLim_Check, 6, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_11.addWidget(self.line, 11, 0, 1, 2)
        self.Tab_3_YLim_min = QtWidgets.QDoubleSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_YLim_min.setDecimals(5)
        self.Tab_3_YLim_min.setMinimum(-1000000.0)
        self.Tab_3_YLim_min.setMaximum(1000000.0)
        self.Tab_3_YLim_min.setProperty("value", -25.0)
        self.Tab_3_YLim_min.setObjectName("Tab_3_YLim_min")
        self.gridLayout_11.addWidget(self.Tab_3_YLim_min, 9, 0, 1, 1)
        self.Tab_3_Draw_Grid_Checkbox = QtWidgets.QCheckBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Draw_Grid_Checkbox.setChecked(True)
        self.Tab_3_Draw_Grid_Checkbox.setObjectName("Tab_3_Draw_Grid_Checkbox")
        self.gridLayout_11.addWidget(self.Tab_3_Draw_Grid_Checkbox, 5, 0, 1, 1)
        self.Tab_3_Steps_Spinbox = QtWidgets.QSpinBox(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Steps_Spinbox.setMinimum(1)
        self.Tab_3_Steps_Spinbox.setMaximum(100000)
        self.Tab_3_Steps_Spinbox.setProperty("value", 1000)
        self.Tab_3_Steps_Spinbox.setObjectName("Tab_3_Steps_Spinbox")
        self.gridLayout_11.addWidget(self.Tab_3_Steps_Spinbox, 2, 1, 1, 1)
        self.Tab_3_Label_to = QtWidgets.QLabel(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Label_to.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Tab_3_Label_to.setObjectName("Tab_3_Label_to")
        self.gridLayout_11.addWidget(self.Tab_3_Label_to, 1, 0, 1, 1)
        self.Tab_3_Button_Plot_SymPy = QtWidgets.QPushButton(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Button_Plot_SymPy.setObjectName("Tab_3_Button_Plot_SymPy")
        self.gridLayout_11.addWidget(self.Tab_3_Button_Plot_SymPy, 13, 1, 1, 1)
        self.Tab_3_RedrawPlot_Button = QtWidgets.QPushButton(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_RedrawPlot_Button.setObjectName("Tab_3_RedrawPlot_Button")
        self.gridLayout_11.addWidget(self.Tab_3_RedrawPlot_Button, 10, 0, 1, 2)
        self.Tab_3_Button_SavePlot = QtWidgets.QPushButton(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.Tab_3_Button_SavePlot.setObjectName("Tab_3_Button_SavePlot")
        self.gridLayout_11.addWidget(self.Tab_3_Button_SavePlot, 13, 0, 1, 1)
        self.Tab_3_Tab_2_Config_scrollArea.setWidget(self.Tab_3_Tab_2_Config_scrollAreaWidgetContents)
        self.gridLayout_8.addWidget(self.Tab_3_Tab_2_Config_scrollArea, 12, 0, 1, 1)
        self.Tab_3_TabWidget.addTab(self.Tab_3_Tab_2_Config, "")
        self.Tab_3_gridLayout_upper.addWidget(self.Tab_3_TabWidget, 0, 2, 1, 1)
        self.Tab_3_ScrollArea = QtWidgets.QScrollArea(self.Tab_3_splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_ScrollArea.sizePolicy().hasHeightForWidth())
        self.Tab_3_ScrollArea.setSizePolicy(sizePolicy)
        self.Tab_3_ScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Tab_3_ScrollArea.setWidgetResizable(True)
        self.Tab_3_ScrollArea.setObjectName("Tab_3_ScrollArea")
        self.Tab_3_ScrollArea_Layout = QtWidgets.QWidget()
        self.Tab_3_ScrollArea_Layout.setGeometry(QtCore.QRect(0, 0, 573, 472))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_ScrollArea_Layout.sizePolicy().hasHeightForWidth())
        self.Tab_3_ScrollArea_Layout.setSizePolicy(sizePolicy)
        self.Tab_3_ScrollArea_Layout.setObjectName("Tab_3_ScrollArea_Layout")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Tab_3_ScrollArea_Layout)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Tab_3_Display = MplWidget_2D_Plot(self.Tab_3_ScrollArea_Layout)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tab_3_Display.sizePolicy().hasHeightForWidth())
        self.Tab_3_Display.setSizePolicy(sizePolicy)
        self.Tab_3_Display.setObjectName("Tab_3_Display")
        self.gridLayout_6.addWidget(self.Tab_3_Display, 0, 0, 1, 1)
        self.Tab_3_ScrollArea.setWidget(self.Tab_3_ScrollArea_Layout)
        self.Tab_3_gridLayout.addWidget(self.Tab_3_splitter, 0, 0, 1, 1)
        self.gridLayout_10.addLayout(self.Tab_3_gridLayout, 0, 0, 1, 5)
        self.tabWidget.addTab(self.Tab_3, "")
        self.Tab_4 = QtWidgets.QWidget()
        self.Tab_4.setObjectName("Tab_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.Tab_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.Tab_4_Splitter_Main = QtWidgets.QSplitter(self.Tab_4)
        self.Tab_4_Splitter_Main.setOrientation(QtCore.Qt.Horizontal)
        self.Tab_4_Splitter_Main.setObjectName("Tab_4_Splitter_Main")
        self.Tab_4_Splitter_Left = QtWidgets.QSplitter(self.Tab_4_Splitter_Main)
        self.Tab_4_Splitter_Left.setOrientation(QtCore.Qt.Vertical)
        self.Tab_4_Splitter_Left.setObjectName("Tab_4_Splitter_Left")
        self.Tab_4_tabWidget = QtWidgets.QTabWidget(self.Tab_4_Splitter_Left)
        self.Tab_4_tabWidget.setObjectName("Tab_4_tabWidget")
        self.Tab_4_Tab_1 = QtWidgets.QWidget()
        self.Tab_4_Tab_1.setObjectName("Tab_4_Tab_1")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.Tab_4_Tab_1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.Tab_4_1_Dimension_Input = QtWidgets.QLineEdit(self.Tab_4_Tab_1)
        self.Tab_4_1_Dimension_Input.setObjectName("Tab_4_1_Dimension_Input")
        self.gridLayout_9.addWidget(self.Tab_4_1_Dimension_Input, 1, 0, 1, 1)
        self.Tab_4_1_Matrix_Input = QtWidgets.QTableWidget(self.Tab_4_Tab_1)
        self.Tab_4_1_Matrix_Input.setRowCount(3)
        self.Tab_4_1_Matrix_Input.setColumnCount(3)
        self.Tab_4_1_Matrix_Input.setObjectName("Tab_4_1_Matrix_Input")
        self.gridLayout_9.addWidget(self.Tab_4_1_Matrix_Input, 0, 0, 1, 4)
        self.Tab_4_1_Save_Matrix_Button = QtWidgets.QPushButton(self.Tab_4_Tab_1)
        self.Tab_4_1_Save_Matrix_Button.setObjectName("Tab_4_1_Save_Matrix_Button")
        self.gridLayout_9.addWidget(self.Tab_4_1_Save_Matrix_Button, 1, 3, 1, 1)
        self.Tab_4_1_Configure_Button = QtWidgets.QPushButton(self.Tab_4_Tab_1)
        self.Tab_4_1_Configure_Button.setObjectName("Tab_4_1_Configure_Button")
        self.gridLayout_9.addWidget(self.Tab_4_1_Configure_Button, 1, 1, 1, 1)
        self.Tab_4_1_Name_Input = QtWidgets.QLineEdit(self.Tab_4_Tab_1)
        self.Tab_4_1_Name_Input.setObjectName("Tab_4_1_Name_Input")
        self.gridLayout_9.addWidget(self.Tab_4_1_Name_Input, 1, 2, 1, 1)
        self.Tab_4_tabWidget.addTab(self.Tab_4_Tab_1, "")
        self.Tab_4_Tab_2 = QtWidgets.QWidget()
        self.Tab_4_Tab_2.setObjectName("Tab_4_Tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.Tab_4_Tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Tab_4_2_New_Equation_Button = QtWidgets.QPushButton(self.Tab_4_Tab_2)
        self.Tab_4_2_New_Equation_Button.setObjectName("Tab_4_2_New_Equation_Button")
        self.gridLayout_4.addWidget(self.Tab_4_2_New_Equation_Button, 1, 3, 1, 1)
        self.Tab_4_History = QtWidgets.QListWidget(self.Tab_4_Tab_2)
        self.Tab_4_History.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Tab_4_History.setObjectName("Tab_4_History")
        self.gridLayout_4.addWidget(self.Tab_4_History, 0, 0, 1, 4)
        self.Tab_4_2_Load_Selected_Button = QtWidgets.QPushButton(self.Tab_4_Tab_2)
        self.Tab_4_2_Load_Selected_Button.setObjectName("Tab_4_2_Load_Selected_Button")
        self.gridLayout_4.addWidget(self.Tab_4_2_Load_Selected_Button, 1, 2, 1, 1)
        self.Tab_4_2_New_Equation_Name_Input = QtWidgets.QLineEdit(self.Tab_4_Tab_2)
        self.Tab_4_2_New_Equation_Name_Input.setObjectName("Tab_4_2_New_Equation_Name_Input")
        self.gridLayout_4.addWidget(self.Tab_4_2_New_Equation_Name_Input, 1, 1, 1, 1)
        self.Tab_4_tabWidget.addTab(self.Tab_4_Tab_2, "")
        self.Tab_4_Matrix_List = QtWidgets.QListWidget(self.Tab_4_Splitter_Left)
        self.Tab_4_Matrix_List.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.Tab_4_Matrix_List.setObjectName("Tab_4_Matrix_List")
        self.Tab_4_Splitter_Right = QtWidgets.QSplitter(self.Tab_4_Splitter_Main)
        self.Tab_4_Splitter_Right.setOrientation(QtCore.Qt.Vertical)
        self.Tab_4_Splitter_Right.setObjectName("Tab_4_Splitter_Right")
        self.layoutWidget2 = QtWidgets.QWidget(self.Tab_4_Splitter_Right)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.Tab_4_Display_gridLayout = QtWidgets.QGridLayout(self.layoutWidget2)
        self.Tab_4_Display_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.Tab_4_Display_gridLayout.setObjectName("Tab_4_Display_gridLayout")
        self.Tab_4_Display = MplWidget_LaTeX(self.layoutWidget2)
        self.Tab_4_Display.setObjectName("Tab_4_Display")
        self.Tab_4_Display_gridLayout.addWidget(self.Tab_4_Display, 0, 0, 1, 1)
        self.Tab_4_FormulaInput = QtWidgets.QLineEdit(self.layoutWidget2)
        self.Tab_4_FormulaInput.setObjectName("Tab_4_FormulaInput")
        self.Tab_4_Display_gridLayout.addWidget(self.Tab_4_FormulaInput, 1, 0, 1, 1)
        self.Tab_4_DirectInput = QtWidgets.QTextEdit(self.Tab_4_Splitter_Right)
        self.Tab_4_DirectInput.setObjectName("Tab_4_DirectInput")
        self.gridLayout_7.addWidget(self.Tab_4_Splitter_Main, 0, 0, 1, 1)
        self.tabWidget.addTab(self.Tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.Font_Size_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.Font_Size_spinBox.setMinimum(5)
        self.Font_Size_spinBox.setMaximum(25)
        self.Font_Size_spinBox.setProperty("value", 9)
        self.Font_Size_spinBox.setObjectName("Font_Size_spinBox")
        self.gridLayout.addWidget(self.Font_Size_spinBox, 0, 1, 1, 1)
        AMaDiA_Main_Window.setCentralWidget(self.centralwidget)
        self.Menubar_Main = QtWidgets.QMenuBar(AMaDiA_Main_Window)
        self.Menubar_Main.setGeometry(QtCore.QRect(0, 0, 906, 21))
        self.Menubar_Main.setObjectName("Menubar_Main")
        self.Menubar_Main_Options = QtWidgets.QMenu(self.Menubar_Main)
        self.Menubar_Main_Options.setObjectName("Menubar_Main_Options")
        AMaDiA_Main_Window.setMenuBar(self.Menubar_Main)
        self.statusbar = QtWidgets.QStatusBar(AMaDiA_Main_Window)
        self.statusbar.setObjectName("statusbar")
        AMaDiA_Main_Window.setStatusBar(self.statusbar)
        self.Menubar_Main_Options_action_Reload_Modules = QtWidgets.QAction(AMaDiA_Main_Window)
        self.Menubar_Main_Options_action_Reload_Modules.setObjectName("Menubar_Main_Options_action_Reload_Modules")
        self.Menubar_Main_Options_action_Advanced_Mode = QtWidgets.QAction(AMaDiA_Main_Window)
        self.Menubar_Main_Options_action_Advanced_Mode.setCheckable(True)
        self.Menubar_Main_Options_action_Advanced_Mode.setObjectName("Menubar_Main_Options_action_Advanced_Mode")
        self.Menubar_Main_Options_action_Eval_Functions = QtWidgets.QAction(AMaDiA_Main_Window)
        self.Menubar_Main_Options_action_Eval_Functions.setCheckable(True)
        self.Menubar_Main_Options_action_Eval_Functions.setChecked(True)
        self.Menubar_Main_Options_action_Eval_Functions.setObjectName("Menubar_Main_Options_action_Eval_Functions")
        self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display = QtWidgets.QAction(AMaDiA_Main_Window)
        self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display.setCheckable(True)
        self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display.setEnabled(False)
        self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display.setObjectName("Menubar_Main_Options_action_Use_Pretty_LaTeX_Display")
        self.Menubar_Main_Options.addAction(self.Menubar_Main_Options_action_Reload_Modules)
        self.Menubar_Main_Options.addAction(self.Menubar_Main_Options_action_Advanced_Mode)
        self.Menubar_Main_Options.addAction(self.Menubar_Main_Options_action_Eval_Functions)
        self.Menubar_Main_Options.addAction(self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display)
        self.Menubar_Main.addAction(self.Menubar_Main_Options.menuAction())

        self.retranslateUi(AMaDiA_Main_Window)
        self.tabWidget.setCurrentIndex(0)
        self.Tab_3_TabWidget.setCurrentIndex(0)
        self.Tab_3_Steps_comboBox.setCurrentIndex(0)
        self.Tab_4_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AMaDiA_Main_Window)
        AMaDiA_Main_Window.setTabOrder(self.Font_Size_spinBox, self.tabWidget)
        AMaDiA_Main_Window.setTabOrder(self.tabWidget, self.Tab_1_History)
        AMaDiA_Main_Window.setTabOrder(self.Tab_1_History, self.Tab_1_InputField)
        AMaDiA_Main_Window.setTabOrder(self.Tab_1_InputField, self.Tab_2_InputField)
        AMaDiA_Main_Window.setTabOrder(self.Tab_2_InputField, self.Tab_2_ConvertButton)
        AMaDiA_Main_Window.setTabOrder(self.Tab_2_ConvertButton, self.Tab_2_LaTeXOutput)
        AMaDiA_Main_Window.setTabOrder(self.Tab_2_LaTeXOutput, self.Tab_2_History)
        AMaDiA_Main_Window.setTabOrder(self.Tab_2_History, self.Tab_3_Formula_Field)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Formula_Field, self.Tab_3_Button_Plot)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Button_Plot, self.Tab_3_Button_Clear)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Button_Clear, self.Tab_3_ScrollArea)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_ScrollArea, self.Tab_3_TabWidget)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_TabWidget, self.Tab_3_History)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_History, self.Tab_3_Tab_2_Config_scrollArea)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Tab_2_Config_scrollArea, self.Tab_3_From_Spinbox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_From_Spinbox, self.Tab_3_To_Spinbox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_To_Spinbox, self.Tab_3_Steps_comboBox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Steps_comboBox, self.Tab_3_Steps_Spinbox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Steps_Spinbox, self.Tab_3_Draw_Grid_Checkbox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Draw_Grid_Checkbox, self.Tab_3_Axis_ratio_Checkbox)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_Axis_ratio_Checkbox, self.Tab_3_XLim_Check)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_XLim_Check, self.Tab_3_XLim_min)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_XLim_min, self.Tab_3_XLim_max)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_XLim_max, self.Tab_3_YLim_Check)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_YLim_Check, self.Tab_3_YLim_min)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_YLim_min, self.Tab_3_YLim_max)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_YLim_max, self.Tab_3_RedrawPlot_Button)
        AMaDiA_Main_Window.setTabOrder(self.Tab_3_RedrawPlot_Button, self.Tab_3_Button_Plot_SymPy)

    def retranslateUi(self, AMaDiA_Main_Window):
        _translate = QtCore.QCoreApplication.translate
        AMaDiA_Main_Window.setWindowTitle(_translate("AMaDiA_Main_Window", "AMaDiA"))
        self.Tab_1_InputField.setPlaceholderText(_translate("AMaDiA_Main_Window", "Enter something and hit return to calculate. Use crtl+return to not solve divisions, roots, etc."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_1), _translate("AMaDiA_Main_Window", "Calculator"))
        self.Tab_2_LaTeXOutput.setToolTip(_translate("AMaDiA_Main_Window", "Only First line of Input!"))
        self.Tab_2_InputField.setPlaceholderText(_translate("AMaDiA_Main_Window", "Add Mathematical Expression to be Converted to LaTeX. Use crtl+return or the Convert button to display. (First use after start can take a few secconds) Please give Feedback if return should convert and shift+return adds a new line instead!"))
        self.Tab_2_ConvertButton.setToolTip(_translate("AMaDiA_Main_Window", "<html><head/><body><p>Shortcut: crtl+return while having the Input field selected</p></body></html>"))
        self.Tab_2_ConvertButton.setText(_translate("AMaDiA_Main_Window", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_2), _translate("AMaDiA_Main_Window", "LaTeX"))
        self.Tab_3_Button_Clear.setText(_translate("AMaDiA_Main_Window", "Clear"))
        self.Tab_3_Formula_Field.setPlaceholderText(_translate("AMaDiA_Main_Window", "Enter a function f(x) (eg. \"x^2\" or a constant (eg. \"23+4\" for a horizontal line or \"x=23+4\" for a vertical line at 27) and hit return."))
        self.Tab_3_Button_Plot.setText(_translate("AMaDiA_Main_Window", "Plot"))
        self.Tab_3_TabWidget.setTabText(self.Tab_3_TabWidget.indexOf(self.Tab_3_Tab_1_History), _translate("AMaDiA_Main_Window", "History"))
        self.Tab_3_YLim_Check.setToolTip(_translate("AMaDiA_Main_Window", "Limit the part of the y axis that is shown"))
        self.Tab_3_YLim_Check.setText(_translate("AMaDiA_Main_Window", "Limit Y"))
        self.Tab_3_Axis_ratio_Checkbox.setText(_translate("AMaDiA_Main_Window", "1:1 axis ratio"))
        self.Tab_3_Steps_comboBox.setCurrentText(_translate("AMaDiA_Main_Window", "Steps total"))
        self.Tab_3_Steps_comboBox.setItemText(0, _translate("AMaDiA_Main_Window", "Steps total"))
        self.Tab_3_Steps_comboBox.setItemText(1, _translate("AMaDiA_Main_Window", "Steps per Unit"))
        self.Tab_3_Label_from.setText(_translate("AMaDiA_Main_Window", "From"))
        self.Tab_3_XLim_Check.setToolTip(_translate("AMaDiA_Main_Window", "Limit the part of the x axis that is shown"))
        self.Tab_3_XLim_Check.setText(_translate("AMaDiA_Main_Window", "Limit X"))
        self.Tab_3_Draw_Grid_Checkbox.setText(_translate("AMaDiA_Main_Window", "Draw Grid"))
        self.Tab_3_Label_to.setText(_translate("AMaDiA_Main_Window", "To"))
        self.Tab_3_Button_Plot_SymPy.setToolTip(_translate("AMaDiA_Main_Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">It is advised to use the normal Plot.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Note:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- Control the Plotted area with Limit X and Limit Y</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">    (Don\'t forget to enable these with the checkboxes)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- Opens new window</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Advantages of SymPy Plotting:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- Easier zomming</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- More options when saving the Plot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">Disadvantages:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- Plots are not saved in the History</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- (Currently) Only one graph per plot</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- (Currently) Limited configuration via the main window</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">- Can not plot as many functions as the main plotter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">  (The main plotter has several methods of plotting which are used</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">   if the normal method fails while the SymPy plotter only has the normal method)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.Tab_3_Button_Plot_SymPy.setText(_translate("AMaDiA_Main_Window", "Plot with SymPy"))
        self.Tab_3_RedrawPlot_Button.setToolTip(_translate("AMaDiA_Main_Window", "Apply settings"))
        self.Tab_3_RedrawPlot_Button.setText(_translate("AMaDiA_Main_Window", "Redraw Plot"))
        self.Tab_3_Button_SavePlot.setToolTip(_translate("AMaDiA_Main_Window", "<html><head/><body><p>Save the current Plot (exactly as displayed including size and resoltuion)</p><p>as a .png in the Plots folder where the AMaDiA.py is located.</p><p>Tip: This option is also accessible in the right klick menu of the Plot.</p></body></html>"))
        self.Tab_3_Button_SavePlot.setText(_translate("AMaDiA_Main_Window", "Save Plot"))
        self.Tab_3_TabWidget.setTabText(self.Tab_3_TabWidget.indexOf(self.Tab_3_Tab_2_Config), _translate("AMaDiA_Main_Window", "Config"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_3), _translate("AMaDiA_Main_Window", "2D Plot"))
        self.Tab_4_1_Dimension_Input.setInputMask(_translate("AMaDiA_Main_Window", "00\\xD0"))
        self.Tab_4_1_Dimension_Input.setText(_translate("AMaDiA_Main_Window", "3x3"))
        self.Tab_4_1_Save_Matrix_Button.setText(_translate("AMaDiA_Main_Window", "Save"))
        self.Tab_4_1_Configure_Button.setText(_translate("AMaDiA_Main_Window", "Configure"))
        self.Tab_4_1_Name_Input.setPlaceholderText(_translate("AMaDiA_Main_Window", "Name"))
        self.Tab_4_tabWidget.setTabText(self.Tab_4_tabWidget.indexOf(self.Tab_4_Tab_1), _translate("AMaDiA_Main_Window", "Matrix Input"))
        self.Tab_4_2_New_Equation_Button.setText(_translate("AMaDiA_Main_Window", "New Equation"))
        self.Tab_4_2_Load_Selected_Button.setText(_translate("AMaDiA_Main_Window", "Load Selected"))
        self.Tab_4_2_New_Equation_Name_Input.setToolTip(_translate("AMaDiA_Main_Window", "Enter the equation name"))
        self.Tab_4_2_New_Equation_Name_Input.setPlaceholderText(_translate("AMaDiA_Main_Window", "Enter the equation name"))
        self.Tab_4_tabWidget.setTabText(self.Tab_4_tabWidget.indexOf(self.Tab_4_Tab_2), _translate("AMaDiA_Main_Window", "History"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab_4), _translate("AMaDiA_Main_Window", "Multi-Dim"))
        self.Font_Size_spinBox.setToolTip(_translate("AMaDiA_Main_Window", "Font Size"))
        self.Menubar_Main_Options.setTitle(_translate("AMaDiA_Main_Window", "O&ptions"))
        self.Menubar_Main_Options_action_Reload_Modules.setText(_translate("AMaDiA_Main_Window", "Reload Modules"))
        self.Menubar_Main_Options_action_Advanced_Mode.setText(_translate("AMaDiA_Main_Window", "Advanced Mode"))
        self.Menubar_Main_Options_action_Eval_Functions.setText(_translate("AMaDiA_Main_Window", "Eval Functions"))
        self.Menubar_Main_Options_action_Use_Pretty_LaTeX_Display.setText(_translate("AMaDiA_Main_Window", "Use Pretty LaTeX Display"))

from AMaDiA_Widgets import MplWidget_2D_Plot, MplWidget_LaTeX
