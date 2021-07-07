import random
import urllib.request as urllib2
from builtins import type

import psycopg2
from psycopg2 import Error
from faker import Faker
from collections import defaultdict

# read image
image_url = 'https://images.ctfassets.net/hrltx12pl8hq/7yQR5uJhwEkRfjwMFJ7bUK/dc52a0913e8ff8b5c276177890eb0129/offset_comp_772626-opt.jpg?fit=fill&w=800&h=300'
image_data = urllib2.urlopen(image_url).read()
fake = Faker()
fake_data = defaultdict(list)


flag = False
conn = psycopg2.connect(user="postgres",
                        password="kiki",
                        host="localhost",
                        port="5432",
                        database="myDB")
print("connect to database")


############################################################################################################# for reply
sql = """
 SELECT "comment_id","u_id","v_id"
    from public.comment


            """

cursor = conn.cursor()
cursor.execute(sql)
out6 = cursor.fetchall()
conn.commit()
print(out6)
conn.close()
###############################################################################################################

conn = psycopg2.connect(user="postgres",
                        password="kiki",
                        host="localhost",
                        port="5432",
                        database="myDB")
print("connect to database")


for _ in range(1,19):

    #######################################################################################################################  fake user

    # CREATE EXTENSION pgcrypto; use this just first one
    if flag == False:
    # sql = """
    #
    #         INSERT INTO public."User" ("user_ID" ,username, email ,date_join,photo, password) VALUES
    #          (%(userID)s,%(username)s,%(email)s,%(joinDate)s,%(image)s,crypt('12345', gen_salt('bf')));
    #         """
    # else:
    #     sql = """
    #             INSERT INTO public."User" ("user_ID" ,username, email ,date_join,photo, password) VALUES
    #              (%(userID)s,%(username)s,%(email)s,%(joinDate)s,%(image)s,crypt('12345', gen_salt('bf')));
    #             """
    # flag = True
    # data_insert = {
    #     'userID': _,
    #     'username': fake.user_name(),
    #     'email': fake.email(),
    #     # save image in DB
    #     'joinDate': fake.date(),
    #     'image': psycopg2.Binary(image_data)
    #
    # }





    ########################################################################################################################### fake channel

    #     sql = """
    #
    #             INSERT INTO channel ("channel_ID" ,c_name, date_create ,description,photo, "u_ID") VALUES
    #              (%(c_ID)s,%(name)s,%(date_create)s,%(des)s,%(photo)s,%(u_id)s);
    #             """
    # else:
    #     sql = """
    #                 INSERT INTO channel ("channel_ID" ,c_name, date_create ,description,photo, "u_ID") VALUES
    #                  (%(c_ID)s,%(name)s,%(date_create)s,%(des)s,%(photo)s,%(u_id)s);
    #                 """
    # flag = True
    # Faker.seed(_)
    # data_insert = {
    #     'c_ID': _,
    #     'name': fake.user_name(),
    #    # 'email': fake.email(),
    #     # save image in DB
    #     'date_create': fake.date(),
    #     'des': fake.paragraph(nb_sentences=1),
    #     'photo': psycopg2.Binary(image_data),
    #     'u_id': random.randint(1,19)
    # }
    #
    # cursor = conn.cursor()
    # cursor.execute(sql, data_insert)
    #
    # conn.commit()



    ##############################################################################################################  fake video

    #     sql = """
    #
    #             INSERT INTO video ("video_ID" ,video_name, date_upload ,description,duration, thumbnail,"c_ID","storage_id","p_id") VALUES
    #              (%(v_ID)s,%(name)s,%(date_upload)s,%(des)s,%(duration)s,%(thumb)s,%(c_id)s,%(storage)s,%(p_id)s);
    #             """
    # else:
    #     sql = """
    #                 INSERT INTO video ("video_ID" ,video_name, date_upload ,description,duration, thumbnail,"c_ID","storage_id","p_id") VALUES
    #                   (%(v_ID)s,%(name)s,%(date_upload)s,%(des)s,%(duration)s,%(thumb)s,%(c_id)s,%(storage)s,%(p_id)s);
    #                 """
    # flag = True
    # Faker.seed(_)
    # data_insert = {
    #     'v_ID': _,
    #     'name': fake.user_name(),
    #    # 'email': fake.email(),
    #     # save image in DB
    #     'date_upload': fake.date(),
    #     'des': fake.paragraph(nb_sentences=1),
    #     'duration':fake.time(),
    #     'thumb': psycopg2.Binary(image_data),
    #     'c_id': random.randint(1,19),
    #     'storage':_,
    #     'p_id':random.randint(1,19)
    # }

    #
    #     sql = """
    #
    #             INSERT INTO public."playList" ("playlist_ID" ,playlist_name, acces ,"u_ID") VALUES
    #              (%(p_ID)s,%(name)s,%(acces)s,%(u_id)s);
    #             """
    # else:
    #     sql = """
    #                 INSERT INTO public."playList" ("playlist_ID" ,playlist_name, acces ,"u_ID") VALUES
    #                   (%(p_ID)s,%(name)s,%(acces)s,%(u_id)s);
    #                 """
    # flag = True
    # Faker.seed(_)
    # data_insert = {
    #     'p_ID': _,
    #     'name': fake.name(),
    #     'acces':fake.boolean(),
    #     'u_id': random.randint(1, 19)
    #
    # }




    ######################################################################################################## fake playlist
    # sql = """
    #             INSERT INTO public."playList" ("playlist_ID" ,playlist_name, acces ,"u_ID") VALUES
    #               (%(p_ID)s,%(name)s,%(acces)s,%(u_id)s);
    #             """
    #
    # Faker.seed(_)
    # data_insert = {
    #     'p_ID': _+20,
    #     'name': "watch later",
    #     'acces':False,
    #     'u_id': _
    #
    # }


    ################################################################################################### fake comment

    #     sql = """
    #
    #             INSERT INTO public.comment ("comment_id" ,text ,"u_id","v_id","like_video") VALUES
    #                    (%(co_ID)s,%(text)s,%(u_id)s,%(v_id)s,%(like)s);
    #             """
    # else:
    #     sql = """
    #                 INSERT INTO public.comment ("comment_id" ,text ,"u_id","v_id","like_video") VALUES
    #                   (%(co_ID)s,%(text)s,%(u_id)s,%(v_id)s,%(like)s);
    #                 """
    # flag = True
    # Faker.seed(_)
    # data_insert = {
    #     'co_ID': _,
    #     'text': fake.paragraph(nb_sentences=1),
    #     'u_id': random.randint(1,19),
    #     'v_id':random.randint(1,19),
    #     'like': random.randint(0,2)
    # }



