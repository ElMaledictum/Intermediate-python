import smtplib
import datetime as dt

date = dt.datetime.now()
year = date.year
month = date.month
day = date.day
weekday = date.weekday() #0 for MOnday, 6 for Sunday
# print (year, month, day)

# birth_date = dt.datetime(year=1995, month=12, day=15)
# print (birth_date)


email_g = "pytest.mailgoog@gmail.com"
email_y = "pytest.mailym@yahoo.com"
password = "Pdu6gydoop"

if weekday ==6:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls() #encrypt email
        connection.login(user=email_g, password=password)
        connection.sendmail(from_addr=email_g, to_addrs=email_y,
        msg="Subject:It's Sunday\n\nGood Sunday to you!")


 
