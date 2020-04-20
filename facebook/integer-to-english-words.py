def integer_to_english_words(num):
    ret = ""
    billion = 1000000000
    million = 1000000
    thousand = 1000
    n_to_english = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Sevnteen',
        18: 'Eighteen',
        19: 'Ninteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Fourty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninty'
    }
    if num >= billion:
        ret += integer_to_english_words(num / billion) + " Billion "
        num = num % billon
    if num >= million:
        ret += integer_to_english_words(num / million) + " Million "
        num = num % million
    if num >= thousand:
        ret += integer_to_english_words(num / thousand) + " Thousand "
        num = num % thousand
    if num >= 100:
        ret += n_to_english[num / 100] + " Hundred "
        num = num % 100
    if num == 10:
        return  ret + " Ten"
    if num > 10:
        ret += n_to_english[num/10*10] + " "
        num = num % 10
    if num > 0:
        ret += n_to_english[num]

    return ret.strip()


print integer_to_english_words(9999999)
print integer_to_english_words(1234567)

        
        
