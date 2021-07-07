import urllib.request as urllib2
import psycopg2

conn = psycopg2.connect(user="postgres",
                        password="kiki",
                        host="localhost",
                        port="5432",
                        database="myDB")
print("connect to database")

create_channel_dict = {}
upload_video_dict = {}
remove_video_dict = {}
watch_video_dict = {}
comment_vid = {}
reply = {}
remove_comment = {}
create_playlist = {}
insertTo_playlist_dict = {}
removeFrom_playlist_dict = {}
join_channel = {}
Leave_channel = {}
NumWatched_comment = {}
NumLike_comment = {}
NumComment_comment = {}
remove_channel = {}
NumJoin = {}
removeVid = {}
get_reply = {}
search_video = {}
search_channel = {}
search_playlist = {}
remove_playlist_dict = {}

storage = 20
user_id = int(input("Enter your user id: "))
print("x = 2 -> Create Channel")
print("x = 3 -> upload video into channel")
print("x = 4 -> remove video from channel")
print("x = 5 -> watch video")
print("x = 6 -> Comment to video")
print("x = 7 -> replay to comment")
print("x = 8 -> remove comment")
print("x = 9 -> Create Playlist")
print("x = 10 -> Insert into Playlist")
print("x = 11 -> remove from playlist")
print("x = 12 -> Join channel")
print("x = 13 -> Leave channel")
print("x = 14 -> Number of watched")
print("x = 15 -> Number of likes/dislikes")
print("x = 16 -> Number of comments")
print("x = 17 -> Number of joined users")
print("x = 18 -> get replies of a video (replies of its comments)")
print("x = 19 -> remove channel")
print("x = 20 -> remove playlist")
print("x = 21 -> Search according to video name")
print("x = 22 -> Search according to channel name")
print("x = 23 -> Search according to playlist name")

print("x = 0 -> exit()")

