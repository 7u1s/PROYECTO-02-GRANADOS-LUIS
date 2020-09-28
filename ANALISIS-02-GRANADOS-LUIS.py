# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 16:52:40 2020

@author: lUIS_lEONEL_GRANADOS_IBARRA
"""

import csv
exportotal=[]
importotal=[]
totalista=[]
with open("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    
    for linea in lector:
        totalista.append(linea)
        if linea["direction"]=="Exports":
            exportotal.append(linea)
            # open ("exportaciones.txt","a") as archivo:
            #     archivo.writelines(linea)
                
        else:
            importotal.append(linea)
    
   
   
    
 

direccion=input("elige exportaciones o importaciones    ")
if direccion== "exportaciones":
      total=exportotal
      print("las 10  rutas de exportaciones mas valiosas son :")
elif direccion=="importaciones":
    total=importotal
    print("las 10  rutas de importaciones mas valiosas son :")
else:
   print("no es opcion valida")
   quit()
   
   
totaltotaltotal=0
for t in totalista:
    totaltotaltotal+=int(t["total_value"])
print("el total de valores es ",totaltotaltotal)    
totaltotal=0
for t in total:
    totaltotal+=int(t["total_value"])
print("el total de valores en ",direccion, "es ", totaltotal)

#print(totaltotal/totaltotaltotal)


contador=0
listacontados=[]  
paisvalue=[]
totalporpais=[]
valor=0
for ex in total:
    ruta=[ex["origin"],ex["destination"]]
    if ruta not in listacontados:
        for por in total:
          if   ruta == [por["origin"],por["destination"]]:
              #print(ex)
              paisvalue.append(por["total_value"])
              valor+=int(por["total_value"])
        listacontados.append(ruta)
        totalporpais.append([ruta,len(paisvalue),valor,valor/len(paisvalue)])
        valor=0
        paisvalue=[]
#print(totalporpais)

paisesordenados=sorted(totalporpais, key=lambda pai: pai[2],reverse=True)
for p in range(9):
    print(p+1,"la ruta  ", paisesordenados[p][0], "con valor de", paisesordenados[p][2], "y valor unitario de ",paisesordenados[p][3])





     
contador=0
paisesordenados=[]
listacontados=[]  
paisvalue=[]
totalporpais=[]
valor=0
for ex in total:
    transporte=ex["transport_mode"]
    if transporte not in listacontados:
        for por in total:
          if   transporte == por["transport_mode"]:
              #print(ex)
              paisvalue.append(por["total_value"])
              valor+=int(por["total_value"])
        listacontados.append(transporte)
        totalporpais.append([transporte,len(paisvalue),valor,valor/len(paisvalue)])
        valor=0
        paisvalue=[]
#print(totalporpais)
paisesordenados=sorted(totalporpais, key=lambda pai: pai[2],reverse=True)
for p in range(3):
    print(p+1,"el mejor transporte es", paisesordenados[p][0], "con valor de", paisesordenados[p][2])
    
 
    
contador=0
paisesordenados=[]
listacontados=[]  
paisvalue=[]
totalporpais=[]
valor=0
for ex in totalista:
    pais=ex["origin"]
    if pais not in listacontados:
        for por in totalista:
          if   pais == por["origin"]:
              #print(ex)
              paisvalue.append(por["total_value"])
              valor+=int(por["total_value"])
        listacontados.append(pais)
        totalporpais.append([pais,len(paisvalue),valor,valor/len(paisvalue)])
        valor=0
        paisvalue=[]
#print(totalporpais)
paisesordenados=sorted(totalporpais, key=lambda pai: pai[2],reverse=True)
# for p in range(len(paisesordenados)):
#     print(paisesordenados[p])
#     if paisesordenados[p][2]/totaltotaltotal >= .3:
#         print(p+1,"los paises mas valiosos en general son", paisesordenados[p][0], "con valor de", paisesordenados[p][2])
p=0
suma=0
while suma/totaltotaltotal < .8:
    print(p+1,"los paises mas valiosos en general son", paisesordenados[p][0], "con valor de", paisesordenados[p][2])
    suma+=int(paisesordenados[p][2])
    p+=1

    
 
    
 
    
 
    
    
# def generador(direccion):
    # if direccion== "exportaciones":
    #     total=exportotal
    # elif direccion=="importaciones":
    #     total=importotal
    # else:
    #     return print("no es opcion valida")
    
    
        
#     contador=0
#     listacontados=[]  
#     paisvalue=[]
#     totalporpais=[]
#     for ex in total:
#         origen=ex["origin"]
#         if origen not in listacontados:
#             for por in total:
#               if   origen == por["origen"]:
#                   print(ex)
#                   paisvalue.append(por["total_value"])
#             listacontados.append(origen)
#             totalporpais.append(origen,paisvalue)
#             paisvalue=[]
#     print(totalporpais)
    
    
    
#  generador(importotal)   
    
    
    
    
# print(len(exportotal))
# print(len(importotal))
# def filtropais() 
#exporden= dict(sorted(exportotal.items(),key="origin")


#[3:14 a. m., 27/9/2020] L: Hacer listas de país actual y de países contados y de conjunto de envios
#[3:14 a. m., 27/9/2020] L: Luego ver cómo hacerlo función para los diferentes casos
    
# paisescontados=[]
# for origen en exportotal:
#     if origen["origin"]== 

# def promedio_xpais(pais):
#     nombre=pais["origin"]
#     exportes=pais["total_v"]
#     promediopais= sum(exportes)/len(exportes)
#     return promediopais
# def promedios
#     for pais in listapaises:
#     promedio_pais(pais["origin"])
    
 