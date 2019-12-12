# This Python file uses the following encoding: utf-8

# if__name__ == "__main__":
#     pass

import sys
sys.path.append('..')
from PyQt5 import QtWidgets,QtCore,QtGui,Qt#,QtQuick
#QtQuick.
#from PyQt5.QtQuick import Controls as QtControls
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas #CLEANUP: Delete this line?
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('Qt5Agg')
from mpl_toolkits.axes_grid1 import Divider, Size
from mpl_toolkits.axes_grid1.mpl_axes import Axes
import numpy as np
import scipy
import sympy
from sympy.parsing.sympy_parser import parse_expr
import re
import time

import warnings

from External_Libraries.python_control_master import control

from AMaDiA_Files import AMaDiA_Functions as AF
from AMaDiA_Files.AMaDiA_Functions import common_exceptions, ExceptionOutput, NotificationEvent, sendNotification
from AMaDiA_Files import AMaDiA_Classes as AC
from AMaDiA_Files import AMaDiA_ReplacementTables as ART

import importlib
def ReloadModules():
    importlib.reload(AF)
    importlib.reload(AC)
    importlib.reload(ART)


# Use MplWidget for things that have a matplot output
# Ensure using PyQt5 backend
#matplotlib.use('QT5Agg')

# Matplotlib canvas class to create figure

class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MplWidget, self).__init__(parent)

    def SetColour(self,BG,FG):
        self.background_Colour = BG
        self.TextColour = FG
        self.HexcolourText = '#%02x%02x%02x' % (int(self.TextColour[0]*255),int(self.TextColour[1]*255),int(self.TextColour[2]*255))
        try:
            self.canvas.fig.set_facecolor(self.background_Colour)
            self.canvas.fig.set_edgecolor(self.background_Colour)
            self.canvas.ax.set_facecolor(self.background_Colour)
        except common_exceptions:
            ExceptionOutput(sys.exc_info())
        try:
            self.canvas.draw()
        except common_exceptions:
            ExceptionOutput(sys.exc_info())

    #def eventFilter(self, source, event):
    #    if event.type() == QtCore.QEvent.PaletteChange:
    #        try:
    #            source.SetColour(QtWidgets.QApplication.instance().BG_Colour , QtWidgets.QApplication.instance().TextColour)
    #        except common_exceptions:
    #            ExceptionOutput(sys.exc_info())
    #    return super(MplWidget, self).eventFilter(source, event)

# -----------------------------------------------------------------------------------------------------------------

class MplCanvas_2D_Plot(Canvas):
    def __init__(self):
        #plt.style.use('dark_background')
        self.fig = Figure(constrained_layout =True)
        self.fig.set_facecolor(AF.background_Colour)
        
        self.ax = self.fig.add_subplot(111)
        
        self.ax.set_facecolor(AF.background_Colour)
        
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        Canvas.updateGeometry(self)

# Matplotlib widget
class MplWidget_2D_Plot(MplWidget):
    # Inspired by https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5?noredirect=1&lq=1 from 10.07.2019
    def __init__(self, parent=None):
        super(MplWidget_2D_Plot, self).__init__(parent)
        QtWidgets.QWidget.__init__(self)           # Inherit from QWidget
        self.canvas = MplCanvas_2D_Plot()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.layout().setContentsMargins(0,0,0,0)
        
    def SetColour(self,BG,FG):
        super(MplWidget_2D_Plot, self).SetColour(BG,FG)
        self.canvas.ax.spines['bottom'].set_color(self.TextColour)
        self.canvas.ax.spines['left'].set_color(self.TextColour)
        self.canvas.ax.xaxis.label.set_color(self.TextColour)
        self.canvas.ax.yaxis.label.set_color(self.TextColour)
        self.canvas.ax.tick_params(axis='x', colors=self.TextColour)
        self.canvas.ax.tick_params(axis='y', colors=self.TextColour)
        self.canvas.draw()
    
    def UseTeX(self,TheBool):
        # This Method changes the settings for not only one but all widgets...
        # This makes the clear function of the plotter slow if the LaTeX display has been used in LaTeX mode directly before
        # It could help to separate the two widgets into two files...
        # ... but it is also possible that this setting is global not only for the file but the program which would make the seperation a massive waste of time...
        # Maybe test this in a little testprogram to not waste that much time...
        
        #Both seem to do the same:
        matplotlib.rcParams['text.usetex'] = TheBool
        plt.rc('text', usetex=TheBool)
        return matplotlib.rcParams['text.usetex']

# -----------------------------------------------------------------------------------------------------------------
class MplCanvas_LaTeX(Canvas):
    def __init__(self,w,h):
        #plt.style.use('dark_background')
        #self.fig = Figure(constrained_layout =True)
        self.fig = Figure(figsize = (w,h),dpi=90)
        self.fig.set_facecolor(AF.background_Colour)
        
        #h = [Size.Fixed(1.0), Size.Fixed(4.5)]
        #v = [Size.Fixed(0.7), Size.Fixed(5.)]
        #divider = Divider(self.fig, (0.0, 0.0, 1., 1.), h, v, aspect=False)
        
        self.ax = self.fig.add_subplot(111)
        #self.ax = Axes(self.fig, divider.get_position())
        
        self.ax.set_facecolor(AF.background_Colour)
        self.ax.set_anchor('W')
        self.fig.subplots_adjust(left=0.01)
        self.ax.axis('off')
        
        #self.ax.set_axes_locator(divider.new_locator(nx=1, ny=1))
        #self.fig.add_axes(self.ax)
        
        Canvas.__init__(self, self.fig)
        #Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        #Canvas.updateGeometry(self)

