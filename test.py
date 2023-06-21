from bs4 import BeautifulSoup
import requests
import re
from flask import Flask, jsonify


url = "https://g01.digialm.com//per/g01/pub/1329/touchstone/AssessmentQPHTMLMode1/1329O231/1329O231S1D274/16869981227984868/AT2300008_1329O231S1D274E1.html"
page = requests.get(url)

page_content = BeautifulSoup(page.content, "lxml")
divsoup = page_content.find_all('table',class_="questionPnlTbl")
td_elements = page_content.find_all("td", class_="rightAns")
count = 0
correct_answers = []
sa ={}
qa = {}
va = {}
sa_score = 0
qa_score = 0
va_score = 0

main_info = page_content.find_all('div',class_="main-info-pnl")
user_info = {}
user_info["participant_id"] = re.search(r"Participant ID: (\w+)", main_info[0].text).group(1)
user_info["name"] = re.search(r"(?<=Participant Name: )\w+ \w+", main_info[0].text).group()
user_info["test_center_name"] = re.search('Test Center Name: (.*) Test Date', main_info[0].text).group(1)






# for i in td_elements:
#     # numbers = re.findall(r'>\d+', i)
#     if count <15 or count>=85:
#         correct_answers.append(i.text[17])
#         count += 1
#         continue
#     correct_answers.append(i.text[0])
#     count += 1

# answered = []
# for j in range(15):
    
#     pattern = r'Given Answer :(\d+)'
#     match = re.search(pattern, divsoup[j].text)
    
#     try:
#         extracted_number = match.group(1)
        
#         answered.append(extracted_number)
#     except:
#         answered.append(None)

# for j in range(15,85):
    
#     pattern = r'Chosen Option :(\d+)'
#     match = re.search(pattern, divsoup[j].text)
    
#     try:
#         extracted_number = match.group(1)
        
#         answered.append(extracted_number)
#     except:
#         answered.append(None)

# for j in range(85,90):
    
#     pattern = r'Given Answer :(\d+)'
#     match = re.search(pattern, divsoup[j].text)
    
#     try:
#         extracted_number = match.group(1)
        
#         answered.append(extracted_number)
#     except:
#         answered.append(None)

# for k in range(15):
    
#     if answered[k] is None:
#         sa["q"+str(k+1)] = "unanswered"
#     if answered[k] == correct_answers[k]:
#         sa["q"+str(k+1)] = "correct"
#         sa_score += 1
#     if answered[k] != correct_answers[k]:
#         sa["q"+str(k+1)] = "incorrect"
# sa["score"] = sa_score

# for k in range(15,45):
    
#     if answered[k] is None:
#         qa["q"+str(k-14)] = "unanswered"
#     if answered[k] == correct_answers[k]:
#         qa["q"+str(k-14)] = "correct"
#         qa_score += 1
#     if answered[k] != correct_answers[k]:
#         qa["q"+str(k-14)] = "incorrect"
#         qa_score -= 1
# qa["score"] = qa_score

# for k in range(45,90):
    
#     if answered[k] is None:
#         va["q"+str(k-44)] = "unanswered"
#     if answered[k] == correct_answers[k]:
#         va["q"+str(k-44)] = "correct"
#         va_score += 1
#     if answered[k] != correct_answers[k]:
#         va["q"+str(k-44)] = "incorrect"
#         va_score -= 1
# va["score"] = va_score

# okok = [sa,qa,va]