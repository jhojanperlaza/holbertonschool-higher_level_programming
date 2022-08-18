#!/usr/bin/node
const axios = require('axios').default;
const url = 'https://swapi-api.hbtn.io/api/films/';

axios.get(url)
  .then(function (response) {
    for (let i = 0; i < response.data.results.length; i++) {
      if (i + 1 === parseInt(process.argv[2], 10)) {
        const dict = response.data.results[i].characters;
        dict.forEach((link) => {
          axios.get(link)
            .then(function (response) {
              console.log(response.data.name);
            });
        });
      }
    }
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
