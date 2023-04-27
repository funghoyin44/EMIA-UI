# -*- coding: utf-8 -*-
"""hwtime.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q3G9O7dudvdY25qlIUcEJEQJ8kVvin0M

# import

>
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np

import pandas as pd       
import matplotlib.pyplot as plt               #visulization
import matplotlib
import datetime                           #show user how he finish his work



"""define function"""

def suggesttime(cga,df):    #helper function
  percentagetile=1-((cga-2.0)/2.0)
  index=int(percentagetile*len(df))
  index=df.index[index]
  return round(df['time'][index]*1.1,-1)

def serachcourse_withoutgraph(coursecode,index,cga): #input parameter and return max,min and suggest time,boolean value represent does it find the course and print the graph
  df1=pd.read_csv('hwtime.csv')         #0utput those max min and suggest tme in the UI
  df2=df1[(df1['coursecode']==coursecode)]
  df2=df2[df2['hwindex']==index]
  if(df2.empty):
    print("no such course code or hwindex is found")
    return False
  values, base = np.histogram(df2['time'], bins=10)
  base=base[:-1]
  cumulative = np.cumsum(values)
  plt.plot(base,cumulative)
  #xnew = np.linspace(base.min(), base.max(), 100)      #can smooth the graph(but will change it into non cumulative graph)
  #power_smooth = make_interp_spline(base,cumulative)(xnew)
  #plt.plot(xnew, power_smooth)
  plt.xlabel("time to finish/minutes")
  ax = plt.gca()
  ax.get_yaxis().set_visible(False) #clear the yaxis
  #plt.show()
  print('Maximum of time used in the homework by past data:',df2['time'].max(),'minutes')
  print('Minimum of time used in the homework by past data:',df2['time'].min(),'minutes')
  print('suggest time for you to do the homework:',suggesttime(cga,df2))
  return int(df2['time'].min()), int(df2['time'].max()), int(suggesttime(cga,df2)),True

def serachcourse_withgraph(coursecode,index,cga): #input parameter and return max,min and suggest time,boolean value represent does it find the course and print the graph
  df1=pd.read_csv('hwtime.csv')         #0utput those max min and suggest tme in the UI
  df2=df1[(df1['coursecode']==coursecode)]
  df2=df2[df2['hwindex']==index]
  if(df2.empty):
    print("no such course code or hwindex is found")
    return False
  values, base = np.histogram(df2['time'], bins=10)
  base=base[:-1]
  cumulative = np.cumsum(values)
  plt.plot(base,cumulative)
  #xnew = np.linspace(base.min(), base.max(), 100)      #can smooth the graph(but will change it into non cumulative graph)
  #power_smooth = make_interp_spline(base,cumulative)(xnew)
  #plt.plot(xnew, power_smooth)
  plt.xlabel("time to finish/minutes")
  ax = plt.gca()
  ax.get_yaxis().set_visible(False) #clear the yaxis
  #plt.show()
  plt.savefig("homework.png")


def uploaddata(coursecode,index,hwtime,userid,cga,finishtime): #input all the parameter and things will be upload to csv
  df1=pd.read_csv('hwtime.csv',index_col=[0])                   #return true when success and false when the data already appear(same user and hw and course)
  df=df1[df1['coursecode']==coursecode]
  df=df[df['hwindex']==index]
  df=df[df['userid']==userid]
  if(not df.empty):
    print('you have already upload this hw once')
    return False
  if(finishtime=='0'):
    deadline=datetime.datetime.now()
    deadline=deadline.timestamp()
  else:
    finishtime=finishtime+' 00:00:00.929149'
    deadline = datetime.datetime.strptime(finishtime,'%Y-%m-%d %H:%M:%S.%f')
    deadline=deadline.timestamp()
  newdata={'coursecode':coursecode,'hwindex':index,'time':hwtime,'cga':cga,'userid':userid,'timehandin':deadline}
  #we may implement a tools for checking the time isnt real or not
  df1.loc[len(df1)]=newdata
  df1.to_csv("hwtime.csv")
  return True

def login(userid):    #maynot be that useful for this function as it require console, this one maybe require you to implement in the UI yourself
  '''complete=True      #changed to input user id and search through the csv about the person
  while(complete):
    print('please enter the userid')
    userid=input()'''
  df=pd.read_csv('user.csv',index_col=[0])
  df1=df[df['userid']==userid]
  if(not df1.empty):
    return userid,df1['cga'][0],True
  return False

def checkdeadlinefighter(user): #find the user past data, just input the data name and output true when he is a deadlinefighter, otherwise false
  now=datetime.datetime.now()   #if true maybe output some words that remind him as a deadline fighter
  now=now.timestamp()
  df=pd.read_csv('hwtime.csv',index_col=[0])  #df is the whole dataframe
  df1=df[df['userid']==user]  #df1:the hw submitted by user
  deadline=[]
  percentage=[]
  for i in df1.index:
    course=df1['coursecode'][i]
    index=df1['hwindex'][i]
    df2=df[df['coursecode']==course]
    df2=df2[df2['hwindex']==index]
    hours=int((df2['timehandin'].max()-df1['timehandin'][i])/3600)
    deadline=deadline+[hours]
    percentage+=[df2['timehandin'].rank(pct=True)[i]]

  #values, base = np.histogram(hours, bins=40)
  #print(values)
  #print(base)
  #base=base[:-1]
  #cumulative = np.cumsum(values)
  #print(cumulative)
  length=[]
  plt.scatter(deadline,(now-df1['timehandin'].rank())/86400)
  plt.xlabel('time you hand in hw before the last one handed in')
  plt.ylabel('how much time ago you hand in the hw')
  plt.xlim(left=0)
  j=0
  for i in deadline:
    plt.annotate(df1['coursecode'][df1.index[j]]+' '+df1['hwindex'][df1.index[j]],(i,(now-df1['timehandin'].rank()[df1.index[j]])/86400),size=6)
    j+=1
  #ax = plt.gca()
  #ax.get_yaxis().set_visible(False)
  #plt.show()
  plt.savefig("temp.png")
  """"
  temp=float(1-(sum(percentage)/len(percentage)))
  print('there are averagely',end='')
  print(temp,end='')
  print('% of people finish the hw earlier than you')
  """
  if((sum(percentage)/len(percentage))<0.5):
    return True
  else:
    return False


"""#initialization

