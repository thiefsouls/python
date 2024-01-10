from PyQt5 import uic,QtWidgets
import mysql.connector
import win32com.client as win32

#Conecta no banco da Dados
conector = mysql.connector.connect(
    host='167.99.252.245',
    user='BES_E14', 
    passwd='E2W123', 
    database="BES_E14")
cursor = conector.cursor(buffered=True)

categoria = ""

#Declaração Funçao Principal para Formulario
def funcao_principal():     
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()
    linha6 = formulario.lineEdit_6.text()
    linha7 = formulario.lineEdit_7.text()

#verificar se o RadioButton foi clicado
    if formulario.radioButton.isChecked():
        print("Genero Masculino foi selecionado")
        categoria = "Masculino"
    elif formulario.radioButton_2.isChecked():
        print("Genero Feminina foi selecionado")
        categoria = "Feminina"
 
#Impressao Teste Terminal
    print("teste")
    print("NOME:",linha1)
    print("IDADE",linha2)
    print("TELEFONE",linha3)
    print("ENDERECO",linha4)
    print("CIDADE",linha5)
    print("BAIRRO",linha6)
    print("EMAIL",linha7)
    

    cursor = conector.cursor()
    # Vai pegar o que esta sendo digitado nas caixas, e envia para o banco da dados.
    comando_SQL = "INSERT INTO CLIENTE (NOME,IDADE,TELEFONE,ENDERECO,CIDADE,BAIRRO,EMAIL,GENERO) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1),str(linha2),str(linha3),str(linha4),str(linha5),str(linha6),str(linha7),categoria)
    cursor.execute(comando_SQL,dados)
    conector.commit()
    formulario.lineEdit.setText("")
    formulario.lineEdit_2.setText("") 
    formulario.lineEdit_3.setText("")
    formulario.lineEdit_4.setText("")
    formulario.lineEdit_5.setText("")
    formulario.lineEdit_6.setText("")
    formulario.lineEdit_7.setText("")

#Declaração Funçao Principal para Lista_Dados Verificação Banco de Dados.
def funcao_segundaria():
    lista_dados.show()

    cursor = conector.cursor()
    comando_SQL = "SELECT * FROM `CLIENTE`"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    
    lista_dados.tableWidget.setRowCount(len(dados_lidos))
    lista_dados.tableWidget.setColumnCount(9)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 9):
            lista_dados.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

#Interface do Aplicativo
app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario_.ui")
lista_dados=uic.loadUi("lista_dados.ui")
formulario.pushButton.clicked.connect(funcao_principal)
formulario.pushButton_2.clicked.connect(funcao_segundaria)

#Interface Principal assim que abre o programa."Que vai aparecer"
formulario.show()
app.exec()
