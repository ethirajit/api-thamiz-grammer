# -*- coding: utf-8 -*-

import thamiz_unicode_letter

#Global variable
#உயிர் எழுத்துகள்
uyir                  = thamiz_unicode_letter.uyir
uyir_kuril            = thamiz_unicode_letter.uyir_kuril
uyir_nedil            = thamiz_unicode_letter.uyir_nedil
punarum_uyir          = thamiz_unicode_letter.punarum_uyir
punarum_uyir_kuril    = thamiz_unicode_letter.punarum_uyir_kuril
punarum_uyir_nedil    = thamiz_unicode_letter.punarum_uyir_nedil
#மெய் எழுத்துகள்
mei                   = thamiz_unicode_letter.mei
vallinam              = thamiz_unicode_letter.vallinam
mellinam              = thamiz_unicode_letter.mellinam
idaiyinam             = thamiz_unicode_letter.idaiyinam
#உயிர்மெய் எழுத்துகள்
agara_uyirmei         = thamiz_unicode_letter.agara_uyirmei
uyir_mei              = thamiz_unicode_letter.uyir_mei
uyir_mei_kuril        = thamiz_unicode_letter.uyir_mei_kuril
uyir_mei_nedil        = thamiz_unicode_letter.uyir_mei_nedil
uyir_mei_vallinam     = thamiz_unicode_letter.uyir_mei_vallinam
uyir_mei_mellinam     = thamiz_unicode_letter.uyir_mei_mellinam
uyir_mei_idaiyinam    = thamiz_unicode_letter.uyir_mei_idaiyinam
#மற்றவை
akku                  = thamiz_unicode_letter.akku
akku_kuri             = thamiz_unicode_letter.akku_kuri
om                    = thamiz_unicode_letter.om



'''
நோக்கம்:
UNICODE அமைப்பின்படி அகரத்திற்கு புணரும் குறி இல்லையாமையால்
கொடுக்கப்பட்ட எழுத்து அகர உயிர்மெய்யா அல்லது அகரம் அல்லாத உயிர்மெய்யா என சரிபார்

Input  => Unicode string, Index of the latter
Return =>  புணரும் குறி or empty string
'''
def சரிபார்_அகரம்_அல்லாத_உயிர்மெய்யா(input_string, idx):
    if input_string[idx] in punarum_uyir:
        return input_string[idx]
    else:
        return ""

'''
நோக்கம்:
UNICODE அமைப்பின்படி அகரத்திற்கு புணரும் குறி இல்லையாமையால்
கொடுக்கப்பட்ட எழுத்து அகர உயிர்மெய்யா, அகர மெய்யா, அகரம் அல்லாத உயிர்மெய்யா அல்லது அகரம் அல்லாத மெய்யா என சரிபார்

Input  => Unicode string, Index of the latter
Return =>  புணரும் குறி or empty string
'''
def சரிபார்_அகரம்_அல்லாத_உயிர்மெய்யா_மெய்யா(input_string, idx):
    if (input_string[idx] in punarum_uyir) or (input_string[idx] in akku_kuri):
        return input_string[idx]
    else:
        return ""

'''
நோக்கம்:
வார்த்தையை எழுத்து எழுத்தாக பிரித்தல்

Input  => Unicode string
Output => Tuple of splitted word
'''
def split_word_to_letter(input_string):
    out_list = []
    for idx in range(1, len(input_string)):
        அகரம்_அல்லாத_உயிர்மெய்_மெய் = சரிபார்_அகரம்_அல்லாத_உயிர்மெய்யா_மெய்யா(input_string, idx)
        if அகரம்_அல்லாத_உயிர்மெய்_மெய்:
            out_list.append(input_string[idx-1]+அகரம்_அல்லாத_உயிர்மெய்_மெய்)
        else:
            அகரம்_அல்லாத_உயிர்மெய்_மெய் = சரிபார்_அகரம்_அல்லாத_உயிர்மெய்யா_மெய்யா(input_string, idx-1)
            if not அகரம்_அல்லாத_உயிர்மெய்_மெய்:
                out_list.append(input_string[idx-1])
    return tuple(out_list)

