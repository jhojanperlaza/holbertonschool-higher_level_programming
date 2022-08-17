#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;

const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

axios.get(url)
  .then(function (response) {
    /* if I want to make a request of
    all movies the command would be
    "console.log(response.data);" */
    console.log(response.data.title);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
