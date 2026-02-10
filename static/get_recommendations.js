document.getElementById('recs-form').addEventListener('submit', function (event) {event.preventDefault();
    /* getElementById() retrieves an object with the specified id.
       .value retrieves the value of the selected button.

       querySelector('input[name="artist-gender"]:checked') retrieves an object that is currently checked.
       
       querySelectorAll('input[name="artist-region"]:checked') retrives all the objects the user selected.
    */
    let trackTitle = document.getElementById('input-track-title').value;
    let artist = document.getElementById('input-artist').value;
    let artistPopularity = document.getElementById('artist-popularity-score').value;
    let artistGender = document.querySelector('input[name="artist-gender"]:checked').value;
    // Converts the NodeList to an array; map() creates a new array by applaying a function to each element of the array. Here, it extracts .value of each checkbox:
    let artistRegion = Array.from(document.querySelectorAll('input[name="artist-region"]:checked')).map(cb => cb.value);

    fetch('/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({title: trackTitle,
                            artist: artist,
                            popularity: artistPopularity,
                            gender: artistGender,
                            region: artistRegion
                            })
    })
    
    // Takes the HTTP response from the server, reads it & parses it as a JS object.
    .then(response => response.json()) // It returns a Promise that resolves with the parsed JSON.
    .then(data => {
        console.log('Recommended songs:', data);
        let resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        let messageDiv = document.getElementById('message');
        if (data.message) {
            messageDiv.textContent = data.message;
        }

        if (data.result.length > 0) {
            let header = document.createElement('h2');
            header.textContent = 'You may like these tracks:';
            resultsDiv.appendChild(header)
        }

        data.result.forEach(element => {
            const para = document.createElement('p');
            para.innerHTML = `${element.song_name} by ${element.artist}`;
            resultsDiv.appendChild(para);
        });
    })
    .catch(error => console.error('Error: ', error));    
})

console.log('Script loaded!')