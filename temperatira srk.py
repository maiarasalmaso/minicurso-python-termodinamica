import CoolProp.CoolProp as CP
Temperatura = CP.PropsSI("T","P",101325,"Q",0,"SRK::Propane")
print (Temperatura)