class MplWidget_LaTeX(MplWidget):
    def __init__(self, parent=None):
        super(MplWidget_LaTeX, self).__init__(parent)
        QtWidgets.QWidget.__init__(self)           # Inherit from QWidget
        self.canvas = MplCanvas_LaTeX(100,100)                  # Create canvas object
        #self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        #self.vbl.addWidget(self.canvas)
        #self.setLayout(self.vbl)
        
        self.setLayout(QtWidgets.QVBoxLayout())
        self.scroll = QtWidgets.QScrollArea(self)
        self.scroll.setWidget(self.canvas)

        #self.Tab_2_LaTeX_LaTeXOutput.nav = NavigationToolbar(self.Tab_2_LaTeX_LaTeXOutput.canvas, self.Tab_2_LaTeX_LaTeXOutput)
        #self.Tab_2_LaTeX_LaTeXOutput.layout().addWidget(self.Tab_2_LaTeX_LaTeXOutput.nav)
        self.layout().addWidget(self.scroll)
        self.layout().setContentsMargins(0,0,0,0)

        self.LastCall = False
        
    def SetColour(self,BG,FG):
        super(MplWidget_LaTeX, self).SetColour(BG,FG)
        if self.LastCall != False:
            self.Display(self.LastCall[0],self.LastCall[1],self.LastCall[2],self.LastCall[3])
        else:
            try:
                self.canvas.draw()
            except common_exceptions:
                pass
    
    def UseTeX(self,TheBool):
        # This Method changes the settings for not only one but all widgets...
        # This makes the clear function of the plotter slow if the LaTeX display has been used in LaTeX mode directly before
        # It could help to separate the two widgets into two files...
        # ... but it is also possible that this setting is global not only for the file but the program which would make the seperation a massive waste of time...
        # Maybe test this in a little testprogram to not waste that much time...
        
        matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
        #Both seem to do the same:
        matplotlib.rcParams['text.usetex'] = TheBool
        plt.rc('text', usetex=TheBool)
        return matplotlib.rcParams['text.usetex']

    def PreloadLaTeX(self):
        try:
            self.UseTeX(True)
            self.canvas.ax.clear()
            self.canvas.ax.set_title("$1$",
                        loc = "left",
                        y=(1.15-(20/5000)),
                        horizontalalignment='left',
                        verticalalignment='top',
                        fontsize=20,
                        color = "white"
                        ,bbox=dict(boxstyle="round", facecolor="black",
                        ec="0.1", pad=0.1, alpha=0)
                        )
            self.canvas.ax.axis('off')
            self.canvas.draw()
            time.sleep(0.1)
            self.canvas.ax.clear()
            self.canvas.ax.axis('off')
            self.canvas.draw()
            self.UseTeX(False)
        except common_exceptions:
            try:
                self.UseTeX(False)
            except common_exceptions:
                ExceptionOutput(sys.exc_info())
            ExceptionOutput(sys.exc_info())
    
    def Display(self,Text_L,Text_N,Font_Size,Use_LaTeX = False):
        """
        Retrun Value compatible with NotifyUser.\n
        Returns (0,0) if everything worked, (3,str) if minor exception, (2,str) if medium exception, (1,str) if not able to display
        """
        self.LastCall = [Text_L, Text_N, Font_Size, Use_LaTeX]

        #SIMPLIFY: https://matplotlib.org/3.1.1/_modules/matplotlib/text.html#Text _get_rendered_text_width and similar
        # Use this to adjust the size of the "plot" to the Text?

        # You can set Usetex for each individual text object. Example:
        # plt.xlabel('$x$', usetex=True)

        self.Text = Text_L
        self.Font_Size = Font_Size * 2
        returnTuple = (0,0)
        #-----------IMPORTANT-----------
        if Use_LaTeX:
            self.Text = Text_L
            self.UseTeX(True)
        else:
            self.UseTeX(False)
            Text_N = Text_N.replace("\limits","") # pylint: disable=anomalous-backslash-in-string
            self.Text = Text_N
        #-----------IMPORTANT-----------
        self.w=9
        self.h=9
        #self.canvas = MplCanvas_LaTeX(self.w+1, self.h+1) 
        #self.scroll.setWidget(self.canvas)
        #self.layout().addWidget(self.scroll)
        #self.canvas.resize(self.w+1, self.h+1)
        #self.canvas.__init__(self.w+1, self.h+1)
        self.canvas.ax.clear() # makes Space for the new text
        
        
        self.canvas.ax.set_title(self.Text,
                      loc = "left",
                      #x=-0.12,
                      y=(1.15-(self.Font_Size/5000)),
                      horizontalalignment='left',
                      verticalalignment='top',
                      fontsize=self.Font_Size,
                      color = self.TextColour
                      ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                      ec="0.1", pad=0.1, alpha=0)
                      )
                      
        """ For Figure(figsize = (100,100),dpi=90)
        self.canvas.ax.set_title(self.Text,
                      loc = "left",
                      #x=-0.12,
                      y=(1.15-(self.Font_Size/5000)),
                      horizontalalignment='left',
                      verticalalignment='top',
                      fontsize=self.Font_Size,
                      color = self.TextColour
                      ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                      ec="0.1", pad=0.1, alpha=0)
                      )
        """
        """ For Figure(figsize = (100,10),dpi=90)
        self.canvas.ax.set_title(self.Text,
                      loc = "left",
                      #x=-0.12,
                      y=(1.195-(self.Font_Size/180)),
                      horizontalalignment='left',
                      verticalalignment='top',
                      fontsize=self.Font_Size,
                      color = self.TextColour
                      ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                      ec="0.1", pad=0.1, alpha=0)
                      )
        """
        
        self.canvas.ax.axis('off')
        # Show the "graph"
        try:
            self.canvas.draw()
        except common_exceptions:
            returnTuple = (4,"Could not display in Mathmode")
            self.Text = Text_N
            if Use_LaTeX:
                self.UseTeX(True)
            else:
                self.UseTeX(False)
            self.canvas.ax.clear()
            self.canvas.ax.set_title(self.Text,
                      loc = "left",
                      #x=-0.12,
                      y=(1.15-(self.Font_Size/5000)),
                      horizontalalignment='left',
                      verticalalignment='top',
                      fontsize=self.Font_Size,
                      color = self.TextColour
                      ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                      ec="0.1", pad=0.1, alpha=0)
                      )
            self.canvas.ax.axis('off')
            #--------------------------
            
            try:
                self.canvas.draw()
            except common_exceptions:
                ExceptionOutput(sys.exc_info())
                print("Trying to output without LaTeX")
                returnTuple = (2,"Could not display with LaTeX")
                self.Text = Text_N.replace("\limits","") # pylint: disable=anomalous-backslash-in-string
                self.UseTeX(False)
                self.canvas.ax.clear()
                self.canvas.ax.set_title(self.Text,
                          loc = "left",
                          #x=-0.12,
                          y=(1.15-(self.Font_Size/5000)),
                          horizontalalignment='left',
                          verticalalignment='top',
                          fontsize=self.Font_Size,
                          color = self.TextColour
                          ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                          ec="0.1", pad=0.1, alpha=0)
                          )
                self.canvas.ax.axis('off')
                #--------------------------
                try:
                    self.canvas.draw()
                except common_exceptions:
                    ExceptionOutput(sys.exc_info())
                    returnTuple = (1,"Could not display at all")
                    self.UseTeX(False)
                    self.canvas.ax.clear()
                    if Use_LaTeX:
                        ErrorText = "The text can't be displayed. Please send your input and a description of your problem to the developer"
                    else:
                        ErrorText = "The text can't be displayed. Please note that many things can't be displayed without LaTeX Mode."
                        if not AF.LaTeX_dvipng_Installed:
                            ErrorText += "\n Please install LaTeX (and dvipng if it is not already included in your LaTeX distribution) and restart AMaDiA"
                    self.canvas.ax.set_title(ErrorText,
                            loc = "left",
                            #x=-0.12,
                            y=(1.15-(self.Font_Size/5000)),
                            horizontalalignment='left',
                            verticalalignment='top',
                            fontsize=self.Font_Size,
                            color = self.TextColour
                            ,bbox=dict(boxstyle="round", facecolor=self.background_Colour,
                            ec="0.1", pad=0.1, alpha=0)
                            )
                    self.canvas.ax.axis('off')
                    try:
                        self.canvas.draw()
                    except common_exceptions:
                        ExceptionOutput(sys.exc_info())
                        returnTuple = (1,"Critical Error: MatPlotLib Display seems broken")
                        print("Can not display anything")
                
        finally:
            self.UseTeX(False)
            return returnTuple


# -----------------------------------------------------------------------------------------------------------------

