import requests
from bs4 import BeautifulSoup

headers = {
    'authority': 'www.skysports.com',
    'cache-control': 'max-age=0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'sec-fetch-dest': 'document',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'referer': 'https://www.google.com/',
    'accept-language': 'en-IE,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6,zh-TW;q=0.5',
    '$cookie': 'check=true; AMCVS_0ABA4673527831C00A490D45%40AdobeOrg=1; AMCV_0ABA4673527831C00A490D45%40AdobeOrg=1406116232%7CMCIDTS%7C18359%7CMCMID%7C70144093986199053473887472973299229673%7CMCAAMLH-1586747096%7C6%7CMCAAMB-1586747096%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1586149496s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C2.5.0; consentUUID=39555651-308e-4b9b-89a1-2f90a401deac; _cb_ls=1; _cb=BaHFxcDtfOmpBUhPDG; _chartbeat2=.1586142297598.1586142297598.1.5VN9VD_dJnuDSM3b5CGr-H62nFq-.1; _cb_svref=https%3A%2F%2Fwww.google.com%2F; _sp_v1_uid=1:167:40e4c297-d4d0-4326-98be-8b64cb0b1789; _sp_v1_ss=1:H4sIAAAAAAAAAItWqo5RKimOUbKKxsrIAzEMamN1YpRSQcy80pwcILsErKC6lgwJpVgAEA5-UnQAAAA%3D; _sp_v1_csv=2.0.1190; _sp_v1_lt=1:msg|true:; __gads=ID=689c528f06e23ad6:T=1586142297:S=ALNI_MbZYTrQngnrH9wLie5kAQ7e6gJ2PA; s_sq=bskybdtmskysportsprod%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fwww.skysports.com%25252Fpremier-league-table%2526link%253DAccept%2526region%253Dsp_choices%2526.activitymap%2526.a%2526.c; _sp_v1_data=2:35319:1586142297:0:1:-1:1:0:0:c74365eb-a04c-49d9-ac41-4f75a12751c5:49817; _sp_v1_opt=1:login|true:last_id|11:; c=undefinedwww.google.comwww.google.com; s_ctq=1; s_cc=true; euconsent=BOxahuXOxahuXAGABBENDE-AAAAu1guYXCiIQ4XJlBwBJAQAECuEgCDEgAAUDAAPAgARpwAiCAEgQAAgQUgAAkAAEAQIBRBAAAAQAgAAAgBBAAACAAAAEAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA; _sp_enable_dfp_personalized_ads=true; polaris-engine-test=prospect%3Dtrue%2Cany_tv%3Dfalse; aam_tnt=seg%3D1901449; aam_uuid=70035516328028599933862603208280667507; _sp_v1_consent=1\\u00211:1:-1:-1; ecos.dt=1586142404674',
    'if-none-match': '082d8e0f730207f314d5b982f83fc5c88cdf0d3d',
}

def page_to_soup():
    response = requests.get('https://www.skysports.com/premier-league-table', headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def table_data(soup):
	rows = soup.find_all('tr')
	for row in rows: 
		row = row.text.strip().replace('\n',',').replace(',,', ',')
		if len(row) == 0:
			print('"0"',)
		else:
			print(row,)
# 		return row   # uncomment this line of code for unittest

def main():
    soup = page_to_soup()
    table_data(soup)
    
if __name__ == '__main__':
    main()