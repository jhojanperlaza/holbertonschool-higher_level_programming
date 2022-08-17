#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;
const fs = require('fs');

axios.get(process.argv[2])
  .then(function (response) {
    fs.writeFile(process.argv[3], response.data, err => {
      if (err) {
        console.error(err);
      }
    });
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
