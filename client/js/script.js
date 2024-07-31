const apiurl = 'http://127.0.0.1:5000';

const outputElement = document.getElementById('output');
const cassette_Selector = document.getElementById('cassette_Selector');

const requestOptions = {
    method: 'GET',
    mode: "no-cors"
};
function show_results(){
    fetch(apiurl, requestOptions)
        .then(response => {
            console.log(response);
            return response.json();
        })
        .then(data => {
            console.log(data);
        })
        // .catch(error => {
        //     console.error('Error:', error);
        // });
    }