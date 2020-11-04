from flask import Flask, render_template, request

import numpy as np
import datetime
import random
from datetime import date
import pandas as pd

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("test.html")

@app.route('/aicalculatorresult',methods = ['POST'])
def aicalculatorresult():
    prediction=''
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
     
        df=pd.read_excel('/Users/lota/Downloads/Demo自動配對.xlsx')
        df = df.drop(df.columns[[ 7,8,9,10,11,12,13,14,15,16,17,18,19 ]], axis=1)
        df=df.loc[df['失效日期'].dt.date>=date.today()]
        df.派單上限=df.派單上限.fillna(10)
        df.預算上限=df.預算上限.fillna(20)
        df['超標']=df['派單上限']-df['9月派單']
        df=df.where(df['超標']>0)
        df=df.dropna()
        df3=df
        df = df.drop(df.columns[[0,8]], axis=1)
        df=pd.get_dummies(df,columns=['預算上限','風格'])
        pp=0
        for i in df['預算上限_40']:
            if i==1:
                    df['預算上限_20'][df.index[pp]]=df['預算上限_20'][df.index[pp]]+1
            pp+=1
        pp=0
        for i in df['預算上限_50']:
            if i==1:
                    df['預算上限_20'][df.index[pp]]=df['預算上限_20'][df.index[pp]]+1
                    df['預算上限_40'][df.index[pp]]=df['預算上限_40'][df.index[pp]]+1
            pp+=1
        customer=pd.DataFrame([[str(to_predict_list['z1']),str(to_predict_list['z2']),str(to_predict_list['z3']),str(to_predict_list['z4'])]], columns=['名字', '預算上限', '風格','裝修/設計'],index=[1000])
        customer=customer.drop(customer.columns[[0]], axis=1)
        zz=pd.get_dummies(customer,columns=['預算上限','風格'])
        df=df.append(zz)
        df=df.drop(df.columns[[2,3]], axis=1)
        df=df.fillna(0)
        num=df.index[-1]
        if df['預算上限_40'][num]==1:
            df['預算上限_20'][num]=df['預算上限_20'][num]+1
        if df.iloc[df.shape[0]-1,:]['預算上限_50']==1:
            df['預算上限_20'][num]=df['預算上限_20'][num]+1
            df['預算上限_40'][num]=df['預算上限_40'][num]+1
        df=df.where(df['裝修/設計']==df['裝修/設計'][1000])
        df=df.dropna()
        df3=df
        df = df.drop(df.columns[[1,2]], axis=1)
        cha=['預算上限_20', '預算上限_40', '預算上限_50', '預算上限_50-100', '風格_古典風',
            '風格_現代風']
        cc=1
        ca=0
        big=[]
        finalrow=df.shape[0]-1
        for e in range(6):
            z=0
            ind=[]
            if df.iloc[finalrow,:][cc]==1:
                for i in df.iloc[0:finalrow,:][cha[ca]]:
                    if i==df.iloc[finalrow,:][cc]:
                        ind.append(z)
                        
                    z+=1
                big.append(ind)
            cc+=1
            ca+=1
        import itertools
        v=set.intersection(set(big[0]),*itertools.islice(big,1,None))
        cnn=1
        for i in list(v):
            if cnn!=4:
                
                cnn+=1
            else:
                break
        df3['neworder']=list(range(df3.shape[0]))
        df3=df3.set_index('neworder')
        cq=df3['評分'].to_dict()
        ra={}
        for i in list(v):
            q={i:cq[i]}
            ra.update(q)
        finallist={k: v for k, v in sorted(ra.items(), key=lambda item: item[1],reverse=True)}
        newv=list(finallist.keys())[0:3]
        cnn=1
        com=[]
        for i in newv:
            if cnn!=4:
                com.append(df.iloc[i,:][0])
                cnn+=1
            else:
                break
        try:
            c1=com[0]
        except:
            c1='沒有匹配'
        try:
            c2=com[1]
        except:
            c2='沒有匹配'
        try:
            c3=com[2]
        except:
            c3='沒有匹配'
        
        from keras.preprocessing import image

        a='YBJ'
        image_path="/Users/lota/Downloads/c21/static/{}.jpg".format(a)
        img = image.load_img(image_path)

        return render_template("aicalculatorresult.html",com=com,c1=c1,c2=c2,c3=c3,img=img)

