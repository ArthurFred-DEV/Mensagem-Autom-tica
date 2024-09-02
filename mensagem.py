import pywhatkit    
# Aqui você coloca o número que deseja enviar a mensagem automatica, usando o código do país e o DDD.
phone_number = ''
# Escreve a frase que deseja ser enviada a pessoa.
messege = 'OLÁ, ESSA MENSAGEM FOI ENVIADA USANDO PYTHON!!'
#Define a hora que a mensagem sera enviada
hours = 11 
minutes = 29
pywhatkit.sendwhatmsg(phone_number, messege, hours, minutes)
print('Mensagem enviada')
