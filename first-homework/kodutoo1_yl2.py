def to_camel_case(text):
    a = text.find("-") 
    b = text.find("_") 
    if a>0 and b<0:
        c = text.split("-")
        d = c[0]
        c.remove(c[0])
        for item in c:
            d = d+item.title()
    elif b>0 and a<0:
        c = text.split("_")
        d = c[0]
        c.remove(c[0])
        for item in c:
            d = d + item.title()
    elif a>0 and b>0: #kui peaks nii - ja _ olema
        c = text.split("-")
        for string in c:
            e = string.find("_") #leia string arrays kus on _
            if e>0:
                c.remove(string) #eemalda see arrayst
                f = string.split("_")
                for items in f:
                    c.append(items) #lisa tagasi arraysse splitituna
        d = "" #paljas d sest enne oli baas d = c[0]
        for item in c:
            d = d+item #for tsükliga lisa elemendid
        return d
    else:
        return ""
    return d
#kolm test runnerit
print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("the_Stealth_Warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case('the-Pippi-Is_pippi'))
print(to_camel_case('The_pippi_was_Omoshiroi'))
print(to_camel_case('A-Cat-is-Savage'))
print(to_camel_case('a-Pippi-was-cute'))
print(to_camel_case('a-Cat-Is_Pippi'))
print(to_camel_case('a_Pippi-Was-cute'))
print(to_camel_case('A_cat_Was_Hungry'))