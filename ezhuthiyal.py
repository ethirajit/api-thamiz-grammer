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
uyir_mei              = thamiz_unicode_letter.uyir_mei
uyir_mei_kuril        = thamiz_unicode_letter.uyir_mei_kuril
uyir_mei_nedil        = thamiz_unicode_letter.uyir_mei_nedil
uyir_mei_vallinam     = thamiz_unicode_letter.uyir_mei_vallinam
uyir_mei_mellinam     = thamiz_unicode_letter.uyir_mei_mellinam
uyir_mei_idaiyinam    = thamiz_unicode_letter.uyir_mei_idaiyinam
#மற்றவை
akku                  = thamiz_unicode_letter.akku
om                    = thamiz_unicode_letter.om


'''

இந்த செயல்பாட்டின் நோக்கம்
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
                    if input_string[idx+2] in punarum_uyir: # சரிபார் : ஆயுத எழுத்துக்கு பின்னே அகரம் அல்லாத வல்லின உயிர்மெய்
                        status = [True for i in uyir_mei_vallinam if input_string[idx+1]+input_string[idx+2] in i]
                        if status:
                            return True
                    else: # சரிபார் : ஆயுத எழுத்துக்கு பின்னே அகர வல்லின உயிர்மெய்
                        status = [True for i in uyir_mei_vallinam if input_string[idx+1] in i]
                        if status:
                            return True
        except IndexError as e:
            print e
    return False

input_string = thamiz_unicode_letter.string_to_unicode("எஃகு")

print check_ayutha_ezhuthu_in_word(input_string)

