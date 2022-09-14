const axios = require("axios");
const cheerio = require("cheerio");
const pretty = require("pretty");
const fs = require("fs");

async function scrapeData() {
    try {
        const url = ["https://www.d3indepth.com/introduction",
                    "https://www.d3indepth.com/gettingstarted",
                    "https://www.d3indepth.com/selections",
                    "https://www.d3indepth.com/datajoins",
                    "https://www.d3indepth.com/enterexit",
                    "https://www.d3indepth.com/scales",
                    "https://www.d3indepth.com/shapes",
                    "https://www.d3indepth.com/axes",
                    "https://www.d3indepth.com/hierarchies",
                    "https://www.d3indepth.com/chords",
                    "https://www.d3indepth.com/force-layout",
                    "https://www.d3indepth.com/geographic",
                    "https://www.d3indepth.com/requests",
                    "https://www.d3indepth.com/transitions",
                    "https://www.d3indepth.com/interaction",
                    "https://www.d3indepth.com/zoom-and-pan"];

        const divDataArr = [];

        for (let link of url){
        
            // Fetch HTML of the page we want to scrape
            const { data } = await axios.get(link);
            // Load HTML we fetched in the previous line
            const $ = cheerio.load(data);
            // Select all the list items in plainlist class
            const divItem = $(".page-content");
            // Stores data for all countries
            const divText = divItem.text();
            //console.log(divText);     
            divDataArr.push(divText) 
        }
        
        console.log('writing the data to file...')
        
        fs.writeFile("siteData.txt", JSON.stringify(divDataArr, null,'\t'), (err) => {
            if (err) {
            console.error(err);
            return;
            }
            console.log("Successfully written data to file");
        });

      } catch (err) {
        console.error(err);
      }
}
    // Invoke the for loop with scraping function
scrapeData()