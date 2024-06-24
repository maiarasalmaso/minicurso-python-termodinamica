import CoolProp.CoolProp as CP
densidade = CP.PropsSI("D","P",101325,"Q",0,"SRK::Propane")
volume = 1 / densidade
print (volume)
