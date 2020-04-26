import urllib3   #https://urllib3.readthedocs.io/en/latest/
import json
import pickle
import datetime

http = urllib3.PoolManager()

'''
total_cases - 0
total_recovered - 1
total_deaths - 2
total_new_cases_today - 3
total_new_deaths_today - 4
total_active_cases - 5
'''
countries = {'AF': 'Afghanistan', 'AL': 'Albania', 'DZ': 'Algeria', 'AO': 'Angola', 'AR': 'Argentina', 'AM': 'Armenia', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BD': 'Bangladesh', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BT': 'Bhutan', 'BO': 'Bolivia', 'BA': 'Bosnia', 'BW': 'Botswana', 'BR': 'Brazil', 'BN': 'Brunei', 'BG': 'Bulgaria', 'BF': 'Burkina', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CF': 'Central', 'TD': 'Chad', 'CL': 'Chile', 'CN': 'China', 'CO': 'Colombia', 'CG': 'Congo', 'CR': 'Costa', 'HR': 'Croatia', 'CU': 'Cuba', 'CY': 'Cyprus', 'CZ': 'Czechia', 'CD': 'DR', 'DK': 'Denmark', 'DP': 'Diamond', 'DJ': 'Djibouti', 'DO': 'Dominican', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El', 'GQ': 'Equatorial', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French', 'TF': 'French', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GR': 'Greece', 'GL': 'Greenland', 'GT': 'Guatemala', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HN': 'Honduras', 'HK': 'Hong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran', 'IQ': 'Iraq', 'IE': 'Ireland', 'IL': 'Israel', 'IT': 'Italy', 'CI': 'Ivory', 'JM': 'Jamaica', 'JP': 'Japan', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KP': 'North', 'XK': 'Republic', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': 'Lao', 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MK': 'Macedonia', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'ML': 'Mali', 'MR': 'Mauritania', 'MX': 'Mexico', 'MD': 'Moldova', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New', 'NZ': 'New', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PS': 'Palestine', 'PA': 'Panama', 'PG': 'Papua', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto', 'QA': 'Qatar', 'RO': 'Romania', 'RU': 'Russia', 'RW': 'Rwanda', 'SA': 'Saudi', 'SN': 'Senegal', 'RS': 'Serbia', 'SL': 'Sierra', 'SG': 'Singapore', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon', 'SO': 'Somalia', 'ZA': 'South', 'KR': 'South', 'SS': 'South', 'ES': 'Spain', 'LK': 'Sri', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian', 'TW': 'Taiwan', 'TJ': 'Tajikistan', 'TZ': 'Tanzania', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TT': 'Trinidad', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'AE': 'UAE', 'UG': 'Uganda', 'UA': 'Ukraine', 'GB': 'United', 'UY': 'Uruguay', 'US': 'USA', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela', 'VN': 'Vietnam', 'EH': 'Western', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}

def update_data():
    update_data = {}
    for c in countries.keys():
        response = http.request('GET','https://api.thevirustracker.com/free-api?countryTotal=%s'%(c))
        data = response.data #byte
        data = data.decode('utf8') #converting byte to string
        data = json.loads(data)
        data = data['countrydata'][0]
        update_date = datetime.datetime.now().date().strftime("%d/%m/%Y")
        update_data[c] = [data['total_cases'], data['total_recovered'], data['total_deaths'], data['total_new_cases_today'], data['total_new_deaths_today'], data['total_active_cases'], update_date]
        #print(update_data)
    with open('virus_data.pickle', 'wb') as handle:
        pickle.dump(update_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print("Data Updated")

