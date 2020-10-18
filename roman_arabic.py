import sys
import re
import array

word = input('How can I help you? ')
string = word
c_input = 'Please convert'
c_input_location = string.find(c_input)
single_word = string.split(' ')
input_using = 'using'
input_minimally = 'minimally'

def correct_form(string):

    if not string.find(c_input) == 0:
        return False
    else:
        if string.find('using') > 0 or string.find('minimally') > 0:
            using = string[c_input_location:].find('using')
            minimally = string[c_input_location:].find('minimally')
            using_num = 0
            minimally_num = 0
            if using > -1 and minimally > -1:
                return False
            if using > -1:
                using_num += 1
            if minimally > -1:
                minimally_num += 1
            if using_num > 1 or minimally_num > 1:
                return False
        using_location = 0
        minimally_location = 0
        if 'using' in string:
            for i in single_word:
                if i == 'using':
                    break
                else:
                    using_location += 1
            rest1 = single_word[using_location - 1:c_input_location + 1:-1]
            rest2 = single_word[using_location + 1:]
            if not rest1:
                return False
            if not rest2:
                return False

            a1 = len(rest1)
            a2 = len(rest2)
            if a1 > 1:
                return False
            if a2 > 1:
                return False
            else:
                return True
        if 'minimally' in string:
            for j in single_word:
                if j == 'minimally':
                    break
                else:
                    minimally_location += 1
            rest3 = single_word[minimally_location - 1:c_input_location + 1:-1]
            if not rest3:
                return False
            a3 = len(rest3)
            if a3 > 1:
                return False
            else:
                return True
        else:
            rest0 = single_word[:c_input_location + 1:-1]
            a0 = len(rest0)
            if a0 > 1:
                return False
            if a0 == 0:
                return False
            else:
                return True

def correct_num(string):
    if first_input(string):
        print('Sure! It is ', first_input(string), sep='')
        sys.exit()
    if second_input(string):
        print('Sure! It is ', second_input(string), sep='')
        sys.exit()
    if third_input(string):
        print('Sure! It is ', third_input(string)[0], ' using ', third_input(string)[1], sep='')
        sys.exit()
    else:
        return False

def convert_alabo_roman(num):
    ccc = int(num)
    num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roman_list = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    c_num1 = ''
    for i in range(len(num_list)):
        while ccc >= num_list[i]:
            ccc -= num_list[i]
            c_num1 += roman_list[i]
    return c_num1

roman = (('M', 1000), ('CM', 900), ('D', 500),
        ('CD', 400), ('C', 100), ('XC', 90),
        ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
        ('V', 5), ('IV', 4), ('I', 1))

correct_roman = r"^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$"

def first_input(string):
    if correct_form(string):
        if re.search(input_using, string):
            return False
        else:
            if re.search(input_minimally, string):
                return False
            else:
                num_1 = single_word[:c_input_location + 1:-1]
                st_num = ''.join(num_1)
                a = st_num[0]
                if not st_num.isdigit():
                    if not st_num.isupper():
                        return False
                if st_num.isdigit() or st_num.isupper():
                    if st_num.isdigit():
                        if a == 0:
                            return False
                        else:
                            k = int(st_num)
                            if k > 3999:
                                return False
                            else:
                                j = convert_alabo_roman(st_num)
                                output_num1 = j
                                return output_num1
                    else:
                        output_num1 = 0
                        check = 0
                        for roman_num, integers in roman:
                            while st_num[check:check + len(roman_num)] == roman_num:
                                output_num1 += integers
                                check += len(roman_num)
                        return output_num1


