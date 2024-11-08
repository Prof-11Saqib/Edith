async function fetchData() {
    try {
        const response = await fetch('http://127.0.0.1:5000/get_data');
        const data = await response.json();
        console.log(data)
        // Populate the containers with the fetched data
        document.getElementById('full_name').textContent = data.full_name;
        // document.getElementById('fname').textContent = data.fname;
        document.getElementById('headshot').src = data.headshot_url;
        // document.getElementById('headshot').textContent = data.headshot_url; 
        document.getElementById('teamname').textContent = data.team_name;
        document.getElementById('nameacro').textContent = data.name_acronym;
        document.getElementById('drivernum').textContent = data.driver_number;
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the fetch function when the page loads
window.onload = fetchData;