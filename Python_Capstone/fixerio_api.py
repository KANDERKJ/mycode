#!/usr/bin/env python3



import requests
import json

# goal: import data from api, translate json to python, use data to run currency conversion script

# dictionary with country and abbreviations
country_dict= {
  "Australia Dollar": "AUD",
  "Great Britain Pound": "GBP",
  "Euro": "EUR",
  "Japan Yen": "JPY",
  "Switzerland Franc": "CHF",
  "USA Dollar": "USD",
  "Afghanistan Afghani": "AFN",
  "Albania Lek": "ALL",
  "Algeria Dinar": "DZD",
  "Angola Kwanza": "AOA",
  "Argentina Peso": "ARS",
  "Armenia Dram": "AMD",
  "Aruba Florin": "AWG",
  "Austria Schilling": "ATS",
  "Belgium Franc": "BEF",
  "Azerbaijan New Manat": "AZN",
  "Bahamas Dollar": "BSD",
  "Bahrain Dinar": "BHD",
  "Bangladesh Taka": "BDT",
  "Barbados Dollar": "BBD",
  "Belarus Ruble": "BYR",
  "Belize Dollar": "BZD",
  "Bermuda Dollar": "BMD",
  "Bhutan Ngultrum": "BTN",
  "Bolivia Boliviano": "BOB",
  "Bosnia Mark": "BAM",
  "Botswana Pula": "BWP",
  "Brazil Real": "BRL",
  "Brunei Dollar": "BND",
  "Bulgaria Lev": "BGN",
  "Burundi Franc": "BIF",
  "CFA Franc BCEAO": "XOF",
  "CFA Franc BEAC": "XAF",
  "CFP Franc": "XPF",
  "Cambodia Riel": "KHR",
  "Canada Dollar": "CAD",
  "Cape Verde Escudo": "CVE",
  "Cayman Islands Dollar": "KYD",
  "Chili Peso": "CLP",
  "China Yuan/Renminbi": "CNY",
  "Colombia Peso": "COP",
  "Comoros Franc": "KMF",
  "Congo Franc": "CDF",
  "Costa Rica Colon": "CRC",
  "Croatia Kuna": "HRK",
  "Cuba Convertible Peso": "CUC",
  "Cuba Peso": "CUP",
  "Cyprus Pound": "CYP",
  "Czech Koruna": "CZK",
  "Denmark Krone": "DKK",
  "Djibouti Franc": "DJF",
  "Dominican Republich Peso": "DOP",
  "East Caribbean Dollar": "XCD",
  "Egypt Pound": "EGP",
  "El Salvador Colon": "SVC",
  "Estonia Kroon": "EEK",
  "Ethiopia Birr": "ETB",
  "Falkland Islands Pound": "FKP",
  "Finland Markka": "FIM",
  "Fiji Dollar": "FJD",
  "Gambia Dalasi": "GMD",
  "Georgia Lari": "GEL",
  "Germany Mark": "DMK",
  "Ghana New Cedi": "GHS",
  "Gibraltar Pound": "GIP",
  "Greece Drachma": "GRD",
  "Guatemala Quetzal": "GTQ",
  "Guinea Franc": "GNF",
  "Guyana Dollar": "GYD",
  "Haiti Gourde": "HTG",
  "Honduras Lempira": "HNL",
  "Hong Kong Dollar": "HKD",
  "Hungary Forint": "HUF",
  "Iceland Krona": "ISK",
  "India Rupee": "INR",
  "Indonesia Rupiah": "IDR",
  "Iran Rial": "IRR",
  "Iraq Dinar": "IQD",
  "Ireland Pound": "IED",
  "Israel New Shekel": "ILS",
  "Italy Lira": "ITL",
  "Jamaica Dollar": "JMD",
  "Jordan Dinar": "JOD",
  "Kazakhstan Tenge": "KZT",
  "Kenya Shilling": "KES",
  "Kuwait Dinar": "KWD",
  "Kyrgyzstan Som": "KGS",
  "Laos Kip": "LAK",
  "Latvia Lats": "LVL",
  "Lebanon Pound": "LBP",
  "Lesotho Loti": "LSL",
  "Liberia Dollar": "LRD",
  "Libya Dinar": "LYD",
  "Lithuania Litas": "LTL",
  "Luxembourg Franc": "LUF",
  "Macau Pataca": "MOP",
  "Macedonia Denar": "MKD",
  "Malagasy Ariary": "MGA",
  "Malawi Kwacha": "MWK",
  "Malaysia Ringgit": "MYR",
  "Maldives Rufiyaa": "MVR",
  "Malta Lira": "MTL",
  "Mauritania Ouguiya": "MRO",
  "Mauritius Rupee": "MUR",
  "Mexico Peso": "MXN",
  "Moldova Leu": "MDL",
  "Mongolia Tugrik": "MNT",
  "Morocco Dirham": "MAD",
  "Mozambique New Metical": "MZN",
  "Myanmar Kyat": "MMK",
  "NL Antilles Guilder": "ANG",
  "Namibia Dollar": "NAD",
  "Nepal Rupee": "NPR",
  "Netherlands Guilder": "NLG",
  "New Zealand Dollar": "NZD",
  "Nicaragua Cordoba Oro": "NIO",
  "Nigeria Naira": "NGN",
  "North Korea Won": "KPW",
  "Norway Kroner": "NOK",
  "Oman Rial": "OMR",
  "Pakistan Rupee": "PKR",
  "Panama Balboa": "PAB",
  "Papua New Guinea Kina": "PGK",
  "Paraguay Guarani": "PYG",
  "Peru Nuevo Sol": "PEN",
  "Philippines Peso": "PHP",
  "Poland Zloty": "PLN",
  "Portugal Escudo": "PTE",
  "Qatar Rial": "QAR",
  "Romania New Lei": "RON",
  "Russia Rouble": "RUB",
  "Rwanda Franc": "RWF",
  "Samoa Tala": "WST",
  "Sao Tome/Principe Dobra": "STD",
  "Saudi Arabia Riyal": "SAR",
  "Serbia Dinar": "RSD",
  "Seychelles Rupee": "SCR",
  "Sierra Leone Leone": "SLL",
  "Singapore Dollar": "SGD",
  "Slovakia Koruna": "SKK",
  "Slovenia Tolar": "SIT",
  "Solomon Islands Dollar": "SBD",
  "Somali Shilling": "SOS",
  "South Africa Rand": "ZAR",
  "South Korea Won": "KRW",
  "Spain Peseta": "ESP",
  "Sri Lanka Rupee": "LKR",
  "St Helena Pound": "SHP",
  "Sudan Pound": "SDG",
  "Suriname Dollar": "SRD",
  "Swaziland Lilangeni": "SZL",
  "Sweden Krona": "SEK",
  "Syria Pound": "SYP",
  "Taiwan Dollar": "TWD",
  "Tanzania Shilling": "TZS",
  "Thailand Baht": "THB",
  "Tonga Pa'anga": "TOP",
  "Trinidad/Tobago Dollar": "TTD",
  "Tunisia Dinar": "TND",
  "Turkish New Lira": "TRY",
  "Turkmenistan Manat": "TMM",
  "Uganda Shilling": "UGX",
  "Ukraine Hryvnia": "UAH",
  "Uruguay Peso": "UYU",
  "United Arab Emirates Dirham": "AED",
  "Vanuatu Vatu": "VUV",
  "Venezuela Bolivar": "VEB",
  "Vietnam Dong": "VND",
  "Yemen Rial": "YER",
  "Zambia Kwacha": "ZMK",
  "Zimbabwe Dollar": "ZWD"
}

# retrieving api data in json format
params = {"api_key": "ab4eae6c092bb90fd6e41e8c17e40486", "format": "jsonp"}
r = requests.get('http://data.fixer.io/api/latest?access_key=ab4eae6c092bb90fd6e41e8c17e40486')
# translating json into python data as dictionary
api_dict = r.json()["rates"]


print("What currency do you need?")
print(country_dict)
print(" What is the abbreviation of the currency you want to convert from EUR?\
        Options:")
for item in api_dict.keys():
    print(item, end=" ")
print()
while True:
  try:
    currency = input("Please enter one of these values:\n")
    foreign_cash = float(api_dict[currency])
    break
  except:
    print("That's not an acceptable currency. Try again.")
while True:
  try:
    amount = float(input("Enter amount:\n"))
    print(f'{amount} EUR is equal to {amount * foreign_cash}\
        {currency}')
    break
  except:
    print("That's not a real amount. Try again.")                                
