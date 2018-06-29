#Demo Program
#Read the page source or directory
#soup to break it into sections
#save sections in parallel arrays for product price, title, seller, post etc.
#write data to CSV file

from bs4 import BeautifulSoup
import csv
import urllib2
import os




def extractAndsaveData(pagefilePath, csvFile):
    product_titles = []
    product_prices = []
    selllers = []
    posts = []

    f = open(pagefilePath, "r")
    page = f.read()
    f.close()
    soup = BeautifulSoup(page)
    urlpage = ""
    page = urllib2.urlopen(urlpage)
    soup = BeautifulSoup(page, "html5lib")

    metaData = soup.find_all("dt")
    postData = soup.find_all("dd")

    print "Parsing data..for product, product price and seller."
    for html in metaData:
        text = BeautifulSoup(str(html).strip()).get_text().encode("utf-8").replace("\n", "")
        product_titles.append(text.split("Product_title:")[1].split("Post by:")[0].strip())
        product_prices.append(text.split("product_price:")[1].split(" on ")[0].strip())
        selllers.append(text.split("Seller:")[1].strip())


    for post in postData:
        posts.append(BeautifulSoup(str(post)).get_text().encode("utf-8").strip())

    csvfile = open(csvFile, 'ab') #append data
    writer = csv.writer(csvfile)


    writer.writerow(["Product_title", "Product_price", "Selller", "Post"])

    for product_title, product_price, selller, post in zip(product_titles, product_prices, selllers, posts):
        writer.writerow([product_title, product_price, selller, post])


    csvfile.close()


def main():
    dir = "/Users/vyas/dogeroad-forums/2014-01-20/" #configure Directory FilePath

    csvFile = "silkroad_forum.csv"
    csvfile = open(csvFile, 'wb')
    writer = csv.writer(csvfile)
    writer.writerow(["Product_title", "Product_price", "Selller", "Post"])
    csvfile.close()


    fileList = os.listdir(dir)
    totalLen = len(fileList)
    count = 1

    for htmlFile in fileList:
        pathHtml = os.path.join(dir, htmlFile)
        extractAndsaveData(pathHtml, csvFile)
        print "Processed '" + path + "'(" + str(count) + "/" + str(totalLen) + ")..."
        count = count + 1

if __name__ == "__main__":
    main()
