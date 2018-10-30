# -*- coding: utf-8 -*-

def generate_mei_uyirmei(agara_mei, punar_kuri=None):
    return_var = []
    if punar_kuri: #உயிர்மெய் எழுத்துகள்
        for i in agara_mei:
            uyir_mei_list = []
            if punar_kuri != punarum_uyir_nedil: #Skip agara_uyirmei in Nedil
                uyir_mei_list.append(i)
            for j in punar_kuri:
                uyir_mei_list.append(i+j) #Unicode concatenation
            return_var.append(uyir_mei_list)
        return_var = tuple(return_var)
        return return_var
	
    else: #மெய் எழுத்துகள்
        for i in agara_mei:
            return_var.append(i+akku_kuri) #Unicode concatenation
        return_var = tuple(return_var)
        return return_var


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

mei = generate_mei_uyirmei(agara_uyirmei) #மெய் எழுத்துகள்
vallinam = generate_mei_uyirmei(agara_vallinam) #வல்லினம்
mellinam = generate_mei_uyirmei(agara_mellinam) #மெல்லினம்
idaiyinam = generate_mei_uyirmei(agara_idaiyinam) #இடையினம்

#உயிர்மெய் எழுத்துகள் உருவாக்கம், அகர உயிர்மெய் எழுத்திலிருந்து
uyir_mei = []
uyir_mei_kuril = []
uyir_mei_nedil = []
uyir_mei_vallinam = []
uyir_mei_mellinam = []
uyir_mei_idaiyinam = []

uyir_mei = generate_mei_uyirmei(agara_uyirmei, punarum_uyir) #216 உயிர்மெய் எழுத்துகள்
uyir_mei_kuril = generate_mei_uyirmei(agara_uyirmei, punarum_uyir_kuril) #90 உயிர்மெய் குறில் எழுத்துகள்
uyir_mei_nedil = generate_mei_uyirmei(agara_uyirmei, punarum_uyir_nedil) #126 உயிர்மெய் நெடில் எழுத்துகள்
uyir_mei_vallinam = generate_mei_uyirmei(agara_vallinam, punarum_uyir) #72 உயிர்மெய் வல்லினம் எழுத்துகள்
uyir_mei_mellinam = generate_mei_uyirmei(agara_mellinam, punarum_uyir) #72 உயிர்மெய் மெல்லினம் எழுத்துகள்
uyir_mei_idaiyinam = generate_mei_uyirmei(agara_idaiyinam, punarum_uyir) #72 உயிர்மெய் இடையினம் எழுத்துகள்



om = "ௐ"
digit = "௦௧௨௩௪௫௬௭௮௯" # எண் 0-9
numeric = "௰௱௲" #10, 100, 1000
calender = "௳௴௵" #Day, Month, Year
clerical = "௶௷௸"#Debit, Credit, As Above
currency = "௹" #Rupees Sign
number_sign = "௺" # Number sign same as '#'
other_letter = "ஜஶஷஸஹ" #JA, SHA, SSA, SA, HA
anusvara = "ஂ" #Not used for Tamiz,


