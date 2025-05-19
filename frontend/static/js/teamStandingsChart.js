import { fetchJSON } from './utilities.js';

const ctx = document.getElementById('teamStandingsChart').getContext('2d');
let chart;

async function loadTeamData(season) {
  const rawData = await fetchJSON(`/api/${season}/constructorStandings/`);
  const labels = rawData.map(item => item.Constructor.name);
  const points = rawData.map(item => item.points);

  const data = {
    labels,
    datasets: [{
      label: 'Team Points',
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
          text: `Team Standings - ${season}`
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
};

const seasonSelector = document.getElementById('seasonSelector');
loadTeamData(seasonSelector.value);

seasonSelector.addEventListener('change', () => {
  loadTeamData(seasonSelector.value);
});

// Utility to generate a random RGB color
function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return `rgb(${r},${g},${b})`;
}