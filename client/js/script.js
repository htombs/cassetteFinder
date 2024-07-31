const apiurl = 'http://127.0.0.1:5000';
const outputElement = document.getElementById('output');

function show_results(){
    fetch(apiurl)
        .then(response => {
            if (!response.ok) {
                if (response.status === 404) {
                    throw new Error('Data not found');
                }   else if (response.status === 500) {
                    throw new Error('Server error');
                }   else {
                    throw new Error('Network response was not ok');
                }
            }
            return response.json();
        })
        .then(data=> {
            outputElement.textContent = JSON.stringify(data, null, 2);
        })
        .catch(error => {
            console.eroor('Error:', error);
        });
}
