import { fetchJSON } from './utilities.js';

(async () => {
  const rawData = await fetchJSON('/api/driver_standings');
  const labels = rawData.map(item => item.driver); 
  const points = rawData.map(item => item.points);

  const data = {
    labels,
    datasets: [{
      label: 'Driver Points',
      data: points,
      backgroundColor: labels.map(() => randomColor())
    }]
  };

  const ctx = document.getElementById('driverStandingsChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Driver Standings since the last 5 Seasons'
        }
      },
      scales: {
        y: {
          beginAtZero: true,
          title: { display: true, text: 'Points' }
        },
        x: {
          title: { display: true, text: 'Driver' }
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