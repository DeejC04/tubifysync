window.onload = function getVariableFromFlask() {
    fetch('/get_spotify_key')
        .then(response => response.json())
        .then(data => {
            var spotify_key = data.spotify_key;
            console.log("spotify key ", spotify_key);
        });
}

