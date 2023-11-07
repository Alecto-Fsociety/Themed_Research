import requests,random,pathlib,itertools,sys,time
from bs4 import BeautifulSoup
from pprint import pprint 


target_url = "https://www.jaspa.or.jp/mechanic/past/2022/2nd.html"

def get_links(html_number=["1st.html","2nd.html"],list_link=[]):

    url = "https://www.jaspa.or.jp/mechanic/past/"

    for year in range(2004,2019):
        for html in html_number:
            
            list_link.append(f"{url}{year}/{html}")
    return list_link


def get_tages_update(link_date,base_link="https://www.jaspa.or.jp/"):

    res_html = requests.get(link_date).text

    soup = BeautifulSoup(res_html,"html.parser")

    tages_date = [tages.a.get("href") for tages in soup.td.find_all("strong")]

    return tages_date
    
    
        
def get_tages(target_name,path_name="pdf_path",cycle=itertools.cycle(r"/-\|")):

    url_date = "https://www.jaspa.or.jp"

    soup = BeautifulSoup(target_name,"html.parser")

    tage_date = [date_tage.a.get("href") for date_tage in soup.td.find_all("strong")]

    #date = (tage_date[0]).split("/")[9]

    #file_name = date.split(".")[0]

    pathlib.Path(path_name).mkdir(exist_ok=True)

    for tage_link in tage_date:

        file_name = tage_link.split("/")[9]

        year = tage_link.split("/")[8]

        url_pdf = url_date + tage_link

        sys.stdout.write("\r")
        sys.stdout.write(f"{year} / {file_name} ~ {next(cycle)}")
        sys.stdout.flush()

        pdf_res = requests.get(url_pdf).content
 
        pathlib.Path("")
        with open(f"{path_name}/{file_name}","wb+")as pdf_file:

             pdf_file.write(pdf_res)

        #time.sleep(1)

def test_main(list_date):

    for date in list_date:

        print(date.split("/"))
       
def main():
    #random_link = random.choice(get_links())
    #date_link = get_tages_update(random_link)
    #print(date_link)
    for link in get_links():
        get_tages(requests.get(link).text)
       
if __name__ == "__main__":

  main()
  

