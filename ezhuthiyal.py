# -*- coding: utf-8 -*-

import thamiz_unicode_letter

#Global variable
uyir       = thamiz_unicode_letter.uyir
uyir_kuril = thamiz_unicode_letter.uyir_kuril
uyir_nedil = thamiz_unicode_letter.uyir_nedil
uyir_kuri  = thamiz_unicode_letter.punarum_uyir
punarum_uyir_kuril  = thamiz_unicode_letter.punarum_uyir_kuril
punarum_uyir_nedil  = thamiz_unicode_letter.punarum_uyir_nedil

mei       = thamiz_unicode_letter.mei
uyir_mei  = thamiz_unicode_letter.uyir_mei
uyir_mei_kuril = thamiz_unicode_letter.uyir_mei_kuril
uyir_mei_nedil = thamiz_unicode_letter.uyir_mei_nedil
uyir_mei_vallinam = thamiz_unicode_letter.uyir_mei_vallinam
uyir_mei_mellinam = thamiz_unicode_letter.uyir_mei_mellinam
uyir_mei_idaiyinam = thamiz_unicode_letter.uyir_mei_idaiyinam

akku      = thamiz_unicode_letter.akku
om        = thamiz_unicode_letter.om


#இது தனக்கு முன்னே ஒரு குற்றெழுத்தையும்  பின்னே ஒரு வல்லின மெய் எழுத்தையும் துணையாகக் கொண்டு வரும்
def check_ayutha_ezhuthu_in_word(input_string):
    if akku in input_string:
        input_string = list(input_string)
        idx = input_string.index(akku)
        try:
            if idx >= 0:
                status = [True for i in uyir_mei_kuril if input_string[idx-1] in i]
                if (input_string[idx-1] in uyir_kuril) or status[0]:    
                    if input_string[idx+2] in uyir_kuri:
                        status = [True for i in uyir_mei_vallinam if input_string[idx+1]+input_string[idx+2] in i]
                        if status:
                            return True
                    else:
                        status = [True for i in uyir_mei_vallinam if input_string[idx+1] in i]
                        if status:
                            return True
        except IndexError as e:
            print e
    return False

input_string = u"எஃகு"

print check_ayutha_ezhuthu_in_word(input_string)

