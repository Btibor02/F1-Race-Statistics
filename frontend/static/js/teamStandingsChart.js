import { fetchJSON } from './utilities.js';

(async () => {
  const rawData = await fetchJSON('/api/2024/constructorStandings/');
  const labels = rawData.map(item => item.Constructor.name);
  const points = rawData.map(item => item.points);

  console.log(rawData)

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
  return `rgb(${r},${g},${b})`;
}