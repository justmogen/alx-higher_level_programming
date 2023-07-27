#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Error: Movie ID not provided.');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movieData = JSON.parse(body);
      console.log(movieData.title);
    } else {
      console.error(`Error: Failed to retrieve movie data. Status code: ${response.statusCode}`);
    }
  }
});
