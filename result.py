import random #line:1
import sys #line:2
import time #line:3
from math import sqrt #line:4
def run ():#line:7
    OOO0OOOO0O00OOOOO =0 #line:8
    while True :#line:9
        time .sleep (0.05 )#line:10
        OOO0OOOO0O00OOOOO +=0.01 #line:11
        O00000OO0OO00O00O =100 *(OOO0OOOO0O00OOOOO -sqrt (OOO0OOOO0O00OOOOO ))/(OOO0OOOO0O00OOOOO -1 )#line:13
        O0000OOOO00OOO0OO ="▓"*int (O00000OO0OO00O00O )#line:14
        O00OO000OO0OOOOOO ="-"*(100 -int (O00000OO0OO00O00O ))#line:15
        print ("\r",end ="")#line:16
        print ("\r{:^3.2f}%[{}->{}]".format (O00000OO0OO00O00O ,O0000OOOO00OOO0OO ,O00OO000OO0OOOOOO ),end ="")#line:18
print ("欢迎使用ChatRick，本模型基于Rick Astley于27 July 1987发表的论文:Ne jamais vous abandonner.")#line:22
def isGameOver (OO0O00OO0OO0O0000 ):#line:25
    ""#line:30
    OO0O0OOOOOO000O00 =True #line:31
    for OOOO00OOO0O0OO0OO in range (4 ):#line:32
        for O0O00O0OOOOO0OOO0 in range (3 ):#line:33
            if OO0O00OO0OO0O0000 [OOOO00OOO0O0OO0OO ][O0O00O0OOOOO0OOO0 ]==0 :#line:34
                OO0O0OOOOOO000O00 =False #line:35
                break #line:36
            else :#line:37
                if OO0O00OO0OO0O0000 [OOOO00OOO0O0OO0OO ][O0O00O0OOOOO0OOO0 ]==OO0O00OO0OO0O0000 [OOOO00OOO0O0OO0OO ][O0O00O0OOOOO0OOO0 +1 ]or OO0O00OO0OO0O0000 [O0O00O0OOOOO0OOO0 ][OOOO00OOO0O0OO0OO ]==OO0O00OO0OO0O0000 [O0O00O0OOOOO0OOO0 +1 ][OOOO00OOO0O0OO0OO ]:#line:38
                    OO0O0OOOOOO000O00 =False #line:39
                    break #line:40
    return OO0O0OOOOOO000O00 #line:41
print ("清选择模型输出方式：")#line:45
from os import path #line:46
def check_for_file ():#line:49
    print ("Does file exist:",path .exists ("data.csv"))#line:50
print ("======================")#line:53
def os ():#line:56
    for OO0000000OO00O0OO in range (1 ):#line:57
        O0O0OO0OOO0O00000 =dict ()#line:58
        O00OOOOOOO0000000 =OO0000000OO00O0OO ["author"]["mid"]#line:59
        OO000OO00O0OOO0O0 =OO0000000OO00O0OO ["author"]["uname"]#line:60
        OO00000OOO0OO0O00 =OO0000000OO00O0OO ["content"]#line:61
        try :#line:62
            O0O00O00O0O00O000 =OO0000000OO00O0OO ["progress"]#line:63
        except KeyError :#line:64
            O0O00O00O0O00O000 ="无"#line:65
        O0O00000O0OO0000O =OO0000000OO00O0OO ["score"]#line:66
        O0O0OO0OOO0O00000 ["author"]=O00OOOOOOO0000000 #line:67
        O0O0OO0OOO0O00000 ["name"]=OO000OO00O0OOO0O0 #line:68
        O0O0OO0OOO0O00000 ["content"]=OO00000OOO0OO0O00 #line:69
        O0O0OO0OOO0O00000 ["progress"]=O0O00O00O0O00O000 #line:70
        O0O0OO0OOO0O00000 ["score"]=O0O00000O0OO0000O #line:71
        list ().append (O0O0OO0OOO0O00000 )#line:72
