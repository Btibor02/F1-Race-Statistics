import { fetchJSON } from './utilities.js';

(async () => {
  const rawData = await fetchJSON('/api/team_standings');
  const labels = rawData.map(item => item.team_id);
  const points = rawData.map(item => item.points);

  const data = {
    labels,
    datasets: [{
      label: 'Team Points',
      data: points,
      backgroundColor: labels.map(() => randomColor())
    }]
  };
  const ctx = document.getElementById('teamStandingsChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Team Standings since the last five seasons'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Points' }
        },
        x: {
          title: { display: true, text: 'Team' }
        }
      }
    }
  });
})();

// Utility to generate a random RGB color
function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return String( "rgb(${r},${g},${b})");
}