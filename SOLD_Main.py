#Programma che usa un oggetto di WrapperDB
from SOLD_Wrapper import WrapperDB         

# CREO OGGETTO WRAPPER--------------------------------------------------------
wrp = WrapperDB()


print()
print("\n***** TEST elencoPost *****")
print(wrp.elencoPost(as_dict = True))
print("*****************************")


print()
print("\n***** TEST singoloPost *****")
print(wrp.singoloPost(1))
print("******************************")


print()
print("\n***** TEST daiLikeAPost *****")
print("Prima:")
print(wrp.singoloPost(1))
wrp.daiLikeAPost(1)
print("Dopo:")
print(wrp.singoloPost(1))
print("*******************************")


print()
print("\n***** TEST aggiungiCommento *****")
print(wrp.aggiungiCommento((1, 'W', 'WW')))
print("*****************************")


print()
print("\n***** TEST modificaCommento *****")
print(wrp.modificaCommento(('W', 'WWWWWW', 1)))
print("*****************************")


print()
print("\n***** TEST eliminaCommento *****")
print(wrp.eliminaCommento((2)))
print("*****************************")


print()
print("\n***** TEST inserisciPost *****")
parametri = ("Omino del meteo", "Ieri nevicava!!!")
wrp.inserisciPost(parametri)
print(wrp.elencoPost(as_dict = True))
print("********************************")


print()
print("\n***** TEST inserisciPostSP *****")
parametri = ("PC", "Test con stored procedure")
print(wrp.inserisciPostSP(parametri))
print(wrp.elencoPost(as_dict = True))
print("********************************")


print()
print("\n***** TEST eliminaPost *****")
print("Prima:")
print(wrp.elencoPost(as_dict = True))
wrp.eliminaPost(3)
print("Dopo:")
print(wrp.elencoPost(as_dict = True))
print("******************************")