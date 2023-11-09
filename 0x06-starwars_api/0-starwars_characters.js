#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const movie = process.argv[2];
const api = 'https://swapi-api.hbtn.io/api/';
const url = api + 'films/' + movie + '/';
request.get({ url: url }, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    order(characters);
  }
});

function order (characters) {
  if (characters.length > 0) {
    request.get({ url: characters.shift() }, function (err, res, body) {
      if (!err) {
        console.log(JSON.parse(body).name);
        order(characters);
      }
    });
  }
}
