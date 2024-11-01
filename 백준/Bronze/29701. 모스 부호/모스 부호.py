# a = int(input)
# b = input
# c = 0
# string = ''
# dict = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     "1": ".----",
#     "2": "..---",
#     "3": "...--",
#     "4": "....-",
#     "5": ".....",
#     "6": "-....",
#     "7": "--...",
#     "8": "---..",
#     "9": "----.",
#     "0": "-----",
#     ",": "--..--",
#     ".": ".-.-.-",
#     "?": "..--..",
#     ":": "---...",
#     "-": "-....-",
#     "@": ".--.-.",
# }
# for i in b:
#     if i == ' ' :
#         string += b[c:i].dict.keys()
#         c = i


# 모스 부호 딕셔너리
morse_code_dict = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0",
    "--..--": ",",
    ".-.-.-": ".",
    "..--..": "?",
    "---...": ":",
    "-....-": "-",
    ".--.-.": "@",
}

# 첫째 줄 입력: 문자열의 길이 (사용하지 않지만 입력 받기)
N = int(input())

# 둘째 줄 입력: 모스 부호 메시지
morse_input = input()

# 모스 부호 메시지를 공백으로 분리 -> 배열을 만든거임(문자형을 가지는)
morse_sequences = morse_input.split()

# 모스 부호를 해독하여 문자열로 변환
decoded_string = ""
for sequence in morse_sequences:
    if sequence in morse_code_dict:  # 각 모스 부호 시퀀스를 딕셔너리에서 찾아 해독
        decoded_string += morse_code_dict[sequence]

# 해독된 문자열 출력
print(decoded_string)