print ("1. 长文本输出")#line:75
def getyear ():#line:78
    OOOOOO0OO0O00OOOO =int (input ("输入一个年份: "))#line:79
    if (OOOOOO0OO0O00OOOO %4 )==0 :#line:80
        if (OOOOOO0OO0O00OOOO %100 )==0 :#line:81
            if (OOOOOO0OO0O00OOOO %400 )==0 :#line:82
                print ("{0} 是闰年".format (OOOOOO0OO0O00OOOO ))#line:83
            else :#line:84
                print ("{0} 不是闰年".format (OOOOOO0OO0O00OOOO ))#line:85
        else :#line:86
            print ("{0} 是闰年".format (OOOOOO0OO0O00OOOO ))#line:87
    else :#line:88
        print ("{0} 不是闰年".format (OOOOOO0OO0O00OOOO ))#line:89
def binarySearch (O00O00OO00OO0000O ,OOO0OOOO00OO000O0 ,O00OO00O00000O000 ,O000OOOO0O00OOOOO ):#line:92
    if O00OO00O00000O000 >=OOO0OOOO00OO000O0 :#line:93
        OOOOOOO0OO0OOO000 =int (OOO0OOOO00OO000O0 +(O00OO00O00000O000 -OOO0OOOO00OO000O0 )/2 )#line:95
        if O00O00OO00OO0000O [OOOOOOO0OO0OOO000 ]==O000OOOO0O00OOOOO :#line:96
            return OOOOOOO0OO0OOO000 #line:97
        elif O00O00OO00OO0000O [OOOOOOO0OO0OOO000 ]>O000OOOO0O00OOOOO :#line:98
            return binarySearch (O00O00OO00OO0000O ,OOO0OOOO00OO000O0 ,OOOOOOO0OO0OOO000 -1 ,O000OOOO0O00OOOOO )#line:99
        else :#line:100
            return binarySearch (O00O00OO00OO0000O ,OOOOOOO0OO0OOO000 +1 ,O00OO00O00000O000 ,O000OOOO0O00OOOOO )#line:101
    else :#line:103
        return -1 #line:104
print ("2. 连续对话")#line:107
print ("0. 退出")#line:108
def columnToRow (O000OO0OOO00000O0 ):#line:111
    ""#line:116
    OO00O000O00OOOO0O =list ()#line:117
    for OOOOO000OO0OO0OOO in range (3 ,-1 ,-1 ):#line:119
        O0O0O0OO00O0OOO00 =list ()#line:120
        for O00OOOO0O0OOOOOOO in range (4 ):#line:122
            O0O0O0OO00O0OOO00 .append (O000OO0OOO00000O0 [O00OOOO0O0OOOOOOO ][OOOOO000OO0OO0OOO ])#line:123
        OO00O000O00OOOO0O .append (O0O0O0OO00O0OOO00 )#line:124
    return OO00O000O00OOOO0O #line:125
def rowToColumn (O00OOO0OOO0OO00O0 ):#line:128
    ""#line:133
    OO000OOOOOO00OOOO =list ()#line:134
    for O000OO0O0O00OOO0O in range (4 ):#line:136
        OOOO000O0O0000OO0 =list ()#line:138
        for OO0O0O0OOO00OOOOO in range (3 ,-1 ,-1 ):#line:139
            OOOO000O0O0000OO0 .append (O00OOO0OOO0OO00O0 [OO0O0O0OOO00OOOOO ][O000OO0O0O00OOO0O ])#line:140
        OO000OOOOOO00OOOO .append (OOOO000O0O0000OO0 )#line:141
    return OO000OOOOOO00OOOO #line:142
