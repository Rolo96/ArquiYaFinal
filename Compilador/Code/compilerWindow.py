from compiler import Ui_Compiler
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QErrorMessage
from PyQt5.QtGui import QFont

class EditorWindow(QtWidgets.QMainWindow, Ui_Compiler):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

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
        
        self.show()

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
        if data[0]!='E':
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
                           'IBDLE':'110100111001','IBDGE':'101000111001','IBDAL':'111000111001','IBD':'111000111001'}

        registers = {'R0':'0000','R1':'0001','R2':'0010','R3':'0011','R4':'0100','R5':'0101','R6':'0110','R7':'0111',
                    'R8':'1000','R9':'1001','R10':'1010','R11':'1011','R12':'1100','R13':'1101','R14':'1110','R15':'1111'}


        instructionsText = self.textEdit.toPlainText()
        instructions = instructionsText.split("\n")#Lista con lineas del editor de texto
        contador = 1
        instructionNumber = 1
        totalBinary = ''
        etiquetas = {}  
        instNumber = 0
        for inst in instructions:
            if inst[len(inst)-1]==':':#Etiqueta
                etiquetas[inst[:len(inst)-1]] = instNumber + 1
            else:
                instNumber += 1
        if (len(instructions)!=1 or instructions[0] != ""):#Len minimo es 1
            for instruction in instructions: #itera las instrucciones
                binary = ''
                parts = instruction.split(" ") #Se obtienen los operandos e instruccion
                if parts[0][len(parts[0])-1]==':' and len(parts)==1: #Etiqueta
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
        #print(totalBinary)
        return totalBinary