class MplCanvas_CONTROL(Canvas):
    Titles = ['Step Response','Impulse Response','Forced Response',
                        'Bode Plot','BODE_PLOT_2',
                        'Nyquist Plot','Nichols Plot','Pole-Zero-Plot',
                        'Root-Locus-Plot','LaTeX-Display']
    def __init__(self):
        #self.fig = Figure()
        self.fig = plt.figure(num="CONTROL",constrained_layout =True)
        self.fig.set_facecolor(AF.background_Colour)

        combined = True # should Phase and Magnitude of the Bodeplot share a plot?
        if combined:
            self.gs = self.fig.add_gridspec(3, 3)
            
            self.p_step_response = self.fig.add_subplot(self.gs[0,0])
            self.p_impulse_response = self.fig.add_subplot(self.gs[0,1])
            self.p_forced_response = self.fig.add_subplot(self.gs[0,2])
            self.p_bode_plot_1 = self.fig.add_subplot(self.gs[1,0])
            self.p_bode_plot_2 = self.p_bode_plot_1.twinx()
            self.p_nyquist_plot = self.fig.add_subplot(self.gs[1,1])
            self.p_nichols_plot = self.fig.add_subplot(self.gs[1,2])
            self.p_pzmap = self.fig.add_subplot(self.gs[2:,0])
            self.p_root_locus = self.fig.add_subplot(self.gs[2:,1])
            self.p_LaTeX_Display = self.fig.add_subplot(self.gs[2:,2])
        
        else:
            self.gs = self.fig.add_gridspec(6, 3)
            
            self.p_step_response = self.fig.add_subplot(self.gs[0:2,0])
            self.p_impulse_response = self.fig.add_subplot(self.gs[0:2,1])
            self.p_TODO = self.fig.add_subplot(self.gs[0:2,2])     #TODO
            self.p_bode_plot_2 = self.fig.add_subplot(self.gs[3,0])
            self.p_bode_plot_1 = self.fig.add_subplot(self.gs[2,0],sharex=self.p_bode_plot_2)
            self.p_nyquist_plot = self.fig.add_subplot(self.gs[2:4,1])
            self.p_nichols_plot = self.fig.add_subplot(self.gs[2:4,2])
            self.p_pzmap = self.fig.add_subplot(self.gs[4:,0])
            self.p_root_locus = self.fig.add_subplot(self.gs[4:,1])
            self.p_LaTeX_Display = self.fig.add_subplot(self.gs[4:,2])

        self.p_plot_LIST = [ self.p_step_response, self.p_impulse_response, self.p_forced_response,
                            self.p_bode_plot_1, self.p_bode_plot_2,
                            self.p_nyquist_plot, self.p_nichols_plot, self.p_pzmap,
                            self.p_root_locus, self.p_LaTeX_Display]
        
        for i,p in enumerate(self.p_plot_LIST):
            p.set_facecolor(AF.background_Colour)
            if self.Titles[i] == "BODE_PLOT_2":
                p.set_title("  ")
            elif self.Titles[i] != 'LaTeX-Display':
                p.set_title(self.Titles[i])
            # set labels that control can find the axes
            if self.Titles[i] == "Bode Plot":
                p.set_label('control-bode-magnitude')
            elif self.Titles[i] == "BODE_PLOT_2":
                p.set_label('control-bode-phase')
            #elif self.Titles[i] == 'Nyquist Plot':
            #    p.set_label('control-nyquist')
        #self.fig.tight_layout()
        
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        Canvas.updateGeometry(self)

class MplWidget_CONTROL(MplWidget):
    def __init__(self, parent=None):
        super(MplWidget_CONTROL, self).__init__(parent)
        QtWidgets.QWidget.__init__(self)           # Inherit from QWidget
        self.canvas = MplCanvas_CONTROL()                  # Create canvas object
        self.vbl = QtWidgets.QVBoxLayout()         # Set box for plotting
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)
        self.layout().setContentsMargins(0,0,0,0)
        
        
        #self.setLayout(QtWidgets.QVBoxLayout())
        #self.scroll = QtWidgets.QScrollArea(self)
        #self.scroll.setWidget(self.canvas)

        self.Curr_Sys = (None, None, 0.0, 0.0, "", "")
        self.LastCall = False
        self.Curr_Sys_LaTeX = ""
        
    def SetColour(self,BG=None,FG=None):
        try:
            if BG != None and FG != None:
                self.background_Colour = BG
                self.TextColour = FG
                self.HexcolourText = '#%02x%02x%02x' % (int(self.TextColour[0]*255),int(self.TextColour[1]*255),int(self.TextColour[2]*255))
            self.canvas.fig.set_facecolor(self.background_Colour)
            self.canvas.fig.set_edgecolor(self.background_Colour)
            for i,p in enumerate(self.canvas.p_plot_LIST):
                p.set_facecolor(self.background_Colour)
                if p.get_title() == "N/A":
                    p.axis('off')
                    p.text(0.5,0.5,"N/A", horizontalalignment='center', verticalalignment='center',color=self.TextColour)
                    p.set_title(self.canvas.Titles[i],color=self.TextColour)
                    continue
                if self.canvas.Titles[i] == "BODE_PLOT_2":
                    p.set_title("  ",color=self.TextColour)
                elif self.canvas.Titles[i] != 'LaTeX-Display':
                    p.set_title(self.canvas.Titles[i],color=self.TextColour)
                if self.canvas.Titles[i] == "BODE_PLOT_2" or self.canvas.Titles[i] == 'Bode Plot':
                    p.spines['right'].set_color(self.TextColour)
                else:
                    p.yaxis.label.set_color(self.TextColour)
                p.xaxis.label.set_color(self.TextColour)
                p.spines['bottom'].set_color(self.TextColour)
                p.spines['left'].set_color(self.TextColour)
                p.tick_params(axis='x', colors=self.TextColour)
                p.tick_params(axis='y', colors=self.TextColour)
                if self.canvas.Titles[i] == 'LaTeX-Display':
                    p.axis('off')
            self.canvas.p_LaTeX_Display.text(0.5,0.5,self.Curr_Sys_LaTeX, horizontalalignment='center', verticalalignment='center',color=self.TextColour)#,usetex=True)
            if self.Curr_Sys[4] != "" and False: # Disabled since the Legend covers the entire axes when Window not fullscreen
                self.canvas.p_forced_response.legend(["Input Function: "+self.Curr_Sys[4]])#,color=self.TextColour)
        except common_exceptions:
            ExceptionOutput(sys.exc_info())
        try:
            self.canvas.draw()
        except common_exceptions:
            ExceptionOutput(sys.exc_info())
        
        #if self.LastCall != False:
        #    self.Display(self.LastCall[0],self.LastCall[1],self.LastCall[2],self.LastCall[3])
        #else:
        #    try:
        #        self.canvas.draw()
        #    except common_exceptions:
        #        pass
    
    def UseTeX(self,TheBool):
        # This Method changes the settings for not only one but all widgets...
        # This makes the clear function of the plotter slow if the LaTeX display has been used in LaTeX mode directly before
        # It could help to separate the two widgets into two files...
        # ... but it is also possible that this setting is global not only for the file but the program which would make the seperation a massive waste of time...
        # Maybe test this in a little testprogram to not waste that much time...
        
        matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{amsmath}'
        #Both seem to do the same:
        matplotlib.rcParams['text.usetex'] = TheBool
        plt.rc('text', usetex=TheBool)
        return matplotlib.rcParams['text.usetex']
    
    def Display(self,sys1,Use_LaTeX = False, T=None, X0 = 0.0, U=0.0, Ufunc = ""):
        """
        Retrun Value compatible with NotifyUser.
        sys1 = System
        Use_LaTeX = bool
        T = Time steps at which the input is defined; values must be evenly spaced.
        X0 = Initial condition
        U = Input array giving input at each time T used for "Forced Response"-plot
        Ufunc = string (Name of the function that created U)
        """
        returnTuple = (0,"")
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore")
                for i in self.canvas.p_plot_LIST:
                    i.clear()
            Torig = T
            Uorig = U
            try:
                if T == None:
                    syst = control.timeresp._get_ss_simo(sys1)
                    T = scipy.signal.ltisys._default_response_times(syst.A, 500)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))


            # If U not given try to create using Ufunc. If Ufunc not given or creation failed set U and Ufunc to 0
            if U == 0.0:
                if Ufunc != "":
                    try:
                        Function = parse_expr(AF.AstusParse(Ufunc))
                        x = sympy.symbols('x')
                        evalfunc = sympy.lambdify(x, Function, modules=['numpy','sympy'])
                        U = evalfunc(T)
                        U = np.asarray(U)
                        if type(U) == int or type(U) == float or U.shape == (): #This also catches the case exp(x)
                            U = np.full_like(T, U)
                        if U.shape != T.shape:
                            raise Exception("Dimensions do not match")
                    except common_exceptions:
                        ExceptionOutput(sys.exc_info())
                        Ufunc = ""
                if Ufunc == "":
                    Ufunc = "u(x)=0"


            self.Curr_Sys_LaTeX = str(sys1) #TODO: MAKE PROPER LaTeX
            self.Curr_Sys = (sys1, Torig, X0, Uorig, Ufunc, self.Curr_Sys_LaTeX)


            self.canvas.p_bode_plot_1.set_label('control-bode-magnitude')
            self.canvas.p_bode_plot_2.set_label('control-bode-phase')
            
        except common_exceptions:
            returnTuple = (1, ExceptionOutput(sys.exc_info()))
            self.UseTeX(False)
            return returnTuple
        try:
            try: # 0
                oT,y = control.step_response(sys1, number_of_samples=500, T=T, X0 = X0)
                self.canvas.p_step_response.plot(oT,y)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_step_response.set_title("N/A")

            try: # 1
                oT,y = control.impulse_response(sys1, number_of_samples=500, T=T, X0 = X0)
                self.canvas.p_impulse_response.plot(oT,y)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_impulse_response.set_title("N/A")

            try: # 2
                oT,y, xout = control.forced_response(sys1, T=T, X0 = X0, U=U) # pylint: disable=unused-variable
                self.canvas.p_forced_response.plot(oT,y)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_forced_response.set_title("N/A")

            try: # 3+4
                plt.figure(self.canvas.fig.number) # set figure to current that .gfc() in control.bode_plot can find it
                control.bode_plot(sys1, dB=True, omega_num=500)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_bode_plot_1.set_title("N/A")

            try: # 5
                plt.sca(self.canvas.p_nyquist_plot)
                control.nyquist_plot(sys1,number_of_samples=500)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_nyquist_plot.set_title("N/A")

            try: # 6
                plt.sca(self.canvas.p_nichols_plot)
                control.nichols_plot(sys1, number_of_samples=500)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_nichols_plot.set_title("N/A")

            try: # 7
                poles,zeros = control.pzmap(sys1,Plot=False)
                if len(poles) > 0:
                    self.canvas.p_pzmap.scatter(np.real(poles), np.imag(poles), s=50, marker='x', c="red")
                if len(zeros) > 0:
                    self.canvas.p_pzmap.scatter(np.real(zeros), np.imag(zeros), s=25, marker='o', c="orange")
                self.canvas.p_pzmap.grid(True)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_pzmap.set_title("N/A")

            try: # 8
                #plt.sca(self.canvas.p_root_locus)
                #control.rlocus(sys1)
                control.root_locus_AMaDiA(sys1,self.canvas.p_root_locus)
                self.canvas.p_root_locus.grid(True)
            except common_exceptions:
                returnTuple = (3, returnTuple[1]+"\n"+ExceptionOutput(sys.exc_info()))
                self.canvas.p_root_locus.set_title("N/A")

            # 9 + Plot
            self.SetColour() # Set Colour, Titles, etc... and the Display
        except common_exceptions:
            returnTuple = (1, ExceptionOutput(sys.exc_info()))
        self.UseTeX(False)
        return returnTuple

