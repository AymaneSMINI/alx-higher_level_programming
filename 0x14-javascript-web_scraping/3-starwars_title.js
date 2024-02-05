#!/usr/bin/node
const request = require('request');
const id =  process.argv[2];
request.get(`https://swapi-api.alx-tools.com/api/films/${id}`).on('response', function (response, body) {
  const responseJSON = JSON.parse(body);
  console.log(responseJSON.title);
});
