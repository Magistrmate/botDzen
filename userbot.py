from pyrogram import Client
import sqlite3

import config

app = Client('my_account')
conn = sqlite3.connect('users.db')
cursor = conn.cursor()


def update_base(user_id, column_name, change_parameter, change_parameter_old):
    cursor.execute('INSERT INTO update_data (user_id, ' + column_name + ') VALUES (?,?)',
                   (user_id, change_parameter_old))
    cursor.execute('UPDATE users SET ' + column_name + ' = ? WHERE user_id = ?',
                   (change_parameter, user_id))


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
                    first_name_old = result_l[2]
                    last_name_old = result_l[3]
                    username_old = result_l[4]
                    join_date_old = result_l[5]
                    is_contact_old = result_l[6]
                    is_mutual_contact_old = result_l[7]
                    is_deleted_old = result_l[8]
                    is_verified_old = result_l[9]
                    is_restricted_old = result_l[10]
                    is_scam_old = result_l[11]
                    is_fake_old = result_l[12]
                    is_premium_old = result_l[13]
                    status_old = result_l[14]
                    last_online_date_old = result_l[15]
                    next_offline_date_old = result_l[16]
                    language_code_old = result_l[17]
                    dc_id_old = result_l[18]
                    phone_number_old = result_l[19]
                    photo_old = result_l[20]
                    restriction_old = result_l[21]
                    mention_old = result_l[22]
                    if first_name != first_name_old:
                        update_base(user_id, 'first_name', first_name, first_name_old)
                    if last_name != last_name_old:
                        update_base(user_id, 'last_name', last_name, last_name_old)
                    if username != username_old:
                        update_base(user_id, 'username', username, username_old)
                    if join_date != join_date_old:
                        update_base(user_id, 'join_date', join_date, join_date_old)
                    if is_contact != is_contact_old:
                        update_base(user_id, 'is_contact', is_contact, is_contact_old)
                    if is_mutual_contact != is_mutual_contact_old:
                        update_base(user_id, 'is_mutual_contact', is_mutual_contact, is_mutual_contact_old)
                    if is_deleted != is_deleted_old:
                        update_base(user_id, 'is_deleted', is_deleted, is_deleted_old)
                    if is_verified != is_verified_old:
                        update_base(user_id, 'is_verified', is_verified, is_verified_old)
                    if is_restricted != is_restricted_old:
                        update_base(user_id, 'is_restricted', is_restricted, is_restricted_old)
                    if is_scam != is_scam_old:
                        update_base(user_id, 'is_scam', is_scam, is_scam_old)
                    if is_fake != is_fake_old:
                        update_base(user_id, 'is_fake', is_fake, is_fake_old)
                    if is_premium != is_premium_old:
                        update_base(user_id, 'is_premium', is_premium, is_premium_old)
                    if status != status_old:
                        update_base(user_id, 'status', status, status_old)
                    if last_online_date != last_online_date_old:
                        update_base(user_id, 'last_online_date', last_online_date, last_online_date_old)
                    if next_offline_date != next_offline_date_old:
                        update_base(user_id, 'next_offline_date', next_offline_date, next_offline_date_old)
                    if language_code != language_code_old:
                        update_base(user_id, 'language_code', language_code, language_code_old)
                    if dc_id != dc_id_old:
                        update_base(user_id, 'dc_id', dc_id, dc_id_old)
                    if phone_number != phone_number_old:
                        update_base(user_id, 'phone_number', phone_number, phone_number_old)
                    if photo != photo_old:
                        update_base(user_id, 'photo', photo, photo_old)
                    if restriction != restriction_old:
                        update_base(user_id, 'restriction', restriction, restriction_old)
                    if mention != mention_old:
                        update_base(user_id, 'mention', mention, mention_old)
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
#         #                'phone_number, photo, restriction, mention, join_date VALUES '
#         #                '(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
#         #                (user_id, is_contact, is_mutual_contact, is_deleted, is_verified,
#         #                 is_restricted, is_scam, is_fake, is_premium, first_name, last_name, status,
#         #                 last_online_date, next_offline_date, username, language_code, dc_id,
#         #                 phone_number, photo, restriction, mention, join_date))
#     conn.commit()

app.run(main())
