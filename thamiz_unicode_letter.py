# -*- coding: utf-8 -*-

# உயிர் எழுத்துகள்
uyir = "அஆஇஈஉஊஎஏஐஒஓஔ" # உயிர்
uyir_kuril = "அஇஉஎஒ" # உயிர்குறில்
uyir_nedil = "ஆஈஊஏஐஓஔ"# உயிர்நெடில்

# புணரும் உயிர்
punarum_uyir = "ாிீுூெேைொோௌ" # புணரும் உயிர்
punarum_uyir_kuril = "ிுெொ" # புணரும் குறில்
punarum_uyir_nedil = "ாீூேைோௌ" # புணரும் நெடில்

# ஆயுத எழுத்து
akku = "ஃ"
akku_kuri = "்" # புள்ளி

# அகர உயிர்மெய் எழுத்துகள்
agara_uyirmei = "கஙசஞடணதநபமயரலவழளறன" # அகர உயிர்மெய் எழுத்துகள் 
agara_vallinam = "கசடதபற" # அகர வல்லினம்
agara_mellinam = "ஙஞணநமன" # அகர மெல்லினம்
agara_idaiyinam = "யரலவழள" # அகர இடையினம்

# மெய் எழுத்துகள் உருவாக்கம், அகர உயிர்மெய் எழுத்திலிருந்து
mei = []
vallinam = []
mellinam = []
idaiyinam = []

for i in agara_uyirmei: #மெய் எழுத்துகள்
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

for i in agara_uyirmei: #216 உயிர்மெய் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei.append(uyir_mei_list)
uyir_mei = tuple(uyir_mei)

for i in agara_uyirmei: #90 உயிர்மெய் குறில் எழுத்துகள்
    uyir_mei_list = []
    uyir_mei_list.append(i)
    for j in punarum_uyir_kuril:
        uyir_mei_list.append(i+j) #Unicode concatenation
    uyir_mei_kuril.append(uyir_mei_list)
uyir_mei_kuril = tuple(uyir_mei_kuril)

for i in agara_uyirmei: #126 உயிர்மெய் நெடில் எழுத்துகள்
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


om = "ௐ"
digit = "௦௧௨௩௪௫௬௭௮௯" # எண் 0-9
numeric = "௰௱௲" #10, 100, 1000
calender = "௳௴௵" #Day, Month, Year
clerical = "௶௷௸"#Debit, Credit, As Above
currency = "௹" #Rupees Sign
number_sign = "௺" # Number sign same as '#'
other_letter = "ஜஶஷஸஹ" #JA, SHA, SSA, SA, HA
anusvara = "ஂ" #Not used for Tamiz,

