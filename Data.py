from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hai {}

Selamat datang di {}

Saya dapat mengekstrak teks dari gambar menggunakan teknologi OCR.

By @AnkiSatya
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
Anda Sangat Membutuhkan Bantuan ?!?!?!?!

Cukup Kirim Gambar Saja.

Note : Anda dapat mengirim sejumlah gambar sekaligus dan itu akan bekerja dengan kecepatan dan akurasi yang sama.

More features in development. Keep track by joining @StarkBots.
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @AnkiSatya

Source Code : [Click Here](https://github.com/StarkBotsIndustries/OCRBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
