import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '../')))

#import Libraries for scraping using selenium
from selenium import webdriver  # for chrome open library for scraping
import time #time library for sleep
from selenium.webdriver.common.keys import Keys  # chrome keys libraries for input forms
from selenium.webdriver.common.action_chains import ActionChains #performing action libraries in chrome like Enter ESC
from bs4 import BeautifulSoup, NavigableString #Libraries to parse HTML
from werkzeug.wrappers import Response
from flask import Flask, request, send_file

#driver path for chrome browser
DRIVER_PATH = webdriver.Chrome(executable_path = r"/home/programmer-0/lushiv-git/daraz-scarper-app/chromedriver") #TODO: path get from config.ini

def get_daraz_data(payload):
    try:
        scraping_url = payload.get('scraping_url','')
        filename = payload.get('filename','')
        driver = DRIVER_PATH

        #list for all products URL save
        list1=[]

        #create CSV for Saving Data of scraping_url
        data=open(filename+'.csv','a',encoding="utf-8")

        #writing header for the FILE
        data.write("product_number,brand,product_name,price,image,product_detail,source_link,description,customer_options\n") #TODO: its manage from front in future task

        #First URL of DARAZ where scraping list
        URL = scraping_url
        for i in range(1,2): #loop for total number of pages in DARAZ
            # URL to open one by one
            URL = scraping_url+'?page='+str(i)
            #open that URL for finding the URLS of Every Product on that page
            driver.get(URL)  					
            print(URL)

            # Getting The META DATA of that page 				
            src=driver.page_source

            #parge that meta data in to HTML
            soup=BeautifulSoup(src,'html.parser')

            #Sleep for 2 seconds 
            time.sleep(2)
            #finding the URLS of products						
            urll=soup.findAll('div',{'data-qa-locator':'product-item'}) 
            for i in urll:
                #finding the Tag a in that div
                i=i.find('a')   
                print(i['href'])
                # now url is in the HREF
                list1.append(i['href'])    

        #now all the URLS i have in the list
        urllist=list1 
        #for priting the current product which is parsing at that time
        countproduct=0 	

        driver = DRIVER_PATH

        #parse one by one that product URL
        for i in urllist:
            #increment the current product one by one			
            countproduct=countproduct+1	
            #print the current product
            print('Product '+str(countproduct))
            #removing the end line for open link clearly
            i=i.replace('\n','')
            #apped https: in the URL 
            URL = 'https:'+str(i) 	
            driver.get(URL)			
            print(URL)				
            src=driver.page_source	
            soup=BeautifulSoup(src,'html.parser') 
            time.sleep(2) 
            
            #pdp-mod-product-badge-title
            brandtitle=''			
            #checking product Name
            #Checking the Brand Title Exist or not
            if(soup.find('span',{'class':'pdp-mod-product-badge-title'})):		
                #Getting the Brand Title 
                brandtitle=soup.find('span',{'class':'pdp-mod-product-badge-title'})
                #Now Parse the HTML and Get the text in the html tag of that span 	
                brandtitle=brandtitle.get_text()			
                brandtitle=brandtitle.strip()				
                brandtitle=brandtitle.replace(',','')		
                brandtitle=brandtitle.replace('.','')
                brandtitle=brandtitle.replace('\n','')
                brandtitle=brandtitle.replace('\t','')
                brandtitle=brandtitle.replace('"','')
                print(brandtitle)

            description=''			
            #checking product Name
            #Checking the Brand Title Exist or not
            if(soup.find('div',{'class':'pdp-product-detail'})):
                #Getting the Brand Title 		
                description=soup.find('div',{'class':'pdp-product-detail'})
                #Now Parse the HTML and Get the text in the html tag of that span 
                description=description.get_text()			
                description=description.strip()				
                description=description.replace(',','-')		
                description=description.replace('.','')
                description=description.replace('\n','')
                description=description.replace('\t','')
                description=description.replace('"','')
                print(description)

            customer_options_data=''			
            #checking product Name
            #Checking the Brand Title Exist or not
            if(soup.find('div',{'class':'sku-selector'})):		
                customer_options_data=soup.find('div',{'class':'sku-selector'})
                #Getting the Brand Title 
                customer_options_data=customer_options_data.get_text()
                #Now Parse the HTML and Get the text in the html tag of that span 			
                customer_options_data=customer_options_data.strip()				
                customer_options_data=customer_options_data.replace(',','-')		
                customer_options_data=customer_options_data.replace('.','')
                customer_options_data=customer_options_data.replace('\n','')
                customer_options_data=customer_options_data.replace('\t','')
                customer_options_data=customer_options_data.replace('"','')
                print(customer_options_data)					

            brandname=''				 
            #checking Brand Name
            if(soup.find('div',{'class':'pdp-product-brand'})):			
                brandname=soup.find('div',{'class':'pdp-product-brand'})	
                brandname=brandname.find('a')					
                brandname=brandname.get_text()					
                brandname=brandname.strip()						
                print(brandname)								
            
            price=''							
            #checking price
            if(soup.find('span',{'class':'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'})):			
                price=soup.find('span',{'class':'pdp-price pdp-price_type_normal pdp-price_color_orange pdp-price_size_xl'})			
                price=price.get_text()			
                price=price.strip()	
                price = price.replace(',','')		
                print(price)
                
            image=''
            if(soup.find('img',{'class':'pdp-mod-common-image gallery-preview-panel__image'})):		
                image=soup.find('img',{'class':'pdp-mod-common-image gallery-preview-panel__image'})		
                image=image.get('src')
                image=image.strip()			
                print(image)

            product_detail=''
            if(soup.find('h2',{'pdp-mod-section-title outer-title'})):		
                product_detail=soup.find('h2',{'class':'pdp-mod-section-title outer-title'})		
                product_detail=product_detail.get_text()
                product_detail=product_detail.strip()
                product_detail = product_detail.replace(',','')			
                print(product_detail)

            data.write('Product '+str(countproduct)+","+brandname+","+brandtitle+","+price+","+image+"," +product_detail+"," +URL+","+description+","+customer_options_data+",") #writing in the CSV
            data.write('\n')
        
        # Quit thefor Memory Cleaning and stop the process
        csv_dir  = os.getcwd()
        csv_file = filename +".csv"
        csv_path = os.path.join(csv_dir, csv_file)
        return send_file(csv_path, as_attachment=True, attachment_filename=csv_file)

    except Exception as e:
        print ({'error' : e})
        return False