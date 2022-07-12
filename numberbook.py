import requests

code = input('''
Code country
Kuwait = KW
Saudi Arabia = SA
Unitad Emirates = AE
Oman = OM
Qatar = QA
Bahrain = BH
Yemen = YE
Iraq = IQ
Jordan = JO
Syria = SY
United Kingdom = GB

Enter country code please: ''')
numbers = input ("Enter your number: " )

req =requests.get(f"http://146.148.112.105/caller/index.php/UserManagement/search_number?number={numbers}&country_code={code}")

try:

  if '"response":"0"' in req.text:
      name = req.json()["result"][0]["name"]
      number= req.json()["result"][0]["number"]
      print(f"Name is: {name}\nNumber is: {number}")
  elif '"response":"2"' in req.text:
    print(f"Not Found {numbers}")
    
except:
  print(req.text)