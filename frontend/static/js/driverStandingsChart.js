import { fetchJSON } from './utilities.js';

const ctx = document.getElementById('driverStandingsChart').getContext('2d');
let chart;

async function loadDriverData(season) {
  const rawData = await fetchJSON(`/api/standings/${season}`);
  const labels = rawData.map(item => item.Driver.code); 
  const points = rawData.map(item => item.points);

  const data = {
    labels,
    datasets: [{
      label: 'Driver Points',
      data: points,
      backgroundColor: labels.map(() => randomColor())
    }]
  };

  if (chart) {
    chart.destroy();
  }
  chart = new Chart(ctx, {
    type: 'bar',
    data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: `Driver Standings  - ${season}`
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
};

const seasonSelector = document.getElementById('seasonSelector');
loadDriverData(seasonSelector.value);

seasonSelector.addEventListener('change', () => {
  loadDriverData(seasonSelector.value);
});

// Utility to generate a random RGB color
function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return `rgb(${r},${g},${b})`;
}