from pyrogram import Client, filters
import sqlite3
import config

app = Client('my_account')
conn = sqlite3.connect('botDzenDataBase.db')
cursor = conn.cursor()


def update_base(user_id, column_name, change_parameter, change_parameter_old):
    cursor.execute('INSERT INTO update_data (user_id, ' + column_name + ') VALUES (?,?)',
                   (user_id, change_parameter_old))
    cursor.execute('UPDATE users SET ' + column_name + ' = ? WHERE user_id = ?',
                   (change_parameter, user_id))


@app.on_message(filters.chat(config.chat_dzen))
async def record(client, message):
    print(client)
    member_list = []
    async for member in app.get_chat_members(config.chat_dzen):
        member_list.append(member.user.id)
        user_id = member.user.id
        is_deleted = member.user.is_deleted
        if is_deleted:
            cursor.execute('INSERT INTO delete_users SELECT * FROM users WHERE user_id = ?',
                           (user_id,))
            cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
        elif member.user.is_self or member.user.is_bot is False:
            is_contact = member.user.is_contact
            is_mutual_contact = member.user.is_mutual_contact
            is_verified = member.user.is_verified
            is_restricted = member.user.is_restricted
            is_scam = member.user.is_scam
            is_fake = member.user.is_fake
            is_premium = member.user.is_premium
            first_name = member.user.first_name
            last_name = member.user.last_name
            status = member.user.status.value
            last_online_date = str(member.user.last_online_date)
            next_offline_date = str(member.user.next_offline_date)
            username = member.user.username
            language_code = member.user.language_code
            dc_id = member.user.dc_id
            phone_number = member.user.phone_number
            photo = member.user.photo
            if photo is not None:
                photo = member.user.photo.big_file_id
            restriction = member.user.restrictions
            mention = member.user.mention
            join_date = str(member.joined_date)
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
                if last_online_date != last_online_date_old and (last_online_date
                                                                 and last_online_date_old) != 'None':
                    update_base(user_id, 'last_online_date', last_online_date, last_online_date_old)
                if next_offline_date != next_offline_date_old and (next_offline_date and
                                                                   next_offline_date_old) != 'None':
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
    user_id = message.from_user.id
    if message.reply_to_top_message_id is None:
        theme_id = message.reply_to_message_id
    else:
        theme_id = message.reply_to_top_message_id
    match theme_id:
        case 800:
            theme_name = 'Помощь коллеге'
        case 226:
            theme_name = 'Просьбы о помощи'
        case 1:
            theme_name = 'Уведомления'
        case 9:
            theme_name = 'Отчеты о проделанной работе'
        case 6:
            theme_name = 'Светские беседы'
        case 4:
            theme_name = 'Ссылки на каналы'
        case _:
            theme_name = ''
    message_id = message.id
    message_media_group_id = message.media_group_id
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
    cursor.execute('INSERT INTO messages (user_id, theme_name, message_id, message_media_group_id, '
                   'message_text, message_media, media_link, message_entities, date) '
                   'VALUES (?,?,?,?,?,?,?,?,?)', (user_id, theme_name, message_id,
                                                  message_media_group_id, message_text, message_media,
                                                  media_link, message_entities, date,))
    cursor.execute('SELECT user_id FROM users')
    result = cursor.fetchall()
    for user_id in result:
        member_user = False
        for member in member_list:
            if user_id[0] == member:
                member_user = True
        if member_user is False:
            cursor.execute('INSERT INTO leave_users SELECT * FROM users WHERE user_id = ?',
                           (user_id[0],))
            cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id[0],))
    conn.commit()


app.run()
