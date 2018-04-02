# Scraping Google Scholar Citations

Google scholar doesn't have an API to download all the papers that cites yours. This hack loads all the citations on your profile page and enter each one to write its title/authors/proceeding in one txt file

## How to use 

Follow the instruction to install https://www.seleniumhq.org/

Change the url to your own google scholar page

```
#this is the main google scholar profile page
	driver.get("https://scholar.google.com/citations?user=aaTHLnkAAAAJ&hl=en&oi=sra")
```

Google might check if you're a robot. For that sake, I added a pause

```
when webpage is ready, click enter: 
```

Finish your Robot challenge if Google insists. After that, hit enter in commandline to keep going. 


## Built With

* [Selenium](https://www.seleniumhq.org/) - Automates browswers

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