# -----------------------------------------------------------------------------------------------------------------

class MplCanvas_CONTROL_single_plot(Canvas):
    def __init__(self):
        #self.fig = Figure()
        self.fig = plt.figure(constrained_layout =True)
        self.fig.set_facecolor(AF.background_Colour)
        
        self.ax = self.fig.add_subplot(111)
        self.ax1 = self.ax.twinx()
        self.ax1.axis('off')
        
        Canvas.__init__(self, self.fig)
        Canvas.setSizePolicy(self, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        Canvas.updateGeometry(self)

class MplWidget_CONTROL_single_plot(MplWidget):
    def __init__(self, parent=None):
        super(MplWidget_CONTROL_single_plot, self).__init__(parent)
        self.Bode = False
        self.FuncLabel = ""
        self.Title = "Doubleclick on a control plot to display it here"

        self.Grid = QtWidgets.QGridLayout(self)
        self.Grid.setContentsMargins(0, 0, 0, 0)
        self.Grid.setSpacing(0)
        self.Grid.setObjectName("Grid")

        #self.ScrollWidgetC = QtWidgets.QWidget(self)
        #self.ScrollWidgetCGrid = QtWidgets.QGridLayout(self.ScrollWidgetC)
        #self.ScrollWidgetCGrid.setContentsMargins(0, 0, 0, 0)
        #self.ScrollWidgetCGrid.setSpacing(0)
        #self.ScrollWidgetCGrid.setObjectName("ScrollWidgetCGrid")
        self.ScrollWidget = QtWidgets.QScrollArea(self)#.ScrollWidgetC)
        self.ScrollWidget.setWidgetResizable(True)
        self.ScrollWidget.setObjectName("ScrollWidget")
        self.ScrollWidgetContents = QtWidgets.QWidget()
        #self.ScrollWidgetContents.setGeometry(QtCore.QRect(0, 0, 221, 264))
        self.ScrollWidgetContents.setObjectName("ScrollWidgetContents")
        self.ScrollGrid = QtWidgets.QGridLayout(self.ScrollWidgetContents)
        self.ScrollGrid.setContentsMargins(0, 0, 0, 0)
        self.ScrollGrid.setSpacing(0)
        self.ScrollGrid.setObjectName("ScrollGrid")

        self.canvas = MplCanvas_CONTROL_single_plot()
        self.x_from_input = QtWidgets.QDoubleSpinBox(self.ScrollWidgetContents)
        self.x_to_input = QtWidgets.QDoubleSpinBox(self.ScrollWidgetContents)
        self.x_checkbox = QtWidgets.QCheckBox(self.ScrollWidgetContents)
        self.y_from_input = QtWidgets.QDoubleSpinBox(self.ScrollWidgetContents)
        self.y_to_input = QtWidgets.QDoubleSpinBox(self.ScrollWidgetContents)
        self.y_checkbox = QtWidgets.QCheckBox(self.ScrollWidgetContents)
        self.apply_zoom_button = QtWidgets.QPushButton(self.ScrollWidgetContents)

        self.x_from_input.setDecimals(5)
        self.x_from_input.setMinimum(-1000000.0)
        self.x_from_input.setMaximum(1000000.0)
        self.x_from_input.setProperty("value", -10.0)
        self.x_to_input.setDecimals(5)
        self.x_to_input.setMinimum(-1000000.0)
        self.x_to_input.setMaximum(1000000.0)
        self.x_to_input.setProperty("value", 10.0)
        self.x_checkbox.setText("Limit x")
        self.y_from_input.setDecimals(5)
        self.y_from_input.setMinimum(-1000000.0)
        self.y_from_input.setMaximum(1000000.0)
        self.y_from_input.setProperty("value", 0.0)
        self.y_to_input.setDecimals(5)
        self.y_to_input.setMinimum(-1000000.0)
        self.y_to_input.setMaximum(1000000.0)
        self.y_to_input.setProperty("value", 5.0)
        self.y_checkbox.setText("Limit y")
        self.apply_zoom_button.setText("Apply Limits")
        
        self.ScrollWidget.setWidget(self.ScrollWidgetContents)

        self.ScrollGrid.addWidget(self.x_from_input,1,0)
        self.ScrollGrid.addWidget(self.x_to_input,1,1)
        self.ScrollGrid.addWidget(self.x_checkbox,1,2)
        self.ScrollGrid.addWidget(self.y_from_input,1,3)
        self.ScrollGrid.addWidget(self.y_to_input,1,4)
        self.ScrollGrid.addWidget(self.y_checkbox,1,5)
        self.ScrollGrid.addWidget(self.apply_zoom_button,1,6)

        #self.ScrollWidgetCGrid.addWidget(self.ScrollWidget,1,0)

        self.Grid.addWidget(self.canvas,0,0)
        self.Grid.addWidget(self.ScrollWidget,1,0)#C
        
        self.setLayout(self.Grid)

        # TODO: Reimplement these to let them fit the height to the contents automaticall
        self.ScrollWidgetContents.setMaximumHeight(50)
        self.ScrollWidget.setMaximumHeight(70)
        
        self.apply_zoom_button.clicked.connect(self.ApplyZoom)
        
    def ApplyZoom(self):
        try:
            xmin , xmax = self.x_from_input.value(), self.x_to_input.value()
            if xmax < xmin:
                xmax , xmin = xmin , xmax
            xlims = (xmin , xmax)
            ymin , ymax = self.y_from_input.value(), self.y_to_input.value()
            if ymax < ymin:
                ymax , ymin = ymin , ymax
            ylims = (ymin , ymax)
            
            self.canvas.ax.relim()
            self.canvas.ax1.relim()
            self.canvas.ax.autoscale()
            self.canvas.ax1.autoscale()
            if self.x_checkbox.isChecked():
                self.canvas.ax.set_xlim(xlims)
                self.canvas.ax1.set_xlim(xlims)
            if self.y_checkbox.isChecked():
                self.canvas.ax.set_ylim(ylims)
                self.canvas.ax1.set_ylim(ylims)
            
            try:
                self.canvas.draw()
            except RuntimeError: #This is only a failsave
                ExceptionOutput(sys.exc_info(),False)
                print("Trying to output without LaTeX")
                self.UseTeX(False)
                self.canvas.draw()
        except common_exceptions:
            Error = ExceptionOutput(sys.exc_info())
            self.window().NotifyUser(1,Error)
        
    def SetColour(self,BG=None,FG=None):
        returnTuple = (0,0)
        if BG != None and FG != None:
            super(MplWidget_CONTROL_single_plot, self).SetColour(BG,FG)
        try:
            self.canvas.ax.set_facecolor(self.background_Colour)
            self.canvas.ax.spines['bottom'].set_color(self.TextColour)
            self.canvas.ax.spines['left'].set_color(self.TextColour)
            if not self.Bode:
                self.canvas.ax.yaxis.label.set_color(self.TextColour)
            self.canvas.ax.xaxis.label.set_color(self.TextColour)
            self.canvas.ax.tick_params(axis='x', colors=self.TextColour)
            self.canvas.ax.tick_params(axis='y', colors=self.TextColour)
            self.canvas.ax.set_title(self.Title, color=self.TextColour)
            if self.Bode:
                self.canvas.ax1.set_facecolor(self.background_Colour)
                self.canvas.ax1.spines['bottom'].set_color(self.TextColour)
                self.canvas.ax1.spines['left'].set_color(self.TextColour)
                self.canvas.ax1.tick_params(axis='x', colors=self.TextColour)
                self.canvas.ax1.tick_params(axis='y', colors=self.TextColour)
            #if self.Bode:
                self.canvas.ax1.grid(c='orange',ls='--')
                self.canvas.ax.spines['right'].set_color(self.TextColour)
                self.canvas.ax1.spines['right'].set_color(self.TextColour)
                # TODO: Colour the Margins better
            if self.FuncLabel != "":
                self.canvas.ax.legend()#,color=self.TextColour)
        except common_exceptions:
            returnTuple = (2, ExceptionOutput(sys.exc_info()))
        try:
            self.canvas.draw()
        except common_exceptions:
            if returnTuple == (0,0):
                returnTuple = (1, ExceptionOutput(sys.exc_info()))
            else:
                returnTuple = (1, returnTuple[1]+ExceptionOutput(sys.exc_info()))
        return returnTuple
    
    def UseTeX(self,TheBool):
        # This Method changes the settings for not only one but all widgets...
        # This makes the clear function of the plotter slow if the LaTeX display has been used in LaTeX mode directly before
        # It could help to separate the two widgets into two files...
        # ... but it is also possible that this setting is global not only for the file but the program which would make the seperation a massive waste of time...
        # Maybe test this in a little testprogram to not waste that much time...
        
        #Both seem to do the same:
        matplotlib.rcParams['text.usetex'] = TheBool
        plt.rc('text', usetex=TheBool)
        return matplotlib.rcParams['text.usetex']

    def clear(self):
        self.Title = "Doubleclick on a control plot to display it here"
        try:
            self.canvas.ax.remove()
        except common_exceptions:
            pass
        try:
            self.canvas.ax1.remove()
        except common_exceptions:
            pass
        try:
            self.canvas.fig.clear()
        except common_exceptions:
            pass
        try:
            self.canvas.ax = self.canvas.fig.add_subplot(111)
            self.canvas.ax1 = self.canvas.ax.twinx()
            self.canvas.ax1.axis('off')
        except common_exceptions:
            pass
        self.Bode = False
        try: # CLEANUP: Clean up clear function
            self.canvas.ax.set_facecolor(self.background_Colour)
            self.canvas.ax.spines['bottom'].set_color(self.TextColour)
            self.canvas.ax.spines['left'].set_color(self.TextColour)
            #if not self.Bode:
            self.canvas.ax.yaxis.label.set_color(self.TextColour)
            self.canvas.ax.xaxis.label.set_color(self.TextColour)
            self.canvas.ax.tick_params(axis='both',which='both', colors=self.TextColour)
            #self.canvas.ax.tick_params(axis='y', colors=self.TextColour)
            self.canvas.ax.set_title(self.Title, color=self.TextColour)
            #if self.Bode:
            #    self.canvas.ax1.set_facecolor(self.background_Colour)
            #    self.canvas.ax1.spines['bottom'].set_color(self.TextColour)
            #    self.canvas.ax1.spines['left'].set_color(self.TextColour)
            #    self.canvas.ax1.tick_params(axis='both',which='both', colors=self.TextColour)
            #    #self.canvas.ax1.tick_params(axis='y', colors=self.TextColour)
            #if self.Bode:
            #    self.canvas.ax1.grid(c='orange',ls='--')
            #    self.canvas.ax.spines['right'].set_color(self.TextColour)
            #    self.canvas.ax1.spines['right'].set_color(self.TextColour)
        except common_exceptions:
            pass
        try:
            self.canvas.draw()
        except common_exceptions:
            pass

    def Plot(self,system,PlotName):
        """
        Retrun Value compatible with NotifyUser.
        """
        returnTuple = (0,"")
        self.FuncLabel = ""
        Titles = MplCanvas_CONTROL.Titles
        (sys1, T, X0 , U, Ufunc, Curr_Sys_LaTeX) = system # pylint: disable=unused-variable
        try:
            if T == None:
                syst = control.timeresp._get_ss_simo(sys1)
                T = scipy.signal.ltisys._default_response_times(syst.A, 5000)
        except common_exceptions:
            pass
        self.clear()

        # Plot the Plot
        try:
            if PlotName == Titles[0]:
                oT,y = control.step_response(sys1, number_of_samples=5000, T=T, X0 = X0)
                self.canvas.ax.plot(oT,y)
            elif PlotName == Titles[1]:
                oT,y = control.impulse_response(sys1, number_of_samples=5000, T=T, X0 = X0)
                self.canvas.ax.plot(oT,y)
            elif PlotName == Titles[2]:
                # If U not given try to create using Ufunc. If Ufunc not given or creation failed set U and Ufunc to 0
                if U == 0.0:
                    if Ufunc != "":
                        try:
                            Function = parse_expr(AF.AstusParse(Ufunc))
                            x = sympy.symbols('x')
                            evalfunc = sympy.lambdify(x, Function, modules=['numpy','sympy'])
                            U = evalfunc(T)
                            U = np.asarray(U)
                            if type(U) == int or type(U) == float or U.shape == (): #This also catches the case exp(x)
                                U = np.full_like(T, U)
                            if U.shape != T.shape:
                                raise Exception("Dimensions do not match")
                        except common_exceptions:
                            ExceptionOutput(sys.exc_info())
                            Ufunc = ""
                    if Ufunc == "":
                        Ufunc = "u(x)=0"
                
                self.FuncLabel = Ufunc
                oT,y,xout = control.forced_response(sys1, T=T, X0 = X0, U=U) # pylint: disable=unused-variable
                self.canvas.ax.plot(oT,y,label="Response")
                self.canvas.ax.plot(T,U,label="Input Function: "+Ufunc)
            elif PlotName == Titles[3] or PlotName == Titles[4] or PlotName == "  ":
                self.Bode = True
                self.canvas.ax1.axis('on')
                self.canvas.ax.set_label('control-bode-magnitude')
                self.canvas.ax1.set_label('control-bode-phase')
                plt.figure(self.canvas.fig.number)
                control.bode_plot(sys1, dB=True, omega_num=5000,Dense_Phase_Major_Ticks=True)#, margins=True) # TODO:Margins not pretty yet
            elif PlotName == Titles[5]:
                plt.sca(self.canvas.ax)
                control.nyquist_plot(sys1, number_of_samples=5000)
                self.FuncLabel = "Nyquist"
            elif PlotName == Titles[6]:
                plt.sca(self.canvas.ax)
                control.nichols_plot(sys1, number_of_samples=5000)
            elif PlotName == Titles[7]:
                poles,zeros = control.pzmap(sys1,Plot=False)
                if len(poles) > 0:
                    self.canvas.ax.scatter(np.real(poles), np.imag(poles), s=50, marker='x', c="red")
                if len(zeros) > 0:
                    self.canvas.ax.scatter(np.real(zeros), np.imag(zeros), s=25, marker='o', c="orange")
                self.canvas.ax.grid(True)
            elif PlotName == Titles[8]:
                control.root_locus_AMaDiA(sys1,self.canvas.ax)
                self.canvas.ax.grid(True)
            else: # LaTeX Display (Uses Title as display string)
                return (4,"This Plot is not implemented yet")
            


            # Get Plotname
            if PlotName == Titles[3] or PlotName == Titles[4] or PlotName == "  ":
                self.Title = Titles[3]
            else:
                self.Title = PlotName

            #Colour everything and draw it
            cReturnTuple = self.SetColour()
            if cReturnTuple != (0,0):
                if returnTuple == (0,0):
                    returnTuple = cReturnTuple
                else:
                    returnTuple = (1," "+returnTuple[1])
                    returnTuple = (1,cReturnTuple[1]+returnTuple[1])
        except common_exceptions:
            returnTuple = (1, ExceptionOutput(sys.exc_info()))
        self.UseTeX(False)
        return returnTuple


# -----------------------------------------------------------------------------------------------------------------

class ATextEdit(QtWidgets.QTextEdit): # TODO: Fix Undo/Redo
    returnPressed = QtCore.pyqtSignal()
    returnCtrlPressed = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtWidgets.QTextEdit.__init__(self, parent)
        self.Highlighter = LineEditHighlighter(self.document(), self)
        self.cursorPositionChanged.connect(self.CursorPositionChanged)
        self.textChanged.connect(self.validateCharacters)
        self.installEventFilter(self)
        self.setTabChangesFocus(True)
        
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter)
                and event.modifiers() == QtCore.Qt.ControlModifier):
            source.returnCtrlPressed.emit()
        if (event.type() == QtCore.QEvent.KeyPress # Connects to returnPressed
                and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter)):
            source.returnPressed.emit()
        return super(ATextEdit, self).eventFilter(source, event)

    #def contextMenuEvent(self, event): # Template in case the context menu needs to be modified
        ##super(ATextEdit, self).contextMenuEvent(event)
        #menu = self.createStandardContextMenu(event.pos())
        #menu.exec_(event.globalPos())

    def text(self):
        return self.toPlainText()

    def insertFromMimeData(self, MIMEData):
        try:
            Text = MIMEData.text()
            self.textCursor().insertText(Text)
        except common_exceptions:
            pass

    def CursorPositionChanged(self):
        cursor = self.textCursor()
        curPos = cursor.position()
        self.document().contentsChange.emit(curPos,0,0)
        #theformat = QtGui.QTextBlockFormat()
        #theformat.setForeground(QtGui.QColor('green'))
        #for i in range(0,self.document().blockCount()):
        #    cursor2 = QtGui.QTextCursor(self.document().findBlockByNumber(i))
        #    cursor2.setBlockFormat(theformat)
        #self.document().contentsChange.emit(curPos,0,0)

    def validateCharacters(self):
        #forbiddenChars = []
        cursor = self.textCursor()
        curPos = cursor.position()
        Text = self.toPlainText()
        found = 0
        #for e in forbiddenChars:
        #    found += Text.count(e)
        #    Text = Text.replace(e, '')

        # Windows doesn't like to type the combining dot above or double dot. This is a fix for the behavior that I observe on my PC
        found += Text.count("\u005C\u0307")
        Text = Text.replace("\u005C\u0307","\u0307")
        found += Text.count("\u00BF\u0308")
        Text = Text.replace("\u00BF\u0308","\u0308")
        
        self.blockSignals(True)
        self.setText(Text)
        self.blockSignals(False)
        try:
            cursor.setPosition(curPos-found)
            self.setTextCursor(cursor)
        except common_exceptions:
            ExceptionOutput(sys.exc_info())

