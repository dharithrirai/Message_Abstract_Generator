from tokenize import group
from urllib import request
from flask import Flask,request,jsonify
import json
from flask_cors import CORS
import requests
import ast

from transformers import pipeline

import shutil 


 
from reportlab.pdfgen import canvas
from reportlab.lib import colors

text=None

summary_path="F:\\000006\\Fask\\summary\\"

def pdf_generator(from_name,to_name,sub_info,sub_content):

    name_to=" " + from_name
    name_from=" " + to_name
    subject_info=" " + sub_info

    temp=" "
    new_text=[]
    fileName = from_name+".pdf"
    documentTitle = 'sample'
    title = 'LEGAL NOTICE'
    subTitle = 'ADVERSE ACTION LETTER'
    #textLines = "In this article, we will be learning how to create PDFs in Python. A very famous module named pypdf2 is used to modify and read existing pdfs but its major disadvantage is that it cannot create new pdf files. So Today we are looking to learn about another python module named reportlab that helps us to create new pdf files and edit our heart’s content on it."
    textlines = sub_content
    fromm='From:'+ name_from
    to='To:'+name_to
    subject="Subject:"+subject_info
    pdf = canvas.Canvas(fileName)
    array=[]

    pdf.setTitle(documentTitle)
    pdf.drawCentredString(300, 770, title)
    pdf.drawCentredString(60, 660, fromm)
    pdf.drawCentredString(50, 630, to)
    pdf.drawCentredString(60, 600, subject)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 720, subTitle)

    # drawing a line
    pdf.line(30, 710, 550, 710)
    text = pdf.beginText(40, 570)
    text.setFont("Courier", 12)
    text.setFillColor(colors.red)

    #word count
    array=textlines.split(' ')
    print(array)
    for i in range(len(array)):
        if(i%10!=0):
            temp=temp+array[i]+" "
        else:
            text.textLine(temp)
            temp=""
            i=0


    pdf.drawText(text)
    pdf.save()
    shutil.move(f'.\\{from_name}.pdf',f'{summary_path}\\{from_name}.pdf')

# Add a page
 

ip="192.168.137.1"
groupId='8b5298b7-d58b-491d-b734-ae3809beabc6'
URL=f'https://t2c-api-stage.solutionsbytext.com/groups/{groupId}/messages'

app=Flask(__name__)
CORS(app)
TOKEN="eyJhbGciOiJSUzI1NiIsImtpZCI6ImRyVjJrN1RTN3dFR0J6SnQyNVU4bHciLCJ0eXAiOiJhdCtqd3QifQ.eyJuYmYiOjE2NjcxOTE0NDgsImV4cCI6MTY2NzE5NTA0OCwiaXNzIjoiaHR0cHM6Ly9sb2dpbi1zdGFnZS5zb2x1dGlvbnNieXRleHQuY29tIiwiYXVkIjoidDJjYWNjb3VudHMiLCJjbGllbnRfaWQiOiJKOFZOMFVKVDZHVlM5UDNMSEoyNCIsInQyY0FjY291bnRJZCI6IjM0NjU5ZTlhLWUzMjEtNGYxYS05MGZjLWRiM2Q0YTJiNjIwNyIsInQyY0JyYW5kSWQiOiIwNmFmZTZkZi0zZmVjLTRkMDktYmQ0MS02NDYwMzk4ZTA0MmIiLCJpc0JyYW5kQ2xpZW50IjoidHJ1ZSIsImFwaV9jbGllbnQiOiJ0cnVlIiwidGVuYW50X2lkIjoiOTMxNDcwOTAtNjgwYS00OTE3LWEzYWItOTdiZTk4ZjBhNmUzIiwianRpIjoiaUFidzBYdXZWTFlIN3dteWFQRWg2USIsInNjb3BlIjpbInQyYy5hY2NvdW50LmluZm86ciIsInQyYy5hY2NvdW50Lmxvb2t1cDpyIiwidDJjLmFjY291bnQucmVwb3J0czpyIiwidDJjLmJyYW5kOnIiLCJ0MmMuYnJhbmQuYWxsX2dyb3VwczpyIiwidDJjLmJyYW5kLnJlcG9ydHM6ciIsInQyYy5ncm91cC5rZXl3b3JkczptIiwidDJjLmdyb3VwLm1lc3NhZ2VzOnJ3IiwidDJjLmdyb3VwLnNjaGVkdWxlX21lc3NhZ2VzOnJ3IiwidDJjLmdyb3VwLnNjaGVkdWxlX3RlbXBsYXRlbWVzc2FnZXM6cnciLCJ0MmMuZ3JvdXAuc3Vic2NyaWJlcnM6bSIsInQyYy5ncm91cC5zeXN0ZW1fbWVzc2FnZXM6cnciLCJ0MmMuZ3JvdXAudGVtcGxhdGVtZXNzYWdlOnJ3IiwidDJjLmdyb3VwLnRlbXBsYXRlczptIiwidDJjLnNtYXJ0Y2xpY2s6cnciLCJ0MmMuc21hcnRjbGljay5yZXBvcnRzOnIiXX0.G0pWS3DpfZdAU64tTvw7tSE4yifDep010QvjXJ5vzg4f3oANSg2pOvCtAJC5AyAbxgnunuzooMtPA0n5FaOYVMzFzVMScJSuzFRVjfdFUG914bLN2GKv0zDv_zTFh2rKpfrtC1WUvfM5Bd1moqj-MU5rKG_ajCUxh3OA1_Dd6KCJkse3bstPjyrwRGT_CSraTIwPcJunj059vGZ9cgaGa4u2f85CnDEdLikiRTTLtUFD3W8QnmKsPkHGf6Rb8M5S4YjoUcKwjzELbklW2ii_1SThcfBS-hxu9Nf46Jlg-MCopul2DqsLAN2uOQAmoxAyka9KCD6IZLgz3rgcKnJQRw"
#TOKEN=''
REQ_DATA={
  "from": "string",
  "message": "message from d3a squad",
  "messageType": "BroadcastMessage",
  "referenceId": "string",
  "variables": [
    {
      "name": "string",
      "value": "string"
    }
  ],
  "subscribers": [
    {
      "msisdn": "15712297714",
      "variables": [
        {
          "name": "string",
          "value": "string"
        }
      ]
    }
  ]
}


@app.route('/')
def home():
    return '<h1>HOME</h1>'

@app.post("/generate")
def summerizer():
    data =json.loads(request.data)
    print(data)
    file_name=data['name']+'.pdf'
    res={}
    
    summarizer = pipeline("summarization")
     
    output=summarizer(data['content'],min_length=30 , max_length=320, do_sample=False)
    print(output[0]['summary_text'])
    pdf_generator(data['name'],data['to'],data['subject'],data['content'])
    res['pdfurl']=summary_path+file_name
    res['summary']=output[0]['summary_text']
    
    return jsonify(res),200

@app.post('/send')
def send():
    print('coming')
    data =json.loads(request.data)
    print(data)
    headers = {'Content-Type': 'application/json',"Authorization": f'Bearer {TOKEN}'}
    # res=requests.post(f'{py_ip.ip}:5000/api/auth/register',headers=headers,data=json.dumps(datas))
    REQ_DATA["message"]=f'{data[2]},{data[1]}'
    res=requests.post(URL,headers=headers,data=json.dumps(REQ_DATA))
    # dict=ast.literal_eval(res.text)
    res_data=json.loads(res.text)
    print(res_data)
    if(res_data['appCode']==401):
        return jsonify({"message":"Unauthorized"} ),401
    else:
        return jsonify({"message":"message sent"} ),200

  


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 5000)
