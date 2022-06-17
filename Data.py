from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can force your group's users to join a particular chat. 
The chat can be a group or channel. It can be private or public.

Use below buttons to learn more !

Made By [🇮🇳AerodynamicV1 OFFICIAL🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("👁️‍🗨️New Update or More✅", url="https://t.me/AerodynamicV1_UPDATE")],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("•Aboutℹ️", callback_data="about")
        ],
        [InlineKeyboardButton("👁️‍🗨️Store💎", url="https://t.me/AerodynamicV1_Store_TG"),
        InlineKeyboardButton("•Support💬", url="https://t.me/AerodynamicV1_SUPPORT")],
[InlineKeyboardButton("✨Free Promotion🚀", url="https://t.me/AerodynamicV1_Promotion")]
    ]

    # Help Message
    HELP = """
1) Add me as **Admin** to a group.

2) Add me to the particular chat as **Admin** where you want to force your users to join. It can be any group or channel, public or private.

3) Use /fsub chat_id/username to make me functional. Use /id if you need chat id.
Example : `/fsub -1001505616678` or `/forcesubscribe -1001375849192`

4) [Optional] Use /settings to change settings!

5) You are good to go. Leave the rest to me.

     🔰**Available Commands**🔰

/fsub - See current force subscribe chat
/fsub Or /forcesubscribe chat_id/username - Force users to join the particular chat
/settings - Change Group Settings
/id - Get the chat id of any group or channel
/about - About The Bot
/help - This Message
/start - Start the Bot

Powered By [🇮🇳AerodynamicV1~Update🇮🇳](https://t.me/AerodynamicV1_UPDATE)
    """

    # About Message
    ABOUT = """
**About This Bot** 

A telegram force subscribing bot Made By [🇮🇳AerodynamicV1 OFFICIAL🇮🇳](https://t.me/AerodynamicV1_OFFICIAL)

Source Code : [Click Here](https://github.com/AerodynamicV1Botz/Force-Subscribe-Bot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

[New Update or More✅](https://t.me/AerodynamicV1_UPDATE) : [Free Promotion🚀](https://t.me/AerodynamicV1_Promotion)

Developer : @AerodynamicV1_OFFICIAL
    """