initialing csv into ur google drive of file emia
"""
'''
#initialize user database
userdata={
    'userid':['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','test1','test2','test3','test4','test5','test6'],
    #'password':[],
    'cga':[3.6,3.7,2.5,2.6,3.0,2.4,2.7,3.6,2.7,3.3,3.4,2.8,2.9,3.1,3.4,3.5,3.2,3.9,3.4,2.6,3.7,3.1]
}
df=pd.DataFrame(userdata)
df.to_csv("user.csv")

#initialize the csv file(have different class and hwindex is fine)
#run one time is fine
#the main use of this is to build up a csv file in ur google drive
hwtimedata={  #22 rows
    'coursecode':['emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','emia2020','comp1021','emia2020','comp1021'],
    'hwindex':['hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw1','hw2','pa1','hw2','pa1'],
    'time':[200,210,220,220,240,250,260,260,260,260,280,290,290,300,300,340,350,360,500,540,123,120,130,140],
    'cga':[3.6,3.7,2.5,2.6,3.0,2.4,2.7,3.6,2.7,3.3,3.4,2.8,2.9,3.1,3.4,3.5,3.2,3.9,3.4,2.6,3.2,3.2,2.5,2.5], #do we need cga in the dataframe
    'userid':['a','b','c','d','e','f','h','i','j','k','l','m','n','o','p','q','test1','test2','test3','test4','test1','test1','c','c'],
    'timehandin':[1682000000,1681897564,1682123456,1682111111,168222222,1682111222,1681999999,1681888888,168000222,1681444444,1681224565,1681111111,1681546555,1681789456,1681237564,1682000000,1680000000,1682222374,1682229300,1682229274,1682300000,1678456123,1682355000,1678956123]
}
'''
'''
"""#main function"""

if __name__ == '__main__':
  run=True


  userid,cga=login()
  checkdeadlinefighter(userid)
  while(run):
    print("what do u want to do")
    print("1:serach hw time")
    print("2:upload ur homework finish time")
    print("3:exit")
    x=input()

    if(x=='1'):
      print("Please type in your course name")
      course_name=input()
      print('please enter the hwname(eg.hw1/pa1/hw2...)(not title):')
      hwindex=input()
      serachcourse(course_name,hwindex,cga)

    if(x=='2'):
      print("please enter the course code")
      course_code=input()
      print('please enter the hwname(eg.hw1/pa1/hw2...)(not title):')
      hwindex=input()
      print('please enter the time you finish by minutes')
      time=int(input())
      print('when have you finished this hw?(0 if u finish now and in format of YYYY-MM-DD)')
      finishtime=input()
      uploaddata(course_code,hwindex,time,userid,cga,finishtime)

    if(x=='3'):
      run=False'''
