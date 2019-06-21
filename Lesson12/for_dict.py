#dict
pref_code = {'Hokkaido': 1, 'Aomori': 2, 'Tokyo': 13, 'Osaka': 27}
#keys 
for code in pref_code.keys():
      print(code)
      
#values 
for value in pref_code.values():
      print(value)
      
#items 
for key, value in pref_code.items():
      print(f"{key} : {value}")
      