#################################################################################################### fake reply

    #     sql = """
    #
    #             INSERT INTO public.reply ("reply_id" ,text, "u_id",like_comment,"c_ID","v_id") VALUES
    #            (%(r_ID)s,%(text)s,%(u_id)s,%(like)s,%(c_ID)s,%(v_id)s);
    #             """
    # else:

    # sql = """
    #             INSERT INTO public.reply ("reply_id" ,text, "u_id",like_comment,"c_ID","v_id") VALUES
    #               (%(r_ID)s,%(text)s,%(u_id)s,%(like)s,%(c_ID)s,%(v_id)s);
    #             """
    # Faker.seed(_)
    # data_insert = {
    #     'r_ID': _,
    #     'text': fake.paragraph(nb_sentences=1),
    #     'u_id': out6[_][1],
    #     'like':random.randint(0,2),
    #     'c_ID':out6[_][0],
    #     'v_id':out6[_][2]
    # }


    ############################################################################################# fake join channel

    #     sql = """
    #
    #             INSERT INTO public.join_channel ("join_ID" , "u_id","c_id") VALUES
    #            (%(j_ID)s,%(u_id)s,%(c_ID)s);
    #             """
    # else:
    #     sql = """
    #                 INSERT INTO public.join_channel ("join_ID" , "u_id","c_id") VALUES
    #                  (%(j_ID)s,%(u_id)s,%(c_ID)s);
    #                 """
    # flag = True
    # Faker.seed(_)
    # data_insert = {
    #     'j_ID': _,
    #     'u_id': random.randint(1,19),
    #     'c_ID':random.randint(1,19)
    # }


    ##################################################################################################### fake watch
        sql = """

                INSERT INTO public.watch ("watch_id" , "u_id",watched,"v_id") VALUES
               (%(w_ID)s,%(u_id)s,%(watched)s,%(v_ID)s);
                """
    else:
        sql = """
                    INSERT INTO public.watch("watch_id" , "u_id",watched,"v_id") VALUES
                    (%(w_ID)s,%(u_id)s,%(watched)s,%(v_ID)s);
                    """
    flag = True
    Faker.seed(_)
    data_insert = {
        'w_ID': _,
        'u_id': random.randint(1,19),
        'watched': fake.boolean(),
        'v_ID':random.randint(1,19)
    }

    cursor = conn.cursor()
    cursor.execute(sql, data_insert)
    conn.commit()
conn.close()

# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
