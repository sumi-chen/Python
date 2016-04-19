#coding:utf-8
import sys
import urllib2
import json
import smtplib

from email.mime.text import MIMEText

reload(sys)
#sys.setdefaultencoding('utf8')

mail_host="smtp.qq.com"
mail_user="1799689844@qq.com"
mail_pass="1662sda"
mailto_list=['18759884827@139.com']

def send_mail(to_list,sub,content):
    me="笑话来了"+"<"+mail_user+">"
    msg=MIMEText(content,_subtype='html',_charset='utf-8')
    msg['Subject']=sub
    msg['From']=me 
    msg['To']=";".join(to_list)
    try:
        s=smtplib.SMTP
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False

if __name__=='__main__': 
    appkey="e2376cfbe3b27dff923ed61698839a67"
    url='http://apis.baidu.com/showapi_open_bus/showapi_joke/joke_text?page=1'
    #req=urllib2.request_url(url)
    req=urllib2.Request(url)
    req.add_header("apikey",appkey)
    resp=urllib2.urlopen(req)
    content=resp.read()
    if content:
        json_result=json.loads(content)
        content_list=json_result['showapi_res_body']['contentlist']
        minlen=10000
        for item in content_list:
            if len(item['text'])<minlen:
                first_title=item['title'].encode('utf8')
                first_text=item['text'].encode('utf8')
                minlen=len(item['text'])  
        #first_title=content_list[0]['title']
        print 'title:'+first_title
        print 'content：'+first_text
        length=len(first_text)
        part1=first_text[0:10]
        part2=first_text[10:22]
        part3=first_text[22:length]
        part=part1+part2+part3
        print part1,"+",part2,"+",part3
        if send_mail(mailto_list,first_title,part):
            print "send msg succeed"
        else:
            print "send msg failed"
    else:
        print "get joke error"