def second_input(string):
    if correct_form(string):
        using_location = 0
        if not re.search(input_using, string):
            return False
        else:
            for i in single_word:
                if i == 'using':
                    break
                else:
                    using_location += 1
            num2 = single_word[using_location - 1:c_input_location + 1:-1]
            num3 = single_word[using_location + 1:]
            st_num2 = ''.join(num2)
            st_num3 = ''.join(num3)
            p = st_num2[0]
            reverse_st_num3 = st_num3[:: -1]
            check_num2 = st_num2[0]
            check_st_num3 = []

            if st_num2.isalpha():
                for x in st_num2:
                    if x not in st_num3:
                        return False
            for x in st_num3:
                a = st_num3.count(x)
                if a > 1:
                    return False
            if not (st_num2.isdigit() or st_num2.isalpha()):
                return False
            if not st_num3.isalpha():
                return False
            if st_num2.isdigit() or st_num2.isalpha():
                if check_num2 == 0:
                    return False
            if st_num3.isdigit():
                return False
            k =0
            reverse_dict = {}
            c = len(reverse_st_num3)
            n = 0
            if c < 4:
                l = reverse_st_num3[n]
                reverse_dict[l] = 10 ** k
                if c == 2:
                    ll = reverse_st_num3[n + 1]
                    reverse_dict[ll] = 5 * reverse_dict[l]
                    reverse_dict[l + ll] = 4 * reverse_dict[l]
                if c == 3:
                    ll = reverse_st_num3[n + 1]
                    reverse_dict[ll] = 5 * reverse_dict[l]
                    reverse_dict[l + ll] = 4 * reverse_dict[l]
                    lll = reverse_st_num3[n + 2]
                    reverse_dict[lll] = 10 ** (k + 1)
                    reverse_dict[l + lll] = 9 * reverse_dict[l]
            else:
                for n in range(0, c, 4):
                    l = reverse_st_num3[n]
                    reverse_dict[l] = 10 ** k
                    if n + 1 < c:
                        ll = reverse_st_num3[n + 1]
                        reverse_dict[ll] = 5 * reverse_dict[l]
                        reverse_dict[l + ll] = 4 * reverse_dict[l]
                    if n + 2 < c:
                        lll = reverse_st_num3[n + 2]
                        reverse_dict[lll] = 10 ** (k + 1)
                        reverse_dict[l + lll] = 9 * reverse_dict[l]
                    if n + 3 < c:
                        llll = reverse_st_num3[n + 3]
                        reverse_dict[llll] = 5 * reverse_dict[lll]
                        reverse_dict[lll + llll] = 4 * reverse_dict[lll]
                    if n + 4 < c:
                        l5 = reverse_st_num3[n + 4]
                        reverse_dict[l5] = 10 * reverse_dict[lll]
                        reverse_dict[lll + l5] = 9 * reverse_dict[lll]
                    k += 2
            keys = list(reverse_dict.keys())
            values = list(reverse_dict.values())
            new_roman_list = list(zip(keys, values))
            new_roman_list = sorted(new_roman_list, key=lambda s: s[1], reverse=True)
            if st_num2.isalpha():
                for r in range(1, len(reverse_st_num3), 2):
                    continuous_num = reverse_st_num3[r]
                    inccorect_num = continuous_num + continuous_num
                    if r + 1 < len(reverse_st_num3):
                        last_num = reverse_st_num3[r + 1]
                        inccorect_num2 = continuous_num + last_num
                        if re.search(inccorect_num2, st_num2):
                            return False
                    if re.search(inccorect_num, st_num2):
                        return False
                for ten_times in range(0, len(reverse_st_num3), 2):
                    continuous_num1 = reverse_st_num3[ten_times]
                    inccorect_num3 = 4 * continuous_num1
                    if inccorect_num3 in st_num2:
                        return False
                for o in range(0, len(reverse_st_num3)):
                    pointer1 = reverse_st_num3[o]
                    value1 = reverse_dict[pointer1]
                    for b in range(0, len(reverse_st_num3)):
                        pointer2 = reverse_st_num3[b]
                        value2 = reverse_dict[pointer2]
                        if value2 > value1:
                            error1 = pointer1 + pointer2 + pointer1
                            error2 = 2 * pointer1 + pointer2
                            if error1 in st_num2:
                                return False
                            if error2 in st_num2:
                                return False
                        if value2 / value1 >= 50:
                            error3 = pointer1 + pointer2
                            if error3 in st_num2:
                                return False
                    output_num2 = 0
                    check = 0
                    for new_roman_num, integers in new_roman_list:
                        while st_num2[check:check + len(new_roman_num)] == new_roman_num:
                            output_num2 += integers
                            check += len(new_roman_num)
                    return output_num2
            if st_num2.isdigit():
                if int(p) == 0:
                    print('Hey, ask me something that\'s not impossible to do!')
                    sys.exit()
                n = int(st_num2)
                output_num2 = ''
                for new_roman_num, integers in new_roman_list:
                    while n >= integers:
                        output_num2 += new_roman_num
                        n -= integers
                for items in st_num3:
                    if 4 * items in output_num2:
                        return False
                    else:
                        return output_num2

