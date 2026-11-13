import string
from unittest import result


# def is_odd(n):
#     return n % 2 == 1
# print(is_odd(4))
#-----------------------------------------------------
# def is_leapyear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(is_leapyear(2024))
#-----------------------------------------------------
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#         return True
#     print(is_prime(10))
# ----------------------------------------------------
# def printTriangularNumbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total += i
#     print(total)
# printTriangularNumbers(5)
# printTriangularNumbers(10)
#-------------------------------------------------------
# def remove_all(sub,s):
#     return s.replace(sub,"")
#
# print(remove_all("l","hello world"))
#---------------------------------------------------------
# def reverse(String):
#     result=" "
#     for char in String:
#         result =char+result
#     return result
# print(reverse("hello"))
# print(reverse("world"))
#
#
# def reverseSlice(s):
#     return s[::-1]
# print(reverseSlice("hello"))
# print(reverseSlice("world"))
#-------------------------------------------------------
# def substitue(message,key):
#     alphabet = "abcçdefgğhjklmnoöprsştuüvyz"
#     result = ""
#     for ch  in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "eoııoutoskıwpelşepwpwfıoğeroruı"
# print(substitue("hello,world!",key))
# print(substitue("hello,world!",key))

# def remove_dups(s):
#     result = " "
#     for ch in s:
#         if ch in result:
#             result += ch
#     return result
#
# print(remove_dups("hello world"))