def isGameHaveEmpty (OO0OO00OO0O0OOOO0 ):#line:145
    ""#line:150
    for O00O0000O00OO0O00 in OO0OO00OO0O0OOOO0 :#line:151
        for OO00O0OOOOO0O000O in O00O0000O00OO0O00 :#line:152
            if OO00O0OOOOO0O000O ==0 :#line:153
                return True #line:154
class GamingCore :#line:157
    classBoard =list ()#line:158
    score =0 #line:159
    def __init__ (O00OOO0000O0O000O ):#line:161
        for O0O0O0000000O00OO in range (0 ,4 ):#line:163
            O00OOO0000O0O000O .classBoard .append ([0 ,0 ,0 ,0 ])#line:164
    def createNewNumber (OOO0O0O000O00O0O0 ):#line:166
        ""#line:170
        if not isGameHaveEmpty (OOO0O0O000O00O0O0 .classBoard ):#line:171
            return #line:172
        OO00O00000O0OO0OO =list ()#line:173
        for OOOO0O00O00000000 in range (4 ):#line:174
            for O0OO00000O00O0O00 in range (4 ):#line:175
                if OOO0O0O000O00O0O0 .classBoard [OOOO0O00O00000000 ][O0OO00000O00O0O00 ]==0 :#line:176
                    OO00O00000O0OO0OO .append ([OOOO0O00O00000000 ,O0OO00000O00O0O00 ])#line:177
        O00O0O0OO0OOO0O00 =random .randint (0 ,len (OO00O00000O0OO0OO )-1 )#line:178
        if OOO0O0O000O00O0O0 .score >=200 :#line:179
            OOO0O0O000O00O0O0 .classBoard [OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][0 ]][OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][1 ]]=8 #line:180
        elif 100 <=OOO0O0O000O00O0O0 .score <=200 :#line:181
            OOO0O0O000O00O0O0 .classBoard [OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][0 ]][OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][1 ]]=4 #line:182
        else :#line:183
            OOO0O0O000O00O0O0 .classBoard [OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][0 ]][OO00O00000O0OO0OO [O00O0O0OO0OOO0O00 ][1 ]]=2 #line:184
        OOO0O0O000O00O0O0 .score =0 #line:185
        for OOOO0O00O00000000 in OOO0O0O000O00O0O0 .classBoard :#line:186
            for O0OO00000O00O0O00 in OOOO0O00O00000000 :#line:187
                OOO0O0O000O00O0O0 .score +=O0OO00000O00O0O00 #line:188
    def printClassBoard (OOO0OO0OOO000O00O ):#line:190
        ""#line:194
        for O00OO00OOO00000O0 in OOO0OO0OOO000O00O .classBoard :#line:195
            for OOO0O000O0000OO00 in O00OO00OOO00000O0 :#line:196
                print (OOO0O000O0000OO00 ,end ="\t")#line:197
            print ("")#line:198
        if isGameOver (OOO0OO0OOO000O00O .classBoard ):#line:199
            print ("游戏结束，分数为："+str (OOO0OO0OOO000O00O .score ))#line:200
            sys .exit ()#line:201
    def __OOO000OOOO0OOOOOO (O0OOO0OO0O000000O ):#line:203
        ""#line:207
        for O0OOOOO00OOO000O0 in range (4 ):#line:208
            for O0OOOO000OOO0OO0O in range (4 ):#line:209
                if O0OOO0OO0O000000O .classBoard [O0OOOOO00OOO000O0 ][O0OOOO000OOO0OO0O ]==0 :#line:210
                    O0OOO0OO0O000000O .classBoard [O0OOOOO00OOO000O0 ].remove (O0OOO0OO0O000000O .classBoard [O0OOOOO00OOO000O0 ][O0OOOO000OOO0OO0O ])#line:211
                    O0OOO0OO0O000000O .classBoard [O0OOOOO00OOO000O0 ].append (0 )#line:212
                else :#line:213
                    continue #line:214
        return O0OOO0OO0O000000O #line:215
    def __OO0O0OO00OO0OOO00 (O0OOO000O0O0000O0 ):#line:217
        ""#line:221
        for OOOO0O0O0OOO0OOOO in range (4 ):#line:223
            for O000O0OOO00O0O000 in range (1 ,4 ):#line:224
                if O0OOO000O0O0000O0 .classBoard [OOOO0O0O0OOO0OOOO ][O000O0OOO00O0O000 ]==O0OOO000O0O0000O0 .classBoard [OOOO0O0O0OOO0OOOO ][O000O0OOO00O0O000 -1 ]:#line:225
                    O0OOO000O0O0000O0 .classBoard [OOOO0O0O0OOO0OOOO ][O000O0OOO00O0O000 -1 ]*=2 #line:226
                    O0OOO000O0O0000O0 .classBoard [OOOO0O0O0OOO0OOOO ][O000O0OOO00O0O000 ]=0 #line:227
        return O0OOO000O0O0000O0 #line:228
    def moveLeft (O0O0000000OOOO00O ):#line:230
        ""#line:234
        O0O0000000OOOO00O .__OOO000OOOO0OOOOOO ().__OO0O0OO00OO0OOO00 ().__OOO000OOOO0OOOOOO ()#line:235
        os .system ("cls")#line:236
        print ("分数："+str (O0O0000000OOOO00O .score ))#line:237
        O0O0000000OOOO00O .createNewNumber ()#line:238
        O0O0000000OOOO00O .printClassBoard ()#line:239
    def moveUp (O0O000OO0OOOO0000 ):#line:241
        ""#line:245
        O0O000OO0OOOO0000 .classBoard =columnToRow (O0O000OO0OOOO0000 .classBoard )#line:246
        O0O000OO0OOOO0000 .__OOO000OOOO0OOOOOO ().__OO0O0OO00OO0OOO00 ().__OOO000OOOO0OOOOOO ()#line:247
        os .system ("cls")#line:248
        print ("分数："+str (O0O000OO0OOOO0000 .score ))#line:249
        O0O000OO0OOOO0000 .classBoard =rowToColumn (O0O000OO0OOOO0000 .classBoard )#line:250
        O0O000OO0OOOO0000 .createNewNumber ()#line:251
        O0O000OO0OOOO0000 .printClassBoard ()#line:252
    def moveRight (O0OO000OOOOO00000 ):#line:254
        ""#line:258
        for OO0O0OOOO00OO00OO in range (4 ):#line:259
            O0OO000OOOOO00000 .classBoard [OO0O0OOOO00OO00OO ]=O0OO000OOOOO00000 .classBoard [OO0O0OOOO00OO00OO ][::-1 ]#line:260
        O0OO000OOOOO00000 .__OOO000OOOO0OOOOOO ().__OO0O0OO00OO0OOO00 ().__OOO000OOOO0OOOOOO ()#line:261
        os .system ("cls")#line:262
        for OO0O0OOOO00OO00OO in range (4 ):#line:263
            O0OO000OOOOO00000 .classBoard [OO0O0OOOO00OO00OO ]=O0OO000OOOOO00000 .classBoard [OO0O0OOOO00OO00OO ][::-1 ]#line:264
        os .system ("cls")#line:265
        print ("分数："+str (O0OO000OOOOO00000 .score ))#line:266
        O0OO000OOOOO00000 .createNewNumber ()#line:267
        O0OO000OOOOO00000 .printClassBoard ()#line:268
    def moveDown (OOO00OO00OOO00O00 ):#line:270
        ""#line:274
        OOO00OO00OOO00O00 .classBoard =rowToColumn (OOO00OO00OOO00O00 .classBoard )#line:275
        OOO00OO00OOO00O00 .__OOO000OOOO0OOOOOO ().__OO0O0OO00OO0OOO00 ().__OOO000OOOO0OOOOOO ()#line:276
        os .system ("cls")#line:277
        OOO00OO00OOO00O00 .classBoard =columnToRow (OOO00OO00OOO00O00 .classBoard )#line:278
        os .system ("cls")#line:279
        print ("分数："+str (OOO00OO00OOO00O00 .score ))#line:280
        OOO00OO00OOO00O00 .createNewNumber ()#line:281
        OOO00OO00OOO00O00 .printClassBoard ()#line:282
