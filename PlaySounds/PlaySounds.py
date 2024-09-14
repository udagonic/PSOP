import pygame
import sys
import os
import keyboard

# Pygameを初期化
pygame.init()

# サウンドファイルが格納されているディレクトリのパス
sounds_directory = os.path.join('C:\\Users\\yuusu\\Desktop\\ゆきちん\\sounds')

# サウンドファイルとキーコードのマッピング
sound_mapping = {
    'a': 'maou_se_inst_piano2_1do.mp3',
    'b': '泡がはじける.mp3',
    'c': 'ドアチャイム1.mp3',
    'd': 'ドアを閉める2.mp3',
    'e': 'maou_se_inst_piano2_5so.mp3',
    'f': '魚を釣り上げる.mp3',
    'g': '歓声.mp3',
    'h': 'ボヨン.mp3',
    'i': 'maou_se_inst_piano2_2re.mp3',
    'j': 'パフ.mp3',
    'k': 'ピコッ.mp3',
    'l': 'DJのスクラッチ1.mp3',
    'm': 'シーン切り替え2.mp3',
    'n': '小鼓（こつづみ）.mp3',
    'o': 'maou_se_inst_piano2_6ra.mp3',
    'p': '拍子木2.mp3',
    'q': '宝箱を開ける.mp3',
    'r': '教会の鐘1.mp3',
    's': 'クイズ早押しボタン2.mp3',
    't': '驚く.mp3',
    'u': 'maou_se_inst_piano2_3mi.mp3',
    'v': '目が点になる.mp3',
    'w': 'ショック5.mp3',
    'x': 'ニュッ3.mp3',
    'y': 'ニュッ2.mp3',
    'z': 'ニュッ1.mp3',
    '0': '「0（ゼロ）」.mp3',
    '1': '「1」.mp3',
    '2': '「2」.mp3',
    '3': '「3」.mp3',
    '4': '「4（よん）」.mp3',
    '5': '「5」.mp3',
    '6': '「6」.mp3',
    '7': '「7」.mp3',
    '8': '「8」.mp3',
    '9': '「9」.mp3',
    '-': '間抜け1.mp3',
    '=': '間抜け2.mp3',
    '[': '間抜け3.mp3',
    ']': 'ピューンと逃げる.mp3',
    ';': 'ヒューンと落下.mp3',
    '\'': '目をパチパチ.mp3',
    '\\': 'ヒーローの決めポーズ.mp3',
    '`': 'ジャンプ.mp3',
    ',': 'グサッ1.mp3',
    '.': '超高速ダッシュ.mp3',
    '/': '可愛い動作.mp3',
    'shift': '可愛く座る.mp3',
    'ctrl': 'スイッチを押す.mp3',
    'alt': '靴でブレーキ.mp3',
    'space': 'アヒルが大笑い.mp3'
}

# サウンドの初期化
pygame.mixer.init()

# サウンドを読み込む関数
def load_sound(file):
    file_path = os.path.join(sounds_directory, file)
    try:
        return pygame.mixer.Sound(file_path)
    except pygame.error as e:
        print(f"Error loading sound file {file_path}: {e}")
        return None

# サウンドオブジェクトを作成
sounds = {key: load_sound(file) for key, file in sound_mapping.items()}

# キーが押されたときにサウンドを再生するコールバック関数
def play_sound(event):
    key = event.name
    if key in sounds:
        sound = sounds[key]
        if sound:
            sound.play()

# キーイベントにコールバック関数を登録
for key in sound_mapping.keys():
    keyboard.on_press_key(key, play_sound)

# メインループ
try:
    while True:
        pygame.time.wait(100)  # 少し待機
except KeyboardInterrupt:
    pass
finally:
    pygame.quit()
    sys.exit()

# ターミナルでスクリプトを終了しないようにする
print("Press Enter to exit...")
input()