x = int(input("Select between operations: "))
while (x):
    if x == 2:
        print("Create Channel")
        # print("please input channel_id, channel_name, date_create, description, user_id, photo_url: ")
        for i in range(4):
            while i == 0:
                print("please enter channel_name: ")
                k = str(input())
                if k == '#':
                    print("Name of channel cannot be Null!")
                    i = 0
                else:
                    create_channel_dict['channel_name'] = k
                    break

            while i == 1:
                print("please enter date_create: ")
                k = str(input())
                if k == '#':
                    print("date_create of channel cannot be Null!")
                    i = 1
                else:
                    create_channel_dict['date_create'] = k
                    break

            if i == 2:
                print("please enter description: ")
                k = str(input())
                create_channel_dict['description'] = k

            if i == 3:
                print("please enter photo_url: ")
                k = str(input())
                if k == '#':
                    create_channel_dict[
                        'photo_url'] = 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png'
                else:
                    create_channel_dict['photo_url'] = k

        ################################### create channel

        other1 = """
        	SELECT MAX("channel_ID")  
                from public.channel

        """
        cursor = conn.cursor()
        cursor.execute(other1)
        out1 = cursor.fetchall()
        conn.commit()

        sql1 = """
             INSERT INTO public.channel(
          "channel_ID", c_name, date_create, description, "u_ID", photo)
          VALUES 
             (%(channel_ID)s,%(c_name)s,%(date_create)s,%(description)s,%(u_ID)s,%(photo)s);
        """
        image_data = psycopg2.Binary(urllib2.urlopen(create_channel_dict['photo_url']).read())

        s1 = {
            'channel_ID': out1[0][0] + 1,
            'c_name': create_channel_dict['channel_name'],
            'date_create': create_channel_dict['date_create'],
            'description': create_channel_dict['description'],
            'u_ID': user_id,
            'photo': image_data
        }

        cursor = conn.cursor()
        cursor.execute(sql1, s1)
        # out=cursor.fetchall()
        conn.commit()

        #####################################################

        x = int(input("Select between operations: "))
    elif x == 3:
        print("upload video into channel")

        upload_video_dict['video_id'] = 'missed'
        # print(" "video_ID", video_name, date_upload, description, duration, "c_ID", storage_id, thumbnail, p_id ")
        for i in range(6):
            while i == 0:
                print("please enter video_name: ")
                k = str(input())
                if k == '#':
                    print("Name of video cannot be Null!")
                    i = 0
                else:
                    upload_video_dict['video_name'] = k
                    break

            while i == 1:
                print("please enter date_upload: ")
                k = str(input())
                if k == '#':
                    print("date_upload of video cannot be Null!")
                    i = 1
                else:
                    upload_video_dict['date_upload'] = k
                    break

            if i == 2:
                print("please enter description: ")
                k = str(input())
                upload_video_dict['description'] = k

            if i == 3:
                print("please enter thumbnail: ")
                k = str(input())
                if k == '#':
                    upload_video_dict[
                        'thumbnail_url'] = 'https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png'
                else:
                    upload_video_dict['thumbnail_url'] = k

            while i == 4:
                print("please enter channel ID: ")
                k = str(input())
                if k == '#':
                    print("channel ID of video cannot be Null!")
                    i = 4
                else:
                    upload_video_dict['c_ID'] = k
                    break
            while i == 5:
                print("please enter  duration: ")
                k = str(input())
                if k == '#':
                    print("duration of video cannot be Null!")
                    i = 5
                else:
                    upload_video_dict['duration'] = k
                    break

            # while i == 5:
            #     print("please enter storage_id: ")
            #     k = str(input())
            #     if k == '#':
            #         print("storage_id of video cannot be Null!")
            #         i = 1
            #     else:
            #         upload_video_dict['storage_id'] = k
            #         break

            if i == 5:
                print("please enter playlist id: ")
                k = str(input())
                upload_video_dict['playlist_id'] = k

        #########################  upload video
        other2 = """
        	SELECT "channel_ID"
                from public.channel
                WHERE  "channel_ID"=%(ci)s;
        """
        o2 = {
            'ci': upload_video_dict['c_ID']
        }
        cursor = conn.cursor()
        cursor.execute(other2, o2)
        out2 = cursor.fetchall()
        conn.commit()

        if out2 is None:
            print("channel id is not recognized!")
            exit()

        other3 = """
        	SELECT MAX("video_ID")  
                from public.video

        """
        cursor = conn.cursor()
        cursor.execute(other3)
        out3 = cursor.fetchall()
        conn.commit()

        sql2 = """
        INSERT INTO public.video(
          "video_ID", video_name, date_upload, description, duration, "c_ID", storage_id,thumbnail, p_id)
          VALUES   (%(video_ID)s,%(video_name)s,%(date_upload)s,%(description)s,%(duration)s,%(c_ID)s,%(storage_id)s,%(thumbnail)s,%(p_id)s);

        """

        image_data = urllib2.urlopen(upload_video_dict['thumbnail_url']).read()

        s2 = {
            'video_ID': out3[0][0] + 1,
            'video_name': upload_video_dict['video_name'],
            'date_upload': upload_video_dict['date_upload'],
            'description': upload_video_dict['description'],
            'duration': upload_video_dict['duration'],
            'c_ID': upload_video_dict['c_ID'],
            'storage_id': storage,
            'thumbnail': psycopg2.Binary(image_data),
            'p_id': None
        }
        cursor = conn.cursor()
        cursor.execute(sql2, s2)
        # out=cursor.fetchall()
        conn.commit()
        storage += 1
        ######################################

        x = int(input("Select between operations: "))
    elif x == 4:
        print("remove video from channel")

        # remove_video_dict['channel_id'] = 'missed'
        other4 = """
            	SELECT distinct "video_ID", video_name
                    from public.video

            """
        cursor = conn.cursor()
        cursor.execute(other4)
        out4 = cursor.fetchall()
        conn.commit()
        for d in range(len(out4)):
            print(out4[d])
        k = int(input("enter video id  "))
        remove_video_dict['video id'] = k

        ########################  remove video

        sd = """
                      DELETE FROM public.reply 
                        WHERE "v_id"=%(v_id)s

                      """
        so = {
            'v_id': remove_video_dict['video id']
        }

        cursor = conn.cursor()
        cursor.execute(sd, so)
        # outpu=cursor.fetchall()
        conn.commit()

        sq3 = """
                DELETE FROM public.comment 
                  WHERE "v_id"=%(v_id)s

                """
        ss3 = {
            'v_id': remove_video_dict['video id']
        }

        cursor = conn.cursor()
        cursor.execute(sq3, ss3)
        # outpu=cursor.fetchall()
        conn.commit()

        sql3 = """
        DELETE FROM public.video
          WHERE "video_ID"=%(v_id)s;

        """
        s3 = {
            'v_id': remove_video_dict['video id']
        }

        cursor = conn.cursor()
        cursor.execute(sql3, s3)
        # out=cursor.fetchall()
        conn.commit()

        #################################

        x = int(input("Select between operations: "))

    elif x == 5:
        print("watch video")

        watch_video_dict['watch_id'] = 'missed'
        # print("please input watch_id, u_id, watched, v_id: ")
        print("Enter the video id: ")
        k = int(input())
        watch_video_dict['v_id'] = k
        watch_video_dict['watched'] = True

        ############################  watch
        other4 = """
        	SELECT MAX("watch_id")  
                from public.watch

        """
        cursor = conn.cursor()
        cursor.execute(other4)
        out4 = cursor.fetchall()
        conn.commit()

        sql4 = """

        INSERT INTO public.watch(
          "watch_id", u_id, watched, v_id)
          VALUES (%(watch_id)s,%(u_id)s,%(watched)s,%(v_id)s);


        """

        s4 = {
            'watch_id': out4[0][0] + 1,
            'u_id': user_id,
            'watched': watch_video_dict['watched'],
            'v_id': watch_video_dict['v_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql4, s4)
        # out=cursor.fetchall()
        conn.commit()
        ##########################################

        x = int(input("Select between operations: "))
    elif x == 6:
        print("Comment to video")

        # comment_id, text, u_id, v_id, like_video
        comment_vid['comment_id'] = 'missed'
        for i in range(3):
            while i == 0:
                print("Please enter the video id: ")
                k = int(input())
                if k == '#':
                    print("Id of video cannot be Null!")
                    i = 0
                else:
                    comment_vid['v_id'] = k
                    break
            if i == 1:
                print("Please enter the text of comment: ")
                k = str(input())
                comment_vid['text'] = k

            while i == 2:
                print("Do you want to like video? enter 1 - or dislike? enter 2 - otherwise? enter 0: ")
                k = int(input())
                if k == '#':
                    print("cannot be Null!")
                    i = 2
                else:
                    comment_vid['like_video'] = k
                    break

        ################################   comment
        other5 = """
        	SELECT MAX("comment_id")  
                from public.comment

        """
        cursor = conn.cursor()
        cursor.execute(other5)
        out5 = cursor.fetchall()
        conn.commit()

        sql5 = """
        INSERT INTO public.comment(
          comment_id, text, u_id, v_id, like_video)

            VALUES (%(comment_id)s,%(text)s,%(u_id)s,%(v_id)s,%(like_video)s);
        """

        s5 = {
            'comment_id': out5[0][0] + 1,
            'text': comment_vid['text'],
            'u_id': user_id,
            'v_id': comment_vid['v_id'],
            'like_video': comment_vid['like_video']
        }

        cursor = conn.cursor()
        cursor.execute(sql5, s5)
        # out=cursor.fetchall()
        conn.commit()

        ################################################

        x = int(input("Select between operations: "))

    elif x == 7:
        print("replay to comment")
        # reply_id, text, u_id, like_comment, "co_ID"
        for i in range(3):
            while i == 0:
                print("Please enter the comment id: ")
                k = int(input())
                if k == '#':
                    print("Id of comment cannot be Null!")
                    i = 0
                else:
                    reply['co_ID'] = k
                    break
            if i == 1:
                print("Please enter the text of comment: ")
                k = str(input())
                reply['text'] = k

            while i == 2:
                print("Do you want to like comment? enter 1 - or dislike? enter 2 - otherwise? enter 0: ")
                k = int(input())
                if k == '#':
                    print("cannot be Null!")
                    i = 2
                else:
                    reply['like_comment'] = k
                    break

        ######################### reply

        other6 = """
        	SELECT MAX("reply_id")
                from public.reply

        """
        cursor = conn.cursor()
        cursor.execute(other6)
        out6 = cursor.fetchall()
        conn.commit()

        oth = """
         	SELECT "v_id"  
                 from public.comment
                 WHERE "comment_id" = %(c_ID)s;

         """
        go = {
            'c_ID': reply['co_ID']
        }

        cursor = conn.cursor()
        cursor.execute(oth, go)
        outtt = cursor.fetchall()
        conn.commit()

        sql6 = """
        INSERT INTO public.reply(
          "reply_id", text, u_id, like_comment, "c_ID","v_id")
          VALUES
             (%(reply_id)s,%(text)s,%(u_id)s,%(like_comment)s,%(c_ID)s,%(v_id)s);
        """

        s6 = {
            'reply_id': out6[0][0] + 1,
            'text': reply['text'],
            'u_id': user_id,
            'like_comment': reply['like_comment'],
            'c_ID': reply['co_ID'],
            'v_id': outtt[0][0]
        }

        cursor = conn.cursor()
        cursor.execute(sql6, s6)
        # out=cursor.fetchall()
        conn.commit()

        #################################

        x = int(input("Select between operations: "))
    elif x == 8:
        print("remove comment")

        remove_comment["comment_id"] = 'missed'
        print("Please enter the video id: ")
        k = int(input())
        remove_comment['v_id'] = k

        ######################## remove comment

        hello = """
        SELECT COUNT("comment_id")
         FROM public.comment
          WHERE "v_id"=%(v_id)s
            and "u_id"=%(u_id)s;
        """

        he7 = {
            'v_id': remove_comment['v_id'],
            'u_id': user_id
        }

        cursor = conn.cursor()
        cursor.execute(hello, he7)
        helloout = cursor.fetchall()
        conn.commit()

        if helloout[0][0] == 0:
            print("You dont have comment for this video!")
            exit()

        bye = """
        SELECT "comment_id"
         FROM public.comment
          WHERE "v_id"=%(v_id)s
            and "u_id"=%(u_id)s;
        """

        bye7 = {
            'v_id': remove_comment['v_id'],
            'u_id': user_id
        }

        cursor = conn.cursor()
        cursor.execute(bye, bye7)
        byeout = cursor.fetchall()
        conn.commit()

        eight = """
        UPDATE public.reply
        	SET   "c_ID"=null 
        	WHERE "v_id"=%(v_id)s
        	     and "u_id"=%(u_id)s
        	     and  "c_ID"=%(C_ID)s;

        """
        eight8 = {
            'v_id': remove_comment['v_id'],
            'u_id': user_id,
            'C_ID': byeout[0][0]
        }

        cursor = conn.cursor()
        cursor.execute(eight, eight8)
        # out=cursor.fetchall()
        conn.commit()

        sql7 = """
        DELETE FROM public.comment
          WHERE "v_id"=%(v_id)s
            and "u_id"=%(u_id)s;


        """

        s7 = {
            'v_id': remove_comment['v_id'],
            'u_id': user_id
        }

        cursor = conn.cursor()
        cursor.execute(sql7, s7)
        # out=cursor.fetchall()
        conn.commit()
        ######################################

        x = int(input("Select between operations: "))
    elif x == 9:
        print("Create Playlist")
        # "playlist_ID", playlist_name, acces, "u_ID"

        create_playlist['playlist_ID'] = 'missed'
        for i in range(2):
            while i == 0:
                print("Enter the name of playlist: ")
                k = str(input())
                if k == '#':
                    print("cannot be Null!")
                    i = 0
                else:
                    create_playlist['playlist_name'] = k
                    break

            if i == 1:
                print("Do you want a public(True) playlist or private(False)? ")
                k = bool(input())
                if k == '#' or k == False:
                    create_playlist['acces'] = False
                else:
                    create_playlist['acces'] = True

        ########################## create play list

        other7 = """
        	SELECT MAX("playlist_ID")  
                from public."playList"

        """
        cursor = conn.cursor()
        cursor.execute(other7)
        out7 = cursor.fetchall()
        conn.commit()

        sql8 = """
        INSERT INTO public."playList"(
          "playlist_ID", playlist_name, acces, "u_ID")
          VALUES (%(playlist_ID)s,%(playlist_name)s,%(acces)s,%(u_ID)s);

        """

        s8 = {
            'playlist_ID': out7[0][0] + 1,
            'playlist_name': create_playlist['playlist_name'],
            'acces': create_playlist['acces'],
            'u_ID': user_id
        }

        cursor = conn.cursor()
        cursor.execute(sql8, s8)
        # out=cursor.fetchall()
        conn.commit()

        ###################################################
        ######################################## add video to playlist
        x = int(input("Select between operations: "))
    elif x == 10:
        print("Insert into Playlist")

        y = int(input("if you want add video with video id enter 1 and with video name enter 2: "))
        if y == 1:
            print("please enter video id: ")
            k = int(input())
            insertTo_playlist_dict['video_id'] = k
            s = int(input("Enter the playlist Id: "))
            insertTo_playlist_dict['playList_id'] = s
            other8 = """
                   UPDATE public.video
                   	SET   p_id=%(playlist_ID)s
                   	WHERE "video_ID"=%(v_id)s;

                   """

            o8 = {
                'playlist_ID': insertTo_playlist_dict['playList_id'],
                'v_id': insertTo_playlist_dict['video_id']
            }
            cursor = conn.cursor()
            cursor.execute(other8, o8)
            # out8 = cursor.fetchall()
            conn.commit()

        if y == 2:
            print("please enter video name: ")
            k = str(input())
            insertTo_playlist_dict['video_name'] = k
            s = int(input("Enter the playlist Id: "))
            insertTo_playlist_dict['playList_id'] = s
            vid = """
                UPDATE public.video
                    SET   p_id=%(playlist_ID)s
                    WHERE "video_name"=%(v_name)s;

                """

            v8 = {
                'playlist_ID': insertTo_playlist_dict['playList_id'],
                'v_name': insertTo_playlist_dict['video_name']
            }
            cursor = conn.cursor()
            cursor.execute(vid, v8)
            # out8 = cursor.fetchall()
            conn.commit()

        #############################################

        ############################## remove from play list

        x = int(input("Select between operations: "))

    elif x == 11:
        print("remove from playlist")

        y = int(input("if you want remove video with video id enter 1 and with video name enter 2: "))
        if y == 1:
            print("please enter video id: ")
            k = int(input())
            removeFrom_playlist_dict['video_id'] = k

            aa = """
                UPDATE public.video
                   	SET "p_id"=null 
                    WHERE "video_ID"=%(v_id)s 
                         and "p_id" in (SELECT ("p_id")   
                            from public."playList"
                                WHERE "u_ID"=%(user)s)
                   """
            a8 = {
                'v_id': removeFrom_playlist_dict['video_id'],
                'user': user_id
            }

            cursor = conn.cursor()
            cursor.execute(aa, a8)
            #            aout = cursor.fetchall()
            conn.commit()

        if y == 2:
            print("please enter video name: ")
            k = str(input())
            removeFrom_playlist_dict['video_name'] = k
            xx = """
                   UPDATE public.video
                   	SET "p_id"=null 
                    WHERE "video_name"=%(v_name)s 
                         and "p_id" in (SELECT ("p_id")   
                            from public."playList"
                                WHERE "u_ID"=%(user)s)
                   """
            xx8 = {
                'v_name': removeFrom_playlist_dict['video_name'],
                'user': user_id
            }

            cursor = conn.cursor()
            cursor.execute(xx, xx8)
            # out8 = cursor.fetchall()
            conn.commit()

        ################################################
        x = int(input("Select between operations: "))
    elif x == 12:
        print("Join channel")

        i = 0
        while i == 0:
            print("Enter the id of channel: ")
            k = int(input())
            if k == '#':
                print("cannot be Null!")
                i = 0
            else:
                join_channel['c_id'] = k
                break

        ###################################### join channel

        other10 = """
        	SELECT MAX("join_ID")  
                from public.join_channel

        """
        cursor = conn.cursor()
        cursor.execute(other10)
        out10 = cursor.fetchall()
        conn.commit()

        sql9 = """
        INSERT INTO public.join_channel(
          "join_ID", u_id, c_id)
          VALUES (%(join_ID)s,%(u_id)s,%(c_id)s);


        """

        s9 = {
            'join_ID': out10[0][0] + 1,
            'u_id': user_id,
            'c_id': join_channel['c_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql9, s9)
        # out=cursor.fetchall()
        conn.commit()

        ##################################################

        x = int(input("Select between operations: "))

    elif x == 13:
        print("Leave channel")

        i = 0
        while i == 0:
            print("Enter the id of channel: ")
            k = int(input())
            if k == '#':
                print("cannot be Null!")
                i = 0
            else:
                Leave_channel['c_id'] = k
                break

        ################################ remove of channel

        sql10 = """
        DELETE FROM public.join_channel
          WHERE u_id=%(u_id)s and
          c_id=%(c_id)s;

        """

        s10 = {
            'c_id': Leave_channel['c_id'],
            'u_id': user_id,

        }

        cursor = conn.cursor()
        cursor.execute(sql10, s10)
        # out=cursor.fetchall()
        conn.commit()

        ########################################

        x = int(input("Select between operations: "))

    elif x == 14:
        print("Number of watched")

        print("Please enter the video id: ")
        k = int(input())
        NumWatched_comment['v_id'] = k

        ############################  number of watch video

        sql11 = """
        select COUNT ( v_id)
        from public.watch
        where watched= true and "v_id"=%(v_id)s ;

        """
        sf = {
            'v_id': NumWatched_comment['v_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql11, sf)
        out11 = cursor.fetchall()
        conn.commit()
        print("number of watch videos = ")
        print(out11[0][0])

        ###########################################################

        x = int(input("Select between operations: "))

    elif x == 15:
        print("Number of likes/dislikes")

        print("Please enter the video id: ")
        k = int(input())
        NumLike_comment['v_id'] = k

        ######################################### number of like

        sql12 = """
        select COUNT ( v_id)
        from public.comment
        where like_video=1 and "v_id"=%(v_id)s  ;

        """
        op = {
            'v_id': NumLike_comment['v_id']
        }
        cursor = conn.cursor()
        cursor.execute(sql12, op)
        out12 = cursor.fetchall()
        conn.commit()
        print("number of likes = ")
        print(out12[0][0])
        #####################################################

        ######################################### number of dislike
        sql13 = """
        select COUNT ( v_id)
        from public.comment
        where like_video=2 and "v_id"=%(v_id)s;

        """
        opx = {
            'v_id': NumLike_comment['v_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql13, opx)
        out13 = cursor.fetchall()
        conn.commit()
        print("number of dislikes = ")
        print(out13[0][0])

        ##################################################

        x = int(input("Select between operations: "))

    elif x == 16:
        print("Number of comments")

        print("Please enter the video id: ")
        k = int(input())
        NumComment_comment['v_id'] = k

        ########################################### tedad comment

        sql14 = """
        select COUNT( distinct "comment_id")
        from public.comment
        where v_id=%(v_id)s ;

        """

        s14 = {
            'v_id': NumComment_comment['v_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql14, s14)
        out14 = cursor.fetchall()
        conn.commit()
        print("number of comments = ")
        print(out14[0][0])

        #################################################

        x = int(input("Select between operations: "))

    elif x == 17:
        print("Number of joined users")

        print("Please enter the channel id: ")
        k = int(input())
        NumJoin['c_id'] = k

        ########################### number of join channel

        sql15 = """
        select COUNT (distinct "join_ID")
        from public.join_channel
        where  c_id=%(c_id)s;

        """

        s15 = {
            'c_id': NumJoin['c_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql15, s15)
        out15 = cursor.fetchall()
        conn.commit()
        print("number of join channel = ")
        print(out15[0][0])

        ##################################################

        x = int(input("Select between operations: "))

    elif x == 18:
        print("get replies of a video (replies of its comments)")

        print("Please enter the video id: ")
        k = int(input())
        get_reply['v_id'] = k

        #################################### get reply of videos

        sql16 = """
        SELECT  text
        	FROM public.reply
        	WHERE "v_id"=%(v_id)s;

        """

        s16 = {
            'v_id': get_reply['v_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql16, s16)
        out16 = cursor.fetchall()
        conn.commit()
        print("reply = ")
        print(out16[0][0])

        #################################################

        ##################################### remove video and channel

        x = int(input("Select between operations: "))

    elif x == 19:
        print("remove channel")

        print("please enter video id: ")
        k = int(input())
        remove_channel['channel_id'] = k

        sql45 = """
                 DELETE FROM public.join_channel
                   WHERE "c_id"=%(channel_id)s;

                 """

        s45 = {
            'channel_id': remove_channel['channel_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql45, s45)
        # out16 =cursor.fetchall()
        conn.commit()

        sql18 = """
                 DELETE FROM public.video
                   WHERE "c_ID"=%(channel_id)s;
              """

        s18 = {
            'channel_id': remove_channel['channel_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql18, s18)
        # out16 =cursor.fetchall()
        conn.commit()

        sql17 = """
               DELETE FROM public.channel
                 WHERE "channel_ID"=%(channel_id)s;

               """

        s17 = {
            'channel_id': remove_channel['channel_id']
        }

        cursor = conn.cursor()
        cursor.execute(sql17, s17)
        # out16 =cursor.fetchall()
        conn.commit()

        x = int(input("Select between operations: "))

        ###############################################

    elif x == 20:
        print("remove playlist")

        print("please enter playlist id: ")
        k = int(input())
        if k > 20 and k < 38:
            print("You cant remove watchlater playlist! ")
            exit()

        remove_playlist_dict['playlist_id'] = k
        ##################################### remove play list

        hye = """
                SELECT COUNT("playlist_ID")
                    from public."playList"
                    WHERE "u_ID"=%(u_id)s and "playlist_ID" = %(playlist_id)s
                """

        hye7 = {
            'u_id': user_id,
            'playlist_id': remove_playlist_dict['playlist_id']
        }

        cursor = conn.cursor()
        cursor.execute(hye, hye7)
        uout = cursor.fetchall()
        conn.commit()

        if uout[0][0] == 0:
            print("You cannot remove this playlist . you didnt create this playlist!")
            exit()

        bu = """
            UPDATE public.video
                SET "p_id" = null 
                    WHERE  "p_id" in (SELECT "playlist_ID"  
                                     from public."playList"
                                      WHERE "u_ID"=%(user)s)
                           """
        bb = {
            'user': user_id
        }

        cursor = conn.cursor()
        cursor.execute(bu, bb)
        conn.commit()

        ko = """
        DELETE FROM public."playList"
          WHERE "u_ID"=%(user)s and
          "playlist_ID"=%(playlist_id)s;
                           """
        kiki = {
            'user': user_id,
            'playlist_id': remove_playlist_dict['playlist_id']
        }

        cursor = conn.cursor()
        cursor.execute(ko, kiki)
        # aout = cursor.fetchall()
        conn.commit()
        x = int(input("Select between operations: "))
    ##########################################################
    elif x == 21:

        print("search video")
        print("please enter video name:")
        k = str(input())
        search_video['serach_video'] = k

        gj = """
                SELECT COUNT("video_ID"), "storage_id"
                    from public.video
                    WHERE "video_name"=%(serach_video)s
                    GROUP BY storage_id
                """

        gj7 = {
            'serach_video': search_video['serach_video']
        }

        cursor = conn.cursor()
        cursor.execute(gj, gj7)
        you = cursor.fetchall()
        conn.commit()

        if you == []:
            print("this video dosent exist!")
            exit()

        print("storage id =")
        print(you[0][1])
        x = int(input("Select between operations: "))
    ##########################################################
    elif x == 22:

        print("search channel")
        print("please enter channel name:")
        k = str(input())
        search_channel['search_channel'] = k

        sa = """
                SELECT COUNT("channel_ID")
                    FROM public.channel
                    WHERE "c_name"=%(search_channel)s

                """

        sa1 = {
            'search_channel': search_channel['search_channel']
        }

        cursor = conn.cursor()
        cursor.execute(sa, sa1)
        me = cursor.fetchall()
        conn.commit()

        if me[0][0] == 0:
            print("this channel dosent exist!")
            exit()

        print(" this channel exists and number of channel with this name is :")
        print(me[0][0])
        x = int(input("Select between operations: "))

        ##########################################

    elif x == 23:

        print("search playlist")
        print("please enter playlist name:")
        k = str(input())
        search_playlist['search_playlist'] = k

        her = """
                       SELECT COUNT("playlist_ID")
                           FROM public."playList"
                           WHERE "playlist_name" = %(search_playlist)s;

                       """

        her1 = {
            'search_playlist': search_playlist['search_playlist']
        }

        cursor = conn.cursor()
        cursor.execute(her, her1)
        he = cursor.fetchall()
        conn.commit()

        if he[0][0] == 0:
            print("this playlist dosent exist!")
            exit()

        print(" this channel exists and number of playlist with this name is :")
        print(he[0][0])
        x = int(input("Select between operations: "))

conn.commit()
conn.close()
