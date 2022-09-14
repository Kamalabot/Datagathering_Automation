import fetch from 'node-fetch';	//npm install node-fetch
/*
const myData = [];

fetch('https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json')
  .then(res => res.json())
  .then(mainJson => {
    const libArray = mainJson['rows'];
    //console.log(libArray.slice(0,10))
    for (let obj of libArray.slice(0,10)){
      const pkg = obj["project"];
      //console.log(pkg)
      fetch(`https://libraries.io/api/Pypi/${pkg}?api_key=598f29e15e3a1e7ac5df0b0b43b67711`)
      .then(res => res.json())
      .then(json => {
          const result ={
                    "dependent_repos_count" : json["dependent_repos_count"],
                    "dependents_count":json["dependents_count"],
                    "description":json["description"]
                  }
          myData.push(result)
          //console.log(myData)
      })
      .catch(err => console.log(err));
      } //closing for loop
    })
.catch(err => console.log(err));
console.log(myData)
*/

fetch('https://hugovk.github.io/top-pypi-packages/top-pypi-packages-30-days.json')
  .then(res => res.json())
  .then(mainJson => {
    const libArray = mainJson['rows'];
    //console.log(libArray.slice(0,10))
    mainJson['dependency'] = [];
    libArray.slice(0,10).forEach(element => {
      const pkg = element["project"];
      //console.log(pkg)
      const data = fetch(`https://libraries.io/api/Pypi/${pkg}?api_key=598f29e15e3a1e7ac5df0b0b43b67711`)
      .then(res => res.json())
      .then(json => {
          const result ={
                    "dependent_repos_count" : json["dependent_repos_count"],
                    "dependents_count":json["dependents_count"],
                    "description":json["description"]
                  }
          mainJson['dependency'].push(result)
          //console.log(myData)
      })
      .catch(err => console.log(err));
    })
    console.log(data)
  })
.catch(err => console.log(err));

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
