English to Indian Languages Translator
A simple translator using Google Translate API (free version)
Supports: Hindi, Bengali, Tamil, Telugu, Marathi, Gujarati, Kannada, Malayalam, Punjabi, Urdu
"""
from googletrans import Translator, LANGUAGES
import sys
import asyncio

translator = Translator()

# Dictionary of Indian languages with their codes
INDIAN_LANGUAGES = {
    '1': ('hi','Hindi'),
    '2': ('bn','Bengali'),
    '3': ('ta','Tamil'),
    '4': ('te','Telugu'),
    '5': ('mr','Marathi'),
    '6': ('gu','Gujarati'),
    '7': ('kn','Kannada'),
    '8': ('ml','Malayalam'),
    '9': ('pa','Punjabi'),
    '10': ('ur','Urdu')
}


def display_menu():
    print("\n"+"="*50)
    print(" ENGLISH to and from INDIAN LANGUAGES TRANSLATOR")
    print("="*50)
    print("\nSelect target language:")
    print("-"*50)
    for key,(code, name) in INDIAN_LANGUAGES.items():
        print(f"{key}. {name}")
    print("-"*50)
    print("0. Exit")
    print()


async def translate_text(text, target_lang_code, source_lang='en'):
    try:
        result = await translator.translate(text, src=source_lang, dest=target_lang_code)
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"


async def detect_language(text):
    try:
        detected = await translator.detect(text)
        lang_name = LANGUAGES.get(detected.lang, 'Unknown')
        return detected.lang, lang_name
    except:
        return None, None
async def main():
    print("\n Welcome to the Language Translator! :)")

    while True:
        display_menu()
        choice=input("Enter your choice (0-10):").strip()

        if choice=='0':
            print("\n Thank you for using the translator! Goodbye!")
            sys.exit()

        if choice not in INDIAN_LANGUAGES:
            print("\n Invalid choice! Please select a number from 0-10.")
            continue

        target_code,target_name=INDIAN_LANGUAGES[choice]

        # translation direction
        print(f"\n Selected Language: {target_name}")
        print("\nTranslation Direction:")
        print(f"1. English to {target_name}")
        print(f"2. {target_name} to English")

        direction = input("\nChoose direction (1 or 2):").strip()
        if direction not in ['1', '2']:
            print("\n Invalid direction! Please choose 1 or 2.")
            continue

        # text to translate
        print("\n"+"-"*50)
        text_input=input("Enter text to translate (or 'back' to return): ")
        if text_input.lower()=='back':
            continue
        if not text_input:
            print("\n Please enter some text to translate!")
            continue

        print("\n Translating...")

        if direction=='1':
            # English to Indian language
            translated=await translate_text(text_input, target_code,'en')
            print("\n"+"="*50)
            print(f"Original (English): {text_input}")
            print(f"Translated ({target_name}): {translated}")
            print("="*50)
        else:
            # Indian language to English
            translated = await translate_text(text_input,'en', target_code)
            print("\n"+"="*50)
            print(f"Original ({target_name}): {text_input}")
            print(f"Translated (English): {translated}")
            print("="*50)

        # Option to continue or exit
        print("\n")
        continue_choice=input("Press Enter to continue or type 'exit' to quit: ").strip()
        if continue_choice.lower()=='exit':
            print("\n Thank you for using the translator! Goodbye!")
            break


# Run the translator
if __name__=="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\n Program interrupted. Goodbye!")
        sys.exit()
    except Exception as e:
        print(f"\n An unexpected error occurred: {str(e)}")
        sys.exit(1)
