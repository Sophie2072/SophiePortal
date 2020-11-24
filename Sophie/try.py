string = '[{"id":1,"start":"2020-01-01T12:00:00+00:00","end":"2020-01-01T16:00:00+00:00","extendedProps":{"is_final":false},"title":"#1: Job (4.00h)","notes":"","borderColor":"rgb(154,99,36)","backgroundColor":"rgba(154,99,36,0.75)"}'

if not string == "":
    print("OKK")
else:
    print("STRING is empty")

print(string.decode("utf-8"))
