from pyrogram import Client
import sqlite3

import config

app = Client('my_account')
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


async def main():
    async with app:
        async for member in app.get_chat_members(config.chat_dzen):
            if member.user.is_self or member.user.is_bot is False:
                user_id = member.user.id
                is_contact = member.user.is_contact
                is_mutual_contact = member.user.is_mutual_contact
                is_deleted = member.user.is_deleted
                is_verified = member.user.is_verified
                is_restricted = member.user.is_restricted
                is_scam = member.user.is_scam
                is_fake = member.user.is_fake
                is_premium = member.user.is_premium
                first_name = member.user.first_name
                last_name = member.user.last_name
                status = member.user.status.value
                last_online_date = member.user.last_online_date
                next_offline_date = member.user.next_offline_date
                username = member.user.username
                language_code = member.user.language_code
                dc_id = member.user.dc_id
                phone_number = member.user.phone_number
                photo = member.user.photo
                if photo is not None:
                    photo = member.user.photo.big_file_id
                restriction = member.user.restrictions
                mention = member.user.mention
                join_date = member.joined_date
                result = cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
                result_l = result.fetchone()
                if result_l is not None:
                    first_name_b = str(result_l[1])
                    last_name = result_l[2]
                    username_b = result_l[3]
                    join_date_b = result_l[5]
                    is_contact_b = result_l[6]
                    is_mutual_contact_b = result_l[7]
                    is_deleted_b = result_l[8]
                    is_verified_b = result_l[9]
                    is_restricted_b = result_l[10]
                    is_scam_b = result_l[11]
                    is_fake_b = result_l[12]
                    is_premium_b = result_l[13]
                    status_b = result_l[14]
                    last_online_date_b = result_l[15]
                    next_offline_date_b = result_l[16]
                    language_code_b = result_l[17]
                    dc_id_b = result_l[18]
                    phone_number_b = result_l[19]
                    photo_b = result_l[20]
                    restriction_b = result_l[21]
                    mention_b = result_l[22]
                    if first_name != first_name_b:
                        cursor.execute('INSERT INTO update_date (user_id, first_name) VALUES (?,?)',
                                       (user_id, first_name))
                else:
                    cursor.execute('INSERT INTO users (user_id, is_contact, is_mutual_contact, is_deleted, '
                                   'is_verified, is_restricted, is_scam, is_fake, is_premium, first_name, last_name, '
                                   'status, last_online_date, next_offline_date, username, language_code, dc_id, '
                                   'phone_number, photo, restriction, mention, join_date) VALUES '
                                   '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                                   (user_id, is_contact, is_mutual_contact, is_deleted, is_verified,
                                    is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status,
                                    last_online_date, next_offline_date, username, language_code, dc_id,
                                    phone_number, photo, restriction, mention, join_date))
        conn.commit()


# async def main():
#     async with app:
#         name = 'Danil'
#         idTwo = '2'
#         cursor.execute('UPDATE users set first_name = ? WHERE id = ?', (name, idTwo))
#         # cursor.execute('INSERT INTO users (user_id, is_contact, is_mutual_contact, is_deleted, is_verified, '
#         #                'is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status, '
#         #                'last_online_date, next_offline_date, username, language_code, dc_id, '
#         #                'phone_number, photo, restriction, mention, join_date) VALUES '
#         #                '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
#         #                (user_id, is_contact, is_mutual_contact, is_deleted, is_verified,
#         #                 is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status,
#         #                 last_online_date, next_offline_date, username, language_code, dc_id,
#         #                 phone_number, photo, restriction, mention, join_date))
#     conn.commit()

app.run(main())
