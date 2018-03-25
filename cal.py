import json
dic=json.load(open("cal.json"))
dic_se=json.load(open("se.json"))
def Count_cal(text_food, text_exe):
    val = 1785
    count = 0
    cal_val = 0
    burn_val = 0
    list_food = text_food.split(",")
    list_exe = str(text_exe)
    print(list_food)
    for data in dic:
        for item in list_food:
            if(str(item)==str(data['name'])):
                count = count+1
                cal_val=cal_val+int(data['value'])

    for data in dic_se:
        if(list_exe==str(data['name'])):
            burn_val = data['value']

    print(cal_val)
    r_value = ((val+(cal_val*2))/2)-burn_val
    return [cal_val, burn_val,r_value]

def Count_per(temp):
    new_val = (int(temp) - 1750)/10
    return new_val

def Count_money(per):
    sav = 0.0
    if float(per)>=50:
        sav=((per*7900)/100)
    elif float(per)<50 and float(per)>30:
        sav=((per*3995)/100)
    elif float(per)<30:
        sav = 0.0
    return sav

if __name__=="__main__":
    #print(dic[0]['value'])
    t = "milk,bread,coffee,pizza,burgar,cheese,butter,chicken,beef"
    ans = Count_cal(text_food=t,text_exe="walking")
    print(ans)
