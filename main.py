import random
b=0
def main():
  a=input("请输入你的导关次数。>")
  try:
    a=int(a)
  except:
    print("你他妈能不能用数字而不是傻逼的字符串？")
    return
  while 1:
      if random.randint(int(a),int(a)**random.randint(int(a))) == random.randint(int(a),int(a)**114):
        print("导关失败。你几把炸了。")
        break
      print(f"成功导关 {b}")
      b+=1

if __name__ == "__main__":
  main()
