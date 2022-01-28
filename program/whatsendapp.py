import pywhatkit

print("""
__        ___           _                      _    _                
\ \      / / |__   __ _| |_ ___  ___ _ __   __| |  / \   _ __  _ __  
 \ \ /\ / /| '_ \ / _` | __/ __|/ _ \ '_ \ / _` | / _ \ | '_ \| '_ \ 
  \ V  V / | | | | (_| | |_\__ \  __/ | | | (_| |/ ___ \| |_) | |_) |
   \_/\_/  |_| |_|\__,_|\__|___/\___|_| |_|\__,_/_/   \_\ .__/| .__/ 
                                                        |_|   |_|    V0.1
""")
print("""
Program slouží pro odeslání WhatsApp zprávy v určitý čas na česká telefonní čísla.
Poznámka! Pro funkčnost programu, musíte být přihlášeni k WhatsApp web.
https://web.whatsapp.com/
""")



tel = "+420" + input("Zadejte telefonní číslo příjemce: ")
mes = input("Zadejte zprávu pro příjemce: ")
print("Teď nastavíme čas odeslání zprávy")
h = int(input("Zadejte pouze hodinu odeslání ve tvaru hh: "))
m = int(input("Teď zadejte minuty ve tvaru mm: "))

pywhatkit.sendwhatmsg(tel, mes, h, m)

#pywhatkit.sendwhatmsg("+420775775488", "Test", 13, 5)