class TextEdit(ATextEdit):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self.installEventFilter(self)

        # FEATURE: Make subscript and superscript work and add an option to disable it (fro small font)
        # See https://www.qtcentre.org/threads/38633-(SOLVED)-QTextEdit-subscripted-text for a startingpoint
        
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter)
                and event.modifiers() == QtCore.Qt.ControlModifier):
            source.returnCtrlPressed.emit()
            return True
        return super(TextEdit, self).eventFilter(source, event)

class LineEdit(ATextEdit):
    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)

        QTextEditFontMetrics =  QtGui.QFontMetrics(self.font())
        self.QTextEditRowHeight = QTextEditFontMetrics.lineSpacing()
        self.setFixedHeight(2 * self.QTextEditRowHeight)
        self.setLineWrapMode(QtWidgets.QTextEdit.NoWrap)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        self.installEventFilter(self)
        # Connect Signals
        self.textChanged.connect(self.validateCharacters)

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.FontChange): # Rescale if font size changes
            QTextEdFontMetrics =  QtGui.QFontMetrics(source.font())
            source.QTextEdRowHeight = QTextEdFontMetrics.lineSpacing()+9
            source.setFixedHeight(source.QTextEdRowHeight)
        if (event.type() == QtCore.QEvent.KeyPress # Move to beginning if up key pressed
                and event.key() == QtCore.Qt.Key_Up):
            cursor = source.textCursor()
            cursor.movePosition(cursor.Start)
            source.setTextCursor(cursor)
            return True
        if (event.type() == QtCore.QEvent.KeyPress # Move to end if down key pressed
                and event.key() == QtCore.Qt.Key_Down):
            cursor = source.textCursor()
            cursor.movePosition(cursor.End)
            source.setTextCursor(cursor)
            return True
        if (event.type() == QtCore.QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter)):
            source.returnPressed.emit()
            return True
        return super(LineEdit, self).eventFilter(source, event)

    def validateCharacters(self):
        forbiddenChars = ['\n']
        cursor = self.textCursor()
        curPos = cursor.position()
        Text = self.toPlainText()
        found = 0
        for e in forbiddenChars:
            found += Text.count(e)
            Text = Text.replace(e, '')
        
        self.blockSignals(True)
        self.setText(Text)
        self.blockSignals(False)
        try:
            cursor.setPosition(curPos-found)
            self.setTextCursor(cursor)
        except common_exceptions:
            ExceptionOutput(sys.exc_info())
        super(LineEdit, self).validateCharacters()


