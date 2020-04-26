import pickle
import discord
from discord.ext import commands
import data
import matplotlib.pyplot as plt
import urllib3
import json

token = 'your token from discord'

virus_data = {}

update_flag = False

visual_types = ['pie','line']

def update_local():
    with open('virus_data.pickle', 'rb') as handle:
        local_data = pickle.load(handle)
        return local_data

try:
    virus_data = update_local()
except:
    print("No data. Collecting now")
    data.update_data()
    virus_data = update_local()

'''
total_cases - 0
total_recovered - 1
total_deaths - 2
total_new_cases_today - 3
total_new_deaths_today - 4
total_active_cases - 5
'''

countries = {'AF': 'Afghanistan', 'AL': 'Albania', 'DZ': 'Algeria', 'AO': 'Angola', 'AR': 'Argentina', 'AM': 'Armenia', 'AU': 'Australia', 'AT': 'Austria', 'AZ': 'Azerbaijan', 'BS': 'Bahamas', 'BD': 'Bangladesh', 'BY': 'Belarus', 'BE': 'Belgium', 'BZ': 'Belize', 'BJ': 'Benin', 'BT': 'Bhutan', 'BO': 'Bolivia', 'BA': 'Bosnia', 'BW': 'Botswana', 'BR': 'Brazil', 'BN': 'Brunei', 'BG': 'Bulgaria', 'BF': 'Burkina Faso', 'BI': 'Burundi', 'KH': 'Cambodia', 'CM': 'Cameroon', 'CA': 'Canada', 'CF': 'Central', 'TD': 'TChad', 'CL': 'Chile', 'CN': 'China', 'CO': 'Colombia', 'CG': 'Congo', 'CR': 'Costa Rica', 'HR': 'Croatia', 'CU': 'Cuba', 'CY': 'Cyprus', 'CZ': 'Czechia', 'CD': 'DR Congo', 'DK': 'Denmark', 'DP': 'Diamond', 'DJ': 'Djibouti', 'DO': 'Dominican', 'EC': 'Ecuador', 'EG': 'Egypt', 'SV': 'El Salvador', 'GQ': 'Equatorial', 'ER': 'Eritrea', 'EE': 'Estonia', 'ET': 'Ethiopia', 'FK': 'Falkland', 'FJ': 'Fiji', 'FI': 'Finland', 'FR': 'France', 'GF': 'French', 'TF': 'French', 'GA': 'Gabon', 'GM': 'Gambia', 'GE': 'Georgia', 'DE': 'Germany', 'GH': 'Ghana', 'GR': 'Greece', 'GL': 'Greenland', 'GT': 'Guatemala', 'GN': 'Guinea', 'GW': 'Guinea-Bissau', 'GY': 'Guyana', 'HT': 'Haiti', 'HN': 'Honduras', 'HK': 'Hong Kong', 'HU': 'Hungary', 'IS': 'Iceland', 'IN': 'India', 'ID': 'Indonesia', 'IR': 'Iran', 'IQ': 'Iraq', 'IE': 'Ireland', 'IL': 'Israel', 'IT': 'Italy', 'CI': 'Ivory', 'JM': 'Jamaica', 'JP': 'Japan', 'JO': 'Jordan', 'KZ': 'Kazakhstan', 'KE': 'Kenya', 'KP': 'North Korea', 'XK': 'Republic of Kosovo', 'KW': 'Kuwait', 'KG': 'Kyrgyzstan', 'LA': 'Lao', 'LV': 'Latvia', 'LB': 'Lebanon', 'LS': 'Lesotho', 'LR': 'Liberia', 'LY': 'Libya', 'LT': 'Lithuania', 'LU': 'Luxembourg', 'MK': 'Macedonia', 'MG': 'Madagascar', 'MW': 'Malawi', 'MY': 'Malaysia', 'ML': 'Mali', 'MR': 'Mauritania', 'MX': 'Mexico', 'MD': 'Moldova', 'MN': 'Mongolia', 'ME': 'Montenegro', 'MA': 'Morocco', 'MZ': 'Mozambique', 'MM': 'Myanmar', 'NA': 'Namibia', 'NP': 'Nepal', 'NL': 'Netherlands', 'NC': 'New', 'NZ': 'New', 'NI': 'Nicaragua', 'NE': 'Niger', 'NG': 'Nigeria', 'NO': 'Norway', 'OM': 'Oman', 'PK': 'Pakistan', 'PS': 'Palestine', 'PA': 'Panama', 'PG': 'Papua', 'PY': 'Paraguay', 'PE': 'Peru', 'PH': 'Philippines', 'PL': 'Poland', 'PT': 'Portugal', 'PR': 'Puerto', 'QA': 'Qatar', 'RO': 'Romania', 'RU': 'Russia', 'RW': 'Rwanda', 'SA': 'Saudi', 'SN': 'Senegal', 'RS': 'Serbia', 'SL': 'Sierra', 'SG': 'Singapore', 'SK': 'Slovakia', 'SI': 'Slovenia', 'SB': 'Solomon', 'SO': 'Somalia', 'ZA': 'South Africa', 'KR': 'South Korea', 'SS': 'South Sudan', 'ES': 'Spain', 'LK': 'Sri Lanka', 'SD': 'Sudan', 'SR': 'Suriname', 'SJ': 'Svalbard', 'SZ': 'Swaziland', 'SE': 'Sweden', 'CH': 'Switzerland', 'SY': 'Syrian', 'TW': 'Taiwan', 'TJ': 'Tajikistan', 'TZ': 'Tanzania', 'TH': 'Thailand', 'TL': 'Timor-Leste', 'TG': 'Togo', 'TT': 'Trinidad', 'TN': 'Tunisia', 'TR': 'Turkey', 'TM': 'Turkmenistan', 'AE': 'UAE', 'UG': 'Uganda', 'UA': 'Ukraine', 'GB': 'United', 'UY': 'Uruguay', 'US': 'USA', 'UZ': 'Uzbekistan', 'VU': 'Vanuatu', 'VE': 'Venezuela', 'VN': 'Vietnam', 'EH': 'Western', 'YE': 'Yemen', 'ZM': 'Zambia', 'ZW': 'Zimbabwe'}

