#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;
let cont = 0;

axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      const dict = response.data.results[i].characters;
      dict.forEach((link) => {
        if (link.search('18') !== -1) {
          /* con search busco que el link tenga el numero 18 */
          cont++;
        }
      });
    }
    console.log(cont);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
