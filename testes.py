import smtplib


server = smtplib.SMTP(local_hostname='notebook', host='192.168.72.2', port='5432')
server.sendmail(from_addr='cleiton_biou@hotmail.com',to_addrs=5, msg="To: cleiton_tebit@homail.comFrom: cleiton_biou@hotmail.comBEWATE THE IDES OFMARCH. ")
server.quit()