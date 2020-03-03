import xlrd
data=[]
import math
import sys
import os
import nltk
import pandas as pd
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
ps = PorterStemmer()
listss=stopwords.words('english')
from textblob import TextBlob as tb
#x=['large','diagosed','diagnose','diagnosis','partner','partners',"'",'"',"schedule","scheduled","schedules","took","neck","iui","trigger","eat","grain",'whole','quit','smoke','possible','possibilities','possibility','happen','took','taken','face','pound','light','remove','removed','30','40','lefts','left','two','13','2ww','food','meal','pap','smear','endocrinologist','reproduction','cm','temp','line','thick','lost','recent','chart','wii','fit','cut','situations','situation','peoples','people','situated','saw','situation','next','step','bad','hurt','line','appointment','appointed','minute','minutes','-',"'",'happy','happiness','sad','many','related','specialist','appt','dr','improve','improved','improves','refer','refers','glass','wedding','marriage','married','news','exciting','excited','found','scale','number','tuesday','result','forever','final','thought','term','manage','nature','change','track','fire','turbo','appreciate','appreciated','thank','thanks','bed','rest','sex','drive','soul','cyster','fun','little','give','inform','everyday','nothing','clear','use','book','read','shave','done','crave','craving','sweet','insurance','pay','paid','whatever','find','cover','sure','drill','cry','cried','crying','tear','tears','dinner','breakfast','site','names','name','fun','little','actual','ok','find','finds','whatever','pay','give','inform','develop','fine','yesterday','surprise','surprises','actually','done','excited','super','arm','unprotected','unprotect',"0.0",'rollers','everything','god','trust','count','ask','question','soulcysters','boys','boy','girls','girl','away','pass','fridays','saturdays','sunday','sundays','post','thread','class','school','due','date','play','trick','live','life','least','dont','doesnt','bless','keep','prayer','great','fiance','background','never','site','coaster','roller','comment','post','plans','planning','plan','friday','saturday','buys','buy','around','luck','wish','try','tried','way','breakfast','lunch','dinner','buy','cancel','comment','however','god','faith','job','area','come','son','boy','girl','boyfriend','breakfast','lunch','dinner','alright','amount','decide','baby','babies','angel','apart','april',"0.0",'10am','1st','2nd','2005','advice','advise','alone','along','alot','still','fingers','finger','crossed','cross','anyone','everyone','anything','january','september','october','week','month','polycyst','syndrome','syndrom','shot','doctor','wanna','wan','na','born','morning','morn','woke','every','single','singl','night','hello','doctor','tried','try','right','2008','2009','not',"n't",'anyone',"'ll",'favorite','week','motiv','oh','well','wait','take','pcos','pco','say','think','round','first','something','december','decemb','month','gonna','ndividual.asp','favourite','share','without','help','could','put','website','call','friend','came','better','make','work','good','leader','thing','really','load','','need','long','info','nature','please','look','said','went','even','though','today','anyone','else','side','want','blog','always','bottle','also','back','new','august','know','start','stop','told','want','got','families','family','lol','7/3-7/4',"n't",'video','may','2013','2016','-','ago','last','2007', 'since','manage', 'gid=54257','individual.asp', 'www.sparkpeople.com/myspark/groups_i','af', 'day', 'see','ca', 'day', 'go','husband','almost', 'feel', 'like','go', 'much', 'see','old', 'year','day', 'get', 'hope', 'time',"im","i've","hi,",'abl',"can't", 'one',",","-","3","1","2","4","5","6","7","8","9","10","i'v","\n","one...so","i'd","'d",'nan','jan','feb','mar','apr','you','hi','have','was',"'ve","'m",'would','will','are','were','n','not','be','http','your','coz','don',"'s",'had','it','am','we','on',"i'm","i","...","its","it's","me",'\ni', '(06:44)','be','some','to','have','has','with','to','out','be','www.mypcos.info']
x=["critic","doctor","dose","stress","seanhann","nearli","occur","parti","recent","rememb","saturday","women","diseas\\xe2\\x80\\xa6","improv","level","it\\xe2\\x80\\x99","statement","wear","think","tell","point","still","share","turn","the\\xe2\\x80\\xa6","'ve","adulthood","anim","b'http","b'i","cardiovascular","chang","cnn","coffe","daili","dental","detect","eat","first","event","give","h\\xe2\\x80\\xa6","he\\xe2\\x80\\x99","hope","killer","i\\xe2\\x80\\xa6","man","n\\n\\xf0\\x9f\\xa4\\xb8\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\xe2\\x9b\\xb9\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x82\\xef\\xb8\\x8f\\xf0\\x9f\\xa4\\xbe\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\xf0\\x9f\\x8f\\x8a\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x82\\xef\\xb8\\x8f\\xf0\\x9f\\x9a\\xb4\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\n\\nregular","consum","high","higher","lazi","least","one","per","suffer","sever","air","cure","reduc","recoveri","seriou","sleep","week","heartdiseas","coconut","condit","complic","crisi","clevelandclin","develop","fact","problem","chronicpainwar","cancer.\\n3","10","2017","accord","american","b'a","black","cancer.\\n3","day","due","engrossingfact","http","n\\n1","xe2\\x80\\xa6","well","via","disease.\\n2","diabet","cdc","eroii","big","check","center","clinic","d\\xe2\\x80\\xa6","half","goo\\xe2\\x80\\xa6","heartnew","ischem","help","make","made","import","research","accmediacent","disease\\xe2\\x80\\xa6","livpsi","respiratori","someon","suggest","use","unit","state","time","stori","stent","presid","thegooglefact","die","affect","bodi","he\\xe2\\x80\\xa6","n","menopause\\xe2\\x80\\xa6","person","see","stroke\\xe2\\x80\\xa6","itzwikipedia","incid","join","potu","realdonaldtrump","a\\xe2\\x80\\xa6","3","b'have","b'the","found","goredforwomen","mean","news","live","know","s\\xe2\\x80\\xa6","read","b'girl","b'start","patient","menarch","progress","lead","effect","danger","effect","ill","lead","girl","start","heighten","could","way","danc","caus","prevent","u.s.\\xe2\\x80\\xa6","par\\xe2\\x80\\xa6","2010","ischaem","primari","replac","activ", "b'rt","n\\n\\xf0\\x9f\\xa4\\xb8\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\xe2\\x9b\\xb9\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x82\\xef\\xb8\\x8f\\xf0\\x9f\\xa4\\xb","whosearo","aha", "dan","emce","jake","mcbride","skoff","aynrandpaulryan", "doesn\\xe2\\x80\\x99t","like","need","statin","trump\\xe2\\x80\\x99","b'more", "evid","b'rt", "n\\n\\xf0\\x9f\\xa4\\xb8\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\xe2\\x9b\\xb9\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x82\\xef\\xb8\\x8f\\xf0\\x9f\\xa4\\xb","million","doesn\\xe2\\x80\\x99t", "need","trump\\xe2\\x80\\x99","suc\\xe2\\x80\\xa6","noncommunic","emce", "mcbride","emce", "skoff","xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\xf0\\x9f\\x8f\\x8a\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x82\\xef\\xb8\\x8f\\xf0\\x9f\\x9a\\xb4\\xf0\\x9f\\x8f\\xbd\\xe2\\x80\\x8d\\xe2\\x99\\x80\\xef\\xb8\\x8f\\n\\nregular","fatal", "texasobserv","fatal", "get","floor", "hit", "kick-off","nwa","social","tomorrow","get", "xe2\\x80\\x9cd-\\xe2\\x80\\xa6","sanjay","gupta","tomorrow","sinc", "in\\nth","2010", "in\\nth","homicid","lanaihealth","mercola","mayoclin","medscap","eclips","studi",'increas',"you\\xe2\\x80\\x99r","manag","includ","lower","includ","signagnststrok","low\\xe2\\x80\\xa6","factor", "tie","amp","westmids_ca","awar","b'when", "rais","dr", "health","jackson", "health","care", "come","good","hard","u.s","ahanews\\xe2\\x80\\xa6", "b'for","asid","b","b'for","b'four", "hard", "dege\\xe2\\x80\\xa6","feb", "go","adult", "top","among","e","top","womenswel","to\\xe2\\x80\\xa6","agreement","sarahnormancx","midland","limit","sky-high","left","earli","left","girl","greater","in\\xe2\\x80\\xa6","along","start","later","access","sensimeliajah","along","also","nscsafeti","american_heart","declin","action","possibl","protect","friday","barrett_jackson","k\\xe2\\x80\\xa6","team","kill","aid", "murder","war\\xe2\\x80\\xa6","qualiti","alzheimer\\xe2\\x80\\x99","attack", "goo\\xe2\\x8","xf0\\x9f\\x91\\x89\\xf0\\x9f\\x8f\\xbdthe","ca\\xe2\\x80\\xa6", "summitmedicalnj", "fayettevil","goo\\xe2\\x8", "untreat", "xf0\\x9f\\x91\\x89\\xf0\\x9f\\x8f\\xbdthe","texa", "uninsur", "fight","creat","govern","ahanews\\nhttp","disciple96", "t.\\xe2\\x80\\xa6","local","wellb","west","scotref","acut","may","board","across", "allianc","they\\xe2\\x80\\x99r","red","2","type","access","ahanwa","rate","'s","accid","accident","1","5","work","all-tim","moyamoya","b'earli","strokeaha_asa","town","paint","old","take","stop","cyprusman","common", "enhanc","nation","mediat","gene","circaha","peopl","urg","signal","variant","nos3",'wait',"assocd","12","life","congress","2,200","can\\xe2\\x80\\x99t","w/\\xe2\\x80\\xa6","trump","rt","institu\\xe2\\x80\\xa6","invest","billi","age","period","clear","took","year","drsanjaygupta","'re","proud","everi","major","discuss","follow","interest","scienc","us","chanc","back","got","today","lister","futur","new","around","nwith","score","bike","relationship","t.co/szkalboeyu","associ","find","independ","particularli","show","put","gum","link","cost","poor","mani","topic","review","w\\xe2\\x80\\xa6","\\xe2\\x80\\xa6","w\\xe2\\x80\\xa6","t.co/eien2iibl6","t.co/am2d6tjoro","t.co/hcqb03py6v","t.co/eien2iibl6","t.co/am2d6tjoro","t.co/hcqb03py6v","t.co/eien2iibl6","t.co/am2d6tjoro","t.co/hcqb03py6v","251,000\\xc2\\xa0liv",]
#x=[]
def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    #print("n -con  ",sum(1 for blob in bloblist if word in blob.words))
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    #print("idf  ",math.log(len(bloblist) / (1 + n_containing(word, bloblist))))
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)

