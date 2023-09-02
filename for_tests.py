from pyrogram import Client
import sqlite3
import config
app = Client("my_account")
conn = sqlite3.connect('botDzenDataBase.db')
cursor = conn.cursor()


async def main():
    async with (app):
        async for message in app.get_chat_history(config.chat_group):
            if message.reply_to_message_id is not None:
                user_id = message.from_user.id
                if message.reply_to_top_message_id is None:
                    theme_id = message.reply_to_message_id
                else:
                    theme_id = message.reply_to_top_message_id
                message_id = message.media_group_id
                message_text = message.text
                message_entities = ''
                if message.entities is not None:
                    message_entities = message.entities[0].type.name
                    message_text = message.text.markdown
                if message_text is None:
                    message_media = message.media.value
                    message_text = message.caption
                    if message.caption_entities is not None:
                        message_entities = message.caption_entities[0].type.name
                        message_text = message.caption.markdown
                else:
                    message_media = ''
                match message_media:
                    case 'photo':
                        media_link = message.photo.file_id
                    case 'voice':
                        media_link = message.voice.file_id
                    case 'video':
                        media_link = message.video.file_id
                    case 'document':
                        media_link = message.document.file_id
                    case 'poll':
                        media_link = message.poll.id
                    case _:
                        media_link = ''
                date = message.date
                cursor.execute('INSERT INTO messages (user_id, theme_name, message_id, message_text, message_media,'
                               'media_link, message_entities, date) VALUES (?,?,?,?,?,?,?,?)',
                               (user_id, theme_id, message_id, message_text, message_media, media_link,
                                message_entities, date,))
    conn.commit()


app.run(main())
