"""
What to do:
1. Remove comments, and run the code.  You will get the same result.
2. welcome_message is a variable.  Change it to a different variable name.
  Then run the code.  What happens?
  ==> NameError: name 'welcome_message' is not defined
3. Learn how to use print()
4. Learn print(type(m))
5. Learn about a string
5. Learn input()
6. Learn f-strings
7. Finally, create your own Mad Libs app in Japanese.

"""

m = """
    'Mad Libs'アプリへようこそ!

    このアプリでは、指示にしたがって、単語を入力します。
    すると、入力した単語でMad Libが生成されます。
"""

print(m)
print(type(m))

place = input("Enter a place: ")
year = input("Enter a year: ")
number = input("Enter a number: ")
adjective = input("形容詞「～な」を入力してください: ")
ing_verb1 = input("動詞「～して」を入力してください: ")
ing_verb2 = input("もう一つ動詞「～して」を入力してください: ")

mad_lib = f"""
    昨年の夏休み、父の車で私たちは {place}に行きました。
    私たちの車は、ドアが{number}ある{year}年製の車で、
    {adjective}エンジンがついています。 私たちは、日の出とともに
    出発しました。私たちは一晩中{ing_verb1}、朝まで{ing_verb2}
    ました!
"""

print("これが、あなたの'Mad Lib'です。")
print(mad_lib)
