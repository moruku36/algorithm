#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
簡単なPythonサンプルプログラム
基本的なプログラミング概念のデモンストレーション
"""

import random
from datetime import datetime

def greet_user():
    """ユーザーに挨拶する関数"""
    print("🐍 Pythonサンプルプログラムへようこそ！")
    name = input("あなたの名前を教えてください: ")
    print(f"こんにちは、{name}さん！")
    return name

def calculate_age():
    """年齢計算機能"""
    try:
        birth_year = int(input("生まれた年を入力してください（例：1990）: "))
        current_year = datetime.now().year
        age = current_year - birth_year
        print(f"あなたは約{age}歳ですね！")
        return age
    except ValueError:
        print("正しい年を入力してください。")
        return None

def number_guessing_game():
    """数当てゲーム"""
    print("\n🎯 数当てゲームを始めましょう！")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"1から100までの数字を当ててください。{max_attempts}回まで挑戦できます。")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"予想（{attempts + 1}/{max_attempts}回目）: "))
            attempts += 1
            
            if guess == secret_number:
                print(f"🎉 正解！{attempts}回で当てました！")
                return True
            elif guess < secret_number:
                print("もっと大きい数字です。")
            else:
                print("もっと小さい数字です。")
                
        except ValueError:
            print("数字を入力してください。")
            attempts += 1
    
    print(f"😅 残念！正解は{secret_number}でした。")
    return False

def show_multiplication_table(num):
    """掛け算表を表示"""
    print(f"\n📊 {num}の掛け算表:")
    for i in range(1, 11):
        result = num * i
        print(f"{num} × {i:2d} = {result:3d}")

def analyze_text(text):
    """テキスト分析"""
    print(f"\n📝 テキスト分析結果:")
    print(f"文字数: {len(text)}")
    print(f"単語数: {len(text.split())}")
    print(f"大文字の数: {sum(1 for c in text if c.isupper())}")
    print(f"小文字の数: {sum(1 for c in text if c.islower())}")
    print(f"数字の数: {sum(1 for c in text if c.isdigit())}")

def main():
    """メイン関数"""
    print("=" * 50)
    
    # ユーザー挨拶
    user_name = greet_user()
    
    # 年齢計算
    user_age = calculate_age()
    
    # メニュー表示
    while True:
        print("\n" + "=" * 30)
        print("何をしますか？")
        print("1. 数当てゲーム")
        print("2. 掛け算表を表示")
        print("3. テキスト分析")
        print("4. 今日の運勢")
        print("5. 終了")
        
        choice = input("選択してください (1-5): ")
        
        if choice == "1":
            number_guessing_game()
            
        elif choice == "2":
            try:
                num = int(input("掛け算表を作る数字を入力してください: "))
                show_multiplication_table(num)
            except ValueError:
                print("正しい数字を入力してください。")
                
        elif choice == "3":
            text = input("分析したいテキストを入力してください: ")
            if text.strip():
                analyze_text(text)
            else:
                print("テキストが入力されていません。")
                
        elif choice == "4":
            fortunes = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
            today_fortune = random.choice(fortunes)
            print(f"🔮 {user_name}さんの今日の運勢: {today_fortune}")
            
        elif choice == "5":
            print(f"👋 {user_name}さん、またお会いしましょう！")
            break
            
        else:
            print("1から5の数字を選択してください。")

if __name__ == "__main__":
    main()