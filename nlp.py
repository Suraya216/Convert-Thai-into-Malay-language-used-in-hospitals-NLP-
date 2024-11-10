
# from pythainlp import word_tokenize
# from pythainlp.util import dict_trie

# with open('corpus.txt', 'r', encoding='utf-8') as dictionary_file:
#     dictionary = dictionary_file.readlines()
#     print(dictionary)

# with open('มลายูถิ่น.txt', 'r', encoding='utf-8') as dictionary_file:
#     dictionary = dictionary_file.readlines()
#     print(dictionary)



# PATH_TO_CUSTOM_DICTIONARY = "corpus.txt"
# melayu = dict_trie(dict_source=PATH_TO_CUSTOM_DICTIONARY)
# text = "ฉันปวดท้อง และอาเจียน"

# tok = word_tokenize(text,custom_dict=melayu)
# print(tok)

# text = "ฉันปวดท้อง และอาเจียน"

# # ตัดคำ
# tokens = word_tokenize(text)


# print("คำที่ตัด:", tok)

# # # ดึงความหมายจากพจนานุกรม
# meaning = {}
# for line in dictionary:
#      word, mean = line.strip().split(':')
# meaning[word] = mean

# # # แสดงความหมายของคำที่ตัด
# for token in tok:
#    if token in meaning:        print(f"คำ '{token}' หมายถึง '{meaning[token]}'")
#    else:
#     print(f"ไม่พบความหมายของคำ '{token}' ในพจนานุกรม")
import pythainlp
from pythainlp import word_tokenize
from pythainlp.util import dict_trie

# อ่านไฟล์ corpus.txt เพื่อใช้เป็นพจนานุกรม
with open('corpus.txt', 'r', encoding='utf-8') as dictionary_file:
    corpus = dictionary_file.readlines()

# สร้าง Trie จาก corpus.txt
corpus_trie = dict_trie(dict_source=corpus)

# ประโยคภาษาไทยที่ต้องการตัดคำ
text = "ปัสสาวะลำบาก นอนไม่หลับ"

# ตัดคำโดยใช้ Trie จาก corpus.txt
tokens = word_tokenize(text, custom_dict=corpus_trie)

print("คำที่ตัด:", tokens)

# ดึงความหมายจากพจนานุกรมมลายูถิ่น.txt
with open('มลายูถิ่น.txt', 'r', encoding='utf-8') as melayu_dictionary_file:
    melayu_dictionary = melayu_dictionary_file.readlines()

melayu_meaning = {}
for line in melayu_dictionary:
    word, meaning = line.strip().split(':', 1)
    melayu_meaning[word] = meaning

# แสดงความหมายของคำที่ตัด
# for text in tokens:
#     if text in melayu_meaning:
#         print(f"คำ '{text}' หมายถึง '{melayu_meaning[text]}'")
#     else:
#         print(f"ไม่พบความหมายของคำ '{text}' ในพจนานุกรมมลายู")

# ประโยคที่เป็นผลลัพธ์หลังจากตัดคำ
result_sentence = ""

for text in tokens:
    if text in melayu_meaning:
        result_sentence += melayu_meaning[text]
    else:
        result_sentence += text  # ใช้คำตั้งต้นถ้าไม่มีความหมาย

# แสดงประโยคที่เป็นผลลัพธ์หลังจากประกอบคำ
print("ประโยคมลายูถิ่น:", result_sentence)       








