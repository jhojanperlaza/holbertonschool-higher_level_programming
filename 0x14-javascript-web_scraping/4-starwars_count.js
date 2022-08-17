#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;
let cont = 0;

axios.get(process.argv[2])
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      const dict = response.data.results[i];
      for (const key in dict) {
        if (key === 'characters') {
          const array = dict[key];
          array.forEach((link) => {
            const linkReference = 'https://swapi-api.hbtn.io/api/people/18/';
            if (link === linkReference) {
              cont++;
            }
          });
        }
      }
    }
    console.log(cont);
  });
