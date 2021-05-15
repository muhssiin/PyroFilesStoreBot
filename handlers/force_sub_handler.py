# (c) @AbirHasan2005

from configs import Config
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Channel](https://t.me/MCubeMediaOfficial).",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join Our Main Channel to use this Bot!** \n**നിങ്ങൾ ഇപ്പോഴും ചേർന്നിട്ടില്ല ☹️, ഈ ബോട്ട് ഉപയോഗിക്കുന്നതിന് ദയവായി ഞങ്ങളുടെ പ്രധാന ചാനലിൽ ചേരുക** \n\nOnly Channel Subscribers can use the Bot \n\n\n നീ ഇപ്പോ ഫയൽ തപ്പി അല്ലേ വന്നത് അതിന് നിനക്ക് ഫയൽ കിട്ടണമെങ്കിൽ ഞങ്ങളുടെ പ്രധാന ചാനലിൽ ജോയിൻ ചെയ്തേപറ്റൂ അതിന് ശേഷം ഒന്നു കൂടി ശ്രമിച്ചു നോക്കൂ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🤖 Join Updates Channel", url=invite_link.invite_link)
                    ],
                    [
                        InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Channel](https://t.me/MCubeMediaOfficial).",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
