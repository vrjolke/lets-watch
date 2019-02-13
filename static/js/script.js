function main() {
    $('#getRandomMovie').click(getRandomMovie);
}

function getRandomMovie() {
    const url = '/get/movie';
    $.getJSON(url, function (response) {
        console.log(response);
    });
}

function printMovieData(movieData){
    movieHtml =
    `
            
    
    `;

    $('movie').html(movieHtml);
}

main();