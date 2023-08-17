from pyrogram import Client, filters
import sqlite3

import config

app = Client('my_account')
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


# @app.on_message(filters.text & filters.private)
# async def main(client, message):
#     async for member in app.get_chat_members(config.chat_dzen):
#         if member.user.is_self or member.user.is_bot is False:
#             user_id = member.user.id
#             is_contact = member.user.is_contact
#             is_mutual_contact = member.user.is_mutual_contact
#             is_deleted = member.user.is_deleted
#             is_verified = member.user.is_verified
#             is_restricted = member.user.is_restricted
#             is_scam = member.user.is_scam
#             is_fake = member.user.is_fake
#             is_premium = member.user.is_premium
#             first_name = member.user.first_name
#             last_name = member.user.last_name
#             status = member.user.status.value
#             last_online_date = member.user.last_online_date
#             next_offline_date = member.user.next_offline_date
#             username = member.user.username
#             language_code = member.user.language_code
#             dc_id = member.user.dc_id
#             phone_number = member.user.phone_number
#             photo = member.user.photo
#             if photo is not None:
#                 photo = member.user.photo.small_file_id
#             restriction = member.user.restrictions
#             mention = member.user.mention
#             join_date = member.joined_date
#             cursor.execute('INSERT INTO users (user_id, is_contact, is_mutual_contact, is_deleted, is_verified, '
#                            'is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status, '
#                            'last_online_date, next_offline_date, username, language_code, dc_id, '
#                            'phone_number, photo, restriction, mention, join_date) VALUES '
#                            '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
#                            (user_id, is_contact, is_mutual_contact, is_deleted, is_verified,
#                             is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status,
#                             last_online_date, next_offline_date, username, language_code, dc_id,
#                             phone_number, photo, restriction, mention, join_date))
#     conn.commit()


async def main():
    async with app:
        async for member in app.get_chat_members(config.chat_dzen):
            print(member)
            await app.download_media(member.user.photo.small_file_id)
            await app.download_media(member.user.photo.big_file_id)

        user_id = 515964210
        result = cursor.execute('SELECT photo FROM users WHERE user_id = ?', (user_id,))
        print(result.fetchone()[0])
        # AQADAgADqacxGzL9wB4AEAMAAzL9wB4ABCQXtuS5Qe8GAAQeBA
        await app.send_photo("me", 'AQADAgAD0KcxG8KFdgwAEAMAA8KFdgwABCDyoQrKukmUAAQeBA')

app.run(main())
# print('Launch')
