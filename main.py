import random
b=0
def main():
  a=input("请输入你的导关次数。>")
  if 122 > ord(a) > 97 and  65 < ord(a) <90:
    while 1:
      if random.randint(int(a),int(a)**random.randint(int(a))) == random.randint(int(a),int(a)**114):
        print("导关失败。你几把炸了。")
        break
      print(f"成功导关 {b}")
      b+=1

if __name__ == "__main__":
  main()
