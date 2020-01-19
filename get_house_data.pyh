from bs4 import BeautifulSoup
import seaborn as sns
from urllib.request import Request, urlopen
import re
sns.set()
#to run
# run then enter URL
zipcode = input('Enter zipcode:')
url = "https://www.zillow.com/homes/"+zipcode+"_rb/"

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

# Creating a BeautifulSoup object of the html page for easy extraction of data.
soup = BeautifulSoup(webpage, 'html.parser')
html = soup.prettify('utf-8')

test = soup.find_all("article",class_="list-card list-card-short list-card_not-saved")
test2 = soup.find_all("a",class_="list-card-link list-card-info")

def recurse_search(element,depth,maxdepth):
    children = element.findChildren()
    output = []
    depth += 1
    if depth >= maxdepth:
        return output
    for i in children:
        i_value = i.text
        if i_value:
            if re.search("(li)|(div)|(span)",i.name):
                output.append(i_value.replace("\n","")+":"+i.name.replace("\n",""))
        output += recurse_search(i,depth,maxdepth)
    return list(dict.fromkeys(output))

def search_house_site(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    house_soup = BeautifulSoup(webpage, 'html.parser')
    t = house_soup.find_all("li",class_="ds-home-fact-list-item")
    t_test = house_soup.find_all("div",class_="ds-home-details-chip")[0]
    out = {}
    for i in t_test:
        output = recurse_search(i, 0, 2)
        for x in output:
            if re.search("^\$.*span$",x):
                out["p"] = x.replace(":span","")

            x = x.replace(":span","")
            if re.search("[0-9]+ sqft$",x):
                out["sqft"] = x
            if re.search("[0-9]+ bd$",x):
                out["bd"] = x
            if re.search("[0-9]+ ba$",x):
                out["ba"] = x

    for i in t:
        output = recurse_search(i, 0, 3)
        out[output[0].replace("::span","")] = output[-1].replace(":span","")
    return out

csv_houses = []
for t in test2:
    link = t['href']
    print(link)
    try:
        house_info = search_house_site(link)
        if len(house_info) >= 7:
            csv_houses.append(house_info)
        #output = recurse_search(t,0,3)
    except Exception as e:
        print(e)

    #for i in output:
    #    print(i)
    print("Next House")
    #print(output.join("\n"))


csv_columns = ['price','sqft','Type',"Year Built","Heating","Cooling","Parking","Lot","Price/sqft","Year built","Deposit & fees"]
csv_file = "houses.csv"

try:
    with open(csv_file, 'w') as csvfile:
        for line in csv_houses:
            try:
                price = line["p"].replace(",","")
                sqft = line["sqft"].replace(",","")
                type = line["Type"]
                #built = line["Year built"]
                bd = ""
                ba = ""
                if line["bd"]:
                    bd = line["bd"]

                if line["ba"]:
                    ba = line["ba"]
                out = price+","+ sqft+","+ type+","+ bd+","+ ba+"\n"
                csvfile.write(out)
            except Exception as e:
                print(e)
except Exception as e:
    print(e)

#Price
# Area
# bedrooms
# bathrooms
# type
# furneshed
# distance from downtown