'''
நோக்கம்:
ஒரு வார்த்தை ஆயுத எழுத்தை கொண்டுள்ளதா என சரிபார்க்கவும், கொண்டுள்ளதெனில் கீழ் வரும் இலக்கணத்தை கடைபிடிக்க வேண்டும்

இலக்கணம்:
ஆயுதம் தனக்கு முன்னே ஒரு குற்றெழுத்தையும் பின்னே ஒரு வல்லின மெய் எழுத்தையும் துணையாகக் கொண்டு வரும்

Input  => Unicode string
Return =>  True or False
'''
def check_ayutha_ezhuthu_in_word(input_string):
    if akku in input_string:
        input_string = list(input_string)
        idx = input_string.index(akku)
        try:
            if idx > 0:
                status = [True for i in uyir_mei_kuril if input_string[idx-1] in i]
                if (input_string[idx-1] in uyir_kuril) or status: # சரிபார் : ஆயுத எழுத்துக்கு முன்னே உயிர்மெய் குறில் அல்லது உயிர்குறில்
                    அகரம்_அல்லாத_உயிர்மெய் = சரிபார்_அகரம்_அல்லாத_உயிர்மெய்யா(input_string, idx+2)
                    status = [True for i in uyir_mei_vallinam if input_string[idx+1]+அகரம்_அல்லாத_உயிர்மெய் in i] # சரிபார் : ஆயுத எழுத்துக்கு பின்னே ஒரு வல்லின மெய்எழுத்து
                    if status:
                        return True
        except IndexError as e:
            print (e)
    return False
	
'''
நோக்கம்:
ஒரு வார்த்தை ஒற்றளபெடை இலக்கணத்தை கடைபிடிக்கின்றனவா என்பதை சாரிப்பர்.

இலக்கணம்:
    ஒற்றளபெடை என்பது ஒற்றெழுத்து தனக்குரிய அரை மாத்திரையிலிருந்து நீண்டொலிப்பதாகும்.
    ஒற்று + அளபெடை = ஒற்றளபெடை
    செய்யுளில் ஓசை குறையுமிடத்து அதனை நிறைவு செய்ய மெய்யெழுத்துகளில் ங், ஞ், ண், ந், ம், ன், வ், ய், ல் ,ள் என்பனவும் ஆய்தமும் மொழிக்கு இடை, கடை ஆகிய
    இடங்களில் குறிற்கீழும் குறிலிணையின் கீழும் அளபெடுக்கும். இதுவே ஒற்றளபெடை ஆகும்.

எ.கா:
வெஃஃகு வார்க்கில்லை	குறிற்கீழ் இடை
கண்ண் கருவிளை	குறிற்கீழ் கடை
கலங்ங்கு நெஞ்ச்மிலை	குறிலிணைகீழ் இடை
மடங்ங் கலந்த மன்னே	குறிலிணைகீழ் கடை

Input  => Unicode string
Return =>  ஒற்றளபெடை வகைகள் or False
'''
def check_ottralabadai_in_word(input_string):
    check_lists = ("ங்", "ஞ்", "ண்", "ந்", "ம்", "ன்", "வ்", "ய்", "ல்", "ள்", "ஃ")
    split_words = split_word_to_letter(input_string)
    for check_list in check_lists:
        for idx in range(len(split_words)):
            if split_words[idx] == check_list:
                if split_words[idx+1] == check_list:
                    if len(split_words) == idx+2: #கடை
                        if idx == 1:
                            return "குறிற்கீழ் கடை"
                        elif idx == 2:
                            return "குறிலிணைகீழ் கடை"
                    else: #இடை
                        if idx == 1:
                            return "குறிற்கீழ் இடை"
                        elif idx == 2:
                            return "குறிலிணைகீழ் இடை"
    return False

input_string = "குறிலிணைகீழ் கடை"

print(check_ottralabadai_in_word(input_string))

