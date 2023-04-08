with open('mp3_sounds_split/plasma_split/summarized_minutes.txt', 'r') as f:
    lines = f.readlines()

# 改行を削除した行を含むリストを作成
lines = [line.rstrip('\n') for line in lines]

# 新しいファイルに書き込みます
with open('result.txt', 'w') as f:
    for line in lines:
        f.write(line)
