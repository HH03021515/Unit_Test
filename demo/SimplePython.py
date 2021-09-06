# 一些常用好用的python代码
# 来源：
import streamlit as st
from collections import Counter

def reversed_string():
    """Reversing a string using slicing 反转字符串"""
    my_string = "ABCDE"
    reversed_string = my_string[::-1]
    print(reversed_string)

reversed_string()


def name_string():
    """字符串首字母大写"""
    my_string = "my name is todd combs"
    new_string = my_string.title()
    print(new_string)

name_string()


def research_string():
    """查找字符串的唯一要素，去掉字符串中的重复字符"""
    my_string = "aavvccccddddeee"
    temp_set = set(my_string)
    new_string = ' '.join(temp_set)
    print(new_string)

research_string()


def printlist():
    """输出N次字符串或列表，直接使用*相乘"""
    n = 3
    my_string = "abcd"
    my_list = [1, 2, 3]
    print(my_string*n)
    print(my_list*n)

    # 一个有趣的用例是定义一个具有恒定值的列表，假设为零
    n = 4
    my_list = [0]*n

printlist()


def onebyone_list():
    """列表解析，对列表的每个元素进行操作"""
    original_list = [1, 2, 3, 4]
    new_list = [2*x for x in original_list]
    print(new_list)

onebyone_list()


def change_string():
    """交换变量的值"""
    a = 1
    b = 2
    a, b = b, a
    print(a)
    print(b)

change_string()


def split_string():
    """使用split()方法拆分字符串"""
    string_one = "My name is Todd Combs"
    string_two = "sample/ string_two"
    print(string_one.split())
    print(string_two.split('/'))

split_string()


def join_string():
    """列表元素合并，将字符串列表整合成单个字符串"""
    list_of_string = ['My', 'name', 'is', 'Todd', 'Combs']
    print(','.join(list_of_string))

join_string()


def palindrome_string():
    """检查字符串是否是回文（反转后的文字）"""
    my_string = "abcba"
    if my_string == my_string[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

palindrome_string()


def count_string():
    """统计列表元素中最常出现的元素"""
    my_list = [1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 4, 4]
    count = Counter(my_list)
    print(count)
    print(count[2])
    print(count.most_common(1))

count_string()


def anagrams():
    """查找两个字符串是否为anagrams，
    两个字符串的counter对象相等，则他们就是anagrams"""
    str_one, str_two, str_three = "acbde", "abced", "abcda"
    cnt_one, cnt_two, cnt_three = Counter(str_one), Counter(str_two), Counter(str_three)
    if cnt_one == cnt_two:
        print("1 and 2 is anagrams")
    if cnt_one == cnt_three:
        print("1 and 3 is anagrams")

anagrams()

def try_except():
    """使用try-except-else模块"""
    a, b = 1, 0
    try:
        print(a/b)
    except ZeroDivisionError:
        print("division by zero")
    else:
        print("no exceptions raised")
    finally:
        print("Run this always")

try_except()