print ("======================")#line:285
while True :#line:286
    choice =input ("请输入选择：")#line:287
    if choice .isdigit ():#line:288
        if int (choice )<0 or int (choice )>2 :#line:289
            print ("输入错误，请重新输入。")#line:290
            continue #line:291
        else :#line:292
            if int (choice )==1 :#line:293
                import os #line:294
                import configparser #line:295
                """
                一份简单的文档：
                在plugins下创建.py文件，main.py执行时会调用插件的run()方法。
                具体实现详见testPlugin.py
                """#line:301
                def loadConfig ():#line:304
                    if os .path .exists ("configs/config.ini"):#line:305
                        O0O0OO00OO0O0OOO0 =configparser .ConfigParser ()#line:306
                        O0O0OO00OO0O0OOO0 .read ("configs/config.ini",encoding ="utf-8")#line:307
                        O000O0OOO0OO0000O =O0O0OO00OO0O0OOO0 .get ("KeyWord","cmd")#line:308
                        O0OO00O0O000O000O =O0O0OO00OO0O0OOO0 .get ("KeyWord","placeholdertext")#line:309
                        O000O0O0O0OO0OO0O =dict ()#line:310
                        O000O0O0O0OO0OO0O ["CMD"]=O000O0OOO0OO0000O #line:311
                        O000O0O0O0OO0OO0O ["PHT"]=O0OO00O0O000O000O #line:312
                    else :#line:313
                        O0O0OO00OO0O0OOO0 =configparser .ConfigParser ()#line:314
                        O0O0OO00OO0O0OOO0 .add_section ("KeyWord")#line:315
                        O0O0OO00OO0O0OOO0 .set ("KeyWord","cmd","> ")#line:316
                        O0O0OO00OO0O0OOO0 .set ("KeyWord","placeholdertext","Type here")#line:317
                        O0O0OO00OO0O0OOO0 .write (open ("configs/config.ini","w",encoding ="utf-8"))#line:318
                        O000O0O0O0OO0OO0O ={"CMD":">","PHT":"Type here",}#line:322
                    return O000O0O0O0OO0OO0O #line:323
                def loadPlugin ():#line:326
                    O0OO000O0OOOOO000 =os .getcwd ()+"\\plugins"#line:328
                    O0OO000O0OOOOO000 ="plugins/"#line:329
                    O00OO0OO00OO0OOOO =os .listdir (O0OO000O0OOOOO000 )#line:330
                    O00OO0OO00OO0OOOO .remove ("__pycache__")#line:331
                    OOOO0OOOOOOO00O0O =dict ()#line:332
                    OO0OOOOO0O0O0O00O =list ()#line:333
                    OO0OO0O00O0000OOO =list ()#line:334
                    for OO0O0OOOOOOOO0000 in O00OO0OO00OO0OOOO :#line:335
                        OO0O0OOOOOOOO0000 =OO0O0OOOOOOOO0000 .replace (".py","")#line:336
                        OOO0O0OO00OO00O0O =__import__ ("plugins."+OO0O0OOOOOOOO0000 ,fromlist =OO0O0OOOOOOOO0000 ,level =0 )#line:337
                        OOO0O0OO00OO00O0O .run ()#line:338
                        try :#line:339
                            OO0OO0O00O0000OOO .append (OOO0O0OO00OO00O0O .setCompleter ())#line:340
                        except :#line:341
                            pass #line:342
                        OOOO0OOOOOOO00O0O [OO0O0OOOOOOOO0000 ]=OOO0O0OO00OO00O0O .registerCommand ()#line:343
                    OO0OOOOO0O0O0O00O .append (OOOO0OOOOOOO00O0O )#line:345
                    OO0OOOOO0O0O0O00O .append (OO0OO0O00O0000OOO )#line:346
                    return OO0OOOOO0O0O0O00O #line:347
                input ("请输入想要生成的主题：")#line:350
                def registerCommand ():#line:353
                    return "config"#line:354
                print ("正在为您生成，请勿中途关闭，以免影响参数。")#line:359
                run ()#line:360
            elif int (choice )==2 :#line:361
                print ("正在初始化模型，请勿中途关闭，以免影响参数。")#line:362
                def getresult ():#line:365
                    for OO0O00OOOO00O000O in range (1 ,10 ):#line:366
                        for OO0000O0OOO00OOO0 in range (1 ,OO0O00OOOO00O000O +1 ):#line:367
                            print ('{}x{}={}\t'.format (OO0000O0OOO00OOO0 ,OO0O00OOOO00O000O ,OO0O00OOOO00O000O *OO0000O0OOO00OOO0 ),end ='')#line:368
                        print ()#line:369
                run ()#line:373
            elif int (choice )==0 :#line:374
                print ("正在保存模型，请勿中途关闭。")#line:375
                run ()#line:376
    else :#line:377
        def show_scores (OOOO00OO0O0O00O00 ):#line:378
            OOO0OO000OOOO0O00 ="pd.DataFrame(info_list)"#line:380
            print (OOO0OO000OOOO0O00 )#line:381
        print ("输入错误，请重新输入。")#line:385
        class Student (object ):#line:388
            def __init__ (O00O0O0O0O0000000 ,OO00O0O00O0O0O00O ,OOOO00OO0000O0OO0 ,OO0OOO00000OOOOOO ):#line:389
                O00O0O0O0O0000000 .name =OO00O0O00O0O0O00O #line:390
                O00O0O0O0O0000000 .gender =OOOO00OO0000O0OO0 #line:391
                O00O0O0O0O0000000 .tel =OO0OOO00000OOOOOO #line:392
            def __str__ (O00OOO000O00OO000 ):#line:394
                return f'{O00OOO000O00OO000.name}, {O00OOO000O00OO000.gender}, {O00OOO000O00OO000.tel}'#line:395
        continue #line:399
