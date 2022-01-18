import pywhatkit

print("""
__        ___           _                      _    _                
\ \      / / |__   __ _| |_ ___  ___ _ __   __| |  / \   _ __  _ __  
 \ \ /\ / /| '_ \ / _` | __/ __|/ _ \ '_ \ / _` | / _ \ | '_ \| '_ \ 
  \ V  V / | | | | (_| | |_\__ \  __/ | | | (_| |/ ___ \| |_) | |_) |
   \_/\_/  |_| |_|\__,_|\__|___/\___|_| |_|\__,_/_/   \_\ .__/| .__/ 
                                                        |_|   |_|    V1
""")
print("Poznámka! Pro správnou funkčnost programu, musíte být přihlášeni k WhatsApp web")

tel = "+420" + input("Zadejte telefonní číslo příjemce: ")
mes = input("Zadejte zprávu pro příjemce: ")
h = input("Zadejte hodinu odeslání: ")
m = input("Zadejte minutu odeslání: ")

print(tel)


pywhatkit.sendwhatmsg(tel, mes, h, m)




#pywhatkit.sendwhatmsg("+420775775488", "Test", 13, 5)