non_bmp=dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
wb = xlrd.open_workbook('F://strokedata.xlsx')
sh=wb.sheets()[0]
print(sh.nrows,sh.ncols)
for sheet in wb.sheets():
    
    number_of_rows = sheet.nrows
    number_of_columns = sheet.ncols
    for row in range(number_of_rows):
        for col in range(number_of_columns):
            value=(sheet.cell(row,col).value)
            if(len(value)!=0):
                data.append((value.translate(non_bmp)).lower())
#print(data)



import csv
with open('H://Pro2/csvdata.csv','w',encoding = "utf-8-sig",newline='') as myfile:
    wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
    for d in data:
        b=[]
        a = nltk.word_tokenize(d)
        for i in a:
            if i not in x and i not in listss:
                b.append(ps.stem(i))
        wr.writerow(b)
print(b)

with open('H://Pro2/csvdata.csv','r',encoding = "utf-8-sig") as myfile:
    rdr=csv.reader(myfile,quoting=csv.QUOTE_ALL)
    data = list(rdr)
bloblist=[]
for d in data:
    str1=""
    for q in d:
        str1+=q+" "
    bloblist.append(tb(str1))

print(d)
mydict={'key':'value'}

totalword=0
import csv
with open('out.csv','w',encoding = "utf-8-sig",newline='') as myfile:
    wr=csv.writer(myfile,quoting=csv.QUOTE_ALL)
    
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words if word not in x and word not in listss}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        wordss=[]
        for word, score in sorted_words:
            if(score>0.15):
                print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
                wordss.append(word)
        wr.writerow(wordss)
        totalword +=len(wordss)
        mydict.update({i+1:wordss})

#my_df = pd.DataFrame(wordss)
#my_df.to_csv('out.csv',index=False,header = False)
#print (my_df)
#print(mydict)


   




import pickle
with open("H://Pro2/mySavedDict.txt", "wb") as myFile:
    pickle.dump(mydict, myFile)
