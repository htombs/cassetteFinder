const apiurl = 'http://127.0.0.1:5000';

const outputElement = document.getElementById('option');
const cassette_Selector = document.getElementById('cassette_Selector');
 
const requestOptions = {
    method: 'GET',
    mode: "no-cors"
};

function show_results() {
    fetch(apiurl, requestOptions)
    // this section was throwing an error, so I've commented it out to fix other issues
            // .then(response => {
            //     if (!response.ok) {
            //         throw new Error(`HTTP error! status: ${response.status}`);
            //     }
            //     return response.json();
            // })
            .then(data => {
                console.log(data);
                data.forEach(cassette => {
                    const option = document.getElementById('ratio_dropdown');
                    option.value = cassette.id;
                    option.textContent = cassette.name;
                    cassette_Selector.appendChild('option');
                });
            })
            .catch(error => {
                console.error('Error:', error);
                outputElement.textContent = 'An error occurred while fetching data.';
            });
        }

        // this is the old function that didn't work, so trying a new way to call show the data
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