function main() {
    $('#getRandomMovie').click(getRandomMovie);
    movieOrShow();
    changeGenreList();
}

function changeGenreList() {
    $('#show-cb').click(function () {
        $('#movie-genres-select').css('display', 'none');
        $('#shows-genres-select').css('display', 'block');
    })
    $('#movie-cb').click(function () {
        $('#movie-genres-select').css('display', 'block');
        $('#shows-genres-select').css('display', 'none');
    })
}


function getSelectedGenre() {

}

//movie or tv show
function getSelectedType() {
    if ($("#movie-cb").prop("checked")) {
        return "movie";
    } else {
        return "tv";
    }
}


function getRandomMovie() {
    let url = "";
    if (getSelectedType() == "movie") {
        url = '/get/movie';
    } else {
        url = 'get/tv';
    }

    $('#movie').html("");
    $('#loader').css('display', 'block');
    $.ajax({
        type: "POST",
        url: url,
        success: function (response) {
            $('#loader').css('display', 'none');
            console.log(response);
            printMovieData(response);
        }
    });
}

function printMovieData(movieData) {
    $('#movie').html("");
    movieHtml =
        `
        <img src="http://image.tmdb.org/t/p/w185/${movieData.poster_path}">
        <div id="movie-inner">
            <h2>${movieData.title}</h2>
            <p>${movieData.release_date.substr(0, 4)}<span>Score: ${movieData.vote_average}</span></p>
            <p>${shortenDescription(movieData.overview)}</p>
        </div>    
    `;

    $('#movie').html(movieHtml);
}


function shortenDescription(description){
    if(description.length > 290){
        description = description.substr(0,260).substr(0,description.lastIndexOf(" ")+2);
        description += "[...]";
    }
    return description;
}

function movieOrShow() {
    $('input.type-checkbox').on('change', function () {
        $('input.type-checkbox').not(this).prop('checked', false);
    });
}

main();