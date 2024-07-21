// const apiKey = '00e2c23905671b634b1bd83275fbc152'; 
// const PREMIER_LEAGUE_ID = 39; 

// let isListVisible = false;

// async function getTeams() {
//   const response = await fetch('https://api-football-v3.p.rapidapi.com/v3/leagues', {
//     method: 'GET',
//     headers: {
//       'x-rapidapi-host': 'api-football-v3.p.rapidapi.com',
//       'x-rapidapi-key': apiKey
//     }
//   });
//   const data = await response.json();
  
//   const premierLeagueData = data.response.find(league => league.league_id === PREMIER_LEAGUE_ID);
//   const teamNames = premierLeagueData.teams.map(team => team.team_name);
  
//   createListItems(teamNames); 
// }

// function createListItems(names) {
//     const dropdownlist = document.getElementById('dropdown-list');
//     dropdownlist.innerHTML = ''; 
//     names.forEach(name => {
//       const listItem = document.createElement('li');
//       listItem.textContent = name;
//       listItem.addEventListener('click', () => selectName(name));
//       dropdownlist.appendChild(listItem);
//     });
//   }
  
//   function selectName(name) {
//     const selectedItem = dropdownlist.querySelector('.selected');
//     if (selectedItem) {
//       selectedItem.classList.remove('selected');
//     }
//     dropdownlist.querySelector(`li:contains("${name}")`).classList.add('selected');
//   }
  
//   function filterNames(searchTerm) {
//     const names = document.querySelectorAll('.name-list li'); 
//     const filteredNames = Array.from(names).filter(li =>
//       li.textContent.toLowerCase().includes(searchTerm.toLowerCase())
//     );
//     filteredNames.forEach(item => item.classList.remove('hidden')); 
//     names.forEach(item => !filteredNames.includes(item) && item.classList.add('hidden')); 
//   }
  
//   const searchBar = document.getElementById('search-bar');
//   searchBar.addEventListener('click', () => {
//     if (!isListVisible) {
//       getTeams(); // Fetch teams only on first click
//       isListVisible = true;
//     }
//     searchBar.classList.add('active'); // Add an active class for styling (optional)
//   });
  
//   document.addEventListener('click', (event) => {
//     if (!searchBar.contains(event.target) && isListVisible) {
//       isListVisible = false;
//       searchBar.classList.remove('active'); // Remove active class for styling (optional)
//       // Optionally, hide the list visually:
//       // dropdownlist.style.display = 'none'; // Adjust CSS if needed
//     }
//   });
  
//   searchBar.addEventListener('keyup', (event) => filterNames(event.target.value));