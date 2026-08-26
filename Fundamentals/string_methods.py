txt = "im from iran"
print(txt)
print(txt.capitalize())  # capitalize

txt2 = "iM frOm iRaN"
print(txt2)
print(txt2.casefold())  # casefold

print(txt2.find("f"))  # find
print(txt2.find("frOm"))
print(txt2.index("f"))
# print(txt2.index("from")) error

# format
txt3 = "my name is {} and im from {}"
print(txt3.format("alireza", "iran"))

txt4 = "         hi      there     haha        "
print(txt4)
print(txt4.strip())  # strip:حذف اسپیس های اضافی ابتدا و انتها


txt = "im from iran and i love my country"
print(txt)
print(txt.title())  # title


txt = "hellO i wAnt sHoW yoU someThing"
print(txt)
print(txt.upper())  # upper
print(txt.lower())  # lower

print(len(txt))  # len