def create_c_list(list_of_c):
    c_list_embed = discord.Embed(title = "Country Codes", description = "", color=0x0099ff)
    for key in list_of_c:
        c_list_embed.add_field(name = key, value = countries[key], inline = False)
        print(key, countries[key])
    return c_list_embed

client = commands.Bot(command_prefix='.')
client.remove_command('help')

@client.event
async def on_ready():
    print("I am ready")

@client.command()
async def stats(ctx, *args):
    for c in args:
        c = c.upper()
        if c in countries:
            c_data = virus_data[c]
            case_data = discord.Embed(title = countries[c], description="", color=0xeee657)
            case_data.add_field(name="Total cases", value = c_data[0])
            case_data.add_field(name="Total recovered", value = c_data[1])
            case_data.add_field(name="Total deaths", value = c_data[2])
            case_data.add_field(name="Total new cases today", value = c_data[3])
            case_data.add_field(name="Total new deaths today", value = c_data[4])
            case_data.add_field(name="Total active cases", value = c_data[5])
            case_data.set_author(name = "")
            case_data.set_footer(text = "Date: %s"%(c_data[6]))
            await ctx.send(embed = case_data)
        else:
            not_found = discord.Embed(title = "!Ops", description = "%s not found"%(c), color=0xff0000)
            not_found.add_field(name = "help:", value = "Use .ls to search for country codes")
            await ctx.send(embed = not_found)

@client.command()
async def visual(ctx, v_type, country):
    if v_type in visual_types and country in countries:
        if v_type == 'pie':
            c_data = virus_data[country]
            labels = ['Active: %i'%(c_data[5]), 'Recovered: %i'%(c_data[1]), 'Dead: %i'%(c_data[2])]
            sizes = [c_data[5], c_data[1], c_data[2]]
            colors = ['yellowgreen', 'gold', 'lightskyblue']
            fig = plt.figure(facecolor = 'dimgrey', edgecolor='k', linewidth= 2.0, frameon=True)
            pie = plt.pie(sizes,colors = colors , autopct='%1.1f%%', shadow = False, startangle=90)
            plt.legend(pie[0], labels, loc="best")
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig('pie.png', facecolor=fig.get_facecolor())
            await ctx.send(file=discord.File('pie.png'))
        
        elif v_type == 'line':
            http = urllib3.PoolManager()
            response = http.request('GET','https://api.thevirustracker.com/free-api?countryTimeline=%s'%(country))
            data = response.data #byte
            data = data.decode('utf8') #converting byte to string
            data = json.loads(data)
            data = data['timelineitems'][0]
            dates = list(data.keys())
            values = []
            for x in data.keys():
                if x != 'stat' :
                    values.append(data[x]["total_cases"])
            dates = dates[:len(dates) -1:]
            fig = plt.figure(figsize = (80,20))
            plt.plot(dates,values, color="#ff0000", linewidth=3)
            plt.gcf().autofmt_xdate()
            plt.grid()
            plt.savefig('plt.png')
            await ctx.send(file=discord.File('plt.png'))
        else:
            await ctx.send("Invalid visual")

@client.command()
async def ping(ctx):
    ping = discord.Embed()
    ping.add_field(name = "Ping", value = "Latency: %ims"%(round(client.latency * 1000)))
    await ctx.send(embed = ping)

@client.command()
async def update(ctx):
    global update_flag
    
    if update_flag == False:
        try:
            global virus_data
            update_flag = True
            await ctx.send("Updating. Please Wait")
            data.update_data()
            virus_data = update_local()
            await ctx.send("Data Updated")
            update_flag = False
        
        except:
            update_flag = False
    else:
        print("Update in progess")

@client.command()
async def ls(ctx, args = '-'):
    args = str(args)
    if len(args) == 1 and args.isupper():
        c_list = [t for t in countries if t.startswith(args)]
        await ctx.send(embed = create_c_list(c_list))
    else:
        no_c = discord.Embed(title = "Ops!!", description = "Specify a Letter", color=0xff0000)
        await ctx.send(embed = no_c)

@client.command()
async def help(ctx):
    help_embed = discord.Embed(title = "HELP", description = "", color = 0x6fff00)
    help_embed.add_field(name = "What am I?", value = "A bot to help you keep updated with the COVID-19 cases", inline = False)
    help_embed.add_field(name = "How to Use?", value = 'Here are the list of commands', inline = False)
    help_embed.add_field(name = ".stats [cc] [cc] [cc] ...", value = 'shows country stats', inline = False)
    help_embed.add_field(name = ".visual [visual_type] [cc]", value = 'shows visual reprensentation', inline = False)
    help_embed.add_field(name = "visual types:", value = 'pie - pice chart', inline = False) 
    help_embed.add_field(name = ".ls <First letter of Country Code>", value = 'Shows list of Country codes', inline = False)
    help_embed.add_field(name = ".update", value = 'Update data', inline = False)
    help_embed.add_field(name = ".ping", value = "Bot's latency to server", inline = False)
    help_embed.set_footer(text = "cc: country code")
    await ctx.send(embed = help_embed)

client.run(token)
