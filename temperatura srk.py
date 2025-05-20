import CoolProp.CoolProp as CP
Temperatura = CP.PropsSI("T","P",101325,"Q",0,"SRK::Propane") # temperatura que eu preciso, pressão e título fornecido, modelo termodinamico, componente 
print (Temperatura)
