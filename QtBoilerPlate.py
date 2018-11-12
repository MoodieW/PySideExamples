from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui


def maya_main_window():
    
    '''returns maya Ui refrence pointer to use as parent for QT dialog builds'''
    
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(long(main_window_ptr), QtWidgets.QWidget)
    
class testDialog(QtWidgets.QDialog):
    
    '''boiler plate code for QT UI'''
    
    def __init__(self, parent = maya_main_window()):
        
        '''
        The init function will run all of the of functions we have made at the creation time of the
        UI
        '''
        #call the parents class init function. the parent being QtWidgets.QDialog
        super(testDialog, self).__init__(parent)
        
        self.setWindowTitle("Test Dialog")
        self.setMinimumWidth(200)
        
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.create_widgets()
        self.create_layout()
        self.create_connection()
        
    def create_widgets(self):
        self.lineedit  = QtWidgets.QLineEdit()
        self.checkbox1 = QtWidgets.QCheckBox()
        self.checkbox2 = QtWidgets.QCheckBox()
        self.ok_btn   = QtWidgets.QPushButton('Ok')
        self.cancel_btn   = QtWidgets.QPushButton('Cancel')
        
    def create_layout(self):
        
        #Create FormLayout
        
        form_layout = QtWidgets.QFormLayout()
                           #label , widget
        form_layout.addRow("Name:", self.lineedit)
        form_layout.addRow("Hidden:", self.checkbox1)
        form_layout.addRow("Locked:", self.checkbox2)
        
        #Create HBoxLayout
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.ok_btn)
        button_layout.addWidget(self.cancel_btn)
        
        #Create Main Layout for widgets and child layout
        
        main_layout  = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)
    
    def create_connection(self):
        #signals and slot
        self.cancel_btn.clicked.connect(self.close)
        #self.lineedit.editingFinished.connect(self.print_hello_name)
        self.lineedit.textChanged.connect(self.print_hello_name)
                       #toggled sends a bool paramters 
        self.checkbox1.toggled.connect(self.print_hidden)
        
    def print_hello_name(self,name):
        #name = self.lineedit.text()
        print('hello {0}!'.format(name))
        
    def print_hidden(self, checked):
        #hidden = self.checkbox1.isChecked()
        if checked:
            print("Hidden")
        else:
            print("Visible")
        
if __name__ =="__main__":
    # UI deletion handling this is mainly for devol
    try:
        test_dialog.close()
        test_dialog.deleteLater()
        
    except:
        pass   
    test_dialog = testDialog()
    test_dialog.show()
    
    