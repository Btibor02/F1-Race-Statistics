import { fetchJSON } from './utilities.js';

(async () => {
  const rawData = await fetchJSON('/api/drivers');
  const labels = rawData.map(item => item.nationality);
  const counts = rawData.map(item => item.count);

  const data = {
    labels,
    datasets: [{
      label: 'Driver Nationalities',
      data: counts,
      backgroundColor: labels.map(() => randomColor())
    }]
  };

  const ctx = document.getElementById('nationalityPieChart').getContext('2d');
  new Chart(ctx, {
    type: 'pie',
    data,
    options: {
      responsive: true,
      plugins: {
        title: {
          display: true,
          text: 'Driver Nationalities Distribution'
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