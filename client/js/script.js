const apiurl = 'http://127.0.0.1:5000';

const outputElement = document.getElementById('output');
const cassette_Selector = document.getElementById('cassette_Selector');
 
const requestOptions = {
    method: 'GET',
    mode: "no-cors"
};

function show_results() {
    fetch(apiurl, requestOptions)
            // .then(response => {
            //     if (!response.ok) {
            //         throw new Error(`HTTP error! status: ${response.status}`);
            //     }
            //     return response.json();
            // })
            .then(data => {
                console.log(data);
                data.forEach(cassette => {
                    const option = document.getElementById('option');
                    option.value = cassette.id;
                    option.textContent = cassette.name;
                    cassette_Selector.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Error:', error);
                outputElement.textContent = 'An error occurred while fetching data.';
            });
        }
        // function show_results(){
        //     fetch(apiurl, requestOptions)
        //         .then(response => {
        //             console.log(response);
        //             return response.json();
        //         })
        //         .then(data => {
        //             console.log(data);
        //         })
        //         // .catch(error => {
        //         //     console.error('Error:', error);
        //         // });
        //     }