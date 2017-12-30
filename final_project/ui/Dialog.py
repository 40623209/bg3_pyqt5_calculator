# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from .Ui_Dialog import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        '''以下為使用者自行編寫程式碼區'''
        
        #顯示幕起始
        self.display.setText('0')
        
        # clear 按鍵 slot 設定
        self.clearButton.clicked.connect(self.clear)
       
        digits = [self.one,  self.two,  self.three, \
            self.four,  self.five,  self.six, \
            self.seven,  self.eight,  self.nine,  self.zero]
            
        for i in digits:
            i.clicked.connect(self.digitClicked)
        #self.one.clicked.connect(self.digitClicked)
        
        multiply_divide = [self.timesButton,  self.divisionButton] 
        
        for i in multiply_divide:
            i.clicked.connect(self.multiplicativeOperatorClicked)
            
        plus_minus = [self.plusButton, self.minusButton]  
        
        for i in plus_minus:
            i.clicked.connect (self.additiveOperatorClicked)        
        
        self.equalButton.clicked.connect(self.equalClicked)
        
        self.pendingAdditiveOperator = ''
        
        self.sumSoFar = 0.0
        
        self.waitingForOperand = True
        
        self.pendingMultiplicativeOperator = ''
        
        self.factorSoFar = 0.0
 
        
    def digitClicked(self):
        clickedButton = self.sender()
        digitValue = int(clickedButton.text())
        
        # 處理顯示幕為 0 或輸入 0.0 時
        if self.display.text() == '0' and digitValue == 0.0:
            return
            
        # 切換是否等待輸入運算數狀態, 一開始等待運算數, 一有輸入值, 則刷新顯示幕
        if self.waitingForOperand:
            self.display.clear()
            self.waitingForOperand = False
            
        self.display.setText(self.display.text() + str(digitValue))
    
    def unaryOperatorClicked(self):
        '''單一運算元按下後處理方法'''
        pass
        
    def additiveOperatorClicked(self):
        '''加或減按下後進行的處理方法'''
      #  pass
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.sumSoFar))
        else:
            self.sumSoFar = operand

        self.pendingAdditiveOperator = clickedOperator
        self.waitingForOperand = True      
        
    def multiplicativeOperatorClicked(self):
        clickedButton = self.sender()
        clickedOperator = clickedButton.text()
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            self.display.setText(str(self.factorSoFar))
        else:
            self.factorSoFar = operand

        self.pendingMultiplicativeOperator = clickedOperator
        self.waitingForOperand = True       
        
    def equalClicked(self):
        '''等號按下後的處理方法'''
        #pass
        operand = float(self.display.text())

        if self.pendingMultiplicativeOperator:
            if not self.calculate(operand, self.pendingMultiplicativeOperator):
                self.abortOperation()
                return

            operand = self.factorSoFar
            self.factorSoFar = 0.0
            self.pendingMultiplicativeOperator = ''

        if self.pendingAdditiveOperator:
            if not self.calculate(operand, self.pendingAdditiveOperator):
                self.abortOperation()
                return

            self.pendingAdditiveOperator = ''
        else:
            self.sumSoFar = operand

        self.display.setText(str(self.sumSoFar))
        self.sumSoFar = 0.0
        self.waitingForOperand = True  
     
    
    def pointClicked(self):
        '''小數點按下後的處理方法'''
        pass
        
    def changeSignClicked(self):
        '''變號鍵按下後的處理方法'''
        pass
        
    def backspaceClicked(self):
        '''回復鍵按下的處理方法'''
        pass
        
    def clear(self):
        # 清除顯示幕, 回復到原始顯示 0
        self.display.setText('0')
        # 重置判斷是否等待輸入運算數狀態
        self.waitingForOperand = True

        
    def clearAll(self):
        '''全部清除鍵按下後的處理方法'''
        pass
        
    def clearMemory(self):
        '''清除記憶體鍵按下後的處理方法'''
        pass
        
    def readMemory(self):
        '''讀取記憶體鍵按下後的處理方法'''
        pass
        
    def setMemory(self):
        '''設定記憶體鍵按下後的處理方法'''
        pass
        
    def addToMemory(self):
        '''放到記憶體鍵按下後的處理方法'''
        pass
        
    def createButton(self):
        ''' 建立按鍵處理方法, 以 Qt Designer 建立對話框時, 不需要此方法'''
        pass
        
    def abortOperation(self):
        '''中斷運算'''
        pass
        
    def calculate(self, rightOperand, pendingOperator):
        '''計算'''
        #pass
        if pendingOperator == "+":
            self.sumSoFar += rightOperand
        if pendingOperator == "-":
            self.sumSoFar -= rightOperand
        if pendingOperator == "*":
            self.factorSoFar *= rightOperand
        if pendingOperator == "/":
            if rightOperand == 0.0:
                return False
 
            self.factorSoFar /= rightOperand
 
        return True