@app.route("/aicalculator", methods=['POST','GET'])
def aicalculator():
        return render_template('aicalculator.html')

@app.route("/test", methods=['POST','GET'])
def test():

        return render_template('test.html')
@app.route("/result", methods=['POST','GET'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        name=to_predict_list['username']
        budget=to_predict_list['budget']
        consider=to_predict_list['consider']
        favour=to_predict_list['favour']
        ft=str(to_predict_list['username'])+'正在尋找一個理想家園，理想家園中的'+str(to_predict_list['consider'])+'對他來說非常重要。'
        if str(to_predict_list['consider'])=='讀書學費':
    
            g2=random.choice([208,204]) 
            if g2==208:
                a1='泰國Chapter Chula-Samyan'
                l1='泰國'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/chapter-chula-samyan/'
            else:
                a1='馬來西亞Bukit Bintang City Centre'
                l1='馬來西亞'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/bukit-bintang-city-centre%ef%bc%88bbcc%ef%bc%89/'
            g3=random.choice([200,212]) 
            if g3==200:
                a2='保加利亞龍脈天下'
                l2='保加利亞'
            else:
                a2='馬來西亞柏威年白沙羅嶺'
                l2='馬來西亞'
            g4=random.choice([205,203]) 
            if g4==205:
                a3='泰國Plum Condo Donmuang Airport'
                l3='泰國'
            else:
                a3='馬來西亞Axon Bukit Bintang'
                l3='馬來西亞'
            gg4=random.choice([700,800]) 
            gg5=random.choice([750,600]) 
            gg6=random.choice([900,600]) 
        elif str(to_predict_list['consider'])=='生活水平':
        
            g2=random.choice([202,207])
            if g2==202:
                a1='土耳其Taksim Petek Residence'
                l1='土耳其'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/taksim-petek-residence/'
            else:
                a1='土耳其Tyrese Gardon Condominium' 
                l1='土耳其'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/tyrese-gardon-condominium/'
            g3=random.choice([209,201])
            if g3==209:
                a2='土耳其Rotana Condominium'
                l2='土耳其'
            else:
                a2='泰國Ideo Charan 70' 
                l1='泰國'
            g4=random.choice([210,230]) 
            if g4==110:
                a3='泰國Noble Above Wireless'
                l3='泰國'
            else:
                a3='泰國Bave Binoal'
                l3='泰國'
            gg4=random.choice([700,800]) 
            gg5=random.choice([750,600]) 
            gg6=random.choice([900,600]) 
        else:
            
            g2=random.choice([208,204]) 
            if g2==208:
                a1='泰國Chapter Chula-Samyan'
                l1='泰國'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/chapter-chula-samyan/'
            else:
                a1='馬來西亞Bukit Bintang City Centre'
                l1='馬來西亞'
                link='https://overseae.com/%E6%B5%B7%E5%A4%96/bukit-bintang-city-centre%ef%bc%88bbcc%ef%bc%89/'
            g3=random.choice([209,201])
            if g3==209:
                a2='土耳其Rotana Condominium'
                l2='土耳其'
            else:
                a2='泰國Ideo Charan 70' 
                l2='泰國'
            g4=random.choice([205,203]) 
            if g4==205:
                a3='泰國Plum Condo Donmuang Airport'
                l3='泰國'
            else:
                a3='馬來西亞Axon Bukit Bintang'
                l3='馬來西亞'
    
            gg4=random.choice([700,800]) 
            gg5=random.choice([750,600]) 
            gg6=random.choice([900,600]) 
        return render_template('result.html',name=name,budget=budget,consider=consider,favour=favour,ft=ft,g2=g2,g3=g3,g4=g4,a2=a2,a3=a3,a1=a1,gg4=gg4,gg5=gg5,gg6=gg6,l1=l1,l2=l2,l3=l3,link=link)

@app.route('/',methods = ['POST'])
def home1():
    if request.method == 'POST':
        return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
