function main() {
    $('#getRandomMovie').click(getRandomMovie);
}

function getRandomMovie() {
    $('#movie').html("");
    $('#loader').css('display', 'block');
    const url = '/get/movie';
    $.getJSON(url, function (response) {
        $('#loader').css('display', 'none');
        console.log(response);
        printMovieData(response);
    });
}

function printMovieData(movieData){
    $('#movie').html("");
    movieHtml =
    `
        <img src="http://image.tmdb.org/t/p/w185/${movieData.poster_path}">
        <div id="movie-inner">
            <h2>${movieData.title}</h2>
            <p>${movieData.release_date.substr(0,4)}<span>Score: ${movieData.vote_average}</span></p>
            <p>${movieData.overview}</p>
        </div>    
    
    `;

    $('#movie').html(movieHtml);
}

main();