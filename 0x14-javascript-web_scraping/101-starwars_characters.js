#!/usr/bin/node

const request = require('request');
const apiUrl = `https://swapi.dev/api/films/${process.argv[2]}/`;

request(apiUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const charactersUrls = JSON.parse(body).characters;
    let fetchedCharacters = 0;

    const fetchCharacterName = (characterUrl) => {
      request(characterUrl, function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          console.log(characterData.name);

          fetchedCharacters++;
          if (fetchedCharacters === charactersUrls.length) {
            // All characters fetched, exit the script
            process.exit(0);
          }
        } else {
          console.error(`Error: Failed to retrieve character data. Status code: ${response.statusCode}`);
          process.exit(1);
        }
      });
    };

    charactersUrls.forEach(fetchCharacterName);
  } else {
    console.error(`Error: Failed to retrieve movie data. Status code: ${response.statusCode}`);
    process.exit(1);
  }
});