a =[1 ,5 ,2 ,3 ,8 ,9 ]#line:401
def func (OOOOOO000000OOO00 ):#line:404
    OO00000O00OO0O0OO =len (OOOOOO000000OOO00 )#line:405
    for OOOO0OOO0OOO00O0O in range (1 ,OO00000O00OO0O0OO ):#line:407
        O0O000000000OOO0O =False #line:408
        for OO000O0O0000O0O0O in range (OO00000O00OO0O0OO -OOOO0OOO0OOO00O0O ):#line:409
            if OOOOOO000000OOO00 [OO000O0O0000O0O0O ]>OOOOOO000000OOO00 [OO000O0O0000O0O0O +1 ]:#line:410
                OOOOOO000000OOO00 [OO000O0O0000O0O0O ],OOOOOO000000OOO00 [OO000O0O0000O0O0O +1 ]=OOOOOO000000OOO00 [OO000O0O0000O0O0O +1 ],OOOOOO000000OOO00 [OO000O0O0000O0O0O ]#line:411
                O0O000000000OOO0O =True #line:412
        if not O0O000000000OOO0O :#line:413
            return OOOOOO000000OOO00 #line:414
    return OOOOOO000000OOO00 #line:415
def Merge (OOO0OOOO00OOOOOOO ,O00O0OO000O000OOO ):#line:418
    OO0O0O0OOO000OOO0 ={**OOO0OOOO00OOOOOOO ,**O00O0OO000O000OOO }#line:419
    return OO0O0O0OOO000OOO0 #line:420
