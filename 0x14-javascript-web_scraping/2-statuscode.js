#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;

axios.get(process.argv[2])
  .then(function (response) {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
