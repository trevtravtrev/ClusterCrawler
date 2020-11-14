import re
from tldextract import extract


email_regex = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[
    a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[
    0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[
    \x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

phone_regex = r"""(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[
02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([
0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"""

phone_regex2 = r"""^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[
02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([
0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$"""

phone_regex3 = r"""(?:(?:\+?([1-9]|[0-9][0-9]|[0-9][0-9][0-9])\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[
2-9][02-8][02-9])\s*\)|([0-9][1-9]|[0-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][
02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?"""


email = """T-Mobile – number@tmomail.net
Virgin Mobile – number@vmobl.com
AT&T – number@txt.att.net
Sprint – number@messaging.sprintpcs.com
Verizon – number@vtext.com
Tracfone – number@mmst5.tracfone.com
Ting – number@message.ting.com
Boost Mobile – number@myboostmobile.com
U.S. Cellular – number@email.uscc.net
Metro PCS – number@mymetropcs.com
trevor@wayne.edu
twhite+42094@gmail.com
twhite434@gmail.com"""

email2 = "Hi my name is John and email address is john.doe@somecompany.co.uk and my friend's email is jane_doe124@gmail.com"

phone = """
Hello here is a phone number list: (734) 552-3120
+(313)456-7890
1(313)456-7890
(313)-456-7890
+(313) - 456-78-90
225-456-7890
313.456.7890
3424435545
+31336363634
075-63546725
(734)442-3233
+1(337)434-3293
7342384837
(313) 456-7890
775-456-7890
13135678390
754-3010
(541) 754-3010
+1-541-754-3010
1-541-754-3010
001-541-754-3011
191 541 754 3010
number with extension: 7345533627ext2344
01632 960722
phone: +44 1632 960723
hello
7234773734
2354235424532435243234
"""



def extract_emails():
    emails = re.finditer(email_regex, email)
    i = 0
    for mail in emails:
        print(i, mail.group())
        i += 1


def extract_phones():
    phones = re.finditer(phone_regex, phone)
    i = 0
    for number in phones:
        num = number.group()
        if len(num) > 7:
            print(i, num.strip('\n'))
        i += 1

def get_domain_from_url(url):
    result = extract(url)
    return f"{result.domain}.{result.suffix}"
