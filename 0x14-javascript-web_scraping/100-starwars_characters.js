#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Movie ID not provided.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    const fetchCharacters = (urls) => {
      if (urls.length === 0) {
        return;
      }

      const characterUrl = urls.shift();

      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error(`Error: Failed to retrieve character data. Status code: ${response.statusCode}`);
        }

        fetchCharacters(urls);
      });
    };

    fetchCharacters(charactersUrls);
  } else {
    console.error(`Error: Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
