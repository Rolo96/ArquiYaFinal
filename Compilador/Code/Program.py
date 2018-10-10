from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QErrorMessage, QGraphicsScene, QMainWindow
from PyQt5.QtGui import QFont, QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image


Filename = None
Size = None

class Ui_Compiler(QtWidgets.QMainWindow):
    def setupUi(self, Compiler):
        Compiler.setObjectName("Compiler")
        Compiler.resize(800, 700)
        Compiler.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(Compiler)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(0, 29, 800, 671))
        self.textEdit.setMaximumSize(QtCore.QSize(800, 700))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("color: rgb(85, 170, 127);")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 41, 28))
        self.pushButton.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/new.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 0, 31, 28))
        self.pushButton_2.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 0, 31, 28))
        self.pushButton_3.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(100, 0, 31, 28))
        self.pushButton_4.setStyleSheet("background-color: rgb(189, 189, 189);")
        self.pushButton_4.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../Images/compile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setObjectName("pushButton_4")
        Compiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Compiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuNew = QtWidgets.QMenu(self.menubar)
        self.menuNew.setObjectName("menuNew")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        Compiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Compiler)
        self.statusbar.setObjectName("statusbar")
        Compiler.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(Compiler)
        self.actionNew.setEnabled(True)
        self.actionNew.setIcon(icon)
        self.actionNew.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionNew.setVisible(True)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(Compiler)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(Compiler)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(Compiler)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../Images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon4)
        self.actionExit.setObjectName("actionExit")
        self.actionCopy = QtWidgets.QAction(Compiler)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../Images/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon5)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(Compiler)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../Images/Cut-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon6)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(Compiler)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../Images/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon7)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(Compiler)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../Images/Undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon8)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(Compiler)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../Images/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon9)
        self.actionRedo.setObjectName("actionRedo")
        self.actionBold = QtWidgets.QAction(Compiler)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../Images/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon10)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(Compiler)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../Images/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon11)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUndeline = QtWidgets.QAction(Compiler)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../Images/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndeline.setIcon(icon12)
        self.actionUndeline.setObjectName("actionUndeline")
        self.actionCenter = QtWidgets.QAction(Compiler)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../Images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter.setIcon(icon13)
        self.actionCenter.setObjectName("actionCenter")
        self.actionCenter_2 = QtWidgets.QAction(Compiler)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../Images/center.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCenter_2.setIcon(icon14)
        self.actionCenter_2.setObjectName("actionCenter_2")
        self.actionRight = QtWidgets.QAction(Compiler)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../Images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRight.setIcon(icon15)
        self.actionRight.setObjectName("actionRight")
        self.actionJustify = QtWidgets.QAction(Compiler)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../Images/justify.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionJustify.setIcon(icon16)
        self.actionJustify.setObjectName("actionJustify")
        self.actionAbout = QtWidgets.QAction(Compiler)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../Images/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon17)
        self.actionAbout.setObjectName("actionAbout")
        self.actionCompile = QtWidgets.QAction(Compiler)
        self.actionCompile.setIcon(icon3)
        self.actionCompile.setObjectName("actionCompile")
        self.menuNew.addAction(self.actionNew)
        self.menuNew.addAction(self.actionOpen)
        self.menuNew.addAction(self.actionSave)
        self.menuNew.addAction(self.actionCompile)
        self.menuNew.addSeparator()
        self.menuNew.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuNew.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(Compiler)
        QtCore.QMetaObject.connectSlotsByName(Compiler)

        self.actionNew.triggered.connect(self.fileNew)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionExit.triggered.connect(self.close)
        self.actionCompile.triggered.connect(self.fileCompile)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionCut.triggered.connect(self.cut)
        self.actionUndo.triggered.connect(self.textEdit.undo)
        self.actionRedo.triggered.connect(self.textEdit.redo)
        self.actionBold.triggered.connect(self.textBold)
        self.actionAbout.triggered.connect(self.about)
        self.pushButton.clicked.connect(self.fileNew)
        self.pushButton_2.clicked.connect(self.openFile)
        self.pushButton_3.clicked.connect(self.fileSave)
        self.pushButton_4.clicked.connect(self.fileCompile)

    def retranslateUi(self, Compiler):
        _translate = QtCore.QCoreApplication.translate
        Compiler.setWindowTitle(_translate("Compiler", "Compiler"))
        self.menuNew.setTitle(_translate("Compiler", "File"))
        self.menuEdit.setTitle(_translate("Compiler", "Edit"))
        self.menuHelp.setTitle(_translate("Compiler", "Help"))
        self.actionNew.setText(_translate("Compiler", "New"))
        self.actionNew.setShortcut(_translate("Compiler", "Ctrl+N"))
        self.actionOpen.setText(_translate("Compiler", "Open"))
        self.actionOpen.setShortcut(_translate("Compiler", "Ctrl+O"))
        self.actionSave.setText(_translate("Compiler", "Save"))
        self.actionSave.setShortcut(_translate("Compiler", "Ctrl+S"))
        self.actionExit.setText(_translate("Compiler", "Exit"))
        self.actionExit.setShortcut(_translate("Compiler", "Esc"))
        self.actionCopy.setText(_translate("Compiler", "Copy"))
        self.actionCopy.setShortcut(_translate("Compiler", "Ctrl+C"))
        self.actionCut.setText(_translate("Compiler", "Cut"))
        self.actionCut.setShortcut(_translate("Compiler", "Ctrl+X"))
        self.actionPaste.setText(_translate("Compiler", "Paste"))
        self.actionPaste.setShortcut(_translate("Compiler", "Ctrl+P"))
        self.actionUndo.setText(_translate("Compiler", "Undo"))
        self.actionUndo.setShortcut(_translate("Compiler", "Ctrl+Z"))
        self.actionRedo.setText(_translate("Compiler", "Redo"))
        self.actionRedo.setShortcut(_translate("Compiler", "Ctrl+Y"))
        self.actionBold.setText(_translate("Compiler", "Bold"))
        self.actionBold.setShortcut(_translate("Compiler", "Ctrl+B"))
        self.actionItalic.setText(_translate("Compiler", "Italic"))
        self.actionItalic.setShortcut(_translate("Compiler", "Ctrl+I"))
        self.actionUndeline.setText(_translate("Compiler", "Undeline"))
        self.actionUndeline.setShortcut(_translate("Compiler", "Ctrl+U"))
        self.actionCenter.setText(_translate("Compiler", "Left"))
        self.actionCenter.setShortcut(_translate("Compiler", "Ctrl+Shift+L"))
        self.actionCenter_2.setText(_translate("Compiler", "Center"))
        self.actionCenter_2.setShortcut(_translate("Compiler", "Ctrl+Shift+C"))
        self.actionRight.setText(_translate("Compiler", "Right"))
        self.actionRight.setShortcut(_translate("Compiler", "Ctrl+Shift+R"))
        self.actionJustify.setText(_translate("Compiler", "Justify"))
        self.actionJustify.setShortcut(_translate("Compiler", "Ctrl+Shift+J"))
        self.actionAbout.setText(_translate("Compiler", "About"))
        self.actionAbout.setShortcut(_translate("Compiler", "F1"))
        self.actionCompile.setText(_translate("Compiler", "Compile"))
        self.actionCompile.setShortcut(_translate("Compiler", "F5"))

    def fileNew(self):
        self.textEdit.clear()

    def openFile(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')
        if filename[0]:
            f = open(filename[0],'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def fileSave(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')[0]
        if filename:
            filename += '.rs'
            f = open(filename,'w')
            with f:
                text = self.textEdit.toPlainText()
                f.write(text)
                QMessageBox.about(self, "Save File", "File Saved Successfully")


    def fileCompile(self):
        data = self.binaryConvert()
        if data!= '' and data[0]!='E':
            filename = QFileDialog.getSaveFileName(self, 'Save File')[0]
            if filename:
                filename += '.rs'
                f = open(filename,'w')
                with f:
                    f.write(data)
                    QMessageBox.about(self, "Compile File", "File Compiled Successfully")
        else:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage(data)
            

    def exitApp(self):
        self.close()

    def copy(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected

    def paste(self):
        self.textEdit.append(self.copiedText)

    def cut(self):
        cursor = self.textEdit.textCursor()
        textSelected = cursor.selectedText()
        self.copiedText = textSelected
        self.textEdit.cut()

    def textBold(self):
        font = QFont()
        font.setBold(True)
        self.textEdit.setFont(font)

    def about(self):
        QMessageBox.about(self, "Compiler", "2RB Compiler V1.0")

    def binaryConvert(self):

        global Size
        Size = 0
        instuctionCodes = {'ADDEQ':'00000000001','ADDNE':'00010000001','ADDLT':'10110000001','ADDGT':'11000000001',
                           'ADDLE':'11010000001','ADDGE':'10100000001','ADDAL':'11100000001','ADD':'11100000001',
                           
                           'SUBEQ':'00000000011','SUBNE':'00010000011','SUBLT':'10110000011','SUBGT':'11000000011',
                           'SUBLE':'11010000011','SUBGE':'10100000011','SUBAL':'11100000011','SUB':'11100000011',
                           
                           'MULEQ':'00000000101','MULNE':'00010000101','MULLT':'10110000101','MULGT':'11000000101',
                           'MULLE':'11010000101','MULGE':'10100000101','MULAL':'11100000101','MUL':'11100000101',
                           
                           'MOVEQ':'00000000111','MOVNE':'00010000111','MOVLT':'10110000111','MOVGT':'11000000111',
                           'MOVLE':'11010000111','MOVGE':'10100000111','MOVAL':'11100000111','MOV':'11100000111',
                           
                           'CMPEQ':'00000001001','CMPNE':'00010001001','CMPLT':'10110001001','CMPGT':'11000001001',
                           'CMPLE':'11010001001','CMPGE':'10100001001','CMPAL':'11100001001','CMP':'11100001001',
                           
                           'BEQ':'00001010','BNE':'00011010','BLT':'10111010','BGT':'11001010','BLE':'11011010',
                           'BGE':'10101010','BAL':'11101010','B':'11101010',
                           
                           'LDREQ':'00000100001','LDRNE':'00010100001','LDRLT':'10110100001','LDRGT':'11000100001',
                           'LDRLE':'11010100001','LDRGE':'10100100001','LDRAL':'11100100001','LDR':'11100100001',
                           
                           'STREQ':'00000100000','STRNE':'00010100000','STRLT':'10110100000','STRGT':'11000100000',
                           'STRLE':'11010100000','STRGE':'10100100000','STRAL':'11100100000','STR':'11100100000',

                           'ANDEQ':'00000010001','ANDNE':'00010010001','ANDLT':'10110010001','ANDGT':'11000010001',
                           'ANDLE':'11010010001','ANDGE':'10100010001','ANDAL':'11100010001','AND':'11100010001',
                           
                           'OREQ':'00000010011','ORNE':'00010010011','ORLT':'10110010011','ORGT':'11000010011',
                           'ORLE':'11010010011','ORGE':'10100010011','ORAL':'11100010011','OR':'11100010011',
                           
                           'PRDEQ':'000000110101','PRDNE':'000100110101','PRDLT':'101100110101','PRDGT':'110000110101',
                           'PRDLE':'110100110101','PRDGE':'101000110101','PRDAL':'111000110101','PRD':'111000110101',
                           
                           'STPEQ':'000000110111','STPNE':'000100110111','STPLT':'101100110111','STPGT':'110000110111',
                           'STPLE':'110100110111','STPGE':'101000110111','STPAL':'111000110111','STP':'111000110111',

                           'IBDEQ':'000000111001','IBDNE':'000100111001','IBDLT':'101100111001','IBDGT':'110000111001',
                           'IBDLE':'110100111001','IBDGE':'101000111001','IBDAL':'111000111001','IBD':'111000111001',

                           'ADR': '111111'}

        registers = {'R0':'0000','R1':'0001','R2':'0010','R3':'0011','R4':'0100','R5':'0101','R6':'0110','R7':'0111',
                    'R8':'1000','R9':'1001','R10':'1010','R11':'1011','R12':'1100','R13':'1101','R14':'1110','R15':'1111'}


        instructionsText = self.textEdit.toPlainText()
        instructions = instructionsText.split("\n")#Lista con lineas del editor de texto
        contador = 1
        instructionNumber = 1
        totalBinary = ''
        etiquetas = {}  
        variables = {}
        instNumber = 0
        for inst in instructions:
            if inst[len(inst)-1]==':':#Etiqueta
                etiquetas[inst[:len(inst)-1]] = instNumber + 1
            else:
                instNumber += 1

        for inst in instructions:
            if inst[:5]=='FILL ':#Fill
                parts = inst.split(" ")
                if len(parts)==3: #Fill
                    try:
                        variables[parts[1]] = Size
                        Size += int(parts[2])
                    except:
                        error = 'Error invalid instruction: ' + inst 
                        return error
        
        if (len(instructions)!=1 or instructions[0] != ""):#Len minimo es 1
            for instruction in instructions: #itera las instrucciones
                binary = ''
                parts = instruction.split(" ") #Se obtienen los operandos e instruccion
                if (parts[0][len(parts[0])-1]==':' and len(parts)==1) or (parts[0]=='FILL' and len(parts)==3): #Etiqueta
                    instructionNumber -= 1
                elif parts[0] in instuctionCodes.keys():
                    opCode = instuctionCodes[parts[0]]
                    binary += opCode
                    
#---------------------------------------------Aritmeticas(ADD,SUB,MUL,AND,OR)------------------------------------
                    if (parts[0][0]!='C' and (parts[0][:2]!='ST') and parts[0][0]!='L' and parts[0][0]!='I'
                        and parts[0][0]!='P' and parts[0][0]!='B' and parts[0][1]!='O' and len(parts) == 4):
                        
                        #----------------Operando1---------------------
                        if parts[2] in registers.keys():#Operando1 es registro
                            operand1 = registers[parts[2]]
                            binary += operand1
                        else:#error de operando
                            error = 'Error in line: ' + str(contador) + ': invalid instruction operand 1: ' + parts[2]
                            return error

                        #------------------------Destino----------------
                        if parts[1] in registers.keys():#Destino es registro
                            dest = registers[parts[1]]
                            binary += dest
                        else:#error de destino
                            error = 'Error in line: ' + str(contador) + ': invalid instruction destination: ' + parts[1]
                            return error             

                        
                        #--------------------Operando2-------------------
                        if parts[3] in registers.keys():#Operando2 es registro
                            operand2 = registers[parts[3]]
                            binary = binary[:6] + '0' + binary[6:] #Agrega 0 en la posicion de I
                            binary += '00000000' + operand2
                        else:
                            try:
                                if parts[3][0]=='#':#Operando2 puede ser inmediato
                                    try:#Operando2 inmediato
                                        operand2 = int(parts[3][1:])
                                        operand2Binary = format(operand2, "08b")
                                        binary = binary[:6] + '1' + binary[6:] #Agrega 1 en la posicion de I
                                        binary += '0000' + operand2Binary
                                        
                                    except:#Error de operando2
                                        error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                        return error 
                                else:
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                    return error 
                            except:#Error de operando2
                                error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                return error 
         
#----------------------------------------------------------MOV---------------------------------------------------------------
                    elif len(parts)==3 and parts[0][1]=='O': #MOV
                        binary += '0000'
                        #-----------------------------Destino------------------------------
                        if parts[1] in registers.keys():#Destino es registro
                            dest = registers[parts[1]]
                            binary += dest
                        else:#error de destino
                            error = 'Error in line: ' + str(contador) + ': invalid instruction destination: ' + parts[1]
                            return error 
                        #-----------------------------Operando------------------------------
                        if parts[2] in registers.keys():#Operando es registro
                            operand = registers[parts[2]]
                            binary = binary[:6] + '0' + binary[6:] #Agrega 0 en la posicion de I
                            binary += '00000000' + operand
                        else:
                            try:
                                if parts[2][0]=='#':#Operando puede ser inmediato
                                    try:#Operando inmediato
                                        operand = int(parts[2][1:])
                                        operandBinary = format(operand, "08b")
                                        binary = binary[:6] + '1' + binary[6:] #Agrega 1 en la posicion de I
                                        binary += '0000' + operandBinary
                                    except:#Error de operando
                                        error = 'Error in line: ' + str(contador) + ': invalid instruction operand: ' + parts[2]
                                        return error 
                                else:
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction operand: ' + parts[2]
                                    return error 
                            except:#Error de operando
                                error = 'Error in line: ' + str(contador) + ': invalid instruction operand: ' + parts[2]
                                return error 

#----------------------------------------------------------CMP---------------------------------------------------------------
                    elif parts[0][0]=='C' and len(parts)==3: #CMP
                        #-----------------------------Operando1------------------------------
                        if parts[1] in registers.keys():#Destino es registro
                            operand = registers[parts[1]]
                            binary += operand + '0000'
                        else:#error de destino
                            error = 'Error in line: ' + str(contador) + ': invalid instruction operand 1: ' + parts[1]
                            return error 
                        #-----------------------------Operando------------------------------
                        if parts[2] in registers.keys():#Operando es registro
                            operand2 = registers[parts[2]]
                            binary = binary[:6] + '0' + binary[6:] #Agrega 0 en la posicion de I
                            binary += '00000000' + operand2
                        else:
                            try:
                                if parts[2][0]=='#':#Operando puede ser inmediato
                                    try:#Operando inmediato
                                        operand2 = int(parts[2][1:])
                                        operand2Binary = format(operand2, "08b")
                                        binary = binary[:6] + '1' + binary[6:] #Agrega 1 en la posicion de I
                                        binary += '0000' + operand2Binary
                                    except:#Error de operando
                                        error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[2]
                                        return error 
                                else:
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[2]
                                    return error 
                            except:#Error de operando
                                error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[2]
                                return error 

#----------------------------------------------------------LDR y STR-----------------------------------------
                    elif (len(parts)==3 or len(parts)==4) and (parts[0][0]=='L' or parts[0][:3]=='STR') : #LDR y STR
                        binary = binary[:6] + '1' + binary[6:] #Agrega 1 en la posicion de I SOLO SOPORTA INMM
                        #-----------------------------Destino------------------------------
                        dest = 'a'
                        if parts[1] in registers.keys():#Destino es registro
                            dest = registers[parts[1]]
                        else:#error de destino
                            error = 'Error in line: ' + str(contador) + ': invalid instruction destination: ' + parts[1]
                            return error 

                        #------------------Cuando es solo con registro-----------------------------
                        if len(parts) == 3:

                            #------------------------Operando--------------------------
                            if parts[2][0] == '[' and parts[2][len(parts[2])-1] == ']':
                                partsDescription = parts[2][1:len(parts[2])-1]
                                if partsDescription in registers.keys():#operand es registro
                                    operand = registers[partsDescription]
                                    binary += operand + dest + '000000000000'
                                else:#error de destino
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction baseadress: ' + parts[2]
                                    return error 
                            else:#operando sin []
                                error = 'Error in line: ' + str(contador) + ': invalid instruction baseadress(Needs []): ' + parts[2]
                                return error 
                        #------------------Cuando es con registro e inmediato-----------------------------
                        elif len(parts) == 4:
                            #------------------------Operando1--------------------------
                            if parts[2][0] == '[':
                                partsDescription = parts[2][1:]
                                if partsDescription in registers.keys():#operand es registro
                                    operand = registers[partsDescription]
                                    binary += operand + dest
                                else:#error de destino
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction baseadress: ' + parts[2]
                                    return error 
                            else:#operando sin [
                                error = 'Error in line: ' + str(contador) + ': invalid instruction baseadress (Needs [ ): ' + parts[2]
                                return error 
                            #------------------------Operando2--------------------------
                            if parts[3][len(parts[3])-1] == ']':
                                partsDescription = parts[3][:len(parts[3])-1]
                                try:
                                    if parts[3][0]=='#':#Operando2 inmediato
                                        try:#Operando2 inmediato
                                            operand2 = int(parts[3][1:len(parts[3])-1])
                                            operand2Binary = format(operand2, "012b")
                                            binary += operand2Binary                                  
                                        except:#Error de operando2
                                            error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                            return error 
                                    else:
                                        error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                        return error 
                                except:#Error de operando2
                                    error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2: ' + parts[3]
                                    return error 
                            else:
                                error = 'Error in line: ' + str(contador) + ': invalid instruction operand 2 (Needs ] ): ' + parts[3]
                                return error 

#----------------------------------------------------------Branch---------------------------------------------------------------
                    elif parts[0][0]=='B' and len(parts) == 2: #Branch
                        if parts[1] in etiquetas.keys():
                            instNumber = etiquetas[parts[1]]
                            branch = instNumber - instructionNumber
                            branchBinary = format(branch & 0xffffffff, '24b')
                            branchBinaryCorrected = ''
                            for bit in branchBinary:
                                if bit == ' ':
                                    branchBinaryCorrected += '0'
                                else:
                                    branchBinaryCorrected += bit
                            if len(branchBinaryCorrected) == 32:
                                branchBinaryCorrected = branchBinaryCorrected[8:]
                            binary += branchBinaryCorrected
                        else:
                            error = 'Error in line: ' + str(contador) + ': invalid instruction label): ' + parts[1]
                            return error

#---------------------------------------------PRM,STP,IBD------------------------------------
                    elif (parts[0][0]=='P' or parts[0][0]=='I' or parts[0][:3]=='STP') and len(parts) == 3:
                        
                        #----------------Operando1---------------------
                        if parts[2] in registers.keys():#Operando1 es registro
                            operand1 = registers[parts[2]]
                            binary += operand1
                        else:#error de operando
                            error = 'Error in line: ' + str(contador) + ': invalid instruction operand 1: ' + parts[2]
                            return error

                        #------------------------Destino----------------
                        if parts[1] in registers.keys():#Destino es registro
                            dest = registers[parts[1]]
                            binary += dest + '000000000000'
                        else:#error de destino
                            error = 'Error in line: ' + str(contador) + ': invalid instruction destination: ' + parts[1]
                            return error

#---------------------------------------------ADR------------------------------------
                    elif parts[0][0]=='A' and len(parts) == 3:
                        
                        #----------------Destino---------------------
                        if parts[1] in registers.keys():#Destino es registro
                            dest = registers[parts[1]]
                            binary += dest
                        else:#error de operando
                            error = 'Error in line: ' + str(contador) + ': invalid instruction destination: ' + parts[2]
                            return error

                        #------------------------Inmm----------------
                        if parts[2] in variables.keys():#Existe la variable
                            operand = format(variables[parts[2]], "022b")
                            binary += operand
                        else:#error de operando
                            error = 'Error in line: ' + str(contador) + ': invalid instruction operand: ' + parts[2]
                            return error
#---------------------------------------------Unrecognize instruction------------------------------------                        
                    else:
                        error = 'Error in line: ' + str(contador) + ': Unrecognize instruction parts'
                        return error 
                    if (totalBinary == ''):
                        totalBinary += binary
                    else:
                        totalBinary += '\n'
                        totalBinary += binary
#----------------------------------------------------------------------------------------------------------------------------
                else:#Error de nombre de instruccion
                    error = 'Error in line: ' + str(contador) + ': invalid instruction name: ' + parts[0] 
                    return error
                contador+=1
                instructionNumber += 1
        print(variables)
        return totalBinary


class Ui_imageLoad(QMainWindow):
    def setupUi(self, imageLoad):
        imageLoad.setObjectName("imageLoad")
        imageLoad.resize(800, 700)
        imageLoad.setMaximumSize(QtCore.QSize(800, 700))
        self.centralwidget = QtWidgets.QWidget(imageLoad)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(200, 130, 400, 300))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 530, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        imageLoad.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(imageLoad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        imageLoad.setMenuBar(self.menubar)
        self.actionOpenI = QtWidgets.QAction(imageLoad)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Images/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenI.setIcon(icon)
        self.actionOpenI.setObjectName("actionOpenI")
        self.action_2 = QtWidgets.QAction(imageLoad)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Images/compile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_2.setIcon(icon1)
        self.action_2.setObjectName("action_2")
        self.actionExitI = QtWidgets.QAction(imageLoad)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../Images/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExitI.setIcon(icon2)
        self.actionExitI.setObjectName("actionExitI")
        self.menuFile.addAction(self.actionOpenI)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExitI)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(imageLoad)
        QtCore.QMetaObject.connectSlotsByName(imageLoad)
        self.pushButton.setEnabled(False)

        self.actionOpenI.triggered.connect(self.openFile)
        self.actionExitI.triggered.connect(self.exitApp)
        self.pushButton.clicked.connect(self.compileImage)

    def retranslateUi(self, imageLoad):
        _translate = QtCore.QCoreApplication.translate
        imageLoad.setWindowTitle(_translate("imageLoad", "imageLoad"))
        self.pushButton.setText(_translate("imageLoad", "Compile"))
        self.menuFile.setTitle(_translate("imageLoad", "File"))
        self.actionOpenI.setText(_translate("imageLoad", "Open"))
        self.actionOpenI.setShortcut(_translate("imageLoad", "Ctrl+O"))
        self.action_2.setText(_translate("imageLoad", "Compile"))
        self.action_2.setShortcut(_translate("imageLoad", "F5"))
        self.actionExitI.setText(_translate("imageLoad", "Exit"))
        self.actionExitI.setShortcut(_translate("imageLoad", "Esc"))

    def openFile(self):
        global Filename, Size
        Filename = QFileDialog.getOpenFileName(self, 'Open File', '/home')[0]
        pixelMap = QtGui.QPixmap(Filename)
        height = pixelMap.height()
        width = pixelMap.width()
        Size = height * width

        if Size <= 310000:
            self.scene = QGraphicsScene()
            self.scene.addPixmap(pixelMap)
            self.graphicsView.setScene(self.scene)
            self.pushButton.setEnabled(True)
            QMessageBox.about(self, "Image Size", ("The image size is: Height: " +str(height)+ ", Width: "+str(width)+", Total Size: "+str(Size)))

        else:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage("Error: Size is too big")

    def exitApp(self):
        program.close()

    def compileImage(self):
        global Filename
        image = Image.open(Filename, 'r')
        pixels = list(image.getdata())
	
        mif_name = 'Image.mif'

        mif_file = open(mif_name, 'w+')

        mif_file.write('DEPTH={};\nWIDTH={};\nADDRESS_RADIX=DEC;\nDATA_RADIX=BIN;\nCONTENT\nBEGIN\n\n'.format(len(pixels), 32))
    
        address = 0
        for i in range(image.size[1]):
            for j in range(image.size[0]):
                r = format(pixels[address][0], '08b')
                g = format(pixels[address][1], '08b')
                b = format(pixels[address][2], '08b')
                mif_file.write(str(i * image.size[0] + j) + ":      ")
                address+=1
                mif_file.write(' '+'00000000'+r+g+b)
                mif_file.write(';\n')
        mif_file.write("END;")
        mif_file.close()

        image.close()   
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Compiler()
        self.ui.setupUi(self.window)
        program.close()
        self.window.show()
        QMessageBox.about(self, "Compile File", "File Compiled Successfully")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    program = QtWidgets.QMainWindow()
    ui = Ui_imageLoad()
    ui.setupUi(program)
    program.show()
    sys.exit(app.exec_())

