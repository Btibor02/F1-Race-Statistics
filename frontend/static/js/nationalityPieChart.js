import { fetchJSON } from './utilities.js';

const ctx = document.getElementById('nationalityPieChart').getContext('2d');
let chart;

async function loadNationality(season) {
  const rawData = await fetchJSON('/api/2024/drivers');
  const nationalityCounts = {};

  for (const driver of rawData) {
    const nat = driver.nationality;
    nationalityCounts[nat] = (nationalityCounts[nat] || 0) + 1;
  }

  const labels = Object.keys(nationalityCounts);
  const counts = Object.values(nationalityCounts);

  const data = {
    labels,
    datasets: [{
      label: 'Driver Nationalities',
      data: counts,
      backgroundColor: labels.map(() => randomColor())
    }]
  };

  if (chart) {
    chart.destroy();
  }
  chart = new Chart(ctx, {
    type: 'pie',
    data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: `Driver Nationalities Distribution - ${season}` 
        }
      }
    }
  });
};

const seasonSelector = document.getElementById('seasonSelector');
loadNationality(seasonSelector.value);

seasonSelector.addEventListener('change', () => {
  loadNationality(seasonSelector.value);
});

// Utility to generate a random RGB color
function randomColor() {
  const r = Math.floor(Math.random() * 150);
  const g = Math.floor(Math.random() * 150);
  const b = Math.floor(Math.random() * 150);
  return `rgb(${r},${g},${b})`;
}