class LineEditHighlighter(QtGui.QSyntaxHighlighter): # TODO: Unhighlight, performance, Fix FindPair
    def __init__(self, document, Widget):
        QtGui.QSyntaxHighlighter.__init__(self, document)
        self.Widget = Widget
        self.init_Styles()
        self.enabled = True

        # init the rules # Currently Unused...
        rules = [(r'%s' % b, 0, self.STYLES['brace']) for b in self.braces]
        self.rules = [(QtCore.QRegExp(pat), index, fmt) for (pat, index, fmt) in rules]

    def init_Styles(self):
        # init Lists
        self.braces = ['\{', '\}', '\(', '\)', '\[', '\]'] # pylint: disable=anomalous-backslash-in-string

        # Init Formats
        self.RedFormat = QtGui.QTextCharFormat()
        self.RedFormat.setForeground(QtGui.QColor('red'))
        self.GreenFormat = QtGui.QTextCharFormat()
        self.GreenFormat.setForeground(QtGui.QColor('green'))
        self.BlueFormat = QtGui.QTextCharFormat()
        self.BlueFormat.setForeground(QtGui.QColor('blue'))
        self.CyanFormat = QtGui.QTextCharFormat()
        self.CyanFormat.setForeground(QtGui.QColor('cyan'))
        self.MagentaFormat = QtGui.QTextCharFormat()
        self.MagentaFormat.setForeground(QtGui.QColor('magenta'))

        # Collect all Formats in a dictionary
        self.STYLES = {'brace': self.RedFormat,'pair': self.RedFormat}

    def highlightBlock(self, text):
        # TODO: Unhighlight all other blocks
        if not self.enabled:
            self.setCurrentBlockState(0)
            return
        cursor = self.Widget.textCursor()
        curPos = cursor.positionInBlock()
        pattern = ""
        TheList = []
        for i in ART.LIST_l_normal_pairs:
            for j in i:
                if not j[0] in TheList:
                    TheList.append(j[0])
                if not j[1] in TheList:
                    TheList.append(j[1])
        TheList.sort(key=len,reverse=True)
        for i in TheList:
            pattern += re.escape(i)
            pattern += "|"
            pattern += re.escape(i)
            pattern += "|"
        pattern = pattern[:-1]
        braces_list = [[m.start(),m.end()] for m in re.finditer(pattern, text)]
        braces_list.sort(key=AF.takeFirst,reverse=False)
        for i in braces_list:
            if curPos <= i[1] and curPos >= i[0]:
                self.setFormat(i[0], i[1]-i[0], self.STYLES['pair'])
                Element = text[i[0]:i[1]]
                try:
                    Pair = AF.Counterpart(Element, ListOfLists=ART.LIST_l_normal_pairs, Both=True)
                except Exception:
                    ExceptionOutput(sys.exc_info())#break
                if Pair[0] == Element:
                    Pair = Pair.FirstResult
                    a,b = AF.FindPair(text,Pair,i[0])
                    self.setFormat(b, len(Pair[1]), self.STYLES['pair'])
                else:
                    # IMPROVE: Opening pair finder

                    #---------method1----------
                    # FIXME: Does not work!!!!!!!!!!!!!! NEEDS FIX OF AF.FindPair ???
                        #k=0
                        #found = False
                        #while k < len(Pair):
                        #    a,b = AF.FindPair(text,Pair.List[k],end=i[1])
                        #    if b == i[0] and Pair.List[k][1] == Element:
                        #        c,d = a, len(Pair.List[k][0])
                        #        found = True
                        #    k+=1
                    #if found:
                    #    self.setFormat(c, d, self.STYLES['pair'])


                    #---------method2----------
                    found = False
                    for j in braces_list:
                        Element2 = text[j[0]:j[1]]
                        try:
                            Pair2 = AF.Counterpart(Element2, ListOfLists=ART.LIST_l_normal_pairs, Both=True)
                        except Exception:
                            ExceptionOutput(sys.exc_info())#break
                        k=0
                        while k < len(Pair2):
                            a,b = AF.FindPair(text,Pair2.List[k],j[0])
                            if b == i[0] and Pair2.List[k][1] == Element:
                                c,d = a, len(Pair2.List[k][0])
                                found = True
                                break
                            k+=1
                    if found:
                        self.setFormat(c, d, self.STYLES['pair'])


                break
        
        self.setCurrentBlockState(0)


class TableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent)
        #print(type(self.itemDelegate()))
        self.TheDelegate = TableWidget_Delegate(self)
        self.setItemDelegate(self.TheDelegate)
        self.installEventFilter(self)
        
    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and source in self.window().findChildren(QtWidgets.QTableWidget) and source.isEnabled() and source.tabKeyNavigation()):
            index = source.currentIndex()
            if event.key() == QtCore.Qt.Key_Backtab:
                if index.row() == index.column() == 0:
                    source.setCurrentCell(0,0)
                    source.clearSelection()
                    QtWidgets.QAbstractScrollArea.focusNextPrevChild(source, False)
                    return True
            elif event.key() == QtCore.Qt.Key_Tab:
                model = source.model()
                if (index.row() == model.rowCount() - 1 and index.column() == model.columnCount() - 1):
                    source.setCurrentCell(0,0)
                    source.clearSelection()
                    QtWidgets.QAbstractScrollArea.focusNextPrevChild(source, True)
                    return True
        return super(TableWidget, self).eventFilter(source, event)

class TableWidget_Delegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, parent=None):
        super(TableWidget_Delegate, self).__init__(parent)
        self.installEventFilter(self)

    def createEditor(self, parent, options, index):
        return LineEdit(parent)

    def setEditorData(self, editor, index):
        editor.setText(index.data())

    def setModelData(self, editor, model, index):
        model.setData(index, editor.toPlainText())

    def eventFilter(self, source, event):
        if (event.type() == QtCore.QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Tab or event.key() == QtCore.Qt.Key_Backtab)):
            # Commit Editing, end Editing mode and re-send Tab/Backtab
            self.commitData.emit(source)
            self.closeEditor.emit(source, QtWidgets.QAbstractItemDelegate.NoHint)
            event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,event.key(),event.modifiers())
            self.parent().window().MainApp.sendEvent(self.parent(),event)
            return True
        elif (event.type() == QtCore.QEvent.KeyPress and (event.key() == QtCore.Qt.Key_Return or event.key() == QtCore.Qt.Key_Enter)):
            # Commit Editing and end Editing mode
            self.commitData.emit(source)
            self.closeEditor.emit(source, QtWidgets.QAbstractItemDelegate.NoHint)
            event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress,event.key(),event.modifiers())
            self.parent().window().MainApp.sendEvent(self.parent(),event)
            return True
        return super(TableWidget_Delegate, self).eventFilter(source, event)


