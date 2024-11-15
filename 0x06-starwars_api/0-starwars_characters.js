#!/usr/bin/env node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode === 200) {
    const film = JSON.parse(body);
    const characters = film.characters;

    characters.forEach((characterUrl) => {
      request(characterUrl, (err, resp, charBody) => {
        if (!err && resp.statusCode === 200) {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  } else {
    console.error(`Failed to retrieve film with ID ${movieId}. Status code: ${response.statusCode}`);
  }
});
