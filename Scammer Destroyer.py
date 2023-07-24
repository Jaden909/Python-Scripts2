import json
import random

genUser=1
#whether or not to generate a first name
genPass=1
#whether or not to generate a password
genAddress=1
#whether or not to generate an address
genPNuumber=1
#whether or not to generate a phone number
genZipCode=1
#whether or not to generate a zip code
genCity=1
#whether or not to genrate a city (currently Alaskan cities only)
genLastName=1
#whether or not to generate a last name
showFullName=1
#whether or not to show the full name on one line
genCCDetails=1
#whether or not to generate credit card details

url="placeholder"

nameList=json.load(open('names.json'))
nounList=json.load(open('nouns.json'))
cityList=json.load(open('alaskan cities.json'))
lastNameList=json.load(open('last names.json'))
ccNumList=json.load(open('fake cc numbers.json'))

for user in range(genUser):
    user=random.choice(nameList)
    randomNumbersList=random.sample('1234567890!?.', k=random.choice([2,3,4,5]))
    randomNumbers=''.join(randomNumbersList)
    username=user+randomNumbers+random.choice(['@yahoo.com','@gmail.com','@outlook.com','@hotmail.com'])
    print(username)

for password in range(genPass):
    pword=random.choice(nounList)  
    randomPwNumbersList=random.sample('1234567890!?.', k=random.choice([2,3,4,5]))
    randomPwNumbers=''.join(randomPwNumbersList)
    password=pword+randomPwNumbers
    print(password)

for address in range(genAddress):
    randomAddressName=random.choice(nameList)
    randomAddressNumbersList=random.sample('1234567890', k=random.choice([2,3]))
    randomAddressNumbers=''.join(randomAddressNumbersList)
    address=randomAddressNumbers+' '+randomAddressName+' '+random.choice(['st.','ln.','dr.','ave.','blvd.','rd.'])
    print(address)

for pnumber in range(genPNuumber):
    areaCodeList=random.sample('1234567890', k=3)
    secPartList=random.sample('1234567890', k=3)
    lastPartList=random.sample('1234567890', k=4)
    areaCode=''.join(areaCodeList)
    secPart=''.join(secPartList)
    lastPart=''.join(lastPartList)
    pnumber=areaCode+'-'+secPart+'-'+lastPart
    print(pnumber)

for zipCode in range(genZipCode):
    zipCodeList=random.sample('1234567890', k=5)
    zipCode=''.join(zipCodeList)
    print(zipCode)

for city in range(genCity):
    city=random.choice(cityList)
    print(city+', AK')

for lastName in range(genLastName):
    lastName=random.choice(lastNameList)

for fullName in range(showFullName):
    fullName=user+' '+lastName
    print(fullName)

for ccNumber in range(genCCDetails):
    ccNumber=random.choice(ccNumList)
    print(ccNumber)
    cvvList=random.sample('1234567890', k=3)
    cvv=''.join(cvvList)
    print(cvv)
    exDate1=random.choice(['1','2','3', '4','5','6','7','8','9','10','11','12'])
    exDate2=random.choice(['22','23','24','25','26','27','28','29','30'])
    exDate=exDate1+'/'+exDate2
    print(exDate)