def third_input(string):
    minimally_location = 0
    if re.search(input_minimally, string):
        for j in single_word:
            if j == 'minimally':
                break
            else:
                minimally_location += 1
        num4 = single_word[minimally_location - 1:c_input_location + 1:-1]
        st_num4 = ''.join(num4)
        new_roman_list = []
        reverse_num4 = st_num4[::-1]
        if not st_num4.isalpha():
            return False
        if len(st_num4) > 1:
            if st_num4[0] == st_num4[len(st_num4) - 1]:
                return False
        for i in range(len(st_num4) - 1, -1, -1):
            check_point = 0
            for j in range(len(st_num4) - 1, -1, -1):
                if st_num4[i] == st_num4[j]:
                    check_point += 1
            if st_num4[i] in new_roman_list:
                if st_num4[i] == st_num4[i - 1]:
                    if st_num4[i] == new_roman_list[-1]:
                        if len(new_roman_list) % 2 == 0:
                            new_roman_list.remove(st_num4[i])
                            new_roman_list.append('_')
                            new_roman_list.append(st_num4[i])
            if st_num4[i] not in new_roman_list:
                if check_point == 1:
                    new_roman_list.append(st_num4[i])
                if check_point >= 2:
                    if i >= 1:
                        if st_num4[i - 1] == st_num4[i]:
                            if len(new_roman_list) % 2 == 1:
                                new_roman_list.append('_')
                            new_roman_list.append(st_num4[i])
                    if i >= 2:
                        if st_num4[i - 2] == st_num4[i]:
                            if st_num4[i] != st_num4[i - 1]:
                                if len(new_roman_list) % 2 == 1:
                                    new_roman_list.append('_')
                                new_roman_list.append(st_num4[i - 1])
                                new_roman_list.append('_')
                                new_roman_list.append(st_num4[i])
                    if i >= 3:
                        if st_num4[i - 3] == st_num4[i]:
                            if st_num4[i] != st_num4[i - 1]:
                                if st_num4[i] != st_num4[i - 2]:
                                    if st_num4[i - 1] != st_num4[i - 2]:
                                        if len(new_roman_list) % 2 == 1:
                                            new_roman_list.append('_')
                                        new_roman_list.append(st_num4[i - 1])
                                        new_roman_list.append('_')
                                        new_roman_list.append(st_num4[i])
                                        new_roman_list.append(st_num4[i - 2])
                    if i >= 0:
                        if st_num4[i] not in new_roman_list:
                            new_roman_list.append(st_num4[i])
        for i in range(0, len(new_roman_list), +2):
            if i + 1 < len(new_roman_list):
                number_1 = 0
                number_2 = 0
                reverse_1 = new_roman_list[i]
                reverse_2 = new_roman_list[i + 1]
                for item in st_num4:
                    if new_roman_list[i] == item:
                        number_1 += 1
                    if new_roman_list[i + 1] == item:
                        number_2 += 1
                if number_1 == 1 and number_2 == 1:
                    new_roman_list[i] = reverse_2
                    new_roman_list[i + 1] = reverse_1
        form_output = str(''.join(new_roman_list[::-1]))
        k = 0
        reverse_dict = {}
        c = len(form_output)
        n = 0
        if c < 4:
            l = new_roman_list[n]
            reverse_dict[l] = 10 ** k
            if c == 2:
                ll = new_roman_list[n + 1]
                reverse_dict[ll] = 5 * reverse_dict[l]
                reverse_dict[l + ll] = 4 * reverse_dict[l]
            if c == 3:
                ll = new_roman_list[n + 1]
                reverse_dict[ll] = 5 * reverse_dict[l]
                reverse_dict[l + ll] = 4 * reverse_dict[l]
                lll = new_roman_list[n + 2]
                reverse_dict[lll] = 10 ** (k + 1)
                reverse_dict[l + lll] = 9 * reverse_dict[l]
        else:
            for n in range(0, c, 4):
                l = new_roman_list[n]
                reverse_dict[l] = 10 ** k
                if n + 1 < c:
                    ll = new_roman_list[n + 1]
                    reverse_dict[ll] = 5 * reverse_dict[l]
                    reverse_dict[l + ll] = 4 * reverse_dict[l]
                if n + 2 < c:
                    lll = new_roman_list[n + 2]
                    reverse_dict[lll] = 10 ** (k + 1)
                    reverse_dict[l + lll] = 9 * reverse_dict[l]
                if n + 3 < c:
                    llll = new_roman_list[n + 3]
                    reverse_dict[llll] = 5 * reverse_dict[lll]
                    reverse_dict[lll + llll] = 4 * reverse_dict[lll]
                if n + 4 < c:
                    l5 = new_roman_list[n + 4]
                    reverse_dict[l5] = 10 * reverse_dict[lll]
                    reverse_dict[lll + l5] = 9 * reverse_dict[lll]
                k += 2
        keys = list(reverse_dict.keys())
        values = list(reverse_dict.values())
        new_roman_list1 = list(zip(keys, values))
        new_roman_list1 = sorted(new_roman_list1, key=lambda s: s[1], reverse=True)
        for r in range(1, len(new_roman_list), 2):
            continuous_num = new_roman_list[r]
            inccorect_num = continuous_num + continuous_num
            if r + 1 < len(new_roman_list):
                last_num = new_roman_list[r + 1]
                inccorect_num2 = continuous_num + last_num
                if re.search(inccorect_num2, st_num4):
                    return False
            if re.search(inccorect_num, st_num4):
                return False
        for ten_times in range(0, len(new_roman_list), 2):
            continuous_num1 = new_roman_list[ten_times]
            inccorect_num3 = 4 * continuous_num1
            if inccorect_num3 in st_num4:
                return False
        for o in range(0, len(new_roman_list)):
            pointer1 = new_roman_list[o]
            value1 = reverse_dict[pointer1]
            for b in range(0, len(new_roman_list)):
                pointer2 = new_roman_list[b]
                value2 = reverse_dict[pointer2]
                if value2 > value1:
                    error1 = pointer1 + pointer2 + pointer1
                    error2 = 2 * pointer1 + pointer2
                    if error1 in st_num4:
                        return False
                    if error2 in st_num4:
                        return False
                if value2 / value1 >= 50:
                    error3 = pointer1 + pointer2
                    if error3 in st_num4:
                        return False
        output_num3 = 0
        check = 0
        for new_roman_num, integers in new_roman_list1:
            while st_num4[check:check + len(new_roman_num)] == new_roman_num:
                output_num3 += integers
                check += len(new_roman_num)
        return output_num3, form_output


if not correct_form(string):
    print('I don\'t get what you want, sorry mate!')
    sys.exit()
else:
    if correct_num(string) is False:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()