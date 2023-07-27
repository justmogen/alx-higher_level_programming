#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charactersUrls = JSON.parse(body).characters;

    const fetchCharacterName = (characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);
        } else {
          console.error(`Error: Failed to retrieve character data. Status code: ${response.statusCode}`);
        }
      });
    };

    charactersUrls.forEach(fetchCharacterName);
  } else {
    console.error(`Error: Failed to retrieve movie data. Status code: ${response.statusCode}`);
  }
});