class TopBar_Widget(QtWidgets.QWidget): # TODO: 3 in TopBar_Widget
    def __init__(self, parent=None, DoInit=False, IncludeMenu = False, IncludeFontSpinBox = False, IncludeErrorButton = False):
        super(TopBar_Widget, self).__init__(parent)
        self.moving = False
        self.offset = 0
        self.IncludeMenu, self.IncludeFontSpinBox, self.IncludeErrorButton = IncludeMenu, IncludeFontSpinBox, IncludeErrorButton
        if DoInit:
            self.init(IncludeMenu, IncludeFontSpinBox, IncludeErrorButton)

    def init(self, IncludeMenu = False, IncludeFontSpinBox = False, IncludeErrorButton = False):
        # TODO: Add a handle to resize the window
        # TODO: Add the font size spinbox here and handle it here
        # TODO: Add the ErrorButton here and handle it here
        self.IncludeMenu, self.IncludeFontSpinBox, self.IncludeErrorButton = IncludeMenu, IncludeFontSpinBox, IncludeErrorButton
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setObjectName("TopBar")
        if self.layout() == None:
            self.gridLayout = QtWidgets.QGridLayout(self)
            self.gridLayout.setContentsMargins(0, 0, 0, 0)
            self.gridLayout.setSpacing(0)
            self.gridLayout.setObjectName("gridLayout")
            self.setLayout(self.gridLayout)

        self.ButtonSizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.CloseButton = QtWidgets.QToolButton(self)
        self.CloseButton.setObjectName("CloseButton")
        self.layout().addWidget(self.CloseButton, 0, 104, 1, 1,QtCore.Qt.AlignRight)
        self.CloseButton.setText("🗙")

        self.RedHighlightPalette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(155, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.RedHighlightPalette.setBrush(QtGui.QPalette.All, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.RedHighlightPalette.setBrush(QtGui.QPalette.All, QtGui.QPalette.ButtonText, brush)
        self.CloseButton.installEventFilter(self)
        self.CloseButton.setAutoRaise(True)
        self.CloseButton.setSizePolicy(self.ButtonSizePolicy)

        self.MaximizeButton = QtWidgets.QToolButton(self)
        self.MaximizeButton.setObjectName("MaximizeButton")
        self.layout().addWidget(self.MaximizeButton, 0, 103, 1, 1,QtCore.Qt.AlignRight)
        self.MaximizeButton.setText("🗖")
        self.MaximizeButton.installEventFilter(self)
        self.MaximizeButton.setAutoRaise(True)
        self.MaximizeButton.setSizePolicy(self.ButtonSizePolicy)

        self.MinimizeButton = QtWidgets.QToolButton(self)
        self.MinimizeButton.setObjectName("MinimizeButton")
        self.layout().addWidget(self.MinimizeButton, 0, 102, 1, 1,QtCore.Qt.AlignRight)
        self.MinimizeButton.setText("🗕")
        self.MinimizeButton.installEventFilter(self)
        self.MinimizeButton.setAutoRaise(True)
        self.MinimizeButton.setSizePolicy(self.ButtonSizePolicy)

        self.MoveMe = QtWidgets.QLabel(self)
        self.MoveMe.setObjectName("MoveMe")
        self.layout().addWidget(self.MoveMe, 0, 101, 1, 1,QtCore.Qt.AlignRight)
        self.MoveMe.setText("  🖐  ")#▨
        self.MoveMe.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        self.CloseButton.clicked.connect(self.Exit)
        self.MaximizeButton.clicked.connect(self.ToggleMinMax)
        self.MinimizeButton.clicked.connect(self.Minimize)

        try:
            #self.window().menuBar().installEventFilter(self)
            if IncludeMenu:
                self.Menu = QtWidgets.QToolButton(self)
                self.Menu.setObjectName("Menu")
                self.layout().addWidget(self.Menu, 0, 100, 1, 1,QtCore.Qt.AlignRight)
                self.Menu.setText("\u2630")#☰ #("≡")
                self.Menu.setAutoRaise(True)
                self.Menu.setPopupMode(QtWidgets.QToolButton.InstantPopup)
                self.Menu.setMenu(self.window().Menu)
                self.Menu.setSizePolicy(self.ButtonSizePolicy)
        except common_exceptions:
            pass #ExceptionOutput(sys.exc_info())

        if IncludeFontSpinBox:
            self.Font_Size_spinBox = QtWidgets.QSpinBox(self)
            self.Font_Size_spinBox.setMinimum(5)
            self.Font_Size_spinBox.setMaximum(25)
            self.Font_Size_spinBox.setProperty("value", 9)
            self.Font_Size_spinBox.setObjectName("Font_Size_spinBox")
            self.layout().addWidget(self.Font_Size_spinBox, 0, 99, 1, 1,QtCore.Qt.AlignRight)
            self.Font_Size_spinBox.valueChanged.connect(self.ChangeFontSize)

        if IncludeErrorButton:
            self.Error_Label = QtWidgets.QPushButton(self)
            self.Error_Label.setObjectName("Error_Label")
            self.layout().addWidget(self.Error_Label, 0, 98, 1, 1,QtCore.Qt.AlignRight)
            self.Error_Label.installEventFilter(self)
            self.Error_Label.clicked.connect(QtWidgets.QApplication.instance().Show_Notification_Window)

    def Minimize(self):
        self.window().showMinimized()

    def ToggleMinMax(self):
        if not self.window().isFullScreen():
            if self.window().isMaximized():
                self.window().showNormal()
                self.MaximizeButton.setText("🗖")
            else:
                self.window().setGeometry(
                    Qt.QStyle.alignedRect(
                        QtCore.Qt.LeftToRight,
                        QtCore.Qt.AlignCenter,
                        self.window().size(),
                        QtWidgets.QApplication.instance().desktop().availableGeometry(self.window())))
                self.window().showMaximized()
                self.MaximizeButton.setText("🗗")
        else:
            try:
                if self.window().LastOpenState == self.window().showMaximized:
                    self.MaximizeButton.setText("🗗")
                else:
                    self.MaximizeButton.setText("🗖")
                self.window().LastOpenState()
            except AttributeError:
                self.MaximizeButton.setText("🗗")
                self.window().showMaximized()

    def Exit(self):
        self.window().close()

    def ChangeFontSize(self):
        try:
            QtWidgets.QApplication.instance().SetFont(PointSize = self.Font_Size_spinBox.value(), source=self.window())
        except common_exceptions:
            ExceptionOutput(sys.exc_info())
        

    def eventFilter(self, source, event):
        #if event.type() == 5: # QtCore.QEvent.MouseMove
        #    if self.moving: self.window().move(event.globalPos()-self.offset)
        #elif event.type() == 2: # QtCore.QEvent.MouseButtonPress
        #    if event.button() == QtCore.Qt.LeftButton:
        #        self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        #        self.MoveMe.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        #        self.MaximizeButton.setText("🗖")
        #        self.moving = True; self.offset = event.globalPos()-self.window().geometry().topLeft()
        #elif event.type() == 3: # QtCore.QEvent.MouseButtonRelease
        #    self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #    self.MoveMe.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        #    self.moving = False
        #    if event.button() == QtCore.Qt.LeftButton:
        #        pos = self.window().pos()
        #        #if (pos.x() < 0):
        #        #    pos.setX(0)
        #        #    self.window().move(pos)
        #        if (pos.y() < 0):
        #            pos.setY(0)
        #            self.window().move(pos)
        if event.type() == 10 or event.type() == 11:# QtCore.QEvent.Enter or QtCore.QEvent.Leave
            if source == self.CloseButton:
                if event.type() == QtCore.QEvent.Enter:#HoverMove
                    self.CloseButton.setPalette(self.RedHighlightPalette)
                elif event.type() == QtCore.QEvent.Leave:#HoverLeave
                    self.CloseButton.setPalette(self.palette())
            elif source == self.MaximizeButton:
                if event.type() == QtCore.QEvent.Enter:
                    self.MaximizeButton.setAutoRaise(False)
                elif event.type() == QtCore.QEvent.Leave:
                    self.MaximizeButton.setAutoRaise(True)
            elif source == self.MinimizeButton:
                if event.type() == QtCore.QEvent.Enter:
                    self.MinimizeButton.setAutoRaise(False)
                elif event.type() == QtCore.QEvent.Leave:
                    self.MinimizeButton.setAutoRaise(True)
        elif self.IncludeErrorButton and source is self.Error_Label and event.type() == QtCore.QEvent.Enter: #==10
            QtWidgets.QToolTip.showText(QtGui.QCursor.pos(),self.Error_Label.toolTip(),self.Error_Label)
        return super(TopBar_Widget, self).eventFilter(source, event)

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            self.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
            self.MoveMe.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
            self.MaximizeButton.setText("🗖")
            self.moving = True; self.offset = event.globalPos()-self.window().geometry().topLeft()

    def mouseReleaseEvent(self,event):
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MoveMe.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        if event.button() == QtCore.Qt.LeftButton:
            pos = self.window().pos()
            #if (pos.x() < 0):
            #    pos.setX(0)
            #    self.window().move(pos)
            if (pos.y() < 0):
                pos.setY(0)
                self.window().move(pos)

    def mouseMoveEvent(self,event):
        if self.moving: self.window().move(event.globalPos()-self.offset)

# -----------------------------------------------------------------------------------------------------------------



