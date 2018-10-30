# -*- coding: utf-8 -*-

#encode() - Represent unicode string as a string of bytes [unicode -> string]
#uni = u'\u0B85' #Unicode for அ
#print uni.encode('utf-8') #It will print string literal of அ, which is equla to à®…

#decode() - Convert string of bytes as a unicode [string -> unicode]
#str = 'à®…' or str = 'அ' #String literal
#print str.decode('utf-8') #It will print unicode of அ, which is equal to u'அ'

def string_to_unicode(str_literal):
   """
   Shorthand for decoding utf-8 string literal to unicode
   """
   return str_literal.decode('utf-8')

# உயிர் எழுத்துகள்
uyir = string_to_unicode("அஆஇஈஉஊஎஏஐஒஓஔ") # உயிர்
uyir_kuril = string_to_unicode("அஇஉஎஒ") # உயிர்குறில்
uyir_nedil = string_to_unicode("ஆஈஊஏஐஓஔ")# உயிர்நெடில்

# புணரும் உயிர்
punarum_uyir = string_to_unicode("ாிீுூெேைொோௌ") # புணரும் உயிர்
punarum_uyir_kuril = string_to_unicode("ிுெொ") # புணரும் குறில்
punarum_uyir_nedil = string_to_unicode("ாீூேைோௌ") # புணரும் நெடில்

# ஆயுத எழுத்து
akku = string_to_unicode("ஃ")
akku_kuri = string_to_unicode("்") # புள்ளி

# அகர உயிர்மெய் எழுத்துகள்
agara_mei = string_to_unicode("கஙசஞடணதநபமயரலவழளறன") # அகர உயிர்மெய் எழுத்துகள் 
agara_vallinam = string_to_unicode("கசடதபற") # அகர வல்லினம்
agara_mellinam = string_to_unicode("ஙஞணநமன") # அகர மெல்லினம்
agara_idaiyinam = string_to_unicode("யரலவழள") # அகர இடையினம்

# மெய் எழுத்துகள் உருவாக்கம், அகர உயிர்மெய் எழுத்திலிருந்து
mei = []
vallinam = []
mellinam = []
idaiyinam = []

for i in agara_mei: #மெய் எழுத்துகள்
    mei.append(i+akku_kuri) #Unicode concatenation
mei = tuple(mei)

for i in agara_vallinam: #வல்லினம்
    vallinam.append(i+akku_kuri) #Unicode concatenation
vallinam = tuple(vallinam)

for i in agara_mellinam: #மெல்லினம்
    mellinam.append(i+akku_kuri) #Unicode concatenation
mellinam = tuple(mellinam)

for i in agara_idaiyinam: #இடையினம்
    idaiyinam.append(i+akku_kuri) #Unicode concatenation
idaiyinam = tuple(idaiyinam)

#உயிர்மெய் எழுத்துகள் உருவாக்கம், அகர உயிர்மெய் எழுத்திலிருந்து
uyir_mei = []
uyir_mei_kuril = []
uyir_mei_nedil = []
uyir_mei_vallinam = []
uyir_mei_mellinam = []
uyir_mei_idaiyinam = []

for i in agara_mei: #216 உயிர்மெய் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei.append(uyir_mei_list)
uyir_mei = tuple(uyir_mei)

for i in agara_mei: #90 உயிர்மெய் குறில் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir_kuril:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_kuril.append(uyir_mei_list)
uyir_mei_kuril = tuple(uyir_mei_kuril)

for i in agara_mei: #126 உயிர்மெய் நெடில் எழுத்துகள்
    uyir_mei_list = []
    for j in punarum_uyir_nedil:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_nedil.append(uyir_mei_list)
uyir_mei_nedil = tuple(uyir_mei_nedil)

for i in agara_vallinam: #72 உயிர்மெய் வல்லினம் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_vallinam.append(uyir_mei_list)
uyir_mei_vallinam = tuple(uyir_mei_vallinam)

for i in agara_mellinam: #72 உயிர்மெய் மெல்லினம் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_mellinam.append(uyir_mei_list)
uyir_mei_mellinam = tuple(uyir_mei_mellinam)

for i in agara_idaiyinam: #72 உயிர்மெய் இடையினம் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_idaiyinam.append(uyir_mei_list)
uyir_mei_idaiyinam = tuple(uyir_mei_idaiyinam)


om = string_to_unicode("ௐ")
digit = string_to_unicode("௦௧௨௩௪௫௬௭௮௯") # எண் 0-9
numeric = string_to_unicode("௰௱௲") #10, 100, 1000
calender = string_to_unicode("௳௴௵") #Day, Month, Year
clerical = string_to_unicode("௶௷௸")#Debit, Credit, As Above
currency = string_to_unicode("௹") #Rupees Sign
number_sign = string_to_unicode("௺") # Number sign same as '#'
other_letter = string_to_unicode("ஜஶஷஸஹ") #JA, SHA, SSA, SA, HA
anusvara = string_to_unicode("ஂ") #Not used for Tamiz,

