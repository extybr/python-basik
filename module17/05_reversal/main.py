
text = 'qwhertyuihop'

new_text = [index for index in range(len(text)) if text[index] == 'h']
# print(new_text)
print(text[(new_text[1] - 1):new_text[0]:-1])

# зачет!
