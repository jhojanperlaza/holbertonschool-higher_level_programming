#!/usr/bin/node
/*  script that display the status code of a GET reques */
const axios = require('axios').default;
const dictResult = {};

axios.get(process.argv[2])
  .then(function (response) {
    for (let x = 0; x < response.data.length; x++) {
      const dict = response.data[x];
      if (dict.completed === true) {
        const key = dict.userId.toString();
        if (key in dictResult) {
          /* mirar si la key esta en el diccionario */
          const newValue = dictResult[key] + 1;
          dictResult[key] = newValue;
        } else {
          dictResult[key] = 1;
        }
      }
    }
    console.log(dictResult);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
