#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const baseUrl = 'https://swapi-api.alx-tools.com/api';

function getCharacterName (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const character = JSON.parse(body);
        resolve(character.name);
      }
    });
  });
}

function getMovieCharacters (movieId) {
  const movieUrl = `${baseUrl}/films/${movieId}/`;

  request(movieUrl, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    try {
      const movie = JSON.parse(body);
      const characterUrls = movie.characters;
      const characterPromises = characterUrls.map(url => getCharacterName(url));
      const characterNames = await Promise.all(characterPromises);
      characterNames.forEach(name => console.log(name));
    } catch (err) {
      console.error('Error processing movie data:', err);
    }
  });
}
getMovieCharacters(movieId);
