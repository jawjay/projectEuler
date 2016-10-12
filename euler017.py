def threeName(N):
    single_digits = ['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
    if len(N<3):
        if len(N<2):
            return single_digits(single_digits[int(N)-1])
        return a

def euler017(N):
    def tryThree(a):
        single_digits = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
        double_digits = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen','Twenty']
        tens_digits = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety','One Hundred']

        special = False
        # if int(a[:-1]) == 0:
        #     pass
        #     # Now we need at 


        out_number = ''
        t = list(map(lambda x: int(x) , list(a)))
        if int(a)==0:
            return ''
        if int(a)<10:
            return single_digits[t[0]]
        if int(a)==10:  
            return single_digits[-1]
        if int(a)<20:
            return double_digits[t[-1]]
        
        if int(a)>99:
            # we have a three digit number
            out_number += single_digits[t[0]]+' Hundred'

        if int(a)%100>20:
            # number 
            out_number += tens_digits[t[-2]]+' '
            out_number += single_digits[t[-1]]
            return out_number
        elif int(a)%100 >10:
            out_number += double_digits[t[2]]
            return out_number

        return out_number
        try:
            return single_digits[t[0]]+double_digits[t[1]]+single_digits[t[2]]
        except IndexError:
            try:
                return single_digits[t[0]]+single_digits[t[1]]
            except IndexError:
                return single_digits[t[0]]
        return a


    num_places = len(str(N))
    sN = str(N)
    places = ['','Trillion','Billion','Million','Thousand','']
    np = range(0,num_places,3)


    out_word = ''

    for i in range(1,num_places+1,3):

        
        if num_places-i>3:
            if int(sN[-i-2:][:3])==0:
                continue
            # print(tryThree(sN[-i-2:][:3]),-int(i/3))
            out_word= tryThree(sN[-i-2:][:3]) +' '+ places[-int(i/3)]+out_word
        else:
            # print(sN[-i-2:][:num_places-i+1])
            # print(tryThree(sN[-i-2:][:num_places-i+1]))
            if(int(sN[-i-2:][:num_places-i+1]))==0:
                continue
            out_word = tryThree(sN[-i-2:][:num_places-i+1])+' '+places[-int(i/3)-1]+' '+out_word
    return out_word

    #9 zeros is 1 billion
    # 6 zeros is 1 million
    # 3 zerios is 1 thousand


# print(euler017('4000'))
print(euler017('100100'))


